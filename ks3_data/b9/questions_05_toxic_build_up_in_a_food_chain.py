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
    # ── MRB-335 top-up ──────────────────────────────────────────────────
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "b9-05-e05",
        "band": "easier",
        "text": "A pollutant is described as persistent. What does that mean?",
        "options": [
            {"text": "It is extremely poisonous, so a very small amount does "
                     "a great deal of harm.", "correct": False,
             "why": "That is how toxic it is, which is a separate question. "
                    "Persistent describes how long it lasts."},
            {"text": "It is not broken down — by an organism, or in the "
                     "environment — for years or decades.", "correct": True},
            {"text": "It keeps being sprayed year after year, so it is always "
                     "present somewhere.", "correct": False,
             "why": "That describes how it is used. A persistent chemical "
                    "stays put after a single application, because nothing "
                    "breaks it down."},
            {"text": "It spreads through the water until every organism in "
                     "the lake has taken some in.", "correct": False,
             "why": "Spreading is how it reaches the organisms. Persistence "
                    "is what happens once it is inside one — nothing removes "
                    "it."},
        ],
        "figure": None,
    },
    {
        "id": "b9-05-e06",
        "band": "easier",
        "text": "A chemical is described as fat-soluble. Why does that make "
                "it dangerous in a food chain?",
        "options": [
            {"text": "Because fat-soluble chemicals are more poisonous than "
                     "water-soluble ones.", "correct": False,
             "why": "Dissolving in fat says nothing about how poisonous a "
                    "chemical is. What it decides is whether the body can get "
                    "rid of it."},
            {"text": "Because animals with more fat eat more, so they take in "
                     "more of it.", "correct": False,
             "why": "How much an animal eats is not the mechanism. Dissolving "
                    "in fat means the body stores the chemical instead of "
                    "filtering it out."},
            {"text": "Because the body stores it in fat instead of filtering "
                     "it out, so it stays for life.", "correct": True},
            {"text": "Because it dissolves in the lake water and so reaches "
                     "every organism there.", "correct": False,
             "why": "That is what water-soluble means, and the water-soluble "
                    "case is the safe one — the kidneys remove it within "
                    "days."},
        ],
        "figure": None,
    },
    {
        "id": "b9-05-e07",
        "band": "easier",
        "text": "Concentrations of a pollutant in water are often given in "
                "parts per million. Roughly what is 1 part per million?",
        "options": [
            {"text": "About 1 milligram in a litre.", "correct": True},
            {"text": "About 1 gram in a litre.", "correct": False,
             "why": "A gram in a litre is a thousand times more concentrated "
                    "— that is a part per thousand. A milligram is a "
                    "thousandth of a gram."},
            {"text": "About 1 milligram in a million litres.",
             "correct": False,
             "why": "That is a millionth of the concentration meant. Parts "
                    "per million means one part in a million parts, which in "
                    "water is about a milligram in a litre."},
            {"text": "About one millionth of the amount that would cause "
                     "harm.", "correct": False,
             "why": "It is a unit of concentration, not a measure of safety. "
                    "Whether 1 ppm is harmful depends entirely on the "
                    "substance."},
        ],
        "figure": None,
    },
    {
        "id": "b9-05-e08",
        "band": "easier",
        "text": "A pesticide measures far higher in an osprey than in the "
                "lake water it came from. Has the chemical become stronger on "
                "the way up?",
        "options": [
            {"text": "Yes — each animal changes it into a more dangerous form "
                     "as it passes it on.", "correct": False,
             "why": "Nothing is converted. The molecule leaving a minnow is "
                    "the same molecule that arrived in it."},
            {"text": "Yes, because a predator's body concentrates it by "
                     "reacting it with fat.", "correct": False,
             "why": "It is stored in fat, not reacted with it. Storing is "
                    "what makes the concentration climb; the chemical itself "
                    "is unchanged."},
            {"text": "No — the concentration is the same all the way up, and "
                     "only the osprey is harmed.", "correct": False,
             "why": "The concentration really does climb, by a hundred "
                    "thousand times in this case. What does not change is the "
                    "chemical."},
            {"text": "No — the chemical is unchanged, but it is packed into "
                     "fewer and fewer bodies at each step.", "correct": True},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "b9-05-s05",
        "band": "standard",
        "text": "Polar bears eat seals, seals eat fish, and the fish eat "
                "plankton. Why does a polar bear carry far more of a "
                "persistent pollutant than a seal does?",
        "options": [
            {"text": "Because a polar bear is much larger, and a large body "
                     "holds more of everything.", "correct": False,
             "why": "A larger body holds more in total, and what is measured "
                    "is the concentration — the amount in each kilogram. A "
                    "basking shark is enormous and carries very little."},
            {"text": "Because each bear eats many seals over its life and "
                     "keeps the pollutant from all of them.", "correct": True},
            {"text": "Because the pollutant becomes more poisonous each time "
                     "it is passed on.", "correct": False,
             "why": "The chemical does not change. What changes is how much "
                    "of it has been packed into one body."},
            {"text": "Because polar bears swim more than seals do, so they "
                     "absorb more from the water.", "correct": False,
             "why": "Almost all of the intake comes through food rather than "
                    "water, and seals spend far more time in the sea in any "
                    "case."},
        ],
        "figure": None,
    },
    {
        "id": "b9-05-s06",
        "band": "standard",
        "text": "In one lake the fish-eating birds are dying while the fish "
                "they eat look healthy. A student concludes the pesticide "
                "must be poisonous to birds and harmless to fish. What is "
                "wrong with that?",
        "options": [
            {"text": "The birds carry a far higher concentration of the same "
                     "chemical than the fish do.", "correct": True},
            {"text": "Nothing is wrong — different animals are harmed by "
                     "different chemicals.", "correct": False,
             "why": "They can be, and this case does not show it. The birds "
                    "are meeting a dose hundreds of times higher than the "
                    "fish are."},
            {"text": "The fish are harmed too, but nobody has looked closely "
                     "enough to notice.", "correct": False,
             "why": "There may be effects nobody has measured, and the "
                    "straightforward explanation is concentration. The fish "
                    "sit lower down the chain that multiplies it."},
            {"text": "The birds must be eating something else in the lake "
                     "that is poisoning them.", "correct": False,
             "why": "Nothing needs adding to the story. Eating many fish, "
                    "each carrying the chemical, is enough on its own."},
        ],
        "figure": None,
    },
    {
        "id": "b9-05-s07",
        "band": "standard",
        "text": "A persistent pesticide is banned and no more is used "
                "anywhere near a lake. Why is the level in the ospreys still "
                "high several years later?",
        "options": [
            {"text": "Because farmers went on using it in secret after the "
                     "ban.", "correct": False,
             "why": "Nothing has to be assumed about breaking the law. A "
                    "persistent chemical is still there whether or not any "
                    "more is added."},
            {"text": "Because the ospreys keep making more of it inside their "
                     "own bodies.", "correct": False,
             "why": "No animal makes it. Every molecule came from the "
                    "spraying, and none of it has been broken down since."},
            {"text": "Because nothing breaks it down, so what is already in "
                     "the lake and in the animals stays there.",
             "correct": True},
            {"text": "Because the ban stopped new spraying only, and the "
                     "chemical evaporates back out of the soil each summer.",
             "correct": False,
             "why": "Some movement between soil and air does happen, and it "
                    "is not the reason. The reason is that neither the "
                    "environment nor the birds can break it down."},
        ],
        "figure": None,
    },
    {
        "id": "b9-05-s08",
        "band": "standard",
        "text": "Two seabirds feed on the same fish in the same bay. One "
                "lives about four years, the other about thirty. Which "
                "carries more of a persistent pollutant, and why?",
        "options": [
            {"text": "The four-year bird, because a young body takes a "
                     "chemical in faster.", "correct": False,
             "why": "Nothing about being young speeds up the intake. What "
                    "matters is how long an animal has been taking it in "
                    "without being able to get rid of it."},
            {"text": "Both the same, because they eat the same fish at the "
                     "same concentration.", "correct": False,
             "why": "The same food does not give the same body burden. A "
                    "persistent chemical is kept, so it adds up for as long "
                    "as the animal lives."},
            {"text": "The thirty-year bird, because a large old bird eats "
                     "more each day.", "correct": False,
             "why": "The right bird for not quite the right reason. What "
                    "counts is the total taken in across a whole life, which "
                    "goes on adding up whatever the daily amount."},
            {"text": "The thirty-year bird, because it has been accumulating "
                     "the chemical for far longer.", "correct": True},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "b9-05-h05",
        "band": "harder",
        "text": "A persistent chemical measures 0.004 ppm in a lake's water "
                "and multiplies by about ten at each of five steps up to the "
                "ospreys. Harm begins at 100 ppm. What is the concentration "
                "in the ospreys?",
        "options": [
            {"text": "0.02 ppm, which is far below the level at which harm "
                     "begins.", "correct": False,
             "why": "That multiplies by five once, instead of by ten at each "
                    "of five steps. Five steps of ten times is a hundred "
                    "thousand times altogether."},
            {"text": "400 ppm, which is well above the level at which harm "
                     "begins.", "correct": True},
            {"text": "40 ppm, which is below the level at which harm begins.",
             "correct": False,
             "why": "That is four steps rather than five. One more step of "
                    "ten times takes it to 400 ppm, and past the harm "
                    "level."},
            {"text": "0.00000004 ppm, which is far too little to matter.",
             "correct": False,
             "why": "Going up a chain the concentration multiplies; it is the "
                    "energy that divides. Dividing five times is the "
                    "arithmetic from a different lesson."},
        ],
        "figure": None,
    },
    {
        "id": "b9-05-h06",
        "band": "harder",
        "text": "DDT was sprayed on farmland from the 1940s. Twenty years "
                "later peregrines and ospreys were laying eggs with shells so "
                "thin they broke under the sitting bird. Why did the damage "
                "appear in birds that were never sprayed?",
        "options": [
            {"text": "Because DDT is far more poisonous to birds than to "
                     "insects.", "correct": False,
             "why": "It was made to kill insects and it did. What reached the "
                    "birds was a concentration hundreds of thousands of times "
                    "higher than anything in the fields."},
            {"text": "Because the birds ate the sprayed insects directly and "
                     "took the spray in with them.", "correct": False,
             "why": "Those birds eat other birds and fish rather than insects "
                    "off a crop. The chemical reached them up a chain of "
                    "several steps, each one multiplying it."},
            {"text": "Because DDT is persistent and fat-soluble, so it "
                     "concentrated up every chain it entered.",
             "correct": True},
            {"text": "Because the spray drifted on the wind and settled on "
                     "the birds' nesting cliffs.", "correct": False,
             "why": "Drift moved some of it about, and drift concentrates "
                    "nothing. The build-up happened inside the animals, meal "
                    "by meal."},
        ],
        "figure": None,
    },
    {
        "id": "b9-05-h07",
        "band": "harder",
        "text": "An osprey and a heron feed on the same lake. The osprey eats "
                "perch, which eat minnows, which eat water fleas. The heron "
                "eats frogs and water snails, which graze the algae. Which "
                "bird carries more of a persistent pollutant?",
        "options": [
            {"text": "The osprey, because its food comes from two steps "
                     "further up the chain.", "correct": True},
            {"text": "The heron, because snails and frogs live in the mud "
                     "where the chemical settles.", "correct": False,
             "why": "Some chemicals do settle in sediment, and the build-up "
                    "here comes from the number of steps. The heron is "
                    "feeding close to the bottom of the chain."},
            {"text": "Both the same, because they feed on the same lake at "
                     "the same concentration in the water.", "correct": False,
             "why": "The water is the same for both, and neither bird gets it "
                    "from the water. It arrives through the food, and their "
                    "foods sit at different levels."},
            {"text": "The heron, because frogs and snails are eaten whole, so "
                     "nothing is left behind.", "correct": False,
             "why": "How the prey is eaten does not decide it. What decides "
                    "it is how many steps of multiplying have happened before "
                    "the food reaches the bird."},
        ],
        "figure": None,
    },
    {
        "id": "b9-05-h08",
        "band": "harder",
        "text": "Two persistent chemicals are both found in a lake at "
                "0.01 ppm. Chemical P multiplies by about ten at each of four "
                "steps; chemical Q multiplies by about two at each of the "
                "same four steps. What arrives at the top?",
        "options": [
            {"text": "100 ppm and 8 ppm, so a small difference per step makes "
                     "little difference overall.", "correct": False,
             "why": "Q is 0.01 doubled four times, which is 0.16 ppm rather "
                    "than 8. And the gap between them is enormous rather than "
                    "small."},
            {"text": "40 ppm and 8 ppm, so P climbs about five times as far "
                     "as Q does.", "correct": False,
             "why": "P is 0.01 multiplied by ten four times, which is "
                    "100 ppm. The two do not finish within five times of each "
                    "other; they finish hundreds of times apart."},
            {"text": "100 ppm and 0.16 ppm, and both would be enough to harm "
                     "a top predator.", "correct": False,
             "why": "The two concentrations are right and the conclusion is "
                    "not. One is more than six hundred times the other, which "
                    "is the difference between reaching a harmful level and "
                    "coming nowhere near it."},
            {"text": "100 ppm and 0.16 ppm, so what is kept at each step "
                     "matters enormously.", "correct": True},
        ],
        "figure": None,
    },

    # ── MRB-338 top-up ───────────────────────────────────────────────────
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "b9-05-e09",
        "band": "easier",
        "text": "A gull eats a small amount of a persistent chemical every "
                "week for ten years. Nothing in its body ever breaks the "
                "chemical down or removes it. What happens to the amount it "
                "holds?",
        "options": [
            {"text": "It stays the same throughout, because a small weekly "
                     "amount never adds up to much.", "correct": False,
             "why": "Small amounts really do add up when nothing removes "
                    "them — ten years of weekly doses is five hundred or so "
                    "doses, all still there."},
            {"text": "It keeps rising for as long as the gull keeps taking "
                     "in more than it loses.", "correct": True},
            {"text": "It rises for a while and then levels off, once the "
                     "gull's body is full.", "correct": False,
             "why": "There is no such ceiling in the chemical's behaviour "
                    "here. With nothing removing it, each new dose simply "
                    "adds to what is already there."},
            {"text": "It falls slowly, because some of every dose is used "
                     "up by the gull's own body.", "correct": False,
             "why": "Nothing here is using the chemical up. If nothing "
                    "removes it, none of it is lost, so none of it falls."},
        ],
        "figure": None,
    },
    {
        "id": "b9-05-e10",
        "band": "easier",
        "text": "A chemical is broken down completely within a few days of "
                "an animal taking it in. Would you expect it to bioaccumulate "
                "up a food chain?",
        "options": [
            {"text": "No — it is removed so quickly that another dose "
                     "never gets the chance to add to it.", "correct": True},
            {"text": "Yes — every chemical builds up eventually, no matter how quickly the body deals with it, given enough time.", "correct": False,
             "why": "Given enough time is exactly what this chemical never "
                    "gets. It is gone within days, well before the next "
                    "dose arrives."},
            {"text": "Yes, but only in animals at the very top of the "
                     "chain.", "correct": False,
             "why": "Position in the chain matters for a chemical that IS "
                    "kept. One that is removed within days never reaches a "
                    "top predator in the first place."},
            {"text": "It depends on how toxic the chemical is.",
             "correct": False,
             "why": "Toxicity decides the damage from a single dose. "
                    "Whether a dose accumulates at all is a separate "
                    "question about how long it lasts."},
        ],
        "figure": None,
    },
    {
        "id": "b9-05-e11",
        "band": "easier",
        "text": "Mercury released into a lake is not broken down by any "
                "organism. Which property does that give it in common with a "
                "persistent pesticide?",
        "options": [
            {"text": "It reacts with the lake water itself, so it forms an entirely new and more dangerous compound as time passes.", "correct": False,
             "why": "No new compound is formed here. What matters is that "
                    "nothing removes the mercury once an animal has taken it "
                    "in."},
            {"text": "It kills fish quickly enough to be noticed within "
                     "days.", "correct": False,
             "why": "Nothing here says mercury acts quickly. Sharing a "
                    "persistent pesticide's slow, cumulative behaviour is "
                    "the point, not a fast kill."},
            {"text": "It is not removed once an animal has taken it in, so "
                     "it stays and can add up.", "correct": True},
            {"text": "It only affects fish, and not birds that eat the "
                     "fish.", "correct": False,
             "why": "A chemical that persists reaches whatever eats along "
                    "the chain, birds included. Nothing here limits it to "
                    "fish."},
        ],
        "figure": None,
    },
    {
        "id": "b9-05-e12",
        "band": "easier",
        "text": "Killer whales off some coasts carry very high levels of "
                "PCBs, industrial chemicals banned decades ago. Why would "
                "banning them not immediately fix the problem?",
        "options": [
            {"text": "Because orcas keep making new PCBs inside their own "
                     "bodies.", "correct": False,
             "why": "No animal produces PCBs. Every molecule an orca "
                    "carries came from what it has eaten over its life."},
            {"text": "Because PCBs are so toxic in a single dose that even a total worldwide ban could never make them safe again.", "correct": False,
             "why": "Toxicity is not what a ban changes. The problem is "
                    "that PCBs already in the sea and in animals are not "
                    "removed by banning further use."},
            {"text": "Because orcas live too far offshore for a ban to "
                     "reach them.", "correct": False,
             "why": "Where an animal lives does not matter here — a ban "
                    "stops new use, and it cannot remove a chemical that "
                    "persists once it is already there."},
            {"text": "Because PCBs already in the sea and in animals are "
                     "not broken down, so they remain.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b9-05-e13",
        "band": "easier",
        "text": "Which pair correctly matches a chemical property to what "
                "happens to it in the body?",
        "options": [
            {"text": "Water-soluble — removed in urine; fat-soluble — "
                     "stored in body fat.", "correct": True},
            {"text": "Water-soluble — stored in body fat; fat-soluble — "
                     "removed in urine.", "correct": False,
             "why": "That is the two properties swapped. Water-soluble "
                    "chemicals dissolve out with the urine; fat-soluble "
                    "ones are what gets stored."},
            {"text": "Water-soluble — broken down by sunlight; fat-soluble "
                     "— broken down by enzymes.", "correct": False,
             "why": "Neither property is about breakdown by sunlight or "
                    "enzymes. Solubility decides whether the kidneys can "
                    "remove a chemical, not whether it is broken down."},
            {"text": "Water-soluble — carried in the blood forever; "
                     "fat-soluble — removed within hours.", "correct": False,
             "why": "This has both halves backwards. A water-soluble "
                    "chemical is what leaves quickly, and a fat-soluble one "
                    "is what is kept."},
        ],
        "figure": None,
    },
    {
        "id": "b9-05-e14",
        "band": "easier",
        "text": "A pollutant is said to cause harm 'above a certain "
                "concentration'. What does that mean?",
        "options": [
            {"text": "Below that concentration the chemical is not present "
                     "at all.", "correct": False,
             "why": "It is still present below that concentration — the "
                    "level in the water is never zero. It is simply "
                    "too low to cause damage."},
            {"text": "Below it, the concentration is too low to cause "
                     "damage; above it, damage occurs.", "correct": True},
            {"text": "It means the chemical becomes a different, safer "
                     "substance below that concentration.", "correct": False,
             "why": "The molecule does not change at any concentration. "
                    "What changes is simply how much of it is present."},
            {"text": "It means that only the very largest animals are ever affected below that particular concentration.", "correct": False,
             "why": "The concentration threshold is not sorted by the size "
                    "of the animal. It is the concentration itself, "
                    "wherever it is measured, that decides."},
        ],
        "figure": None,
    },
    {
        "id": "b9-05-e15",
        "band": "easier",
        "text": "Toxic and persistent describe two different properties of a "
                "chemical. Which statement keeps them separate correctly?",
        "options": [
            {"text": "A chemical cannot be both toxic and persistent at "
                     "once.", "correct": False,
             "why": "Many pesticides are exactly that — both toxic in a "
                    "single dose and persistent over years. The two "
                    "properties are independent, not opposites."},
            {"text": "Toxic means how long a chemical lasts; persistent "
                     "means how much harm one dose causes.", "correct": False,
             "why": "This has the two definitions swapped. Persistence is "
                    "about how long it lasts; toxicity is about the harm "
                    "from one dose."},
            {"text": "Toxic means how much harm one dose causes; persistent "
                     "means how long the chemical lasts.", "correct": True},
            {"text": "Both words describe exactly the same property, just "
                     "for different audiences.", "correct": False,
             "why": "They are not the same property. A chemical can be "
                    "highly toxic and break down within days, or mildly "
                    "toxic and last for decades."},
        ],
        "figure": None,
    },
    {
        "id": "b9-05-e16",
        "band": "easier",
        "text": "In a chain where a persistent chemical concentrates at "
                "every step, which organism carries the lowest "
                "concentration?",
        "options": [
            {"text": "The top predator, because predators break down "
                     "chemicals fastest.", "correct": False,
             "why": "Predators do not break this kind of chemical down at "
                    "all — that is what persistent means. The top of the "
                    "chain carries the highest concentration, not the "
                    "lowest."},
            {"text": "Whichever organism is largest, regardless of its "
                     "position in the chain.", "correct": False,
             "why": "Size is not the mechanism here. Position in the "
                    "chain — how many steps of concentrating an organism "
                    "sits above the water — decides it."},
            {"text": "It is the same at every level, since the chemical "
                     "itself never changes.", "correct": False,
             "why": "The chemical is unchanged, and the amount held at "
                    "each level is not the same — that is exactly what the "
                    "word bioaccumulation describes."},
            {"text": "The producers or the water itself, at the very "
                     "bottom of the chain.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b9-05-e17",
        "band": "easier",
        "text": "A chemical is quickly broken down by every organism that "
                "takes it in. Would a food chain concentrate it the way it "
                "concentrates a persistent chemical?",
        "options": [
            {"text": "No — with nothing ever kept from one step to the "
                     "next, the concentration never climbs.", "correct": True},
            {"text": "Yes — any chemical passed along a food chain eventually concentrates, whatever its own chemical properties happen to be.", "correct": False,
             "why": "Concentrating up a chain needs the chemical to be "
                    "kept at each step. One that is broken down quickly is "
                    "not kept, so nothing accumulates."},
            {"text": "Yes, but only across chains with more than five "
                     "levels.", "correct": False,
             "why": "The length of the chain is not what fixes this. A "
                    "chemical that does not persist fails to concentrate "
                    "whatever the chain's length."},
            {"text": "It depends on how toxic the chemical is to the top "
                     "predator.", "correct": False,
             "why": "Toxicity decides the damage from a dose that arrives. "
                    "Whether a dose accumulates at all depends on "
                    "persistence, not toxicity."},
        ],
        "figure": None,
    },
    {
        "id": "b9-05-e18",
        "band": "easier",
        "text": "Decades can pass between a persistent pesticide being "
                "sprayed and a top predator's population collapsing. Why "
                "does the harm take so long to appear?",
        "options": [
            {"text": "Because the pesticide takes decades to become "
                     "poisonous after it is sprayed.", "correct": False,
             "why": "The molecule is poisonous from the moment it is made. "
                    "What takes time is the concentration climbing high "
                    "enough at the top of the chain."},
            {"text": "Because the concentration has to climb through "
                     "several feeding steps before it reaches a harmful "
                     "level.", "correct": True},
            {"text": "Because predators are naturally resistant to "
                     "pesticides for the first few decades of exposure.",
             "correct": False,
             "why": "There is no such resistance stage. What changes over "
                    "the decades is how much of the chemical has built up, "
                    "not the predator's tolerance."},
            {"text": "Because it takes that long for the pesticide to "
                     "travel from the fields to the top predator's "
                     "habitat.", "correct": False,
             "why": "The chemical reaches the water and the first feeding "
                    "step quickly. The slow part is the concentration "
                    "climbing through the chain that follows."},
        ],
        "figure": None,
    },
    {
        "id": "b9-05-e19",
        "band": "easier",
        "text": "Not every pesticide used today builds up a food chain the "
                "way DDT once did. What has to be true of a pesticide for it "
                "not to bioaccumulate?",
        "options": [
            {"text": "It has to be sprayed in very small amounts.",
             "correct": False,
             "why": "Quantity sets the starting concentration, not whether "
                    "it builds up at all. A small amount of a persistent "
                    "chemical still concentrates up a chain."},
            {"text": "It has to be too toxic for any animal along the chain to survive eating even a single contaminated meal.", "correct": False,
             "why": "Toxicity and persistence are separate properties. A "
                    "highly toxic chemical can still fail to bioaccumulate "
                    "if it breaks down quickly."},
            {"text": "It has to be broken down or excreted rather than "
                     "stored in the body.", "correct": True},
            {"text": "It has to dissolve in fat rather than in water.",
             "correct": False,
             "why": "That is the property that lets a chemical accumulate, "
                    "not the one that stops it. A water-soluble chemical is "
                    "the one that fails to build up."},
        ],
        "figure": None,
    },
    {
        "id": "b9-05-e20",
        "band": "easier",
        "text": "Persistent chemicals sprayed on farmland thousands of "
                "kilometres away have been found in polar bears in the "
                "Arctic, where no pesticide has ever been used. How does "
                "that happen?",
        "options": [
            {"text": "Polar bears must migrate to farmland to feed "
                     "occasionally.", "correct": False,
             "why": "Polar bears do not travel to farmland. The chemical "
                    "reaches them by a different route."},
            {"text": "The chemical is carried by wind and water currents, "
                     "then enters Arctic food chains.", "correct": True},
            {"text": "The chemical is manufactured naturally in Arctic "
                     "ice.", "correct": False,
             "why": "Persistent pesticides are made by industry, not by "
                    "ice. Nothing manufactures them in the Arctic itself."},
            {"text": "Seals swim south to warmer seas, pick up the chemical there from local fish, and then carry it back north.", "correct": False,
             "why": "The chemical does not need an animal to carry it "
                    "across oceans. Persistent chemicals travel through "
                    "air and water currents on their own."},
        ],
        "figure": None,
    },
    {
        "id": "b9-05-e21",
        "band": "easier",
        "text": "A female mammal has accumulated a persistent, fat-soluble "
                "chemical over her life. How can some of it pass to her "
                "offspring even though she never sprays anything on them?",
        "options": [
            {"text": "It passes through the placenta or in her milk, since "
                     "both are rich in fat.", "correct": True},
            {"text": "It jumps directly from her bloodstream into theirs "
                     "without any route at all.", "correct": False,
             "why": "Nothing crosses without a route. Fat in the placenta "
                    "and in milk is exactly the route a fat-soluble "
                    "chemical would take."},
            {"text": "It cannot pass to offspring at all, since only food "
                     "chains carry it.", "correct": False,
             "why": "A mother's body is itself part of the chain her "
                    "offspring feed from. Milk is rich in fat, and a "
                    "fat-soluble chemical goes where the fat goes."},
            {"text": "It only ever passes to offspring that happen to be born after she has stopped accumulating it.", "correct": False,
             "why": "Nothing about birth timing removes a stored chemical. "
                    "It is present in her fat throughout, offspring born "
                    "before or after."},
        ],
        "figure": None,
    },
    {
        "id": "b9-05-e22",
        "band": "easier",
        "text": "A single meal of contaminated fish contains far too little "
                "of a persistent chemical to harm anyone eating it once. "
                "Does that make the fish safe to eat regularly for years?",
        "options": [
            {"text": "Yes — if one meal on its own is judged safe, then any number of repeated meals must also be perfectly safe.", "correct": False,
             "why": "That treats a single dose and a lifetime of doses as "
                    "the same question. A persistent chemical adds up, so "
                    "repeated meals are not the same as one."},
            {"text": "Not necessarily — a persistent chemical eaten "
                     "repeatedly can still add up over years.",
             "correct": True},
            {"text": "Yes, because the chemical is broken down between "
                     "meals.", "correct": False,
             "why": "Whether it is broken down is exactly what 'persistent' "
                    "rules out. If it is not, nothing between meals removes "
                    "it."},
            {"text": "No — a single meal is already dangerous, regardless "
                     "of the chemical.", "correct": False,
             "why": "The question states the single meal is safe. What is "
                    "in question is whether repeating it stays safe."},
        ],
        "figure": None,
    },
    {
        "id": "b9-05-e23",
        "band": "easier",
        "text": "Spray A kills insects within minutes and then breaks down "
                "within a day. Spray B takes a week to kill and then lasts "
                "for years in the environment. Which is the greater "
                "long-term risk to a food chain?",
        "options": [
            {"text": "Spray A, because acting within minutes on the insect means far more of the chemical gets absorbed overall.", "correct": False,
             "why": "How fast it acts on the insect it is sprayed on does "
                    "not decide what happens afterwards. Spray A breaks "
                    "down within a day, so nothing is left to concentrate "
                    "up a chain."},
            {"text": "Neither — both are equally risky, since both are "
                     "pesticides.", "correct": False,
             "why": "They are not equal. One breaks down within a day and "
                    "the other lasts for years, and it is persistence that "
                    "decides whether a chain concentrates it."},
            {"text": "Spray B, because it lasts long enough in the "
                     "environment to be taken up repeatedly.",
             "correct": True},
            {"text": "Spray B, because a week to kill means it must be "
                     "more toxic.", "correct": False,
             "why": "How long it takes to kill is not the same as how "
                    "toxic it is, and neither is the reason it is the "
                    "greater risk. What matters here is that it lasts for "
                    "years rather than a day."},
        ],
        "figure": None,
    },
    {
        "id": "b9-05-e24",
        "band": "easier",
        "text": "If an animal takes in a persistent chemical at a steady "
                "rate and none is ever removed, what happens to the total "
                "amount in its body over its life?",
        "options": [
            {"text": "It never stops rising, for as long as the animal "
                     "lives.",
             "correct": True},
            {"text": "It rises then falls back to zero by the time the "
                     "animal dies.", "correct": False,
             "why": "Nothing here removes the chemical, so there is no "
                    "route for the total to fall. Persistent means kept, "
                    "not returned."},
            {"text": "It stays constant from birth, because the first dose "
                     "sets the level for good.", "correct": False,
             "why": "Each new dose adds to what is already there. The "
                    "first dose is not the final amount if intake "
                    "continues."},
            {"text": "It rises and falls with no overall pattern.",
             "correct": False,
             "why": "This intake has a clear pattern — steady in, none "
                    "out — which gives a steadily rising total rather than "
                    "an unpredictable one."},
        ],
        "figure": None,
    },
    {
        "id": "b9-05-e25",
        "band": "easier",
        "text": "A scavenger bird feeds only on the bodies of dead top "
                "predators from a contaminated lake system. Would you "
                "expect it to carry a high or low concentration of a "
                "persistent pollutant?",
        "options": [
            {"text": "Low, because a dead animal has already lost its "
                     "store of the chemical.", "correct": False,
             "why": "Dying does not remove a stored chemical. Whatever "
                    "concentration the predator held in life is still "
                    "there in its body."},
            {"text": "Low, because scavengers are more resistant to "
                     "pollutants than hunters are.", "correct": False,
             "why": "Resistance is not the mechanism here. What decides "
                    "the concentration is what an animal's food has "
                    "already accumulated, not how tolerant it is."},
            {"text": "The same as an animal eating at the very bottom of the chain, since scavenging counts as a completely different kind of feeding altogether.", "correct": False,
             "why": "The kind of feeding does not reset the chain. A "
                    "scavenger eating top predators is still eating food "
                    "that has concentrated the chemical fully."},
            {"text": "High — it is effectively feeding at the very top of "
                     "the chain, on animals that had already concentrated "
                     "the chemical.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b9-05-e26",
        "band": "easier",
        "text": "A bioaccumulation model uses round figures for its "
                "concentrations, rather than measurements from one real "
                "chemical spill. What are round figures like these meant to "
                "show?",
        "options": [
            {"text": "That real bioaccumulation never happens in whole, "
                     "round numbers.", "correct": False,
             "why": "The point is not about whole numbers appearing in "
                    "nature. It is that the pattern — persistence causing a "
                    "climbing concentration — is realistic even though the "
                    "exact figures are chosen for teaching."},
            {"text": "The general pattern that a persistent chemical "
                     "multiplies at every step, even though the exact "
                     "figures are chosen for clarity.", "correct": True},
            {"text": "That DDT concentrations in the real world were measured at exactly these same numbers, in every lake it was ever sprayed near, anywhere on Earth.", "correct": False,
             "why": "Teaching figures like these are of the same order as "
                    "real reported measurements, but are not taken from one "
                    "particular study."},
            {"text": "That bioaccumulation has no basis in real chemistry "
                     "and is purely a teaching idea.", "correct": False,
             "why": "It is very much a real phenomenon, documented in "
                    "cases like DDT and eggshell thinning. Only the "
                    "specific bench figures are simplified for teaching."},
        ],
        "figure": None,
    },
    {
        "id": "b9-05-e27",
        "band": "easier",
        "text": "What did Rachel Carson's book Silent Spring do when it was "
                "published in 1962?",
        "options": [
            {"text": "It banned DDT for agricultural use across most "
                     "countries immediately.", "correct": False,
             "why": "The book itself banned nothing — governments did that "
                    "afterwards, during the 1970s. The book put the "
                    "evidence in front of the public."},
            {"text": "It proved that DDT was completely safe for use "
                     "around farms.", "correct": False,
             "why": "It showed the opposite — evidence of harm to "
                    "wildlife, which is why bans followed it rather than "
                    "continued approval."},
            {"text": "It put evidence of DDT's effects on wildlife in "
                     "front of the public.", "correct": True},
            {"text": "It invented the process of capture–mark–recapture "
                     "for counting wildlife.", "correct": False,
             "why": "Capture–mark–recapture is a method for counting "
                    "animals. Silent Spring is about the evidence for DDT's "
                    "build-up and harm."},
        ],
        "figure": None,
    },
    {
        "id": "b9-05-e28",
        "band": "easier",
        "text": "Why is DDT still used indoors in "
                "some countries today, even though it is banned for farming "
                "almost everywhere?",
        "options": [
            {"text": "Because indoor DDT breaks down before it can enter a "
                     "food chain.", "correct": False,
             "why": "Indoor DDT is no less persistent than outdoor DDT, and "
                    "it would not need to break down for the indoor use to "
                    "make sense — the reason is weighing a present danger "
                    "against a longer-term one."},
            {"text": "Because no other insecticide has ever been invented "
                     "since DDT.", "correct": False,
             "why": "Other insecticides exist. The reason given for "
                    "keeping DDT for this one use is the balance between an "
                    "immediate disease risk and a longer-term ecological "
                    "one."},
            {"text": "Because indoor spraying inside a house never reaches an outdoor food chain in the surrounding countryside at all.", "correct": False,
             "why": "Nobody claims indoor use is fully contained. The "
                    "reason it continues is a deliberate trade-off, not a "
                    "claim of zero risk."},
            {"text": "Because malaria kills people now, and the disease's "
                     "cost is judged greater than the ecological cost.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b9-05-e29",
        "band": "easier",
        "text": "In one lake chain, harm begins once a persistent chemical "
                "passes 100 ppm. The ospreys measure 300 ppm and the perch "
                "measure 30 ppm. Which organisms are above the level that "
                "causes harm?",
        "options": [
            {"text": "Both the perch and the ospreys.", "correct": False,
             "why": "30 ppm is below the 100 ppm harm level. Only the "
                    "ospreys, at 300 ppm, are above it."},
            {"text": "The ospreys only.", "correct": True},
            {"text": "Neither — 100 ppm is never reached anywhere in this "
                     "chain.", "correct": False,
             "why": "The ospreys, at 300 ppm, are three times past that "
                    "level. It is reached and passed at the top of the "
                    "chain."},
            {"text": "The perch only, since they sit just below the "
                     "ospreys.", "correct": False,
             "why": "The perch, at 30 ppm, sit well below the 100 ppm harm "
                    "level. It is the ospreys above them that pass it."},
        ],
        "figure": None,
    },
    {
        "id": "b9-05-e30",
        "band": "easier",
        "text": "For one water-soluble chemical, a lake model reports 'no "
                "measurable effect' at every level, from the lake water to "
                "the ospreys. What does that verdict tell you about the "
                "chemical's behaviour, not about its danger in general?",
        "options": [
            {"text": "That this particular chemical is excreted as fast as "
                     "it arrives, so nothing concentrates.", "correct": True},
            {"text": "That no water-soluble chemical could ever be "
                     "dangerous in any amount.", "correct": False,
             "why": "The verdict is about this chemical's behaviour, not a "
                    "general rule about every water-soluble chemical. It "
                    "reports one case, nothing wider."},
            {"text": "That the lake itself contains no pollution of any "
                     "kind.", "correct": False,
             "why": "The chemical is still present in the water at every "
                    "level — the verdict is about whether it builds up, "
                    "not about whether it is there at all."},
            {"text": "That the chemical has been completely destroyed by the time it has travelled all the way up to the ospreys.", "correct": False,
             "why": "Nothing here destroys the chemical. It is excreted "
                    "rather than destroyed, which is a different process "
                    "with the same practical result: no build-up."},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "b9-05-s09",
        "band": "standard",
        "text": "A persistent chemical starts at 0.002 ppm in the water and "
                "multiplies by ten at each of four feeding steps. What is "
                "the concentration at the top of the chain?",
        "options": [
            {"text": "0.008 ppm, adding a small amount at each step",
             "correct": False,
             "why": "That adds rather than multiplies. Each step "
                    "multiplies the figure by ten instead of adding a "
                    "fixed amount."},
            {"text": "0.2 ppm, two steps of multiplying by ten",
             "correct": False,
             "why": "That is only two of the four steps. Multiplying by "
                    "ten four times over needs the ×10 applied twice "
                    "more."},
            {"text": "20 ppm, four steps of multiplying by ten",
             "correct": True},
            {"text": "200 ppm, five steps of multiplying by ten",
             "correct": False,
             "why": "That is one step too many. The chain here has four "
                    "steps above the water, not five."},
        ],
        "figure": None,
    },
    {
        "id": "b9-05-s10",
        "band": "standard",
        "text": "In a chain, the water measures 0.004 ppm and the algae "
                "immediately above it measure 0.04 ppm. If the same factor "
                "applies at every step, what will the level be two steps "
                "above the algae?",
        "options": [
            {"text": "0.4 ppm, one step above the algae", "correct": False,
             "why": "That is only one step further, not two. The factor "
                    "has to be applied twice from the algae's figure."},
            {"text": "4.0 ppm, two steps above the algae", "correct": True},
            {"text": "0.08 ppm, adding the same amount twice",
             "correct": False,
             "why": "This adds rather than multiplies. The step from water "
                    "to algae was a ×10 multiplication, not an addition."},
            {"text": "40 ppm, three steps above the algae", "correct": False,
             "why": "That applies the factor one time too many. Two steps "
                    "above the algae is 4.0 ppm, not 40 ppm."},
        ],
        "figure": None,
    },
    {
        "id": "b9-05-s11",
        "band": "standard",
        "text": "In river X, a persistent chemical multiplies by ten at "
                "each of four steps. In river Y, the same chemical "
                "multiplies by ten at each of six steps, starting from the "
                "same concentration in the water. How many times higher is "
                "the top of river Y's chain than the top of river X's?",
        "options": [
            {"text": "Ten times higher", "correct": False,
             "why": "Ten times would be the effect of one extra step, not "
                    "two."},
            {"text": "Sixty times higher", "correct": False,
             "why": "This adds the extra steps together rather than "
                    "multiplying the extra factors. Two extra steps of ×10 "
                    "each multiply, giving a hundred, not sixty."},
            {"text": "Two times higher", "correct": False,
             "why": "Two is the number of extra steps, not the size of "
                    "their effect. Each extra step multiplies by ten, so "
                    "two extra steps multiply by a hundred."},
            {"text": "A hundred times higher", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b9-05-s12",
        "band": "standard",
        "text": "A pesticide is approved after being tested only on fish "
                "living directly in treated water. Years later, otters that "
                "eat those fish are found with dangerously high levels. What "
                "did the test fail to allow for?",
        "options": [
            {"text": "That fish are more resistant to pesticides than "
                     "otters are.", "correct": False,
             "why": "Nothing here is about one species being more "
                    "resistant. What was missed is that an animal eating "
                    "many fish accumulates far more than any one fish "
                    "holds."},
            {"text": "That an animal eating the fish would accumulate far "
                     "more than any single fish contains.", "correct": True},
            {"text": "That fish absorb pesticides faster through their "
                     "gills than otters do through their skin.",
             "correct": False,
             "why": "How a chemical is absorbed is not the issue here. The "
                    "issue is what happens after it is absorbed — whether "
                    "it builds up through a chain."},
            {"text": "That the pesticide would somehow become far more toxic once it is safely stored inside a fish's own body.", "correct": False,
             "why": "The chemical is not changed at all once it is inside "
                    "an animal. What changes going up the chain is the "
                    "concentration, not the substance."},
        ],
        "figure": None,
    },
    {
        "id": "b9-05-s13",
        "band": "standard",
        "text": "An eagle's blood tests at 200 ppm for a persistent "
                "chemical that multiplies by about ten at each of three "
                "feeding steps below it. About what concentration would you "
                "expect in the water at the bottom of that chain?",
        "options": [
            {"text": "20 ppm", "correct": False,
             "why": "That divides by ten once. Three steps of ×10 each "
                    "need dividing by ten three times over."},
            {"text": "2,000 ppm", "correct": False,
             "why": "That multiplies rather than divides. Working back "
                    "down a chain, you divide by the per-step factor at "
                    "each step."},
            {"text": "0.2 ppm", "correct": True},
            {"text": "0.02 ppm", "correct": False,
             "why": "That divides one time too many. Three steps of ÷10 "
                    "each from 200 ppm gives 0.2 ppm, not 0.02 ppm."},
        ],
        "figure": None,
    },
    {
        "id": "b9-05-s14",
        "band": "standard",
        "text": "A persistent pesticide is sprayed on fields many "
                "kilometres from the nearest river. Fish caught in that "
                "river years later still show measurable levels. Suggest "
                "how the chemical got there.",
        "options": [
            {"text": "It must have been sprayed directly into the river at "
                     "some point.", "correct": False,
             "why": "Nothing in the case says that happened, and it does "
                    "not need to. A chemical that is not broken down can be "
                    "carried off fields by rain and drainage into rivers."},
            {"text": "Rain and drainage washed it off the fields, into "
                     "streams, and eventually into the river.",
             "correct": True},
            {"text": "Fish swam upstream to the fields and picked it up "
                     "there.", "correct": False,
             "why": "Fish cannot leave a river to visit a field. The "
                    "chemical has to reach the water, not the other way "
                    "round."},
            {"text": "The chemical evaporated from the fields and later "
                     "condensed as rain over the river.", "correct": False,
             "why": "That kind of long-range movement is possible for some "
                    "persistent chemicals, and a much simpler route — being "
                    "washed off the land into the drainage that feeds the "
                    "river — fits fields near a river better."},
        ],
        "figure": None,
    },
    {
        "id": "b9-05-s15",
        "band": "standard",
        "text": "A persistent pesticide was banned twenty years ago. A "
                "local newspaper reports 'the ban means the fish are now "
                "safe to eat.' Is that a safe conclusion?",
        "options": [
            {"text": "Yes — a ban always removes a chemical from the "
                     "environment straight away.", "correct": False,
             "why": "A ban stops new use. It does nothing to chemical that "
                    "is already in the sediment, the water and the "
                    "animals, and a persistent one stays there."},
            {"text": "No — twenty years is nowhere near long enough for any chemical anywhere to properly be considered banned.", "correct": False,
             "why": "The length of a ban is not the issue raised here. The "
                    "issue is whether the chemical already in the "
                    "ecosystem has gone, which persistence says it has "
                    "not."},
            {"text": "No — the chemical already in the ecosystem does not "
                     "disappear just because using more of it is banned.",
             "correct": True},
            {"text": "Yes, because fish only take in chemicals that are "
                     "currently being sprayed.", "correct": False,
             "why": "Fish take in whatever is present in their food and "
                    "water at the time, whether newly sprayed or left over "
                    "from decades ago."},
        ],
        "figure": None,
    },
    {
        "id": "b9-05-s16",
        "band": "standard",
        "text": "Flame retardant chemicals added to furniture and "
                "electronics have been found building up in the eggs of "
                "seabirds far from any city. What must be true of these "
                "chemicals?",
        "options": [
            {"text": "They persist in the environment and are not broken "
                     "down or excreted by the birds.", "correct": True},
            {"text": "They must be extremely toxic in a single dose before they could ever be found there at all.", "correct": False,
             "why": "Toxicity is not what this finding shows. Finding a "
                    "chemical concentrated in eggs shows that it persists "
                    "and accumulates, whatever its toxicity."},
            {"text": "They must be manufactured directly from seabird "
                     "food.", "correct": False,
             "why": "Nothing about how a chemical is manufactured decides "
                    "whether it accumulates. What matters is whether it is "
                    "broken down once it is out in the environment."},
            {"text": "They must dissolve easily in water to travel so "
                     "far.", "correct": False,
             "why": "Persistent, fat-soluble chemicals are the ones that "
                    "travel this way and accumulate — a water-soluble "
                    "chemical would be excreted rather than stored, and "
                    "would not concentrate in an egg."},
        ],
        "figure": None,
    },
    {
        "id": "b9-05-s17",
        "band": "standard",
        "text": "A persistent chemical measures 0.5 mg/kg in small fish and "
                "50 mg/kg in the seals that eat them. How many times higher "
                "is the seal's level?",
        "options": [
            {"text": "5 times", "correct": False,
             "why": "That divides incorrectly. 50 divided by 0.5 is a "
                    "hundred, not five."},
            {"text": "About 10 times", "correct": False,
             "why": "Ten times 0.5 is 5, not 50. Check the division again: "
                    "50 ÷ 0.5 = 100."},
            {"text": "1,000 times", "correct": False,
             "why": "That would need the seal's level to be 500 mg/kg. At "
                    "50 mg/kg, the true multiple is a hundred."},
            {"text": "100 times", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b9-05-s18",
        "band": "standard",
        "text": "Chemical M is never broken down and dissolves in water. "
                "Chemical N is never broken down and dissolves in fat. Both "
                "enter the same lake at the same concentration. Which is "
                "more likely to bioaccumulate up the food chain, and why?",
        "options": [
            {"text": "Chemical M, because being broken down slowly is what "
                     "allows build-up.", "correct": False,
             "why": "Neither chemical is broken down at all — that part is "
                    "the same for both. What differs is whether the body "
                    "can excrete it, and water-soluble chemicals are "
                    "excreted easily."},
            {"text": "Chemical N, because being fat-soluble means it is "
                     "stored in the body rather than excreted.",
             "correct": True},
            {"text": "Neither, because a chemical that is never broken "
                     "down cannot enter a food chain at all.",
             "correct": False,
             "why": "Not being broken down is exactly the property that "
                    "lets a chemical stay in a food chain. It does not "
                    "stop it entering one."},
            {"text": "Both equally, since neither chemical is ever broken "
                     "down.", "correct": False,
             "why": "Not being broken down is only half the story. Whether "
                    "it is stored (fat-soluble) or removed in urine "
                    "(water-soluble) decides whether it actually builds "
                    "up."},
        ],
        "figure": None,
    },
    {
        "id": "b9-05-s19",
        "band": "standard",
        "text": "A rare owl eats only a single vole every few weeks and "
                "nothing else. The vole carries a persistent, fat-soluble "
                "chemical. Would you expect the owl's concentration to climb "
                "the way a top predator eating many contaminated prey a year "
                "would?",
        "options": [
            {"text": "Yes, because the chemical is persistent and "
                     "fat-soluble, which is all that is needed.",
             "correct": False,
             "why": "Persistence is one of the two conditions. The other "
                    "is a predator eating many of the level below across "
                    "its life, which this owl never does."},
            {"text": "No — over a whole life it eats so few voles that "
                     "the toxin of only a handful of bodies is ever "
                     "collected into one.", "correct": True},
            {"text": "Yes, because any predator sitting at the very top of a chain automatically accumulates a persistent chemical regardless.",
             "correct": False,
             "why": "Position at the top is not automatic protection or "
                    "automatic risk on its own — it still depends on how "
                    "much is actually being eaten."},
            {"text": "No, because voles do not carry enough of the "
                     "chemical to matter.", "correct": False,
             "why": "How much one vole carries is not stated as "
                    "negligible; the point here is how few voles this owl "
                    "eats, not how much one contains."},
        ],
        "figure": None,
    },
    {
        "id": "b9-05-s20",
        "band": "standard",
        "text": "Two ospreys hunt the same lake. One eats almost only fish; "
                "the other, more unusually, takes waterfowl that themselves "
                "eat large amounts of fish. Which osprey is likely to carry "
                "the higher concentration of a persistent chemical, and "
                "why?",
        "options": [
            {"text": "The one eating waterfowl, because its food sits one "
                     "feeding step higher up the same chain.",
             "correct": True},
            {"text": "The one eating fish, because fish are more numerous "
                     "and so carry more of the chemical in total.",
             "correct": False,
             "why": "Being more numerous does not raise an individual "
                    "fish's concentration. What raises a predator's own "
                    "concentration is how many steps of concentrating "
                    "stand below its food."},
            {"text": "Both the same, because they hunt the identical "
                     "lake.", "correct": False,
             "why": "Hunting the same lake does not mean eating at the "
                    "same level of the chain. The waterfowl-eating osprey's "
                    "food has already concentrated the chemical once "
                    "more."},
            {"text": "Neither, because ospreys are already sitting at the very top of the chain, regardless of what prey they choose.", "correct": False,
             "why": "Being generally 'at the top' does not fix a number. "
                    "Taking prey that is itself one step higher raises the "
                    "osprey's own concentration further."},
        ],
        "figure": None,
    },
    {
        "id": "b9-05-s21",
        "band": "standard",
        "text": "A persistent chemical measures 0.008 ppm in the water. It "
                "multiplies by ten at each of the next two feeding steps, "
                "reaching the minnows. What is the level in the minnows?",
        "options": [
            {"text": "0.016 ppm, doubling the water figure",
             "correct": False,
             "why": "Doubling would be the result of adding the water "
                    "figure to itself, not of two steps that each multiply "
                    "by ten."},
            {"text": "0.08 ppm, one step of multiplying by ten",
             "correct": False,
             "why": "That is only one step's worth. The minnows are two "
                    "steps above the water, so ten multiplies the figure "
                    "twice."},
            {"text": "0.8 ppm, two steps of multiplying by ten",
             "correct": True},
            {"text": "8 ppm, taking three steps of multiplying by ten each time",
             "correct": False,
             "why": "That is one step too many. Water to minnows is two "
                    "steps, not three."},
        ],
        "figure": None,
    },
    {
        "id": "b9-05-s22",
        "band": "standard",
        "text": "A student says: 'If a chemical measures about the same "
                "concentration in the water as it does in the fish living "
                "there, then it probably is not bioaccumulating.' Is that "
                "reasoning sound?",
        "options": [
            {"text": "Yes — bioaccumulation means the concentration "
                     "climbing at each step, so equal levels suggest "
                     "nothing is building up.", "correct": True},
            {"text": "No — a persistent chemical always ends up being far more concentrated in the fish than it ever is in the water itself.",
             "correct": False,
             "why": "That is usually true for a persistent, fat-soluble "
                    "chemical, and it does not make the student's general "
                    "reasoning wrong. Equal levels really would suggest no "
                    "build-up is happening."},
            {"text": "No — the water level is always the one that "
                     "matters, whatever the fish contain.", "correct": False,
             "why": "It is the comparison between the two levels that "
                    "shows whether something is accumulating, not the "
                    "water figure taken on its own."},
            {"text": "It cannot be judged without knowing how toxic the "
                     "chemical is.", "correct": False,
             "why": "Toxicity decides the danger of whatever concentration "
                    "is found. Whether concentrations are climbing at all "
                    "is a separate question the comparison already "
                    "answers."},
        ],
        "figure": None,
    },
    {
        "id": "b9-05-s23",
        "band": "standard",
        "text": "A chemical is partly broken down at each feeding step, so "
                "only some of each dose is kept. Starting at 0.01 ppm and "
                "multiplying by three at each of four steps, would this "
                "chemical be more, or less, of a build-up risk than one "
                "multiplying by ten at each step from the same start?",
        "options": [
            {"text": "Less of a risk over the same number of steps, but it "
                     "still accumulates rather than staying flat.",
             "correct": True},
            {"text": "More of a risk, because breaking down part of each dose somehow makes the remaining chemical stronger overall.", "correct": False,
             "why": "Nothing about being partly broken down makes a "
                    "chemical stronger. It only removes part of each dose, "
                    "which slows the build-up rather than speeding it."},
            {"text": "The same risk, because both chemicals are described "
                     "as building up.", "correct": False,
             "why": "Multiplying by three each step gives a far smaller "
                    "number after several steps than multiplying by ten "
                    "each step does — the risk is real but smaller."},
            {"text": "No risk at all, because any breakdown at all means "
                     "nothing accumulates.", "correct": False,
             "why": "Partial breakdown means part of the dose is kept, not "
                    "none of it. What remains still adds up over several "
                    "steps, just more slowly."},
        ],
        "figure": None,
    },
    {
        "id": "b9-05-s24",
        "band": "standard",
        "text": "Bats that feed heavily on insects from sprayed farmland "
                "have shown much higher pesticide levels than bats feeding "
                "over unsprayed woodland, even though both catch similar "
                "numbers of insects each night. What is the most likely "
                "reason?",
        "options": [
            {"text": "The insects from sprayed farmland themselves carry "
                     "the chemical, so it is passed on with every catch.",
             "correct": True},
            {"text": "Bats flying over farmland fly noticeably faster, and so absorb far more chemical straight through the air.", "correct": False,
             "why": "Speed of flight is not a route the chemical takes "
                    "into a bat. It arrives through the food, which is the "
                    "insects, not the air."},
            {"text": "Farmland bats simply eat more insects overall than "
                     "woodland bats do.", "correct": False,
             "why": "The two groups are described as catching similar "
                    "numbers. What differs is what their food itself is "
                    "carrying, not how much of it they eat."},
            {"text": "Woodland insects are naturally more resistant to the "
                     "chemical.", "correct": False,
             "why": "Resistance in the insects is not the issue here — "
                    "woodland insects were never sprayed with it in the "
                    "first place, so they were never exposed."},
        ],
        "figure": None,
    },
    {
        "id": "b9-05-s25",
        "band": "standard",
        "text": "A persistent chemical multiplies by ten at each feeding "
                "step. The top of a chain measures ten thousand times the "
                "concentration in the water. How many feeding steps lie "
                "between them?",
        "options": [
            {"text": "Two", "correct": False,
             "why": "Two steps of ×10 each give a hundred times, not ten "
                    "thousand."},
            {"text": "Three", "correct": False,
             "why": "Three steps of ×10 each give a thousand times, not "
                    "ten thousand."},
            {"text": "Four", "correct": True},
            {"text": "Ten thousand", "correct": False,
             "why": "That is the total multiple itself, not the count of "
                    "steps that produced it. Four steps of ×10 each "
                    "multiply out to ten thousand."},
        ],
        "figure": None,
    },
    {
        "id": "b9-05-s26",
        "band": "standard",
        "text": "A country cuts its use of a persistent pesticide by half "
                "every year. A campaigner expects levels in top predators "
                "to fall by half in that same year too. Why might that not "
                "happen?",
        "options": [
            {"text": "Because cutting use by half never actually reduces "
                     "the total amount used.", "correct": False,
             "why": "Halving use each year genuinely reduces the amount "
                    "going in. The issue is not whether less is being "
                    "used, but what happens to what is already out there."},
            {"text": "Because predators would need to breed twice as fast "
                     "to show any change at all.", "correct": False,
             "why": "Breeding rate affects how fast a population "
                    "recovers, not how fast the chemical level in an "
                    "existing animal falls. The chemical itself is simply "
                    "still there."},
            {"text": "Because halving pesticide use always somehow increases the concentration reaching top predators, at least for a while in the short term.", "correct": False,
             "why": "There is no reason a cut in use would raise "
                    "concentrations. Less new pesticide entering the "
                    "system can only help, even if the existing store "
                    "takes years to clear."},
            {"text": "Because the chemical already built up in the "
                     "ecosystem and in the animals does not disappear just "
                     "because less is now being added.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b9-05-s27",
        "band": "standard",
        "text": "A herbivorous fish grazing algae and a predatory fish "
                "hunting smaller fish live in the same lake, at similar "
                "body size. Which is likely to carry a higher concentration "
                "of a persistent, fat-soluble chemical, and why?",
        "options": [
            {"text": "The predatory fish, because its food has already "
                     "concentrated the chemical from the algae upward.",
             "correct": True},
            {"text": "The herbivorous fish, because it eats far more often "
                     "than a predator does.", "correct": False,
             "why": "How often each fish eats is not what is being "
                    "compared here. What matters is how many steps of "
                    "concentrating sit beneath each one's food."},
            {"text": "Both the same, because body size alone is what decides how much any single fish ends up accumulating.", "correct": False,
             "why": "Body size is not the mechanism. Position in the "
                    "chain is, and the predatory fish feeds one step "
                    "higher."},
            {"text": "Neither, because fish of the same lake are always "
                     "exposed to the same water.", "correct": False,
             "why": "Sharing the same water is not the same as sharing "
                    "the same food. The predatory fish's food has already "
                    "passed through an extra feeding step."},
        ],
        "figure": None,
    },
    {
        "id": "b9-05-s28",
        "band": "standard",
        "text": "A stretch of ocean holds 0.001 mg/kg of mercury in its "
                "plankton. Small fish that graze the plankton measure "
                "0.01 mg/kg, and the large predatory fish that eat those "
                "small fish measure 0.1 mg/kg. What multiplying factor is "
                "being applied at each step?",
        "options": [
            {"text": "Two", "correct": False,
             "why": "Doubling would take 0.001 to 0.002, not to 0.01. The "
                    "actual jump each step is much larger than that."},
            {"text": "Five", "correct": False,
             "why": "Five times 0.001 is 0.005, still short of the "
                    "measured 0.01 at the next step."},
            {"text": "Ten", "correct": True},
            {"text": "A hundred", "correct": False,
             "why": "A hundred times 0.001 would be 0.1, which skips the "
                    "small-fish level entirely. Check it one step at a "
                    "time: ×10 each time fits both jumps."},
        ],
        "figure": None,
    },
    {
        "id": "b9-05-s29",
        "band": "standard",
        "text": "A vulture that scavenges dead animals across a large area "
                "eats far more food, in total mass, than a small owl that "
                "eats only a few mice a week. Yet the owl could easily "
                "carry a higher concentration of a persistent pollutant. "
                "How can that be?",
        "options": [
            {"text": "It cannot be — eating a greater total mass of food always means accumulating more of any pollutant present.", "correct": False,
             "why": "Total mass eaten is not what decides concentration. "
                    "What decides it is how many feeding steps lie beneath "
                    "the food, and a scavenger feeding across many species "
                    "and levels is not simply 'higher up' than an owl."},
            {"text": "The vulture must break the chemical down, while the "
                     "owl cannot.", "correct": False,
             "why": "Nothing here suggests the vulture excretes the "
                    "chemical any faster. The comparison is about chain "
                    "position, not about who can break it down."},
            {"text": "Only warm-blooded animals accumulate persistent "
                     "chemicals.", "correct": False,
             "why": "Both the vulture and the owl are warm-blooded, and "
                    "fish and other cold-blooded animals accumulate "
                    "persistent chemicals too. This is not what decides "
                    "it."},
            {"text": "Concentration depends on the chain position of the "
                     "food eaten, not on the total mass of food eaten.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b9-05-s30",
        "band": "standard",
        "text": "A persistent chemical multiplies by ten at each feeding "
                "step. Which would raise the top predator's concentration "
                "more: doubling the starting concentration in the water, or "
                "adding one extra feeding step to the chain?",
        "options": [
            {"text": "Doubling the starting concentration, since it "
                     "directly changes the amount entering the chain.",
             "correct": False,
             "why": "Doubling only ever doubles the final figure. One "
                    "extra step multiplies the final figure by ten, which "
                    "is a far bigger change."},
            {"text": "Both would have exactly the same effect on the "
                     "final concentration.", "correct": False,
             "why": "Doubling multiplies the end result by two; an extra "
                    "step multiplies it by ten. Those are not the same "
                    "effect."},
            {"text": "Neither changes the final concentration, since the "
                     "chemical itself is unchanged.", "correct": False,
             "why": "The chemical being unchanged is true and is not what "
                    "is being asked. Both changes affect how much of it "
                    "collects at the top, even though the substance itself "
                    "stays the same."},
            {"text": "Adding one extra feeding step, since that multiplies "
                     "the final figure by ten rather than by two.",
             "correct": True},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "b9-05-h09",
        "band": "harder",
        "text": "A persistent chemical measures 0.05 ppm in the water. It "
                "multiplies by five at each of three feeding steps to reach "
                "the top predator. Harm begins at 50 ppm. Is the top "
                "predator's level above or below the level that causes "
                "harm?",
        "options": [
            {"text": "Above — the top predator measures 62.5 ppm.",
             "correct": False,
             "why": "That is the right three steps of ×5 worked on "
                    "0.5 ppm instead of 0.05 ppm. From 0.05 ppm the answer "
                    "is 6.25 ppm."},
            {"text": "Below — the top predator measures about 6.25 ppm, "
                     "well under 50 ppm.", "correct": True},
            {"text": "Above — the top predator's level measures out at "
                     "roughly 500 ppm in total.",
             "correct": False,
             "why": "That treats the per-step factor as ten rather than "
                    "five. At ×5 per step the true figure is 6.25 ppm."},
            {"text": "It cannot be worked out without knowing how many "
                     "organisms are at each level.", "correct": False,
             "why": "The number of organisms at each level is not part of "
                    "this calculation. The concentration is worked out "
                    "from the starting figure, the per-step factor and the "
                    "number of steps."},
        ],
        "figure": None,
    },
    {
        "id": "b9-05-h10",
        "band": "harder",
        "text": "A student argues that bioaccumulation is a problem caused "
                "entirely by pesticides, and that banning pesticides "
                "worldwide would end it. Evaluate that claim.",
        "options": [
            {"text": "The claim is correct — no other kind of chemical anywhere in the world is ever both persistent and fat-soluble in exactly the same way.", "correct": False,
             "why": "Mercury and industrial chemicals such as PCBs are "
                    "neither pesticides nor broken down by living things, "
                    "and they bioaccumulate in exactly the same way."},
            {"text": "The claim is correct, because only farmland "
                     "chemicals ever enter a food chain.", "correct": False,
             "why": "Chemicals from factories, mining and other "
                    "industries reach food chains too, through rivers, "
                    "air and the sea, without ever being sprayed as a "
                    "pesticide."},
            {"text": "The claim cannot be evaluated without knowing which "
                     "pesticides are meant.", "correct": False,
             "why": "The claim can be tested against what bioaccumulation "
                    "actually needs — persistence and storage in the "
                    "body — and pesticides are only one source of "
                    "chemicals with those properties."},
            {"text": "The claim is wrong — other persistent, fat-soluble "
                     "substances, such as mercury and industrial "
                     "chemicals, bioaccumulate the same way.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b9-05-h11",
        "band": "harder",
        "text": "A factory upstream releases a persistent, fat-soluble "
                "chemical into a stream once. Dragonfly larvae there graze "
                "algae, and fish eat the larvae, and herons eat the fish. "
                "Which organism would you expect to be affected LAST, and "
                "why?",
        "options": [
            {"text": "The algae, because producers absorb chemicals "
                     "directly from the water.", "correct": False,
             "why": "The algae are exposed first, right at the bottom of "
                    "the chain, not last. Being a producer does not delay "
                    "exposure."},
            {"text": "The dragonfly larvae, because insects are more "
                     "sensitive to pollution than fish are.", "correct": False,
             "why": "Sensitivity is not what this question is about. "
                    "Position in the chain, not sensitivity, decides the "
                    "order effects show up in."},
            {"text": "The herons, because their food has already passed "
                     "through two extra feeding steps that each "
                     "concentrate the chemical further.", "correct": True},
            {"text": "All four organisms are affected at exactly the same moment in time, since the release into the stream only ever happened the once.",
             "correct": False,
             "why": "A single release still travels through the chain "
                    "step by step. The concentration reaching each "
                    "organism, and the time it takes, both depend on how "
                    "many feeding steps stand below it."},
        ],
        "figure": None,
    },
    {
        "id": "b9-05-h12",
        "band": "harder",
        "text": "A student claims that because about ten per cent of "
                "energy passes on at each feeding step, exactly ten times "
                "the concentration of any toxin must also pass on at each "
                "step. Is that reasoning sound?",
        "options": [
            {"text": "Yes — the two figures must be the same, because concentration and energy both travel through a food chain by the same underlying process.", "correct": False,
             "why": "They come from two different processes. Energy loss "
                    "is about respiration and movement; toxin "
                    "concentration is about what is stored versus what is "
                    "excreted, and the two numbers do not have to match."},
            {"text": "No — the ×10 figure for this chemical comes from its own storage and excretion, not from the ×10 energy rule, and a different chemical's factor would not have to match it.", "correct": True},
            {"text": "No, because energy and toxins always move through a food chain in exactly the same direction, from what is eaten to what eats it.", "correct": False,
             "why": "They do move in the same direction, from eaten to "
                    "eater, and that shared direction is not what makes "
                    "the reasoning wrong. What is wrong is assuming the "
                    "two numbers must be linked."},
            {"text": "Yes, because nothing passing through a food chain can ever multiply by a different factor from the fixed ten per cent energy loss.",
             "correct": False,
             "why": "One chemical may multiply by ×10 at each step, "
                    "another by ×3 and another not at all, none of which is "
                    "forced to match the energy figure."},
        ],
        "figure": None,
    },
    {
        "id": "b9-05-h13",
        "band": "harder",
        "text": "Marine food chains often run to five or six feeding "
                "steps; many land food chains stop at three or four. What "
                "does that suggest about persistent chemical risk in the "
                "two settings?",
        "options": [
            {"text": "Land chains carry the greater risk, because land "
                     "chemicals are usually more toxic.", "correct": False,
             "why": "Nothing here compares toxicity between settings. The "
                    "comparison is about chain length, and land chains are "
                    "described as the shorter ones."},
            {"text": "Both settings carry an identical risk overall, since exactly the same chemicals are commonly used both on land and at sea.",
             "correct": False,
             "why": "Even the same chemical, at the same starting "
                    "concentration, ends up far more concentrated after "
                    "five or six multiplying steps than after three or "
                    "four."},
            {"text": "Marine chains can carry a greater risk at the top, "
                     "because more feeding steps mean more multiplying.",
             "correct": True},
            {"text": "Neither setting carries any special risk, because "
                     "concentration depends only on the chemical, not on "
                     "chain length.", "correct": False,
             "why": "Chain length is one of the two things that decide "
                    "how far a chemical concentrates — the chemical's own "
                    "properties are the other."},
        ],
        "figure": None,
    },
    {
        "id": "b9-05-h14",
        "band": "harder",
        "text": "A persistent chemical enters a chain at 0.1 ppm and "
                "multiplies by ten at every feeding step. Harm begins at "
                "500 ppm. What is the smallest number of feeding steps "
                "needed before the concentration first passes 500 ppm?",
        "options": [
            {"text": "Three — the concentration reaches 500 ppm exactly.",
             "correct": False,
             "why": "Three steps give 100 ppm, which is still below "
                    "500 ppm. It has not yet passed it."},
            {"text": "Two — because ten squared is a hundred, close to "
                     "five hundred.", "correct": False,
             "why": "Two steps give 10 ppm, nowhere close to 500 ppm. A "
                    "hundred is what three steps give, and that is still "
                    "below the threshold."},
            {"text": "Four — three steps give 100 ppm, still below the "
                     "threshold, and a fourth step takes it to 1,000 ppm.",
             "correct": True},
            {"text": "Five — because a persistent chemical realistically needs one extra feeding step built in as a safety margin.", "correct": False,
             "why": "There is no such margin built in. Four steps are "
                    "already enough to pass 500 ppm; a fifth is not needed "
                    "to answer the question asked."},
        ],
        "figure": None,
    },
    {
        "id": "b9-05-h15",
        "band": "harder",
        "text": "The usual explanation for a persistent chemical building "
                "up is that it dissolves in fat rather than water. "
                "Methylmercury, a form of mercury found in fish, is not "
                "especially fat-soluble, yet it still bioaccumulates "
                "strongly. What does that suggest?",
        "options": [
            {"text": "That methylmercury cannot really be bioaccumulating at all, since its behaviour clearly breaks the general rule that only fat-soluble chemicals build up.",
             "correct": False,
             "why": "Methylmercury really is documented as bioaccumulating "
                    "strongly in fish and the animals that eat them. What "
                    "breaks is the assumption that fat-solubility is the "
                    "only route to not being excreted."},
            {"text": "That storage can happen by more than one mechanism — "
                     "fat-solubility is one route to not being excreted, "
                     "but not the only possible one.", "correct": True},
            {"text": "That the whole idea of bioaccumulation must be "
                     "wrong.", "correct": False,
             "why": "Bioaccumulation is well documented for many "
                    "chemicals, methylmercury included. One chemical not "
                    "fitting the simplest mechanism does not undo the "
                    "wider pattern."},
            {"text": "That mercury is not persistent, since it does not "
                     "follow the fat-solubility rule.", "correct": False,
             "why": "Persistence and the storage mechanism are two "
                    "different properties. Mercury is famously "
                    "persistent — it is not broken down at all — "
                    "regardless of how it is stored."},
        ],
        "figure": None,
    },
    {
        "id": "b9-05-h16",
        "band": "harder",
        "text": "DDT reached ospreys mainly through farmland spraying "
                "washing into lakes. Mercury reaching similar birds today "
                "often comes from coal-burning power stations, entering the "
                "air before settling in water. What do the two cases have "
                "in common, despite the different sources?",
        "options": [
            {"text": "Both chemicals are pesticides, sprayed for the same "
                     "purpose.", "correct": False,
             "why": "Mercury is not a pesticide and is never sprayed on "
                    "crops. What the two cases share is not their "
                    "source."},
            {"text": "Both chemicals were banned in the same decade, for "
                     "the same reason.", "correct": False,
             "why": "Their regulatory histories differ, and that is not "
                    "the shared feature this question is pointing at — the "
                    "shared mechanism of build-up is."},
            {"text": "Neither chemical is particularly fat-soluble, so by that reasoning neither of them should really accumulate at all.", "correct": False,
             "why": "Both are stored rather than readily excreted, by "
                    "whatever mechanism, which is exactly why both "
                    "accumulate — the claim that neither should is not "
                    "supported."},
            {"text": "Both are persistent chemicals that, once in the "
                     "water, concentrate up the food chain in the same "
                     "way.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b9-05-h17",
        "band": "harder",
        "text": "Chemical P starts at 0.02 ppm and multiplies by ten at "
                "each of three steps. Chemical Q starts at 0.2 ppm and "
                "multiplies by two at each of three steps. Which reaches "
                "the higher concentration at the top, and by roughly how "
                "much?",
        "options": [
            {"text": "Chemical Q, because it starts ten times higher than "
                     "chemical P.", "correct": False,
             "why": "Starting higher is outweighed here by the much "
                    "larger per-step factor chemical P has. P ends up the "
                    "higher of the two despite starting lower."},
            {"text": "Both chemicals reach the very same final concentration, since both of them undergo exactly three feeding steps in total.", "correct": False,
             "why": "The number of steps being equal does not make the "
                    "results equal — the per-step factor is ten for P and "
                    "only two for Q, which makes a very large difference "
                    "over three steps."},
            {"text": "Chemical Q, because a smaller per-step factor is "
                     "safer and therefore leaves more of the chemical.",
             "correct": False,
             "why": "A smaller per-step factor means less multiplying, "
                    "which leaves less of the chemical at the top, not "
                    "more. Chemical P's larger factor is what takes it "
                    "higher."},
            {"text": "Chemical P, reaching about 20 ppm against chemical "
                     "Q's 1.6 ppm — roughly twelve times higher.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b9-05-h18",
        "band": "harder",
        "text": "A person who eats a top predator fish just once a month "
                "argues that bioaccumulation cannot be a risk to them, "
                "since the fish, not the person, is what has been building "
                "up the chemical for years. Is that reasoning sound?",
        "options": [
            {"text": "Yes — bioaccumulation happens only ever inside the fish's own body itself, and a person eating it just occasionally is never really part of that ongoing process.", "correct": False,
             "why": "A person is themselves an organism that can go on to "
                    "store what it takes in. Eating a top predator "
                    "regularly, even once a month over years, can add to a "
                    "person's own long-term levels."},
            {"text": "Yes, because the fish's concentration falls to zero "
                     "the moment it is caught.", "correct": False,
             "why": "Nothing about being caught changes what is stored in "
                    "the fish's body. The concentration built up over its "
                    "life is still there when it is eaten."},
            {"text": "No, because eating fish at all makes bioaccumulation "
                     "certain regardless of how often.", "correct": False,
             "why": "Frequency does matter — the person's own "
                    "concentration builds from repeated intake, so eating "
                    "far less often genuinely does change the risk, even "
                    "though it does not remove it completely."},
            {"text": "Not entirely — the person is also an organism that "
                     "can store and accumulate a persistent chemical, even "
                     "if less of it arrives less often.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b9-05-h19",
        "band": "harder",
        "text": "A safety limit for a persistent chemical is set by "
                "testing a two-step chain (water to small fish) and finding "
                "the concentration safe. The same chemical is later found "
                "at dangerous levels in ospreys at the top of a five-step "
                "chain. What was the flaw in using the two-step test to set "
                "the limit?",
        "options": [
            {"text": "The two-step test used the wrong species of fish.",
             "correct": False,
             "why": "The species is not named as the problem. The flaw is "
                    "that the test only reached two feeding steps, while "
                    "the real risk sits three steps further up."},
            {"text": "The test never reached the extra feeding steps where "
                     "the concentration climbs much higher.",
             "correct": True},
            {"text": "There is no flaw — a safety limit only ever needs to "
                     "be tested at the bottom of a chain.", "correct": False,
             "why": "That is the flaw itself, restated as though it were "
                    "correct. A concentration safe near the bottom can be "
                    "far above harm three steps higher up."},
            {"text": "The chemical must have changed between the two-step "
                     "test and the five-step chain.", "correct": False,
             "why": "The molecule does not change anywhere in the chain. "
                    "What changes between the two tests is simply how many "
                    "multiplying steps stand below the point being "
                    "measured."},
        ],
        "figure": None,
    },
    {
        "id": "b9-05-h20",
        "band": "harder",
        "text": "Persistent chemicals in the ocean often stick to tiny "
                "pieces of plastic, which plankton mistake for food. Fish "
                "eat the plankton, and seabirds eat the fish. "
                "Would you expect a seabird eating fish from a "
                "heavily plastic-polluted area to carry a higher or lower "
                "concentration than one from a clean area, assuming both "
                "eat the same amount of fish?",
        "options": [
            {"text": "Higher — more of the chemical is entering the base "
                     "of the chain, so more is available to concentrate "
                     "upward.", "correct": True},
            {"text": "Lower — the plastic traps the chemical, preventing "
                     "it from ever reaching the plankton.", "correct": False,
             "why": "The plankton are described as eating the plastic "
                    "itself, along with whatever has stuck to it. Trapping "
                    "does not stop it entering the chain — it is the "
                    "route in."},
            {"text": "The same — the amount of fish eaten is what decides "
                     "a seabird's concentration, not where the fish came "
                     "from.", "correct": False,
             "why": "How much fish is eaten is not the only factor. How "
                    "contaminated that fish's own food chain has been is "
                    "what changes between a polluted and a clean area."},
            {"text": "It cannot be predicted, since plastic and pesticides "
                     "work in completely different ways.", "correct": False,
             "why": "They work by the same principle for this purpose — "
                    "something persistent enters the bottom of a chain and "
                    "something above it eats many of the level below. The "
                    "vehicle differs; the mechanism does not."},
        ],
        "figure": None,
    },
    {
        "id": "b9-05-h21",
        "band": "harder",
        "text": "A persistent chemical multiplies by ten at each of the "
                "first two feeding steps and then by three at the third and "
                "final step, reaching 60 ppm at the top. What was the "
                "concentration in the water at the start?",
        "options": [
            {"text": "0.6 ppm", "correct": False,
             "why": "That undoes the two ×10 steps but leaves the ×3 step "
                    "in place. Divide 60 by three as well and the water "
                    "figure is 0.2 ppm."},
            {"text": "About 2 ppm", "correct": False,
             "why": "That undoes two of the three steps. One more "
                    "division — by the first ×10 step — is still needed, "
                    "giving 0.2 ppm."},
            {"text": "0.2 ppm", "correct": True},
            {"text": "6 ppm", "correct": False,
             "why": "That divides 60 by ten only once, missing the second "
                    "×10 step and the ×3 step entirely."},
        ],
        "figure": None,
    },
    {
        "id": "b9-05-h22",
        "band": "harder",
        "text": "A company redesigns a pesticide to be broken down within "
                "a week instead of persisting for decades, but the new "
                "version is somewhat more toxic per dose to the insects it "
                "targets. From the point of view of food-chain build-up, is "
                "this redesign likely to help or harm wildlife further up "
                "the chain?",
        "options": [
            {"text": "It is likely to help, because losing persistence "
                     "removes the ability to bioaccumulate at all, "
                     "whatever the per-dose toxicity.", "correct": True},
            {"text": "It is likely to harm, because a chemical that is more toxic per dose is always going to be worse for wildlife, regardless of how long it lasts in the environment.", "correct": False,
             "why": "How toxic a single dose is affects the risk to "
                    "whatever eats it directly and soon after. It says "
                    "nothing about whether the chemical concentrates up a "
                    "chain over years, which is what stops happening once "
                    "it is no longer persistent."},
            {"text": "It makes no difference, since toxicity and "
                     "persistence always move together.", "correct": False,
             "why": "They are independent properties, and this exact "
                    "redesign is a case of them moving in opposite "
                    "directions — toxicity up, persistence down."},
            {"text": "It cannot be judged, because nothing has been said "
                     "about how it dissolves in fat or water.",
             "correct": False,
             "why": "Persistence alone is decisive here: something broken "
                    "down within a week is not present long enough to "
                    "accumulate regardless of its solubility."},
        ],
        "figure": None,
    },
    {
        "id": "b9-05-h23",
        "band": "harder",
        "text": "A specialist predator eats only one prey species, all of "
                "it contaminated with a persistent chemical from the same "
                "source. A generalist predator eats five different prey "
                "species, only one of which is contaminated. Both eat "
                "similar total amounts of food. Which is likely to carry "
                "the higher concentration?",
        "options": [
            {"text": "The specialist, because all of its intake comes "
                     "from the contaminated route, while the generalist's "
                     "is diluted across four uncontaminated sources.",
             "correct": True},
            {"text": "The generalist, because eating a much wider variety of prey exposes it to a far greater range of chemicals overall, from many different sources.", "correct": False,
             "why": "Being exposed to a wider variety is not the same as "
                    "taking in more of this chemical. Four of the "
                    "generalist's five foods are described as "
                    "uncontaminated."},
            {"text": "Both the same, since both eat a similar total amount "
                     "of food.", "correct": False,
             "why": "Total amount eaten is not what decides concentration "
                    "here — what fraction of that food carries the "
                    "chemical is, and for the specialist that fraction is "
                    "everything."},
            {"text": "Neither, because being a specialist or generalist "
                     "has no bearing on bioaccumulation.", "correct": False,
             "why": "It has a direct bearing here: it decides what "
                    "fraction of an animal's diet is exposed to the "
                    "contaminated source."},
        ],
        "figure": None,
    },
    {
        "id": "b9-05-h24",
        "band": "harder",
        "text": "Ecologists want to stop a persistent chemical from "
                "bioaccumulating further up a particular chain, without "
                "being able to remove the chemical itself. Which single "
                "change would do the most to stop the build-up?",
        "options": [
            {"text": "The only change that stops it directly is breaking "
                     "the feeding link that carries it — for instance, if "
                     "the top predator switched entirely to an "
                     "uncontaminated food source.", "correct": True},
            {"text": "Reducing the number of top predators in the chain.",
             "correct": False,
             "why": "Fewer top predators would each still accumulate the "
                    "chemical from what they eat. Reducing their number "
                    "does not change the concentration each one reaches."},
            {"text": "Increasing the number of organisms at the bottom of "
                     "the chain.", "correct": False,
             "why": "More organisms at the bottom does not dilute the "
                    "concentration each one carries or interrupt how it is "
                    "passed on upward."},
            {"text": "Waiting for natural breakdown to happen on its own, since every chemical eventually degrades given enough time in the environment.", "correct": False,
             "why": "The chemical is described as persistent, meaning it "
                    "is not broken down on any useful timescale. Waiting "
                    "does not interrupt anything here."},
        ],
        "figure": None,
    },
    {
        "id": "b9-05-h25",
        "band": "harder",
        "text": "Some sources use 'biomagnification' for the concentration "
                "increasing from one feeding level to the next, and reserve "
                "'bioaccumulation' for what happens inside a single "
                "organism across its own lifetime. Using that distinction, "
                "which process explains why the osprey's level is so much "
                "higher than the water fleas', and which explains why an "
                "old osprey holds more than a young one?",
        "options": [
            {"text": "Biomagnification explains both differences.",
             "correct": False,
             "why": "Biomagnification is the between-level increase. The "
                    "age difference within one species is explained by "
                    "build-up over time in a single organism, which is "
                    "bioaccumulation."},
            {"text": "Bioaccumulation explains both differences.",
             "correct": False,
             "why": "The jump from water fleas to ospreys is a difference "
                    "between feeding levels, which the distinction assigns "
                    "to biomagnification, not to build-up within one "
                    "organism."},
            {"text": "Neither term really applies any more once a food chain has grown long enough to reach five or more feeding levels in total length.", "correct": False,
             "why": "Chain length does not retire either term. Both "
                    "processes are still happening at every level of a "
                    "long chain, exactly as at a short one."},
            {"text": "Biomagnification explains the difference between "
                     "levels; bioaccumulation explains the difference "
                     "between ages within one level.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b9-05-h26",
        "band": "harder",
        "text": "Regulators want a chain in which the top predator's "
                "concentration never exceeds 200 ppm for a persistent "
                "chemical that starts at 0.01 ppm and multiplies by ten at "
                "each step. What is the maximum number of feeding steps "
                "that chain could safely have?",
        "options": [
            {"text": "Three, since three steps already reach a large "
                     "concentration.", "correct": False,
             "why": "Three steps give 10 ppm, well under the 200 ppm "
                    "limit — a fourth step is still safe."},
            {"text": "Five, since the regulation set by the regulators only ever cares about the single final figure produced at the very end.", "correct": False,
             "why": "Five steps give 1,000 ppm, five times over the "
                    "200 ppm limit. That chain would not meet the "
                    "regulation."},
            {"text": "Four, since four steps give 100 ppm, under the "
                     "limit, while a fifth would give 1,000 ppm, over it.",
             "correct": True},
            {"text": "It cannot have any feeding steps at all above the water if the final concentration must stay under 200 ppm.", "correct": False,
             "why": "Even four steps of multiplying by ten from 0.01 ppm "
                    "stay under 200 ppm, at 100 ppm. A chain can safely "
                    "have several steps here."},
        ],
        "figure": None,
    },
    {
        "id": "b9-05-h27",
        "band": "harder",
        "text": "Peregrine falcon numbers recovered within a few decades "
                "of DDT being banned in most countries. Some seabird "
                "populations exposed to older, still-persisting industrial "
                "chemicals in sediment have recovered far more slowly. What "
                "is the most likely reason for the difference?",
        "options": [
            {"text": "The chemicals reaching the seabirds are still "
                     "present in the sediment and continuing to enter the "
                     "chain, unlike DDT which stopped being added.",
             "correct": True},
            {"text": "Peregrine falcons breed unusually slowly compared to "
                     "seabirds.", "correct": False,
             "why": "Peregrines are not fast breeders either, and "
                    "breeding rate is not the reason given here — whether "
                    "the source chemical is still entering the chain is."},
            {"text": "Seabirds are simply far more sensitive to this particular kind of ongoing chemical pollution than peregrine falcons have ever needed to be, generation after generation.", "correct": False,
             "why": "Sensitivity is not what the scenario compares. It "
                    "compares whether the chemical is still being added "
                    "to the environment or not."},
            {"text": "DDT was never actually removed from the environment "
                     "either.", "correct": False,
             "why": "DDT use was stopped, which is exactly what let the "
                    "falcons' exposure fall over time. The seabirds' case "
                    "differs because their chemical source has not "
                    "stopped."},
        ],
        "figure": None,
    },
    {
        "id": "b9-05-h28",
        "band": "harder",
        "text": "Which of these actions would most directly lower the "
                "concentration already present in a population of ospreys, "
                "rather than just stopping it from getting any worse?",
        "options": [
            {"text": "Banning further use of the persistent chemical.",
             "correct": False,
             "why": "A ban stops new pesticide entering the system, which "
                    "helps in the long run. It does not remove what is "
                    "already stored in the ospreys or their food."},
            {"text": "Passing a stronger new law that makes it formally illegal for anyone to deliberately harm or disturb a wild osprey in any way.", "correct": False,
             "why": "Legal protection from hunting or disturbance does "
                    "nothing to the chemical already inside an osprey's "
                    "body."},
            {"text": "Nothing directly and quickly — a persistent chemical "
                     "is never broken down or excreted fast enough to bring "
                     "the level down in a hurry.", "correct": True},
            {"text": "Moving the ospreys to a chemical-free lake.",
             "correct": False,
             "why": "Moving to clean water would stop further intake, and "
                    "it would not remove what a bird has already "
                    "accumulated over its life, since the chemical is not "
                    "excreted."},
        ],
        "figure": None,
    },
    {
        "id": "b9-05-h29",
        "band": "harder",
        "text": "Chain A reaches a thousand-fold concentration over two "
                "steps (roughly ×32 each); chain B reaches the same "
                "thousand-fold concentration over six steps (roughly ×3 "
                "each). Both end with the same concentration at the top. "
                "Is the risk to the top predator therefore identical in "
                "both chains?",
        "options": [
            {"text": "Yes — an identical top concentration between the two chains must always mean an identical risk to the animal there.", "correct": False,
             "why": "The chemical concentration is the same, and that is "
                    "not the whole of what matters here — how many "
                    "feeding steps, and so how much energy has been lost, "
                    "differs sharply between the two chains."},
            {"text": "Not entirely — chain B's predator sits six energy-losing steps up rather than two, and so is likely a far rarer animal.", "correct": True},
            {"text": "No, because a longer chain always ends up producing a lower final concentration at the very top of it than a shorter one.", "correct": False,
             "why": "The question fixes both chains at the same final "
                    "concentration despite their different lengths, so "
                    "that is not the difference being asked about."},
            {"text": "No, because chain A's own per-step multiplying factor of about thirty-two is simply far too large to be realistic in nature.", "correct": False,
             "why": "Realism of the exact factor is not what is being "
                    "tested. The question is about what else differs "
                    "between the two chains besides the final "
                    "concentration."},
        ],
        "figure": None,
    },
    {
        "id": "b9-05-h30",
        "band": "harder",
        "text": "Two lakes are contaminated with the same persistent "
                "chemical at the same starting concentration. Lake 1 has a "
                "short food chain and was contaminated recently. Lake 2 has "
                "a long food chain and was contaminated decades ago. Which "
                "lake's top predator is likely to carry the highest "
                "concentration, and why?",
        "options": [
            {"text": "Lake 1, because a recent contamination means a "
                     "fresher, more concentrated chemical.", "correct": False,
             "why": "The chemical itself does not lose or gain strength "
                    "with time — it is either present or removed. What "
                    "changes with time is how much has been able to build "
                    "up."},
            {"text": "Both lakes equally, since they started with the "
                     "same concentration in the water.", "correct": False,
             "why": "The starting concentration is only one of the "
                    "factors that matter. Chain length and how long the "
                    "exposure has lasted both change how far it "
                    "climbs."},
            {"text": "Neither lake shows any build-up, since both started "
                     "at the same low concentration.", "correct": False,
             "why": "A low starting concentration does not rule out "
                    "build-up — a few thousandths of a part per million in "
                    "the water can still reach hundreds of parts per "
                    "million at the top of a long chain."},
            {"text": "Lake 2, because both a longer chain and a longer "
                     "exposure time favour a higher build-up.",
             "correct": True},
        ],
        "figure": None,
    },
]
