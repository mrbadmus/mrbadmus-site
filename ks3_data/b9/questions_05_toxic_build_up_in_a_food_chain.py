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
]
