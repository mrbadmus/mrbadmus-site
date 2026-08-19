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
]
