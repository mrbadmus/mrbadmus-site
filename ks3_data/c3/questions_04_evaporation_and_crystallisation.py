"""C3 lesson 04 — Evaporation and crystallisation: twelve questions (MRB-269).

The lesson's argument is that the method changes the CRYSTAL and never the
YIELD: three ways of taking the water off, nine runs on the bench, and the same
mass of solute recovered every single time. These twelve probe that argument
from the angles the ladder leaves alone — which of the two words names what
the solute does, which half of the mixture the method keeps and which half it
throws away, and what a claim that joins speed to yield is actually getting
wrong.

⚠️ This question bank is NEW PROSE. Unlike the lesson record, none of it is
lifted from Design's page; it is written to the bar in the authoring brief §4
and §5, and every science claim in it is checked against the lesson body. No
question introduces a fact the lesson does not teach, and no `why` retracts
anything the lesson says.

The distractors are built from the lesson's two declared misconceptions.
MIX-09 (faster evaporation gives more product) drives the wrong options in
e03, s01, s02, s03 and h03 — every one of them treats speed, heat or
"efficiency" as something that changes how much solid comes out, when the
bench holds the recovered mass at 5.0 g through all nine runs. MIX-08
(evaporated water is gone — destroyed) drives e02, h01 and h04's first
distractor, where the solvent is imagined as annihilated, absorbed, converted
into the solute, or manufactured from nothing.

A third strand, everywhere in the lesson and not in the register, is that
evaporation keeps the SOLID and loses the LIQUID, so it is the wrong method
the moment the liquid is what you want: e01, e04, s04 and h02 each carry a
distractor that has the two the wrong way round, or that expects to keep both.

⚑ h02 rests on the stretch layer (water of crystallisation, science flag 8).
It is in the `harder` band for that reason, and it asks only what the stretch
paragraph and the bench's own warning both say: the water built into the
crystal is driven out, and cooling does not put it back.
"""

UNIT = "C3"
LESSON = "evaporation-and-crystallisation"
LESSON_NUMBER = 4

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "c3-04-e01",
        "band": "easier",
        "text": "Evaporation and crystallisation are two different things "
                "happening at the same time in the dish. Which one describes "
                "what the solute does?",
        "options": [
            {"text": "Evaporation — the solute leaves the dish as a gas",
             "correct": False,
             "why": "The solvent is the one that leaves as a gas. The solute "
                    "stays in the dish, which is the only reason this method "
                    "is worth doing at all."},
            {"text": "Crystallisation — the solute joins a growing, regular "
                     "arrangement", "correct": True},
            {"text": "Evaporation — the solute spreads out evenly through "
                     "the liquid", "correct": False,
             "why": "That is dissolving, and it had already happened before "
                    "the dish went anywhere near the heat. Evaporation is the "
                    "solvent leaving."},
            {"text": "Crystallisation — the solvent turns into a solid in "
                     "the dish", "correct": False,
             "why": "The solvent goes into the air as a gas; it does not turn "
                    "solid. What turns solid is the solute coming out of "
                    "solution."},
        ],
        "figure": None,
    },
    {
        "id": "c3-04-e02",
        "band": "easier",
        "text": "A dish of salt solution is left in a warm room until it is "
                "completely dry. Where is the water now?",
        "options": [
            {"text": "It was destroyed as the dish dried out", "correct": False,
             "why": "Nothing is destroyed by evaporation. Every water "
                    "particle that left the dish is still a water particle, "
                    "somewhere in the room."},
            {"text": "It turned into the salt that is left in the dish",
             "correct": False,
             "why": "Water cannot turn into salt. Both were there all along "
                    "— the salt dissolved and invisible, the water "
                    "around it — and only the water has left."},
            {"text": "It is in the air as a gas, and could be collected on a "
                     "cold surface", "correct": True},
            {"text": "It soaked into the dish and could be squeezed back out",
             "correct": False,
             "why": "An evaporating dish absorbs nothing. The water left the "
                    "surface one particle at a time and joined the air above "
                    "it."},
        ],
        "figure": None,
    },
    {
        "id": "c3-04-e03",
        "band": "easier",
        "text": "Three dishes of the same solution are dried three ways: "
                "boiled hard over a Bunsen, warmed over a water bath, and "
                "left on a windowsill. Which gives the largest crystals?",
        "options": [
            {"text": "The windowsill, because only a few crystals start and "
                     "they grow slowly", "correct": True},
            {"text": "The Bunsen, because heat makes crystals grow faster "
                     "and so grow bigger", "correct": False,
             "why": "Heat makes the water leave faster, not the crystals grow "
                    "bigger. Thousands start at the same moment and none of "
                    "them gets big."},
            {"text": "The water bath, because that is the method a school "
                     "practical uses", "correct": False,
             "why": "The water bath is the compromise, not the best result: "
                    "quick enough to finish in a lesson, and the crystals it "
                    "gives are small and clear rather than large."},
            {"text": "All three the same, because the solution and the mass "
                     "of salt are the same", "correct": False,
             "why": "The mass really is the same in all three. The crystals "
                    "are not — how fast the solvent leaves is exactly what "
                    "sets their size."},
        ],
        "figure": None,
    },
    {
        "id": "c3-04-e04",
        "band": "easier",
        "text": "Evaporating a solution to dryness gives you one half of the "
                "mixture and costs you the other. Which way round is it?",
        "options": [
            {"text": "You keep both, in two separate containers",
             "correct": False,
             "why": "Keeping both takes something that catches the vapour. "
                    "Plain evaporation has nothing to catch it, so the "
                    "solvent is gone."},
            {"text": "You lose both — the dish ends up empty",
             "correct": False,
             "why": "Weigh the dish afterwards and the solute is there to the "
                    "gram. Only the solvent leaves."},
            {"text": "You keep the liquid and lose the solid", "correct": False,
             "why": "It is the other way round. The solute stays behind in "
                    "the dish and the solvent goes into the air."},
            {"text": "You keep the solid and lose the liquid", "correct": True},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "c3-04-s01",
        "band": "standard",
        "text": "A student wants one large, sharp copper sulfate crystal to "
                "keep. Which method should she use?",
        "options": [
            {"text": "Boil it dry over a Bunsen, because it is finished "
                     "inside one lesson", "correct": False,
             "why": "Speed costs her the one thing she is after. Boiling "
                    "gives a fine crust, and heating a dry dish of copper "
                    "sulfate turns it white and ruins it."},
            {"text": "Warm it over a water bath, because a school practical "
                     "always uses one", "correct": False,
             "why": "A water bath gives small, clear, well-formed crystals "
                    "inside a lesson. A large one needs longer than a lesson, "
                    "whatever the usual practical does."},
            {"text": "Leave it to evaporate slowly over days, because big "
                     "crystals are made of time", "correct": True},
            {"text": "Any of the three, because the crystals are set by the "
                     "substance and not the method", "correct": False,
             "why": "The substance sets the shape. The rate sets the size — "
                    "which is why one solution gives a crust one way and "
                    "centimetre crystals another."},
        ],
        "figure": None,
    },
    {
        "id": "c3-04-s02",
        "band": "standard",
        "text": "A student boils 20 cm³ of salt solution dry over a Bunsen "
                "and recovers 5.0 g of salt. Her partner leaves an identical "
                "20 cm³ of the same solution on a windowsill until it is dry. "
                "What mass of salt does he recover?",
        # Four options of equal length; only the number changes. The hedge is
        # the same in all four — there is none — so nothing about the
        # wording can point at the answer.
        "options": [
            {"text": "5.0 g", "correct": True},
            {"text": "7.5 g", "correct": False,
             "why": "Slow evaporation is not more efficient. It cannot put "
                    "salt into the dish that was never dissolved in the "
                    "solution to begin with."},
            {"text": "3.5 g", "correct": False,
             "why": "Salt does not evaporate. However long the dish stands, "
                    "the solute cannot leave it — only the solvent can."},
            {"text": "2.5 g", "correct": False,
             "why": "Nothing is lost by waiting. The solution held 5.0 g of "
                    "salt, and all 5.0 g is in the dish once the water has "
                    "gone."},
        ],
        "figure": None,
    },
    {
        "id": "c3-04-s03",
        "band": "standard",
        "text": "Boiling a solution dry leaves a crust of crystals too small "
                "to pick up individually. Why are they so small?",
        "options": [
            {"text": "The heat keeps breaking the crystals up as fast as "
                     "they form", "correct": False,
             "why": "Nothing is breaking them. They are small because there "
                    "are so many of them, each sharing out the same amount of "
                    "solute."},
            {"text": "Solute comes out everywhere at once, so thousands of "
                     "crystals start together", "correct": True},
            {"text": "Boiling makes the solute particles themselves smaller "
                     "than they were", "correct": False,
             "why": "Particles do not change size. The crystals are small "
                    "because so many of them started at the same moment, not "
                    "because the particles shrank."},
            {"text": "Most of the solute has already gone by the time the "
                     "dish is dry", "correct": False,
             "why": "All of the solute is still there — the recovered mass "
                    "is the same as a slow run gives. It is shared across "
                    "thousands of crystals instead of a few."},
        ],
        "figure": None,
    },
    {
        "id": "c3-04-s04",
        "band": "standard",
        "text": "A coastal village has all the sea water it could want and "
                "needs drinking water. Why is boiling sea water dry in an "
                "open pan exactly the wrong thing to do?",
        "options": [
            {"text": "Boiling does not actually take the salt out of sea "
                     "water", "correct": False,
             "why": "It separates them perfectly well. The trouble is which "
                    "half they are left holding: the salt stays in the pan "
                    "and the water goes into the air."},
            {"text": "The salt would burn and spoil whatever water was left "
                     "in the pan", "correct": False,
             "why": "Salt does not burn, and there is no water left in the "
                    "pan at the end. That is the whole of the difficulty."},
            {"text": "Sea water is a compound, so no method can separate it "
                     "into parts", "correct": False,
             "why": "Sea water is a mixture and separating it is "
                    "straightforward. The only question is which part the "
                    "method keeps."},
            {"text": "It keeps the part they mean to throw away and loses "
                     "the part they want", "correct": True},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "c3-04-h01",
        "band": "harder",
        "text": "While a dish of salt solution is evaporating, a cold glass "
                "plate is held above it. Drops of clear liquid form on the "
                "underside of the plate. What does that show?",
        "options": [
            {"text": "The cold plate is pulling water back out of the salt "
                     "left in the dish", "correct": False,
             "why": "The salt is giving nothing up. The drops are solvent "
                    "that had already left the solution, cooled on the plate "
                    "back into a liquid."},
            {"text": "The water that left the solution is still water, and "
                     "can be turned back to liquid", "correct": True},
            {"text": "Some of the salt evaporated along with the water, "
                     "so the drops on the plate will taste salty",
             "correct": False,
             "why": "The drops are fresh. Salt does not evaporate at these "
                    "temperatures, so only the solvent ever reached the "
                    "plate."},
            {"text": "The plate is making new water out of the gases that "
                     "were in the room", "correct": False,
             "why": "Nothing is being made. The particles on the plate are "
                    "the ones that left the dish, and there are exactly as "
                    "many of them as left it."},
        ],
        "figure": None,
    },
    {
        "id": "c3-04-h02",
        "band": "harder",
        "text": "A student grows deep blue copper sulfate crystals, then "
                "heats the dry dish hard to finish it off. The blue crystals "
                "become a white powder. What happened, and will cooling the "
                "dish bring the blue back?",
        "options": [
            {"text": "Water built into the crystals was driven out, and "
                     "cooling alone will not restore them", "correct": True},
            {"text": "The copper sulfate was destroyed by the heat, so "
                     "nothing at all will restore it", "correct": False,
             "why": "The substance is still in the dish and can still be "
                    "weighed. What has gone is the water that was built into "
                    "the crystal, not the copper sulfate."},
            {"text": "The blue colour was bleached by the flame, and cooling "
                     "will bring the colour back", "correct": False,
             "why": "This is not a colour fading. The crystals themselves "
                    "have gone, and the white powder is what is left once the "
                    "water in them is driven off."},
            {"text": "The crystals melted, and they will set again as blue "
                     "crystals as the dish cools", "correct": False,
             "why": "Nothing melted — melted crystals would run, and this "
                    "is a dry powder. Cooling gives back neither the water "
                    "nor the crystals."},
        ],
        "figure": None,
    },
    {
        "id": "c3-04-h03",
        "band": "harder",
        "text": "A student writes: “Boiling is the better method because "
                "it is faster, so you get more of the solid.” Which part "
                "of that is right?",
        "options": [
            {"text": "All of it, because speed and how much you get go "
                     "together in any separation", "correct": False,
             "why": "They do not go together here at all. The mass recovered "
                    "was identical for all three methods; the only thing that "
                    "changed was the crystals."},
            {"text": "None of it, because boiling is neither faster nor "
                     "better in any situation at all", "correct": False,
             "why": "Boiling genuinely is faster, and when only the mass "
                    "matters that makes it the right choice. It is the 'more "
                    "of the solid' half that fails."},
            {"text": "Only the second half, because boiling is in fact the "
                     "slowest of the three methods on the bench",
             "correct": False,
             "why": "Boiling is the fastest of the three — four minutes "
                    "against six days on a windowsill. It is the yield claim "
                    "that does not survive."},
            {"text": "Only the first half, because the mass recovered is the "
                     "same whichever method is used", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c3-04-h04",
        "band": "harder",
        "text": "Gypsum crystals in a Mexican cave grew metres long, in "
                "mineral-rich water held at a steady temperature for hundreds "
                "of thousands of years. What best explains their size?",
        "options": [
            {"text": "The cave was warm, and heat is what makes crystals "
                     "grow large rather than small", "correct": False,
             "why": "Heat is not what grows a crystal large. A Bunsen is the "
                    "hottest option on the bench and gives the smallest "
                    "crystals of the three."},
            {"text": "There was far more dissolved mineral there than any "
                     "laboratory dish could ever hold", "correct": False,
             "why": "More solute gives more solid, not bigger single "
                    "crystals. Boil a very concentrated solution and you "
                    "still get a crust."},
            {"text": "Very few crystals started, and everything coming out "
                     "of solution afterwards joined those", "correct": True},
            {"text": "Separate crystals kept joining each other over time "
                     "until they had merged into one beam", "correct": False,
             "why": "They grew rather than merged. Each beam is one regular "
                    "arrangement that particles kept joining, in order, for a "
                    "very long time."},
        ],
        "figure": None,
    },
]
