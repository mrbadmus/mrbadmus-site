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
    # ── MRB-335 top-up ───────────────────────────────────────────────────
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "b11-02-e05",
        "band": "easier",
        "text": "What does it mean to say that a characteristic is inherited?",
        "options": [
            {"text": "It appeared in a parent during its life and was then "
                     "handed on to its offspring.",
             "correct": False,
             "why": "This is the mistaken idea natural selection replaced. "
                    "What a parent does or acquires during its life never "
                    "reaches the DNA in its gametes."},
            {"text": "It is a habit an animal picks up by watching its "
                     "parents.",
             "correct": False,
             "why": "Copying a parent is learning, not inheritance. Inherited "
                    "characteristics arrive through genes, before an animal "
                    "has watched anything."},
            {"text": "It was passed from parents to offspring through their "
                     "genes.",
             "correct": True},
            {"text": "It is a feature the surroundings give an organism as it "
                     "grows.",
             "correct": False,
             "why": "The surroundings decide which organisms survive; they do "
                    "not paint characteristics on. Colour, size and shape come "
                    "from the genes an organism was born with."},
        ],
        "figure": None,
    },
    {
        "id": "b11-02-e06",
        "band": "easier",
        "text": "What is meant by one generation of a population?",
        "options": [
            {"text": "One round of a population being born, surviving and "
                     "reproducing.",
             "correct": True},
            {"text": "One calendar year in the life of a population.",
             "correct": False,
             "why": "A generation is not a fixed length of time. Bacteria "
                    "manage one in twenty minutes and an elephant takes more "
                    "than a decade."},
            {"text": "The whole length of time a species goes on existing "
                     "before it changes into another one.",
             "correct": False,
             "why": "That is far longer than a generation. Almost nothing "
                    "changes in one generation, and a great deal changes "
                    "across fifty."},
            {"text": "The set of offspring produced by one pair of parents in "
                     "a single season.",
             "correct": False,
             "why": "A generation covers the whole population, not one family. "
                    "It is the round of births, deaths and breeding the "
                    "population goes through together."},
        ],
        "figure": None,
    },
    {
        "id": "b11-02-e07",
        "band": "easier",
        "text": "Peppered moths rest on tree trunks and are hunted by birds "
                "that eat whatever they can see. On clean bark mottled with "
                "pale lichen, which moths survive better, and why?",
        "options": [
            {"text": "The dark ones, because dark colours are harder to see at "
                     "a distance.",
             "correct": False,
             "why": "Against pale mottled lichen a dark moth is the most "
                    "obvious thing on the trunk. What decides it is the match "
                    "with the background, not the shade itself."},
            {"text": "The pale ones, because they are hard to see against pale "
                     "mottled lichen.",
             "correct": True},
            {"text": "Neither, because a bird finds a resting moth by smell "
                     "rather than by sight.",
             "correct": False,
             "why": "These birds hunt by sight, which is why colour matters at "
                    "all. A moth that matches the bark is one the bird does "
                    "not spot."},
            {"text": "The pale ones, because lichen is a food they can eat and "
                     "the dark ones cannot.",
             "correct": False,
             "why": "Neither moth eats the lichen. The lichen matters because "
                    "of what it looks like, not because of what it offers."},
        ],
        "figure": None,
    },
    {
        "id": "b11-02-e08",
        "band": "easier",
        "text": "What does the term natural selection describe?",
        "options": [
            {"text": "Individuals changing to suit their surroundings and "
                     "then passing that change on to the offspring they have "
                     "later.",
             "correct": False,
             "why": "No individual changes. That is the older explanation this "
                    "one replaced, and it fails because nothing an organism "
                    "does in its life reaches its gametes."},
            {"text": "Nature choosing which individuals should survive and "
                     "which should not.",
             "correct": False,
             "why": "Nothing is choosing. The word selection is the trap here: "
                    "a bird eats what it can see, and no part of the process "
                    "is aiming at a result."},
            {"text": "The strongest members of a population physically "
                     "defeating the weaker ones in direct contests.",
             "correct": False,
             "why": "Strength is one variation among many. It is regularly the "
                    "small, the drab and the unimpressive that come through."},
            {"text": "Variations that suit the conditions becoming commoner, "
                     "as their carriers survive to breed.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b11-02-e09",
        "band": "easier",
        "text": "In nineteenth-century industrial Britain the trunks of many "
                "trees became blackened. What caused that?",
        "options": [
            {"text": "Dark moths resting on the trunks in very large numbers.",
             "correct": False,
             "why": "The moths did not colour the trees; the trees changed "
                    "first. Soot killed the lichen and darkened the bark, and "
                    "the moth population followed."},
            {"text": "Soot from coal-burning factories, which killed the "
                     "lichen and darkened the bark.",
             "correct": True},
            {"text": "The trees producing a darker bark in response to the "
                     "polluted air.",
             "correct": False,
             "why": "A tree does not repaint itself to match its surroundings "
                    "any more than a moth does. The soot settled on the bark "
                    "and killed the pale lichen growing there."},
            {"text": "Warmer, wetter weather that encouraged a dark fungus to "
                     "grow on the trunks.",
             "correct": False,
             "why": "The cause was industrial rather than seasonal. Coal smoke "
                    "put soot on the trunks and killed the lichen that had "
                    "made them pale."},
        ],
        "figure": None,
    },
    {
        "id": "b11-02-e10",
        "band": "easier",
        "text": "In a population where one form survives a little better than "
                "another, how much does the population change in a single "
                "generation?",
        "options": [
            {"text": "It changes completely, because only the better-suited "
                     "form survives long enough to breed.",
             "correct": False,
             "why": "Both forms go on surviving; one simply does so at a "
                    "higher rate. A form that survives 45 times in 100 is not "
                    "being wiped out."},
            {"text": "It does not change at all until a whole species has "
                     "been replaced by another.",
             "correct": False,
             "why": "It changes a little every generation. What is true is "
                    "that the change in any one of them is too small to "
                    "notice."},
            {"text": "Very little — the change is small and only shows over "
                     "many generations.",
             "correct": True},
            {"text": "It changes fastest in the first generation and then "
                     "slows down.",
             "correct": False,
             "why": "There is nothing special about the first generation. The "
                    "same small change happens each time, and it is the "
                    "accumulation that shows."},
        ],
        "figure": None,
    },
    {
        "id": "b11-02-e11",
        "band": "easier",
        "text": "A mouse loses its tail in an accident and later has a litter "
                "of young. What will the young be like?",
        "options": [
            {"text": "Ordinary mice with tails, because an injury does not "
                     "change the genes a parent passes on.",
             "correct": True},
            {"text": "Tailless, because characteristics an animal acquires are "
                     "passed to its offspring.",
             "correct": False,
             "why": "This is the idea the whole of natural selection exists to "
                    "correct. Losing a tail does not rewrite the DNA in the "
                    "mouse's gametes, so there is nothing about it to pass "
                    "on."},
            {"text": "Tailless, but only if the mouse lost its tail before the "
                     "young were conceived.",
             "correct": False,
             "why": "The timing makes no difference. Damage to a parent's body "
                    "never reaches the genetic information in its gametes, "
                    "whenever it happens."},
            {"text": "Mice with unusually short tails, because the change is "
                     "passed on in part.",
             "correct": False,
             "why": "It is not passed on at all, in part or otherwise. "
                    "Acquired damage and inherited characteristics travel by "
                    "completely different routes, and only one of them reaches "
                    "the next generation."},
        ],
        "figure": None,
    },
    {
        "id": "b11-02-e12",
        "band": "easier",
        "text": "Lamarck's explanation of how species change was later shown "
                "to be wrong about the mechanism. What was he right about?",
        "options": [
            {"text": "That using a body part a great deal makes it larger in "
                     "an animal's offspring.",
             "correct": False,
             "why": "That is precisely the mechanism that fails. A "
                    "blacksmith's children are not born with thick arms."},
            {"text": "That the variation a population needs appears when the "
                     "conditions demand it.",
             "correct": False,
             "why": "Nothing appears on demand. The variation has to be there "
                    "beforehand, or there is nothing for the process to work "
                    "on."},
            {"text": "That species change over time, at a period when most "
                     "people thought they did not.",
             "correct": True},
            {"text": "That the surroundings decide which individuals survive "
                     "better than others.",
             "correct": False,
             "why": "That part belongs to the explanation that replaced his. "
                    "Lamarck's idea was that the surroundings change the "
                    "individual, not that they decide which ones survive."},
        ],
        "figure": None,
    },
    {
        "id": "b11-02-e13",
        "band": "easier",
        "text": "Birds eat whichever moths they happen to spot on a trunk. In "
                "that description, what are the birds doing to the moth "
                "population?",
        "options": [
            {"text": "Choosing which colour of moth the population ought to "
                     "become.",
             "correct": False,
             "why": "Nothing is choosing. A bird is not deciding anything "
                    "about the population's future — it eats what it can see, "
                    "and the proportions follow from that."},
            {"text": "Changing the moths they do not eat, so that those moths "
                     "suit the bark better.",
             "correct": False,
             "why": "The survivors are unchanged. They were already the colour "
                    "that suited the bark, which is why the bird failed to "
                    "spot them."},
            {"text": "Giving the population the variation it needs in order to "
                     "survive.",
             "correct": False,
             "why": "They give it nothing. The variation was already there "
                    "before the birds or the bark mattered at all."},
            {"text": "Simply killing a higher proportion of one kind than of "
                     "the other.",
             "correct": True},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "b11-02-s05",
        "band": "standard",
        "text": "In the accepted explanation of how giraffes came to have long "
                "necks, what is the one thing that moves from one generation "
                "to the next?",
        "options": [
            {"text": "The neck length of each individual giraffe, a little at "
                     "a time.",
             "correct": False,
             "why": "No giraffe's neck grows to suit the trees. An animal has "
                    "the neck it grew to adulthood with, and it keeps it."},
            {"text": "The average neck length of the population, because of "
                     "which animals had calves.",
             "correct": True},
            {"text": "The amount of stretching giraffes do, which increases as "
                     "the low leaves run out.",
             "correct": False,
             "why": "Stretching may well increase, and it changes nothing that "
                    "can be inherited. What an animal does in its life does "
                    "not alter the genes in its gametes."},
            {"text": "The species' need for a longer neck, which grows "
                     "stronger with each generation.",
             "correct": False,
             "why": "A need is not a mechanism. Nothing in this process is "
                    "aiming at anything, and a population with no useful "
                    "variation simply dies out."},
        ],
        "figure": None,
    },
    {
        "id": "b11-02-s06",
        "band": "standard",
        "text": "On soot-blackened bark, birds spot and eat a much higher "
                "proportion of pale moths than of dark ones. What happens next "
                "in that population?",
        "options": [
            {"text": "The surviving pale moths darken, so that they are not "
                     "spotted the following year.",
             "correct": False,
             "why": "A moth is the colour it hatched. Nothing about a survivor "
                    "changes, and it could not pass a change on if it did."},
            {"text": "The birds turn to the dark moths once the pale ones "
                     "become scarce.",
             "correct": False,
             "why": "The birds are still eating what they can see, and on "
                    "sooty bark that is still mostly the pale ones. Nothing "
                    "makes them switch."},
            {"text": "More dark moths survive to breed, so a larger share of "
                     "the next generation is dark.",
             "correct": True},
            {"text": "The population shrinks each year until there are no "
                     "moths left on that tree.",
             "correct": False,
             "why": "The dark moths breed perfectly well. What changes is the "
                    "mixture of the population, not whether there is one."},
        ],
        "figure": None,
    },
    {
        "id": "b11-02-s07",
        "band": "standard",
        "text": "A population of moths on sooty bark ends up almost entirely "
                "dark. It is then replaced with a fresh population, half pale "
                "and half dark, on the same sooty bark. What happens to the "
                "new population?",
        "options": [
            {"text": "It goes dark again, because the survival difference on "
                     "sooty bark has not changed.",
             "correct": True},
            {"text": "It stays at half and half, because the change has "
                     "already happened once.",
             "correct": False,
             "why": "Nothing carries over from the first population. Each "
                    "generation is decided by which moths survive on the bark "
                    "that is there now."},
            {"text": "It goes dark faster than the first population did, "
                     "because the process has been through it before.",
             "correct": False,
             "why": "This process has no memory. The new population starts "
                    "from its own mixture and changes at the rate its own "
                    "survival difference produces."},
            {"text": "It goes pale, because the dark form has already had its "
                     "turn.",
             "correct": False,
             "why": "Nothing takes turns. On sooty bark the pale moths are the "
                    "ones a bird can see, whatever happened to an earlier "
                    "population."},
        ],
        "figure": None,
    },
    {
        "id": "b11-02-s08",
        "band": "standard",
        "text": "Someone says the moths of industrial Britain turned dark "
                "because of the pollution. In what sense is that wrong?",
        "options": [
            {"text": "It is not wrong at all — soot is what darkened them.",
             "correct": False,
             "why": "Soot darkened the trunks, not the moths. A moth resting "
                    "on a blackened trunk is not blackened by it, and washing "
                    "one would prove it."},
            {"text": "It is wrong because the pollution had nothing to do with "
                     "the change.",
             "correct": False,
             "why": "It had everything to do with it. The soot changed which "
                    "moths a bird could see, and that changed which ones "
                    "survived to breed."},
            {"text": "It is wrong because dark moths did not exist until the "
                     "factories were built.",
             "correct": False,
             "why": "They did exist, and had done for a very long time — they "
                    "were simply rare. That is what made the change possible "
                    "at all."},
            {"text": "No moth turned dark: the pollution changed which moths "
                     "were eaten, not what any moth was like.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b11-02-s09",
        "band": "standard",
        "text": "A scientist releases equal numbers of marked pale and dark "
                "peppered moths into a soot-polluted wood and into a clean, "
                "lichen-rich wood, then recaptures as many as he can from "
                "each. What should he expect to recapture?",
        "options": [
            {"text": "More pale moths than dark ones in both woods, since pale "
                     "is the commoner form.",
             "correct": False,
             "why": "How common a form is where it started does not decide who "
                    "survives in each wood. What matters is which moth a bird "
                    "can see against that wood's bark."},
            {"text": "More dark moths from the polluted wood, and more pale "
                     "ones from the clean wood.",
             "correct": True},
            {"text": "Equal numbers of both forms from both woods, since he "
                     "released equal numbers.",
             "correct": False,
             "why": "He released equal numbers, and the woods then did "
                    "something to them. Releasing into two different woods is "
                    "how the difference the bark makes is measured."},
            {"text": "More pale moths from the polluted wood, because dark "
                     "moths are eaten wherever they are.",
             "correct": False,
             "why": "On soot-blackened bark it is the pale moth that stands "
                    "out. The advantage swaps when the background does."},
        ],
        "figure": None,
    },
    {
        "id": "b11-02-s10",
        "band": "standard",
        "text": "A student writes: after the trunks were blackened, the dark "
                "moths were better adapted. What needs adding to that "
                "sentence?",
        "options": [
            {"text": "Nothing at all — better adapted is a complete "
                     "description all by itself.",
             "correct": False,
             "why": "Adapted is always adapted to something. Move the same "
                    "dark moth to a clean lichen trunk and it is the one the "
                    "birds find first."},
            {"text": "That the dark moths gradually became better adapted "
                     "once the bark around them darkened.",
             "correct": False,
             "why": "They did not become anything. They were already dark, and "
                    "the bark darkening is what turned that colour into an "
                    "advantage."},
            {"text": "What they were better adapted to — bark blackened by "
                     "soot.",
             "correct": True},
            {"text": "That the pale moths were badly adapted from the start.",
             "correct": False,
             "why": "They were superbly adapted to the trunks as those trunks "
                    "had been for centuries. What changed was the trunks."},
        ],
        "figure": None,
    },
    {
        "id": "b11-02-s11",
        "band": "standard",
        "text": "Suppose moth colour were decided by something in a "
                "caterpillar's food rather than by its genes, with birds still "
                "eating the moths they can see. Would a population on sooty "
                "bark still become mostly dark over many generations?",
        "options": [
            {"text": "Yes, because the birds would still be eating the pale "
                     "ones.",
             "correct": False,
             "why": "They would, and it would get the population nowhere. The "
                    "survivors' colour would not reach their offspring, so "
                    "each generation would start from the same mixture."},
            {"text": "Yes, because the survivors would still be the dark ones "
                     "each year.",
             "correct": False,
             "why": "Surviving is only half of it. The advantage has to be "
                    "passed on, or the next generation is no darker than the "
                    "last."},
            {"text": "No, because with no genes involved there would be no "
                     "variation to begin with.",
             "correct": False,
             "why": "There would still be variation — some dark moths and some "
                    "pale ones. What would be missing is the route from a "
                    "survivor to its offspring."},
            {"text": "No, because the survivors' colour would not be passed to "
                     "their offspring.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b11-02-s12",
        "band": "standard",
        "text": "Three of these are things natural selection needs if it is to "
                "change a population. Which one is not needed?",
        "options": [
            {"text": "A direction the population is working towards.",
             "correct": True},
            {"text": "Variation that is already present in the population.",
             "correct": False,
             "why": "You have marked the requirement that has to come first. "
                    "If individuals do not already differ, a difference in "
                    "survival has nothing to act on."},
            {"text": "More offspring produced than the food and space can "
                     "support.",
             "correct": False,
             "why": "This one is needed too. If every offspring survived there "
                    "would be no difference in who breeds, and nothing would "
                    "change."},
            {"text": "Inheritance, so that the survivors' characteristics "
                     "reach their offspring.",
             "correct": False,
             "why": "This one is needed as well. Without it a survivor's "
                    "advantage dies with it, and each generation begins where "
                    "the last one did."},
        ],
        "figure": None,
    },
    {
        "id": "b11-02-s13",
        "band": "standard",
        "text": "A scientist counts the pale and dark moths in a wood in two "
                "successive years and finds almost no difference. She "
                "concludes that natural selection is not happening there. Is "
                "she right?",
        "options": [
            {"text": "Yes — if nothing has changed across a whole year, then "
                     "nothing is happening at all.",
             "correct": False,
             "why": "Almost nothing changes in a single generation even when "
                    "selection is strong. A difference of a few moths in a "
                    "hundred is exactly what one year of it looks like."},
            {"text": "Not necessarily — one generation's change is very small, "
                     "and it shows only across many.",
             "correct": True},
            {"text": "No, because the change always appears suddenly in one "
                     "particular year.",
             "correct": False,
             "why": "There is no sudden year. The change is small and steady, "
                    "which is why a two-year comparison can miss it "
                    "entirely."},
            {"text": "Yes, because a population only changes when its "
                     "surroundings change again.",
             "correct": False,
             "why": "The surroundings can sit still while the population goes "
                    "on shifting. As long as one form survives better, the "
                    "proportions keep moving."},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "b11-02-h05",
        "band": "harder",
        "text": "On clean lichen bark, 85 out of every 100 pale moths survive "
                "each generation and 45 out of every 100 dark ones do. A wood "
                "holds 400 pale moths and 400 dark ones. How many more pale "
                "moths than dark moths survive that generation?",
        "options": [
            {"text": "40 moths",
             "correct": False,
             "why": "That is the gap between the two percentages, and a "
                    "percentage is not a number of moths. Each rate has to be "
                    "applied to the 400 animals first."},
            {"text": "340 moths",
             "correct": False,
             "why": "That is how many pale moths survive. The question asks "
                    "how many more than the dark ones, so the 180 dark "
                    "survivors have still to be taken off."},
            {"text": "160 moths",
             "correct": True},
            {"text": "520 moths",
             "correct": False,
             "why": "That is the two groups of survivors added together. A "
                    "difference is found by subtracting one from the other."},
        ],
        "figure": None,
    },
    {
        "id": "b11-02-h06",
        "band": "harder",
        "text": "A fishery uses nets with a mesh that lets small fish through "
                "and catches large ones. After thirty years the fish of that "
                "species caught there are, on average, noticeably smaller and "
                "breed at a younger age. Which explanation is correct?",
        "options": [
            {"text": "The fish learned to stay small so that they could pass "
                     "through the mesh.",
             "correct": False,
             "why": "A fish cannot decide what size to be, and nothing it "
                    "learned would reach its offspring. What changed is which "
                    "fish lived long enough to breed."},
            {"text": "Fish that were already smaller, or that already bred "
                     "earlier, escaped the nets and left more offspring.",
             "correct": True},
            {"text": "Being caught in nets stunted the fish, and their young "
                     "hatched smaller as a result.",
             "correct": False,
             "why": "Damage to a parent's body does not reach its gametes. A "
                    "fish that survived a net passes on nothing that the net "
                    "did to it."},
            {"text": "The species developed a smaller body in order to survive "
                     "the fishery.",
             "correct": False,
             "why": "Developed and in order to are the two phrases to watch "
                    "for. Together they give the fish an aim, and nothing in "
                    "this process aims at anything."},
        ],
        "figure": None,
    },
    {
        "id": "b11-02-h07",
        "band": "harder",
        "text": "Every moth in one wood is dark, and the trunks are black with "
                "soot. Birds hunt them as usual. Will that population go on "
                "changing?",
        "options": [
            {"text": "Yes, the moths will go on getting darker with each "
                     "generation.",
             "correct": False,
             "why": "There is nothing left to select between. Every moth is "
                    "already dark, and darker is not a direction the "
                    "population can be pushed in."},
            {"text": "Yes, because natural selection acts on a population all "
                     "the time.",
             "correct": False,
             "why": "It can only act where individuals differ. A population in "
                    "which every individual is the same has nothing for a "
                    "difference in survival to work on."},
            {"text": "No — with no variation in colour left, there is nothing "
                     "for a difference in survival to act on.",
             "correct": True},
            {"text": "No, because natural selection stops once a population is "
                     "well suited to its conditions and has nothing "
                     "left to improve.",
             "correct": False,
             "why": "Nothing switches off when a population is well suited. "
                    "What has stopped it here is the absence of variation, and "
                    "a change in the bark would leave the population with none "
                    "to draw on."},
        ],
        "figure": None,
    },
    {
        "id": "b11-02-h08",
        "band": "harder",
        "text": "Two sentences describe the same change. One reads: the moths "
                "became dark so that they could hide on the sooty trunks. The "
                "other reads: dark moths were harder to see on sooty trunks, "
                "so more of them survived to breed. Why do biologists insist "
                "on the second?",
        "options": [
            {"text": "The first gives the moths a purpose, and nothing in the "
                     "process is aiming at a result.",
             "correct": True},
            {"text": "The first is wrong about which moths were hidden, and "
                     "the second corrects it.",
             "correct": False,
             "why": "Both sentences have the right moths hidden on the right "
                    "bark. The problem is the words so that they could, not "
                    "the biology of who was seen."},
            {"text": "The two sentences say the same thing, and biologists "
                     "prefer the longer one.",
             "correct": False,
             "why": "They do not say the same thing. One describes a "
                    "population being filtered; the other describes moths "
                    "acting with an aim in view."},
            {"text": "The first leaves out the birds, which are what does the "
                     "killing.",
             "correct": False,
             "why": "The birds can be added to it and the sentence is still "
                    "wrong. So that they could would still hand the moths a "
                    "goal they cannot have."},
        ],
        "figure": None,
    },
    {
        "id": "b11-02-h09",
        "band": "harder",
        "text": "In a bed of wild poppies a few plants flower about three "
                "weeks earlier than the rest. A gardener mows the bed every "
                "year in mid-June, before most of the poppies have set seed. "
                "What should he expect after many years?",
        "options": [
            {"text": "The poppies will learn to flower before the mowing, and "
                     "all of them will change.",
             "correct": False,
             "why": "A plant cannot learn or decide when to flower. What "
                    "decides the bed's future is which plants managed to set "
                    "seed before the blade came through."},
            {"text": "Most of the poppies in the bed will flower early, "
                     "because only the early ones set seed.",
             "correct": True},
            {"text": "The mowing will damage the plants, so that their seeds "
                     "produce early-flowering poppies.",
             "correct": False,
             "why": "Damage to a plant does not change the genetic "
                    "information in its seeds. The mowing decides which plants "
                    "get to make seeds at all."},
            {"text": "Nothing will change, because mowing affects every poppy "
                     "in the bed equally.",
             "correct": False,
             "why": "It does not affect them equally, and that is the whole "
                    "point. Plants that have already set seed by mid-June lose "
                    "nothing; the rest lose everything."},
        ],
        "figure": None,
    },
    {
        "id": "b11-02-h10",
        "band": "harder",
        "text": "After clean-air laws reduced the soot, British woodland "
                "trunks slowly grew pale again and the proportion of dark "
                "peppered moths fell. Someone says this proves moths can "
                "change back, so they must be able to change to suit their "
                "surroundings. What is the correct reply?",
        "options": [
            {"text": "The moths did change back, but only over a very long "
                     "time.",
             "correct": False,
             "why": "No moth changed at any point, in either direction. What "
                    "went back was the proportion of each form, decided by "
                    "which moths the birds could see."},
            {"text": "The fall proves nothing, because the trunks did not "
                     "really become pale again.",
             "correct": False,
             "why": "They did, as the lichen returned. The observation is "
                    "sound; it is the conclusion drawn from it that is wrong."},
            {"text": "The dark moths were bleached by the cleaner air, which "
                     "is why they became rarer.",
             "correct": False,
             "why": "Air does not repaint a moth. Dark moths became rarer "
                    "because more of them were spotted and eaten once the bark "
                    "was pale again."},
            {"text": "The proportions moved back, and no individual moth "
                     "changed in either direction.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b11-02-h11",
        "band": "harder",
        "text": "Two species live in the same wood and face the same new "
                "predator. One breeds twice a year and its populations run to "
                "millions; the other breeds once every three years and numbers "
                "a few hundred. Which is more likely to end up with a "
                "population that avoids the predator well?",
        "options": [
            {"text": "The second, because a small population changes faster "
                     "than a large one does.",
             "correct": False,
             "why": "A small population has less variation to draw on, not "
                    "more. Fewer individuals means fewer versions of genes "
                    "present at all."},
            {"text": "Neither — how fast a species breeds has nothing to do "
                     "with it.",
             "correct": False,
             "why": "It has a great deal to do with it. The change happens "
                    "between generations, so a species producing six "
                    "generations in three years gets six chances where the "
                    "other gets one."},
            {"text": "The first, because it has more variation and far more "
                     "generations.",
             "correct": True},
            {"text": "The first, because a large population is stronger and "
                     "can simply drive the predator away.",
             "correct": False,
             "why": "Numbers do not drive a predator off. What numbers and "
                    "quick breeding give is more variation and more "
                    "generations for a difference in survival to accumulate "
                    "through."},
        ],
        "figure": None,
    },
    {
        "id": "b11-02-h12",
        "band": "harder",
        "text": "A computer model of the moths holds the population size "
                "constant, uses fixed survival percentages, and allows no new "
                "mutations and no moths arriving from elsewhere. Does that "
                "make its conclusion unreliable?",
        "options": [
            {"text": "Yes — with no mutation there is no source of new "
                     "variation, so nothing could ever change.",
             "correct": False,
             "why": "The variation is already in the population at the start, "
                    "which is all the process needs. Mutation is where "
                    "variation comes from originally, not something required "
                    "in every run."},
            {"text": "Yes, because a real population never stays the same "
                     "size, and changing numbers are what drive the change.",
             "correct": False,
             "why": "Changing numbers are not what drive it. What drives it is "
                    "a difference in the proportion of each form that survives "
                    "to breed."},
            {"text": "No, because a model that leaves things out is always "
                     "more accurate than the real thing.",
             "correct": False,
             "why": "Leaving things out never adds accuracy. It makes one "
                    "mechanism visible, and the honest description is that "
                    "this is a teaching model with real limits."},
            {"text": "No — it leaves out real influences, and the mechanism it "
                     "does show works as it does in a real wood.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b11-02-h13",
        "band": "harder",
        "text": "Cave-dwelling fish in several parts of the world have no "
                "eyes, while their close relatives in nearby rivers have "
                "normal ones. A student writes that the fish stopped using "
                "their eyes in the dark, so the eyes disappeared and their "
                "young were born without them. Which reply is right?",
        "options": [
            {"text": "Not using an organ cannot remove it from the next "
                     "generation; what changed is which fish left the most "
                     "offspring.",
             "correct": True},
            {"text": "The fish's eyes were damaged by the darkness, and that "
                     "damage was inherited.",
             "correct": False,
             "why": "Darkness does not damage an eye, and damage is not "
                    "inherited in any case. Nothing that happens to a parent's "
                    "body reaches the genes in its gametes."},
            {"text": "The fish needed to save energy, so the species got rid "
                     "of its eyes.",
             "correct": False,
             "why": "Needing something is not a mechanism. Nothing is aiming "
                    "at a saving; fish with smaller eyes were at no "
                    "disadvantage in the dark and left as many offspring as "
                    "the rest."},
            {"text": "The eyes must still be there, since a species cannot "
                     "lose a feature it once had, however long it "
                     "goes unused.",
             "correct": False,
             "why": "Species do lose features. What they do not do is lose "
                    "them by not using them — a feature disappears because "
                    "individuals without it did at least as well."},
        ],
        "figure": None,
    },
    # ── easier · the MRB-338 expansion ──────────────────────────────────
    {
        "id": "b11-02-e14",
        "band": "easier",
        "text": "Soot from factory chimneys blackens the trunks in a wood. "
                "Birds hunt the moths resting on them by sight. Which moths "
                "are taken more often once the trunks are black?",
        "options": [
            {"text": "The dark ones, since a dark insect is easier for a bird "
                     "to pick out than a pale one.",
             "correct": False,
             "why": "It is the other way round on a black trunk. How easily a "
                    "moth is seen depends on the background it is sitting "
                    "against, not on the colour by itself."},
            {"text": "The pale ones, because they show up against bark that "
                     "is now black.",
             "correct": True},
            {"text": "Neither kind, since a hunting bird takes whichever moth "
                     "happens to be closest to its perch.",
             "correct": False,
             "why": "The birds in this account hunt by sight, so the one they "
                    "can see is the one they take. Distance is not what is "
                    "deciding here."},
            {"text": "Both kinds, because soot settles on the moths in the "
                     "wood as well as on the bark.",
             "correct": False,
             "why": "Soot on the bark does not repaint the moths. A moth is "
                    "the colour it hatched, and the trunk changing colour is "
                    "what changes which moth is seen."},
        ],
        "figure": None,
    },
    {
        "id": "b11-02-e15",
        "band": "easier",
        "text": "Conditions in a habitat change. What has to have been "
                "present in the population beforehand if natural selection is "
                "going to change it?",
        "options": [
            {"text": "Differences between the individuals, already there "
                     "before the change.",
             "correct": True},
            {"text": "A large enough population for the species to be "
                     "in no danger of dying out.",
             "correct": False,
             "why": "Numbers help, but a million identical individuals give "
                    "selection nothing to work on. What is needed is "
                    "difference, not quantity."},
            {"text": "A warning of the change, so that the population has "
                     "time to prepare for it.",
             "correct": False,
             "why": "Nothing in a population can prepare for anything. The "
                    "change simply arrives, and whatever differences are "
                    "already present are what it acts on."},
            {"text": "A stretch of time in which the conditions stay exactly "
                     "as they were.",
             "correct": False,
             "why": "Steady conditions change nothing on their own. It is the "
                    "difference between individuals that decides who survives "
                    "when conditions do shift."},
        ],
        "figure": None,
    },
    {
        "id": "b11-02-e16",
        "band": "easier",
        "text": "A blacksmith builds up thick arm muscles over twenty years "
                "of work at the forge. What will his children be born with?",
        "options": [
            {"text": "Thicker arms than average, because their father built "
                     "his up before they were born.",
             "correct": False,
             "why": "Muscle built during a life never reaches the genetic "
                    "information passed to a child. This is the idea the "
                    "lesson is careful to take apart."},
            {"text": "Thicker arms, but only if they take up the same trade "
                     "as he did.",
             "correct": False,
             "why": "Then it would be their own work doing it, not "
                    "inheritance. Nothing has been passed on either way."},
            {"text": "Ordinary arms, because what a parent's body does during "
                     "his life is not inherited.",
             "correct": True},
            {"text": "Weaker arms, since the effort used up strength that was "
                     "meant for his children.",
             "correct": False,
             "why": "Strength is not a store that is shared out between a "
                    "parent and his children. Work at a forge has no effect "
                    "on them in either direction."},
        ],
        "figure": None,
    },
    {
        "id": "b11-02-e17",
        "band": "easier",
        "text": "On partly recovered bark, 70 moths in every 100 survive each "
                "generation whichever colour they are. Predict the "
                "proportions of pale and dark after ten generations.",
        "options": [
            {"text": "Mostly dark, because dark is the stronger colour.",
             "correct": False,
             "why": "Neither colour is stronger. A colour only does well "
                    "where it is harder to see, and on this bark neither is."},
            {"text": "Mostly pale, because pale was the original colour of "
                     "the species before any soot fell.",
             "correct": False,
             "why": "Being the original form gives no advantage. Only a "
                    "difference in who survives moves the proportions, and "
                    "there is none here."},
            {"text": "All one colour, because ten generations is long enough "
                     "for one of them to take over completely.",
             "correct": False,
             "why": "Generations do nothing on their own. Without a survival "
                    "difference to accumulate, a thousand generations would "
                    "leave the population where it started."},
            {"text": "About where they started, with neither colour having "
                     "gained on the other.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b11-02-e18",
        "band": "easier",
        "text": "A cold winter kills a far higher proportion of thin-coated "
                "voles than thick-coated ones. In the language of this "
                "lesson, what is the winter acting as?",
        "options": [
            {"text": "An adaptation of the voles that survive it.",
             "correct": False,
             "why": "An adaptation is a feature of an organism, such as the "
                    "thick coat itself. The weather is not a feature of a "
                    "vole."},
            {"text": "A selection pressure on coat thickness.",
             "correct": True},
            {"text": "A generation of the vole population.",
             "correct": False,
             "why": "A generation is one round of being born, surviving and "
                    "reproducing. A winter is an event acting on the voles, "
                    "not a round of breeding."},
            {"text": "A variation, of the kind coats come in.",
             "correct": False,
             "why": "The coats are the variation. The winter is the thing "
                    "making one version survive better than the other."},
        ],
        "figure": None,
    },
    {
        "id": "b11-02-e19",
        "band": "easier",
        "text": "Give an antibiotic to a large population of bacteria and a "
                "few survive it. Where did the survivors' ability to "
                "withstand the drug come from?",
        "options": [
            {"text": "They had it already, before the drug was ever used on "
                     "anyone.",
             "correct": True},
            {"text": "The drug altered them as it passed through, and the "
                     "altered ones lived.",
             "correct": False,
             "why": "An antibiotic kills bacteria; it does not rewrite the "
                    "ones it fails to kill. The survivors were different "
                    "before it arrived."},
            {"text": "They built it up gradually while the drug was being "
                     "taken, the way a person gets fitter.",
             "correct": False,
             "why": "A bacterium cannot toughen itself against a drug during "
                    "its life. Either it carries the version of the gene that "
                    "lets it survive or it does not."},
            {"text": "They picked it up from the person they were living in.",
             "correct": False,
             "why": "A person's body does not hand bacteria a defence against "
                    "medicine. The difference was in the bacteria themselves "
                    "from the start."},
        ],
        "figure": None,
    },
    {
        "id": "b11-02-e20",
        "band": "easier",
        "text": "A patient asks for an antibiotic to treat a cold, which is "
                "caused by a virus. Why do doctors treat that as a real "
                "problem rather than a harmless request?",
        "options": [
            {"text": "The drug would cure the cold too quickly, so the "
                     "patient's body would not learn to fight it.",
             "correct": False,
             "why": "It would not cure the cold at all. An antibiotic has no "
                    "effect on a virus, which is the first half of the "
                    "problem."},
            {"text": "Antibiotics turn the harmless bacteria already living "
                     "in the body into dangerous ones.",
             "correct": False,
             "why": "A drug does not convert one kind of bacterium into "
                    "another. What it does is remove the ones it can kill and "
                    "leave the rest."},
            {"text": "The cold is unaffected, and the drug still kills the "
                     "bacteria in that person that it can kill, leaving the "
                     "rest to breed.",
             "correct": True},
            {"text": "Taking the drug makes the virus itself resistant to "
                     "antibiotics for the future.",
             "correct": False,
             "why": "A virus was never susceptible to an antibiotic, so there "
                    "is nothing for it to become resistant to. The selection "
                    "falls on bacteria."},
        ],
        "figure": None,
    },
    {
        "id": "b11-02-e21",
        "band": "easier",
        "text": "In a population where some individuals die young and others "
                "live to breed, which individuals pass their versions of the "
                "genes to the next generation?",
        "options": [
            {"text": "All of them, since every individual born is part of the "
                     "population's store of genes.",
             "correct": False,
             "why": "Being born is not enough. An individual that dies before "
                    "breeding passes nothing on, however well it did up to "
                    "that point."},
            {"text": "The ones that survive long enough to reproduce.",
             "correct": True},
            {"text": "The largest and strongest, whether or not they leave "
                     "any offspring behind them.",
             "correct": False,
             "why": "Size and strength pass nothing on by themselves. What "
                    "counts is offspring, and an impressive animal with none "
                    "contributes nothing."},
            {"text": "The ones that live longest from the day of birth.",
             "correct": False,
             "why": "A long life with no offspring passes nothing on. A short "
                    "one with many offspring passes a great deal."},
        ],
        "figure": None,
    },
    {
        "id": "b11-02-e22",
        "band": "easier",
        "text": "Biologists say that natural selection acts on a population. "
                "What does the word population mean here?",
        "options": [
            {"text": "Every living thing sharing one habitat, whatever "
                     "species each of them belongs to.",
             "correct": False,
             "why": "That is a community. A population is one species' worth "
                    "of individuals, which is why they can breed with one "
                    "another."},
            {"text": "The individuals of one species living in one place.",
             "correct": True},
            {"text": "The offspring produced by a single pair of parents in "
                     "one breeding season.",
             "correct": False,
             "why": "That is one family, and it is far too small a group for "
                    "proportions to shift across generations."},
            {"text": "A whole species, everywhere on Earth it is found.",
             "correct": False,
             "why": "A species can hold many populations, and they can be "
                    "changing in different directions at the same time in "
                    "different places."},
        ],
        "figure": None,
    },
    {
        "id": "b11-02-e23",
        "band": "easier",
        "text": "Four things are true of an adult fox. Which of them will its "
                "cubs be born already carrying?",
        "options": [
            {"text": "A scar on its shoulder from a fight last spring.",
             "correct": False,
             "why": "An injury heals in the body that suffered it and goes no "
                    "further. Nothing about it reaches the cubs."},
            {"text": "The route through the town it worked out for itself, "
                     "bin by bin.",
             "correct": False,
             "why": "A cub can follow its parent and learn the same route, "
                    "but it is not born knowing it. Learning is taught or "
                    "worked out again, never inherited."},
            {"text": "The thick winter coat it grew last autumn.",
             "correct": False,
             "why": "Growing a coat is the body responding to the weather. "
                    "What can be inherited is how thick a coat the fox is "
                    "able to grow, not the growing."},
            {"text": "The versions of the genes that set its fur colour.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b11-02-e24",
        "band": "easier",
        "text": "A gardener writes that his roses developed thorns in order "
                "to keep the deer away. Which rewrite of that sentence would "
                "a biologist accept?",
        "options": [
            {"text": "Roses grew thorns because the species needed some "
                     "protection from deer browsing them.",
             "correct": False,
             "why": "Needing something is not a mechanism. A need cannot "
                    "produce a feature in a plant that does not already have "
                    "one growing."},
            {"text": "Thorny roses were browsed less, so more of them set "
                     "seed.",
             "correct": True},
            {"text": "Roses began growing thorns once the deer started "
                     "browsing them.",
             "correct": False,
             "why": "That still has the plant answering the deer. Thorny and "
                    "smooth roses were both there beforehand; the browsing "
                    "only decided which set seed."},
            {"text": "Deer browsing made each rose grow thorns during its own "
                     "lifetime.",
             "correct": False,
             "why": "Being browsed does not put thorns on a smooth plant, and "
                    "anything a plant did in its own lifetime would not reach "
                    "its seed."},
        ],
        "figure": None,
    },
    {
        "id": "b11-02-e25",
        "band": "easier",
        "text": "Which of these is an adaptation, in the sense this lesson "
                "uses the word?",
        "options": [
            {"text": "The spines a hedgehog is born able to grow.",
             "correct": True},
            {"text": "A tree permanently bent by years of sea wind.",
             "correct": False,
             "why": "That shape was forced on the tree by the weather during "
                    "its life. An adaptation is a feature the organism "
                    "inherited the ability to have."},
            {"text": "A sheepdog trained to work to a whistle.",
             "correct": False,
             "why": "Training is something done to an animal after it is "
                    "born. It is not passed to its puppies, and it is not an "
                    "adaptation."},
            {"text": "A fox that has learned which night the bins go out.",
             "correct": False,
             "why": "Learning is an action taken during a life, and this "
                    "lesson is careful that an adaptation is a feature rather "
                    "than an action."},
        ],
        "figure": None,
    },
    {
        "id": "b11-02-e26",
        "band": "easier",
        "text": "An individual survives a hard winter because of a variation "
                "it carries, and then dies without breeding. Why does natural "
                "selection require survivors to reproduce?",
        "options": [
            {"text": "Because surviving is only proof of a variation working "
                     "once, and it has to work twice to count.",
             "correct": False,
             "why": "There is no counting rule of that kind. The problem is "
                    "simply that nothing has been handed on."},
            {"text": "Because breeding is the only route by which its version "
                     "of the gene reaches the next generation.",
             "correct": True},
            {"text": "Because an animal that has not bred is not considered a "
                     "full member of its population.",
             "correct": False,
             "why": "It is a member of the population throughout its life. "
                    "What it has not done is contribute to the generation "
                    "after it."},
            {"text": "Because the variation weakens in an animal that has "
                     "never used it to raise young.",
             "correct": False,
             "why": "A version of a gene does not weaken with disuse. It "
                    "either gets passed on or it stops with that animal."},
        ],
        "figure": None,
    },
    {
        "id": "b11-02-e27",
        "band": "easier",
        "text": "After many generations of natural selection a population is "
                "described as having changed. What is it about the population "
                "that is different?",
        "options": [
            {"text": "Each individual has been altered by what it lived "
                     "through.",
             "correct": False,
             "why": "No individual is altered at any point. This is the one "
                    "claim the whole lesson is built to rule out."},
            {"text": "The proportions of the different kinds of individual "
                     "in it.",
             "correct": True},
            {"text": "The total number of individuals it contains, which "
                     "rises as the population becomes better suited.",
             "correct": False,
             "why": "Numbers can go up, down or nowhere. The change natural "
                    "selection describes is in the make-up of the population, "
                    "not its size."},
            {"text": "The species it belongs to, which becomes a new one once "
                     "enough generations have passed.",
             "correct": False,
             "why": "A shift in proportions within a species is what this "
                    "lesson describes. Nothing here requires a new species to "
                    "appear."},
        ],
        "figure": None,
    },
    {
        "id": "b11-02-e28",
        "band": "easier",
        "text": "Natural selection is described as having no goal. What does "
                "that mean?",
        "options": [
            {"text": "Nothing is working towards anything — what survives "
                     "better depends only on the conditions of the moment.",
             "correct": True},
            {"text": "It means the outcome cannot be predicted at all, even "
                     "when the conditions are known.",
             "correct": False,
             "why": "The outcome often can be predicted. Knowing which "
                    "variation survives better in these conditions tells you "
                    "which way the proportions will move."},
            {"text": "It means the process runs too slowly for anyone to say "
                     "where a population is heading.",
             "correct": False,
             "why": "Speed is a separate matter, and bacteria show the same "
                    "process running in days. Having no goal is about there "
                    "being nothing aimed at."},
            {"text": "It means the population has already reached the best "
                     "form it could take.",
             "correct": False,
             "why": "There is no best form to reach. Conditions shift, and "
                    "what suits them shifts with them."},
        ],
        "figure": None,
    },
    {
        "id": "b11-02-e29",
        "band": "easier",
        "text": "A single mouse cannot adapt during its own life, however "
                "hard the conditions become. Why not?",
        "options": [
            {"text": "Because a mouse does not live long enough for a change "
                     "of that size to show.",
             "correct": False,
             "why": "Length of life is not the obstacle. A tortoise living a "
                    "century could not do it either."},
            {"text": "Because its genes do not rewrite themselves, and what "
                     "changes is which mice breed.",
             "correct": True},
            {"text": "Because a mouse is too small and simple an animal to "
                     "respond to its surroundings.",
             "correct": False,
             "why": "A mouse responds to its surroundings constantly — it "
                    "shivers, hides and hunts for food. None of that alters "
                    "what it passes to its young."},
            {"text": "Because a mouse would need to be told what the "
                     "conditions required of it.",
             "correct": False,
             "why": "Nothing is telling any organism anything. Even a mouse "
                    "that somehow knew what was needed could not rewrite its "
                    "own genes to supply it."},
        ],
        "figure": None,
    },
    {
        "id": "b11-02-e30",
        "band": "easier",
        "text": "How does one variation become commoner in a population over "
                "many generations?",
        "options": [
            {"text": "The individuals that carry it leave more offspring than "
                     "the rest.",
             "correct": True},
            {"text": "The individuals that lack it gradually acquire it as "
                     "the conditions press on them.",
             "correct": False,
             "why": "An individual cannot acquire a variation it was not born "
                    "with. The proportions move because of who breeds, not "
                    "because anyone changes."},
            {"text": "It spreads from individual to individual through the "
                     "population, in the way a disease does.",
             "correct": False,
             "why": "A variation is inherited from a parent, not caught from "
                    "a neighbour. It travels only into the next generation."},
            {"text": "The population produces more of it once the conditions "
                     "call for it.",
             "correct": False,
             "why": "Nothing is answering a call. A population produces "
                    "whatever its parents carried, in the proportions those "
                    "parents managed to breed."},
        ],
        "figure": None,
    },
    # ── standard · the MRB-338 expansion ────────────────────────────────
    {
        "id": "b11-02-s14",
        "band": "standard",
        "text": "A wood with soot-blackened trunks holds 800 pale moths and "
                "200 dark ones. Of every 100 pale moths 45 survive the "
                "generation, and of every 100 dark moths 85 survive. How many "
                "of each kind are left?",
        "options": [
            {"text": "440 pale and 170 dark.",
             "correct": False,
             "why": "The pale figure has been worked out from 55 in every "
                    "100 rather than 45 — the proportion that died instead of "
                    "the proportion that lived."},
            {"text": "360 pale and 30 dark.",
             "correct": False,
             "why": "The dark figure uses 15 in every 100 rather than 85. "
                    "Dark is the colour that does well on sooty bark, so the "
                    "larger share must survive."},
            {"text": "360 pale and 170 dark.",
             "correct": True},
            {"text": "45 pale and 85 dark.",
             "correct": False,
             "why": "Those are the survival rates per hundred, copied out as "
                    "though they were the answer. They still have to be "
                    "applied to 800 moths and to 200."},
        ],
        "figure": None,
    },
    {
        "id": "b11-02-s15",
        "band": "standard",
        "text": "One tenth of a population of 2000 moths is dark, and the "
                "trunks are sooty, so 85 of every 100 dark moths survive the "
                "generation. How many dark moths survive?",
        "options": [
            {"text": "200 moths.",
             "correct": False,
             "why": "That is how many dark moths there were to start with. "
                    "The survival rate has not been applied to it yet."},
            {"text": "170 moths.",
             "correct": True},
            {"text": "1700 moths.",
             "correct": False,
             "why": "That is 85 in every 100 of the whole population of 2000. "
                    "Only a tenth of them are dark."},
            {"text": "85 moths.",
             "correct": False,
             "why": "That is the survival rate per hundred, not a number of "
                    "moths. There are two hundred dark moths, not one "
                    "hundred."},
        ],
        "figure": None,
    },
    {
        "id": "b11-02-s16",
        "band": "standard",
        "text": "In one stretch of a stream, guppies live alongside fish that "
                "eat them and the males are dull brown. Above a waterfall the "
                "same species lives with no such fish, and the males there "
                "are brightly coloured. Which explanation fits?",
        "options": [
            {"text": "The dull males below the falls faded because living in "
                     "danger drains an animal's colour.",
             "correct": False,
             "why": "Fear does not drain colour out of a fish, and even if it "
                    "did, a faded parent would still produce brightly "
                    "coloured young."},
            {"text": "Below the falls the brightest males were seen and eaten "
                     "first, so duller ones did most of the breeding.",
             "correct": True},
            {"text": "The guppies above the falls chose to become brighter "
                     "once there was nothing left in the stream that would "
                     "eat them.",
             "correct": False,
             "why": "No fish chooses its colour. What differs between the two "
                    "stretches is which males lived long enough to breed."},
            {"text": "The two stretches hold different species that happen to "
                     "look alike.",
             "correct": False,
             "why": "They are one species, which is what makes the comparison "
                    "worth making: the same variation has gone different ways "
                    "under different conditions."},
        ],
        "figure": None,
    },
    {
        "id": "b11-02-s17",
        "band": "standard",
        "text": "A disease sweeps through a rabbit population and kills most "
                "of it. Twenty years later the same disease returns and kills "
                "a far smaller proportion. Explain the difference.",
        "options": [
            {"text": "The rabbits that lived through the first outbreak were "
                     "left with a lasting immunity they handed to their "
                     "young.",
             "correct": False,
             "why": "Immunity built during an animal's own life stops with "
                    "that animal. What is passed on is the genes it was born "
                    "with."},
            {"text": "The first outbreak used the disease up, so there was "
                     "less of it left in the population twenty years later.",
             "correct": False,
             "why": "A disease is not a stock that gets spent. It is still "
                    "there in full, and what has changed is which rabbits it "
                    "meets."},
            {"text": "The survivors passed their resistance on.",
             "correct": True},
            {"text": "The rabbits learned to avoid one another after the "
                     "first outbreak, so fewer of them met it.",
             "correct": False,
             "why": "Rabbits do not work out what spread a disease, and "
                    "behaviour learned by one generation is not inherited by "
                    "the next in any case."},
        ],
        "figure": None,
    },
    {
        "id": "b11-02-s18",
        "band": "standard",
        "text": "A student writes: the moths adapted to the sooty bark. The "
                "teacher marks the sentence wrong even though the population "
                "did end up mostly dark. What is the objection?",
        "options": [
            {"text": "Sooty is the wrong word for bark that has been "
                     "blackened by industrial smoke.",
             "correct": False,
             "why": "Sooty describes it perfectly well. The fault is in what "
                    "the sentence says the moths did."},
            {"text": "Adapted is written as something the moths did, when an "
                     "adaptation is a feature they were hatched with.",
             "correct": True},
            {"text": "The sentence should say the moths evolved rather than "
                     "adapted, since only that word is allowed here.",
             "correct": False,
             "why": "Swapping one word for another fixes nothing while the "
                    "sentence still has the moths doing the changing "
                    "themselves."},
            {"text": "The population did not end up mostly dark, so the "
                     "sentence is wrong about the outcome.",
             "correct": False,
             "why": "The outcome in the sentence is right, and that is what "
                    "makes it a useful thing to mark: a true result reached "
                    "by a wrong route."},
        ],
        "figure": None,
    },
    {
        "id": "b11-02-s19",
        "band": "standard",
        "text": "A patient feels better after three days and stops taking his "
                "antibiotic, though he was told to finish the course. Explain "
                "why that can leave a harder infection behind.",
        "options": [
            {"text": "Stopping early gives the bacteria a rest, after which "
                     "they come back stronger than before.",
             "correct": False,
             "why": "Bacteria do not recover strength during a pause. What "
                    "matters is which ones are still alive when the drug "
                    "stops arriving."},
            {"text": "The bacteria least affected by the drug are the ones "
                     "still alive at three days, and they are left to breed.",
             "correct": True},
            {"text": "The unused tablets go on working inside the body and "
                     "train the bacteria to withstand them.",
             "correct": False,
             "why": "A tablet in a cupboard does nothing at all, and no "
                    "bacterium is trained by a drug. The drug only ever "
                    "removes the ones it can kill."},
            {"text": "Feeling better is a sign the infection has already "
                     "gone, so the remaining tablets do no work.",
             "correct": False,
             "why": "Feeling better usually means numbers are down, not that "
                    "none are left. The ones left are the hardest to kill, "
                    "which is the point."},
        ],
        "figure": None,
    },
    {
        "id": "b11-02-s20",
        "band": "standard",
        "text": "Four things happen when natural selection changes a "
                "population. Which of them has to be in place before any of "
                "the others can matter?",
        "options": [
            {"text": "Conditions change, so that the place is no longer what "
                     "it was.",
             "correct": False,
             "why": "A change in conditions is usually what starts things "
                    "moving, but it can only sort differences that are "
                    "already there to be sorted."},
            {"text": "Offspring inherit their parents' features, so whatever "
                     "survived is carried forward into the generation after "
                     "it.",
             "correct": False,
             "why": "Inheritance is needed, and it comes later in the "
                    "sequence: there has to be something different to inherit "
                    "before it can be handed on."},
            {"text": "More young are born than the food and space can "
                     "support, so most of them die.",
             "correct": False,
             "why": "Overproduction is what makes the survival difference "
                    "matter, but with every individual identical it would "
                    "simply thin the numbers and change nothing."},
            {"text": "Individuals in the population already differ from one "
                     "another in the feature concerned.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b11-02-s21",
        "band": "standard",
        "text": "In one wood the dark form survives at 85 in 100 and the pale "
                "at 45 in 100. In a second wood the figures are 75 and 65. "
                "Both start half and half. Which population goes dark faster, "
                "and why?",
        "options": [
            {"text": "The first wood, where the gap between the two rates is "
                     "wider.",
             "correct": True},
            {"text": "The second wood, because a small difference acts on "
                     "every moth while a large one only acts on the weakest.",
             "correct": False,
             "why": "A survival rate applies across the whole of each colour "
                    "either way. A wider gap simply removes a larger share of "
                    "the pale moths each generation."},
            {"text": "Both at the same speed, since the dark form is ahead in "
                     "both woods and that is what decides it.",
             "correct": False,
             "why": "Being ahead sets the direction, not the speed. How fast "
                    "the proportions move depends on how big the difference "
                    "in survival is."},
            {"text": "Neither, because the starting proportions are the same "
                     "in the two woods.",
             "correct": False,
             "why": "The starting point is the same, which is exactly why the "
                    "two can be compared. What differs is the size of the "
                    "survival advantage."},
        ],
        "figure": None,
    },
    {
        "id": "b11-02-s22",
        "band": "standard",
        "text": "A fungus kills almost every elm in a county, and a handful "
                "of trees come through it untouched. Before collecting seed "
                "from those trees, what would a scientist most need to know?",
        "options": [
            {"text": "Whether the fungus is likely to return to the county in "
                     "the next few years.",
             "correct": False,
             "why": "Worth knowing, but it does not tell her anything about "
                    "the seed. The question is whether these trees have "
                    "something to pass on."},
            {"text": "Whether their survival came from something inherited "
                     "rather than from where they happened to grow.",
             "correct": True},
            {"text": "Whether the surviving trees are older than the ones "
                     "that died around them.",
             "correct": False,
             "why": "Age is not passed to a seedling. Even if the survivors "
                    "were all old, their seed would not inherit having been "
                    "old."},
            {"text": "Whether the surviving trees can be grown on in a "
                     "nursery before being planted out.",
             "correct": False,
             "why": "That is a practical detail of the planting. It says "
                    "nothing about whether the seed carries the resistance "
                    "she is after."},
        ],
        "figure": None,
    },
    {
        "id": "b11-02-s23",
        "band": "standard",
        "text": "Waste heaps at an old lead mine kill almost every grass "
                "seedling that lands on them, but a few tufts grow there. "
                "Seed collected from those tufts grows well on the same "
                "waste. What has happened?",
        "options": [
            {"text": "The waste heaps have become less poisonous with time, "
                     "so grass now grows on them wherever it lands.",
             "correct": False,
             "why": "Ordinary grass seed still dies there, which is what "
                    "makes the seed from the tufts worth noticing. The heaps "
                    "have not changed."},
            {"text": "The parent tufts were toughened by growing on the "
                     "waste, and their seed inherited that toughening.",
             "correct": False,
             "why": "Hardship endured by a parent plant is not written into "
                    "its seed. The seed does well because of what the parents "
                    "already carried."},
            {"text": "Those few plants already carried a tolerance of the "
                     "metal, and it is inherited by their seed.",
             "correct": True},
            {"text": "The seed picked up the metal from the parent plants and "
                     "is now used to it.",
             "correct": False,
             "why": "Carrying a trace of metal is not the same as tolerating "
                    "it. What the seedlings inherit is the ability to grow "
                    "where the metal is."},
        ],
        "figure": None,
    },
    {
        "id": "b11-02-s24",
        "band": "standard",
        "text": "A scientist wants to test the claim that birds hunting by "
                "sight are what changes moth colour in a wood. Which "
                "measurement would test it, rather than assume it?",
        "options": [
            {"text": "How many moths of each colour are in the wood at the "
                     "start and at the end of the study.",
             "correct": False,
             "why": "That shows the proportions moving but not what moved "
                    "them. Something other than birds could be doing it."},
            {"text": "How many moths of each colour the birds actually take "
                     "from each kind of bark.",
             "correct": True},
            {"text": "How dark the bark is in different parts of the wood, "
                     "measured at several heights on the trunks.",
             "correct": False,
             "why": "A careful description of the background, and no "
                    "information at all about what the birds do with it."},
            {"text": "How many eggs a pale moth lays compared with a dark one "
                     "of the same age.",
             "correct": False,
             "why": "A useful figure for a different question. The claim "
                    "being tested is about which moths are eaten, not about "
                    "how many eggs each lays."},
        ],
        "figure": None,
    },
    {
        "id": "b11-02-s25",
        "band": "standard",
        "text": "An earlier moth experiment was criticised for releasing "
                "moths by day, in numbers no real wood would hold, onto "
                "exposed trunks. A later scientist repeated it with moths in "
                "natural resting places and at natural numbers. Why work that "
                "way?",
        "options": [
            {"text": "Because a result only answers a criticism if the thing "
                     "criticised is what has been changed.",
             "correct": True},
            {"text": "Because an experiment has to be repeated exactly as it "
                     "was first done for the repeat to count.",
             "correct": False,
             "why": "An exact repeat would reproduce the criticised "
                    "conditions along with everything else, and would settle "
                    "nothing that was in dispute."},
            {"text": "Because the first scientist's results had been shown to "
                     "be invented rather than measured.",
             "correct": False,
             "why": "Nothing of the kind was found. The dispute was about the "
                    "conditions the moths were released into, not about "
                    "honesty."},
            {"text": "Because a study always becomes more reliable when it is "
                     "carried out over a longer period of years.",
             "correct": False,
             "why": "Length alone fixes nothing. A long study run under the "
                    "same criticised conditions would meet the same "
                    "objection."},
        ],
        "figure": None,
    },
    {
        "id": "b11-02-s26",
        "band": "standard",
        "text": "A disease kills nine deer in every ten in a herd. The "
                "survivors breed and numbers recover. A farmer says the "
                "disease made the herd stronger. Give the better description.",
        "options": [
            {"text": "The disease toughened the deer that met it and lived, "
                     "and their calves were born tougher as a result.",
             "correct": False,
             "why": "Surviving an illness does not rewrite what an animal "
                    "hands to its calf. The calves inherit the genes their "
                    "parents already had."},
            {"text": "The herd is no different, because losing nine in ten "
                     "leaves the same mixture of animals behind.",
             "correct": False,
             "why": "It leaves a very particular tenth — the ones the disease "
                    "did not kill — so the mixture is not the same at all."},
            {"text": "The deer that already resisted it bred, so more of the "
                     "herd carries what they carried.",
             "correct": True},
            {"text": "The disease removed the oldest deer, and a young herd "
                     "is stronger than an old one.",
             "correct": False,
             "why": "Nothing here says age decided who died, and a shift in "
                    "the ages of a herd is not something passed to the next "
                    "generation."},
        ],
        "figure": None,
    },
    {
        "id": "b11-02-s27",
        "band": "standard",
        "text": "Britain's air is clean and its woodland moths are mostly "
                "pale again. A single valley then reopens its coalworks and "
                "its trunks blacken once more. Predict what happens to that "
                "valley's moths.",
        "options": [
            {"text": "Nothing changes, because the species as a whole has "
                     "settled back to pale.",
             "correct": False,
             "why": "Selection acts where the moths are. A population in a "
                    "blackened valley is being sorted by that valley's "
                    "trunks, not by the country's average."},
            {"text": "The valley's moths grow darker over their lifetimes to "
                     "match the trunks they rest on.",
             "correct": False,
             "why": "No moth darkens to match anything. What shifts is the "
                    "share of dark moths being born, and it shifts across "
                    "generations."},
            {"text": "The valley's population drifts back towards dark while "
                     "the rest of the country stays pale.",
             "correct": True},
            {"text": "Dark moths fly in from elsewhere to fill the valley, "
                     "since the conditions there now suit them.",
             "correct": False,
             "why": "Moths do not travel towards bark that would hide them. "
                    "The change comes from which of the valley's own moths "
                    "survive to breed."},
        ],
        "figure": None,
    },
    {
        "id": "b11-02-s28",
        "band": "standard",
        "text": "Before treatment, about one bacterium in a million in a "
                "patient can withstand a particular antibiotic. A week later "
                "almost all of them can. Did the drug cause the resistance?",
        "options": [
            {"text": "Yes, because a drug that fails to kill a bacterium "
                     "leaves it altered.",
             "correct": False,
             "why": "Failing to kill something changes nothing about it. The "
                    "survivors were already the ones the drug could not "
                    "touch."},
            {"text": "Yes, because resistance appears only where an "
                     "antibiotic has been used.",
             "correct": False,
             "why": "Resistant bacteria have been found in soil sealed away "
                    "long before antibiotics were ever made. Use reveals "
                    "resistance rather than creating it."},
            {"text": "No, because the resistant few were already there and "
                     "the drug cleared the rest out of their way.",
             "correct": True},
            {"text": "No, because the proportion has not really risen, and "
                     "only looks higher once the total number of bacteria "
                     "falls.",
             "correct": False,
             "why": "The proportion genuinely has risen: almost every "
                    "bacterium now present is descended from the resistant "
                    "few."},
        ],
        "figure": None,
    },
    {
        "id": "b11-02-s29",
        "band": "standard",
        "text": "A wood's moths are nine tenths pale, and its trunks have "
                "just been blackened, so dark moths now survive far better "
                "than pale ones. Why does the wood still hold more pale moths "
                "than dark ones after one generation?",
        "options": [
            {"text": "Because pale moths breed faster than dark ones and make "
                     "up their losses within the season.",
             "correct": False,
             "why": "Nothing here says the two colours breed at different "
                    "rates. The reason is simply how many of each there were "
                    "to begin with."},
            {"text": "Because the birds need time to learn that the pale "
                     "moths are now the easy ones to find.",
             "correct": False,
             "why": "The birds take whatever they can see from the first day. "
                    "No learning period is needed for the survival difference "
                    "to apply."},
            {"text": "Because pale moths started far commoner, so a poorer "
                     "survival rate still leaves more of them.",
             "correct": True},
            {"text": "Because one generation is too short a time for any "
                     "moths at all to die.",
             "correct": False,
             "why": "Most of them die within the generation. What one "
                    "generation is too short for is a large shift in the "
                    "proportions."},
        ],
        "figure": None,
    },
    {
        "id": "b11-02-s30",
        "band": "standard",
        "text": "A biologist claims that natural selection is acting on shell "
                "colour in a snail population. What would she have to show "
                "for the claim to stand?",
        "options": [
            {"text": "That the snails with the commoner colour are larger and "
                     "live longer than the rest.",
             "correct": False,
             "why": "Size and length of life say nothing on their own. The "
                    "claim is about colour affecting who breeds, and about "
                    "colour being inherited."},
            {"text": "That one colour survives better than another, and that "
                     "colour is inherited.",
             "correct": True},
            {"text": "That the proportions of the colours have changed over "
                     "the last few years.",
             "correct": False,
             "why": "A change in proportions is what selection would produce, "
                    "but on its own it does not show what produced it."},
            {"text": "That the snails' colour matches the ground they are "
                     "found on more closely than it used to.",
             "correct": False,
             "why": "A close match is suggestive and no more. Without a "
                    "survival difference and inheritance, it could be an "
                    "accident of where snails happen to be found."},
        ],
        "figure": None,
    },
    # ── harder · the MRB-338 expansion ──────────────────────────────────
    {
        "id": "b11-02-h14",
        "band": "harder",
        "text": "A wood on sooty bark starts with 100 pale moths and 100 dark "
                "ones. Of every 100 pale moths 45 survive the generation, and "
                "of every 100 dark moths 85 survive. What share of the "
                "survivors is dark?",
        "options": [
            {"text": "About 65%.",
             "correct": True},
            {"text": "Exactly 50%.",
             "correct": False,
             "why": "That is the share the wood started with. The two "
                    "survival rates are different, so the survivors cannot be "
                    "split evenly."},
            {"text": "About 85%.",
             "correct": False,
             "why": "85 in every 100 dark moths survive, which is not the "
                    "same as dark moths being 85% of the survivors. The pale "
                    "survivors have to be counted too."},
            {"text": "About 40%.",
             "correct": False,
             "why": "That would make dark the smaller share, when dark is the "
                    "colour surviving nearly twice as well on this bark."},
        ],
        "figure": None,
    },
    {
        "id": "b11-02-h15",
        "band": "harder",
        "text": "On sooty bark the dark form spreads quickly at first, then "
                "the population changes more and more slowly even though the "
                "survival rates have not altered. Why does it slow down?",
        "options": [
            {"text": "The birds lose interest in pale moths once there are "
                     "not many of them left to find.",
             "correct": False,
             "why": "A bird eats what it sees, however rare that has become. "
                    "Nothing about the birds' behaviour has changed in this "
                    "account."},
            {"text": "The pale form becomes rare, so each generation there "
                     "are far fewer pale moths left to be removed.",
             "correct": True},
            {"text": "The dark moths begin competing with one another, which "
                     "cancels out their advantage over the pale ones.",
             "correct": False,
             "why": "Competition among dark moths would thin them, but it "
                    "does nothing to the difference in how easily birds spot "
                    "the two colours."},
            {"text": "The survival advantage wears off as a population gets "
                     "used to living with it.",
             "correct": False,
             "why": "A population does not get used to a survival rate. The "
                    "advantage is still there; there is simply less pale left "
                    "for it to act against."},
        ],
        "figure": None,
    },
    {
        "id": "b11-02-h16",
        "band": "harder",
        "text": "A pigeon keeper breeds only from his fastest birds, and "
                "after twenty years his loft is markedly faster. A wild "
                "population of the same pigeon nearby is no faster than it "
                "was. What is the same in the two cases, and what differs?",
        "options": [
            {"text": "The loft birds were altered by their keeper, and wild "
                     "birds can only be altered by a change in the weather.",
             "correct": False,
             "why": "No bird was altered in either place. Weather is one "
                    "possible pressure among many, and it is not what makes "
                    "the two cases comparable."},
            {"text": "Both changed by which birds bred, and the wild birds "
                     "have simply not had enough generations yet to show it.",
             "correct": False,
             "why": "The wild birds have had the same twenty years. Nothing "
                    "there is removing the slower ones, so there is no "
                    "direction for them to move in."},
            {"text": "The loft birds were trained to fly faster, while the "
                     "wild ones were left to fly as they pleased.",
             "correct": False,
             "why": "Training an individual changes nothing it hands to its "
                    "young. The loft changed because of which birds were "
                    "allowed to breed."},
            {"text": "Both changed by which birds bred; in the loft a person "
                     "decided that, and in the wild the conditions did.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b11-02-h17",
        "band": "harder",
        "text": "A fungal disease reaches a population of 2000 frogs and "
                "kills all but two, which happen to carry a version of a gene "
                "that resists it. The species survives and numbers climb "
                "back. What has the population gained, and what has it lost?",
        "options": [
            {"text": "It has gained resistance to every disease, and lost "
                     "only its resistance to the fungus.",
             "correct": False,
             "why": "Surviving one fungus says nothing about any other "
                    "disease, and the resistance to this one is precisely "
                    "what was kept."},
            {"text": "It has gained resistance to the fungus, and lost "
                     "nothing that matters once the numbers are back.",
             "correct": False,
             "why": "Numbers and variation are not the same thing. Every frog "
                    "now descends from two, so the differences the other 1998 "
                    "carried are gone."},
            {"text": "It has gained nothing, because two frogs are too few to "
                     "rebuild a population from.",
             "correct": False,
             "why": "Two can rebuild the numbers, and the resistance is a "
                    "real gain. The problem is what came back with it."},
            {"text": "It has gained resistance to the fungus, and lost almost "
                     "all the rest of its variation.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b11-02-h18",
        "band": "harder",
        "text": "Sparrows are taken to an island with no hawks or cats on it. "
                "Two hundred generations later they are slightly worse at "
                "escaping a hawk than their mainland ancestors were. Explain "
                "how that could happen.",
        "options": [
            {"text": "Without hawks, escaping them stopped making any "
                     "difference to which sparrows bred.",
             "correct": True},
            {"text": "The sparrows forgot how to escape hawks, and passed "
                     "their forgetting on to their young.",
             "correct": False,
             "why": "What an animal remembers or forgets in its own life is "
                    "not inherited. The change is in which birds left "
                    "offspring, over two hundred generations."},
            {"text": "The island sparrows are a different species now, so "
                     "comparing them with the mainland birds proves nothing.",
             "correct": False,
             "why": "They are still the same species in this account, and the "
                    "comparison is exactly what shows the change."},
            {"text": "Escaping hawks was never inherited, so it could never "
                     "have changed in either direction.",
             "correct": False,
             "why": "If it were not inherited, the mainland birds could not "
                    "have been good at it in the first place. It is "
                    "inherited, and it was no longer being tested."},
        ],
        "figure": None,
    },
    {
        "id": "b11-02-h19",
        "band": "harder",
        "text": "A conservationist wants a rare butterfly to become better "
                "able to cope with hotter summers. She can fence the meadow, "
                "keep out collectors and plant more of its food. What can she "
                "not supply by any of that?",
        "options": [
            {"text": "A meadow large enough to hold a population through a "
                     "run of poor years.",
             "correct": False,
             "why": "Fencing a larger meadow is within her power. Space keeps "
                    "a population alive; it does not make its individuals "
                    "differ."},
            {"text": "Enough food plants for the caterpillars to reach adult "
                     "size in a hot summer.",
             "correct": False,
             "why": "Planting more food is one of the things she can do, and "
                    "she is doing it. It helps numbers without giving "
                    "selection anything to act on."},
            {"text": "Protection from people collecting the adults for their "
                     "own collections.",
             "correct": False,
             "why": "That is exactly what keeping collectors out achieves. It "
                    "removes one pressure and supplies no variation."},
            {"text": "Butterflies that already differ from one another in how "
                     "well they cope with heat.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b11-02-h20",
        "band": "harder",
        "text": "Bacteria on one hospital ward are almost all able to "
                "withstand one antibiotic and almost all killed by a "
                "different one. Explain why surviving the first drug brought "
                "no protection against the second.",
        "options": [
            {"text": "Because bacteria can only ever carry resistance to one "
                     "antibiotic at a time.",
             "correct": False,
             "why": "Bacteria can carry resistance to several drugs at once, "
                    "which is what makes some infections so hard to treat. "
                    "There is no limit of one."},
            {"text": "Because the first drug used up the bacteria's ability "
                     "to resist anything further.",
             "correct": False,
             "why": "Resistance is not a store that runs down. It is a "
                    "feature a bacterium either has against a given drug or "
                    "does not."},
            {"text": "Because the second drug is newer, and resistance takes "
                     "a fixed number of years to appear.",
             "correct": False,
             "why": "Age is not what decides it. Resistance appears when the "
                    "population happens to contain individuals the drug "
                    "cannot kill."},
            {"text": "Because the variation that was selected was the one "
                     "that mattered to the first drug, and the second works "
                     "in another way.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b11-02-h21",
        "band": "harder",
        "text": "Bacteria grown from soil that was sealed in 1940, before "
                "the antibiotic existed, turn out to withstand it. Which "
                "claim does that finding support?",
        "options": [
            {"text": "That using an antibiotic is what produces resistance to "
                     "it in the first place.",
             "correct": False,
             "why": "This finding is the clearest evidence against that. The "
                    "resistance is in soil that was sealed away before the "
                    "drug existed."},
            {"text": "That the soil sample was contaminated at some point "
                     "after it was sealed.",
             "correct": False,
             "why": "That would explain the result away rather than follow "
                    "from it, and it is not what repeated sampling of old "
                    "soils has found."},
            {"text": "That antibiotics are made by bacteria themselves rather "
                     "than in a laboratory.",
             "correct": False,
             "why": "Where a drug comes from is a separate question. The "
                    "finding is about when the resistance was present, not "
                    "about who made the drug."},
            {"text": "That resistance was present in bacterial populations "
                     "before the drug was ever used on anybody.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b11-02-h22",
        "band": "harder",
        "text": "Moth colour is set by a single gene. Body size in the same "
                "moth depends on many genes and on how much the caterpillar "
                "managed to eat. Why is colour the easier feature to study "
                "natural selection with?",
        "options": [
            {"text": "Because colour is easier for a scientist to see than "
                     "size is to weigh.",
             "correct": False,
             "why": "Both can be measured accurately enough. The difficulty "
                    "with size is working out how much of it was inherited at "
                    "all."},
            {"text": "Because a moth's colour is inherited whole, so a shift "
                     "in the population's colour is a shift in its genes.",
             "correct": True},
            {"text": "Because size does not vary between moths, so there is "
                     "nothing there for selection to act on.",
             "correct": False,
             "why": "Size varies a great deal. That is not the problem; the "
                    "problem is that feeding accounts for part of the "
                    "variation."},
            {"text": "Because only features controlled by one gene can be "
                     "acted on by natural selection.",
             "correct": False,
             "why": "Selection acts on any inherited feature, however many "
                    "genes are behind it. A single gene simply makes the "
                    "result easier to read."},
        ],
        "figure": None,
    },
    {
        "id": "b11-02-h23",
        "band": "harder",
        "text": "Nine hundred pale moths and one hundred dark ones rest on "
                "blackened trunks. Over a generation the birds take 55 in "
                "every 100 of the pale moths and 15 in every 100 of the dark "
                "ones. How many moths are left at the end of it?",
        "options": [
            {"text": "405 moths.",
             "correct": False,
             "why": "That is the pale survivors on their own. The 85 dark "
                    "moths that also come through the generation have been "
                    "left out of the total."},
            {"text": "510 moths.",
             "correct": False,
             "why": "That reads the two figures as the proportions surviving. "
                    "They are the proportions taken, so 45 in every 100 pale "
                    "moths and 85 in every 100 dark ones are the survivors."},
            {"text": "130 moths.",
             "correct": False,
             "why": "That applies the per-hundred figures as though the wood "
                    "held one hundred moths of each colour, rather than nine "
                    "hundred and one hundred."},
            {"text": "490 moths.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b11-02-h24",
        "band": "harder",
        "text": "A gardener mows his lawn weekly and hopes that over many "
                "years the grass will come to grow sideways instead of "
                "upwards. No plant in his lawn grows sideways now. What does "
                "the mechanism say will happen?",
        "options": [
            {"text": "Nothing of the kind, because there is no sideways "
                     "growth in the lawn for mowing to make commoner.",
             "correct": True},
            {"text": "It will happen, because mowing every week is a strong "
                     "enough pressure to force the change.",
             "correct": False,
             "why": "No pressure, however strong, can select a variation that "
                    "is not present. Mowing can only favour what some plants "
                    "already do."},
            {"text": "It will happen, but only once the grass has been mown "
                     "for a great many more years than that.",
             "correct": False,
             "why": "Time is not the missing ingredient. A thousand years of "
                    "mowing a lawn with no sideways growth in it changes "
                    "nothing."},
            {"text": "It will happen, because grass that is cut responds by "
                     "growing along the ground instead.",
             "correct": False,
             "why": "Some grasses do spread sideways, and those are ones that "
                    "already grow that way. A plant that grows upright does "
                    "not switch because it was cut."},
        ],
        "figure": None,
    },
    {
        "id": "b11-02-h25",
        "band": "harder",
        "text": "Cane toads have spread across northern Australia. The toads "
                "at the leading edge of the spread have noticeably longer "
                "legs than those in the areas settled long ago. Which "
                "explanation fits?",
        "options": [
            {"text": "The toads at the edge stretched their legs by "
                     "travelling so far, and their young were born "
                     "long-legged.",
             "correct": False,
             "why": "Legs lengthened by use are not handed on. The young "
                    "inherit the genes their parents carried, not the miles "
                    "they covered."},
            {"text": "The longest-legged toads travel furthest, so it is "
                     "their offspring that make up the leading edge.",
             "correct": True},
            {"text": "The toads at the edge are younger, and a young toad has "
                     "longer legs for its body.",
             "correct": False,
             "why": "Nothing here says the edge toads are younger, and a "
                    "difference in age would not build up across generations "
                    "the way this one has."},
            {"text": "The species needed to spread quickly, so it produced "
                     "longer legs where they were needed.",
             "correct": False,
             "why": "A species produces no feature to order. Long legs "
                    "happened to be there and happened to end up at the "
                    "front."},
        ],
        "figure": None,
    },
    {
        "id": "b11-02-h26",
        "band": "harder",
        "text": "Fish from a clear lake are put into a cloudy one, and fifty "
                "years later the fish there have larger eyes. A student "
                "writes that they grew larger eyes so they could see in the "
                "murk. Which rewrite is correct?",
        "options": [
            {"text": "The murk forced each fish's eyes to enlarge, and the "
                     "enlarged eyes were then passed to its young.",
             "correct": False,
             "why": "An eye does not enlarge to suit the water, and a change "
                    "made to a parent's body in its own life does not reach "
                    "its young."},
            {"text": "Eye size already varied, and fish with larger eyes fed "
                     "better in the murk and left more young.",
             "correct": True},
            {"text": "The fish with small eyes swam back to the clear lake, "
                     "leaving the large-eyed ones behind.",
             "correct": False,
             "why": "Nothing in the account lets them swim back, and a change "
                    "in who lives where is not the same as a change in the "
                    "population's make-up."},
            {"text": "Cloudy water contains more food, and a well-fed fish "
                     "grows larger eyes than a hungry one.",
             "correct": False,
             "why": "This would make eye size a result of feeding rather than "
                    "of inheritance, and then it could not be passed on at "
                    "all."},
        ],
        "figure": None,
    },
    {
        "id": "b11-02-h27",
        "band": "harder",
        "text": "Clean-air laws clear the soot from a wood, and at the same "
                "time the birds that hunted its moths leave for good. Predict "
                "what happens to the proportions of pale and dark moths, and "
                "explain why.",
        "options": [
            {"text": "They move towards an even split, because with no "
                     "pressure a population always evens out.",
             "correct": False,
             "why": "There is nothing pulling a population towards a half-"
                    "and-half split. With no survival difference, the "
                    "proportions simply stay where they were."},
            {"text": "They swing back towards pale, because pale is the "
                     "colour that suits clean bark.",
             "correct": False,
             "why": "Suiting the bark only matters while something is hunting "
                    "by sight. With the birds gone, being easy to see costs a "
                    "moth nothing."},
            {"text": "They swing further towards dark, because the dark form "
                     "is now free of the one thing holding it back.",
             "correct": False,
             "why": "The birds were not holding the dark form back on sooty "
                    "bark; they were favouring it. With them gone, neither "
                    "colour is favoured."},
            {"text": "They stop moving, because with nothing hunting them "
                     "neither colour survives better than the other.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b11-02-h28",
        "band": "harder",
        "text": "Bacteria that withstand one antibiotic grow more slowly than "
                "ordinary ones when no drug is present. A ward stops using "
                "that antibiotic for a year. Predict what happens to the "
                "resistant share of the bacteria there.",
        "options": [
            {"text": "It falls, because without the drug the resistant cells "
                     "are the ones at a disadvantage.",
             "correct": True},
            {"text": "It stays exactly where it was, because resistance once "
                     "gained by a population is never lost again.",
             "correct": False,
             "why": "What made resistance worth having was the drug. Remove "
                    "it and the slower growth of the resistant cells starts "
                    "to tell against them."},
            {"text": "It rises, because the resistant cells now have a whole "
                     "year with nothing to fight.",
             "correct": False,
             "why": "Having nothing to fight is the point: their resistance "
                    "buys them nothing and still costs them growth."},
            {"text": "It falls to nothing within a week, since a feature that "
                     "costs something disappears at once.",
             "correct": False,
             "why": "A small disadvantage works slowly, generation by "
                    "generation. Falling is right; falling to nothing in a "
                    "week is not."},
        ],
        "figure": None,
    },
    {
        "id": "b11-02-h29",
        "band": "harder",
        "text": "One moth population is split, and half is released into a "
                "wood with soot-blackened trunks while half stays in a "
                "lichen-covered one. Fifty generations later the two "
                "populations differ in colour. What does that show?",
        "options": [
            {"text": "That the same starting variation was pushed in "
                     "different directions by different conditions.",
             "correct": True},
            {"text": "That moths change colour to match whichever wood they "
                     "are put in.",
             "correct": False,
             "why": "No moth changed colour. Two populations that began the "
                    "same ended up different because different moths survived "
                    "in each wood."},
            {"text": "That the two halves were already different before they "
                     "were separated.",
             "correct": False,
             "why": "They came from one population, which is what makes the "
                    "comparison work: the only difference introduced was the "
                    "bark."},
            {"text": "That fifty generations is long enough for a species to "
                     "split into two new ones.",
             "correct": False,
             "why": "A difference in colour between two populations is not a "
                    "new species. Nothing here says they could no longer "
                    "breed together."},
        ],
        "figure": None,
    },
    {
        "id": "b11-02-h30",
        "band": "harder",
        "text": "A population has come to suit its conditions very closely "
                "after many generations. Why does natural selection not stop "
                "acting on it at that point?",
        "options": [
            {"text": "Because the population's variation grows larger each "
                     "generation, giving selection more to work on.",
             "correct": False,
             "why": "Selection tends to reduce the variation it acts on "
                    "rather than build it. The reason it does not stop is "
                    "that the conditions change."},
            {"text": "Because a population can always be improved further, "
                     "however well suited it already is.",
             "correct": False,
             "why": "There is no scale of improvement being climbed. What "
                    "counts as well suited is set by the conditions, and they "
                    "do not hold still."},
            {"text": "Because selection is a force that keeps running once it "
                     "has started.",
             "correct": False,
             "why": "It is not a force that runs on its own. It is what "
                    "happens whenever some individuals survive and breed "
                    "better than others."},
            {"text": "Because conditions keep shifting, and each generation "
                     "is sorted by whatever is happening at the time.",
             "correct": True},
        ],
        "figure": None,
    },
]
