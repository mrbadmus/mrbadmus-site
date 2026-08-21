"""C7 lesson 03 — Endothermic reactions: twelve questions (MRB-272).

The lesson's argument is one shape: an endothermic change takes energy IN from
its surroundings, so the surroundings get colder — and nothing has produced
cold, because there is no such thing to produce. The page teaches it by sorting
eight changes with three reversal pairs among them, so these twelve probe the
angles the mastery ladder leaves alone: what a falling thermometer is actually
reporting, where the energy went, and what reversing a change does to the
direction of the transfer.

The distractors are built from the lesson's two declared misconceptions.

`ENER-05` (an endothermic reaction produces cold) drives the wrong options in
e01, e03, s02 and h01. Each treats cold as a substance that can be made,
released or pumped. h01 is the one that matters: it puts the belief in front of
a fridge, where a student can check it against an appliance in their own
kitchen and find the heat coming off the back.

`ENER-06` (melting and freezing both take energy in, because both involve ice)
drives e04, s01 and h03, where the same substance is treated as deciding the
direction. h03 removes ice from the question altogether and asks about
photosynthesis and respiration instead, so the belief has nothing to hold on
to.

A third strand, on the page and in neither register entry, is that energy which
a thermometer cannot see must have been destroyed. e02, s03, s04 and h04 are
built on it: an endothermic reaction stores energy in its products, and running
it backwards gets it out again.

⚠️ MRB-278 · ANSWER POSITION. The correct answer's index cycles 0, 1, 2, 3
through each band, so this file holds three of each.

Every question here is new prose, and the bar is §13's: each distractor is a
WRONG RULE in the correct answer's own shape, at the correct answer's own
length, and each is a mistake a real student actually makes.
"""

UNIT = "C7"
LESSON = "endothermic-reactions"
LESSON_NUMBER = 3

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "c7-03-e01",
        "band": "easier",
        "text": "Two powders at 20 °C are stirred into water and the "
                "thermometer falls to 12 °C. What has happened?",
        "options": [
            {"text": "Energy has been taken in from the surroundings by the "
                     "reaction", "correct": True},
            {"text": "Cold has been produced by the reaction and released "
                     "into the water", "correct": False,
             "why": "There is no such substance as cold. Nothing was "
                    "produced; energy was removed."},
            {"text": "Energy has been destroyed, which is why the reading "
                     "went down", "correct": False,
             "why": "Energy is never destroyed. It is stored in the new "
                    "substances, where a thermometer cannot read it."},
            {"text": "One of the powders must have been colder than it "
                     "looked", "correct": False,
             "why": "Both were at 20 °C, the same as the water. The fall "
                    "happened only after they were stirred in."},
        ],
        "figure": None,
    },
    {
        "id": "c7-03-e02",
        "band": "easier",
        "text": "Which of these changes is endothermic?",
        "options": [
            {"text": "Burning natural gas on a hob", "correct": False,
             "why": "Combustion is exothermic, always. The whole reason for "
                    "burning anything is the energy it gives out."},
            {"text": "Heating copper carbonate until it decomposes",
             "correct": True},
            {"text": "Neutralising an acid with an alkali in a beaker",
             "correct": False,
             "why": "Neutralisation is exothermic — the mixture warms by "
                    "several degrees, which you measured in the acids unit."},
            {"text": "Respiring glucose in a living cell", "correct": False,
             "why": "Respiration is exothermic. It is why a crowded room "
                    "warms up."},
        ],
        "figure": None,
    },
    {
        "id": "c7-03-e03",
        "band": "easier",
        "text": "An instant cold pack is squeezed and drops close to 0 °C. "
                "Which statement is correct?",
        "options": [
            {"text": "The pack contains something extremely cold that is "
                     "released when it is squeezed", "correct": False,
             "why": "Everything in the pack was at room temperature a moment "
                    "before. Nothing cold was in there to release."},
            {"text": "The pack manufactures cold, which is why it works "
                     "without a freezer", "correct": False,
             "why": "Cold cannot be manufactured. What the pack does is take "
                    "energy in as the ammonium nitrate dissolves."},
            {"text": "The dissolving takes energy in from the water, which "
                     "therefore gets colder", "correct": True},
            {"text": "Squeezing the pack cools it by compressing the gas "
                     "inside", "correct": False,
             "why": "There is no gas involved. Squeezing bursts a pouch of "
                    "water so the solid can dissolve."},
        ],
        "figure": None,
    },
    {
        "id": "c7-03-e04",
        "band": "easier",
        "text": "Melting is endothermic. What does that tell you about "
                "freezing?",
        "options": [
            {"text": "Freezing is endothermic too, because both changes "
                     "involve ice", "correct": False,
             "why": "The substance does not decide it; the direction does. "
                    "Freezing is melting run backwards."},
            {"text": "Freezing involves no energy change, because nothing is "
                     "being heated", "correct": False,
             "why": "A freezer removes energy continuously, and that energy "
                    "is coming out of the water."},
            {"text": "Freezing depends on how cold the freezer is set",
             "correct": False,
             "why": "The freezer's setting changes how FAST it freezes, not "
                    "which way the energy travels."},
            {"text": "Freezing is exothermic, and gives out the same energy "
                     "melting took in", "correct": True},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "c7-03-s01",
        "band": "standard",
        "text": "Photosynthesis is endothermic and respiration is exothermic. "
                "What is the relationship between the two?",
        "options": [
            {"text": "They are unrelated reactions that happen to run in "
                     "opposite directions by coincidence", "correct": False,
             "why": "It is no coincidence. One is very nearly the reverse of "
                    "the other, which is why their energy accounts mirror."},
            {"text": "Respiration releases the energy photosynthesis stored, "
                     "because it is the reverse change", "correct": True},
            {"text": "Photosynthesis stores energy and respiration destroys "
                     "it, which is why food runs out", "correct": False,
             "why": "Nothing is destroyed. Respiration transfers the stored "
                    "energy to where a body can use it."},
            {"text": "Both take energy in, because both are reactions that "
                     "living things have to work at", "correct": False,
             "why": "Respiration gives energy out. If it did not, no animal "
                    "could move."},
        ],
        "figure": None,
    },
    {
        "id": "c7-03-s02",
        "band": "standard",
        "text": "A student says a fridge works by making cold and pumping it "
                "into the food compartment. What is wrong with that?",
        "options": [
            {"text": "Nothing is wrong — that is exactly how a compressor "
                     "fridge works", "correct": False,
             "why": "No part of a fridge makes cold. What the compressor does "
                    "is move energy out of the food."},
            {"text": "The fridge makes cold at the back, not the front, so "
                     "the direction is reversed", "correct": False,
             "why": "The back is where the energy is DUMPED, which is why it "
                    "feels warm. Nothing cold is made anywhere."},
            {"text": "Cold is not a substance. The fridge moves energy out of "
                     "the food and releases it at the back", "correct": True},
            {"text": "A fridge does not change the energy at all — it only "
                     "stops warm air getting in", "correct": False,
             "why": "Insulation helps, but a fridge full of warm food gets "
                    "cold, which insulation alone could never do."},
        ],
        "figure": None,
    },
    {
        "id": "c7-03-s03",
        "band": "standard",
        "text": "Would an endothermic reaction be any use as a fuel?",
        "options": [
            {"text": "Yes, and a very efficient one, because it wastes no "
                     "energy as heat", "correct": False,
             "why": "It gives no energy out at all — so there is nothing to "
                    "be efficient with."},
            {"text": "Yes, but only in a sealed engine where the energy "
                     "cannot escape", "correct": False,
             "why": "Sealing it changes nothing. Energy would still have to "
                    "be supplied continuously to make it run."},
            {"text": "Only if it were run backwards, which would make it a "
                     "different reaction altogether", "correct": False,
             "why": "Running it backwards WOULD give energy out — but then it "
                    "is the reverse change that is the fuel, not this one."},
            {"text": "No, because you would have to keep supplying energy and "
                     "would get nothing back", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c7-03-s04",
        "band": "standard",
        "text": "Copper carbonate only decomposes while the Bunsen is under "
                "it. Take the flame away and the reaction stops. Why?",
        "options": [
            {"text": "Because the reaction is endothermic and can only "
                     "proceed while energy is being supplied", "correct": True},
            {"text": "Because the tube cools too quickly for the powder to "
                     "stay hot enough to react", "correct": False,
             "why": "The tube stays hot for a while and the reaction still "
                    "stops. It is the supply of energy that has ended, not "
                    "the warmth."},
            {"text": "Because the reaction has finished by then, and the "
                     "flame was only ever a signal to start", "correct": False,
             "why": "Take the flame away early and half the powder is still "
                    "green. The reaction stops wherever it had reached."},
            {"text": "Because the carbon dioxide stops escaping once the tube "
                     "is off the flame", "correct": False,
             "why": "The gas stops escaping because the reaction stopped, not "
                    "the other way round."},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "c7-03-h01",
        "band": "harder",
        "text": "A sports cold pack can be used only once, but a reusable "
                "hand warmer resets by being boiled. What is the real "
                "difference between them?",
        "options": [
            {"text": "The hand warmer's chemicals are not used up and the "
                     "cold pack's are", "correct": False,
             "why": "Nothing is used up in either. Both changes could be "
                    "reversed in principle."},
            {"text": "The hand warmer is a reaction and the cold pack is only "
                     "a physical change", "correct": False,
             "why": "It is the other way round if anything — the hand warmer "
                    "is a crystallisation, which is a change of state."},
            {"text": "Whether the reverse change can be run inside the "
                     "packet: boiling works, evaporating dry does not",
             "correct": True},
            {"text": "The cold pack takes energy in, and taking energy in can "
                     "never be undone", "correct": False,
             "why": "It can be undone — that is what evaporating the water "
                    "off would do. It just cannot be done in a sealed bag."},
        ],
        "figure": None,
    },
    {
        "id": "c7-03-h02",
        "band": "harder",
        "text": "A student claims an endothermic reaction breaks the law of "
                "conservation of energy, because energy vanishes from the "
                "beaker. How would you answer them?",
        "options": [
            {"text": "They are right for endothermic reactions, which are the "
                     "one exception to the law", "correct": False,
             "why": "There are no exceptions. The energy is in the products, "
                    "not gone."},
            {"text": "They are right about the beaker, but the law only "
                     "applies to whole systems and not to beakers",
             "correct": False,
             "why": "The law applies to the beaker too. Nothing left the "
                    "beaker — it moved into the new substances inside it."},
            {"text": "They are wrong because the energy went into the air "
                     "instead, and air is hard to measure", "correct": False,
             "why": "Energy went the other way: OUT of the air and into the "
                    "reaction. That is why the air near the beaker cools."},
            {"text": "They are wrong: the energy is stored in the products, "
                     "where a thermometer cannot read it", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c7-03-h03",
        "band": "harder",
        "text": "Endothermic changes are much rarer than exothermic ones. "
                "What do most of them have in common?",
        "options": [
            {"text": "Something has to drive them — a flame, sunlight, or a "
                     "solid pulling itself apart as it dissolves",
             "correct": True},
            {"text": "They all involve water, which is why cold packs and "
                     "melting ice are the standard examples", "correct": False,
             "why": "Thermal decomposition of a carbonate involves no water "
                    "at all, and neither does photosynthesis directly."},
            {"text": "They all happen slowly, which is why they are so hard "
                     "to find in a school lab", "correct": False,
             "why": "A cold pack drops eight degrees in seconds. Rate is not "
                    "what they have in common."},
            {"text": "They all break something apart, which is why they never "
                     "make new substances", "correct": False,
             "why": "Breaking apart is common among them, but photosynthesis "
                    "builds glucose — and every one of them makes something "
                    "new."},
        ],
        "figure": None,
    },
    {
        "id": "c7-03-h04",
        "band": "harder",
        "text": "Why is photosynthesis sometimes called the largest "
                "endothermic process on Earth?",
        "options": [
            {"text": "Because leaves cover more of the planet's surface than "
                     "any other reacting material", "correct": False,
             "why": "Area is not the argument. What matters is how much "
                    "energy the reaction takes in and stores."},
            {"text": "Because it takes in sunlight and stores the energy that "
                     "almost every other living process later spends",
             "correct": True},
            {"text": "Because it is the only reaction on Earth that can take "
                     "energy in rather than giving it out", "correct": False,
             "why": "It is far from the only one. Every thermal "
                    "decomposition and every melting takes energy in too."},
            {"text": "Because it happens continuously, and no other reaction "
                     "runs without stopping", "correct": False,
             "why": "It stops every night, everywhere. The claim is about the "
                    "quantity of energy stored, not about running "
                    "continuously."},
        ],
        "figure": None,
    },
]
