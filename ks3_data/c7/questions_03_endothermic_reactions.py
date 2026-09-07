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
        # ⚑ RE-AUTHORED 21 Aug 2026 (MRB-281). This question previously
        # restated the apply rung VERBATIM — "Melting is endothermic. What
        # does that tell you about freezing?" — which `verify_questions`
        # check 6 refuses, because the bank is additional depth and not a
        # second copy of the ladder.
        #
        # ⚠️ IT WAS SHIPPED THAT WAY. The defect is on `main`, merged in
        # PR #8, so the C6/C7 run pushed with `verify_questions` red. The
        # gate was working; it was not run. Fixed here rather than left,
        # because a red gate blocks C8's push as surely as it should have
        # blocked C7's.
        #
        # The replacement keeps the band and the answer index (3) and asks
        # about the SURROUNDINGS instead of about the reverse change, which
        # is the half of `ENER-05` the other three easier questions do not
        # reach.
        "text": "A beaker of water has a cold pack resting in it and the "
                "water cools from 20 °C to 14 °C. Where has that energy "
                "gone?",
        "options": [
            {"text": "Nowhere — the water lost energy and it was destroyed",
             "correct": False,
             "why": "Energy is never destroyed. If the water has less, "
                    "something else has more."},
            {"text": "Into the thermometer, which is why the reading fell",
             "correct": False,
             "why": "A thermometer reports a temperature; it does not "
                    "swallow the energy behind it."},
            {"text": "Out into the room, because cold spreads from the pack "
                     "outwards",
             "correct": False,
             "why": "Cold is not a substance and does not spread. Energy "
                    "moves, and here it moves INTO the pack."},
            {"text": "Into the change happening inside the pack, which took "
                     "it in",
             "correct": True},
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
             "why": "Breaking apart is common among them but not universal — "
                    "photosynthesis, the biggest of them, builds glucose."},
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

    # ── easier · MRB-335 top-up ─────────────────────────────────────────
    {
        "id": "c7-03-e05",
        "band": "easier",
        "text": "What does endothermic mean?",
        "options": [
            {"text": "A change that produces cold, in the same way that an "
                     "exothermic change produces heat, so that the two are "
                     "opposites of each other",
             "correct": False,
             "why": "Cold is not produced or made. Energy is REMOVED from the "
                    "surroundings"},
            {"text": "A change that gives energy out to its surroundings",
             "correct": False,
             "why": "That is exothermic"},
            {"text": "A change that takes energy in from its surroundings",
             "correct": True},
            {"text": "A change that happens only in a fridge",
             "correct": False,
             "why": "A cold pack works on a mountainside with no electricity "
                    "at all"},
        ],
        "figure": None,
    },
    {
        "id": "c7-03-e06",
        "band": "easier",
        "text": "What is the law of conservation of energy?",
        "options": [
            {"text": "Energy always spreads out from where it is concentrated",
             "correct": False,
             "why": "That is a true and different statement. Conservation is "
                    "about the TOTAL never changing"},
            {"text": "Energy has to be saved rather than wasted",
             "correct": False,
             "why": "That is the everyday sense of conserving. The law is "
                    "about totals"},
            {"text": "Every reaction gives out as much energy as it takes in",
             "correct": False,
             "why": "Reactions are exothermic or endothermic precisely "
                    "because those amounts differ"},
            {"text": "Energy is never created and never destroyed — it can "
                     "only be moved from one store to another",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c7-03-e07",
        "band": "easier",
        "text": "Which of these is endothermic?",
        "options": [
            {"text": "Melting",
             "correct": True},
            {"text": "Burning a candle",
             "correct": False,
             "why": "Every combustion gives energy out"},
            {"text": "Neutralising an acid with an alkali, which is why the "
                     "beaker is noticeably warmer once the two have been "
                     "stirred together",
             "correct": False,
             "why": "The warm beaker is the sign of an EXOTHERMIC change"},
            {"text": "A metal reacting with an acid",
             "correct": False,
             "why": "The tube warms up, so energy is coming out"},
        ],
        "figure": None,
    },
    {
        "id": "c7-03-e08",
        "band": "easier",
        "text": "Photosynthesis is endothermic. What supplies the energy?",
        "options": [
            {"text": "The carbon dioxide the plant takes in, which carries "
                     "energy into the leaf along with the carbon that is "
                     "built into the glucose",
             "correct": False,
             "why": "Carbon dioxide supplies atoms rather than energy. The "
                    "energy comes from light"},
            {"text": "Light",
             "correct": True},
            {"text": "The water the plant draws up",
             "correct": False,
             "why": "Water is a reactant too, and it supplies no energy. A "
                    "watered plant in the dark cannot photosynthesise"},
            {"text": "The warmth of the air",
             "correct": False,
             "why": "A warm plant in the dark makes no glucose. Light is what "
                    "it needs"},
        ],
        "figure": None,
    },
    {
        "id": "c7-03-e09",
        "band": "easier",
        "text": "An instant cold pack drops close to 0 °C when it is "
                "squeezed. What is inside it?",
        "options": [
            {"text": "Ice, which has been kept frozen in an insulated "
                     "compartment until the moment the pack is squeezed and "
                     "the seal between the two halves is broken",
             "correct": False,
             "why": "It sits in a first aid kit at room temperature for "
                    "years. Nothing in it was ever cold"},
            {"text": "A gas under pressure that cools as it escapes",
             "correct": False,
             "why": "That is how some sprays work. This one uses a "
                    "dissolving"},
            {"text": "A solid and a pouch of water, which mix and dissolve "
                     "endothermically",
             "correct": True},
            {"text": "A battery driving a small cooler",
             "correct": False,
             "why": "There is nothing electrical in it. The chemistry does "
                    "the work"},
        ],
        "figure": None,
    },
    {
        "id": "c7-03-e10",
        "band": "easier",
        "text": "Melting is endothermic. What does that make freezing?",
        "options": [
            {"text": "Endothermic as well, since both of them involve ice and "
                     "ice is the cold substance in each case",
             "correct": False,
             "why": "They are opposite changes, so the energy travels in "
                    "opposite directions"},
            {"text": "Neither, because freezing involves no energy change",
             "correct": False,
             "why": "A freezer has to keep removing energy. That energy is "
                    "coming out of the water"},
            {"text": "It depends how cold the freezer is",
             "correct": False,
             "why": "The freezer's temperature changes the rate. The "
                    "direction is fixed"},
            {"text": "Exothermic",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c7-03-e11",
        "band": "easier",
        "text": "What is dissolving?",
        "options": [
            {"text": "A solute spreading through a solvent to make a "
                     "solution",
             "correct": True},
            {"text": "A solid being broken down into the simpler substances "
                     "it was made from, which then spread out through the "
                     "liquid",
             "correct": False,
             "why": "Nothing is broken down. Evaporate the water and the same "
                    "substance comes back"},
            {"text": "A solid melting in a liquid",
             "correct": False,
             "why": "Melting needs heat and one substance. Salt dissolves in "
                    "cold water and melts at 801 °C"},
            {"text": "A change that always takes energy in",
             "correct": False,
             "why": "Some dissolvings take energy in and some give it out"},
        ],
        "figure": None,
    },
    {
        "id": "c7-03-e12",
        "band": "easier",
        "text": "Which way does the thermometer move during an endothermic "
                "change?",
        "options": [
            {"text": "Up",
             "correct": False,
             "why": "That is exothermic. Endothermic takes energy away from "
                    "the surroundings"},
            {"text": "Down",
             "correct": True},
            {"text": "It does not move, because energy is conserved and so "
                     "the total in the beaker is the same before and after",
             "correct": False,
             "why": "Energy IS conserved, and it has moved out of the "
                    "surroundings into the products. The reading falls"},
            {"text": "Up and then down",
             "correct": False,
             "why": "There is no burst of energy out first. It falls from the "
                    "start"},
        ],
        "figure": None,
    },
    {
        "id": "c7-03-e13",
        "band": "easier",
        "text": "What is a reversible change?",
        "options": [
            {"text": "A change that undoes itself over time without anything "
                     "having to be done to it, which is why a reusable hand "
                     "warmer eventually resets on the shelf",
             "correct": False,
             "why": "A hand warmer has to be boiled. Nothing resets on its "
                    "own"},
            {"text": "A change that gives out as much energy as it took in "
                     "while it was happening",
             "correct": False,
             "why": "That is one thing reversing it achieves. The word is "
                    "about being able to run it backwards"},
            {"text": "A change that can be run backwards, which also reverses "
                     "its energy transfer",
             "correct": True},
            {"text": "A change that can be repeated",
             "correct": False,
             "why": "Repeating means doing it again with fresh materials. "
                    "Reversing means undoing it"},
        ],
        "figure": None,
    },

    # ── standard · MRB-335 top-up ───────────────────────────────────────
    {
        "id": "c7-03-s05",
        "band": "standard",
        "text": "A cold pack is rested in a beaker of water. A second, "
                "identical beaker of water is left beside it with nothing in "
                "it. What is the second beaker for?",
        "options": [
            {"text": "To keep the room's temperature steady around the first "
                     "beaker, so that the reading in it is not affected by "
                     "the air moving past",
             "correct": False,
             "why": "A beaker of water does not steady a room. It is there as "
                    "a comparison"},
            {"text": "To be used if the first beaker is spilled",
             "correct": False,
             "why": "A spare is not an experiment. This one is being measured "
                    "alongside"},
            {"text": "It is a control — it shows what the water would have "
                     "done anyway",
             "correct": True},
            {"text": "To warm the first beaker back up afterwards",
             "correct": False,
             "why": "Nothing is being warmed. The second beaker is measured, "
                    "not used"},
        ],
        "figure": None,
    },
    {
        "id": "c7-03-s06",
        "band": "standard",
        "text": "Which is the stronger evidence that a change is endothermic: "
                "that it stops when the flame is removed, or that a "
                "thermometer in it falls?",
        "options": [
            {"text": "Stopping when the flame is removed, because a reaction "
                     "that cannot continue without a supply of energy is one "
                     "that must have been taking energy in the whole time",
             "correct": False,
             "why": "It is good evidence and not decisive — a reaction can "
                    "stop because the tube cooled below the temperature it "
                    "needs to go at any speed"},
            {"text": "Neither — both are equally good",
             "correct": False,
             "why": "One measures the direction of the transfer directly. The "
                    "other is a clue about it"},
            {"text": "Neither — only weighing the products would show it",
             "correct": False,
             "why": "Mass says nothing about energy direction. A thermometer "
                    "says a great deal"},
            {"text": "The falling thermometer, because stopping when the heat "
                     "goes could have other causes",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c7-03-s07",
        "band": "standard",
        "text": "A student says photosynthesis creates energy, because a seed "
                "weighing a gram becomes a tree weighing tonnes. What is the "
                "correction?",
        "options": [
            {"text": "Nothing is created — the energy came from sunlight and "
                     "is now stored in the wood",
             "correct": True},
            {"text": "Nothing is created — the energy came out of the soil, "
                     "which is why a pot of earth weighs measurably less "
                     "after a plant has been grown in it for a season",
             "correct": False,
             "why": "The soil loses almost nothing, which is a famous old "
                    "experiment. The energy came from light"},
            {"text": "The student is right, because a plant makes its own "
                     "food",
             "correct": False,
             "why": "Making food is storing energy from elsewhere. It is not "
                    "creating any"},
            {"text": "The mass came from water, so no energy was involved",
             "correct": False,
             "why": "Water and carbon dioxide supply the atoms, and building "
                    "them into glucose takes a great deal of energy"},
        ],
        "figure": None,
    },
    {
        "id": "c7-03-s08",
        "band": "standard",
        "text": "Salt is spread on a snowy road and the slush that forms ends "
                "up colder than the snow was. Which idea from this lesson is "
                "that?",
        "options": [
            {"text": "The salt is colder than the snow, and it cools the "
                     "slush by contact as the two of them mix together on the "
                     "road surface",
             "correct": False,
             "why": "The salt comes off a lorry at air temperature. Nothing "
                     "cold was added"},
            {"text": "The salt dissolving is endothermic, so it takes energy "
                     "out of the slush",
             "correct": True},
            {"text": "The salt produces cold as it dissolves",
             "correct": False,
             "why": "Cold is not produced. Energy is taken away, which is not "
                    "the same thing"},
            {"text": "The salt stops the snow reflecting sunlight",
             "correct": False,
             "why": "It does darken the surface, which would WARM it. The "
                    "cooling is chemical"},
        ],
        "figure": None,
    },
    {
        "id": "c7-03-s09",
        "band": "standard",
        "text": "Two powders stirred into water drop the temperature by "
                "8 °C. What would twice as much of each powder do, in the same "
                "volume of water?",
        "options": [
            {"text": "Drop it by the same 8 °C, because the temperature a "
                     "change reaches is a property of the substances rather "
                     "than of how much of them there is",
             "correct": False,
             "why": "The amount of energy taken in doubles while the water "
                    "warmed stays the same. The fall gets bigger"},
            {"text": "Drop it by half as much",
             "correct": False,
             "why": "More powder takes in more energy. Halving would need "
                    "less of it"},
            {"text": "Drop it further, because more of the change happens in "
                     "the same amount of water",
             "correct": True},
            {"text": "Have no effect, because the water is what is being "
                     "measured",
             "correct": False,
             "why": "The water is what is being measured, and it is losing "
                    "energy to the change. More change means more loss"},
        ],
        "figure": None,
    },
    {
        "id": "c7-03-s10",
        "band": "standard",
        "text": "A sealed flask of two powders is weighed, they are stirred "
                "together, the temperature falls, and the flask is weighed "
                "again. What does the balance read?",
        "options": [
            {"text": "Less, because energy has left the flask and energy has "
                     "mass",
             "correct": False,
             "why": "No measurable mass leaves with energy. Nothing crossed "
                    "the seal"},
            {"text": "More, because the products hold the energy that was "
                     "taken in",
             "correct": False,
             "why": "The products do hold that energy, and it makes no "
                    "difference a balance can read"},
            {"text": "Less, because some of the powder has dissolved",
             "correct": False,
             "why": "Dissolving moves a substance about inside the flask. "
                    "None of it leaves"},
            {"text": "Exactly the same",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c7-03-s11",
        "band": "standard",
        "text": "Which of these everyday objects works by an endothermic "
                "change, and what tells you?",
        "options": [
            {"text": "An instant cold pack, because it gets colder",
             "correct": True},
            {"text": "A firework, because the energy stored in it has to be "
                     "taken in from somewhere before it can be given out "
                     "again on the night",
             "correct": False,
             "why": "The energy was put in during manufacture. What the "
                    "firework itself does is release it"},
            {"text": "A hand warmer, because it changes temperature",
             "correct": False,
             "why": "Changing temperature is not enough — the DIRECTION is "
                    "what matters, and a hand warmer gets hotter"},
            {"text": "A candle, because it needs lighting",
             "correct": False,
             "why": "Needing a start is not taking energy in overall. A "
                    "candle gives out far more than the match supplied"},
        ],
        "figure": None,
    },
    {
        "id": "c7-03-s12",
        "band": "standard",
        "text": "Why does the same reaction reversed give the same energy "
                "back, rather than some other amount?",
        "options": [
            {"text": "Because energy is conserved, so nothing can ever come "
                     "back in a different amount from the one that went in "
                     "however the change is run",
             "correct": False,
             "why": "Conservation says the total across everything holds. It "
                    "does not by itself fix the amount for one change"},
            {"text": "Because the same joins are being made that were broken, "
                     "so the same energy is involved",
             "correct": True},
            {"text": "Because reactions are always symmetrical",
             "correct": False,
             "why": "Many are hard or impossible to reverse. When they can be "
                    "reversed, the same joins are involved"},
            {"text": "Because the temperature returns to where it started",
             "correct": False,
             "why": "That is a consequence rather than a reason"},
        ],
        "figure": None,
    },
    {
        "id": "c7-03-s13",
        "band": "standard",
        "text": "A student holds a cold pack and says it feels like the cold "
                "is going into their hand. What is really happening?",
        "options": [
            {"text": "Cold is passing from the pack into their hand, which is "
                     "why the hand goes numb from the outside inwards rather "
                     "than all at once",
             "correct": False,
             "why": "Nothing passes into the hand. Energy passes out of it, "
                    "which is what feeling cold is"},
            {"text": "The pack is stopping their hand from making heat",
             "correct": False,
             "why": "The hand goes on respiring and producing energy. The "
                    "pack is taking it faster than that"},
            {"text": "Energy is leaving their hand and going into the pack",
             "correct": True},
            {"text": "Nothing is happening — the sensation is an illusion",
             "correct": False,
             "why": "It is a real transfer. Only the direction is being "
                    "described the wrong way round"},
        ],
        "figure": None,
    },

    # ── harder · MRB-335 top-up ─────────────────────────────────────────
    {
        "id": "c7-03-h05",
        "band": "harder",
        "text": "Why can a reusable hand warmer be reset in a pan of boiling "
                "water while a cold pack cannot be reset at all?",
        "options": [
            {"text": "Because the hand warmer's reaction is exothermic and "
                     "the cold pack's is endothermic, and only an exothermic "
                     "change can ever be reversed",
             "correct": False,
             "why": "Either direction can be reversed in principle. What "
                    "matters is whether it can be done inside the packet"},
            {"text": "Because boiling water is hot enough for one and not the "
                     "other",
             "correct": False,
             "why": "Temperature is not the obstacle. Getting the solid back "
                    "out of solution is"},
            {"text": "Because the hand warmer's change can be reversed inside "
                     "its sealed pouch, and undoing the cold pack would mean "
                     "evaporating the water out of it",
             "correct": True},
            {"text": "Because the cold pack has been used up",
             "correct": False,
             "why": "Every atom is still in the bag. It is dissolved rather "
                    "than gone"},
        ],
        "figure": None,
    },
    {
        "id": "c7-03-h06",
        "band": "harder",
        "text": "An endothermic reaction is run in a well insulated flask. "
                "What does a thermometer in it do over the next hour?",
        "options": [
            {"text": "Falls while the reaction runs and then stays where it "
                     "is, because the insulation keeps the room's energy out "
                     "and there is nothing left inside to change it",
             "correct": False,
             "why": "Insulation slows the leak rather than stopping it. Given "
                    "an hour the flask warms back up"},
            {"text": "Falls steadily for the whole hour",
             "correct": False,
             "why": "The reaction finishes. After that only the room is "
                    "acting on the flask"},
            {"text": "Rises, because the insulation traps energy",
             "correct": False,
             "why": "There is nothing to trap while the reaction is taking "
                    "energy IN. It falls first"},
            {"text": "Falls while the reaction runs, then climbs slowly back "
                     "towards room temperature",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c7-03-h07",
        "band": "harder",
        "text": "A growing tree gets heavier year by year; a burning log gets "
                "lighter in an hour. Both involve the same substances. What is "
                "the relationship?",
        "options": [
            {"text": "The tree is storing what the log is spending — one "
                     "change is endothermic and the other its exothermic "
                     "reverse",
             "correct": True},
            {"text": "The tree takes its mass from the soil and the log gives "
                     "its mass to the air, so the two changes move matter in "
                     "opposite directions between the ground and the sky",
             "correct": False,
             "why": "Almost all the tree's mass comes from the AIR rather "
                    "than the soil. And the point of the pair is the energy"},
            {"text": "They are unrelated, because one is biology and the "
                     "other chemistry",
             "correct": False,
             "why": "The same reaction runs in both, in opposite directions. "
                    "Which subject studies it changes nothing"},
            {"text": "The log releases more energy than the tree ever stored",
             "correct": False,
             "why": "It cannot release more than went in. The reverse change "
                    "returns the same amount"},
        ],
        "figure": None,
    },
    {
        "id": "c7-03-h08",
        "band": "harder",
        "text": "Ammonium nitrate dissolving takes energy in; sodium "
                "hydroxide dissolving gives it out. What does that pair show "
                "about dissolving?",
        "options": [
            {"text": "That one of the two is not really dissolving, since a "
                     "process cannot run in both energy directions and still "
                     "be given a single name",
             "correct": False,
             "why": "Both are genuinely dissolving. A process CAN go either "
                    "way depending on the substances"},
            {"text": "That dissolving has no fixed energy direction — it "
                     "depends on the substance",
             "correct": True},
            {"text": "That sodium hydroxide is reacting rather than "
                     "dissolving",
             "correct": False,
             "why": "It dissolves, and the solution warms. No new substance "
                    "is made"},
            {"text": "That the direction depends on how much water is used",
             "correct": False,
             "why": "The amount changes the size of the change, never its "
                    "direction"},
        ],
        "figure": None,
    },
    {
        "id": "c7-03-h09",
        "band": "harder",
        "text": "A designer wants a cold pack that can be used again and "
                "again. What would the chemistry have to allow?",
        "options": [
            {"text": "A reaction that takes in less energy each time it is "
                     "used",
             "correct": False,
             "why": "A weakening pack would be worse rather than reusable. "
                    "What is needed is a reversal"},
            {"text": "A pack that can be refrigerated between uses",
             "correct": False,
             "why": "That is an ordinary ice pack, and the whole point of an "
                    "instant one is working with no freezer"},
            {"text": "A change that can be reversed inside the pack, which "
                     "for this one would mean getting the solid back out of "
                     "solution",
             "correct": True},
            {"text": "An exothermic reaction instead",
             "correct": False,
             "why": "That would warm rather than cool. The pack has to stay "
                    "endothermic"},
        ],
        "figure": None,
    },
    {
        "id": "c7-03-h10",
        "band": "harder",
        "text": "Melting ice takes energy in and is not usually called a "
                "REACTION. Does that stop it being endothermic?",
        "options": [
            {"text": "Yes — the words exothermic and endothermic are defined "
                     "for chemical reactions, and a change of state needs "
                     "different language of its own",
             "correct": False,
             "why": "The lesson applies both words to melting and freezing "
                    "directly. They describe changes of any kind"},
            {"text": "Yes, because no new substance is made",
             "correct": False,
             "why": "Making a new substance is what decides CHEMICAL. It does "
                    "not decide the energy direction"},
            {"text": "No, because melting is really a slow reaction",
             "correct": False,
             "why": "It is not a reaction at all. It is endothermic anyway"},
            {"text": "No — endothermic describes any change that takes energy "
                     "in, chemical or physical",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c7-03-h11",
        "band": "harder",
        "text": "A plant is given plenty of water and carbon dioxide and kept "
                "in the dark. Why does it make no glucose?",
        "options": [
            {"text": "Because photosynthesis is endothermic and light is what "
                     "supplies the energy it needs",
             "correct": True},
            {"text": "Because a plant needs light to open the pores in its "
                     "leaves, and with those closed the carbon dioxide cannot "
                     "get in however much of it is available",
             "correct": False,
             "why": "Pores do respond to light, and even with the gas inside "
                    "there would be no energy to drive the reaction"},
            {"text": "Because carbon dioxide only reacts in sunlight",
             "correct": False,
             "why": "Carbon dioxide reacts in plenty of dark places. The "
                    "energy is what is missing"},
            {"text": "Because the plant respires instead, and cannot do both",
             "correct": False,
             "why": "It does both at once in the light. Respiring does not "
                    "prevent photosynthesis"},
        ],
        "figure": None,
    },
    {
        "id": "c7-03-h12",
        "band": "harder",
        "text": "A cold pack and a fridge both make food colder. What is the "
                "fundamental difference?",
        "options": [
            {"text": "The pack removes energy and the fridge produces cold",
             "correct": False,
             "why": "Neither produces cold. Both remove energy, and the "
                    "difference is where it ends up"},
            {"text": "The pack stores the energy in its own products; the "
                     "fridge moves it out and releases it at the back",
             "correct": True},
            {"text": "The pack is chemical and the fridge is physical, so "
                     "they cannot be compared",
             "correct": False,
             "why": "They can be compared perfectly well, and both move "
                    "energy out of the food"},
            {"text": "The fridge is endothermic and the pack is not",
             "correct": False,
             "why": "The pack's change is the endothermic one. A fridge is a "
                    "machine rather than a reaction"},
        ],
        "figure": None,
    },
    {
        "id": "c7-03-h13",
        "band": "harder",
        "text": "Reversing an endothermic change gives an exothermic one, by "
                "exactly the same amount. Why does that mean a hand warmer can "
                "be reset but a firework cannot?",
        "options": [
            {"text": "Because the firework's reaction gives out far more "
                     "energy than the warmer's",
             "correct": False,
             "why": "Size is not the obstacle in principle. The products have "
                    "gone into the sky, which is"},
            {"text": "Because a firework's change is exothermic and cannot be "
                     "reversed at all",
             "correct": False,
             "why": "Exothermic changes are reversed all the time — that is "
                    "what resetting a hand warmer is"},
            {"text": "Because the hand warmer's change can be run backwards "
                     "with the energy a pan of water can supply, and the "
                     "firework's products have scattered",
             "correct": True},
            {"text": "Because the hand warmer is sealed and fireworks are "
                     "not",
             "correct": False,
             "why": "The right idea, put too narrowly. What matters is that "
                    "the products are still there to work with"},
        ],
        "figure": None,
    },
]
