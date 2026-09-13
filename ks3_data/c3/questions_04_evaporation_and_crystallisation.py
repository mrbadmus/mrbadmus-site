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
                     "so the drops on the plate will leave a white crust when dried",
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

    # ── easier · MRB-335 top-up ─────────────────────────────────────────
    {
        "id": "c3-04-e05",
        "band": "easier",
        "text": "What is a crystal?",
        "options": [
            {"text": "Any solid that is clear enough to see through, such as "
                     "glass or ice",
             "correct": False,
             "why": "Being see-through has nothing to do with it. Salt "
                    "crystals are opaque and metals are crystalline"},
            {"text": "A solid that has been made by heating a solution",
             "correct": False,
             "why": "Slow evaporation on a windowsill makes the best crystals "
                    "of all, and nothing is heated"},
            {"text": "A very small piece of a solid",
             "correct": False,
             "why": "Crystals come metres long in the right conditions. Size "
                    "is not the definition"},
            {"text": "A solid whose particles sit in a regular repeating "
                     "arrangement, giving flat faces and sharp edges",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c3-04-e06",
        "band": "easier",
        "text": "A geologist has rock salt dissolved and filtered, and needs the mass of the salt today. Which method should she use?",
        "options": [
            {
             "text": "Boil it dry over a Bunsen",
             "correct": True,
            },
            {
             "text": "Leave it on a windowsill for a week, because slow evaporation is the method that recovers the most of the solid",
             "correct": False,
             "why": "The mass recovered is the same either way, and she needs it today",
            },
            {
             "text": "Filter it again through a fresh paper",
             "correct": False,
             "why": "The salt is dissolved, so it goes straight through. It has already been filtered once",
            },
            {
             "text": "Distil it and weigh what comes over",
             "correct": False,
             "why": "Distilling keeps the water and leaves the salt behind. She would be weighing the wrong half",
            },
        ],
        "figure": None,
    },
    {
        "id": "c3-04-e07",
        "band": "easier",
        "text": "Salt pans around the Mediterranean flood a shallow bed with "
                "sea water and let the sun take the water over weeks. What is "
                "that?",
        "options": [
            {"text": "Distillation, done outdoors and on an enormous scale, "
                     "with the sun supplying the heat instead of a burner",
             "correct": False,
             "why": "Nothing catches the vapour, and the water is thrown "
                    "away. Distillation keeps the liquid"},
            {"text": "Evaporation and crystallisation, at the scale of a "
                     "field",
             "correct": True},
            {"text": "Filtration on a large scale",
             "correct": False,
             "why": "Nothing is poured through anything, and the salt was "
                    "dissolved rather than in lumps"},
            {"text": "Chromatography using the sand as the paper",
             "correct": False,
             "why": "Nothing climbs anything and nothing is being separated "
                    "from another dissolved substance"},
        ],
        "figure": None,
    },

    # ── standard · MRB-335 top-up ───────────────────────────────────────
    {
        "id": "c3-04-s05",
        "band": "standard",
        "text": "The instructions say to take the heat away while there is "
                "still a little liquid in the dish, and let the last of it go "
                "on its own. Why?",
        "options": [
            {"text": "Because the last of the liquid is the part that holds "
                     "the impurities, and letting it go slowly leaves them "
                     "behind in the dish",
             "correct": False,
             "why": "Anything dissolved stays in the dish however the last of "
                    "the water goes. The reason is about damaging the "
                    "crystals"},
            {"text": "So that more of the solid is recovered",
             "correct": False,
             "why": "The mass recovered is the same either way. The solute "
                    "cannot leave the dish"},
            {"text": "Because the dish would crack if it were heated dry",
             "correct": False,
             "why": "An evaporating basin takes a dry Bunsen flame without "
                    "trouble. It is the crystals that suffer"},
            {"text": "So that the crystals are not over-heated and driven to "
                     "powder",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c3-04-s06",
        "band": "standard",
        "text": "Two dishes hold the same solution on the same windowsill: "
                "one wide and shallow, one narrow and deep. Which dries "
                "first?",
        "options": [
            {"text": "The wide one, because more of its surface is open to "
                     "the air",
             "correct": True},
            {"text": "The narrow one, because the solution in it is deeper "
                     "and so is warmed right through by the sun much faster "
                     "than a thin layer is",
             "correct": False,
             "why": "A deep body of liquid warms more slowly, not faster — "
                    "and what matters is how much surface is open to the "
                    "air"},
            {"text": "They dry at the same time, because the solution and the "
                     "room are the same",
             "correct": False,
             "why": "Evaporation happens at the surface, so the shape of the "
                    "dish changes how fast it goes"},
            {"text": "The wide one, because a shallow layer holds less "
                     "solution",
             "correct": False,
             "why": "Right answer, wrong reason — the two dishes hold the "
                    "same amount. It is the exposed surface that differs"},
        ],
        "figure": None,
    },
    {
        "id": "c3-04-s07",
        "band": "standard",
        "text": "Sea salt is made by evaporating sea water. Why is what comes "
                "out not pure sodium chloride?",
        "options": [
            {"text": "Because the sun is not hot enough to drive off all of "
                     "the water",
             "correct": False,
             "why": "The pans go dry. What makes it impure is the other "
                    "dissolved substances, not leftover water"},
            {"text": "Because sea water holds several dissolved substances, "
                     "and evaporation leaves all of them behind together",
             "correct": True},
            {"text": "Because some of the sodium chloride evaporates with the "
                     "water",
             "correct": False,
             "why": "Salt does not evaporate at anything like these "
                    "temperatures. All of it stays"},
            {"text": "Because sand blows into the pans",
             "correct": False,
             "why": "That would be a stray bit of grit, and it can be "
                    "filtered out. The dissolved substances cannot"},
        ],
        "figure": None,
    },

    # ── harder · MRB-335 top-up ─────────────────────────────────────────
    {
        "id": "c3-04-h05",
        "band": "harder",
        "text": "A solution holds TWO dissolved solids. It is evaporated to "
                "dryness. What is in the dish?",
        "options": [
            {"text": "The one that dissolves less readily, since the other "
                     "one stays in solution right up until the last of the "
                     "water goes and is then lost with it",
             "correct": False,
             "why": "Neither leaves with the water. Both are left in the dish "
                    "together"},
            {"text": "Whichever crystallises first, on its own",
             "correct": False,
             "why": "One may start first, and the other still comes out "
                    "before the dish is dry. Both end up in it"},
            {"text": "Neither — they cancel each other out",
             "correct": False,
             "why": "Nothing cancels. Evaporation removes the solvent and "
                    "leaves everything that was dissolved"},
            {"text": "Both of them, mixed together",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c3-04-h06",
        "band": "harder",
        "text": "A saturated copper sulfate solution is left on a windowsill "
                "for a month in a flask with a stopper in it, and no crystals "
                "form. Why not?",
        "options": [
            {"text": "The stopper keeps the solvent in, so the solution never "
                     "becomes more concentrated than it already is",
             "correct": True},
            {"text": "The solution was not left for long enough for crystals "
                     "to form",
             "correct": False,
             "why": "An open dish of the same solution gives crystals within "
                    "days. Time is not what is missing"},
            {"text": "Copper sulfate only crystallises when it is heated",
             "correct": False,
             "why": "The largest copper sulfate crystals are grown cold and "
                    "slowly. Heating makes them smaller"},
            {"text": "The flask is the wrong shape for crystals to grow in",
             "correct": False,
             "why": "Shape affects how fast the solvent leaves. With a "
                    "stopper in, none leaves at all"},
        ],
        "figure": None,
    },
    {
        "id": "c3-04-h07",
        "band": "harder",
        "text": "A student writes: “Slow evaporation is the better method, "
                "because you lose less of the solid into the air.” What is "
                "wrong with that?",
        "options": [
            {"text": "Slow evaporation is worse, because leaving a dish "
                     "standing for a week gives dust and dirt from the room "
                     "plenty of time to settle into it",
             "correct": False,
             "why": "Contamination is a real practical worry and it is not "
                    "what is wrong here. The stated reason is the error"},
            {"text": "Nothing is lost into the air by either method, so the "
                     "reason given is not a reason at all",
             "correct": True},
            {"text": "Boiling is the better method in every case",
             "correct": False,
             "why": "Neither method is better in every case. It depends on "
                    "whether you want big crystals or a quick answer"},
            {"text": "Slow evaporation gives smaller crystals, so it is worse "
                     "for a display",
             "correct": False,
             "why": "The other way round. Slow growth is what gives large "
                    "crystals"},
        ],
        "figure": None,
    },

    # ── easier · MRB-338 expansion ──────────────────────────────────────
    {
        "id": "c3-04-e08",
        "band": "easier",
        "text": "Does a solution have to be boiled before the solvent can "
                "leave it?",
        "options": [
            {"text": "No — the solvent leaves the surface at any "
                     "temperature, and heat only makes it faster",
             "correct": True},
            {"text": "Yes — nothing leaves a liquid until it reaches its "
                     "boiling point",
             "correct": False,
             "why": "A puddle dries on a cold day and never gets near 100 °C. "
                    "Boiling is fast evaporation, not the only kind"},
            {"text": "Yes — the solute cannot come out of solution below "
                     "100 °C",
             "correct": False,
             "why": "Crystals grow on a windowsill at room temperature over "
                    "days, and nothing there gets anywhere near 100 °C"},
            {"text": "Only when the solvent happens to be water; every other "
                     "kind of solvent has to be boiled before it will leave",
             "correct": False,
             "why": "Every solvent evaporates below its boiling point, water "
                    "included — which is why washing dries on a winter line"},
        ],
        "figure": None,
    },
    {
        "id": "c3-04-e09",
        "band": "easier",
        "text": "A water bath is a dish of solution standing in a pan of "
                "boiling water. What is the highest temperature the solution "
                "in it can reach?",
        "options": [
            {"text": "As hot as the Bunsen flame itself, so long as the "
                     "flame is left burning",
             "correct": False,
             "why": "The flame heats the pan of water and the pan of water "
                    "heats the dish, so nothing in it gets near flame heat"},
            {"text": "Any temperature at all, as long as the Bunsen is left "
                     "burning for long enough",
             "correct": False,
             "why": "Once the pan is boiling, extra heating makes it boil "
                    "harder rather than hotter. The temperature holds"},
            {"text": "About 100 °C, because the water around it cannot get "
                     "hotter than that",
             "correct": True},
            {"text": "About 37 °C, because a water bath is always kept at "
                     "body temperature",
             "correct": False,
             "why": "That is an incubator in a biology laboratory. A "
                    "chemistry water bath is a pan of boiling water"},
        ],
        "figure": None,
    },
    {
        "id": "c3-04-e10",
        "band": "easier",
        "text": "Why must safety glasses be worn while a solution is evaporated over a Bunsen?",
        "options": [
            {
             "text": "Because the solid left in the dish gives off a fine dust as it dries, which drifts upwards",
             "correct": False,
             "why": "Dry solid sits where it forms and gives off no dust. The hazard is hot solution spitting out of the dish",
            },
            {
             "text": "Because hot solution spits out of the dish as the last of the liquid boils off",
             "correct": True,
            },
            {
             "text": "Because the vapour coming off the dish is corrosive and burns the eyes",
             "correct": False,
             "why": "The vapour is the solvent, and from a salt solution that is plain water. What reaches your face is spray",
            },
            {
             "text": "Because the glare of a roaring blue Bunsen flame damages the eyes",
             "correct": False,
             "why": "A Bunsen is not bright enough to hurt anybody's eyes. It is hot liquid leaving the dish that they guard against",
            },
        ],
        "figure": None,
    },
    {
        "id": "c3-04-e11",
        "band": "easier",
        "text": "A solid is dissolved in propanone, a solvent that catches "
                "fire easily. How should the solvent be removed to get the "
                "solid back?",
        "options": [
            {"text": "Over a roaring blue Bunsen flame, so that it is "
                     "finished as quickly as possible",
             "correct": False,
             "why": "A naked flame beside a flammable solvent is how a fire "
                    "starts. Finishing early is not worth that"},
            {"text": "In a stoppered flask, so that none of the vapour can "
                     "reach the air in the room",
             "correct": False,
             "why": "With a stopper in, the solvent cannot leave at all, so "
                    "nothing evaporates and no solid is recovered"},
            {"text": "It cannot be removed, because a flammable solvent "
                     "will not evaporate from an open dish",
             "correct": False,
             "why": "Propanone evaporates faster than water at the same "
                    "temperature. The care needed is about the flame"},
            {"text": "By warming the dish over a hot water bath, well away "
                     "from any naked flame",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c3-04-e12",
        "band": "easier",
        "text": "A student scrapes her dry crystals out of the dish and weighs them, but a little of the solid stays stuck to the dish. How does that affect the mass she records?",
        "options": [
            {
             "text": "It is lower than the mass of solute that was dissolved in the solution",
             "correct": True,
            },
            {
             "text": "It is higher — the dish goes onto the balance along with the crystals that came out of it",
             "correct": False,
             "why": "The crystals are scraped out before weighing, so the dish is not on the balance. Leaving some behind can only lose mass",
            },
            {
             "text": "It is unchanged — the solute's mass was fixed from the start",
             "correct": False,
             "why": "The mass in the solution was indeed fixed. The mass on the balance is only the part she managed to collect",
            },
            {
             "text": "It is lower, because dry crystals evaporate slowly while they are being scraped out",
             "correct": False,
             "why": "Dry crystals do not evaporate at room temperature. What is missing is the part still stuck to the dish",
            },
        ],
        "figure": None,
    },
    {
        "id": "c3-04-e13",
        "band": "easier",
        "text": "Crystals lifted out of a dish are still wet with solution. Why are they pressed between sheets of filter paper before they are weighed?",
        "options": [
            {
             "text": "Because the liquid on them would dissolve the crystals again while they sat on the balance",
             "correct": False,
             "why": "That liquid is saturated already and can dissolve no more. The trouble is that it has a mass of its own",
            },
            {
             "text": "Because filter paper draws the colour out of the crystals and leaves them purer than before",
             "correct": False,
             "why": "Nothing is taken out of the crystals. The paper takes up the liquid clinging to the outside of them",
            },
            {
             "text": "Because the liquid still on them would be weighed as though it were crystal",
             "correct": True,
            },
            {
             "text": "Because wet crystals stick together and cannot be counted",
             "correct": False,
             "why": "Crystals are weighed rather than counted. It is the mass of the liquid that spoils the reading",
            },
        ],
        "figure": None,
    },
    {
        "id": "c3-04-e14",
        "band": "easier",
        "text": "A dish of copper sulfate solution stands in a warm room. What happens to the concentration of the solution as the water leaves it?",
        "options": [
            {
             "text": "It falls, because some of the solute is carried away with the water that leaves",
             "correct": False,
             "why": "The solute cannot leave. Less water around the same solute means a stronger solution, not a weaker one",
            },
            {
             "text": "It rises, because the same solute is left in less and less water",
             "correct": True,
            },
            {
             "text": "It stays the same, because the solute and the solvent leave the dish together",
             "correct": False,
             "why": "Only the solvent evaporates here. The solute stays in the dish from the first minute to the last",
            },
            {
             "text": "It stays the same, then falls to nothing once crystals appear",
             "correct": False,
             "why": "It rises steadily from the start. Crystals appear because it has risen as far as it can go",
            },
        ],
        "figure": None,
    },
    {
        "id": "c3-04-e15",
        "band": "easier",
        "text": "Two dishes hold the same mass of dissolved salt: one in "
                "20 cm³ of water, the other in 60 cm³. Both are left until "
                "they are dry. Which leaves more salt?",
        "options": [
            {"text": "The 60 cm³ dish, because more water carries more salt "
                     "out of solution as it goes",
             "correct": False,
             "why": "Water carries no salt anywhere. How much of it there "
                    "was changes only how long the drying takes"},
            {"text": "The 20 cm³ dish, because a stronger solution holds on "
                     "to its solute more tightly",
             "correct": False,
             "why": "Nothing is held on to. Both dishes started with the "
                    "same mass of salt and both end with that mass"},
            {"text": "The 20 cm³ dish, because it dries first and so loses "
                     "less salt into the air",
             "correct": False,
             "why": "No salt is lost into the air from either dish. Drying "
                    "first saves time and nothing else"},
            {"text": "Neither — the same mass of salt was dissolved, so the "
                     "same mass is left",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c3-04-e16",
        "band": "easier",
        "text": "Salt crystals come out as cubes and alum crystals come out with eight faces. What decides a crystal's shape?",
        "options": [
            {
             "text": "The substance it is made of",
             "correct": True,
            },
            {
             "text": "How fast the solvent was removed",
             "correct": False,
             "why": "Rate decides the size. Salt gives cubes whether the dish took four minutes or six days",
            },
            {
             "text": "The shape of the dish it grew in",
             "correct": False,
             "why": "Crystals take no shape from their container. A cube grown in a round basin is still a cube",
            },
            {
             "text": "The temperature of the room",
             "correct": False,
             "why": "Temperature changes how fast the solvent leaves, and so the size. The faces come from the substance",
            },
        ],
        "figure": None,
    },
    {
        "id": "c3-04-e17",
        "band": "easier",
        "text": "All of the solid left by an evaporation is stirred back into the same volume of water it came from, with none of it lost on the way. What happens?",
        "options": [
            {
             "text": "Nothing — once a substance has crystallised it cannot be dissolved a second time",
             "correct": False,
             "why": "Crystallising changes nothing about the substance, so it dissolves exactly as it did the first time",
            },
            {
             "text": "They react with the water and a new substance is made",
             "correct": False,
             "why": "No reaction takes place. Dissolving and crystallising are changes of place, not changes of substance",
            },
            {
             "text": "They dissolve again and the solution is back as it was",
             "correct": True,
            },
            {
             "text": "They dissolve, but the solution is weaker than the one they were taken out of",
             "correct": False,
             "why": "The same solute and the same water give the same solution. Nothing was lost along the way",
            },
        ],
        "figure": None,
    },
    {
        "id": "c3-04-e18",
        "band": "easier",
        "text": "A 240 g sample of sugar solution is evaporated to dryness "
                "and leaves 18 g of sugar in the dish. What mass of water "
                "went into the air?",
        "options": [
            {"text": "258 g", "correct": False,
             "why": "That adds the two masses. The water is what is left "
                    "when the sugar is taken off the total"},
            {"text": "222 g", "correct": True},
            {"text": "18 g", "correct": False,
             "why": "18 g is the sugar now in the dish. The water is the "
                    "rest of the 240 g the sample started as"},
            {"text": "240 g", "correct": False,
             "why": "Not all of the sample was water — 18 g of it was "
                    "sugar, and that is still sitting in the dish"},
        ],
        "figure": None,
    },
    {
        "id": "c3-04-e19",
        "band": "easier",
        "text": "A solution contains 20 g of alum in every 1 dm³. A 500 cm³ "
                "sample of it is evaporated to dryness. What mass of alum is "
                "left?",
        "options": [
            {"text": "20 g", "correct": False,
             "why": "20 g is the mass in a full dm³, and this sample is half "
                    "of one"},
            {"text": "40 g", "correct": False,
             "why": "That doubles the concentration instead of halving the "
                    "volume. 500 cm³ is half of 1 dm³"},
            {"text": "5 g", "correct": False,
             "why": "That takes a quarter of the mass in 1 dm³. 500 cm³ is "
                    "a half of it, not a quarter"},
            {"text": "10 g", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c3-04-e20",
        "band": "easier",
        "text": "A solution is made by dissolving 28 g of copper sulfate "
                "in 100 g of water. It is then evaporated to dryness. What "
                "mass of copper sulfate is recovered?",
        "options": [
            {"text": "28 g", "correct": True},
            {"text": "0 g", "correct": False,
             "why": "Nothing dissolved leaves with the water. All of the "
                    "solid is still in the dish at the end"},
            {"text": "128 g", "correct": False,
             "why": "That adds the water's mass to the solid's. The water "
                    "has gone into the air and is not in the dish"},
            {"text": "14 g", "correct": False,
             "why": "Half of the solid does not disappear on the way. Every "
                    "gram that was dissolved is left behind"},
        ],
        "figure": None,
    },
    {
        "id": "c3-04-e21",
        "band": "easier",
        "text": "A student expected 8.0 g of crystals from her solution and "
                "recovered 7.2 g of them. What percentage of the expected "
                "mass did she recover?",
        "options": [
            {"text": "80%", "correct": False,
             "why": "80% of 8.0 g is 6.4 g, and she has more than that in "
                    "the dish"},
            {"text": "72%", "correct": False,
             "why": "That reads the recovered mass straight off as a "
                    "percentage instead of comparing it with 8.0 g"},
            {"text": "90%", "correct": True},
            {"text": "111%", "correct": False,
             "why": "That divides the expected mass by the recovered one. "
                    "A recovery cannot be more than all of it"},
        ],
        "figure": None,
    },
    {
        "id": "c3-04-e22",
        "band": "easier",
        "text": "A kidney stone is a solid crystal that grows when the fluid "
                "in the kidney becomes too concentrated. Which everyday "
                "process is that most like?",
        "options": [
            {"text": "Sand settling out on the bottom of a beaker of water",
             "correct": False,
             "why": "The sand never dissolved, so nothing came out of "
                    "solution. A stone grows from material that was "
                    "dissolved"},
            {"text": "Crystals appearing in a dish as its solution becomes "
                     "too concentrated",
             "correct": True},
            {"text": "Ice forming on the inside of a window on a cold night",
             "correct": False,
             "why": "That is a liquid freezing, with no solute in the story "
                    "at all. A stone is a solute leaving a solution"},
            {"text": "A filter paper catching grit out of a jug of muddy "
                     "water",
             "correct": False,
             "why": "Filtering takes out what never dissolved. A stone is "
                    "built out of material that had dissolved"},
        ],
        "figure": None,
    },
    {
        "id": "c3-04-e23",
        "band": "easier",
        "text": "Glasses washed in hard tap water and left to dry in the air "
                "are marked with faint white patches. What are those "
                "patches?",
        "options": [
            {"text": "Fine scratches left on the glass by the stiff bristles "
                     "of the washing-up brush",
             "correct": False,
             "why": "They wipe off with a cloth, so nothing has been "
                    "scratched. They are solid left behind by the water"},
            {"text": "Soap that was not rinsed off the glass properly",
             "correct": False,
             "why": "The same glasses rinsed in distilled water dry clean. "
                    "What differs is what the water had dissolved in it"},
            {"text": "Water that has soaked into the surface of the glass",
             "correct": False,
             "why": "Glass takes up no water at all. The water has gone into "
                    "the air and left what was dissolved in it"},
            {"text": "Solids that were dissolved in the water, left behind "
                     "as it evaporated",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c3-04-e24",
        "band": "easier",
        "text": "Lithium is won by pumping underground brine into wide "
                "shallow ponds and leaving it in the sun for months. What "
                "leaves those ponds?",
        "options": [
            {"text": "The water, which goes into the air as a gas",
             "correct": True},
            {"text": "The lithium, which is carried off in the vapour",
             "correct": False,
             "why": "A dissolved solid cannot evaporate at these "
                    "temperatures. The lithium is what stays"},
            {"text": "The sunlight, which is taken up by the brine",
             "correct": False,
             "why": "Sunlight is what warms the pond rather than something "
                    "removed from it"},
            {"text": "The insoluble grit, which floats off the top",
             "correct": False,
             "why": "Grit would be filtered out, and that is not the job "
                    "these ponds do"},
        ],
        "figure": None,
    },
    {
        "id": "c3-04-e25",
        "band": "easier",
        "text": "Boiling a solution hard to dryness leaves a crust that has "
                "to be scraped off the dish. Why is a crust harder to "
                "collect than a few large crystals?",
        "options": [
            {"text": "Because a crust is a different substance from the "
                     "crystals a slow run gives",
             "correct": False,
             "why": "It is the same substance. Only the form it has taken, "
                    "and so how it sits in the dish, is different"},
            {"text": "Because it is spread across the dish as one thin "
                     "layer rather than sitting in it as pieces",
             "correct": True},
            {"text": "Because a crust of solid weighs a great deal more than "
                     "the loose crystals that a slower run gives",
             "correct": False,
             "why": "The mass recovered is the same either way. It is only "
                    "the form of it that makes a crust awkward"},
            {"text": "Because a crust is still wet and cannot be lifted "
                     "until it has dried out",
             "correct": False,
             "why": "The dish was taken to dryness, so there is nothing left "
                    "to dry. The trouble is that it is stuck down"},
        ],
        "figure": None,
    },
    {
        "id": "c3-04-e26",
        "band": "easier",
        "text": "What does it mean to evaporate a solution to dryness?",
        "options": [
            {
             "text": "To heat it until the solution is half the volume it started as",
             "correct": False,
             "why": "That is concentrating a solution. Dryness means no liquid at all is left in the dish",
            },
            {
             "text": "To heat it until every trace of the solvent has gone and only solid is left",
             "correct": True,
            },
            {
             "text": "To heat it until the very first crystals appear around the rim of the evaporating dish",
             "correct": False,
             "why": "That is a stage on the way, with liquid still in the dish. Dryness means no liquid at all is left",
            },
            {
             "text": "To dry the recovered crystals between two sheets of filter paper",
             "correct": False,
             "why": "That is drying the product afterwards. Evaporating to dryness describes what happens in the dish",
            },
        ],
        "figure": None,
    },
    {
        "id": "c3-04-e27",
        "band": "easier",
        "text": "A pale blue copper sulfate solution is left in an open dish "
                "in a warm room. What happens to its colour over the next "
                "few days?",
        "options": [
            {"text": "It fades, because the blue escapes with the water "
                     "vapour",
             "correct": False,
             "why": "The vapour is colourless water. The blue substance "
                    "stays put and is packed into less and less of it"},
            {"text": "It turns white, because warmth takes the blue out of "
                     "copper sulfate",
             "correct": False,
             "why": "That needs dry crystals heated hard. A dish standing in "
                    "a warm room does nothing of the kind"},
            {"text": "It deepens, because the same blue substance is left in "
                     "less water",
             "correct": True},
            {"text": "It stays the same until the first crystals appear in "
                     "the dish",
             "correct": False,
             "why": "It deepens steadily as the solution concentrates, long "
                    "before any crystal is there to see"},
        ],
        "figure": None,
    },
    {
        "id": "c3-04-e28",
        "band": "easier",
        "text": "An evaporating basin just lifted off a tripod looks exactly "
                "like a cold one. What should be done before it is picked "
                "up?",
        "options": [
            {"text": "Leave it to cool on the bench, or lift it with tongs",
             "correct": True},
            {"text": "Pick it up quickly, since a brief contact cannot burn",
             "correct": False,
             "why": "Hot ceramic burns on contact, and a basin straight off "
                    "a tripod is hundreds of degrees"},
            {"text": "Run cold water into it to bring the heat out of it",
             "correct": False,
             "why": "Cold water on hot ceramic can crack it, and it would "
                    "dissolve the crystals you have just made"},
            {"text": "Blow across it for a few seconds to take the heat off",
             "correct": False,
             "why": "Blowing shifts almost no heat, and it can scatter a "
                    "light crust of dry crystals"},
        ],
        "figure": None,
    },
    {
        "id": "c3-04-e29",
        "band": "easier",
        "text": "Why does a school practical use a water bath to evaporate a "
                "solution rather than leaving the dish on a windowsill?",
        "options": [
            {"text": "Because a windowsill would give a smaller mass of "
                     "solid at the end",
             "correct": False,
             "why": "The mass recovered is the same either way. What a "
                    "windowsill costs is time and nothing else"},
            {"text": "Because a windowsill run takes days, and a lesson does "
                     "not",
             "correct": True},
            {"text": "Because crystals cannot form at all below about 50 °C",
             "correct": False,
             "why": "The finest crystals of all are grown cold and slowly. "
                    "Warmth is not what crystals need"},
            {"text": "Because a windowsill run leaves the solvent behind in "
                     "the dish",
             "correct": False,
             "why": "The solvent goes into the air either way. Only the time "
                    "taken and the crystals are different"},
        ],
        "figure": None,
    },
    {
        "id": "c3-04-e30",
        "band": "easier",
        "text": "A white crust slowly builds up on the outside of a clay "
                "plant pot that is watered with tap water. How does it get "
                "there?",
        "options": [
            {"text": "The clay reacts with the water that passes through it "
                     "and makes a new white solid on the surface",
             "correct": False,
             "why": "No reaction is needed. The white solid was dissolved in "
                    "the water before it ever reached the pot"},
            {"text": "Water soaks through the clay and evaporates from the "
                     "surface, leaving what was dissolved",
             "correct": True},
            {"text": "Dust out of the air settles on the damp surface and is "
                     "held there",
             "correct": False,
             "why": "Dust would brush off and would not build up where the "
                    "water comes through. This crust came out of the water"},
            {"text": "The clay itself slowly dissolves and forms again on "
                     "the outside of the pot",
             "correct": False,
             "why": "The pot is not losing any material. What is deposited "
                    "arrived dissolved in the water"},
        ],
        "figure": None,
    },
    {
        "id": "c3-04-e31",
        "band": "easier",
        "text": "Two identical dishes of solution stand in the same warm room, and one of them is under a fan. Which dries first?",
        "options": [
            {
             "text": "The one away from the fan",
             "correct": False,
             "why": "The fan moves room air about rather than cooling it, and moving air is what lets more vapour leave",
            },
            {
             "text": "Both together, because the room is at one temperature",
             "correct": False,
             "why": "Temperature is not the only thing that matters. Moving air carries the vapour away from the surface",
            },
            {
             "text": "The one under the fan",
             "correct": True,
            },
            {
             "text": "Neither, because a fan blows the vapour back down into the dish",
             "correct": False,
             "why": "A fan cannot push vapour back into a liquid. It sweeps it away, which speeds the drying up",
            },
        ],
        "figure": None,
    },
    {
        "id": "c3-04-e32",
        "band": "easier",
        "text": "At what point during an evaporation do the first crystals "
                "appear?",
        "options": [
            {"text": "When the solution becomes saturated",
             "correct": True},
            {"text": "As soon as the dish is put over the heat",
             "correct": False,
             "why": "Nothing comes out of solution until enough solvent has "
                    "gone for the solution to be full"},
            {"text": "Only once the last of the solvent has gone",
             "correct": False,
             "why": "Crystals appear while there is still liquid in the "
                    "dish, and they grow as the rest of it goes"},
            {"text": "Once the dish has cooled to room temperature",
             "correct": False,
             "why": "Crystals appear as the solvent leaves, whether the dish "
                    "is still hot or has gone cold"},
        ],
        "figure": None,
    },

    # ── standard · MRB-338 expansion ────────────────────────────────────
    {
        "id": "c3-04-s08",
        "band": "standard",
        "text": "Washing hung outside on a cold, dry, breezy day is bone dry "
                "by the evening, and the temperature never rose above 4 °C. "
                "Explain how the water left it.",
        "options": [
            {"text": "The cold froze the water in the cloth, and the ice "
                     "broke off it through the afternoon",
             "correct": False,
             "why": "It was above freezing all day, and frozen washing is "
                    "still wet once it thaws"},
            {"text": "Water particles left the surface of the cloth and "
                     "joined the air, which happens at any temperature",
             "correct": True},
            {"text": "The wind pushed the water down through the fibres and "
                     "out of the bottom edge of the cloth",
             "correct": False,
             "why": "Wind carries vapour away from a wet surface. It does "
                    "not squeeze liquid through cloth"},
            {"text": "The cold and the wind together destroyed the water "
                     "that was in the cloth",
             "correct": False,
             "why": "Nothing destroys water. It is in the air as a gas, "
                    "spread out too thinly to see"},
        ],
        "figure": None,
    },
    {
        "id": "c3-04-s09",
        "band": "standard",
        "text": "A solution holds a substance that chars and turns brown "
                "above about 120 °C. Explain why a water bath is the right "
                "way to take the solvent off it.",
        "options": [
            {"text": "Because a water bath heats the dish faster than a "
                     "flame does, so the substance spends less time hot",
             "correct": False,
             "why": "A water bath is much the slower of the two. What "
                    "protects the substance is the temperature it cannot "
                    "pass"},
            {"text": "Because a water bath takes the solvent off without any "
                     "of it going into the air",
             "correct": False,
             "why": "The solvent goes into the air from a water bath exactly "
                    "as it does from a dish over a flame"},
            {"text": "Because a water bath makes the crystals grow larger "
                     "than a Bunsen flame can",
             "correct": False,
             "why": "It does give better crystals than boiling, but that is "
                    "not what saves a substance that chars"},
            {"text": "Because a pan of boiling water cannot pass 100 °C, so "
                     "the dish never reaches 120 °C",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c3-04-s10",
        "band": "standard",
        "text": "A dish of solution heated over a Bunsen spits most "
                "violently in the last moments before it goes dry. Explain "
                "why the spitting gets worse at the end.",
        "options": [
            {"text": "The last of the liquid is a thin, very concentrated "
                     "layer, and bubbles forming under it throw it out",
             "correct": True},
            {"text": "The crystals that have already formed burst apart as "
                     "the heat reaches them through the base of the dish",
             "correct": False,
             "why": "Dry crystals do not burst. What leaves the dish is hot "
                    "liquid, thrown out by bubbles underneath it"},
            {"text": "The basin starts to give off gas of its own once there "
                     "is no liquid left to keep it cool",
             "correct": False,
             "why": "An evaporating basin gives off nothing, and the worst "
                    "spitting happens while liquid is still in it"},
            {"text": "The solvent becomes flammable as the last of it is "
                     "used up, so it flares in the flame",
             "correct": False,
             "why": "Water vapour does not burn. The hazard is hot liquid "
                    "being thrown out, not a flare"},
        ],
        "figure": None,
    },
    {
        "id": "c3-04-s11",
        "band": "standard",
        "text": "Ethanol vapour catches fire easily and is heavier than air. "
                "Explain why a small Bunsen flame under a dish of ethanol "
                "solution is still dangerous.",
        "options": [
            {"text": "The ethanol would boil over the side of the dish and "
                     "put the flame out, leaving unburnt gas in the room",
             "correct": False,
             "why": "Gas that never lights is not the danger here. Ethanol "
                    "vapour that reaches a flame catches fire"},
            {"text": "A small flame cannot warm the dish enough, so the "
                     "solution would never evaporate at all",
             "correct": False,
             "why": "A small flame evaporates ethanol perfectly well. The "
                    "trouble is where the vapour can get to"},
            {"text": "Vapour coming off the dish sinks towards the bench and "
                     "reaches the flame, which lights it",
             "correct": True},
            {"text": "The solid left in the dish would catch fire once all "
                     "of the ethanol had gone",
             "correct": False,
             "why": "It is the solvent's vapour that burns, and it is "
                    "dangerous long before the dish is anywhere near dry"},
        ],
        "figure": None,
    },
    {
        "id": "c3-04-s12",
        "band": "standard",
        "text": "Two students start from identical solutions each holding "
                "6.0 g of dissolved salt. One records 6.0 g of crystals, the "
                "other 5.1 g. Suggest what happened in the second run.",
        "options": [
            {"text": "Some of the salt evaporated along with the water while "
                     "the dish was being heated",
             "correct": False,
             "why": "Salt does not evaporate at these temperatures. Whatever "
                    "is missing is still somewhere in the apparatus"},
            {"text": "Some of the salt was left in the dish, or lost on the "
                     "way to the balance",
             "correct": True},
            {"text": "The second solution must have held less salt than it "
                     "was labelled as holding",
             "correct": False,
             "why": "Both solutions are stated to hold 6.0 g. The difference "
                    "was made in the collecting, not the making"},
            {"text": "The second student heated the dish for longer and "
                     "drove some of the salt off",
             "correct": False,
             "why": "Extra heating drives off nothing but water. Once the "
                    "dish is dry, more heat removes no salt"},
        ],
        "figure": None,
    },
    {
        "id": "c3-04-s13",
        "band": "standard",
        "text": "Crystals are weighed, warmed gently, cooled and weighed "
                "again, and the mass has fallen. Warmed and weighed a third "
                "time, the mass holds. Explain what that shows.",
        "options": [
            {"text": "The crystals are breaking down, and will lose a little "
                     "more mass every time they are warmed",
             "correct": False,
             "why": "The mass stopped falling at the third weighing, which "
                    "is exactly what breaking down would not do"},
            {"text": "The balance drifts between readings, so the first mass "
                     "was simply misread",
             "correct": False,
             "why": "A drifting balance would not fall once and then hold. "
                    "Something real left the dish the first time"},
            {"text": "Some crystals were spilled between the first weighing "
                     "and the second one",
             "correct": False,
             "why": "A spill would lose mass again on the third weighing. "
                    "The steady mass says the crystals are dry"},
            {"text": "The first mass included solvent still on the crystals; "
                     "once the mass holds they are dry",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c3-04-s14",
        "band": "standard",
        "text": "Nothing at all appears in an evaporating dish for a long "
                "time, and then crystals begin to form quite suddenly. "
                "Explain why they do not start straight away.",
        "options": [
            {"text": "The solution has to lose enough solvent to become "
                     "saturated, and only then can solute come out",
             "correct": True},
            {"text": "The dish has to reach a set temperature before any "
                     "crystal is able to start growing in it",
             "correct": False,
             "why": "Crystals form on a cold windowsill as readily as over a "
                    "flame. It is losing solvent that starts them"},
            {"text": "The solute has to sink to the bottom first, and can "
                     "only crystallise once it has gathered there",
             "correct": False,
             "why": "A solution is even throughout, and nothing gathers on "
                    "the bottom before the crystals appear"},
            {"text": "Some of the solute has to evaporate before the rest of "
                     "it is able to crystallise",
             "correct": False,
             "why": "None of the solute evaporates. It is the solvent "
                    "leaving that brings the crystals on"},
        ],
        "figure": None,
    },
    {
        "id": "c3-04-s15",
        "band": "standard",
        "text": "A technician can dissolve 10 g of alum in 50 cm³ of hot "
                "water or in 200 cm³. She needs it back as dry crystals by "
                "the end of the day. Which should she choose, and why?",
        "options": [
            {"text": "The 200 cm³, because a weaker solution gives its "
                     "solute up more readily than a strong one",
             "correct": False,
             "why": "A weaker solution simply has more water to lose. The "
                    "mass recovered is the same from either"},
            {"text": "The 50 cm³, because a stronger solution yields a "
                     "greater mass of alum at the end of the run",
             "correct": False,
             "why": "Both hold 10 g of alum and both give 10 g back. What "
                    "the smaller volume saves her is time"},
            {"text": "The 50 cm³, because there is far less water to remove "
                     "and the run is much shorter",
             "correct": True},
            {"text": "Either one, because the volume of water changes "
                     "nothing about how the run goes",
             "correct": False,
             "why": "The volume sets how long it takes — 200 cm³ is four "
                    "times as much water to drive off"},
        ],
        "figure": None,
    },
    {
        "id": "c3-04-s16",
        "band": "standard",
        "text": "Two dishes of the same alum solution are dried: one over a "
                "water bath in half an hour, one on a shelf over a "
                "fortnight. Compare the crystals in the two dishes.",
        "options": [
            {"text": "The shelf gives eight-sided crystals and the water "
                     "bath gives cubes instead",
             "correct": False,
             "why": "Shape comes from the substance, so both are "
                    "eight-sided. Size is what the method changes"},
            {"text": "Both give eight-sided alum crystals, and the shelf "
                     "gives much larger ones",
             "correct": True},
            {"text": "Both give crystals of the same size, and the shelf "
                     "ones are the more regular of the two",
             "correct": False,
             "why": "Slow growth gives larger crystals, not merely tidier "
                    "ones of the same size"},
            {"text": "The water bath gives the larger crystals, because "
                     "warmth helps a crystal to grow",
             "correct": False,
             "why": "Warmth drives the solvent off sooner, so thousands "
                    "start at once and none of them gets big"},
        ],
        "figure": None,
    },
    {
        "id": "c3-04-s17",
        "band": "standard",
        "text": "A student says crystallising must be a chemical reaction, because a solid appears where there was only a clear liquid before. Explain why she is wrong.",
        "options": [
            {
             "text": "A chemical reaction always gives off a gas, and no gas is given off from the dish",
             "correct": False,
             "why": "Plenty of reactions give off no gas at all. What settles it is that no new substance appears",
            },
            {
             "text": "Chemical reactions only happen when two different solutions are mixed together, and only one is used here",
             "correct": False,
             "why": "A single substance heated on its own can react. The test is whether a new substance is made",
            },
            {
             "text": "The solute melted into the water when it dissolved, and has simply set solid again",
             "correct": False,
             "why": "Dissolving is not melting — the solute spread through the water rather than turning to liquid. What settles it is that no new substance appears",
            },
            {
             "text": "No new substance is made — the solute was dissolved there all along and has come back out",
             "correct": True,
            },
        ],
        "figure": None,
    },
    {
        "id": "c3-04-s18",
        "band": "standard",
        "text": "A 250 g sample of a solution leaves 15 g of solid when it "
                "is evaporated to dryness. What mass of solid would 1000 g "
                "of the same solution leave?",
        "options": [
            {"text": "60 g", "correct": True},
            {"text": "15 g", "correct": False,
             "why": "15 g is what the smaller sample gave. Four times as "
                    "much solution carries four times the solid"},
            {"text": "30 g", "correct": False,
             "why": "That doubles the mass, but 1000 g is four times 250 g "
                    "rather than twice it"},
            {"text": "75 g", "correct": False,
             "why": "That multiplies by five. 1000 g is four times 250 g, "
                    "so the solid is four times 15 g"},
        ],
        "figure": None,
    },
    {
        "id": "c3-04-s19",
        "band": "standard",
        "text": "A solution contains 45 g of potassium nitrate in every "
                "1 dm³. What volume of it must be evaporated to dryness to "
                "recover 9.0 g of potassium nitrate?",
        "options": [
            {"text": "450 cm³", "correct": False,
             "why": "That volume holds about 20 g. Nine grams is a fifth of "
                    "45 g, so a fifth of a dm³ is needed"},
            {"text": "5 cm³", "correct": False,
             "why": "That divides 45 by 9 and calls the answer cubic "
                    "centimetres. The volume wanted is a fifth of 1000 cm³"},
            {"text": "200 cm³", "correct": True},
            {"text": "500 cm³", "correct": False,
             "why": "Half a dm³ holds 22.5 g, which is two and a half times "
                    "the mass asked for"},
        ],
        "figure": None,
    },
    {
        "id": "c3-04-s20",
        "band": "standard",
        "text": "100 g of water holds at most 32 g of copper sulfate at 50 °C and 20 g at 20 °C. A solution saturated at 50 °C in 100 g of water cools to 20 °C. What mass crystallises out?",
        "options": [
            {
             "text": "20 g",
             "correct": False,
             "why": "20 g is what the cooler water can still hold. What comes out is the difference between the two figures",
            },
            {
             "text": "12 g",
             "correct": True,
            },
            {
             "text": "32 g",
             "correct": False,
             "why": "32 g is all of the dissolved solid. Only the part the cooler water can no longer hold comes out",
            },
            {
             "text": "52 g",
             "correct": False,
             "why": "That adds the two figures together. The mass that crystallises is the difference between them",
            },
        ],
        "figure": None,
    },
    {
        "id": "c3-04-s21",
        "band": "standard",
        "text": "A solution held 12.5 g of dissolved solid and 11.0 g of dry "
                "crystals was recovered. Give the percentage recovered, and "
                "say where the rest most likely went.",
        "options": [
            {"text": "88%, and the missing solid went into the air with the "
                     "solvent as it evaporated",
             "correct": False,
             "why": "The percentage is right and the reason is not. A "
                    "dissolved solid cannot evaporate at these temperatures"},
            {"text": "114%, and the extra mass is solvent still held inside "
                     "the crystals that were weighed",
             "correct": False,
             "why": "That divides the wrong way round. Less was recovered "
                    "than was dissolved, so it cannot exceed 100%"},
            {"text": "1.5%, and that solid was never dissolved in the "
                     "solution to begin with",
             "correct": False,
             "why": "1.5 g is the mass missing rather than the percentage "
                    "recovered, and all 12.5 g was dissolved"},
            {"text": "88%, and the missing solid is most likely still on the "
                     "dish or the stirring rod",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c3-04-s22",
        "band": "standard",
        "text": "People prone to kidney stones are advised to drink more "
                "water through the day. Explain, in terms of solutions, why "
                "that advice helps.",
        "options": [
            {"text": "More water keeps the dissolved substances well below "
                     "saturation, so no solid comes out",
             "correct": True},
            {"text": "Water dissolves any stone that has already formed, so "
                     "it never has the chance to grow larger",
             "correct": False,
             "why": "The advice is about stopping one forming. Extra solvent "
                    "keeps the solution dilute rather than undoing a solid"},
            {"text": "Water reacts with the dissolved substances and turns "
                     "them into something that cannot crystallise",
             "correct": False,
             "why": "No reaction is involved anywhere. Water is the solvent, "
                    "and more of it makes a weaker solution"},
            {"text": "Water lowers the temperature of the fluid, and solids "
                     "crystallise less readily when they are cool",
             "correct": False,
             "why": "Cooling a solution makes crystals more likely, not "
                    "less. It is the extra solvent that does the work"},
        ],
        "figure": None,
    },
    {
        "id": "c3-04-s23",
        "band": "standard",
        "text": "A cafe's glasses dry without a mark after a final rinse in "
                "distilled water, but dry with white patches after a rinse "
                "in tap water. Explain the difference.",
        "options": [
            {"text": "Distilled water evaporates far faster, so it is gone "
                     "from the glass before it can leave any mark on it",
             "correct": False,
             "why": "How fast it dries is not the point. It leaves nothing "
                    "because there is nothing dissolved in it"},
            {"text": "Distilled water is softer, so it does not scratch the "
                     "surface of the glass as it runs off",
             "correct": False,
             "why": "Water of any kind scratches nothing. The patches are "
                    "dissolved solid left behind on the glass"},
            {"text": "Tap water has solids dissolved in it and leaves them "
                     "behind; distilled water has none to leave",
             "correct": True},
            {"text": "Tap water comes out colder, so the patches are frost "
                     "left on the glass as it dries",
             "correct": False,
             "why": "The patches survive in a warm room and wipe off as a "
                    "powder, so they are solid rather than ice"},
        ],
        "figure": None,
    },
    {
        "id": "c3-04-s24",
        "band": "standard",
        "text": "Brine ponds for winning lithium are built in high deserts where the sun is strong and it almost never rains. Explain why those conditions suit the process.",
        "options": [
            {
             "text": "The thin mountain air holds far more dissolved lithium than air at sea level is able to",
             "correct": False,
             "why": "Air holds no lithium at all. What the site gives is fast evaporation and no rain to undo it",
            },
            {
             "text": "Strong sun drives the water off quickly, and no rain means none is added back",
             "correct": True,
            },
            {
             "text": "Cold desert nights freeze the brine, and freezing is what forces the lithium out of solution",
             "correct": False,
             "why": "The ponds work by losing water to the air rather than by freezing, and rain would simply refill them",
            },
            {
             "text": "The desert sand filters grit out of the brine as it soaks away",
             "correct": False,
             "why": "The ponds are lined so that nothing soaks away. Their job is to lose water, not to filter it",
            },
        ],
        "figure": None,
    },
    {
        "id": "c3-04-s25",
        "band": "standard",
        "text": "A crust of dry solid is stuck to the inside of an "
                "evaporating basin and all of it is needed for weighing. "
                "Suggest how to get it out without losing any.",
        "options": [
            {"text": "Rinse the basin out with water and pour the rinsings "
                     "away down the sink",
             "correct": False,
             "why": "The solid dissolves in the rinse water and goes down "
                    "the drain with it"},
            {"text": "Heat the basin again until the crust loosens and drops "
                     "out of it by itself",
             "correct": False,
             "why": "More heating drives off nothing and can spoil the "
                    "solid. The crust stays exactly where it is"},
            {"text": "Tap the basin sharply on the bench so that the crust "
                     "breaks away from the surface",
             "correct": False,
             "why": "That scatters solid across the bench and risks cracking "
                    "the basin as well"},
            {"text": "Scrape it out with a spatula over a weighed piece of "
                     "paper, so nothing is lost",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c3-04-s26",
        "band": "standard",
        "text": "One instruction says to evaporate a sample to dryness and "
                "another says to crystallise it. Explain what a chemist ends "
                "up with in each case.",
        "options": [
            {"text": "Dryness gives everything dissolved as a powder or "
                     "crust; crystallising gives well-formed crystals of it",
             "correct": True},
            {"text": "Dryness gives the solvent back, and crystallising "
                     "gives the solute back instead",
             "correct": False,
             "why": "Neither gives the solvent back — it is lost to the air "
                    "both times. Both keep the solute"},
            {"text": "Dryness gives a larger mass of solid than "
                     "crystallising the same solution does",
             "correct": False,
             "why": "The mass is the same either way. What differs is the "
                    "form the solid ends up in"},
            {"text": "Crystallising leaves the solid still dissolved in the "
                     "liquid, and only evaporating to dryness takes it out",
             "correct": False,
             "why": "Crystallising IS the solute coming out of solution. "
                    "Both finish with solid in the dish"},
        ],
        "figure": None,
    },
    {
        "id": "c3-04-s27",
        "band": "standard",
        "text": "A dye solution standing in a shallow tray is noticeably "
                "darker by the end of an afternoon, and nothing was added to "
                "it. Explain the change.",
        "options": [
            {"text": "The dye reacted with the air above the tray and a "
                     "darker substance was formed in it",
             "correct": False,
             "why": "No reaction is needed. The dye is unchanged and is "
                    "simply packed into less water than before"},
            {"text": "The dye particles settled towards the bottom, which "
                     "makes the colour look stronger from above",
             "correct": False,
             "why": "A solution stays even throughout. It looks darker "
                    "because there is genuinely less water in it"},
            {"text": "Water evaporated from the tray, so the same dye is "
                     "spread through less liquid",
             "correct": True},
            {"text": "The light in the room changed through the afternoon "
                     "and made the same colour look darker",
             "correct": False,
             "why": "The change is in the tray rather than the lighting — "
                    "the solution really has become stronger"},
        ],
        "figure": None,
    },
    {
        "id": "c3-04-s28",
        "band": "standard",
        "text": "A dish of crystals is taken off a water bath and put "
                "straight onto a balance, and the reading drifts downwards "
                "for several minutes. Explain why, and say what to do.",
        "options": [
            {"text": "Dry crystals lose mass steadily in air however they "
                     "were made, so the first reading should be taken",
             "correct": False,
             "why": "Dry crystals at room temperature hold their mass. This "
                    "dish is still warm, which is why it is still losing"},
            {"text": "The dish is still warm and the last of the solvent is "
                     "still leaving; it should be cooled first",
             "correct": True},
            {"text": "The balance was not zeroed before the dish was put on "
                     "it, so the reading should be zeroed and retaken",
             "correct": False,
             "why": "A zero error gives a reading that is wrong and steady, "
                    "not one that drifts downwards"},
            {"text": "The crystals are dissolving into the air above the "
                     "dish, so a lid should be put on it",
             "correct": False,
             "why": "Solids do not dissolve into air. What is still leaving "
                    "is solvent, driven off by the dish's warmth"},
        ],
        "figure": None,
    },
    {
        "id": "c3-04-s29",
        "band": "standard",
        "text": "A class has one 50-minute lesson and must finish it with "
                "copper sulfate crystals big enough to see the shape of. "
                "Which method should they use, and why?",
        "options": [
            {"text": "A roaring Bunsen, because only strong heat gives "
                     "crystals with clear flat faces",
             "correct": False,
             "why": "Strong heat starts thousands of crystals at once and "
                    "gives a fine crust with no shape to see"},
            {"text": "A windowsill, because that is the only one of the "
                     "three methods that gives crystals at all",
             "correct": False,
             "why": "All three give crystals. A windowsill needs days, and "
                    "the class has under an hour"},
            {"text": "A Bunsen taken to dryness, because that recovers the "
                     "greatest mass of copper sulfate",
             "correct": False,
             "why": "The mass is the same whichever method is used, and "
                    "these crystals would be far too small to look at"},
            {"text": "A water bath, because it is slow enough for clear "
                     "crystals and quick enough for the lesson",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c3-04-s30",
        "band": "standard",
        "text": "A damp brick wall develops a white powdery bloom on its "
                "outside face, always worst where the wall dries fastest. "
                "Explain how the bloom gets there.",
        "options": [
            {"text": "Water carrying dissolved solids moves through the "
                     "brick and evaporates at the face, leaving them there",
             "correct": True},
            {"text": "The bricks are slowly being worn away by the weather, "
                     "and the bloom is the fine dust that it leaves behind",
             "correct": False,
             "why": "The wall loses no material of its own. The bloom "
                    "arrived dissolved in the water"},
            {"text": "Mould grows on the damp brick and dries out into a "
                     "white powder on the surface",
             "correct": False,
             "why": "The bloom is a solid that was dissolved in the water "
                    "rather than anything living"},
            {"text": "Rain blows dust onto the wall and it sticks fast "
                     "wherever the brickwork is wettest",
             "correct": False,
             "why": "It appears where water leaves the wall from inside, and "
                    "builds up as more water evaporates there"},
        ],
        "figure": None,
    },
    {
        "id": "c3-04-s31",
        "band": "standard",
        "text": "Two trays of the same solution stand at the same "
                "temperature: one in a fume cupboard with air drawn steadily "
                "across it, one in a closed cupboard. Which crystallises "
                "sooner, and why?",
        "options": [
            {"text": "The closed cupboard, because still air lets the "
                     "solvent leave the surface undisturbed",
             "correct": False,
             "why": "Still air fills with vapour and the drying slows right "
                    "down. Moving air takes that vapour away"},
            {"text": "Both together, because the temperature of the two "
                     "trays is exactly the same",
             "correct": False,
             "why": "Temperature is not the only thing that sets the rate. "
                    "How fast the air moves matters as well"},
            {"text": "The fume cupboard, because the vapour is carried away "
                     "and more solvent can leave",
             "correct": True},
            {"text": "The closed cupboard, because crystals form sooner in "
                     "the dark than they do in the light",
             "correct": False,
             "why": "Light has nothing to do with crystallising. It is the "
                    "moving air that makes the difference"},
        ],
        "figure": None,
    },
    {
        "id": "c3-04-s32",
        "band": "standard",
        "text": "Equal volumes of a dilute and a concentrated solution of "
                "the same solute stand in identical dishes in one room. "
                "Explain which shows crystals first.",
        "options": [
            {"text": "The dilute one, because a thin solution dries out "
                     "faster than a thick one does",
             "correct": False,
             "why": "Both have the same volume to lose, and the strong one "
                    "is saturated with far more of it still there"},
            {"text": "The concentrated one, because it has less solvent to "
                     "lose before it becomes saturated",
             "correct": True},
            {"text": "Both together, because the same volume of solvent has "
                     "to leave each of the two dishes",
             "correct": False,
             "why": "Crystals start at saturation rather than at dryness, "
                    "and the stronger dish reaches that point sooner"},
            {"text": "The dilute one, because its solute has more room in "
                     "which to build a crystal",
             "correct": False,
             "why": "Room is not what a crystal needs. It needs the solution "
                    "to be full, which comes sooner in the stronger dish"},
        ],
        "figure": None,
    },

    # ── harder · MRB-338 expansion ──────────────────────────────────────
    {
        "id": "c3-04-h08",
        "band": "harder",
        "text": "A student writes: “You cannot crystallise anything without "
                "heating it, because the solvent has to be boiled off.” "
                "Evaluate that claim.",
        "options": [
            {"text": "Right, because a solution left cold simply stays a "
                     "solution however long it is left standing",
             "correct": False,
             "why": "A dish on a windowsill is dry within days and full of "
                    "large crystals, with no heating at all"},
            {"text": "Right, unless the solvent happens to be one that "
                     "evaporates more readily than water does",
             "correct": False,
             "why": "Water itself evaporates unheated — washing dries on a "
                    "cold line. No solvent has to be boiled"},
            {"text": "Wrong twice over — the solvent leaves at any "
                     "temperature, and the best crystals are never heated",
             "correct": True},
            {"text": "Wrong about the heating, but right that the solvent "
                     "must reach its boiling point before it can leave",
             "correct": False,
             "why": "Those two cannot both stand, since reaching a boiling "
                    "point is the heating. It leaves well below it"},
        ],
        "figure": None,
    },
    {
        "id": "c3-04-h09",
        "band": "harder",
        "text": "A substance breaks down above 110 °C. A technician has a "
                "full working day to recover it from solution. Compare a "
                "water bath with a Bunsen, and choose.",
        "options": [
            {"text": "The water bath — it cannot pass 100 °C, and the extra "
                     "time it costs is time she has",
             "correct": True},
            {"text": "The Bunsen — a flame can be held below 110 °C by "
                     "keeping the dish high above it on a tripod",
             "correct": False,
             "why": "A flame cannot be held to a temperature that way, and a "
                    "dish over one passes 110 °C in moments"},
            {"text": "The Bunsen — the substance only breaks down after the "
                     "dish has gone completely dry",
             "correct": False,
             "why": "It breaks down above 110 °C whether liquid is there or "
                    "not, and a flame takes it past that easily"},
            {"text": "Neither — a substance that breaks down on warming "
                     "cannot be recovered from a solution at all",
             "correct": False,
             "why": "It can be recovered by any method that stays below "
                    "110 °C, and a water bath does exactly that"},
        ],
        "figure": None,
    },
    {
        "id": "c3-04-h10",
        "band": "harder",
        "text": "A student plans to boil a solution dry over a Bunsen while leaning over the dish to watch the first crystals form, wearing safety glasses. Evaluate the plan.",
        "options": [
            {
             "text": "Safety glasses guard against everything a drying dish is able to throw out, so the plan is fine as it stands",
             "correct": False,
             "why": "They cover the eyes only, and hot solution spits onto skin as readily as onto a lens",
            },
            {
             "text": "A small enough flame means no spitting at all, so the safety glasses are the part she could drop",
             "correct": False,
             "why": "A small flame still takes a dish to dryness, and a drying dish still spits hot liquid",
            },
            {
             "text": "The first crystals cannot be seen until after the dish has gone dry, so there is nothing there to lean over for",
             "correct": False,
             "why": "Crystals appear at the edges while liquid is still there. The fault in the plan is where her face is",
            },
            {
             "text": "The glasses are right, but leaning over puts the rest of her face above spitting solution",
             "correct": True,
            },
        ],
        "figure": None,
    },
    {
        "id": "c3-04-h11",
        "band": "harder",
        "text": "A laboratory takes flammable solvents off on an "
                "electrically heated water bath rather than over a flame. "
                "Explain what hazard that removes and what it does not.",
        "options": [
            {"text": "It stops the solvent evaporating, so no flammable "
                     "vapour is ever produced in the room",
             "correct": False,
             "why": "Evaporating the solvent is the whole point of the "
                    "operation. The vapour is still produced"},
            {"text": "It removes the source of ignition, but the vapour is "
                     "still flammable and still has to be ventilated",
             "correct": True},
            {"text": "It removes the hazard altogether, because an "
                     "electrically heated bath is not able to set anything "
                     "alight",
             "correct": False,
             "why": "It removes the flame, not the vapour. A spark or a hot "
                    "surface elsewhere can still light it"},
            {"text": "It removes the flammability of the vapour, because "
                     "gentle warming changes what that vapour is",
             "correct": False,
             "why": "Warming changes nothing about the substance. The vapour "
                    "is as flammable at 40 °C as at 400 °C"},
        ],
        "figure": None,
    },
    {
        "id": "c3-04-h12",
        "band": "harder",
        "text": "A student evaporates 0.500 dm³ of a solution containing "
                "48 g of solid per dm³, and weighs 21.6 g of dry crystals. "
                "What percentage of the dissolved solid did she recover?",
        "options": [
            {"text": "45%", "correct": False,
             "why": "That compares 21.6 g with the 48 g in a full dm³. Half "
                    "a dm³ was used, so 24 g was what she should expect"},
            {"text": "111%", "correct": False,
             "why": "That divides the expected mass by the recovered one. "
                    "She collected less than she dissolved, not more"},
            {"text": "90%", "correct": True},
            {"text": "2.4%", "correct": False,
             "why": "2.4 g is the mass she is missing, not a percentage. "
                    "The recovery compares 21.6 g with 24 g"},
        ],
        "figure": None,
    },
    {
        "id": "c3-04-h13",
        "band": "harder",
        "text": "Two students weigh their crystals straight off a water "
                "bath, and each records a mass slightly HIGHER than the mass "
                "of solute dissolved. Explain how that can happen.",
        "options": [
            {"text": "Solvent is still on and in the crystals, and is being "
                     "weighed as though it were solid",
             "correct": True},
            {"text": "Some of the solvent turned into solute during the run "
                     "and added its mass to the crystals",
             "correct": False,
             "why": "A solvent cannot turn into a solute. The extra mass is "
                    "solvent that has not yet been driven off"},
            {"text": "The crystals took up water out of the air on their way "
                     "across the room to the balance",
             "correct": False,
             "why": "Crystals straight off a warm bath are hotter than the "
                    "room. The extra mass is solvent that never left"},
            {"text": "Solid dissolved out of the basin itself while it was "
                     "being heated, and was weighed with the crystals",
             "correct": False,
             "why": "An evaporating basin gives up nothing to the solution. "
                    "What is extra is liquid still in the product"},
        ],
        "figure": None,
    },
    {
        "id": "c3-04-h14",
        "band": "harder",
        "text": "Once the first crystals have appeared and evaporation "
                "carries on, predict what happens to the concentration of "
                "the solution that is still in the dish.",
        "options": [
            {"text": "It keeps rising, because the solute is packed into "
                     "less and less water right up to the end",
             "correct": False,
             "why": "It cannot rise past saturation. Once the solution is "
                    "full, anything extra comes out as crystal"},
            {"text": "It falls steadily, because solute keeps leaving the "
                     "solution and joining the growing crystals",
             "correct": False,
             "why": "Solvent is leaving at the same time, so the solution "
                    "stays full while any liquid remains"},
            {"text": "It rises until the dish is about half dry and then "
                     "drops back to where it started",
             "correct": False,
             "why": "It rises to saturation and holds there. Nothing in the "
                    "dish takes it back down again"},
            {"text": "It holds at saturation, because any solute that can no "
                     "longer stay dissolved joins the crystals",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c3-04-h15",
        "band": "harder",
        "text": "Two tanks hold the same mass of dissolved solid, and tank A "
                "holds twice the volume of solution that tank B does. "
                "Compare the mass recovered and the energy needed.",
        "options": [
            {"text": "Twice as much solid from tank A, because it holds "
                     "twice as much solution as tank B does",
             "correct": False,
             "why": "It holds twice as much SOLVENT. The mass of solid is "
                    "stated to be the same in both tanks"},
            {"text": "The same mass from each, and about twice the energy "
                     "for tank A because it has twice the solvent",
             "correct": True},
            {"text": "The same mass from each and the same energy too, "
                     "because the solid recovered is identical",
             "correct": False,
             "why": "The energy goes into removing solvent, and tank A has "
                    "twice as much of that to remove"},
            {"text": "Half as much solid from tank A, because the solution "
                     "in it is only half as concentrated",
             "correct": False,
             "why": "Concentration is not yield. Both tanks hold the same "
                    "mass of solid and both give all of it back"},
        ],
        "figure": None,
    },
    {
        "id": "c3-04-h16",
        "band": "harder",
        "text": "One mineral is found as centimetre crystals lining a cave "
                "and as a fine powder in a dried-out lake bed. A student "
                "says they must be different substances. Evaluate that.",
        "options": [
            {"text": "Right, because two samples with different crystal "
                     "sizes cannot be the same substance",
             "correct": False,
             "why": "Size comes from the rate. One salt gives a crust in "
                    "minutes and cubes over a week"},
            {"text": "Right, because any substance always crystallises to "
                     "the same size wherever it is found",
             "correct": False,
             "why": "Nothing ties a crystal's size to the substance. The "
                    "cave was slow and the lake bed was fast"},
            {"text": "Wrong — the same substance gives different sizes "
                     "depending on how slowly it came out of solution",
             "correct": True},
            {"text": "Wrong, because size comes from the substance, so the "
                     "two samples must have formed in the same way",
             "correct": False,
             "why": "Half of that is backwards: shape comes from the "
                    "substance and size from the rate"},
        ],
        "figure": None,
    },
    {
        "id": "c3-04-h17",
        "band": "harder",
        "text": "4.0 g of salt is dissolved in 96 g of water and the "
                "solution is evaporated to dryness, leaving 4.0 g of "
                "crystals. Explain what those masses show, and what they do "
                "not.",
        "options": [
            {"text": "The salt was unchanged and none of it was lost; they "
                     "say nothing about the water being destroyed",
             "correct": True},
            {"text": "The water became part of the salt, which is why the "
                     "solution had a mass of 100 g to begin with",
             "correct": False,
             "why": "The 100 g was the two masses side by side, and the "
                    "water left as water. Nothing became salt"},
            {"text": "96 g of matter was destroyed, since the dish now "
                     "weighs far less than the solution did",
             "correct": False,
             "why": "The dish weighs less because the water is in the air. "
                    "Evaporation destroys nothing at all"},
            {"text": "The salt gained no mass, and therefore that nothing "
                     "whatever left the dish during the run",
             "correct": False,
             "why": "96 g did leave the dish, as water vapour. The salt's "
                    "mass says nothing about the solvent"},
        ],
        "figure": None,
    },
    {
        "id": "c3-04-h18",
        "band": "harder",
        "text": "A 400 g sample of solution is heated until 340 g of solvent "
                "has been driven off, leaving a wet paste. Drying the paste "
                "gives 24 g of solid. How much solvent was in the paste?",
        "options": [
            {"text": "60 g", "correct": False,
             "why": "60 g is the whole paste, and 24 g of that turned out to "
                    "be solid"},
            {"text": "24 g", "correct": False,
             "why": "24 g is the solid itself. The solvent is whatever else "
                    "made up the 60 g of paste"},
            {"text": "316 g", "correct": False,
             "why": "That takes the solid off the solvent already driven "
                    "away. The paste weighed only 60 g"},
            {"text": "36 g", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c3-04-h19",
        "band": "harder",
        "text": "Evaporating 250 cm³ of a solution to dryness leaves 3.0 g "
                "of solid. Calculate the concentration of that solution in "
                "grams per dm³.",
        "options": [
            {"text": "3.0 g/dm³", "correct": False,
             "why": "That is the mass in 250 cm³, and a dm³ is four times "
                    "that volume"},
            {"text": "12 g/dm³", "correct": True},
            {"text": "0.75 g/dm³", "correct": False,
             "why": "That divides by four instead of multiplying. A dm³ "
                    "holds more solution than 250 cm³ does"},
            {"text": "750 g/dm³", "correct": False,
             "why": "That multiplies the mass by the volume in cubic "
                    "centimetres rather than scaling up to 1 dm³"},
        ],
        "figure": None,
    },
    {
        "id": "c3-04-h20",
        "band": "harder",
        "text": "Potassium nitrate dissolves to 110 g per 100 g of water at "
                "60 °C, and to 32 g per 100 g at 20 °C. 250 g of water is "
                "saturated at 60 °C and cooled to 20 °C. What crystallises?",
        "options": [
            {"text": "78 g", "correct": False,
             "why": "78 g is the answer for 100 g of water, and there is two "
                    "and a half times that much water here"},
            {"text": "80 g", "correct": False,
             "why": "80 g is what stays dissolved at 20 °C in 250 g of "
                    "water, rather than what comes out of it"},
            {"text": "195 g", "correct": True},
            {"text": "275 g", "correct": False,
             "why": "275 g is all that was dissolved at 60 °C. Some of it "
                    "stays dissolved once the flask is cold"},
        ],
        "figure": None,
    },
    {
        "id": "c3-04-h21",
        "band": "harder",
        "text": "A student recovers 92% of her dissolved solid on her first run and 97% on her second, by the same method. Suggest the likely reason, and say what it cannot be.",
        "options": [
            {
             "text": "She lost less in the transfer the second time; it cannot be that more solute was in the second solution",
             "correct": True,
            },
            {
             "text": "She heated the second dish for longer, so more of the solid came out; it cannot be that she collected it more carefully",
             "correct": False,
             "why": "Heating drives off solvent only. Every gram of solute is in the dish however long the heat is left on",
            },
            {
             "text": "The second solution was stronger, so it gave up a greater percentage; it cannot be that the two solutions were the same",
             "correct": False,
             "why": "The percentage compares what was collected with what was dissolved, so concentration cannot change it",
            },
            {
             "text": "The second run was slower, so less solute went into the air; it cannot be that any stayed in the dish",
             "correct": False,
             "why": "No solute is lost into the air at any speed. What improved was how much she got out of the dish",
            },
        ],
        "figure": None,
    },
    {
        "id": "c3-04-h22",
        "band": "harder",
        "text": "Kidney stones are more common in hot climates than in cool ones. Explain that using what you know about solutions losing their solvent.",
        "options": [
            {
             "text": "Heat makes the dissolved substances less soluble, so they are forced out of solution as a solid",
             "correct": False,
             "why": "Warming usually lets more dissolve rather than less. What matters here is the water lost as sweat",
            },
            {
             "text": "Heat makes crystals grow faster, so the same stone forms in a shorter time than it would when cool",
             "correct": False,
             "why": "How fast a crystal grows is not the issue. Reaching saturation at all is, and losing water does that",
            },
            {
             "text": "Sweating adds extra dissolved salts to the body fluid, so there is more solid in it than before",
             "correct": False,
             "why": "Sweat takes salt and water out of the body rather than putting any in. What changes is how little water is left behind",
            },
            {
             "text": "More water is lost as sweat, so the fluid becomes concentrated enough to reach saturation",
             "correct": True,
            },
        ],
        "figure": None,
    },
    {
        "id": "c3-04-h23",
        "band": "harder",
        "text": "A hotel fits a unit that takes the dissolved solids out of "
                "its water, and its glasses stop drying with white marks. A "
                "guest says the unit must dry the glasses faster. Evaluate.",
        "options": [
            {"text": "Right, because water that dries faster has far less "
                     "time in which to leave any mark on the glass at all",
             "correct": False,
             "why": "Drying time was never the cause. Water with nothing "
                    "dissolved in it leaves nothing however slowly it dries"},
            {"text": "Wrong — the marks were the dissolved solids, and "
                     "taking them out leaves nothing to be deposited",
             "correct": True},
            {"text": "Right, because the treated water evaporates at a "
                     "lower temperature than the old supply did",
             "correct": False,
             "why": "Both evaporate at ordinary room temperature. What has "
                    "changed is what the water had dissolved in it"},
            {"text": "Wrong — the unit coats the glass so that solids can no "
                     "longer stick to its surface",
             "correct": False,
             "why": "Nothing is coated. The solids that used to be left "
                    "behind are simply no longer in the water"},
        ],
        "figure": None,
    },
    {
        "id": "c3-04-h24",
        "band": "harder",
        "text": "A company proposes moving its lithium brine ponds from a "
                "high desert to a cheap coastal site with heavy rainfall. "
                "Evaluate the proposal.",
        "options": [
            {"text": "Good, because the extra rainfall would dissolve more of "
                     "the lithium out of the brine and raise the yield",
             "correct": False,
             "why": "The lithium is dissolved already, and added water "
                    "dilutes it. Rain undoes the work the ponds do"},
            {"text": "Good, because damp sea air takes up water vapour more "
                     "readily than dry desert air can",
             "correct": False,
             "why": "Damp air takes up vapour more slowly, not faster, which "
                    "makes the coastal site worse still"},
            {"text": "Poor, because rain puts solvent back into the ponds, "
                     "so they would take far longer or never finish",
             "correct": True},
            {"text": "Poor, because lithium can only be recovered from brine "
                     "at high altitude in the first place",
             "correct": False,
             "why": "Altitude is not a requirement anywhere. The site fails "
                    "because the rain replaces the water"},
        ],
        "figure": None,
    },
    {
        "id": "c3-04-h25",
        "band": "harder",
        "text": "Two runs on the same solution give the same mass of solid: "
                "one a crust needing a spatula, one loose crystals that tip "
                "out. A student calls the crust run less efficient. "
                "Evaluate.",
        "options": [
            {"text": "Wrong on yield — both recovered the same mass; a crust "
                     "is only harder to lift without losing some",
             "correct": True},
            {"text": "Right, because a crust always holds some of the solid "
                     "back in the dish however hard it is scraped",
             "correct": False,
             "why": "A crust holds nothing back of itself, and the two "
                    "masses were stated to be equal"},
            {"text": "Right, because boiling a solution hard destroys part "
                     "of the solute before it can crystallise",
             "correct": False,
             "why": "Nothing is destroyed. Both runs gave the same mass, "
                    "which is what the bench shows every time"},
            {"text": "Wrong, because the crust run in fact recovers more "
                     "solid than a slow run of the same solution",
             "correct": False,
             "why": "Neither recovers more. The mass is fixed by what was "
                    "dissolved, and both runs collected it"},
        ],
        "figure": None,
    },
    {
        "id": "c3-04-h26",
        "band": "harder",
        "text": "A chemist writes “evaporate to dryness” beside a sample she "
                "wants to weigh, and “crystallise” beside one she wants to "
                "identify from its crystal shape. Explain why they differ.",
        "options": [
            {"text": "Dryness gives a purer solid, and purity matters for a "
                     "weighing but not for an identification",
             "correct": False,
             "why": "Both leave everything that was dissolved, so neither is "
                    "purer. What differs is the form the solid takes"},
            {"text": "Crystallising leaves solvent in the sample, and a "
                     "shape can only be made out in a solid that is damp",
             "correct": False,
             "why": "Crystals are dried before they are examined. Slow "
                    "growth, not dampness, is what gives them faces"},
            {"text": "Dryness recovers more of the solid, and a weighing "
                     "needs all of it while an identification does not",
             "correct": False,
             "why": "The mass recovered is the same either way. What dryness "
                    "buys her is speed rather than yield"},
            {"text": "A weighing needs only the mass, which dryness gives "
                     "fastest; a shape needs crystals grown slowly",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c3-04-h27",
        "band": "harder",
        "text": "A coloured solution deepens in colour as it evaporates, "
                "then the first crystals appear and the liquid stops "
                "deepening. Explain both observations.",
        "options": [
            {"text": "The solute stopped evaporating once the crystals had "
                     "formed, so the colour held where it was",
             "correct": False,
             "why": "The solute never evaporated at all. The colour held "
                    "because the solution could take no more"},
            {"text": "It concentrated until it was saturated; after that any "
                     "extra solute crystallised instead of dissolving",
             "correct": True},
            {"text": "The crystals drew the colour out of the liquid, so "
                     "from then on the liquid began to fade",
             "correct": False,
             "why": "The liquid holds its strength rather than fading. It is "
                    "full, and anything further comes out as solid"},
            {"text": "The dish cooled once crystals had started, and a "
                     "cooler solution of any kind looks paler",
             "correct": False,
             "why": "Cooling a saturated solution brings more solid out, and "
                    "it does not make the liquid paler"},
        ],
        "figure": None,
    },
    {
        "id": "c3-04-h28",
        "band": "harder",
        "text": "A technician weighs her crystals five minutes after taking "
                "them off a water bath, and again an hour later. The later "
                "reading is lower. Which should she report, and why?",
        "options": [
            {"text": "The first, because the crystals were freshest then and "
                     "had lost nothing to the air around them",
             "correct": False,
             "why": "They had not finished losing solvent. The early reading "
                    "counts liquid as though it were crystal"},
            {"text": "The mean of the two, because an average of two "
                     "readings is always more reliable than a single one",
             "correct": False,
             "why": "Averaging a wrong reading with a right one gives a "
                    "wrong answer. Only the dry mass is the mass"},
            {"text": "The later one, because the first was taken while the "
                     "dish was still warm and still losing solvent",
             "correct": True},
            {"text": "The first, because crystals slowly take up water from "
                     "the air and gain mass over an hour on the bench",
             "correct": False,
             "why": "The mass fell over that hour, so nothing was taken up. "
                    "It was still drying out"},
        ],
        "figure": None,
    },
    {
        "id": "c3-04-h29",
        "band": "harder",
        "text": "A school wants the largest possible copper sulfate crystals "
                "for an open evening in a fortnight, and also a weighed "
                "sample of the same solid by Friday. Suggest how to do both.",
        "options": [
            {"text": "Divide the solution: leave part to evaporate slowly "
                     "for the fortnight and take the rest to dryness now",
             "correct": True},
            {"text": "Boil the whole batch dry by Friday, since the mass and "
                     "the display crystals come out of the same run",
             "correct": False,
             "why": "Boiling gives the mass but leaves a fine crust with "
                    "nothing worth putting on a display"},
            {"text": "Leave the whole batch on a windowsill, since the "
                     "display matters more than the date of the weighing",
             "correct": False,
             "why": "That misses Friday altogether, and both jobs can be met "
                    "by splitting the solution between them"},
            {"text": "Boil the batch dry now, then redissolve the crust and "
                     "boil it again to grow the display crystals",
             "correct": False,
             "why": "A second boiling gives a second crust. Large crystals "
                    "need a slow run, not a repeated fast one"},
        ],
        "figure": None,
    },
    {
        "id": "c3-04-h30",
        "band": "harder",
        "text": "A conservator treating a damp historic wall is warned that "
                "washing the white bloom off with water will bring it back "
                "worse. Explain why that could be true.",
        "options": [
            {"text": "Water reacts with the brick and makes a fresh batch of "
                     "the white solid every single time the wall is washed",
             "correct": False,
             "why": "No reaction is involved. The solid was in the wall "
                    "already, dissolved in the water moving through it"},
            {"text": "The bloom comes back because washing removes the layer "
                     "that was sealing the face of the wall",
             "correct": False,
             "why": "The bloom seals nothing at all. Washing simply carries "
                    "the dissolved solids back into the brick"},
            {"text": "Washing cools the wall down, and a cool wall deposits "
                     "far more solid on its face than a warm one",
             "correct": False,
             "why": "Temperature is not what deposits it. Evaporation at the "
                    "surface is, and wetting the wall feeds that"},
            {"text": "The wash water dissolves the solids and carries them "
                     "into the wall, to be left at the face again as it dries",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c3-04-h31",
        "band": "harder",
        "text": "A launderette's drying room blows warm air across the wet "
                "clothes and also extracts air from the room. Explain why "
                "the extraction matters as much as the warmth.",
        "options": [
            {"text": "Extracting the air cools the room, and cool air dries "
                     "clothes more quickly than warm air does",
             "correct": False,
             "why": "Cool air dries more slowly. What extraction does is "
                    "remove air that is already full of vapour"},
            {"text": "Air that stays in the room fills with vapour and takes "
                     "no more, so drier air has to keep arriving",
             "correct": True},
            {"text": "Extracting the air pulls liquid water straight out of "
                     "the cloth, which warming on its own cannot do",
             "correct": False,
             "why": "Extraction moves air and vapour rather than liquid. The "
                    "water still has to evaporate first"},
            {"text": "Extracting the air lowers the pressure until the water "
                     "in the clothes freezes and falls out of them",
             "correct": False,
             "why": "Nothing freezes in a drying room. The extracted air is "
                    "carrying water vapour out with it"},
        ],
        "figure": None,
    },
    {
        "id": "c3-04-h32",
        "band": "harder",
        "text": "Two dishes hold the same mass of dissolved solid, one in twice as much water as the other. Both sit in the same room; the stronger shows crystals on day two and the weaker on day five. Explain the difference in timing, and predict how the two final masses compare.",
        "options": [
            {
             "text": "The stronger crystallises first because strong solutions grow crystals faster, and it ends with the greater mass because it was the stronger one",
             "correct": False,
             "why": "Strength decides when saturation is reached, not how much solid is there. Equal solute gives equal mass",
            },
            {
             "text": "The weaker takes longer because some of its solute is lost through the extra water, and the two masses only appear to be equal",
             "correct": False,
             "why": "Nothing is lost through water. The masses are genuinely equal because equal solute was dissolved",
            },
            {
             "text": "The stronger reaches saturation sooner, having less water to lose; the masses match because both held the same solute",
             "correct": True,
            },
            {
             "text": "The stronger crystallises first because a smaller volume warms up faster, and the extra warmth drives a greater mass out of it",
             "correct": False,
             "why": "Both dishes sat at the same room temperature, and warmth does not add solid. What differed was how much water each had to lose",
            },
        ],
        "figure": None,
    },
]
