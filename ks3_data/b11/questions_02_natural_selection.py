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
]
