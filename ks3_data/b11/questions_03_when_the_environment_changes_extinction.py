"""B11 lesson 03 — When the environment changes: extinction: twelve questions (MRB-269).

The lesson's whole argument is that vulnerability is a property, not a ranking:
what decides survival is whether a population's existing variation and its rate
of reproduction can keep up with the change. The bank probes that from four
directions. The easier band holds the facts the argument rests on — what
extinction actually is, which of the four risk factors is the hidden one, what
decides who survives a new disease, and what a background rate is measured
against. The standard band works the bench's own rows: the panda's high
predator score that explains nothing, why clearing half a wood does more than
halve its dormice, the gulls that moved into towns, and the belief that
something else just takes the place of what is lost. The harder band goes
somewhere new or joins two ideas — the kakapo's freeze response read as a
former advantage, a cave fish that is superbly adapted and still doomed, the
rat's five scores read off the stated colour bands, and the limitation the
one-pressure-at-a-time bench creates.

Both declared misconceptions supply distractors. EVOL-05 (extinction is
unnatural — it only happens because of us) sits behind e04's "the rate now,
because of people" reading of background rate. EVOL-06 (if a species goes
extinct another just takes its place) is the whole of s04, with its two
sub-beliefs split across options — that the replacement does the same job, and
that de-extinction makes the loss reversible. Three further errors the lesson
exists to correct run through the bank: that survival is about size and
strength (s01, s03, h03), that an individual or a species adapts on demand when
conditions change (s03, h02), and that being well adapted is protection against
change rather than the thing that makes a specialist vulnerable (h02). h03's
fourth option is the lesson's own measured point that the rat row has no amber
cell in it.

`figure` is None throughout: the lesson declares `figures: []`, measured — no
`<img>`, `<figure>` or `<picture>` appears anywhere on the page, and the unit's
one ruled diagram belongs to b11-02.
"""

UNIT = "B11"
LESSON = "when-the-environment-changes-extinction"
LESSON_NUMBER = 3

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "b11-03-e01",
        "band": "easier",
        "text": "A conservation group announces that a beetle is extinct. "
                "What exactly has happened?",
        "options": [
            {"text": "Its numbers have crashed to a very small population.",
             "correct": False,
             "why": "A crash is survivable. When disease sweeps through a rat "
                    "population the numbers crash and then rebuild from the "
                    "survivors. Extinction is the point past which there is "
                    "nothing left to rebuild from."},
            {"text": "The last individual of that beetle has died.",
             "correct": True},
            {"text": "It has disappeared from Britain but survives abroad.",
             "correct": False,
             "why": "That is a local loss, and the species still exists "
                    "somewhere. Extinction means the whole species is gone, "
                    "everywhere, and permanently."},
            {"text": "It has been added to the list of endangered species.",
             "correct": False,
             "why": "Endangered means at serious risk of extinction, not past "
                    "it. Kakapo fell to 51 birds and the population is now "
                    "climbing again — endangered, not extinct."},
        ],
        "figure": None,
    },
    {
        "id": "b11-03-e02",
        "band": "easier",
        "text": "Of the four risk factors, the lesson calls one the most "
                "important and the least visible. Which one?",
        "options": [
            {"text": "A specialist diet, because you cannot watch an animal "
                     "eat all year.",
             "correct": False,
             "why": "You can see what a species eats, and the panda's bamboo "
                    "is about as visible as a diet gets. A specialist diet is "
                    "a serious risk factor, but it is not the hidden one."},
            {"text": "A small or fragmented range, because a map does not "
                     "show the gaps.",
             "correct": False,
             "why": "A range is one of the easiest things to see — you can "
                    "draw it. The gaps show up on a map too, which is how the "
                    "dormouse's fragmentation problem was spotted."},
            {"text": "Slow reproduction, because breeding happens out of "
                     "sight in nests and burrows.",
             "correct": False,
             "why": "Breeding rate is countable: five litters a year for a "
                    "rat, one cub every two years for a panda. It is a real "
                    "risk factor and it is not a hidden one."},
            {"text": "Low genetic variation, because it is inside the "
                     "population's genes.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b11-03-e03",
        "band": "easier",
        "text": "A new disease sweeps through a population. What does the "
                "lesson say survival depends on?",
        "options": [
            {"text": "Whether any individuals in the population already carry "
                     "resistance to it.",
             "correct": True},
            {"text": "Whether the individuals are strong and healthy enough "
                     "to fight it off.",
             "correct": False,
             "why": "Strength is not what this is about. Survival depends on "
                    "whether the right genes happen to be there already, "
                    "which is a question about variation, not about how tough "
                    "an animal is."},
            {"text": "Whether the population is big enough that some "
                     "individuals escape infection.",
             "correct": False,
             "why": "Size helps, but only because a large, varied population "
                    "is likely to contain resistant individuals. Gull "
                    "colonies are large and dense, and they spread disease "
                    "very efficiently."},
            {"text": "Whether the species can move away from the area the "
                     "disease is in.",
             "correct": False,
             "why": "A population carries the disease with it, so moving does "
                    "not shake it off. What decides the outcome is whether "
                    "anyone in the population carries resistance."},
        ],
        "figure": None,
    },
    {
        "id": "b11-03-e04",
        "band": "easier",
        "text": "What does the term background rate mean?",
        "options": [
            {"text": "The rate at which species died out during the five mass "
                     "extinctions.",
             "correct": False,
             "why": "That is the opposite. Mass extinctions are the spikes; "
                    "the background rate is the ordinary level those spikes "
                    "are measured against."},
            {"text": "The rate at which species are going extinct now, "
                     "because of people.",
             "correct": False,
             "why": "Current rates are estimated at tens to hundreds of times "
                    "the background rate. The background rate is the thing "
                    "being compared against, not the thing being compared."},
            {"text": "The slow, steady rate at which species go extinct in "
                     "ordinary times.",
             "correct": True},
            {"text": "The total number of species that have ever gone extinct "
                     "on Earth.",
             "correct": False,
             "why": "That is a total, not a rate. A rate is a number of "
                    "extinctions in a stretch of time, which is what makes "
                    "the comparison with today checkable."},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "b11-03-s01",
        "band": "standard",
        "text": "On the bench the giant panda scores 70 against a new "
                "predator, far higher than it scores against anything else. "
                "What does that score tell you about why the panda is in "
                "trouble?",
        "options": [
            {"text": "That predators must be the reason, since that score is "
                     "the one that stands out.",
             "correct": False,
             "why": "It stands out because it is high, not because it "
                    "matters. A high score marks a pressure the species "
                    "handles, and this is the pressure that is not the "
                    "problem."},
            {"text": "That the score is a mistake, because a threatened "
                     "species should score low everywhere.",
             "correct": False,
             "why": "Vulnerability is a property against a particular "
                    "pressure, not a ranking of species. A species in serious "
                    "trouble can still be excellent at one thing, and the "
                    "panda is."},
            {"text": "Nothing — it is a real strength against a pressure that "
                     "is not the problem.",
             "correct": True},
            {"text": "That the panda would cope with habitat loss too, since "
                     "it can defend itself.",
             "correct": False,
             "why": "Being safe from predators does nothing about bamboo "
                    "forest being cleared for farmland. The panda scores 20 "
                    "against habitat loss, and that is a different property "
                    "entirely."},
        ],
        "figure": None,
    },
    {
        "id": "b11-03-s02",
        "band": "standard",
        "text": "Half a wood is cleared. Why does that do more damage to its "
                "dormice than simply halving their number?",
        "options": [
            {"text": "Dormice will not cross open ground, so the survivors "
                     "are stranded in fragments too small to last.",
             "correct": True},
            {"text": "The clearance is bound to take the half of the wood "
                     "that had the hazel trees in it.",
             "correct": False,
             "why": "Which half goes is not the point. Even if the trees left "
                    "behind are perfect, the dormice cannot move between the "
                    "pieces, and that is what does the damage."},
            {"text": "Dormice each need a very large territory, so half a "
                     "wood cannot hold half of them.",
             "correct": False,
             "why": "It is not about how much space one dormouse needs. It is "
                    "that a dormouse will not cross open ground, so each "
                    "remaining piece becomes a separate, isolated world."},
            {"text": "The dormice left behind are eaten quickly, because "
                     "clearing removes their cover from predators.",
             "correct": False,
             "why": "Predators are not the dormouse's worst pressure — it "
                    "scores 45 there and 15 against habitat loss. What does "
                    "the damage is fragmentation, not exposure."},
        ],
        "figure": None,
    },
    {
        "id": "b11-03-s03",
        "band": "standard",
        "text": "Herring gulls have responded to losing coastal habitat by "
                "moving into towns and nesting on roofs. Which idea from the "
                "lesson does that show?",
        "options": [
            {"text": "Gulls adapted to town life during their own lifetimes, "
                     "once the coast filled up.",
             "correct": False,
             "why": "An individual does not adapt on demand. Gulls could "
                    "already eat almost anything and live almost anywhere, so "
                    "nothing new had to evolve — they simply used what they "
                    "already had."},
            {"text": "A generalist can turn a change that would finish a "
                     "specialist into an opportunity.",
             "correct": True},
            {"text": "Habitat loss is not really a serious pressure, since a "
                     "species can move somewhere else.",
             "correct": False,
             "why": "Habitat loss is the commonest cause of extinction today. "
                    "The gull moves because it is a generalist; a dormouse "
                    "will not even cross a field to reach the next wood."},
            {"text": "Gulls are stronger and more aggressive than the species "
                     "that lost the same habitat.",
             "correct": False,
             "why": "Gulls are aggressive, and that is not why they cope. "
                    "What saves them is a varied diet and a wide range — "
                    "strength is not what decides who survives a change."},
        ],
        "figure": None,
    },
    {
        "id": "b11-03-s04",
        "band": "standard",
        "text": "A student says: if a species goes extinct, another one just "
                "takes its place. What is the strongest objection to that?",
        "options": [
            {"text": "Another species does exactly the same job, so the "
                     "ecosystem carries on unchanged.",
             "correct": False,
             "why": "That is the belief itself, not an objection to it. "
                    "Meanwhile the ecosystem runs without whatever the "
                    "missing species was doing, and those effects reach "
                    "species with no obvious connection to it."},
            {"text": "Nothing moves into the space for millions of years, so "
                     "it simply stays empty.",
             "correct": False,
             "why": "Something usually does move into the space, often fairly "
                    "quickly. What takes millions of years is the recovery of "
                    "diversity — the number and variety of species, not one "
                    "gap being filled."},
            {"text": "De-extinction projects will bring the lost species back "
                     "within a few years anyway.",
             "correct": False,
             "why": "De-extinction projects exist and are technically "
                    "interesting, but none has restored a functioning "
                    "population of a lost species. That is not a reason to be "
                    "relaxed about losing one."},
            {"text": "After past extinctions recovery took millions of years, "
                     "and the lost genes are gone.",
             "correct": True},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "b11-03-h01",
        "band": "harder",
        "text": "A kakapo freezes when it is threatened. That was an "
                "excellent defence in New Zealand before people arrived, and "
                "is a fatal one now. What changed?",
        "options": [
            {"text": "Kakapo lost the ability to move quickly at the same "
                     "time as they lost flight.",
             "correct": False,
             "why": "Freezing is a response the bird makes, not something it "
                    "is unable to avoid. It worked perfectly against the "
                    "predator the kakapo evolved alongside — the bird has not "
                    "got worse at anything."},
            {"text": "The predator it evolved with hunted by sight; the "
                     "stoats people brought hunt by smell.",
             "correct": True},
            {"text": "Freezing saves energy, and kakapo cannot spare any in a "
                     "year when no tree fruits.",
             "correct": False,
             "why": "Energy is not the issue here. The trait failed because a "
                    "new predator finds its prey in a completely different "
                    "way, so staying still now hides the bird from nothing."},
            {"text": "Stoats hunt in groups, so a bird that stays still is "
                     "surrounded before it moves.",
             "correct": False,
             "why": "How many hunters there are is not what matters. A "
                    "predator following a scent trail is unaffected by "
                    "whether its prey is moving, which is what makes the "
                    "freeze useless."},
        ],
        "figure": None,
    },
    {
        "id": "b11-03-h02",
        "band": "harder",
        "text": "A cave fish finds food in total darkness better than any "
                "other animal alive. Then the water table drops and the cave "
                "begins to dry out. Which statement is right?",
        "options": [
            {"text": "It was badly adapted all along, or a change like this "
                     "would not threaten it.",
             "correct": False,
             "why": "That argument is circular — you would only call it badly "
                    "adapted after it had died. The fish was superbly fitted "
                    "to the cave as it was, and the cave is what changed."},
            {"text": "It will survive, because a well adapted species is by "
                     "definition hard to kill.",
             "correct": False,
             "why": "Species that go extinct were usually well adapted — to "
                    "conditions that then changed. Being adapted means fitted "
                    "to one environment, not protected against that "
                    "environment changing."},
            {"text": "Being perfectly fitted to one narrow set of conditions "
                     "is exactly what makes it vulnerable.",
             "correct": True},
            {"text": "It will adapt to the new conditions, since it has "
                     "clearly managed to adapt before.",
             "correct": False,
             "why": "A fish cannot adapt on demand. Selection needs variation "
                    "that is already in the population and generations to "
                    "work through it, and a drying cave may leave time for "
                    "neither."},
        ],
        "figure": None,
    },
    {
        "id": "b11-03-h03",
        "band": "harder",
        "text": "On the bench a score of 65 or more is green, 40 to 64 is "
                "muted and below 40 is amber. The brown rat's five scores are "
                "85, 80, 75, 70 and 65. What can you say about that row?",
        "options": [
            {"text": "Every pressure leaves it in the green band, so it has "
                     "no vulnerable column at all.",
             "correct": True},
            {"text": "Its 65 against disease is an amber cell, so disease is "
                     "the pressure that could finish it.",
             "correct": False,
             "why": "65 is the floor of the green band, not amber. Disease is "
                    "the rat's weakest column and it is still not a "
                    "vulnerability — a large, varied population almost "
                    "certainly contains resistant individuals."},
            {"text": "It must be the strongest of the four species, which is "
                     "why it survives everything.",
             "correct": False,
             "why": "Rats are small and physically unimpressive. They survive "
                    "because they eat anything, breed up to five times a year "
                    "and live nearly everywhere — not because they are "
                    "strong."},
            {"text": "The bench must be wrong, because every species has to "
                     "be vulnerable to something.",
             "correct": False,
             "why": "It is tempting to expect a weakness in every row, but a "
                    "generalist really can shrug off all five pressures. That "
                    "is exactly why the rat is on the bench beside the "
                    "dormouse."},
        ],
        "figure": None,
    },
    {
        "id": "b11-03-h04",
        "band": "harder",
        "text": "The bench applies one pressure at a time, and says its "
                "fifty-year figures are illustrative. Which limitation does "
                "that create?",
        "options": [
            {"text": "The four species are invented, so their scores tell you "
                     "nothing about real animals.",
             "correct": False,
             "why": "The four species are real and their traits are "
                    "accurately described. It is the fifty-year population "
                    "figures that are illustrative, not the biology "
                    "underneath them."},
            {"text": "Fifty years is far too short for a species to be lost, "
                     "so every figure is optimistic.",
             "correct": False,
             "why": "Species have been lost in far less than fifty years. The "
                    "window is not the problem; what the bench leaves out is "
                    "that pressures arrive together rather than one at a "
                    "time."},
            {"text": "Real extinctions usually involve several pressures at "
                     "once, which one column cannot show.",
             "correct": True},
            {"text": "Pressures would cancel each other out if they arrived "
                     "together, so the scores are low.",
             "correct": False,
             "why": "Pressures compound rather than cancel. A population "
                    "already broken into fragments and losing variation is "
                    "far less likely to hold the resistance a new disease "
                    "tests for."},
        ],
        "figure": None,
    },
    # ── MRB-335 top-up ───────────────────────────────────────────────────
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "b11-03-e05",
        "band": "easier",
        "text": "A brown rat eats almost anything and lives almost anywhere. "
                "Biologists call it a generalist. What does that mean?",
        "options": [
            {"text": "A species that is the best in its habitat at everything "
                     "it does.",
             "correct": False,
             "why": "A generalist is rarely the best at anything. It is very "
                    "hard to get rid of, which is a different quality "
                    "altogether."},
            {"text": "A species that breeds faster than the other species "
                     "around it.",
             "correct": False,
             "why": "Fast breeding often goes with being a generalist and is "
                    "not what the word means. Generalist describes the range "
                    "of foods and places a species can use."},
            {"text": "A species that can use many different foods and live in "
                     "many different places.",
             "correct": True},
            {"text": "A species that has spread beyond the region it "
                     "originally came from.",
             "correct": False,
             "why": "Spreading is often a consequence of being a generalist "
                    "rather than the definition. A species can be a generalist "
                    "and still live in one country."},
        ],
        "figure": None,
    },
    {
        "id": "b11-03-e06",
        "band": "easier",
        "text": "How many mass extinctions are recorded in the fossil record, "
                "and which was the largest?",
        "options": [
            {"text": "Five, and the largest was at the end of the Permian.",
             "correct": True},
            {"text": "One, at the end of the Cretaceous, when the non-bird "
                     "dinosaurs died out.",
             "correct": False,
             "why": "That is the most famous of them, not the only one and not "
                    "the largest. Five are recorded, and the end-Permian was "
                    "far larger."},
            {"text": "Five, and the largest was the asteroid impact that ended "
                     "the dinosaurs.",
             "correct": False,
             "why": "Five is right and the largest is not. The end-Permian "
                    "removed something like nine tenths of marine species, a "
                    "greater loss than the asteroid caused."},
            {"text": "Hundreds, because species have gone extinct throughout "
                     "Earth's history.",
             "correct": False,
             "why": "Species have gone extinct throughout Earth's history, at "
                    "a slow background rate. A mass extinction is a short "
                    "episode in which a very large share of species is lost, "
                    "and five of those are recorded."},
        ],
        "figure": None,
    },
    {
        "id": "b11-03-e07",
        "band": "easier",
        "text": "What ended the non-bird dinosaurs, and roughly when?",
        "options": [
            {"text": "A slow cooling of the climate, about six hundred "
                     "thousand years ago.",
             "correct": False,
             "why": "The date is far too recent and the cause too gradual. The "
                    "dinosaurs were gone tens of millions of years before "
                    "that."},
            {"text": "Hunting by early humans, about sixty-six thousand years "
                     "ago.",
             "correct": False,
             "why": "No human has ever seen a living non-bird dinosaur. They "
                    "died out about sixty-six million years ago, long before "
                    "our species existed."},
            {"text": "A disease that spread through them, about sixty-six "
                     "million years ago.",
             "correct": False,
             "why": "The date is right and the cause is not. The extinction "
                    "followed an asteroid impact, which is the event recorded "
                    "in the rocks."},
            {"text": "An asteroid impact, about sixty-six million years ago.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b11-03-e08",
        "band": "easier",
        "text": "Which is the commonest cause of extinction today?",
        "options": [
            {"text": "Hunting and collecting by people, for food, for "
                     "trade or as pests.",
             "correct": False,
             "why": "Hunting is a real cause and it is not the largest. It is "
                    "also the one pressure that a decision can switch off."},
            {"text": "Habitat loss, including the breaking up of what is left "
                     "into fragments.",
             "correct": True},
            {"text": "New diseases spreading between populations.",
             "correct": False,
             "why": "A disease can finish a small population with little "
                    "variation, and it accounts for far fewer losses than the "
                    "clearing of habitat."},
            {"text": "Volcanic eruptions and other natural disasters.",
             "correct": False,
             "why": "Those have caused extinctions in the deep past. What is "
                    "doing most of the damage now is the loss and "
                    "fragmentation of habitat."},
        ],
        "figure": None,
    },
    {
        "id": "b11-03-e09",
        "band": "easier",
        "text": "Why is a species that lives in only one small valley at "
                "particular risk?",
        "options": [
            {"text": "Because a small valley cannot hold enough food for a "
                     "species to survive.",
             "correct": False,
             "why": "It can hold plenty, and species live in small ranges for "
                    "long periods. The risk is what a single event in that one "
                    "valley would do."},
            {"text": "Because species that live in small places are always "
                     "specialists.",
             "correct": False,
             "why": "Many are, and that is not what makes a small range risky. "
                    "A generalist confined to one valley is in the same danger "
                    "from a single event."},
            {"text": "Because one event in that valley could remove the whole "
                     "species at once.",
             "correct": True},
            {"text": "Because a species in a small range cannot compete with "
                     "the species around it.",
             "correct": False,
             "why": "It competes there as well as anywhere. The problem is "
                    "that there is nowhere else holding a population if that "
                    "one is lost."},
        ],
        "figure": None,
    },
    {
        "id": "b11-03-e10",
        "band": "easier",
        "text": "Why does a slow breeding rate make a species more vulnerable "
                "when its environment changes?",
        "options": [
            {"text": "Change works through generations, and a slow breeder "
                     "gets very few of them before conditions change again.",
             "correct": True},
            {"text": "Slow breeders produce weaker young, and weak young "
                     "are what a population cannot afford when the "
                     "conditions change.",
             "correct": False,
             "why": "The young are not weaker, and a gap between litters does "
                    "not make a parent worse at it. What the species lacks is "
                    "numbers and generations, which are what replacing losses "
                    "and changing over time both need."},
            {"text": "Slow breeders need more food per animal than fast "
                     "breeders.",
             "correct": False,
             "why": "Food needs are set by size and habits rather than by "
                    "breeding rate. What matters here is how quickly losses "
                    "can be replaced."},
            {"text": "Slow breeders always live in smaller ranges.",
             "correct": False,
             "why": "They may or may not. Breeding rate and range are separate "
                    "risk factors, and a species can carry either without the "
                    "other."},
        ],
        "figure": None,
    },
    {
        "id": "b11-03-e11",
        "band": "easier",
        "text": "What does the term genetic variation mean?",
        "options": [
            {"text": "The number of different species living in one habitat.",
             "correct": False,
             "why": "That is a count of species. Genetic variation is measured "
                    "inside a single species, between the individuals of one "
                    "population."},
            {"text": "The way an individual's genes change during its life.",
             "correct": False,
             "why": "The genes an individual passes on do not change during "
                    "its life. Variation means the differences between one "
                    "individual and another."},
            {"text": "The differences between a species and its closest "
                     "relatives.",
             "correct": False,
             "why": "That is a comparison between species. Genetic variation "
                    "is about how different the members of one population are "
                    "from each other."},
            {"text": "The differences in genes between individuals in the same "
                     "population.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b11-03-e12",
        "band": "easier",
        "text": "Of the pressures that push a species towards extinction, "
                "which one can be removed by a decision?",
        "options": [
            {"text": "A new disease sweeping through the population.",
             "correct": False,
             "why": "A decision cannot call a disease off. What survives it "
                    "depends on whether resistance is already present in the "
                    "population."},
            {"text": "Hunting or collecting by people.",
             "correct": True},
            {"text": "A warming climate shifting the seasons.",
             "correct": False,
             "why": "The climate cannot be switched off by a single decision, "
                    "which is part of what makes it so hard a pressure to "
                    "manage."},
            {"text": "A predator that has already arrived and established "
                     "itself.",
             "correct": False,
             "why": "Removing an established predator is possible in a few "
                    "small places and is enormously difficult. Hunting is the "
                    "one that stops the moment people stop."},
        ],
        "figure": None,
    },
    {
        "id": "b11-03-e13",
        "band": "easier",
        "text": "A species has lived alongside foxes for thousands of years. A "
                "new predator, never seen there before, is introduced. Why is "
                "the new one so much more dangerous?",
        "options": [
            {"text": "Introduced predators are always larger and fiercer than "
                     "local ones.",
             "correct": False,
             "why": "Many are small. A stoat is a fraction of a fox's size and "
                    "has emptied whole islands, because nothing there had ever "
                    "had to deal with one."},
            {"text": "The local species has never had to compete with it for "
                     "food, so it loses out wherever the two of them "
                     "overlap.",
             "correct": False,
             "why": "A predator is not competing with its prey — it is eating "
                    "it. The danger is that the prey has no defence against "
                    "the way it hunts."},
            {"text": "The local species has no evolved defence against it, "
                     "because nothing like it has ever hunted them.",
             "correct": True},
            {"text": "New predators breed faster than the species already "
                     "living there.",
             "correct": False,
             "why": "Some do and many do not. What makes a new predator so "
                    "damaging is that its prey has no defence suited to it."},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "b11-03-s05",
        "band": "standard",
        "text": "A new disease sweeps through a large, varied population of "
                "brown rats. Numbers crash, and within a few years they are "
                "back to what they were. Explain how.",
        "options": [
            {"text": "The rats that survived built up resistance during the "
                     "outbreak and passed it to their young.",
             "correct": False,
             "why": "Resistance is not built up by surviving. The rats that "
                    "came through were already carrying it before the disease "
                    "arrived, and that is what their young inherited."},
            {"text": "Some rats already carried resistance, survived, and bred "
                     "the population back up.",
             "correct": True},
            {"text": "Rats breed so fast that the disease could not keep up "
                     "with the number being born.",
             "correct": False,
             "why": "Fast breeding is what makes the recovery quick, and it "
                    "does not prevent the crash. Something has to survive the "
                    "outbreak first, and that is a question about variation."},
            {"text": "The disease weakened over time until it stopped "
                     "affecting rats at all.",
             "correct": False,
             "why": "Nothing here says the disease changed. What changed is "
                    "that the rats left alive were the ones it could not "
                    "kill."},
        ],
        "figure": None,
    },
    {
        "id": "b11-03-s06",
        "band": "standard",
        "text": "A giant panda eats almost nothing but bamboo and lives in "
                "mountain forest. If the climate warms, the zone suitable for "
                "that bamboo shifts uphill. Why is the panda in trouble, given "
                "that it could walk uphill?",
        "options": [
            {"text": "Pandas cannot climb, so an uphill shift puts the bamboo "
                     "out of reach.",
             "correct": False,
             "why": "Pandas manage mountain slopes perfectly well. The problem "
                    "is what is or is not growing on those slopes when they "
                    "get there."},
            {"text": "Pandas would have to compete with the species already "
                     "living higher up.",
             "correct": False,
             "why": "Competition higher up is a real difficulty and not the "
                    "main one. A specialist can only follow its food if the "
                    "food can move, and bamboo moves slowly."},
            {"text": "The panda would adapt to a new food if it had to, so "
                     "this is not really a problem.",
             "correct": False,
             "why": "No animal adapts on demand. A panda cannot decide to eat "
                    "something else, and there is no reason to expect the "
                    "variation for it to be sitting in the population."},
            {"text": "Bamboo spreads slowly, and above a certain height the "
                     "mountains simply stop.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b11-03-s07",
        "band": "standard",
        "text": "The hazel dormouse is legally protected and nobody hunts it, "
                "and its numbers in England are still falling. What does that "
                "show?",
        "options": [
            {"text": "Removing one pressure does not touch the others — "
                     "habitat loss and fragmentation are still acting.",
             "correct": True},
            {"text": "That legal protection does not work and should not be "
                     "used anywhere, since the numbers fall "
                     "regardless.",
             "correct": False,
             "why": "It works on the pressure it addresses: the dormouse is "
                    "not being hunted. The decline has other causes, and "
                    "protection was never going to reach them."},
            {"text": "That the dormouse must be being hunted illegally.",
             "correct": False,
             "why": "There is no need to invent hunting to explain the "
                    "decline. Fragmented woodland, one small litter a year and "
                    "low variation are enough on their own."},
            {"text": "That hunting was never a serious pressure on any "
                     "species.",
             "correct": False,
             "why": "Hunting has driven many species to extinction. It simply "
                    "is not the pressure that is finishing this one."},
        ],
        "figure": None,
    },
    {
        "id": "b11-03-s08",
        "band": "standard",
        "text": "Herring gulls nest in dense colonies where a disease spreads "
                "very efficiently, and the species is still doing well. How "
                "can both of those be true?",
        "options": [
            {"text": "Diseases cannot really spread through a colony as easily "
                     "as it appears.",
             "correct": False,
             "why": "They spread very efficiently in dense colonies, which is "
                    "exactly why disease is the gull's weakest point. That "
                    "weakness is simply not enough to threaten the species."},
            {"text": "The gulls move away from a colony as soon as a disease "
                     "appears in it.",
             "correct": False,
             "why": "Colonies are not abandoned at the first sign of illness. "
                    "What carries the species through is what its population "
                    "holds, not where it goes."},
            {"text": "The population is large and varied enough to contain "
                     "resistant individuals, so it recovers.",
             "correct": True},
            {"text": "Gulls are large and aggressive, so they fight off "
                     "infection better than smaller birds.",
             "correct": False,
             "why": "Size and aggression have nothing to do with surviving an "
                    "infection. What decides that is whether the right "
                    "versions of genes are present in the population."},
        ],
        "figure": None,
    },
    {
        "id": "b11-03-s09",
        "band": "standard",
        "text": "A motorway is built through a wood, splitting it into two "
                "halves. Almost no trees are lost beyond the width of the "
                "road, and the animals concerned will not cross open tarmac. "
                "Why is this still a serious problem for them?",
        "options": [
            {"text": "It is not a serious problem, because almost no habitat "
                     "has been lost.",
             "correct": False,
             "why": "Almost no habitat has been lost and the population has "
                    "still been cut in two. Each half now loses variation on "
                    "its own and can be wiped out on its own."},
            {"text": "Each half is now a separate small population, losing "
                     "genetic variation with nothing arriving from the other.",
             "correct": True},
            {"text": "The noise of the traffic will drive the animals out of "
                     "both halves of the wood.",
             "correct": False,
             "why": "Disturbance is real and is not what makes fragmentation "
                    "so damaging. The damage is that two populations which "
                    "used to mix no longer can."},
            {"text": "Half the wood will now be too small to hold any animals "
                     "at all.",
             "correct": False,
             "why": "Both halves go on holding animals. The trouble is that "
                    "each half has only its own variation to draw on, and no "
                    "route for animals to arrive."},
        ],
        "figure": None,
    },
    {
        "id": "b11-03-s10",
        "band": "standard",
        "text": "A storm destroys most of the nesting sites used by two "
                "seabird species on the same cliff. One lays six eggs a year, "
                "the other one egg every two years. Ten years later one has "
                "recovered and the other has not. Which risk factor explains "
                "it?",
        "options": [
            {"text": "A specialist diet, since one of them must be fussier "
                     "about food.",
             "correct": False,
             "why": "Nothing has been said about their diets. What separates "
                    "them here is stated plainly — how quickly each can "
                    "replace what it lost."},
            {"text": "Low genetic variation, since one must have less of it "
                     "than the other.",
             "correct": False,
             "why": "Variation matters when a population has to cope with "
                    "something new. This population has to replace numbers, "
                    "and the speed of that is set by the breeding rate."},
            {"text": "A small range, since one of them nests only on that "
                     "cliff.",
             "correct": False,
             "why": "Both were nesting on that cliff. The difference you have "
                    "been given is the number of eggs each species lays."},
            {"text": "Slow reproduction — one species replaces its losses in a "
                     "year and the other takes decades.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b11-03-s11",
        "band": "standard",
        "text": "Aspirin came from willow bark, penicillin from a mould and "
                "the anticancer drug vincristine from the Madagascar "
                "periwinkle. What does that add to the argument for preventing "
                "extinctions?",
        "options": [
            {"text": "It shows that most extinct species would have turned out "
                     "to be medically useful.",
             "correct": False,
             "why": "There is no way to know that, and the argument does not "
                    "need it. The point is that whatever a species held cannot "
                    "be recovered once it is gone."},
            {"text": "It shows that a species can always be replaced by "
                     "another carrying the same compounds.",
             "correct": False,
             "why": "The opposite. Each species carries a genetic combination "
                    "that took millions of years to assemble and that nothing "
                    "else has."},
            {"text": "A species that dies out unstudied takes with it "
                     "compounds nothing else has.",
             "correct": True},
            {"text": "It shows that plants matter more than animals when "
                     "deciding what to protect.",
             "correct": False,
             "why": "Two of those examples happen to be plants and one is a "
                    "mould, and nothing in the argument ranks one group above "
                    "another."},
        ],
        "figure": None,
    },
    {
        "id": "b11-03-s12",
        "band": "standard",
        "text": "A survey finds a beetle species reduced to about two hundred "
                "individuals, all living in a single valley. Which two of the "
                "four risk factors does that description name directly?",
        "options": [
            {"text": "A small range, and low genetic variation.",
             "correct": True},
            {"text": "A specialist diet, and a small range.",
             "correct": False,
             "why": "Nothing has been said about what the beetle eats. What "
                    "the description gives you is where it lives and how few "
                    "of them there are."},
            {"text": "Slow reproduction, and low genetic variation.",
             "correct": False,
             "why": "No breeding rate has been mentioned. The two facts you "
                    "have are the size of the range and the size of the "
                    "population."},
            {"text": "A specialist diet, and slow reproduction.",
             "correct": False,
             "why": "Neither of those appears in the description. Two hundred "
                    "individuals in one valley tells you about range and about "
                    "how much variation is likely to be left."},
        ],
        "figure": None,
    },
    {
        "id": "b11-03-s13",
        "band": "standard",
        "text": "People have poisoned, trapped and hunted brown rats for "
                "centuries, and have never eliminated them anywhere without "
                "first removing their food and shelter. Which explanation "
                "fits?",
        "options": [
            {"text": "Rats have become resistant to every poison people have "
                     "ever used, so nothing on the shelf works on them "
                     "now.",
             "correct": False,
             "why": "Resistance to some poisons has appeared, and it is not "
                    "the whole story. Losses are also replaced almost as fast "
                    "as they are inflicted."},
            {"text": "They breed up to five times a year, eat anything and "
                     "live everywhere, so losses are replaced quickly.",
             "correct": True},
            {"text": "Rats are too strong and aggressive to be caught in any "
                     "numbers.",
             "correct": False,
             "why": "They are caught in enormous numbers. The trouble is that "
                    "a population breeding five times a year rebuilds what has "
                    "been taken."},
            {"text": "Hunting is never an effective pressure on any species.",
             "correct": False,
             "why": "Hunting has driven species to extinction, particularly "
                    "slow-breeding ones with small ranges. It fails here "
                    "because of what a rat population is like."},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "b11-03-h05",
        "band": "harder",
        "text": "Suppose the background extinction rate is about one species "
                "lost per million species each year, and that there are about "
                "eight million species alive. If the rate today is one hundred "
                "times the background rate, roughly how many species are being "
                "lost each year?",
        "options": [
            {"text": "8 species a year",
             "correct": False,
             "why": "That is the background rate applied to eight million "
                    "species. The question asks for one hundred times that, so "
                    "the eight still has to be multiplied."},
            {"text": "100 species a year",
             "correct": False,
             "why": "That is the multiplier written down as an answer. It has "
                    "to be applied to the background loss of eight species a "
                    "year."},
            {"text": "800 species a year",
             "correct": True},
            {"text": "8,000 species a year",
             "correct": False,
             "why": "That is a thousand times the background rate rather than "
                    "a hundred. Eight species a year multiplied by one hundred "
                    "gives eight hundred."},
        ],
        "figure": None,
    },
    {
        "id": "b11-03-h06",
        "band": "harder",
        "text": "A flightless rail lives on one Pacific island, eats one kind "
                "of land snail and lays two eggs a year. Rats arrive on a "
                "visiting ship. Which statement best explains why the species "
                "is in immediate danger?",
        "options": [
            {"text": "It is in danger only because rats have arrived; nothing "
                     "about the bird itself matters, since any species "
                     "would suffer the same.",
             "correct": False,
             "why": "The rats are the trigger and the bird's own properties "
                    "are why it cannot absorb them. One food, two eggs a year "
                    "and one island are three separate vulnerabilities."},
            {"text": "It carries three risk factors at once — one food, a very "
                     "slow breeding rate and a single small range.",
             "correct": True},
            {"text": "It is a specialist, and specialists always go extinct "
                     "when anything changes.",
             "correct": False,
             "why": "Specialists survive for as long as the thing they depend "
                    "on holds. What exposes this one is that slow breeding and "
                    "a single island leave it nothing to fall back on either."},
            {"text": "Being flightless is the risk factor, and the other "
                     "details do not matter.",
             "correct": False,
             "why": "Flightlessness is why the rats are so dangerous rather "
                    "than a risk factor in itself. The diet, the breeding rate "
                    "and the single island are three more."},
        ],
        "figure": None,
    },
    {
        "id": "b11-03-h07",
        "band": "harder",
        "text": "A bird species falls to forty individuals and is then bred "
                "back up to four thousand over twenty years, all descended "
                "from those forty. A newspaper reports that the species is now "
                "safe. What is the strongest reason for doubt?",
        "options": [
            {"text": "Four thousand is still too small a number for any "
                     "species to be safe.",
             "correct": False,
             "why": "Plenty of species live safely at that number and smaller. "
                    "What matters is not the count but how much variation "
                    "those four thousand hold between them."},
            {"text": "The population will crash again, because a species that "
                     "has fallen once always does.",
             "correct": False,
             "why": "Nothing makes a second crash automatic. The concern is "
                    "what the population would have to draw on if one came."},
            {"text": "Birds bred in captivity will not know how to live in the "
                     "wild.",
             "correct": False,
             "why": "That is a real difficulty for released animals and is not "
                    "what this turns on. Even birds raised perfectly would "
                    "carry only the variation the forty founders had."},
            {"text": "The numbers recovered but the variation did not — all "
                     "four thousand descend from forty.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b11-03-h08",
        "band": "harder",
        "text": "A tree species survives only as thirty individuals in botanic "
                "gardens, with none left growing wild. Is it extinct?",
        "options": [
            {"text": "No — extinction means the last individual has died, and "
                     "thirty are alive.",
             "correct": True},
            {"text": "Yes, because a species that no longer lives in the wild "
                     "has been lost.",
             "correct": False,
             "why": "It has been lost from the wild, which is a serious thing "
                    "and is not extinction. Extinction is permanent, and "
                    "thirty living trees can still be planted out."},
            {"text": "Yes, because thirty individuals cannot be a real "
                     "population.",
             "correct": False,
             "why": "Thirty is a dangerously small number and it is not zero. "
                    "The species is at severe risk, which is a different "
                    "statement from being gone."},
            {"text": "No, and it is in no real danger, because the gardens "
                     "will keep it going.",
             "correct": False,
             "why": "The gardens keep individuals alive; they do not keep a "
                    "population varying and evolving. Thirty related trees "
                    "hold very little of what the species once had."},
        ],
        "figure": None,
    },
    {
        "id": "b11-03-h09",
        "band": "harder",
        "text": "One insect feeds only on nettles, which grow almost "
                "everywhere in Britain and are spreading. Another feeds only "
                "on a rare orchid found in three meadows. Both are "
                "specialists. Are both at equal risk?",
        "options": [
            {"text": "Yes — a specialist diet is a risk factor, and both of "
                     "them are specialists.",
             "correct": False,
             "why": "The risk of a specialist diet depends entirely on what "
                    "happens to the one food. Nettles are everywhere and "
                    "spreading; the orchid is in three meadows."},
            {"text": "No — a specialist is only at risk if the thing it "
                     "depends on is itself at risk.",
             "correct": True},
            {"text": "No — the nettle feeder is at greater risk, because "
                     "common foods attract more competitors.",
             "correct": False,
             "why": "Competition for an abundant food is not what threatens "
                    "either insect. What matters is whether the food will "
                    "still be there, and nettles will be."},
            {"text": "Yes, because any species that cannot switch foods will "
                     "run out of them eventually.",
             "correct": False,
             "why": "There is no eventually about it. A food that is abundant "
                    "and spreading is not running out, and the insect that "
                    "depends on it is in no immediate trouble."},
        ],
        "figure": None,
    },
    {
        "id": "b11-03-h10",
        "band": "harder",
        "text": "How can anyone know that most of the species that have ever "
                "lived died out long before humans existed?",
        "options": [
            {"text": "Because the species alive today could not have supported "
                     "that many others.",
             "correct": False,
             "why": "Nothing about today's species tells you what lived in the "
                    "past. The evidence comes from rocks, not from arithmetic "
                    "on the present."},
            {"text": "Because written records go back far enough to cover it.",
             "correct": False,
             "why": "Writing is a few thousand years old and the losses in "
                    "question are hundreds of millions. Records of that age "
                    "are made of rock, not of paper."},
            {"text": "Because fossils of enormous numbers of species are found "
                     "in rock layers and never in the layers above.",
             "correct": True},
            {"text": "Because living species can be compared to work out which "
                     "ones are missing from the family tree they "
                     "form.",
             "correct": False,
             "why": "Comparing living species shows how they are related, not "
                    "what has vanished. A species that left no living "
                    "relatives would be invisible to that method, and fossils "
                    "are what reveal it."},
        ],
        "figure": None,
    },
    {
        "id": "b11-03-h11",
        "band": "harder",
        "text": "The same new disease reaches two populations of one species: "
                "five thousand animals in a continuous forest, and sixty in an "
                "isolated fragment. What should you predict for each, and why?",
        "options": [
            {"text": "Both are likely to be wiped out, since neither has met "
                     "the disease before.",
             "correct": False,
             "why": "Meeting it for the first time is true of both and is not "
                    "what decides the outcome. What decides it is whether "
                    "resistant individuals happen to be present."},
            {"text": "The small population survives better, because a disease "
                     "spreads more slowly among fewer animals.",
             "correct": False,
             "why": "Slower spread does not save a population with nobody "
                    "resistant in it. It is far more likely that the sixty "
                    "carry no resistance at all."},
            {"text": "Both recover, because populations always rebuild after a "
                     "disease has passed through.",
             "correct": False,
             "why": "Populations rebuild only from survivors. A population "
                    "with no resistant individuals has none to rebuild from, "
                    "which is how a disease finishes a species."},
            {"text": "The large one probably contains resistant individuals "
                     "and recovers; the small one may have none.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b11-03-h12",
        "band": "harder",
        "text": "The caterpillars of one butterfly eat the leaves of a single "
                "plant, and they hatch just as those leaves appear. After "
                "several warm springs the plant comes into leaf three weeks "
                "earlier while the butterflies still hatch at the old time. "
                "What is the problem, and why does it hit a specialist "
                "hardest?",
        "options": [
            {"text": "The caterpillars hatch after their only food has "
                     "toughened, and there is nothing else they can eat.",
             "correct": True},
            {"text": "The plant will die out, and the butterflies with it.",
             "correct": False,
             "why": "The plant is doing well — it is leafing earlier, not "
                    "failing. The trouble is that the two events no longer "
                    "line up."},
            {"text": "The butterflies will hatch earlier next year in order to "
                     "match the plant, because the species needs the "
                     "two to line up.",
             "correct": False,
             "why": "An insect cannot move its hatching date to suit its food. "
                    "Whether the population's timing shifts depends on which "
                    "butterflies leave offspring, and that takes generations."},
            {"text": "Warmer springs harm caterpillars directly, whatever they "
                     "eat.",
             "correct": False,
             "why": "The warmth itself is not the problem here. What has "
                    "changed is the timing of the food, and a generalist with "
                    "other plants to eat would barely notice."},
        ],
        "figure": None,
    },
    {
        "id": "b11-03-h13",
        "band": "harder",
        "text": "A polluted river can be cleaned up and its fish will return. "
                "Why is extinction treated differently from other kinds of "
                "environmental damage?",
        "options": [
            {"text": "Because extinction is caused by people and pollution is "
                     "not.",
             "correct": False,
             "why": "Pollution is caused by people too, and most extinctions "
                    "in Earth's history were not. What separates them is "
                    "whether the damage can be undone."},
            {"text": "Because a species that is gone cannot be brought back — "
                     "no de-extinction project has restored a working "
                     "population.",
             "correct": True},
            {"text": "Because extinction happens much faster than pollution "
                     "does.",
             "correct": False,
             "why": "Speed is not what makes it different. A species can "
                    "decline over centuries and still be lost for good at the "
                    "end of it."},
            {"text": "Because a polluted river affects only one place, while "
                     "extinction affects the whole world, which makes "
                     "it a much bigger problem in every case.",
             "correct": False,
             "why": "A local extinction affects one place too, and a river can "
                    "be poisoned along hundreds of miles. The difference is "
                    "that one can be reversed and the other cannot."},
        ],
        "figure": None,
    },
]
