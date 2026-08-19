"""B9 lesson 05 — Toxic build-up in a food chain: twelve questions (MRB-269).

These probe the one claim the lesson exists to establish: that persistence,
not toxicity, is what decides whether a chemical concentrates up a chain, and
that the molecule never changes — only how much of it is packed into each
kilogram of animal. The distractors are built from the lesson's two declared
misconceptions, ECO-09 (the poison gets stronger as it goes up the chain) and
ECO-10 (if the level in the water is safe, the ecosystem is safe), and from
the three wrong rules the bench's own settings exist to break: that toxicity
is the dial, that dissolving in water is what spreads a chemical everywhere,
and that the quantity sprayed decides the figure at the top. Two more come
from the lesson's careful wording — that the ×3 setting accumulates without
reaching harm, so a build-up below the harm line is still a build-up, and
that size is not the mechanism, position in the chain is. The `harder` band
takes the rule somewhere the page never goes: two pesticides of equal
toxicity on the same farmland, a safety test that asked the wrong question, a
recovery time set by lifespan and breeding rate, and two lakes that differ
only in how many feeding steps sit above the water.
"""

UNIT = "B9"
LESSON = "toxic-build-up-in-a-food-chain"
LESSON_NUMBER = 5

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "b9-05-e01",
        "band": "easier",
        "text": "The lesson gives you the word bioaccumulation. What does it "
                "describe?",
        "options": [
            {"text": "A substance becoming more poisonous the longer an "
                     "organism holds it in its body.",
             "correct": False,
             "why": "Nothing about the molecule changes. What builds up is "
                    "how much of it there is, not how strong it is."},
            {"text": "A substance spreading through a lake until every "
                     "organism in it carries the same amount.",
             "correct": False,
             "why": "The bench shows six levels and six different figures. "
                    "It collects into one body at each step; it does not "
                    "spread out evenly."},
            {"text": "A substance building up in an organism because it takes "
                     "it in faster than it can get rid of it.",
             "correct": True},
            {"text": "An organism storing a poison on purpose so that a "
                     "predator is harmed when it eats it.",
             "correct": False,
             "why": "Nothing here is deliberate. The organism simply cannot "
                    "break the chemical down or excrete it, so it stays."},
        ],
        "figure": None,
    },
    {
        "id": "b9-05-e02",
        "band": "easier",
        "text": "One of the three settings on the bench gives a flat line — "
                "every level the same, from the lake water to the ospreys. "
                "Which one, and why?",
        "options": [
            {"text": "Water-soluble, excreted: the kidneys remove it within "
                     "days, so nothing is ever stored.",
             "correct": True},
            {"text": "Persistent, fat-soluble: it is stored so well that "
                     "every organism ends up holding the same amount.",
             "correct": False,
             "why": "Being stored is exactly what makes it climb. That "
                    "setting multiplies by ten at every step and finishes at "
                    "300 ppm."},
            {"text": "Slowly broken down: some of each dose is destroyed, so "
                     "the concentration never changes.",
             "correct": False,
             "why": "Only part of each dose is destroyed, so the rest is "
                    "kept. That line still climbs — it just climbs more "
                    "slowly."},
            {"text": "All three are flat, and they only separate once you get "
                     "as far as the fish.",
             "correct": False,
             "why": "All three start at 0.0030 ppm in the water, and the "
                    "persistent one has already multiplied by ten by the time "
                    "you reach the algae."},
        ],
        "figure": None,
    },
    {
        "id": "b9-05-e03",
        "band": "easier",
        "text": "A persistent chemical is building up in a lake. Which "
                "organisms are harmed first?",
        "options": [
            {"text": "The smallest ones, because they have the least body "
                     "mass to dilute the chemical in.",
             "correct": False,
             "why": "The smallest organisms carry the least. It is position "
                    "in the chain that decides the concentration, not body "
                    "size."},
            {"text": "All of them at once, because every organism in the lake "
                     "shares the same contaminated water.",
             "correct": False,
             "why": "Sharing a lake is not sharing a dose. The same water "
                    "leaves the ospreys with a hundred thousand times what "
                    "the algae carry."},
            {"text": "The ones living closest to where the chemical first "
                     "washed into the lake from the fields.",
             "correct": False,
             "why": "The chemical travels through what each organism eats, "
                    "not through how near it is to the inflow."},
            {"text": "The animals at the top of the chain, at concentrations "
                     "that are harmless lower down.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b9-05-e04",
        "band": "easier",
        "text": "Two conditions both have to hold before anything builds up a "
                "food chain. Remove either one and nothing accumulates. What "
                "are they?",
        "options": [
            {"text": "The chemical is extremely poisonous, and the chain has "
                     "at least five levels in it.",
             "correct": False,
             "why": "How poisonous it is decides the damage once it arrives. "
                    "Whether it builds up at all is a separate question about "
                    "persistence."},
            {"text": "The chemical is not broken down or excreted, and each "
                     "predator eats many of the level below.",
             "correct": True},
            {"text": "The chemical dissolves easily in water, and the animals "
                     "drink a great deal of that water.",
             "correct": False,
             "why": "Dissolving in water is what lets the kidneys remove it, "
                    "and almost all of the intake comes through food rather "
                    "than water."},
            {"text": "The chemical is sprayed in large quantities, and it is "
                     "sprayed again every single year.",
             "correct": False,
             "why": "Quantity sets the starting concentration. A large amount "
                    "of something that breaks down still does not concentrate "
                    "up a chain."},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "b9-05-s01",
        "band": "standard",
        "text": "On the persistent setting the bench prints 0.0030 ppm in the "
                "lake water and 300 ppm in the ospreys. How many times higher "
                "is the osprey figure?",
        "options": [
            {"text": "Ten times, because each step up the chain multiplies "
                     "the concentration by ten.",
             "correct": False,
             "why": "Each step multiplies by ten, and there are five steps "
                    "above the water. Ten multiplied by itself five times is "
                    "a hundred thousand."},
            {"text": "Three hundred times, which is what the reading in the "
                     "ospreys is telling you.",
             "correct": False,
             "why": "300 is the osprey figure itself, not the comparison. To "
                    "compare it you divide it by the 0.0030 ppm in the "
                    "water."},
            {"text": "A hundred thousand times, because five feeding steps "
                     "have each multiplied it by ten.",
             "correct": True},
            {"text": "A hundred times, because 300 divided by 3 gives you a "
                     "hundred.",
             "correct": False,
             "why": "The water figure is 0.0030 ppm, not 3 ppm. Divide by "
                    "three thousandths and the answer is a hundred thousand, "
                    "not a hundred."},
        ],
        "figure": None,
    },
    {
        "id": "b9-05-s02",
        "band": "standard",
        "text": "On the “slowly broken down” setting the concentration climbs "
                "from 0.0030 ppm in the water to 0.729 ppm in the ospreys, "
                "and the bench says that is below the level that causes harm. "
                "What should you conclude?",
        "options": [
            {"text": "It still accumulates — a longer chain or a longer "
                     "exposure would get there.",
             "correct": True},
            {"text": "Nothing accumulated at all, because no level on the "
                     "bench went above the harm line.",
             "correct": False,
             "why": "The top row is over two hundred times the water figure. "
                    "A build-up that has not yet reached harm is still a "
                    "build-up."},
            {"text": "A chemical that can be broken down at all is therefore "
                     "safe to use wherever you like.",
             "correct": False,
             "why": "Slower breakdown is not the same as no accumulation. "
                    "Lengthen the chain or the exposure and the same chemical "
                    "arrives at harm."},
            {"text": "This chemical must be less poisonous than the one on "
                     "the persistent setting.",
             "correct": False,
             "why": "Nothing on the bench changes how poisonous the chemical "
                    "is. The only dial is how fast the body can break it "
                    "down."},
        ],
        "figure": None,
    },
    {
        "id": "b9-05-s03",
        "band": "standard",
        "text": "A water sample from a contaminated lake comes back far below "
                "anything that could harm a fish. A student says the "
                "ecosystem must therefore be safe. Where does that reasoning "
                "fail?",
        "options": [
            {"text": "It fails because one sample proves nothing; several "
                     "samples from around the lake would settle it.",
             "correct": False,
             "why": "Sampling is not the problem. Every sample gives the same "
                    "safe reading, and the ospreys are dying anyway."},
            {"text": "It fails only if somebody adds more of the chemical to "
                     "the lake at some point later on.",
             "correct": False,
             "why": "Nothing was added after the spraying. Every molecule in "
                    "the osprey came out of that same safe-looking water."},
            {"text": "It does not fail — the animals live in the water, so a "
                     "safe water reading covers all of them.",
             "correct": False,
             "why": "An osprey is not exposed to lake water. It is exposed to "
                    "fifty years of lake water, collected by other organisms "
                    "and delivered in a fish."},
            {"text": "It measures the water, but the chain above concentrates "
                     "whatever the water holds.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b9-05-s04",
        "band": "standard",
        "text": "Energy falls by about ten times at each step up a food "
                "chain, while the concentration of a persistent toxin rises "
                "by about ten times. Why do the two go opposite ways?",
        "options": [
            {"text": "Because energy and toxins follow opposite rules, so "
                     "whatever happens to one is reversed for the other.",
             "correct": False,
             "why": "There is one rule, not two. Mass is lost at every step "
                    "and the toxin is not, which is what sends the two "
                    "figures apart."},
            {"text": "Most of the food's mass is respired away while the "
                     "toxin is not, so it sits in far less animal.",
             "correct": True},
            {"text": "Because the predator's body makes more of the toxin out "
                     "of the energy it takes in from its food.",
             "correct": False,
             "why": "Nothing is made and nothing is added. Every molecule in "
                    "the predator came out of the prey it ate."},
            {"text": "Because a predator eats fewer animals than its prey "
                     "did, which packs what is left into one body.",
             "correct": False,
             "why": "A predator eats many of the level below — dozens or "
                    "hundreds of them. That is the other half of why the "
                    "concentration multiplies."},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "b9-05-h01",
        "band": "harder",
        "text": "Two pesticides are used on the same farmland. A breaks down "
                "in soil and water within a week; B dissolves in fat and "
                "lasts for decades. A single dose of each is equally "
                "poisonous. Which is the greater danger to the barn owls "
                "hunting there?",
        "options": [
            {"text": "A, because it acts within days, and speed is what makes "
                     "a chemical dangerous to wildlife.",
             "correct": False,
             "why": "How fast it acts decides the damage from one dose. "
                    "Whether it builds up over a lifetime is a separate "
                    "question about persistence."},
            {"text": "Neither, because a single dose of each is equally "
                     "poisonous, so the risk must be equal too.",
             "correct": False,
             "why": "Equal toxicity per dose is where they are the same. "
                    "Persistence is where they differ, and it decides how "
                    "large a dose reaches the owl."},
            {"text": "B, because it persists, so every dose an owl takes in "
                     "stays with it and the concentration climbs.",
             "correct": True},
            {"text": "B, because a chemical that dissolves in fat is more "
                     "poisonous than one that dissolves in water.",
             "correct": False,
             "why": "Fat-solubility is not toxicity. It decides whether the "
                    "body stores the chemical instead of filtering it out in "
                    "urine."},
        ],
        "figure": None,
    },
    {
        "id": "b9-05-h02",
        "band": "harder",
        "text": "A persistent pesticide is banned. In the same lake, the "
                "minnows — which breed within a year — recover quickly, while "
                "the ospreys, which raise a couple of chicks a year and live "
                "for twenty, take decades. Why?",
        "options": [
            {"text": "Ospreys are much larger, and a larger animal always "
                     "absorbs chemicals faster than a small one.",
             "correct": False,
             "why": "Size is not the mechanism. A basking shark eating "
                    "plankton accumulates far less than a small animal near "
                    "the top of a chain."},
            {"text": "The pesticide stays in the air the ospreys fly through "
                     "long after it has washed out of the lake.",
             "correct": False,
             "why": "The chemical is in the lake, and it reaches the osprey "
                    "through the fish it eats — not through where it spends "
                    "its time."},
            {"text": "Ospreys are further from the sprayed fields, so the "
                     "pesticide takes years longer to reach them.",
             "correct": False,
             "why": "They are further along the chain, not further away. "
                    "That makes their concentration higher, not later in "
                    "arriving."},
            {"text": "They are long-lived and slow-breeding, so they "
                     "accumulate for longest and replace lost adults "
                     "slowly.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b9-05-h03",
        "band": "harder",
        "text": "A new pesticide is approved by putting one dose into a tank "
                "of fish and checking that none of them die. It passes. "
                "Twenty years later the fish-eating birds are dying. What was "
                "wrong with the test?",
        "options": [
            {"text": "It asked how toxic one dose is, and never asked how "
                     "long the chemical lasts or whether it dissolves in "
                     "fat.",
             "correct": True},
            {"text": "The dose was too small — a larger one would have killed "
                     "the fish and the pesticide would have failed.",
             "correct": False,
             "why": "The concentration in the water genuinely is too low to "
                    "harm a fish. The test measured that correctly; it was "
                    "the wrong question."},
            {"text": "The wrong fish were chosen — a large predatory fish "
                     "would have died at that same dose.",
             "correct": False,
             "why": "No fish dies of one dose that size. What kills the bird "
                    "is a lifetime of doses, collected by everything below it "
                    "in the chain."},
            {"text": "The chemical must have changed into something far more "
                     "toxic over those twenty years in the lake.",
             "correct": False,
             "why": "The molecule is identical at the top of the chain and at "
                    "the bottom. What changed is how much of it sits in each "
                    "kilogram of animal."},
        ],
        "figure": None,
    },
    {
        "id": "b9-05-h04",
        "band": "harder",
        "text": "Two lakes get the same persistent chemical at the same "
                "concentration. In lake X the longest chain is algae → water "
                "fleas → small fish. In lake Y it runs on to a large fish and "
                "then a fish-eating bird. Twenty years later, what do you "
                "expect?",
        "options": [
            {"text": "The same at the top of both, because both lakes "
                     "received exactly the same amount of the chemical.",
             "correct": False,
             "why": "The amount sets the starting concentration. How many "
                    "feeding steps sit above the water is what decides how "
                    "often it is multiplied."},
            {"text": "Far more at the top of lake Y, because two extra "
                     "feeding steps have multiplied it again.",
             "correct": True},
            {"text": "More at the top of lake X, because the chemical there "
                     "has fewer organisms to spread itself between.",
             "correct": False,
             "why": "It is not shared out. Each step collects it from many "
                    "bodies into one, so more steps gives a higher figure, "
                    "not a lower one."},
            {"text": "It depends on which lake holds more water, because that "
                     "is what decides how far the chemical is diluted.",
             "correct": False,
             "why": "Dilution sets the figure in the water. The multiplying "
                    "that follows depends on the chain, and lake Y's chain is "
                    "two steps longer."},
        ],
        "figure": None,
    },
]
