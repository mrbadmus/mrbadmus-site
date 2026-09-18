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
                     "it does, from feeding to breeding.",
             "correct": False,
             "why": "A generalist is rarely the best at anything. It is very "
                    "hard to get rid of, which is a different quality "
                    "altogether."},
            {"text": "A species that breeds faster than the species around "
                     "it.",
             "correct": False,
             "why": "Fast breeding often goes with being a generalist and is "
                    "not what the word means. Generalist describes the range "
                    "of foods and places a species can use."},
            {"text": "A species that can use many different foods and live in "
                     "many places.",
             "correct": True},
            {"text": "A species that has spread well beyond the region it "
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
            {"text": "The number of different species living alongside one "
                     "another in a single habitat.",
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
                     "living relatives.",
             "correct": False,
             "why": "That is a comparison between species. Genetic variation "
                    "is about how different the members of one population are "
                    "from each other."},
            {"text": "Differences in genes between individuals in the same "
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
            {"text": "It is not a serious problem, because almost none of the "
                     "habitat has been lost.",
             "correct": False,
             "why": "Almost no habitat has been lost and the population has "
                    "still been cut in two. Each half now loses variation on "
                    "its own and can be wiped out on its own."},
            {"text": "Each half is now a small isolated population, losing "
                     "genetic variation.",
             "correct": True},
            {"text": "The noise and the light from the traffic will drive the "
                     "animals out of both halves of the wood.",
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
            {"text": "A specialist diet, since one of the two species must be "
                     "fussier about its food.",
             "correct": False,
             "why": "Nothing has been said about their diets. What separates "
                    "them here is stated plainly — how quickly each can "
                    "replace what it lost."},
            {"text": "Low genetic variation, since one of the two must have "
                     "far less of it than the other one does.",
             "correct": False,
             "why": "Variation matters when a population has to cope with "
                    "something new. This population has to replace numbers, "
                    "and the speed of that is set by the breeding rate."},
            {"text": "A small range, since one of them nests only on that "
                     "cliff.",
             "correct": False,
             "why": "Both were nesting on that cliff. The difference you have "
                    "been given is the number of eggs each species lays."},
            {"text": "Slow reproduction — one replaces its losses in a year, "
                     "the other in decades.",
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
    # ── easier · the MRB-338 expansion ──────────────────────────────────
    {
        "id": "b11-03-e14",
        "band": "easier",
        "text": "Biologists call one species a specialist. What does that "
                "word tell you about it?",
        "options": [
            {"text": "It is unusually good at surviving, which is how it came "
                     "by the name.",
             "correct": False,
             "why": "It is usually very good at one particular thing. That is "
                    "not the same as being good at surviving, and it is often "
                    "the opposite."},
            {"text": "It is found in only one country, and nowhere else in "
                     "the world.",
             "correct": False,
             "why": "That describes a small range, which is a separate risk "
                    "factor. A specialist can be found over a wide area if "
                    "what it depends on is."},
            {"text": "It depends on one food, one habitat or one narrow set "
                     "of conditions, and has nothing to fall back on.",
             "correct": True},
            {"text": "It has been studied by specialists, so more is known "
                     "about it than about most species.",
             "correct": False,
             "why": "The word describes the animal or plant, not the people "
                    "studying it. It is about what the species depends on."},
        ],
        "figure": None,
    },
    {
        "id": "b11-03-e15",
        "band": "easier",
        "text": "A hazel dormouse has one small litter a year. Why does that "
                "make life harder for the species when something goes wrong "
                "in its wood?",
        "options": [
            {"text": "Losses are replaced very slowly, so the population takes "
                     "years to build back up.",
             "correct": True},
            {"text": "A small litter means each young dormouse is weaker than "
                     "one from a large litter.",
             "correct": False,
             "why": "A small litter usually means better fed young, not "
                    "weaker ones. The difficulty is in how few of them there "
                    "are each year."},
            {"text": "Breeding only once a year means the young are all born "
                     "at the wrong time of year.",
             "correct": False,
             "why": "Dormice breed when their food is available. The problem "
                    "is the number of chances they get, not their timing."},
            {"text": "One litter a year means the parents cannot teach their "
                     "young enough to survive alone.",
             "correct": False,
             "why": "Teaching is not what is short here. What is short is the "
                    "number of young the species can produce while conditions "
                    "are against it."},
        ],
        "figure": None,
    },
    {
        "id": "b11-03-e16",
        "band": "easier",
        "text": "A giant panda eats bamboo and almost nothing else. Its "
                "mountain forest is being cleared for farmland. Why does its "
                "diet make the clearing so serious for it?",
        "options": [
            {"text": "Bamboo is the least nutritious plant in the forest, so "
                     "the panda has to eat a great deal of it.",
             "correct": False,
             "why": "A panda does eat a great deal of bamboo, and that is a "
                    "separate difficulty. The danger here is having no other "
                    "food to turn to."},
            {"text": "Pandas cannot digest anything other than bamboo, "
                     "because their gut is that of a plant-eater.",
             "correct": False,
             "why": "A panda's gut is actually that of a meat-eater, and it "
                    "will take other food occasionally. What it cannot do is "
                    "live on anything else."},
            {"text": "Bamboo grows back too quickly for the forest to be "
                     "cleared properly.",
             "correct": False,
             "why": "Fast regrowth would help a panda rather than harm it. "
                    "Bamboo is in fact slow to spread into new ground."},
            {"text": "There is nothing else it can live on, so losing the "
                     "bamboo means losing everything.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b11-03-e17",
        "band": "easier",
        "text": "A brown rat can have up to five litters a year. How does "
                "that help the species after a poisoning campaign cuts its "
                "numbers?",
        "options": [
            {"text": "It means the rats that survive are the strongest, "
                     "because only strong rats breed that often.",
             "correct": False,
             "why": "Breeding rate is a feature of the species, not a test "
                    "any individual has passed. What matters is how fast the "
                    "numbers come back."},
            {"text": "The survivors can replace the lost numbers within a "
                     "season or two.",
             "correct": True},
            {"text": "It means the poison is diluted between more rats, so "
                     "each one gets a smaller dose.",
             "correct": False,
             "why": "Poison is eaten by individual rats in whatever amount "
                    "they find. Numbers do not share a dose out between "
                    "them."},
            {"text": "The rats can move to another barn before the next "
                     "poisoning begins.",
             "correct": False,
             "why": "Moving is something a generalist can do, and it is a "
                    "different advantage. Breeding rate is about how quickly "
                    "losses are made up."},
        ],
        "figure": None,
    },
    {
        "id": "b11-03-e18",
        "band": "easier",
        "text": "A herring gull will eat fish, waste, chips and almost "
                "anything else, and is found on coasts and in towns across "
                "the northern hemisphere. What does that description make it?",
        "options": [
            {"text": "A specialist, because it has learned to live on one "
                     "reliable food supply from people.",
             "correct": False,
             "why": "Chips are one of very many things it eats. A specialist "
                    "depends on one food, and this bird depends on none in "
                    "particular."},
            {"text": "A generalist, able to use many different foods and live in "
                     "many different places.",
             "correct": True},
            {"text": "An introduced species, since it has spread into towns "
                     "where it did not used to live.",
             "correct": False,
             "why": "Nobody brought it to those towns; it moved in by itself. "
                    "An introduced species is one people carried to a place "
                    "it had never reached."},
            {"text": "A species with a small range, because it is only ever "
                     "found near the sea.",
             "correct": False,
             "why": "Its range covers coasts and towns right across the "
                    "northern hemisphere, which is about as far from a small "
                    "range as a bird gets."},
        ],
        "figure": None,
    },
    {
        "id": "b11-03-e19",
        "band": "easier",
        "text": "One of the four risk factors is a small or fragmented range. "
                "What does a species' range mean?",
        "options": [
            {"text": "The number of foods it can live on.",
             "correct": False,
             "why": "That is its diet, and being narrow about it is a "
                    "different risk factor. Range is about where a species is "
                    "found."},
            {"text": "The difference between the largest and smallest "
                     "individuals of the species.",
             "correct": False,
             "why": "That is one kind of variation within a population. Range "
                    "here is a geographical word, not a measurement of "
                    "bodies."},
            {"text": "The area of ground or water over which the species is "
                     "found.",
             "correct": True},
            {"text": "The number of years a population has been living in one "
                     "particular place.",
             "correct": False,
             "why": "How long it has been there is not the point. What "
                    "matters is how much ground the species covers now."},
        ],
        "figure": None,
    },
    {
        "id": "b11-03-e20",
        "band": "easier",
        "text": "A wildlife report says a habitat has been fragmented. What "
                "has happened to it?",
        "options": [
            {"text": "What is left of it has been broken into separate "
                     "patches that populations cannot move between.",
             "correct": True},
            {"text": "It has been damaged so badly that nothing can live in "
                     "it at all.",
             "correct": False,
             "why": "The patches are usually good habitat still. The problem "
                    "is that they are cut off from one another."},
            {"text": "Several different habitats have been mixed together in "
                     "one place, leaving one larger one.",
             "correct": False,
             "why": "Fragmenting breaks one habitat up rather than blending "
                    "several. Nothing has been added to it."},
            {"text": "It has been made smaller, and nothing else has changed "
                     "about it.",
             "correct": False,
             "why": "Losing area is part of it, and the separation is the "
                    "part that does the extra damage — each patch is now on "
                    "its own."},
        ],
        "figure": None,
    },
    {
        "id": "b11-03-e21",
        "band": "easier",
        "text": "The extinction at the end of the Permian is the largest in "
                "the fossil record. Roughly how much of life in the sea did "
                "it remove?",
        "options": [
            {"text": "About one species in ten.",
             "correct": False,
             "why": "That is nearer an ordinary bad stretch than a mass "
                    "extinction. The end-Permian removed the great majority "
                    "of sea species, not a tenth of them."},
            {"text": "About nine species in every ten.",
             "correct": True},
            {"text": "Only the largest animals, and nothing smaller.",
             "correct": False,
             "why": "Losses ran right through the sizes, from large animals "
                    "down to very small ones. Size is not what decided it."},
            {"text": "About half of all the species in the sea.",
             "correct": False,
             "why": "Half would be an enormous loss and it is still well "
                    "short. This event is the largest of the five for a "
                    "reason."},
        ],
        "figure": None,
    },
    {
        "id": "b11-03-e22",
        "band": "easier",
        "text": "How does the rate at which species are being lost today "
                "compare with the background rate?",
        "options": [
            {"text": "It is about the same, which is why the background rate "
                     "is worked out at all.",
             "correct": False,
             "why": "The background rate is worked out so that today's can be "
                    "compared against it, and the comparison shows a large "
                    "gap rather than a match."},
            {"text": "It is lower, because so many species are now protected "
                     "by law.",
             "correct": False,
             "why": "Protection helps particular species. Across the world "
                    "the rate of loss is well above the background level, not "
                    "below it."},
            {"text": "It is estimated at tens to hundreds of times the "
                     "background rate.",
             "correct": True},
            {"text": "It cannot be compared, because nobody has any idea how "
                     "fast species were lost in the past.",
             "correct": False,
             "why": "The fossil record gives an estimate of the background "
                    "rate, which is exactly what makes the comparison "
                    "possible."},
        ],
        "figure": None,
    },
    {
        "id": "b11-03-e23",
        "band": "easier",
        "text": "A species is described as extinct in the wild. What does "
                "that mean?",
        "options": [
            {"text": "Its last individual died some years ago, and the phrase "
                     "is simply a polite way of saying so.",
             "correct": False,
             "why": "Extinct in the wild means some are still alive. Once the "
                    "last individual anywhere has died, the species is "
                    "extinct without qualification."},
            {"text": "Its numbers in the wild are falling and are expected to "
                     "reach zero soon.",
             "correct": False,
             "why": "That describes a species in serious trouble but still "
                    "present. Extinct in the wild means there are none left "
                    "outside human care."},
            {"text": "None are left outside human care, though some survive "
                     "in zoos or gardens.",
             "correct": True},
            {"text": "It lives only in places people have never visited, so "
                     "nobody has counted it.",
             "correct": False,
             "why": "An uncounted species is simply unstudied. This phrase is "
                    "about where the surviving individuals are, and they are "
                    "all in human hands."},
        ],
        "figure": None,
    },
    {
        "id": "b11-03-e24",
        "band": "easier",
        "text": "Kakapo breed only in the years when a particular tree fruits "
                "heavily, which can be two to four years apart, and they lay "
                "very few eggs. Which risk factor is that?",
        "options": [
            {"text": "Slow reproduction — very few young, and not in every "
                     "year.",
             "correct": True},
            {"text": "A small or fragmented range, since the birds can only "
                     "breed near those trees.",
             "correct": False,
             "why": "Range is about how much ground a species covers. What is "
                    "described here is how rarely it can breed at all."},
            {"text": "Low genetic variation, because so few birds are "
                     "involved in each breeding year.",
             "correct": False,
             "why": "Low variation may follow in time, and the feature "
                    "described is the breeding rate itself — how seldom the "
                    "species gets a generation."},
            {"text": "A specialist diet built around one tree.",
             "correct": False,
             "why": "The tree sets when they breed rather than what they eat. "
                    "This is the reproduction risk factor, not the diet one."},
        ],
        "figure": None,
    },
    {
        "id": "b11-03-e25",
        "band": "easier",
        "text": "One species is found right across several countries. Why "
                "does that usually let it survive a disaster in one place?",
        "options": [
            {"text": "Because a disaster in one part of the range leaves "
                     "populations everywhere else untouched.",
             "correct": True},
            {"text": "Because a species spread over several countries is "
                     "protected by the laws of more than one government.",
             "correct": False,
             "why": "Protection is a separate matter and does not always "
                    "follow. The safety comes from the event reaching only "
                    "part of the species."},
            {"text": "Because animals from the other countries come to "
                     "replace the ones that died.",
             "correct": False,
             "why": "Some species do recolonise, and many cannot move that "
                    "far. The species survives because it was never all in "
                    "one place."},
            {"text": "Because a wide range means each population is larger "
                     "than it would otherwise be.",
             "correct": False,
             "why": "A wide range may be made up of many small populations. "
                    "What matters is that no single event reaches all of "
                    "them."},
        ],
        "figure": None,
    },
    {
        "id": "b11-03-e26",
        "band": "easier",
        "text": "What is a mass extinction?",
        "options": [
            {"text": "The loss of every last member of one single species in "
                     "a short space of time, which is what makes it a mass "
                     "one.",
             "correct": False,
             "why": "That is an ordinary extinction, however fast it "
                    "happened. A mass extinction takes down a great many "
                    "species at once."},
            {"text": "An episode in which a very large share of the world's "
                     "species dies out in a short stretch of geological time.",
             "correct": True},
            {"text": "The loss of all the large animals from one continent.",
             "correct": False,
             "why": "That would be a serious loss and still a local one. A "
                    "mass extinction is worldwide and is not limited to large "
                    "animals."},
            {"text": "A period when far more species are appearing than dying "
                     "out.",
             "correct": False,
             "why": "That is the opposite of an extinction. Species do appear "
                    "in large numbers after one, over millions of years."},
        ],
        "figure": None,
    },
    {
        "id": "b11-03-e27",
        "band": "easier",
        "text": "On the account of the five pressures, where do the new "
                "predators that arrive in a habitat usually come from?",
        "options": [
            {"text": "They evolve on the spot from a species that was already "
                     "living there.",
             "correct": False,
             "why": "A predator that grew up alongside its prey is not a new "
                    "predator in this sense. The dangerous ones arrive from "
                    "somewhere else entirely."},
            {"text": "They arrive by themselves, walking or flying in from a "
                     "neighbouring country.",
             "correct": False,
             "why": "Some species do spread on their own. The ones this "
                    "lesson is concerned with were carried to places they "
                    "could never have reached."},
            {"text": "They are brought by people, usually by accident.",
             "correct": True},
            {"text": "They are released to control a pest.",
             "correct": False,
             "why": "That has happened and has gone badly, and it is one "
                    "route among several. Most arrivals are accidental, on "
                    "ships and in cargo."},
        ],
        "figure": None,
    },
    {
        "id": "b11-03-e28",
        "band": "easier",
        "text": "As the climate warms, the zone in which a species can live "
                "shifts. In which two directions does it usually move?",
        "options": [
            {"text": "Downhill and towards the equator, where it is warmer.",
             "correct": False,
             "why": "That is the wrong way for both. A species tracking "
                    "cooler conditions has to move away from the warmth, not "
                    "towards it."},
            {"text": "Towards the poles, and uphill into the mountains.",
             "correct": True},
            {"text": "Eastwards and westwards, following the way the weather "
                     "travels.",
             "correct": False,
             "why": "Weather systems do travel that way. The zone a species "
                    "can live in is set by temperature, which changes with "
                    "latitude and with height."},
            {"text": "Towards the coast, where the sea keeps temperatures "
                     "steady.",
             "correct": False,
             "why": "Coasts do have steadier temperatures, and that is not "
                    "the general pattern. The suitable zone moves polewards "
                    "and upwards as it warms."},
        ],
        "figure": None,
    },
    {
        "id": "b11-03-e29",
        "band": "easier",
        "text": "Hazel dormice hibernate through the winter. Why is a mild "
                "winter a problem for them?",
        "options": [
            {"text": "A mild winter means fewer hazelnuts, so there is less "
                     "for them to eat when they wake.",
             "correct": False,
             "why": "Nut crops depend mostly on the previous summer. The "
                    "difficulty with a mild winter is what it does while the "
                    "animal is asleep."},
            {"text": "Warmth interrupts the hibernation, burning fat reserves "
                     "the animal cannot replace until spring.",
             "correct": True},
            {"text": "A mild winter lets their predators stay active, so more "
                     "dormice are taken while they sleep.",
             "correct": False,
             "why": "Predators are a pressure in their own right. The problem "
                    "described here is inside the dormouse, in the fat it is "
                    "living on."},
            {"text": "Mild weather makes them breed in winter, and the young "
                     "die of cold.",
             "correct": False,
             "why": "Dormice do not breed in the middle of winter. What the "
                    "warmth does is wake them when there is nothing to eat."},
        ],
        "figure": None,
    },
    {
        "id": "b11-03-e30",
        "band": "easier",
        "text": "Of all the species that have ever lived on Earth, roughly "
                "what share are still alive today?",
        "options": [
            {"text": "About half of them.",
             "correct": False,
             "why": "Nothing like that many. The great majority of species "
                    "that have ever existed died out long before there were "
                    "any people."},
            {"text": "About nine in every ten of them.",
             "correct": False,
             "why": "That is close to the reverse of the real figure. It is "
                    "the extinct ones that run to nine in ten and beyond."},
            {"text": "Fewer than one in a hundred.",
             "correct": True},
            {"text": "About one in five of them.",
             "correct": False,
             "why": "Still far too many. Extinction is the ordinary end of a "
                    "species, and almost every species there has ever been "
                    "has reached it."},
        ],
        "figure": None,
    },
    # ── standard · the MRB-338 expansion ────────────────────────────────
    {
        "id": "b11-03-s14",
        "band": "standard",
        "text": "Two seabirds nest on the same stretch of British coast. One "
                "eats fish, waste and scraps and will nest on a building as "
                "readily as on a cliff; the other eats only sandeels and "
                "nests only on bare cliff ledges. A harbour development "
                "removes half the cliff. Which is more at risk, and why?",
        "options": [
            {"text": "The generalist, because a bird that spreads itself "
                     "across many foods never gets enough of any one of them "
                     "to cope with a loss.",
             "correct": False,
             "why": "Using many foods is the safe position, not a thin one. "
                    "Losing one of them leaves a generalist with everything "
                    "else it was already eating."},
            {"text": "The sandeel feeder, because it has one food and one "
                     "nesting place and cannot swap either for something "
                     "else.",
             "correct": True},
            {"text": "Neither, because both lose the same area of cliff, so "
                     "both lose exactly the same amount of the habitat they "
                     "depend on.",
             "correct": False,
             "why": "The same area lost is not the same loss. One bird has "
                    "other food and other nest sites to fall back on and the "
                    "other has none."},
            {"text": "The generalist, because a bird willing to nest on a "
                     "building has already given up the cliff and has nowhere "
                     "left to return to.",
             "correct": False,
             "why": "Being able to use a building is an extra option, not a "
                    "lost one. The cliff is still available to it as well."},
        ],
        "figure": None,
    },
    {
        "id": "b11-03-s15",
        "band": "standard",
        "text": "Two small woods each hold a separate population of one "
                "beetle. A conservation team plants a strip of woodland "
                "joining them. Why does that help more than adding the same "
                "area to one wood alone?",
        "options": [
            {"text": "Beetles can now move between the two, so the "
                     "populations breed as one and share their variation.",
             "correct": True},
            {"text": "A longer wood holds more beetles per hectare than a "
                     "round one of the same size.",
             "correct": False,
             "why": "Shape does not change how many beetles a hectare feeds. "
                    "What the strip changes is whether the two populations "
                    "can reach each other."},
            {"text": "The strip gives the beetles somewhere to shelter when "
                     "the weather in both woods is bad.",
             "correct": False,
             "why": "A narrow strip is the most exposed part of the whole "
                    "wood. Its value is as a route, not as shelter."},
            {"text": "Predators avoid narrow strips of woodland, so the "
                     "beetles are safer there.",
             "correct": False,
             "why": "Narrow strips are if anything easier for a predator to "
                    "work along. The gain is that two isolated populations "
                    "become one."},
        ],
        "figure": None,
    },
    {
        "id": "b11-03-s16",
        "band": "standard",
        "text": "Kakapo fell to 51 birds. Every living kakapo is now named, "
                "radio-tagged and monitored, and numbers are slowly climbing. "
                "What does that tell you about recovery?",
        "options": [
            {"text": "That recovery is impossible once a population has "
                     "fallen that far.",
             "correct": False,
             "why": "Numbers are climbing, so it is plainly not impossible. "
                    "What the account shows is what it takes."},
            {"text": "That a population recovers by itself once hunting and "
                     "habitat loss have been stopped.",
             "correct": False,
             "why": "Stopping the pressures is necessary and was not enough "
                    "here. Every individual bird needs watching for the "
                    "numbers to move at all."},
            {"text": "That recovery is possible, and costs constant work on "
                     "every single individual.",
             "correct": True},
            {"text": "That the species would have recovered anyway, and the "
                     "monitoring only records what happens.",
             "correct": False,
             "why": "The monitoring is part of the management — nests are "
                    "guarded and birds are fed. It is not a study carried out "
                    "from a distance."},
        ],
        "figure": None,
    },
    {
        "id": "b11-03-s17",
        "band": "standard",
        "text": "Three insects live in one valley. One feeds on fifty kinds "
                "of plant, one on three, one on a single kind. A drought "
                "kills half the plant species in the valley. Rank their risk.",
        "options": [
            {"text": "All three are at the same risk, because the drought "
                     "affects the whole valley.",
             "correct": False,
             "why": "The drought is the same for all three; what differs is "
                    "how much each of them can afford to lose."},
            {"text": "The fifty-plant feeder is at most risk, because it "
                     "depends on more plants than the others.",
             "correct": False,
             "why": "Depending on more plants is the safe position. Losing "
                    "half of fifty still leaves twenty-five it can eat."},
            {"text": "The three-plant feeder is at most risk, because three "
                     "plants is the fewest any insect can manage on.",
             "correct": False,
             "why": "There is nothing special about three. The insect in most "
                    "danger is the one whose only food may be among the "
                    "losses."},
            {"text": "The single-plant feeder is at most risk, then the "
                     "three-plant feeder, with the fifty-plant feeder safest "
                     "of the three.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b11-03-s18",
        "band": "standard",
        "text": "Rats reach a remote island on a ship. The seabirds that nest "
                "there lay their eggs in scrapes on open ground. Why does "
                "that nesting habit make them so vulnerable?",
        "options": [
            {"text": "Eggs on open ground are colder than eggs in a nest, so "
                     "fewer of them hatch.",
             "correct": False,
             "why": "These birds sit on their eggs and keep them warm "
                    "perfectly well. The change is what can now reach them."},
            {"text": "Ground nests are harder for the parents to find again "
                     "than nests in a tree.",
             "correct": False,
             "why": "Seabirds return to the same scrape without difficulty. "
                    "The danger comes from an animal that was never there "
                    "before."},
            {"text": "The island had no ground predator before, so nothing "
                     "about the birds' nesting protects the eggs from one.",
             "correct": True},
            {"text": "Rats prefer eggs to any other food, so they seek out "
                     "seabird colonies wherever in the world they land.",
             "correct": False,
             "why": "Rats eat almost anything and take eggs because they are "
                    "easy to reach. The problem is on the birds' side, not in "
                    "any preference."},
        ],
        "figure": None,
    },
    {
        "id": "b11-03-s19",
        "band": "standard",
        "text": "Rhino horn sells for very large sums. Why is a species "
                "hunted for a valuable product particularly hard to protect, "
                "even where the hunting is illegal?",
        "options": [
            {"text": "The reward for killing one animal stays high however "
                     "few are left, and rarity pushes the price up further.",
             "correct": True},
            {"text": "Illegal hunting cannot be punished, so there is nothing "
                     "to stop anybody doing it.",
             "correct": False,
             "why": "It is punished, sometimes severely. The difficulty is "
                    "that the money on offer outweighs the risk for the "
                    "person taking it."},
            {"text": "Animals with a valuable product are always slow "
                     "breeders, so hunting hits them harder.",
             "correct": False,
             "why": "Many are slow breeders and that is a separate risk "
                    "factor. The difficulty here is the price the product "
                    "commands."},
            {"text": "A hunted species learns to avoid people, which makes it "
                     "impossible for anyone to count or to guard.",
             "correct": False,
             "why": "Counting a wary animal is difficult and it is not the "
                    "main obstacle. The obstacle is how much a horn is worth "
                    "to whoever takes it."},
        ],
        "figure": None,
    },
    {
        "id": "b11-03-s20",
        "band": "standard",
        "text": "A fish stock is fished until about two in every hundred are "
                "left, and then all fishing stops. Twenty years later it has "
                "not recovered. Give the best reason the pause alone was not "
                "enough.",
        "options": [
            {"text": "Fish stocks always take longer than twenty years to "
                     "recover, whatever is done, because a fished sea never "
                     "refills.",
             "correct": False,
             "why": "Some stocks have come back inside twenty years. This one "
                    "has not, and the question is what is different about it."},
            {"text": "The fishing boats went on taking the same fish "
                     "somewhere else in the ocean.",
             "correct": False,
             "why": "Nothing in the account says so, and it would be a "
                    "continuing pressure rather than a reason the pause "
                    "failed where it applied."},
            {"text": "A population reduced that far is small, short of "
                     "variation, and still facing everything else that was "
                     "acting on it.",
             "correct": True},
            {"text": "The remaining fish are the oldest ones, and old fish "
                     "cannot breed.",
             "correct": False,
             "why": "Fishing usually removes the largest and oldest first, so "
                    "what is left is young. Age is not what is holding the "
                    "recovery back."},
        ],
        "figure": None,
    },
    {
        "id": "b11-03-s21",
        "band": "standard",
        "text": "Extinction has gone on throughout Earth's history. Why do "
                "biologists still treat today's losses as an emergency?",
        "options": [
            {"text": "Because the species being lost now are more useful to "
                     "people than the ones lost in the past.",
             "correct": False,
             "why": "Usefulness is not the measure, and nobody knows what the "
                    "species of the past could have offered. The concern is "
                    "about speed."},
            {"text": "Because species are being lost far faster than they "
                     "are being replaced.",
             "correct": True},
            {"text": "Because extinctions in the past were caused by "
                     "asteroids, and the present ones are not.",
             "correct": False,
             "why": "Only one of the five mass extinctions is put down to an "
                    "impact. The cause is not what makes the present rate "
                    "worrying."},
            {"text": "Because extinction used to be a slow process and is now "
                     "instant for each species.",
             "correct": False,
             "why": "An individual species can take decades to go either way. "
                    "What has changed is how many are going at once."},
        ],
        "figure": None,
    },
    {
        "id": "b11-03-s22",
        "band": "standard",
        "text": "The hazel dormouse's best score anywhere on the bench is 80, "
                "against hunting. Explain why that high score is no comfort "
                "at all.",
        "options": [
            {"text": "Because nobody hunts dormice, so the one pressure it "
                     "handles well is the one it never meets.",
             "correct": True},
            {"text": "Because a score of 80 is a poor result on a bench where "
                     "65 is the lowest good figure.",
             "correct": False,
             "why": "Eighty is comfortably in the good band. The trouble is "
                    "which pressure it is good against."},
            {"text": "Because a species that is good against one pressure is "
                     "poor against the rest.",
             "correct": False,
             "why": "The brown rat is good against all five. There is no rule "
                    "that a strength has to be paid for elsewhere."},
            {"text": "Because hunting is the pressure most likely to arrive "
                     "next in southern England.",
             "correct": False,
             "why": "Hunting is the pressure it is safest from, and the ones "
                    "already acting on it are habitat loss and a shifting "
                    "climate."},
        ],
        "figure": None,
    },
    {
        "id": "b11-03-s23",
        "band": "standard",
        "text": "A conservation team must judge how threatened a species is. "
                "Which tells them more: the total number of individuals, or "
                "how many separate populations there are and how varied they "
                "are?",
        "options": [
            {"text": "The total number, because a species with more "
                     "individuals is further from having none and safer from "
                     "every threat.",
             "correct": False,
             "why": "Numbers can be rebuilt from very few animals. The "
                    "variation those animals carry cannot, and that is what "
                    "the next change will test."},
            {"text": "The number of populations and how varied they are, "
                     "because numbers can be rebuilt and lost variation "
                     "cannot.",
             "correct": True},
            {"text": "The total number, because it is the figure that can be "
                     "measured accurately.",
             "correct": False,
             "why": "Ease of measurement does not make a figure the right "
                    "one. A precise count of a population with no variation "
                    "left is a precise misleading answer."},
            {"text": "Neither, since a species is only safe once it is "
                     "protected by law.",
             "correct": False,
             "why": "Legal protection removes one pressure and touches none "
                    "of the others. The dormouse is protected and still "
                    "declining."},
        ],
        "figure": None,
    },
    {
        "id": "b11-03-s24",
        "band": "standard",
        "text": "A very large share of the extinctions recorded in the last "
                "few centuries have been of island species. Suggest why "
                "islands lose species so readily.",
        "options": [
            {"text": "Island species are weaker than mainland ones, having "
                     "had an easier life.",
             "correct": False,
             "why": "They are often superbly fitted to the island. Being well "
                    "fitted to one narrow set of conditions is what leaves "
                    "them exposed."},
            {"text": "Islands have poorer soil and less food than the "
                     "mainland, so island populations are always struggling "
                     "to survive.",
             "correct": False,
             "why": "Many islands are rich enough to support dense "
                    "populations. What they lack is space to retreat into and "
                    "any history of the predators people bring."},
            {"text": "An island species has a small range, nowhere to retreat "
                     "to, and no defence against the predators people bring.",
             "correct": True},
            {"text": "Islands are visited more often by scientists, so more "
                     "of their extinctions get recorded.",
             "correct": False,
             "why": "Better recording would inflate the count a little. It "
                    "does not explain losses on islands nobody studied until "
                    "the species had gone."},
        ],
        "figure": None,
    },
    {
        "id": "b11-03-s25",
        "band": "standard",
        "text": "A developer says draining one marsh cannot make anything "
                "extinct, because the same species live in marshes elsewhere. "
                "When is that argument sound, and when is it not?",
        "options": [
            {"text": "It is sound only if those other marshes really do hold "
                     "healthy populations of the same species.",
             "correct": True},
            {"text": "It is always sound, because a species is not lost while "
                     "any of it survives anywhere.",
             "correct": False,
             "why": "That is true of the final extinction and misses "
                    "everything before it. Each marsh drained removes a "
                    "population and some of the species' variation."},
            {"text": "It is never sound, because every marsh holds species "
                     "found in no other marsh.",
             "correct": False,
             "why": "Many marsh species are widespread. The argument fails "
                    "when the claim about the other sites has not been "
                    "checked, not automatically."},
            {"text": "It is sound only if the drained marsh is smaller than "
                     "the ones left.",
             "correct": False,
             "why": "Size is not what settles it. A small marsh can hold the "
                    "last of something, and a large one may hold nothing "
                    "unusual."},
        ],
        "figure": None,
    },
    {
        "id": "b11-03-s26",
        "band": "standard",
        "text": "Foxes are now commoner in British towns than they have ever "
                "been, while hedgehog numbers in the same towns have fallen "
                "sharply. Which idea from this lesson fits that contrast?",
        "options": [
            {"text": "Foxes are predators and hedgehogs are prey, so the "
                     "numbers of the two must always move in opposite "
                     "directions.",
             "correct": False,
             "why": "Foxes take very few hedgehogs. The contrast is about how "
                    "each species copes with a town, not about one eating the "
                    "other."},
            {"text": "Foxes breed faster than hedgehogs, which is why their "
                     "numbers have risen.",
             "correct": False,
             "why": "The two breed at broadly similar rates. What differs is "
                    "how well each of them uses what a town offers."},
            {"text": "Hedgehogs are protected by law and foxes are not, so "
                     "people leave foxes alone.",
             "correct": False,
             "why": "Protection would help hedgehogs rather than harm them, "
                    "and their numbers have fallen anyway. Legal status is "
                    "not the difference."},
            {"text": "A generalist can turn a change like a town into an "
                     "opportunity, while a species with narrower needs "
                     "cannot.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b11-03-s27",
        "band": "standard",
        "text": "The bench describes the dormouse's genetic variation as low, "
                "and falling as populations are cut off. Why does being cut "
                "off make variation fall?",
        "options": [
            {"text": "Because a cut-off population is exposed to fewer "
                     "different conditions, so it needs less variation.",
             "correct": False,
             "why": "Nothing supplies variation according to need. It is lost "
                    "because each isolated group breeds only within itself."},
            {"text": "Because each fragment breeds only within itself, so the "
                     "differences held elsewhere never reach it.",
             "correct": True},
            {"text": "Because animals in a small wood are all the same age, "
                     "so they are all alike.",
             "correct": False,
             "why": "Age is not inherited and a fragment holds animals of "
                    "several ages. What is lost is the mixing between "
                    "populations."},
            {"text": "Because a fragmented population stops breeding "
                     "altogether until it is joined up again.",
             "correct": False,
             "why": "It goes on breeding, which is the problem: it breeds "
                    "within a shrinking circle of close relatives."},
        ],
        "figure": None,
    },
    {
        "id": "b11-03-s28",
        "band": "standard",
        "text": "A scientist wants to claim that species are being lost "
                "faster now than they normally are. What does she need before "
                "she can say that at all?",
        "options": [
            {"text": "A list of every species currently thought to be at risk "
                     "of extinction.",
             "correct": False,
             "why": "A list of threatened species describes today. Without a "
                    "figure for normal times there is nothing to compare it "
                    "against."},
            {"text": "An estimate of the background rate — how fast species "
                     "were lost in ordinary times.",
             "correct": True},
            {"text": "A count of the species that went extinct in the five "
                     "mass extinctions.",
             "correct": False,
             "why": "Mass extinctions are the exceptional episodes. The "
                    "comparison she needs is with the ordinary rate between "
                    "them."},
            {"text": "Proof that people are the cause of the extinctions she "
                     "has counted.",
             "correct": False,
             "why": "Cause is a separate question from rate. She can show the "
                    "rate is high without having settled what is driving it."},
        ],
        "figure": None,
    },
    {
        "id": "b11-03-s29",
        "band": "standard",
        "text": "Two woods of exactly the same size are cleared. One is the "
                "only place a particular beetle is found; the other is one of "
                "two hundred sites holding that beetle. Why is the first far "
                "worse?",
        "options": [
            {"text": "Clearing the only site removes the whole species at a "
                     "stroke, while clearing one site in two hundred removes "
                     "a fraction of it.",
             "correct": True},
            {"text": "The first wood must have been older, since a species "
                     "found nowhere else has always been in one place a very "
                     "long time.",
             "correct": False,
             "why": "Age of the wood is not what decides it, and nothing here "
                    "says one is older. What matters is how much of the "
                    "species is in it."},
            {"text": "The beetles in the first wood will move to the second "
                     "one and overcrowd it.",
             "correct": False,
             "why": "They are in different places and, on this account, "
                    "cannot reach each other. Nothing moves anywhere."},
            {"text": "Both are equally bad, because the same area of woodland "
                     "and the same number of beetles are lost.",
             "correct": False,
             "why": "The area may match. What is lost differs entirely: one "
                    "loss is a fraction of a species and the other is all of "
                    "it."},
        ],
        "figure": None,
    },
    {
        "id": "b11-03-s30",
        "band": "standard",
        "text": "A butterfly has a population of several million, breeds "
                "twice a year, and its caterpillars eat one plant, which is "
                "now disappearing from Britain. How would you rate its risk?",
        "options": [
            {"text": "Low, because a population of several million cannot be "
                     "lost.",
             "correct": False,
             "why": "Numbers protect a species against most things and not "
                    "against losing its only food. The passenger pigeon ran "
                    "to billions."},
            {"text": "Low, because breeding twice a year gives it plenty of "
                     "generations to adapt.",
             "correct": False,
             "why": "Generations help only if the population contains "
                    "caterpillars able to eat something else. Nothing here "
                    "says it does."},
            {"text": "High, because one risk factor is enough when the thing "
                     "the species depends on is going.",
             "correct": True},
            {"text": "Impossible to say, because the four risk factors have "
                     "to point the same way before a judgement can be made.",
             "correct": False,
             "why": "They rarely all point one way. A single factor can carry "
                    "a species off if it is the one that matters."},
        ],
        "figure": None,
    },
    # ── harder · the MRB-338 expansion ──────────────────────────────────
    {
        "id": "b11-03-h14",
        "band": "harder",
        "text": "A brown tree snake was accidentally introduced to the Pacific island of "
                "Guam after the Second World War. Within a few decades it had wiped out "
                "most of the island's native forest bird species, most of which had "
                "lived there for thousands of years. What is the strongest explanation "
                "for such a complete collapse?",
        "options": [
            {"text": "None of the island's birds had any evolved defence against a "
                     "predator that hunted at night from the trees.",
             "correct": True},
            {"text": "The birds' forest habitat had already been cleared for farmland "
                     "before the snake ever arrived, leaving them nowhere to nest.",
             "correct": False,
             "why": "Guam's forest was largely intact when the snake arrived. The "
                    "collapse followed the snake, not a habitat loss that came before "
                    "it."},
            {"text": "The snake reproduced far faster than any of the island's birds "
                     "could possibly replace the numbers it was taking.",
             "correct": False,
             "why": "Breeding rate is not what this turns on. A predator with nothing "
                    "like it already on the island can finish off a species without "
                    "needing an unusually fast reproduction rate of its own."},
            {"text": "The island's birds were all specialists feeding on a single "
                     "insect, so almost any new pressure was bound to finish them off.",
             "correct": False,
             "why": "Guam's native birds fed on a range of fruit, nectar and insects "
                    "between them. What removed them was a predator they had no "
                    "defence against, not a shared narrow diet."},
        ],
        "figure": None,
    },
    {
        "id": "b11-03-h15",
        "band": "harder",
        "text": "A rare fish species lives only in a single volcanic crater lake, about "
                "four hundred metres across, and carries very high genetic variation. "
                "Does that variation make the species safe from extinction?",
        "options": [
            {"text": "Yes, because high genetic variation is the strongest of the four "
                     "risk factors and offsets a weakness anywhere else on the list.",
             "correct": False,
             "why": "The four risk factors are separate properties rather than points "
                    "on one scale. A species can score well on variation and still be "
                    "finished by an event in the one place it exists."},
            {"text": "No — everything it has lives in one place, so a single event "
                     "there could remove the whole population.",
             "correct": True},
            {"text": "Yes, because a species only becomes seriously at risk once every "
                     "one of the four risk factors is working against it together.",
             "correct": False,
             "why": "A single risk factor can be enough on its own — a specialist that "
                    "loses its only food is finished even if everything else about it "
                    "is healthy. A single tiny range is already that kind of factor "
                    "here."},
            {"text": "No, because a population confined to one small lake is too "
                     "limited in numbers for real genetic variation to build up in it.",
             "correct": False,
             "why": "The question states the variation has already been measured as "
                    "high; doubting that measurement sidesteps the actual question, "
                    "which is about what a small range does regardless of variation."},
        ],
        "figure": None,
    },
    {
        "id": "b11-03-h16",
        "band": "harder",
        "text": "A conservation report estimates that species are being lost worldwide "
                "at about 150 a year, and that this is roughly fifty times the "
                "background rate. At the background rate alone, roughly how many "
                "species would you expect to lose over a five-year period?",
        "options": [
            {"text": "About 3 species, since that is the figure for one single year "
                     "at the slower background rate rather than for the whole period.",
             "correct": False,
             "why": "That is the background rate for one year (150 divided by 50), "
                    "not the total for the five-year period the question asks about."},
            {"text": "About 30 species, found by sharing the total across the number "
                     "of years the report actually covers.",
             "correct": False,
             "why": "That divides 150 by five rather than by fifty, which mixes up "
                    "the number of years with the multiplier between the two rates."},
            {"text": "About 15 species, once the background rate has been separated "
                     "out and then carried forward across the five years asked about.",
             "correct": True},
            {"text": "About 750 species, taking the reported figure and simply "
                     "carrying it forward across the whole five-year period.",
             "correct": False,
             "why": "That multiplies the current elevated rate by five years, rather "
                    "than first dividing by fifty to reach the background rate."},
        ],
        "figure": None,
    },
    {
        "id": "b11-03-h17",
        "band": "harder",
        "text": "A newspaper reports that a bird population recovered after a nature "
                "reserve opened nearby, and concludes the reserve saved the species. A "
                "scientist points out that hunting of the bird was banned in exactly "
                "the same year the reserve opened. What is the strongest response to "
                "the newspaper's conclusion?",
        "options": [
            {"text": "The newspaper must simply be wrong, because reserves never make "
                     "any measurable difference to how a threatened species recovers.",
             "correct": False,
             "why": "Reserves do help many species, often by addressing habitat loss "
                    "or fragmentation directly. The problem here is not that reserves "
                    "are useless, it is that two changes happened together."},
            {"text": "The hunting ban is beside the point, because hunting was clearly "
                     "never the pressure that mattered most for this particular bird.",
             "correct": False,
             "why": "Nothing has been said about which pressure mattered. Two "
                    "possible causes arrived in the same year, and the report gives "
                    "no way to tell which one — or both — did the work."},
            {"text": "The recovery proves the reserve is what worked, since reserves "
                     "are specifically designed and funded to help species like this.",
             "correct": False,
             "why": "Being designed to help does not show that it did, in this case, "
                    "given a second explanation arrived at the very same time and was "
                    "left out of the report."},
            {"text": "The recovery can never be credited to the reserve alone, "
                     "since a second change — the hunting ban — happened at the "
                     "same time.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b11-03-h18",
        "band": "harder",
        "text": "A species can only survive above two thousand metres on one mountain, "
                "whose summit reaches two thousand two hundred metres. As the climate "
                "keeps warming, the zone it needs keeps shifting higher up the slope. "
                "Predict what eventually happens, and explain why this differs from "
                "the same problem for a species spread across a large continent.",
        "options": [
            {"text": "Eventually the zone it needs rises above the summit, leaving "
                     "nowhere higher to go — unlike a continental species, which can "
                     "keep shifting poleward.",
             "correct": True},
            {"text": "The species will start living further down the slope instead, "
                     "since two thousand metres was only ever a rough estimate, and a "
                     "mountain generally has plenty of room lower down.",
             "correct": False,
             "why": "The lower slopes are exactly where the unsuitable conditions the "
                    "species is retreating from now reach. It cannot simply move down "
                    "into the change it is trying to escape."},
            {"text": "Nothing changes for the species, because mountain summits stay "
                     "cooler than the surrounding lowland regardless of the climate.",
             "correct": False,
             "why": "The summit is cooler than the lowlands, and the whole mountain "
                    "is still warming along with everywhere else. What is "
                    "disappearing is the cool zone the species actually needs, not "
                    "cool air in general."},
            {"text": "The problem is exactly the same for the continental species, "
                     "since a warming climate affects the whole planet equally "
                     "everywhere.",
             "correct": False,
             "why": "A continental species facing the same warming can usually keep "
                    "moving towards the poles as the suitable zone shifts. A mountain "
                    "has a top; for practical purposes here, a continent does not."},
        ],
        "figure": None,
    },
    {
        "id": "b11-03-h19",
        "band": "harder",
        "text": "A small tiger population, cut off from all others for many "
                "generations, begins showing physical problems — crossed eyes and "
                "kinked tails — that were never recorded in the species before. What "
                "does that pattern suggest, and why does it matter beyond how the "
                "animals look?",
        "options": [
            {"text": "It suggests a new disease has entered the population, one that "
                     "happens by an unlikely coincidence to produce exactly these "
                     "physical symptoms as it spreads.",
             "correct": False,
             "why": "Nothing here points to an infection, and these traits are "
                    "inherited rather than caught. A pattern like this, appearing "
                    "only after isolation, points to what breeding within a "
                    "shrinking group does to a population's genes."},
            {"text": "It suggests low genetic variation from breeding within a "
                     "small isolated group, leaving it less able to cope with "
                     "future change.",
             "correct": True},
            {"text": "It is a purely cosmetic problem, with no real bearing on the "
                     "population's chances if its conditions were to change.",
             "correct": False,
             "why": "The visible traits are not the real concern. What matters is "
                    "that the same low variation producing visible defects is also "
                    "the variation the population would need in order to adapt to "
                    "anything new."},
            {"text": "It shows the population successfully adapting to isolation, "
                     "since new physical traits are appearing that were not there "
                     "before.",
             "correct": False,
             "why": "Adaptation implies traits that help a population cope with "
                    "something. Crossed eyes and kinked tails help with nothing — "
                    "they are a sign of variation being lost, not gained."},
        ],
        "figure": None,
    },
    {
        "id": "b11-03-h20",
        "band": "harder",
        "text": "A wildfire kills ninety per cent of a population, but the survivors "
                "happen to include at least one individual carrying every gene "
                "variant the population held before the fire. Has the population's "
                "genetic variation been reduced?",
        "options": [
            {"text": "Not necessarily, since a population can crash in numbers while "
                     "still holding onto the same range of variation, provided the "
                     "survivors happen to be representative of it.",
             "correct": True},
            {"text": "Yes, automatically, because any population losing ninety per "
                     "cent of its individuals must lose roughly ninety per cent of "
                     "its variation along with them.",
             "correct": False,
             "why": "Variation is not shared out evenly per individual the way that "
                    "arithmetic assumes. If the range of gene variants happens to "
                    "survive somewhere in the ten per cent left, the variation is "
                    "still there, even though the numbers are not."},
            {"text": "No, because genetic variation in a population is set mainly by "
                     "how many generations have passed, rather than by how many "
                     "individuals happen to be alive at any one time.",
             "correct": False,
             "why": "Time alone does not preserve variation — what is actually "
                    "present in living individuals does. Losing the individuals that "
                    "carried the variation would still lose the variation, whatever "
                    "the generation count."},
            {"text": "Yes, because a crash on this scale always strips out some of a "
                     "population's genetic variation, whoever happens to survive it.",
             "correct": False,
             "why": "A bottleneck usually does reduce variation, and that is not the "
                    "same as always. This question describes the less common case "
                    "where the surviving individuals happen to cover the full range "
                    "that was there before."},
        ],
        "figure": None,
    },
    {
        "id": "b11-03-h21",
        "band": "harder",
        "text": "Someone argues that conservation money should be spent only on "
                "species already known to be medically useful, since that is where "
                "the benefit is proven. What is the strongest problem with "
                "restricting protection this way?",
        "options": [
            {"text": "It is a reasonable rule, since species with proven medical uses "
                     "genuinely matter more to people than ones nobody has studied "
                     "yet.",
             "correct": False,
             "why": "The argument does not need medical usefulness to matter more "
                    "than anything else; using it as the sole test is self-defeating "
                    "on its own terms, because usefulness is discovered by studying "
                    "a species, not established beforehand."},
            {"text": "It would barely change anything, since nearly every species "
                     "eventually turns out to have some medical use once it has been "
                     "properly examined.",
             "correct": False,
             "why": "There is no basis for assuming nearly every species has a "
                    "medical use, and the argument does not need that claim. The "
                    "problem is the test itself: an unstudied species cannot pass "
                    "it, and it dies out unstudied."},
            {"text": "It fails mainly for plants, since the compounds worth "
                     "extracting for medicine are found overwhelmingly in plants "
                     "rather than in animals or fungi.",
             "correct": False,
             "why": "Useful compounds have come from a mould and are found across "
                    "plants, animals and fungi. The flaw in the argument is the same "
                    "whatever kind of organism is being ruled out of protection."},
            {"text": "A species' usefulness is normally discovered only after it has "
                     "been studied, so this rule guarantees losing exactly the "
                     "species nobody has checked yet.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b11-03-h22",
        "band": "harder",
        "text": "Scientists formally describe and name several thousand new species "
                "every year. Does that mean the total number of species alive on "
                "Earth is increasing?",
        "options": [
            {"text": "Yes, since a brand new species comes into existence each time "
                     "one is formally named and entered into the scientific record.",
             "correct": False,
             "why": "Naming a species is an act of classification, not of creation. "
                    "The organisms being described were already living, breeding "
                    "populations before anyone wrote a description of them."},
            {"text": "No — being newly described just means an existing species has "
                     "now been recorded, not that a new one exists.",
             "correct": True},
            {"text": "Yes, because new species are constantly evolving somewhere in "
                     "the world, and naming them simply keeps pace with roughly how "
                     "many now happen to exist.",
             "correct": False,
             "why": "New species do arise through evolution, and that process is far "
                    "too slow to explain thousands of new names appearing each year. "
                    "Almost all of those species were already there, waiting to be "
                    "found."},
            {"text": "No, because scientists have nearly run out of species left to "
                     "describe, which is why the rate of new names is now falling "
                     "each year.",
             "correct": False,
             "why": "The rate of newly described species has not been falling in "
                    "recent decades. The reason the total is not rising is about "
                    "what describing a species means, not about running out of them "
                    "to find."},
        ],
        "figure": None,
    },
    {
        "id": "b11-03-h23",
        "band": "harder",
        "text": "A captive breeding programme releases animals into the wild after "
                "ten generations raised in an enclosure with no predators. Beyond "
                "genetic variation, what other risk does this raise for the released "
                "animals?",
        "options": [
            {"text": "None at all, since anti-predator behaviour is learned entirely "
                     "fresh by each individual, and ten generations without a single "
                     "predator around cannot touch it.",
             "correct": False,
             "why": "Some anti-predator responses are inherited rather than learned "
                    "from scratch, and others are learned by watching wary adults — "
                    "neither of which an enclosure with no predators can provide."},
            {"text": "They may never have needed to recognise or respond to a real "
                     "predator, so anti-predator behaviour could be missing even in "
                     "genetically healthy animals.",
             "correct": True},
            {"text": "The main risk is simply that captive food differs from wild "
                     "food, so the released animals will not recognise anything to "
                     "eat.",
             "correct": False,
             "why": "Diet is a separate concern from how an animal reacts to a "
                    "threat. Ten generations without predators is specifically a "
                    "problem for anti-predator behaviour."},
            {"text": "The animals will simply have weaker bodies, from a lack of the "
                     "exercise a wild environment would otherwise have forced on "
                     "them.",
             "correct": False,
             "why": "Fitness from exercise is a real but different issue. The "
                    "specific risk raised by ten predator-free generations is "
                    "behavioural — not knowing how to respond to a threat — rather "
                    "than physical condition."},
        ],
        "figure": None,
    },
    {
        "id": "b11-03-h24",
        "band": "harder",
        "text": "Insects often evolve resistance to a new pesticide within just a few "
                "growing seasons, while a slow-breeding mammal facing a new pressure "
                "often cannot adapt in time and heads towards extinction instead. "
                "Both cases involve exactly the same underlying mechanism. What is "
                "it?",
        "options": [
            {"text": "Insects are simply better at evolving than mammals are "
                     "overall, because insects belong to a much older group in "
                     "evolutionary terms generally.",
             "correct": False,
             "why": "Age of the group is not what is doing the work here. What "
                    "differs between the two cases is how quickly each species can "
                    "turn its existing variation into generations, not any general "
                    "talent for evolving."},
            {"text": "Pesticides act far more slowly than natural predators do, "
                     "which gives insects extra time that a slow-breeding mammal "
                     "never gets.",
             "correct": False,
             "why": "Nothing in the comparison says the pesticide acts slowly. What "
                    "differs between the cases is the number of generations each "
                    "species fits into a set stretch of time, not the speed of the "
                    "pressure itself."},
            {"text": "How many generations occur within a given stretch of time "
                     "decides how many chances a favourable variant gets to "
                     "spread.",
             "correct": True},
            {"text": "Mammals cannot evolve resistance to anything, since resistance "
                     "of this kind is a specifically insect trait.",
             "correct": False,
             "why": "Mammals can and do evolve resistance to pressures, given "
                    "enough generations. The problem for the slow breeder here is a "
                    "shortage of generations in the time available, not an "
                    "inability to evolve at all."},
        ],
        "figure": None,
    },
    {
        "id": "b11-03-h25",
        "band": "harder",
        "text": "On the bench, disease is the weakest pressure for both the herring "
                "gull (score 60) and the giant panda (score 40). Both scores sit in "
                "the muted-to-amber range, yet the two species are not equally at "
                "risk from disease. Explain the difference.",
        "options": [
            {"text": "There is no real difference, since a score anywhere in the "
                     "muted-to-amber range represents the same level of risk "
                     "whatever species happens to hold it.",
             "correct": False,
             "why": "The score reflects an outcome, not a cause, and reading two "
                    "similar numbers as identical risk misses what is producing "
                    "them: population size and variation, which differ sharply "
                    "between these two species."},
            {"text": "The gull's score is only lower because gulls are studied far "
                     "more closely, so more of their disease cases get formally "
                     "recorded.",
             "correct": False,
             "why": "Nothing about how closely a species is studied changes the "
                    "outcome measured on the bench. The gap between the two species "
                    "comes from what each population actually holds, not from how "
                    "well it is monitored."},
            {"text": "The panda's score would rise to match the gull's if its own "
                     "colonies simply became as densely packed as a typical gull "
                     "colony's are said to be.",
             "correct": False,
             "why": "Density is not what is holding the panda's score down. What "
                    "limits it is a small, isolated population with low genetic "
                    "variation, which crowding the pandas together would not fix."},
            {"text": "The gull's large, varied population likely holds resistant "
                     "individuals despite fast-spreading colony disease; the "
                     "panda's small, isolated population may hold none at all.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b11-03-h26",
        "band": "harder",
        "text": "Green on the bench starts at a score of 65. The hazel dormouse's "
                "lowest score is 15, against habitat loss. By how many points does "
                "that fall short of the green threshold, and what does the gap "
                "represent?",
        "options": [
            {"text": "Fifty points — the gap between the threshold and the "
                     "dormouse's actual score.",
             "correct": True},
            {"text": "Thirty-five points, taken as the difference between the "
                     "dormouse's habitat score and whichever of its other four "
                     "scores happens to be next-lowest.",
             "correct": False,
             "why": "The question asks about the gap to the green threshold of 65, "
                    "not the gap between two of the dormouse's own scores. "
                    "Sixty-five minus fifteen is fifty, not thirty-five."},
            {"text": "Fifteen points, since fifteen is the dormouse's score and the "
                     "only number that the question has actually supplied.",
             "correct": False,
             "why": "Fifteen is the dormouse's score itself, not the distance "
                    "between that score and the threshold. The gap is found by "
                    "subtracting the score from 65."},
            {"text": "Eighty-five points, measured as the distance from the "
                     "dormouse's habitat score up to a perfect possible score of "
                     "100.",
             "correct": False,
             "why": "The green threshold on this bench is 65, not 100. The gap that "
                    "matters here is to the line separating a resilient outcome "
                    "from a vulnerable one, which is 65."},
        ],
        "figure": None,
    },
    {
        "id": "b11-03-h27",
        "band": "harder",
        "text": "A rock layer contains fossils of forty trilobite species. The layer "
                "laid down immediately above it, a short time later in geological "
                "terms, contains none. What does that pattern show, and what can it "
                "not show by itself?",
        "options": [
            {"text": "It shows that the trilobites migrated somewhere else, since an "
                     "absence of fossils in one layer never proves an absence of "
                     "the animals themselves anywhere at all.",
             "correct": False,
             "why": "Migration would still leave fossils somewhere in rock of the "
                    "same age laid down elsewhere, and none has been found. An "
                    "abrupt disappearance across a rock record like this is exactly "
                    "what a genuine loss looks like."},
            {"text": "It shows the group was lost from the fossil record in that "
                     "interval; it can never by itself show what caused the loss, "
                     "or how many separate events were involved.",
             "correct": True},
            {"text": "It shows precisely what caused the loss, since fossils "
                     "themselves are direct physical records of the event as it "
                     "actually happened.",
             "correct": False,
             "why": "A fossil records that an organism existed and, roughly, when. "
                    "It does not record why a whole group of them stopped existing "
                    "— that has to be worked out from other evidence."},
            {"text": "It shows nothing reliable at all, since gaps of this kind in "
                     "the fossil record are far too common to draw any real "
                     "conclusion from.",
             "correct": False,
             "why": "A change from forty species to none across one boundary is a "
                    "strong pattern, not an ordinary gap. It reliably shows a loss "
                    "occurred; the uncertainty is about the cause, not about "
                    "whether anything happened."},
        ],
        "figure": None,
    },
    {
        "id": "b11-03-h28",
        "band": "harder",
        "text": "American mink, introduced to Britain from fur farms, can swim well "
                "enough to follow water voles into the water and are small enough to "
                "enter their burrows — neither of which the native otter, a "
                "longstanding predator of the voles, can do as effectively. Why has "
                "this made the vole's usual defences useless?",
        "options": [
            {"text": "Otters and mink compete with each other for the same fish in "
                     "the same rivers, so the otters have driven the mink to hunt "
                     "voles instead out of necessity.",
             "correct": False,
             "why": "The mink's impact on voles is not explained by competition "
                    "with otters over fish. It follows from the mink's own ability "
                    "to reach places the vole's defences rely on being out of "
                    "reach."},
            {"text": "The vole's escape routes evolved against a predator with "
                     "different abilities, so a predator able to follow it into "
                     "both refuges removes that protection.",
             "correct": True},
            {"text": "Water voles have simply stopped using their burrows since the "
                     "mink arrived, purely out of a general increase in caution.",
             "correct": False,
             "why": "Abandoning a burrow would not explain a defence failing — it "
                    "would remove the vole's shelter altogether. What has happened "
                    "is that the burrow and the water no longer offer safety from "
                    "this particular predator."},
            {"text": "Mink are simply more aggressive than otters, so a vole that "
                     "could survive being attacked by an otter cannot survive an "
                     "attack by a mink.",
             "correct": False,
             "why": "Aggression is not the deciding factor here. What matters is "
                    "that the vole's usual escape routes were shaped by an otter's "
                    "more limited reach, and a mink's reach is not limited in the "
                    "same way."},
        ],
        "figure": None,
    },
    {
        "id": "b11-03-h29",
        "band": "harder",
        "text": "Of the five pressures on the bench, which could a single country's "
                "government reduce to zero by one decision, and which could no "
                "single country eliminate acting alone?",
        "options": [
            {"text": "A new predator could always be eliminated by one swift "
                     "decision, and disease could never be affected by any single "
                     "decision a country makes acting on its own.",
             "correct": False,
             "why": "An established predator can be very difficult to remove once "
                    "it has spread, and disease outbreaks can in fact be limited by "
                    "decisions such as quarantine or vaccination. Hunting is the "
                    "pressure the bench specifically names as stoppable by a "
                    "decision."},
            {"text": "Habitat loss could be reduced to zero by a single decision, "
                     "and hunting could not be touched by any decision a country "
                     "makes on its own.",
             "correct": False,
             "why": "Habitat, once cleared, is not restored by a single decision, "
                    "and clearing can continue for many separate reasons. Hunting "
                    "is the pressure that a single ban can switch off directly."},
            {"text": "Hunting can be stopped by a decision to ban it; climate "
                     "change cannot be eliminated by one country acting alone, "
                     "since it is driven by emissions worldwide.",
             "correct": True},
            {"text": "None of the five pressures could be affected by a single "
                     "country acting alone, since every environmental problem is "
                     "now global in scale.",
             "correct": False,
             "why": "Hunting of a particular species within a country's own "
                    "borders is squarely within that country's own power to stop. "
                    "Climate change is the pressure that genuinely needs action "
                    "beyond any one country."},
        ],
        "figure": None,
    },
    {
        "id": "b11-03-h30",
        "band": "harder",
        "text": "The rat's five scores add up to more than the dormouse's five scores "
                "combined. Does that total prove the rat is the better-adapted "
                "species overall?",
        "options": [
            {"text": "Yes, since a higher combined total always means better "
                     "long-term survival chances overall, no matter what is "
                     "actually causing each of the individual scores that make it "
                     "up.",
             "correct": False,
             "why": "The bench is built to show that a species can score "
                    "brilliantly against one pressure and disastrously against "
                    "another, and it is the pressure actually acting on it that "
                    "decides its fate — not a total that averages the two away."},
            {"text": "No, because scores measured against different pressures "
                     "cannot really be added together, since each one is measured "
                     "on its own separate scale.",
             "correct": False,
             "why": "All five scores use the very same scale, from 0 to 100, so "
                    "there is nothing stopping the arithmetic. The problem with a "
                    "total is not that it cannot be calculated, it is that it hides "
                    "which specific pressure is actually acting on a species."},
            {"text": "No — each score measures resilience to a separate pressure, "
                     "and a species can be strong against one and helpless against "
                     "another, which a summed total hides.",
             "correct": True},
            {"text": "Yes, but only in the special case where both species happen "
                     "to live in exactly the same habitat as one another.",
             "correct": False,
             "why": "Habitat overlap is not what makes a total meaningful or not. A "
                    "summed score misrepresents any species' risk, because what "
                    "actually threatens a species is a specific pressure, not an "
                    "average across five of them."},
        ],
        "figure": None,
    },
]
