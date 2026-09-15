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
            {"text": "A gas held under pressure that cools sharply as it "
                     "escapes through the broken seal",
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
            {"text": "A change that always takes energy in from the "
                     "surroundings around it",
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
            {"text": "To warm the first beaker back up again once its reading "
                     "has finally been taken",
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
            {"text": "Neither of them — only weighing the products before and "
                     "after the change could possibly settle it",
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
            {"text": "The student is right, because a plant makes its own food "
                     "out of nothing more than air and water",
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
            {"text": "The salt stops the snow reflecting sunlight, so the road "
                     "surface takes in more of it",
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
                     "measured and there is the same amount of it",
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
            {"text": "Because the temperature returns to where it started, and "
                     "the same energy must therefore be involved",
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
            {"text": "Rises, because the insulation traps the energy inside "
                     "the flask rather than letting it escape",
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
            {"text": "They are completely unrelated, because one of them is a "
                     "question for biology and the other one is a question for "
                     "chemistry",
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

    # ── MRB-338 night 3 · easier ────────────────────────────────────────
    {
        "id": "c7-03-e14",
        "band": "easier",
        "text": "In photosynthesis, what does a plant build, and what does "
                "it build it from?",
        "options": [
            {"text": "Glucose, from carbon dioxide and water",
             "correct": True},
            {"text": "Oxygen, from the sunlight that falls on the leaf",
             "correct": False,
             "why": "Oxygen is given off as a product, and sunlight is the "
                    "energy supply rather than a raw material."},
            {"text": "Carbon dioxide, from the glucose stored in the leaf "
                     "and the water drawn up from the roots", "correct": False,
             "why": "That is respiration working the other way round. "
                    "Photosynthesis uses carbon dioxide up."},
            {"text": "Water, from the carbon dioxide it takes in",
             "correct": False,
             "why": "Water is one of the raw materials a plant takes in, not "
                    "something photosynthesis makes."},
        ],
        "figure": None,
    },
    {
        "id": "c7-03-e15",
        "band": "easier",
        "text": "The lesson says there is no such thing as cold. If cold is "
                "not a substance, what is it?",
        "options": [
            {"text": "A gas that collects wherever energy has been removed "
                     "from a substance", "correct": False,
             "why": "Nothing collects anywhere. There is no material of any "
                    "kind involved in something being cold."},
            {"text": "It is not a thing at all — it is the absence of energy", "correct": True},
            {"text": "A measure of how much ice a substance contains",
             "correct": False,
             "why": "Things with no ice in them at all get cold, and ice "
                    "itself can be at many different temperatures."},
            {"text": "The opposite of energy, which cancels it out",
             "correct": False,
             "why": "There is nothing that cancels energy. Take energy away "
                    "and what is left is simply less of it."},
        ],
        "figure": None,
    },
    {
        "id": "c7-03-e16",
        "band": "easier",
        "text": "Why is an instant cold pack worth carrying in a first aid "
                "kit up a mountain?",
        "options": [
            {"text": "Because it stays cold for the whole of a day's walk "
                     "once it has been squeezed", "correct": False,
             "why": "It works for minutes, not for a day. Its advantage is "
                    "where it works, not how long."},
            {"text": "Because it can be refilled from a stream and used "
                     "again further up", "correct": False,
             "why": "Adding water does not reset it. The solid has already "
                    "dissolved and cannot be got back."},
            {"text": "Because it works with no freezer, no electricity and no cold water",
             "correct": True},
            {"text": "Because the thinner air higher up makes it colder than "
                     "it would be at sea level", "correct": False,
             "why": "The cooling comes from the change inside the bag, and "
                    "the air outside has nothing to do with it."},
        ],
        "figure": None,
    },
    {
        "id": "c7-03-e17",
        "band": "easier",
        "text": "Why is an instant cold pack put on over clothing or a cloth "
                "rather than straight onto bare skin?",
        "options": [
            {"text": "Because the chemicals inside would soak through and "
                     "sting a cut", "correct": False,
             "why": "The bag is sealed, and a pack that had burst would be "
                    "thrown away rather than used."},
            {"text": "Because the cloth is what makes the pack start working "
                     "in the first place", "correct": False,
             "why": "Squeezing the pack starts it. A cloth plays no part in "
                    "the change at all."},
            {"text": "Because the pack works better when it is not touching "
                     "anything directly", "correct": False,
             "why": "Contact is how the energy gets out of the injury. The "
                    "cloth slows that down on purpose."},
            {"text": "Because it gets cold enough to damage the skin it is "
                     "held against", "correct": True},
        ],
        "figure": None,
    },

    # ── MRB-338 night 3 · standard ──────────────────────────────────────
    {
        "id": "c7-03-s14",
        "band": "standard",
        "text": "Sherbet contains citric acid and sodium hydrogencarbonate, "
                "and it feels cool on the tongue. Which idea from this "
                "lesson explains that?",
        "options": [
            {"text": "The two react once they are wet, and the reaction "
                     "takes energy from the tongue", "correct": True},
            {"text": "The powder is stored cold in the wrapper, and it keeps "
                     "that coldness until it is eaten", "correct": False,
             "why": "Sherbet sits on a warm shop shelf. It is at room "
                    "temperature before it goes anywhere near a mouth."},
            {"text": "The bubbles it makes are cold, and they carry that "
                     "coldness onto the tongue", "correct": False,
             "why": "Cold is not something a bubble can carry. The gas is "
                    "made at the temperature it finds itself in."},
            {"text": "Sugar dissolving is exothermic, so the tongue feels "
                     "the contrast afterwards", "correct": False,
             "why": "An exothermic change would leave the tongue warmer, and "
                    "there is no contrast effect here to feel."},
        ],
        "figure": None,
    },
    {
        "id": "c7-03-s15",
        "band": "standard",
        "text": "A cube of ice and a squeezed cold pack will both cool a "
                "drink. What do the two have in common in energy terms?",
        "options": [
            {"text": "Both hold a store of coldness that they release into "
                     "the drink until it runs out", "correct": False,
             "why": "There is no store of coldness in anything. Both are "
                    "taking energy rather than giving something."},
            {"text": "Both take energy in from the drink, one by melting and "
                     "one by dissolving", "correct": True},
            {"text": "Both are colder than the drink, which is the whole of "
                     "the explanation", "correct": False,
             "why": "A cold pack starts at room temperature, the same as the "
                    "drink, and still cools it."},
            {"text": "Both give energy out as they change, which drives the "
                     "warm drink away from them", "correct": False,
             "why": "A change giving energy out would warm the drink up. "
                    "These two take it in."},
        ],
        "figure": None,
    },
    {
        "id": "c7-03-s16",
        "band": "standard",
        "text": "A grower switches extra lamps on over a crop through the "
                "winter and the plants grow faster. Explain that in terms of "
                "energy.",
        "options": [
            {"text": "The lamps warm the greenhouse, and warmth is what a "
                     "plant grows from", "correct": False,
             "why": "Warmth alone does not build glucose. A warm dark shed "
                    "grows nothing."},
            {"text": "The lamps replace the carbon dioxide that is short in "
                     "winter air", "correct": False,
             "why": "A lamp makes light, not carbon dioxide, and winter air "
                    "holds as much as summer air does."},
            {"text": "Photosynthesis is endothermic, and the lamps supply "
                     "more of the energy it needs", "correct": True},
            {"text": "Extra light makes the plant respire faster, which is "
                     "how the extra mass is put on", "correct": False,
             "why": "Respiration spends the store rather than filling it. "
                    "Growth comes from photosynthesis."},
        ],
        "figure": None,
    },
    {
        "id": "c7-03-s17",
        "band": "standard",
        "text": "Melting and freezing are opposite changes, so their energy "
                "transfers run in opposite directions. Apply the same idea "
                "to boiling and condensing.",
        "options": [
            {"text": "Both take energy in, because both of them involve a "
                     "gas at some point in the change", "correct": False,
             "why": "Involving a gas does not fix the direction. The two "
                    "changes are opposites, so they cannot match."},
            {"text": "Both give energy out, because a gas holds less than a "
                     "liquid does", "correct": False,
             "why": "A gas holds more, not less, and two opposite changes "
                    "cannot both give energy out."},
            {"text": "Condensing takes energy in and boiling gives it out",
             "correct": False,
             "why": "That is the right pairing the wrong way round. It takes "
                    "energy to drive a liquid into a gas."},
            {"text": "Boiling takes energy in and condensing gives it out",
             "correct": True},
        ],
        "figure": None,
    },

    # ── MRB-338 night 3 · harder ────────────────────────────────────────
    {
        "id": "c7-03-h14",
        "band": "harder",
        "text": "A student says that because freezing gives back exactly "
                "what melting took in, you could melt and freeze the same "
                "ice over and over and collect free energy. What is wrong?",
        "options": [
            {"text": "You get back exactly what you put in, so there is "
                     "never anything spare to collect", "correct": True},
            {"text": "Nothing is wrong with it, but the energy comes back so "
                     "slowly that it is not worth the equipment it needs",
             "correct": False,
             "why": "Speed is not the problem. There is no surplus to "
                    "collect however long you wait."},
            {"text": "Freezing gives back rather less than melting took in, "
                     "so the ice runs down", "correct": False,
             "why": "The two are equal. Reversing a change reverses the "
                    "transfer by exactly the same amount."},
            {"text": "Melting and freezing are the same change, so no energy "
                     "moves in either direction", "correct": False,
             "why": "Energy moves both times — in during melting and out "
                    "during freezing. They are opposite changes."},
        ],
        "figure": None,
    },
    {
        "id": "c7-03-h15",
        "band": "harder",
        "text": "Photosynthesis is endothermic, yet a leaf in bright "
                "sunshine does not feel cold. Why not?",
        "options": [
            {"text": "Because a leaf is too thin for anybody to feel a "
                     "temperature difference in it, whatever is going on "
                     "inside", "correct": False,
             "why": "A thin thing can still be measurably cold. The reason "
                    "is where the energy comes from."},
            {"text": "Because the energy it takes in comes from sunlight "
                     "rather than from the air around it", "correct": True},
            {"text": "Because respiration in the same leaf gives out exactly "
                     "as much as photosynthesis takes in", "correct": False,
             "why": "A growing plant photosynthesises far faster than it "
                    "respires, or it would never gain any mass."},
            {"text": "Because photosynthesis is endothermic only at night, "
                     "when the leaf is already cool", "correct": False,
             "why": "Photosynthesis stops in the dark. It runs in the light "
                    "and it is endothermic while it runs."},
        ],
        "figure": None,
    },
    {
        "id": "c7-03-h16",
        "band": "harder",
        "text": "Asked to sort water freezing, a student puts it with the "
                "endothermic changes because ice is cold. What is the error "
                "in that reasoning?",
        "options": [
            {"text": "They have forgotten that ice is not cold until some "
                     "time after it has finished forming", "correct": False,
             "why": "Ice is at 0 °C as it forms. When it got cold is not the "
                    "question."},
            {"text": "They have sorted a physical change, and only chemical "
                     "reactions can be put on either list", "correct": False,
             "why": "Both lists carry physical changes. Melting and "
                    "dissolving are on them."},
            {"text": "They have judged it by how cold the product is instead "
                     "of which way the energy moved", "correct": True},
            {"text": "They have used the freezer rather than the water as "
                     "the thing being classified", "correct": False,
             "why": "They classified the freezing itself. The mistake is in "
                    "the evidence they used to classify it."},
        ],
        "figure": None,
    },
    {
        "id": "c7-03-h17",
        "band": "harder",
        "text": "Why is “endothermic” a better name for these changes than "
                "“cooling reactions” would be?",
        "options": [
            {"text": "Because some of them cool their surroundings by a very "
                     "small amount that would be hard to notice at all",
             "correct": False,
             "why": "How big the drop is has nothing to do with it. A small "
                    "drop is still a drop."},
            {"text": "Because a few of them warm their surroundings instead, "
                     "so the word cooling would be wrong for those",
             "correct": False,
             "why": "Every endothermic change cools its surroundings. None "
                    "of them warms anything."},
            {"text": "Because cooling is a word about weather, so it cannot "
                     "be used about a reaction", "correct": False,
             "why": "Scientists use ordinary words all the time. The problem "
                    "is what the word describes, not where it comes from."},
            {"text": "Because the cooling is only what you notice, while the "
                     "name states which way the energy went", "correct": True},
        ],
        "figure": None,
    },
    # ── MRB-338 night 3 · easier, second pass ───────────────────────────
    {
        "id": "c7-03-e18",
        "band": "easier",
        "text": "What does the ammonium nitrate in a first aid cold pack do "
                "to the water it meets?",
        "options": [
            {"text": "It dissolves, and the dissolving takes energy in from "
                     "the water", "correct": True},
            {"text": "It reacts with the water and releases a gas that "
                     "carries energy away", "correct": False,
             "why": "Nothing is given off. The pack stays sealed and no gas "
                    "is made."},
            {"text": "It freezes the water around each grain, which is what "
                     "cools the pack", "correct": False,
             "why": "The contents are still liquid afterwards, and freezing "
                    "would give energy out rather than take it in."},
            {"text": "It spreads cold out through the water from each grain",
             "correct": False,
             "why": "Cold is not a substance that can spread. Energy moves, "
                    "and it moves out of the water."},
        ],
        "figure": None,
    },
    {
        "id": "c7-03-e19",
        "band": "easier",
        "text": "Why does an unsqueezed instant cold pack sit at room "
                "temperature on a shelf for years?",
        "options": [
            {"text": "Because the chemicals slowly lose their coldness while "
                     "they wait", "correct": False,
             "why": "There is no coldness stored in them. Nothing is waiting "
                    "to be released."},
            {"text": "Because the solid and the water are kept apart until "
                     "it is squeezed", "correct": True},
            {"text": "Because the pack is insulated well enough to hold its "
                     "temperature", "correct": False,
             "why": "Insulation only slows a change down. The pack is simply "
                    "the same temperature as the shelf."},
            {"text": "Because the dissolving needs a warm room before it can "
                     "begin", "correct": False,
             "why": "A squeezed pack works on a cold mountainside too. What "
                    "it needs is the water."},
        ],
        "figure": None,
    },
    {
        "id": "c7-03-e20",
        "band": "easier",
        "text": "A first aid cold pack is set off in a room at 20 °C. "
                "Roughly how far does the thermometer inside it fall?",
        "options": [
            {"text": "By about 2 degrees", "correct": False,
             "why": "A drop that small would not be worth carrying. A pack "
                    "is sold because you can feel what it does."},
            {"text": "By about 20 degrees", "correct": True},
            {"text": "By about 50 degrees", "correct": False,
             "why": "That would take the pack to −30 °C, colder than a "
                    "freezer. It goes down to about freezing point."},
            {"text": "By about 5 degrees", "correct": False,
             "why": "The fall is several times bigger than that. The pack "
                    "ends up near 0 °C."},
        ],
        "figure": None,
    },
    {
        "id": "c7-03-e21",
        "band": "easier",
        "text": "Copper carbonate is heated strongly until it breaks down. "
                "Which way is energy moving during that change?",
        "options": [
            {"text": "Into the surroundings, out of the reaction",
             "correct": False,
             "why": "That is exothermic. This change has to be fed by the "
                    "flame for as long as it runs."},
            {"text": "Neither way — the flame only changes how fast it "
                     "happens", "correct": False,
             "why": "Take the flame away and it stops altogether, so the "
                    "flame is supplying what it needs."},
            {"text": "Out of the reaction and into the gas that is given off",
             "correct": False,
             "why": "The gas leaves the tube, but the change itself is "
                    "taking energy in rather than sending it out."},
            {"text": "Into the reaction, out of the surroundings",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c7-03-e22",
        "band": "easier",
        "text": "Sweat evaporating from skin cools a runner down. Is "
                "evaporating endothermic or exothermic?",
        "options": [
            {"text": "Endothermic, because it takes energy in from the skin",
             "correct": True},
            {"text": "Exothermic, because the skin ends up cooler than it "
                     "was before", "correct": False,
             "why": "A falling temperature is what endothermic does. "
                    "Exothermic warms the surroundings."},
            {"text": "Endothermic, because the sweat gives its cold to the "
                     "skin", "correct": False,
             "why": "The direction is right and the reason is wrong. Nothing "
                    "cold is given; energy is taken."},
            {"text": "Neither, because evaporating is not a chemical "
                     "reaction at all", "correct": False,
             "why": "Both words describe any change that moves energy, "
                    "physical ones included."},
        ],
        "figure": None,
    },
    {
        "id": "c7-03-e23",
        "band": "easier",
        "text": "Melting, photosynthesis, thermal decomposition and ammonium "
                "nitrate dissolving. What do all four have in common?",
        "options": [
            {"text": "They all break a substance down into simpler ones",
             "correct": False,
             "why": "Melting breaks nothing down, and photosynthesis builds "
                    "a substance rather than breaking one."},
            {"text": "They all need a flame or a lamp to make them happen",
             "correct": False,
             "why": "Ice melting in a drink needs neither. What they need is "
                    "energy, from wherever it comes."},
            {"text": "They all take energy in from their surroundings",
             "correct": True},
            {"text": "They all happen only inside a laboratory",
             "correct": False,
             "why": "Three of the four happen in a drink, in a leaf and in a "
                    "first aid kit."},
        ],
        "figure": None,
    },
    {
        "id": "c7-03-e24",
        "band": "easier",
        "text": "A strongly endothermic reaction is run in a glass beaker. "
                "What happens to the outside of the beaker?",
        "options": [
            {"text": "It dries out, because the cold draws any moisture "
                     "inwards", "correct": False,
             "why": "Cold draws nothing. The glass gains water rather than "
                    "losing it."},
            {"text": "Nothing, because the reaction is inside and the glass "
                     "is a barrier", "correct": False,
             "why": "The glass is part of the surroundings, and it cools "
                    "with everything else."},
            {"text": "It warms, because the energy has to leave the beaker "
                     "somewhere", "correct": False,
             "why": "No energy is leaving. The reaction is taking it in, so "
                    "the glass gets colder."},
            {"text": "It mists over, because water from the air condenses on "
                     "the cold glass", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c7-03-e25",
        "band": "easier",
        "text": "Which pair of changes run in opposite energy directions?",
        "options": [
            {"text": "Rusting and respiring", "correct": False,
             "why": "Both give energy out, and neither one is the reverse of "
                    "the other."},
            {"text": "Melting ice and water freezing", "correct": True},
            {"text": "Burning coal and burning natural gas", "correct": False,
             "why": "Both are combustion, so both give energy out."},
            {"text": "Salt dissolving and sugar dissolving", "correct": False,
             "why": "Both are dissolvings, and neither one undoes the "
                    "other."},
        ],
        "figure": None,
    },
    {
        "id": "c7-03-e26",
        "band": "easier",
        "text": "A metal tin picked up in a cold garage feels cold in your "
                "hands. Is that an endothermic change?",
        "options": [
            {"text": "Yes, because your hands lose energy, and losing energy "
                     "is what endothermic means", "correct": False,
             "why": "Endothermic describes a CHANGE that takes energy in. "
                    "Nothing in the tin is changing."},
            {"text": "Yes, because the tin makes cold, which is what a cold "
                     "object does", "correct": False,
             "why": "Nothing makes cold. The tin is simply sitting at the "
                    "garage's temperature."},
            {"text": "No — nothing is changing in the tin; it is just colder "
                     "than your hands", "correct": True},
            {"text": "No, because a metal cannot take part in an endothermic "
                     "change", "correct": False,
             "why": "It can. Heating a metal carbonate until it decomposes "
                    "is endothermic."},
        ],
        "figure": None,
    },
    {
        "id": "c7-03-e27",
        "band": "easier",
        "text": "A thermal decomposition keeps going only while one thing is "
                "supplied to it. What is it?",
        "options": [
            {"text": "Oxygen from the air", "correct": False,
             "why": "Oxygen is what combustion needs. A decomposition breaks "
                    "one substance down on its own."},
            {"text": "Energy", "correct": True},
            {"text": "Water", "correct": False,
             "why": "A decomposition in a test tube is dry. Nothing is added "
                    "to it while it runs."},
            {"text": "A catalyst", "correct": False,
             "why": "A catalyst changes the rate. What the flame supplies is "
                    "the energy the change takes in."},
        ],
        "figure": None,
    },
    {
        "id": "c7-03-e28",
        "band": "easier",
        "text": "An instant cold pack and a reusable hand warmer are lying "
                "side by side. Which way does energy move in each of them "
                "once it is started?",
        "options": [
            {"text": "Out of both of them, because both are changing",
             "correct": False,
             "why": "Only the warmer gives energy out. The pack takes it in, "
                    "which is why it goes cold."},
            {"text": "Into the pack and out of the warmer", "correct": True},
            {"text": "Into both of them, because both hold a store that has "
                     "to be filled", "correct": False,
             "why": "The warmer's store was filled before it was sold, and "
                    "it empties as the warmer works."},
            {"text": "Out of the pack and into the warmer", "correct": False,
             "why": "That is the wrong way round for both. The pack cools "
                    "its surroundings and the warmer heats them."},
        ],
        "figure": None,
    },
    {
        "id": "c7-03-e29",
        "band": "easier",
        "text": "A squeezed cold pack is held against a swollen ankle. Which "
                "of these counts as the SURROUNDINGS of the change inside "
                "it?",
        "options": [
            {"text": "Only the ammonium nitrate that is dissolving",
             "correct": False,
             "why": "That is the change itself. The surroundings are "
                    "everything else."},
            {"text": "Only the ankle, because that is the one thing the "
                     "pack was made to cool", "correct": False,
             "why": "The water, the bag and the air cool as well. All of "
                    "them are surroundings."},
            {"text": "The water, the bag, the cloth and the ankle it is held "
                     "against", "correct": True},
            {"text": "Nothing, because a sealed pack has no surroundings",
             "correct": False,
             "why": "A sealed bag still sits in a room and against a person, "
                    "and both of those cool."},
        ],
        "figure": None,
    },
    {
        "id": "c7-03-e30",
        "band": "easier",
        "text": "Citric acid and sodium hydrogencarbonate powders are left "
                "dry in a jar for a week. What does a thermometer in the jar "
                "read?",
        "options": [
            {"text": "Room temperature, because nothing changes while they "
                     "stay dry", "correct": True},
            {"text": "Several degrees below the room, because the two "
                     "powders are touching", "correct": False,
             "why": "Touching is not enough. The reaction needs water before "
                    "anything happens."},
            {"text": "Several degrees above the room, because dry powders "
                     "hold their energy in", "correct": False,
             "why": "A dry powder sits at whatever temperature its "
                    "surroundings are."},
            {"text": "Falling steadily, because the reaction runs very "
                     "slowly without water", "correct": False,
             "why": "It does not run at all without water. A week later the "
                    "jar is unchanged."},
        ],
        "figure": None,
    },

    # ── MRB-338 night 3 · standard, second pass ─────────────────────────
    {
        "id": "c7-03-s18",
        "band": "standard",
        "text": "A kiln breaks limestone down into calcium oxide, and its "
                "fire is kept burning all day. The fire is damped down for "
                "an hour. Predict what happens inside the kiln.",
        "options": [
            {"text": "The limestone carries on breaking down on the heat "
                     "stored in the kiln walls", "correct": False,
             "why": "The walls cool as they give that up, and the change "
                    "stops with them. An hour is far too long."},
            {"text": "The breaking down slows and stops, because it needs "
                     "energy supplied to it", "correct": True},
            {"text": "The limestone breaks down faster, because a cooler "
                     "kiln lets the gas escape", "correct": False,
             "why": "Cooling a change never speeds it up, and the gas "
                    "leaving is not what drives it."},
            {"text": "Nothing changes, because the limestone has already "
                     "been heated once", "correct": False,
             "why": "A decomposition is not switched on permanently. It runs "
                    "only while it is being fed."},
        ],
        "figure": None,
    },
    {
        "id": "c7-03-s19",
        "band": "standard",
        "text": "Two endothermic reactions are run in identical beakers of "
                "water. One drops the water by 3 °C and the other by 11 °C. "
                "What does that comparison tell you?",
        "options": [
            {"text": "That only the second is endothermic, because 3 °C is "
                     "too small to count", "correct": False,
             "why": "A small fall is still a fall. Both took energy in from "
                    "the water."},
            {"text": "That the second one produced more cold than the first "
                     "one did", "correct": False,
             "why": "Neither produced any cold. The second took more energy "
                    "in."},
            {"text": "That the second one took more energy in from the water "
                     "than the first did", "correct": True},
            {"text": "That the first one started from a warmer temperature "
                     "than the second one", "correct": False,
             "why": "The size of each fall was compared, and that does not "
                    "depend on where either started."},
        ],
        "figure": None,
    },
    {
        "id": "c7-03-s20",
        "band": "standard",
        "text": "An endothermic reaction runs faster when its beaker is "
                "stood in warm water. Does that make it exothermic?",
        "options": [
            {"text": "Yes, because energy is now going into the reaction "
                     "from the warm water", "correct": False,
             "why": "Energy going INTO the reaction is what endothermic "
                    "means. Warming it has not changed the direction."},
            {"text": "Yes, because anything warmed by its surroundings "
                     "counts as exothermic", "correct": False,
             "why": "Exothermic means the SURROUNDINGS get warmer. Here they "
                    "are still losing energy."},
            {"text": "No, because the warm water cancels out the cooling "
                     "exactly", "correct": False,
             "why": "The warm water speeds the change up. Nothing cancels, "
                    "and the mixture still takes energy in."},
            {"text": "No — warming it changes how fast it runs, not which "
                     "way the energy moves", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c7-03-s21",
        "band": "standard",
        "text": "A student writes that an endothermic reaction \"takes heat "
                "out of the beaker\". Improve that sentence so it says where "
                "the energy ends up.",
        "options": [
            {"text": "It takes energy in from the beaker and stores it in "
                     "the new substances", "correct": True},
            {"text": "It takes energy out of the beaker and destroys it as "
                     "the reaction runs", "correct": False,
             "why": "Energy is never destroyed. It has been moved into the "
                    "products."},
            {"text": "It takes energy out of the beaker and turns it into "
                     "cold in the mixture", "correct": False,
             "why": "There is no cold to turn anything into. What is left "
                    "simply has less energy."},
            {"text": "It takes energy out of the beaker and sends it into "
                     "the air above it", "correct": False,
             "why": "Then the air would warm. Everything around the "
                    "reaction cools, the air included."},
        ],
        "figure": None,
    },
    {
        "id": "c7-03-s22",
        "band": "standard",
        "text": "A squeezed cold pack and a metal spoon straight from a "
                "fridge will both cool a drink. What is the difference "
                "between them?",
        "options": [
            {"text": "There is none — both hold a store of cold that they "
                     "let out into the drink until it is gone", "correct": False,
             "why": "Neither holds any cold. The spoon is simply colder, and "
                    "the pack is running a change."},
            {"text": "The spoon is endothermic and the pack is only cold",
             "correct": False,
             "why": "That is the wrong way round. The pack is the one "
                    "running a change that takes energy in."},
            {"text": "The pack runs a change that takes energy in; the spoon "
                     "only started colder", "correct": True},
            {"text": "The spoon cools the drink further, because metal "
                     "carries energy better", "correct": False,
             "why": "A cold spoon runs out of difference in seconds, however "
                    "well metal conducts."},
        ],
        "figure": None,
    },
    {
        "id": "c7-03-s23",
        "band": "standard",
        "text": "Ammonium nitrate dissolving takes energy IN. Explain how "
                "taking energy in is what treats a swollen ankle.",
        "options": [
            {"text": "The cold it makes numbs the ankle and brings the "
                     "swelling down", "correct": False,
             "why": "No cold is made. The pack works by taking energy out of "
                    "the ankle."},
            {"text": "Energy is taken out of the ankle, so the skin there "
                     "gets colder", "correct": True},
            {"text": "The pack pushes energy into the ankle, which the "
                     "swelling then uses up", "correct": False,
             "why": "Energy moves out of the ankle, not into it. That is why "
                    "the area feels cold."},
            {"text": "The dissolving pulls water out of the swelling through "
                     "the skin", "correct": False,
             "why": "The bag is sealed and nothing crosses the skin. Only "
                    "energy moves."},
        ],
        "figure": None,
    },
    {
        "id": "c7-03-s24",
        "band": "standard",
        "text": "A chemist wants a change that will store energy now and "
                "give it back later. Should they look for an endothermic or "
                "an exothermic change?",
        "options": [
            {"text": "Endothermic, because it takes energy in and stores it "
                     "in the products", "correct": True},
            {"text": "Exothermic, because giving energy out is what storing "
                     "it means", "correct": False,
             "why": "An exothermic change spends a store rather than filling "
                    "one."},
            {"text": "Either, because energy is conserved and so both of "
                     "them store the same amount", "correct": False,
             "why": "Conservation says nothing is lost. It does not make the "
                    "two directions the same."},
            {"text": "Neither, because energy can only be stored inside a "
                     "battery", "correct": False,
             "why": "Every substance holds a chemical store, and "
                    "photosynthesis fills one with sunlight."},
        ],
        "figure": None,
    },
    {
        "id": "c7-03-s25",
        "band": "standard",
        "text": "A freezer has to keep running for the water in it to turn "
                "to ice. Does that make freezing endothermic?",
        "options": [
            {"text": "Yes, because energy has to be supplied for the "
                     "freezing to happen", "correct": False,
             "why": "The electricity runs the pump. The water itself is "
                    "giving energy out."},
            {"text": "No — the water gives energy out, and the freezer's job "
                     "is to carry it away", "correct": True},
            {"text": "Yes, because the ice ends up colder than the water "
                     "was", "correct": False,
             "why": "How cold the product ends up does not decide the "
                    "direction. The water lost energy to get there."},
            {"text": "No, because freezing is a physical change and can be "
                     "neither", "correct": False,
             "why": "Both words describe physical changes too — melting is "
                    "the standard example."},
        ],
        "figure": None,
    },
    {
        "id": "c7-03-s26",
        "band": "standard",
        "text": "A beaker of chemicals is 8 °C colder after an endothermic "
                "reaction than it was before. What is now true of the "
                "chemicals themselves?",
        "options": [
            {"text": "They hold less energy than before, which is why the "
                     "reading fell", "correct": False,
             "why": "The reading fell because the water and the glass lost "
                    "energy. The chemicals gained it."},
            {"text": "They hold the same as before, because energy is "
                     "conserved", "correct": False,
             "why": "Conservation means nothing was lost overall. It moved "
                    "from the surroundings into the products."},
            {"text": "They hold no energy at all now, having given it up to "
                     "the surroundings", "correct": False,
             "why": "Every substance holds a chemical store, and this one "
                    "has gained rather than given."},
            {"text": "They hold more energy than they did, taken from the "
                     "water and the glass", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c7-03-s27",
        "band": "standard",
        "text": "The thermometer in an endothermic reaction falls for thirty "
                "seconds and then stops falling. Give the reason.",
        "options": [
            {"text": "The thermometer has reached the lowest reading it is "
                     "able to show", "correct": False,
             "why": "A laboratory thermometer reads well below anything this "
                    "reaction reaches."},
            {"text": "The reaction has started running backwards and is "
                     "giving the energy back", "correct": False,
             "why": "Nothing reverses on its own. Energy would have to be "
                    "supplied to run it the other way."},
            {"text": "The change has finished, so nothing is taking energy "
                     "in any more", "correct": True},
            {"text": "The surroundings have run out of energy to give to the "
                     "reaction", "correct": False,
             "why": "The water and the room hold far more than any beaker "
                    "reaction takes."},
        ],
        "figure": None,
    },
    {
        "id": "c7-03-s28",
        "band": "standard",
        "text": "Before a cold pack is squeezed, the solid inside it is "
                "measured and found to be at room temperature. What does "
                "that measurement rule out?",
        "options": [
            {"text": "That the pack works by holding something already cold "
                     "inside it", "correct": True},
            {"text": "That the pack takes energy in from the water once it "
                     "has been squeezed", "correct": False,
             "why": "It rules nothing out about that. The taking in starts "
                    "when the two are mixed."},
            {"text": "That the solid dissolves in the water rather than "
                     "reacting with it", "correct": False,
             "why": "A reading taken before squeezing says nothing about "
                    "which kind of change follows."},
            {"text": "That the pack would still work on a cold mountainside "
                     "in winter", "correct": False,
             "why": "Starting at room temperature is no obstacle. It is the "
                    "change that does the cooling."},
        ],
        "figure": None,
    },
    {
        "id": "c7-03-s29",
        "band": "standard",
        "text": "A beaker in which an endothermic reaction is running is "
                "standing in a large tank of water at 20 °C. Predict what "
                "the thermometer in the beaker does.",
        "options": [
            {"text": "It falls and it keeps on falling, because the tank "
                     "has so much energy to give", "correct": False,
             "why": "The tank supplies energy, which stops the beaker "
                    "falling further rather than driving it down."},
            {"text": "It stays at 20 °C throughout, because the tank fixes "
                     "the temperature exactly", "correct": False,
             "why": "The reaction takes energy in faster than the tank can "
                    "replace it, so there is a dip."},
            {"text": "It falls a little and is then pulled back towards "
                     "20 °C by the tank", "correct": True},
            {"text": "It rises above 20 °C, because the tank keeps feeding "
                     "energy into the beaker", "correct": False,
             "why": "The tank only replaces what the reaction removed. It "
                    "cannot push the beaker past its own temperature."},
        ],
        "figure": None,
    },
    {
        "id": "c7-03-s30",
        "band": "standard",
        "text": "A student says a cold pack takes its energy in from the "
                "sun. Correct them.",
        "options": [
            {"text": "They are right, and that is why a pack works better "
                     "outdoors", "correct": False,
             "why": "A pack works just as well in a dark room. Sunlight has "
                    "nothing to do with it."},
            {"text": "They are wrong — it takes energy from the water, the "
                     "bag and the skin", "correct": True},
            {"text": "They are wrong — the pack takes its energy from the "
                     "ice sealed inside it", "correct": False,
             "why": "There is no ice in a cold pack, only a solid and a "
                    "pouch of water."},
            {"text": "They are wrong — the pack makes its own cold and needs "
                     "no energy", "correct": False,
             "why": "No cold is made, and the pack certainly does take "
                    "energy in."},
        ],
        "figure": None,
    },

    # ── MRB-338 night 3 · harder, second pass ───────────────────────────
    {
        "id": "c7-03-h18",
        "band": "harder",
        "text": "A plant photosynthesises and respires at the same time. "
                "Explain how it can still gain mass over a summer.",
        "options": [
            {"text": "Because photosynthesis is endothermic, and taking "
                     "energy in always adds mass", "correct": False,
             "why": "Taking energy in adds no weighable mass. The gain is "
                    "the carbon built into the plant."},
            {"text": "Because respiration stops during the day while "
                     "photosynthesis is running", "correct": False,
             "why": "A plant respires every hour of every day. The two run "
                    "alongside each other."},
            {"text": "Because it photosynthesises more than it respires, so "
                     "more is stored than spent", "correct": True},
            {"text": "Because the two cancel exactly, and the extra mass "
                     "comes up out of the soil", "correct": False,
             "why": "If they cancelled, nothing would be gained. The mass "
                    "comes from carbon dioxide in the air."},
        ],
        "figure": None,
    },
    {
        "id": "c7-03-h19",
        "band": "harder",
        "text": "A student argues that because an endothermic reaction takes "
                "energy in, running one in a classroom should cool the room "
                "down. Evaluate that.",
        "options": [
            {"text": "They are right in principle, but a beaker takes far "
                     "too little to change a room", "correct": True},
            {"text": "They are wrong — an endothermic reaction cools the "
                     "beaker and nothing much beyond it", "correct": False,
             "why": "The bench and the air around it cool as well. The "
                    "surroundings are everything nearby."},
            {"text": "They are wrong — the warmth of the room stops any "
                     "reaction cooling anything", "correct": False,
             "why": "The reaction cools its mixture whatever the room is "
                    "doing. The room only warms it back afterwards."},
            {"text": "They are right, and a few beakers would cool a "
                     "classroom noticeably", "correct": False,
             "why": "The amounts are tiny beside a room full of air, walls "
                    "and people."},
        ],
        "figure": None,
    },
    {
        "id": "c7-03-h20",
        "band": "harder",
        "text": "An endothermic change and an exothermic change are run side "
                "by side in one sealed room, and each moves the same amount "
                "of energy. What happens to the room's total energy?",
        "options": [
            {"text": "It falls, because the endothermic change removes "
                     "energy permanently", "correct": False,
             "why": "Nothing is removed permanently. It is stored in the "
                    "products, still inside the room."},
            {"text": "It rises, because the exothermic change releases "
                     "energy that was not there before", "correct": False,
             "why": "That energy was already there, held in its chemicals. "
                    "Nothing new is created."},
            {"text": "It stays the same — energy has only been moved between "
                     "stores", "correct": True},
            {"text": "It cannot be worked out without knowing which of the "
                     "two changes ran first", "correct": False,
             "why": "Order changes nothing. The two transfers are equal and "
                    "opposite whenever they happen."},
        ],
        "figure": None,
    },
    {
        "id": "c7-03-h21",
        "band": "harder",
        "text": "A first aid instructor says a cold pack should come off "
                "after twenty minutes. Suggest why it may have stopped being "
                "useful well before then.",
        "options": [
            {"text": "Because the skin stops feeling cold long before the "
                     "pack itself stops being cold", "correct": False,
             "why": "Whether it is felt is not the question. The pack itself "
                    "stops taking energy in."},
            {"text": "Because the dissolving finishes, after which the pack "
                     "only warms back up", "correct": True},
            {"text": "Because the pack has to be squeezed again every few "
                     "minutes to keep it going", "correct": False,
             "why": "Squeezing a used pack does nothing. The solid has "
                    "already dissolved."},
            {"text": "Because an endothermic change reverses itself once the "
                     "surroundings are cold", "correct": False,
             "why": "It does not reverse on its own. It simply finishes."},
        ],
        "figure": None,
    },
    {
        "id": "c7-03-h22",
        "band": "harder",
        "text": "One student says an endothermic reaction loses energy; "
                "another says it gains energy. Which of them is right?",
        "options": [
            {"text": "The first, because the reading on the thermometer goes "
                     "down", "correct": False,
             "why": "The thermometer reads the surroundings. The chemicals "
                    "gained what the surroundings lost."},
            {"text": "The second, because energy can only ever be gained and "
                     "never lost", "correct": False,
             "why": "Energy is lost by whatever gives it up, and here that "
                    "is the water and the beaker."},
            {"text": "Neither, because energy is conserved and so nothing "
                     "gains or loses any", "correct": False,
             "why": "Conservation means none is created or destroyed. It "
                    "still moves between things."},
            {"text": "Both, about different things — the surroundings lose "
                     "it and the chemicals gain it", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c7-03-h23",
        "band": "harder",
        "text": "An endothermic reaction takes in 4 kJ of energy. The same "
                "reaction is then run backwards to warm a room. How much "
                "energy does it give out?",
        "options": [
            {"text": "8 kJ, twice what it took in", "correct": False,
             "why": "Reversing a change gives back exactly what it took, not "
                    "twice as much."},
            {"text": "4 kJ, the same amount it took in", "correct": True},
            {"text": "2 kJ, because some is always lost on the way back",
             "correct": False,
             "why": "None is lost. The reverse transfer is the same size as "
                    "the forward one."},
            {"text": "None — an endothermic change cannot be run backwards",
             "correct": False,
             "why": "Reversing it is exactly what resets a hand warmer, and "
                    "it is how the energy comes back."},
        ],
        "figure": None,
    },
    {
        "id": "c7-03-h24",
        "band": "harder",
        "text": "One beaker falls from 22 °C to 14 °C and another from 40 °C "
                "to 32 °C. A student says only the first is endothermic, "
                "because 32 °C is still warm. Evaluate that.",
        "options": [
            {"text": "They are right — a reaction that ends up above room "
                     "temperature is exothermic", "correct": False,
             "why": "Where a reaction ends does not matter. The second fell "
                    "by the same eight degrees."},
            {"text": "They are wrong — both fell by 8 °C, and a fall is what "
                     "endothermic means", "correct": True},
            {"text": "They are right, because the second one must have been "
                     "heated up to start with", "correct": False,
             "why": "How it reached 40 °C is a separate question. Once "
                    "running, it took energy in."},
            {"text": "They are wrong, but only because the second one fell "
                     "further than the first", "correct": False,
             "why": "Both fell by exactly eight degrees. The point is that "
                    "both fell at all."},
        ],
        "figure": None,
    },
    {
        "id": "c7-03-h25",
        "band": "harder",
        "text": "A vaccine has to be kept cold for a two-day journey with no "
                "electricity. Evaluate using instant cold packs for the job.",
        "options": [
            {"text": "They would work well, because each pack stays close to "
                     "0 °C for days on end", "correct": False,
             "why": "A pack is cold for minutes rather than days. The "
                    "dissolving finishes quickly."},
            {"text": "They would work well, because a pack can be squeezed "
                     "again whenever it warms", "correct": False,
             "why": "A pack works once. Squeezing a used one does nothing at "
                    "all."},
            {"text": "They would fail, because a cold pack warms whatever it "
                     "is put next to", "correct": False,
             "why": "It cools what it touches. The problem is how briefly, "
                    "not which direction."},
            {"text": "They would fail, because each pack cools only until "
                     "its change has finished", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c7-03-h26",
        "band": "harder",
        "text": "Photosynthesis takes in far more energy each year than all "
                "the world's fires release. Explain why that does not mean "
                "the Earth is steadily getting colder.",
        "options": [
            {"text": "Because plants hand it straight back as they grow, so "
                     "nothing is stored", "correct": False,
             "why": "Growth IS the storing. A tree holds what it took in for "
                    "as long as it stands."},
            {"text": "Because the energy is stored rather than destroyed, "
                     "and respiration and decay release most of it again",
             "correct": True},
            {"text": "Because fires release far more energy than anybody has "
                     "ever managed to measure", "correct": False,
             "why": "The comparison runs the other way, and guessing at the "
                    "number changes nothing."},
            {"text": "Because the Earth makes new energy to replace whatever "
                     "the plants take in", "correct": False,
             "why": "Energy is never created. Nothing replaces it, and "
                    "nothing needs to."},
        ],
        "figure": None,
    },
    {
        "id": "c7-03-h27",
        "band": "harder",
        "text": "A Bunsen is used to burn magnesium, and then to decompose "
                "copper carbonate. Compare what the flame is doing in each "
                "case.",
        "options": [
            {"text": "It supplies the energy for both, and both stop the "
                     "moment it is taken away", "correct": False,
             "why": "Magnesium keeps burning once lit. Only the carbonate "
                    "needs the flame kept under it."},
            {"text": "It starts the burning and can then be taken away; the "
                     "carbonate needs it kept there", "correct": True},
            {"text": "It only starts each of them, and neither one needs it "
                     "once it is going", "correct": False,
             "why": "Take the flame from the carbonate and the decomposition "
                    "stops at once."},
            {"text": "It supplies the oxygen in both cases, which is what "
                     "each change runs on", "correct": False,
             "why": "A Bunsen supplies energy, not oxygen, and a "
                    "decomposition needs no oxygen at all."},
        ],
        "figure": None,
    },
    {
        "id": "c7-03-h28",
        "band": "harder",
        "text": "A cool box can be packed with ice or with squeezed cold "
                "packs. Explain which would hold it at a steady temperature "
                "for longer.",
        "options": [
            {"text": "The cold packs, because each one starts off colder "
                     "than ice does", "correct": False,
             "why": "A pack reaches about 0 °C, no colder than ice, and it "
                    "warms back within minutes."},
            {"text": "Neither — both hold their temperature for exactly as "
                     "long as they last", "correct": False,
             "why": "A pack's change finishes in minutes, while melting ice "
                    "goes on for hours."},
            {"text": "The cold packs, because a chemical change lasts longer "
                     "than a physical one", "correct": False,
             "why": "How long a change lasts has nothing to do with which "
                    "kind of change it is."},
            {"text": "The ice, because it stays at 0 °C for the whole time "
                     "it is melting", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c7-03-h29",
        "band": "harder",
        "text": "A student says exothermic and endothermic are opposites, so "
                "half of all changes must be endothermic. Evaluate that.",
        "options": [
            {"text": "They are wrong — being opposite directions says "
                     "nothing about how many go each way", "correct": True},
            {"text": "They are right, because every change has a reverse "
                     "and so the two of them have to balance", "correct": False,
             "why": "Every change has a reverse, but not every reverse is "
                    "something that happens."},
            {"text": "They are right, and the ones we meet are simply the "
                     "exothermic half of them", "correct": False,
             "why": "There is no hidden half. Endothermic changes really are "
                    "the rarer kind."},
            {"text": "They are wrong, because most changes are neither one "
                     "nor the other", "correct": False,
             "why": "Every change moves energy one way or the other. There "
                    "is no third option."},
        ],
        "figure": None,
    },
    {
        "id": "c7-03-h30",
        "band": "harder",
        "text": "A student argues that because energy is conserved, an "
                "endothermic reaction must eventually give its energy back "
                "on its own. Evaluate that.",
        "options": [
            {"text": "They are right, and that is why a beaker returns to "
                     "room temperature afterwards", "correct": False,
             "why": "The beaker warms because the room warms it. The stored "
                    "energy stays in the products."},
            {"text": "They are right, because conservation means that "
                     "energy cannot stay in one place", "correct": False,
             "why": "Conservation says energy is not created or destroyed. "
                    "It says nothing about having to move."},
            {"text": "They are wrong — the energy comes back only if the "
                     "change is reversed", "correct": True},
            {"text": "They are wrong, because conservation does not apply "
                     "to an endothermic reaction", "correct": False,
             "why": "It applies to every change without exception. That is "
                    "why the energy is still there to find."},
        ],
        "figure": None,
    },
]
