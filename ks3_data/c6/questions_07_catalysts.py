"""C6 lesson 07 — Catalysts: twelve questions (MRB-269).

The lesson's argument is a definition with TWO halves — faster, and not
consumed — and a boundary: a catalyst cannot make an impossible reaction
happen. These twelve probe the angles the mastery ladder leaves alone.

The distractors are built from the lesson's declared misconception.

`ACID-10` (a catalyst is used up slowly, which is why it wears out) drives e02,
s02, h01 and h03. h01 is the one that matters: it puts a working catalytic
converter and a dead one side by side with the same mass of platinum in both,
so "it wore out" has to explain a balance that has not moved.

A second strand, which is the whole construction of the bench and is in no
register entry, is that ADDING SOMETHING IS SUFFICIENT. e04, s01 and h02 are
built on it: the dilute acid changes nothing at all and is still there in full
at the end, the sand is a solid with a large surface area and does nothing
either, and the empty flask reacts anyway given a year.

⊕ 30 Aug 2026 (MRB-295, C6-11). This strand USED to read "FASTER IS
SUFFICIENT", and e04 and h02 were built on the dilute acid being faster than
the control and consumed doing it. That was invented chemistry — acid
stabilises hydrogen peroxide — and Mide ruled the flask honest on 28 Aug
2026. Both questions are re-aimed at what the bench now shows, which is the
same definition approached from its other half: coming back unchanged is not
sufficient either, and the acid is the flask that proves it.

A third strand is that a catalyst makes MORE. e03 and s04 separate rate from
yield, which is the distinction rung 2 turns on and the one a factory pays for.

A fourth strand is the boundary. s03 and h04 ask about reactions that cannot
happen, and reach back to `acid-plus-metal` for the case the student already
has.

Every question here is new prose, and the bar is §13's. No correct answer is
strictly the longest in its set by four words or by 1.4x, and the twelve are
authored level across the four answer positions — three apiece (MRB-278).
"""

UNIT = "C6"
LESSON = "catalysts"
LESSON_NUMBER = 7

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "c6-07-e01",
        "band": "easier",
        "text": "What does a catalyst change about a reaction?",
        "options": [
            {"text": "How fast it goes, and nothing else", "correct": True},
            {"text": "How much product the reaction makes in total",
             "correct": False,
             "why": "The final amount is set by how much you started with. "
                    "Only the time taken is different."},
            {"text": "What the products of the reaction turn out to be",
             "correct": False,
             "why": "The same reactants give the same products. A catalyst "
                    "changes the route, not the destination."},
            {"text": "Whether the reaction is able to happen at all",
             "correct": False,
             "why": "A catalyst can only speed up a reaction that is already "
                    "possible. It cannot start an impossible one."},
        ],
        "figure": None,
    },
    {
        "id": "c6-07-e02",
        "band": "easier",
        "text": "1.00 g of manganese dioxide is added to hydrogen peroxide. "
                "It is filtered out, dried and weighed afterwards. What does "
                "it weigh?",
        "options": [
            {"text": "A little less than 1.00 g, because some was used up",
             "correct": False,
             "why": "None of it is used up. That is the half of the "
                    "definition the fifth flask on the bench fails."},
            {"text": "1.00 g, exactly what it weighed at the start",
             "correct": True},
            {"text": "A little more than 1.00 g, because it absorbed some "
                     "oxygen", "correct": False,
             "why": "It takes no part in the reaction, so it gains nothing. "
                    "The oxygen goes into the syringe."},
            {"text": "Nothing, because it dissolved into the peroxide",
             "correct": False,
             "why": "It is insoluble, which is why it can be filtered out. "
                    "All of it comes back on the paper."},
        ],
        "figure": None,
    },
    {
        "id": "c6-07-e03",
        "band": "easier",
        "text": "Two flasks of the same hydrogen peroxide are left until both "
                "reactions have completely finished. One had a catalyst. How "
                "much oxygen did each make?",
        "options": [
            {"text": "The catalysed flask made more, because it worked "
                     "harder", "correct": False,
             "why": "The same peroxide can only give the same oxygen. What "
                    "changed was how long it took."},
            {"text": "The catalysed flask made less, because some went into "
                     "the powder", "correct": False,
             "why": "The powder takes nothing. Filter it out at the end and "
                    "every milligram is there."},
            {"text": "The same amount, because both reactions ran to the end",
             "correct": True},
            {"text": "It cannot be said without knowing how much catalyst "
                     "went in", "correct": False,
             "why": "More catalyst goes faster still, and the final volume is "
                    "set by the peroxide either way."},
        ],
        "figure": None,
    },
    {
        "id": "c6-07-e04",
        "band": "easier",
        "text": "Dilute acid is added to hydrogen peroxide. The reaction runs "
                "no faster than it did with nothing added, and the acid is "
                "all still there at the end. Is it a catalyst?",
        "options": [
            {"text": "Yes, because it came back unchanged", "correct": False,
             "why": "That is only half the definition, and it is the half "
                    "that is easiest to pass — the sand came back unchanged "
                    "too. A catalyst also has to speed the reaction up."},
            {"text": "Yes, because something was added to the flask",
             "correct": False,
             "why": "Adding something is not the test. Making the reaction "
                    "go faster, and coming back unchanged, is."},
            {"text": "No, because a catalyst has to be a solid powder",
             "correct": False,
             "why": "The liver on the same bench is not a powder and is a "
                    "catalyst. What rules the acid out is that it changed "
                    "nothing."},
            {"text": "No, because it did not speed the reaction up at all",
             "correct": True},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "c6-07-s01",
        "band": "standard",
        "text": "A flask of peroxide with sand in it behaves exactly like the "
                "empty one. What does that flask show?",
        "options": [
            {"text": "That the sand was not fine enough to work properly",
             "correct": False,
             "why": "Surface area is not what it lacks. Sand simply does not "
                    "catalyse this reaction, however fine it is."},
            {"text": "That adding a solid is not by itself enough to speed a "
                     "reaction", "correct": True},
            {"text": "That hydrogen peroxide does not decompose without a "
                     "catalyst", "correct": False,
             "why": "It does — slowly. Both the sand flask and the empty one "
                    "made a couple of cm³ in a minute."},
            {"text": "That sand must be a catalyst for some other reaction "
                     "instead", "correct": False,
             "why": "It may well be, and this flask says nothing about that. "
                    "What it shows is that being a solid is not the point."},
        ],
        "figure": None,
    },
    {
        "id": "c6-07-s02",
        "band": "standard",
        "text": "A catalytic converter stops working after a car has run on "
                "leaded petrol. What has happened to the platinum?",
        "options": [
            {"text": "It has been used up gradually over the miles driven",
             "correct": False,
             "why": "Weigh it and it is all there. A catalyst is not consumed "
                    "by the reaction it speeds up."},
            {"text": "It has reacted with the lead and turned into something "
                     "else", "correct": False,
             "why": "The platinum is still platinum. The lead sits on the "
                    "surface rather than combining with it."},
            {"text": "It is still there, but its surface is coated by lead",
             "correct": True},
            {"text": "It has melted, because a converter runs extremely hot",
             "correct": False,
             "why": "Platinum melts at nearly 1800 degrees and an exhaust "
                    "never gets near it."},
        ],
        "figure": None,
    },
    {
        "id": "c6-07-s03",
        "band": "standard",
        "text": "Would a catalyst make copper react with dilute hydrochloric "
                "acid?",
        "options": [
            {"text": "No, because copper is below hydrogen and cannot "
                     "displace it", "correct": True},
            {"text": "Yes, given enough of it and enough time to work",
             "correct": False,
             "why": "Neither amount nor time helps. There is no reaction "
                    "waiting to be sped up."},
            {"text": "Yes, because that is what catalysts are for",
             "correct": False,
             "why": "A catalyst shortens a reaction that can happen. It does "
                    "not create one."},
            {"text": "No, because copper would poison the catalyst on "
                     "contact", "correct": False,
             "why": "The catalyst would be fine. The reason is that there is "
                    "nothing for it to catalyse."},
        ],
        "figure": None,
    },
    {
        "id": "c6-07-s04",
        "band": "standard",
        "text": "A works finds a catalyst that lets a reaction run at 250 °C "
                "instead of 450 °C, with the same yield. Why is that worth "
                "paying for?",
        "options": [
            {"text": "Because the product comes out purer at the lower "
                     "temperature", "correct": False,
             "why": "The products are unchanged. A catalyst does not alter "
                    "what is made."},
            {"text": "Because the reaction now makes considerably more "
                     "product", "correct": False,
             "why": "The yield is stated as the same. The saving is not in "
                    "the amount."},
            {"text": "Because a lower temperature makes the plant safer to "
                     "run", "correct": False,
             "why": "Safety is a real benefit and it is not the one the "
                    "question is about. The decisive saving is energy."},
            {"text": "Because two hundred degrees less costs far less fuel, "
                     "every hour", "correct": True},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "c6-07-h01",
        "band": "harder",
        "text": "A working converter and a dead one are opened up and both "
                "contain the same mass of platinum. What does that rule out?",
        "options": [
            {"text": "That the dead converter's catalyst was used up",
             "correct": True},
            {"text": "That the dead converter was ever working in the first "
                     "place", "correct": False,
             "why": "The mass says nothing about its history. It only says "
                    "nothing has been consumed."},
            {"text": "That lead was the cause of the failure at all",
             "correct": False,
             "why": "Lead coating the surface is entirely consistent with an "
                    "unchanged mass. That is the point."},
            {"text": "That the two converters were the same design as each "
                     "other", "correct": False,
             "why": "Equal masses suggest the same design rather than ruling "
                    "it out, and the design is not what is in question."},
        ],
        "figure": None,
    },
    {
        "id": "c6-07-h02",
        "band": "harder",
        "text": "Which single result on the five-flask bench proves that "
                "coming back unchanged is not enough to make something a "
                "catalyst?",
        "options": [
            {"text": "The empty flask, which reacted very slowly on its own",
             "correct": False,
             "why": "That is the control the others are measured against. "
                    "Nothing was added to it at all, so there is nothing to "
                    "come back unchanged."},
            {"text": "The dilute acid flask, which changed nothing and was "
                     "all still there at the end", "correct": True},
            {"text": "The liver flask, which was the fastest of all five",
             "correct": False,
             "why": "The liver is a catalyst and it passes both halves. It "
                    "cannot show that one half is insufficient."},
            {"text": "The manganese dioxide flask, which was recovered in "
                     "full", "correct": False,
             "why": "It was recovered in full AND it sped the reaction up. "
                    "Passing both halves is what makes it a catalyst, so it "
                    "cannot show that either half alone is not enough."},
        ],
        "figure": None,
    },
    {
        "id": "c6-07-h03",
        "band": "harder",
        "text": "Boiled liver does nothing in hydrogen peroxide, though fresh "
                "liver froths violently. What does that show about enzymes?",
        "options": [
            {"text": "That boiling used up all the catalase in the liver",
             "correct": False,
             "why": "The catalase is still there. What has gone is its shape, "
                    "and the shape is what does the work."},
            {"text": "That enzymes only work inside a living organism",
             "correct": False,
             "why": "Fresh liver is not alive either. It works because the "
                    "enzyme in it is intact."},
            {"text": "That their shape is what makes them work, and heat "
                     "wrecks it", "correct": True},
            {"text": "That enzymes are consumed faster at high temperatures",
             "correct": False,
             "why": "They are not consumed at any temperature. Heat damages "
                    "them rather than using them up."},
        ],
        "figure": None,
    },
    {
        "id": "c6-07-h04",
        "band": "harder",
        "text": "Two students design a test for whether a black powder is a "
                "catalyst. Which plan settles it?",
        "options": [
            {"text": "Run the reaction with the powder and time how long it "
                     "takes", "correct": False,
             "why": "With nothing to compare it against, a time is a number "
                    "and not a result."},
            {"text": "Run it with and without the powder and compare the two "
                     "times", "correct": False,
             "why": "That settles the first half of the definition only. "
                    "Something can speed a reaction up and still be used up "
                    "doing it, and a stopwatch cannot see the difference."},
            {"text": "Weigh the powder before and after, and check nothing "
                     "was lost", "correct": False,
             "why": "That settles the second half only. Sand also comes back "
                    "weighing the same and is not a catalyst."},
            {"text": "Compare the times with and without, AND weigh the "
                     "powder before and after", "correct": True},
        ],
        "figure": None,
    },

    # ── easier · MRB-335 top-up ─────────────────────────────────────────
    {
        "id": "c6-07-e05",
        "band": "easier",
        "text": "What is a control, in an experiment like the five-flask "
                "bench?",
        "options": [
            {"text": "A trial run with the thing you are testing left out",
             "correct": True},
            {"text": "The flask that gives the fastest reaction, which every "
                     "other flask on the bench is then compared against to "
                     "see how close it comes",
             "correct": False,
             "why": "A control is the flask with NOTHING added. It shows what "
                    "would have happened anyway"},
            {"text": "The person who decides what goes in each flask",
             "correct": False,
             "why": "That is the everyday use of the word. In an experiment "
                    "it names a run"},
            {"text": "The tap that controls how much gas is collected",
             "correct": False,
             "why": "No tap is involved. The word names a comparison run"},
        ],
        "figure": None,
    },
    {
        "id": "c6-07-e06",
        "band": "easier",
        "text": "What is an enzyme?",
        "options": [
            {"text": "A chemical that living things produce in order to "
                     "destroy any catalyst that has found its way into the "
                     "body from outside",
             "correct": False,
             "why": "An enzyme IS a catalyst rather than something that "
                    "destroys one"},
            {"text": "A catalyst made by a living thing",
             "correct": True},
            {"text": "A substance that is used up as a reaction goes on",
             "correct": False,
             "why": "That would make it a reactant. An enzyme is not used "
                    "up"},
            {"text": "A poison that stops a catalyst working",
             "correct": False,
             "why": "That is what lead does to platinum. An enzyme is the "
                    "catalyst, not the poison"},
        ],
        "figure": None,
    },
    {
        "id": "c6-07-e07",
        "band": "easier",
        "text": "The flask with nothing added still gives a few bubbles over "
                "a minute. What does that show?",
        "options": [
            {"text": "That the flask was contaminated, since hydrogen "
                     "peroxide left entirely on its own is completely stable "
                     "and does not decompose at all",
             "correct": False,
             "why": "It decomposes on its own all the time. It is simply far "
                    "too slow to watch"},
            {"text": "That a catalyst is needed for the reaction to be "
                     "possible",
             "correct": False,
             "why": "The bubbles prove the opposite. It is possible without "
                    "one, and merely slow"},
            {"text": "That the reaction was always happening — just too "
                     "slowly to watch",
             "correct": True},
            {"text": "That the peroxide had gone off",
             "correct": False,
             "why": "Slow decomposition is what fresh peroxide does. Nothing "
                    "has gone wrong"},
        ],
        "figure": None,
    },
    {
        "id": "c6-07-e08",
        "band": "easier",
        "text": "What does it mean to say a catalyst has been poisoned?",
        "options": [
            {"text": "That it has been used up faster than expected",
             "correct": False,
             "why": "None of it has been used up. Open a dead converter and "
                    "all the platinum is still there"},
            {"text": "That it has become dangerous to handle",
             "correct": False,
             "why": "The word describes the catalyst's condition, not a "
                    "hazard to a person"},
            {"text": "That it has been turned into a different substance",
             "correct": False,
             "why": "The platinum is still platinum. What has changed is what "
                    "is sitting on top of it"},
            {"text": "That its surface has been coated by something, so the "
                     "reacting substances cannot reach it",
             "correct": True},
        ],
        "figure": None,
    },

    # ── standard · MRB-335 top-up ───────────────────────────────────────
    {
        "id": "c6-07-s05",
        "band": "standard",
        "text": "A catalyst is added to a reaction that takes an hour, and it "
                "now finishes in ten minutes. What has happened to the amount "
                "of product?",
        "options": [
            {"text": "Nothing has changed about it",
             "correct": True},
            {"text": "It has increased six times over, in the same "
                     "proportion as the time taken has come down",
             "correct": False,
             "why": "The time and the amount are not linked like that. The "
                    "amount is set by what you put in"},
            {"text": "It has gone down, because there was less time for the "
                     "reaction to make any",
             "correct": False,
             "why": "Both reactions ran to the end. The faster one simply got "
                    "there sooner"},
            {"text": "It cannot be known without weighing the catalyst",
             "correct": False,
             "why": "The catalyst weighs the same at the end as it did at the "
                    "start, and it is not part of the product"},
        ],
        "figure": None,
    },
    {
        "id": "c6-07-s06",
        "band": "standard",
        "text": "Fresh liver froths violently in hydrogen peroxide. Why does "
                "liver work at all?",
        "options": [
            {"text": "Because liver is acidic, and acid speeds up the "
                     "decomposition of hydrogen peroxide in the same way that "
                     "warming the flask would",
             "correct": False,
             "why": "The dilute-acid flask on the bench changed nothing at "
                    "all. What liver holds is an enzyme"},
            {"text": "Because it is full of catalase, an enzyme whose job is "
                     "to destroy hydrogen peroxide",
             "correct": True},
            {"text": "Because liver is warm, and warmth speeds reactions up",
             "correct": False,
             "why": "The liver on the bench is at room temperature like "
                    "everything else in the flask"},
            {"text": "Because liver dissolves in the peroxide and releases "
                     "oxygen",
             "correct": False,
             "why": "It does not dissolve, and the oxygen comes out of the "
                    "peroxide rather than out of the liver"},
        ],
        "figure": None,
    },
    {
        "id": "c6-07-s07",
        "band": "standard",
        "text": "Catalysts are deliberately made with an enormous surface "
                "area — a honeycomb, or a fine powder. What does that suggest "
                "about how they work?",
        "options": [
            {"text": "That a larger surface holds more catalyst, so more of "
                     "it is available to be used up before the converter "
                     "needs replacing",
             "correct": False,
             "why": "None of it is used up. Surface matters for a different "
                    "reason"},
            {"text": "That the catalyst has to be able to absorb the "
                     "reactants into itself",
             "correct": False,
             "why": "Nothing is taken inside. The reacting substances meet on "
                    "the outside"},
            {"text": "That the reaction happens on the surface, so more "
                     "surface means more places for it to happen",
             "correct": True},
            {"text": "That a catalyst works better when it is cold, and a "
                     "large surface loses heat faster",
             "correct": False,
             "why": "A converter works best once it is hot. The surface is "
                    "about area, not cooling"},
        ],
        "figure": None,
    },
    {
        "id": "c6-07-s08",
        "band": "standard",
        "text": "Why is it worth putting a few grams of platinum into every "
                "car exhaust, when platinum is one of the most expensive "
                "metals there is?",
        "options": [
            {"text": "Because platinum is sold cheaply in bulk to car makers, "
                     "so the price a jeweller pays for it is not the price a "
                     "factory pays at all",
             "correct": False,
             "why": "It is expensive to everybody. What makes it affordable "
                    "is that so little is needed"},
            {"text": "Because the exhaust would not work without a metal in "
                     "it",
             "correct": False,
             "why": "An exhaust pipe works without a converter. The converter "
                    "cleans what comes out of it"},
            {"text": "Because it is replaced at every service",
             "correct": False,
             "why": "It is not replaced at all under normal running. That is "
                    "the point"},
            {"text": "Because it is not used up, so a few grams last the "
                     "life of the car",
             "correct": True},
        ],
        "figure": None,
    },

    # ── harder · MRB-335 top-up ─────────────────────────────────────────
    {
        "id": "c6-07-h05",
        "band": "harder",
        "text": "A works finds a catalyst that lets its reaction run at "
                "200 °C instead of 400 °C, with the same yield. Where does the "
                "saving actually come from?",
        "options": [
            {"text": "From the fuel needed to hold the plant at temperature, "
                     "every hour it runs",
             "correct": True},
            {"text": "From the catalyst itself, which is recovered and sold "
                     "on at the end of each batch to pay for the next one",
             "correct": False,
             "why": "It is reused rather than sold, and the saving is far "
                    "larger than that. It is the fuel"},
            {"text": "From the extra product the catalyst produces",
             "correct": False,
             "why": "The yield is stated to be the same. A catalyst never "
                    "changes how much is made"},
            {"text": "From having to buy less of the starting material",
             "correct": False,
             "why": "The same amount goes in. What changes is the temperature "
                    "it has to be held at"},
        ],
        "figure": None,
    },
    {
        "id": "c6-07-h06",
        "band": "harder",
        "text": "Boiled liver does nothing in hydrogen peroxide, yet all the "
                "same substance is still in the flask. What does that tell you "
                "about enzymes?",
        "options": [
            {"text": "That an enzyme has to be alive to work, so anything "
                     "that kills the tissue it came from stops it working "
                     "too",
             "correct": False,
             "why": "An enzyme is a molecule and is not alive. It works "
                    "perfectly well in an extract"},
            {"text": "That the shape of the molecule is what does the work, "
                     "and heat wrecks the shape",
             "correct": True},
            {"text": "That the boiling used the enzyme up",
             "correct": False,
             "why": "Nothing was used up — it is all still there. What has "
                    "changed is its shape"},
            {"text": "That hydrogen peroxide cannot decompose in hot water",
             "correct": False,
             "why": "The flask is back at room temperature by the time it is "
                    "tested. It is the liver that changed"},
        ],
        "figure": None,
    },
    {
        "id": "c6-07-h07",
        "band": "harder",
        "text": "A student doubles the amount of manganese dioxide in the "
                "flask and runs the reaction again. What changes, and what "
                "does not?",
        "options": [
            {"text": "The reaction is faster and produces twice as much "
                     "oxygen, because twice as much catalyst is available to "
                     "take part in it",
             "correct": False,
             "why": "A catalyst takes no part in the products. The oxygen "
                    "comes out of the peroxide, and there is the same amount "
                    "of that"},
            {"text": "Nothing changes at all, because a catalyst works the "
                     "same however much of it there is",
             "correct": False,
             "why": "More catalyst means more surface for the reaction to "
                    "happen on, so it goes faster. What is unchanged is the "
                    "amount of oxygen"},
            {"text": "The reaction is faster still, and the final volume of "
                     "oxygen is the same",
             "correct": True},
            {"text": "The reaction is slower, because the extra powder gets "
                     "in the way",
             "correct": False,
             "why": "Extra surface speeds it up. Nothing about a catalyst "
                    "obstructs the reaction it is speeding"},
        ],
        "figure": None,
    },
    {
        "id": "c6-07-h08",
        "band": "harder",
        "text": "The ammonia process runs over iron, and the lesson calls the "
                "catalyst the difference between a reaction that is possible "
                "and one that is worth doing. What is that distinction?",
        "options": [
            {"text": "The reaction could not happen at all without the iron, "
                     "so the catalyst is what makes ammonia possible in the "
                     "first place",
             "correct": False,
             "why": "A catalyst never makes an impossible reaction happen. "
                    "This one is possible without the iron"},
            {"text": "The iron makes more ammonia from the same materials",
             "correct": False,
             "why": "The yield is unchanged. What the iron buys is the rate, "
                    "and with it a lower temperature"},
            {"text": "The iron is used up, and its cost is what makes the "
                     "process expensive",
             "correct": False,
             "why": "It is not used up at all — that is what makes a catalyst "
                    "affordable at industrial scale"},
            {"text": "Without the catalyst the reaction happens, but far too "
                     "slowly and hotly to pay for itself",
             "correct": True},
        ],
        "figure": None,
    },

    # ── MRB-338 expansion ───────────
    {
        "id": "c6-07-e09",
        "band": "easier",
        "text": "Hydrogen peroxide decomposes on its own. What two substances does it"
                " turn into?",
        "options": [
            {"text": "Hydrogen and oxygen", "correct": False,
             "why": "The hydrogen ends up in water rather than coming off as a gas "
                    "of its own."},
            {"text": "Water and oxygen", "correct": True},
            {"text": "Water and carbon dioxide", "correct": False,
             "why": "There is no carbon in hydrogen peroxide, so carbon dioxide "
                    "cannot be produced."},
            {"text": "Water and hydrogen", "correct": False,
             "why": "The gas given off relights a glowing splint, which hydrogen "
                    "does not do."},
        ],
        "figure": None,
    },
    {
        "id": "c6-07-e10",
        "band": "easier",
        "text": "What is the test for oxygen?",
        "options": [
            {"text": "It turns limewater milky", "correct": False,
             "why": "That is the test for carbon dioxide, and nothing else on a "
                    "school bench does it."},
            {"text": "It pops with a lit splint", "correct": False,
             "why": "The squeaky pop is the test for hydrogen, which is a different "
                    "gas altogether."},
            {"text": "It relights a glowing splint", "correct": True},
            {"text": "It puts out a lit splint", "correct": False,
             "why": "Almost any gas that is not oxygen puts a splint out, so that "
                    "identifies nothing."},
        ],
        "figure": None,
    },
    {
        "id": "c6-07-e11",
        "band": "easier",
        "text": "Which of the five flasks on the bench held a biological catalyst?",
        "options": [
            {"text": "The one with sand", "correct": False,
             "why": "Sand is not alive and is not a catalyst at all — it changed "
                    "nothing."},
            {"text": "The one with dilute acid", "correct": False,
             "why": "The acid is not alive and made no difference to the speed of "
                    "the reaction."},
            {"text": "The one with manganese dioxide", "correct": False,
             "why": "Manganese dioxide is a catalyst, but it is a mineral rather "
                    "than something from a living thing."},
            {"text": "The one with fresh liver", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c6-07-e12",
        "band": "easier",
        "text": "Does adding a catalyst change what a reaction produces?",
        "options": [
            {"text": "Yes, it always adds itself to the products", "correct": False,
             "why": "It takes no part in the products and can be filtered out "
                    "unchanged at the end."},
            {"text": "Yes, it produces an extra substance alongside the usual ones", "correct": False,
             "why": "The same two products come out of the flask whether a catalyst "
                    "is present or not."},
            {"text": "No", "correct": True},
            {"text": "Only if enough of it is added to the flask", "correct": False,
             "why": "More catalyst goes faster still, but the products are the same "
                    "at any amount."},
        ],
        "figure": None,
    },
    {
        "id": "c6-07-e13",
        "band": "easier",
        "text": "Which expensive metals are used inside a catalytic converter?",
        "options": [
            {"text": "Platinum and rhodium", "correct": True},
            {"text": "Gold and silver together", "correct": False,
             "why": "Both are expensive, but neither is the metal used to catalyse "
                    "an exhaust."},
            {"text": "Copper and zinc", "correct": False,
             "why": "These are cheap everyday metals and are not what a converter is"
                    " built from."},
            {"text": "Lead and tin", "correct": False,
             "why": "Lead is the substance that destroys a converter by coating its "
                    "surface."},
        ],
        "figure": None,
    },
    {
        "id": "c6-07-e14",
        "band": "easier",
        "text": "Which enzyme in liver breaks hydrogen peroxide down?",
        "options": [
            {"text": "Amylase", "correct": False,
             "why": "Amylase works on starch and has nothing to do with hydrogen "
                    "peroxide."},
            {"text": "Catalase", "correct": True},
            {"text": "Protease", "correct": False,
             "why": "Protease works on protein. The peroxide enzyme is a different "
                    "one."},
            {"text": "Lipase", "correct": False,
             "why": "Lipase works on fat, which is a different job again."},
        ],
        "figure": None,
    },
    {
        "id": "c6-07-e15",
        "band": "easier",
        "text": "A bottle of hydrogen peroxide is left alone with nothing added. "
                "Roughly how long does it take to decompose?",
        "options": [
            {"text": "About a second", "correct": False,
             "why": "That is what it takes with a catalyst in the flask, not on its "
                    "own."},
            {"text": "About a minute", "correct": False,
             "why": "A minute is what a catalysed flask needs. Without one the "
                    "change is far too slow to watch."},
            {"text": "About an hour", "correct": False,
             "why": "Even an hour would be visible. The uncatalysed reaction gives "
                    "only a few bubbles in that time."},
            {"text": "About a year", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c6-07-e16",
        "band": "easier",
        "text": "A bought bottle of hydrogen peroxide is kept slightly acidic. Why?",
        "options": [
            {"text": "So that it does not decompose on the shelf", "correct": True},
            {"text": "So that it decomposes faster when it is needed", "correct": False,
             "why": "Acid does not speed this reaction up. If anything it holds it "
                    "back, which is the point."},
            {"text": "So that it can be used to clean metal", "correct": False,
             "why": "The acid is there to protect the peroxide, not to give the "
                    "bottle a second use."},
            {"text": "So that it tastes sharp and is not swallowed", "correct": False,
             "why": "Nothing about the bottle depends on taste, and it is not made "
                    "sharp as a warning."},
        ],
        "figure": None,
    },
    {
        "id": "c6-07-e17",
        "band": "easier",
        "text": "A catalytic converter turns carbon monoxide and unburnt fuel into "
                "what?",
        "options": [
            {"text": "Hydrogen and nitrogen", "correct": False,
             "why": "Neither of these is what leaves a converter, and hydrogen is "
                    "not made in an exhaust."},
            {"text": "Carbon dioxide and water", "correct": True},
            {"text": "Oxygen and carbon", "correct": False,
             "why": "Solid carbon would clog the honeycomb at once. The carbon "
                    "leaves as a gas."},
            {"text": "Nothing — it simply traps them", "correct": False,
             "why": "A converter reacts them rather than collecting them, which is "
                    "why it never fills up."},
        ],
        "figure": None,
    },
    {
        "id": "c6-07-e18",
        "band": "easier",
        "text": "At roughly what temperature do the enzymes in your body do their "
                "work?",
        "options": [
            {"text": "About 100 °C", "correct": False,
             "why": "That is boiling water, and heat at that level destroys an "
                    "enzyme's shape."},
            {"text": "About 250 °C", "correct": False,
             "why": "That is an industrial reaction vessel, not a living body."},
            {"text": "About 37 °C", "correct": True},
            {"text": "About 0 °C", "correct": False,
             "why": "That is freezing point. Your body is held far above it for "
                    "exactly this reason."},
        ],
        "figure": None,
    },
    {
        "id": "c6-07-e19",
        "band": "easier",
        "text": "Why is recovered manganese dioxide not handled with bare hands?",
        "options": [
            {"text": "Because it is harmful if it is swallowed", "correct": True},
            {"text": "Because it is hot enough to burn after the reaction", "correct": False,
             "why": "The flask warms a little, but the powder is not the hazard "
                    "because of heat."},
            {"text": "Because it stains the skin permanently black", "correct": False,
             "why": "It marks the skin but washes off. The reason for care is that "
                    "it is harmful to swallow."},
            {"text": "Because it catches fire when it dries in air", "correct": False,
             "why": "It is dried routinely on a filter paper and does nothing of the"
                    " kind."},
        ],
        "figure": None,
    },
    {
        "id": "c6-07-e20",
        "band": "easier",
        "text": "Why is the liver flask stood in a tray?",
        "options": [
            {"text": "Because the flask becomes too hot to hold safely", "correct": False,
             "why": "The flask warms a little, but a tray is there for the liquid "
                    "rather than the heat."},
            {"text": "Because it froths over the top", "correct": True},
            {"text": "Because the liver would roll out of an open flask", "correct": False,
             "why": "The liver stays in the liquid. It is the foam that leaves the "
                    "flask."},
            {"text": "Because the tray keeps the whole reaction at body temperature "
                      "all along", "correct": False,
             "why": "A plastic tray warms nothing. Its job is to catch what comes "
                    "over the top."},
        ],
        "figure": None,
    },
    {
        "id": "c6-07-e21",
        "band": "easier",
        "text": "What does hydrogen peroxide at the strength used on this bench do to"
                " skin?",
        "options": [
            {"text": "Nothing at all, since it is mostly water", "correct": False,
             "why": "It is concentrated enough to do real damage, which is why "
                    "gloves and goggles are worn."},
            {"text": "Stains it brown", "correct": False,
             "why": "It takes colour out rather than putting it in."},
            {"text": "Bleaches it", "correct": True},
            {"text": "Makes it fizz harmlessly for a moment", "correct": False,
             "why": "Skin does contain catalase, but the damage it does is not "
                    "harmless."},
        ],
        "figure": None,
    },
    {
        "id": "c6-07-s09",
        "band": "standard",
        "text": "Why is one flask run with nothing added to it at all?",
        "options": [
            {"text": "To use up the hydrogen peroxide left over, so that none of it "
                      "is wasted at the end of the lesson", "correct": False,
             "why": "It is run for the reading it gives, not to dispose of anything."},
            {"text": "To warm the apparatus up before the real trials are started on "
                      "it", "correct": False,
             "why": "Nothing needs warming, and this flask gives a measurement of "
                    "its own."},
            {"text": "To check that the gas syringe is working properly before "
                      "anything else at all is added to it", "correct": False,
             "why": "The syringe is checked separately. This flask answers a "
                    "question about the reaction."},
            {"text": "To show what the reaction does on its own, so the others have "
                      "something to be compared with", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c6-07-s10",
        "band": "standard",
        "text": "A glowing splint is held in the gas coming off each flask in turn, "
                "once each has been left long enough. Which relight it?",
        "options": [
            {"text": "Only the two with catalysts, since the others make a different "
                      "gas", "correct": False,
             "why": "Every flask makes oxygen. A catalyst does not change what is "
                    "produced."},
            {"text": "Only the flask with nothing added, since a catalyst uses the "
                      "oxygen up", "correct": False,
             "why": "A catalyst consumes nothing. All five flasks end up with the "
                    "same gas."},
            {"text": "All of them, because every flask produces oxygen", "correct": True},
            {"text": "None of them, because the oxygen is too dilute to relight "
                      "anything", "correct": False,
             "why": "The gas collected is oxygen, and it relights a glowing splint "
                    "readily."},
        ],
        "figure": None,
    },
    {
        "id": "c6-07-s11",
        "band": "standard",
        "text": "1.00 g of manganese dioxide is added and 0.98 g is recovered. A "
                "student says it was partly used up. Evaluate.",
        "options": [
            {"text": "Correct, since any loss of mass shows some of it has been "
                      "consumed", "correct": False,
             "why": "A catalyst is not consumed. Losses on glassware and filter "
                    "paper explain a small shortfall."},
            {"text": "Correct, since a catalyst is used up slowly over many runs", "correct": False,
             "why": "Nothing is consumed slowly either. Catalysts fail by being "
                    "blocked, not by wearing away."},
            {"text": "Wrong, since a heavier recovery would have proved the opposite "
                      "point instead of this one", "correct": False,
             "why": "Extra mass would point to something left on the powder, which "
                    "does not settle the question either."},
            {"text": "Wrong — a little is lost on the paper and the glass, and a "
                      "catalyst is not consumed", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c6-07-s12",
        "band": "standard",
        "text": "The flask with dilute acid gave the same reading as the flask with "
                "nothing in it. Why is that a result rather than a failure?",
        "options": [
            {"text": "Because it shows the acid was far too dilute, so a stronger one"
                      " would have worked instead", "correct": False,
             "why": "Acid does not speed this reaction up at any strength. The flask"
                    " answers a different question."},
            {"text": "Because it was run to test whether adding a liquid is enough, "
                      "and the answer is no", "correct": True},
            {"text": "Because a flask that changes nothing can always be left out of "
                      "the results", "correct": False,
             "why": "Leaving it out would remove the evidence that adding something "
                    "is not enough."},
            {"text": "Because it proves the hydrogen peroxide had already gone off "
                      "before the lesson", "correct": False,
             "why": "The other flasks used the same peroxide and reacted vigorously,"
                    " so it had not gone off."},
        ],
        "figure": None,
    },
    {
        "id": "c6-07-s13",
        "band": "standard",
        "text": "Manganese dioxide and fresh liver are each left until the reaction "
                "is completely finished. Compare the oxygen collected.",
        "options": [
            {"text": "More from the liver, because it frothed faster during the run", "correct": False,
             "why": "Frothing faster means finishing sooner, not making more."},
            {"text": "More from the manganese dioxide, because a mineral catalyst "
                      "lasts longer than an enzyme", "correct": False,
             "why": "Neither is consumed, and the total is set by the peroxide "
                    "rather than by the catalyst."},
            {"text": "The same from both — only the time taken differs", "correct": True},
            {"text": "Less from both than from the flask with nothing added at all", "correct": False,
             "why": "The uncatalysed flask reaches the same total in the end. It "
                    "simply takes about a year."},
        ],
        "figure": None,
    },
    {
        "id": "c6-07-s14",
        "band": "standard",
        "text": "The manganese dioxide is filtered out, dried, and used again on "
                "fresh hydrogen peroxide the next day. Predict what happens.",
        "options": [
            {"text": "Nothing, because a catalyst only works once", "correct": False,
             "why": "It is unchanged, so there is no reason for it to have stopped "
                    "working."},
            {"text": "It works, but only about half as fast as the first time", "correct": False,
             "why": "It comes back weighing the same and in the same state, so it "
                    "works as before."},
            {"text": "It reacts with the fresh peroxide and dissolves away", "correct": False,
             "why": "It does not react with the peroxide at all. That is what being "
                    "a catalyst means."},
            {"text": "It works exactly as it did the first time", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c6-07-s15",
        "band": "standard",
        "text": "The volumes reported for the five flasks are described as "
                "illustrative rather than measured. Why does that matter?",
        "options": [
            {"text": "Because they are invented, so nothing can be concluded", "correct": False,
             "why": "They represent what the flasks really do relative to one "
                    "another, which is what the bench is for."},
            {"text": "Because they show how the flasks compare, not what one "
                      "particular run would give", "correct": True},
            {"text": "Because a real run would give the same numbers every time", "correct": False,
             "why": "Real runs vary. That is part of why a single set of figures is "
                    "not quoted as measurement."},
            {"text": "Because only the catalysed flasks were measured", "correct": False,
             "why": "The note applies to all five. None of them is offered as a "
                    "single measured result."},
        ],
        "figure": None,
    },
    {
        "id": "c6-07-s16",
        "band": "standard",
        "text": "Two of the five flasks change nothing: one holds a solid and one "
                "holds a liquid. Why are both needed?",
        "options": [
            {"text": "Because two flasks that do nothing make the result twice as "
                      "reliable", "correct": False,
             "why": "They are not repeats of one another. Each closes a different "
                    "escape route."},
            {"text": "Because one is a check on the apparatus and the other one is on"
                      " the peroxide", "correct": False,
             "why": "Both are checks on the same idea: that adding something is not "
                    "the same as catalysing it."},
            {"text": "Because the solid one is the real control and the liquid one is"
                      " not", "correct": False,
             "why": "Both do the same work, and the liquid one catches the answer "
                    "most people expect."},
            {"text": "Because one shows a solid is not enough and the other shows a "
                      "liquid is not enough", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c6-07-s17",
        "band": "standard",
        "text": "A student describes a catalyst as a reactant that is put back at the"
                " end. Correct that.",
        "options": [
            {"text": "It is never consumed in the first place, so there is nothing to"
                      " put back", "correct": True},
            {"text": "It is consumed and then remade by the reaction itself, which is"
                      " exactly why the mass matches", "correct": False,
             "why": "Nothing remakes it. It was never taken apart, which is why the "
                    "mass matches."},
            {"text": "It is a product rather than a reactant, since it comes out at "
                      "the end", "correct": False,
             "why": "It was there at the start as well, so it is neither a reactant "
                    "nor a product."},
            {"text": "It is a reactant, but only a very small part of it is ever "
                      "actually used", "correct": False,
             "why": "None of it is used. Filter it out and every milligram is still "
                    "there."},
        ],
        "figure": None,
    },
    {
        "id": "c6-07-s18",
        "band": "standard",
        "text": "Explain how enzymes let a body run reactions at 37 °C that would "
                "otherwise be far too slow.",
        "options": [
            {"text": "They raise the temperature inside the cell to the level the "
                      "reaction needs", "correct": False,
             "why": "The cell stays at body temperature. The enzyme works without "
                    "heating anything."},
            {"text": "They make reactions possible that could not otherwise happen at"
                      " any temperature at all", "correct": False,
             "why": "A catalyst cannot create a reaction. These reactions are "
                    "possible already, just slow."},
            {"text": "They speed the reaction up, so it runs usefully fast at body "
                      "temperature", "correct": True},
            {"text": "They supply the energy the reaction needs, which is why food is"
                      " required", "correct": False,
             "why": "Food supplies energy, but the enzyme itself supplies none. It "
                    "changes the rate."},
        ],
        "figure": None,
    },
    {
        "id": "c6-07-s19",
        "band": "standard",
        "text": "A spatula of manganese dioxide is stirred into a flask of pure "
                "water. Predict what happens.",
        "options": [
            {"text": "Oxygen is given off, because the powder makes oxygen wherever "
                      "it is put", "correct": False,
             "why": "The oxygen came out of the hydrogen peroxide. The powder "
                    "produces nothing itself."},
            {"text": "The water decomposes slowly into hydrogen and oxygen", "correct": False,
             "why": "Water does not decompose in a flask on a bench, catalyst or no "
                    "catalyst."},
            {"text": "The powder dissolves and the water turns black", "correct": False,
             "why": "It is insoluble, and it settles to the bottom leaving the water"
                    " clear."},
            {"text": "Nothing, because there is no reaction for it to speed up", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c6-07-s20",
        "band": "standard",
        "text": "The bench compares the flasks after 60 seconds rather than waiting "
                "for each to finish. Why?",
        "options": [
            {"text": "Because after 60 seconds every flask has finished completely", "correct": False,
             "why": "The uncatalysed flasks are barely started at a minute. They "
                    "take far longer."},
            {"text": "Because a reading taken later on would be far less accurate "
                      "than one taken early in the run itself", "correct": False,
             "why": "A later reading is just as accurate. It simply answers a "
                    "different question."},
            {"text": "Because waiting for the slowest of the flasks to finish would "
                      "take about a year of lessons in all", "correct": False,
             "why": "True of the slow ones, but the real reason is what the "
                    "comparison is meant to show."},
            {"text": "Because left long enough every flask gives the same total, and "
                      "it is the speed being compared", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c6-07-h09",
        "band": "harder",
        "text": "A student claims the acid flask proves acid slows the reaction down."
                " Given that it matched the flask with nothing added, evaluate that.",
        "options": [
            {"text": "Correct, because any flask that is not faster than the control "
                      "must therefore be slower than it", "correct": False,
             "why": "A flask can match the control exactly, which is what this one "
                    "did."},
            {"text": "Correct, because acid is known to hold this reaction back, and "
                      "the bench has now measured it here", "correct": False,
             "why": "The bench measured no difference. A claim about slowing needs a"
                    " reading below the control."},
            {"text": "Wrong, because it matched the control, so on this bench it "
                      "changed nothing that could be measured", "correct": True},
            {"text": "Wrong, because the acid was recovered completely unchanged, and"
                      " that makes it a catalyst after all", "correct": False,
             "why": "Coming back unchanged is not enough. It has to be faster as "
                    "well, and it was not."},
        ],
        "figure": None,
    },
    {
        "id": "c6-07-h10",
        "band": "harder",
        "text": "Manganese dioxide is a black powder that works and sand is a pale "
                "powder that does not. A student concludes black powders are "
                "catalysts. Evaluate.",
        "options": [
            {"text": "Sound, because the only difference between the two flasks was "
                      "the colour of the powder", "correct": False,
             "why": "The two powders are different substances. Colour is the least "
                    "important thing about them."},
            {"text": "Sound, because a dark powder absorbs more energy and so drives "
                      "the reaction faster", "correct": False,
             "why": "Nothing here depends on absorbing light, and the flask works "
                    "just as well in the dark."},
            {"text": "Unsound, because copper oxide is black as well and is not a "
                      "catalyst for this reaction", "correct": True},
            {"text": "Unsound, because sand is not really a powder and so the "
                      "comparison was never fair", "correct": False,
             "why": "Sand is a powder with a large surface, which is exactly why it "
                    "is the control chosen."},
        ],
        "figure": None,
    },
    {
        "id": "c6-07-h11",
        "band": "harder",
        "text": "Compare a catalyst with a reactant, in terms of the mass at the end "
                "and the amount of product made.",
        "options": [
            {"text": "Both of them are consumed, but only the reactant decides how "
                      "much of the product there is at the end of it", "correct": False,
             "why": "A catalyst is not consumed at all, which is the first half of "
                    "the difference."},
            {"text": "Neither of them is consumed, and both of them decide how much "
                      "of the product is made in the end", "correct": False,
             "why": "A reactant certainly is consumed, and it is what sets the "
                    "amount."},
            {"text": "A reactant is consumed and sets how much product there is; a "
                      "catalyst is not, and sets only the time", "correct": True},
            {"text": "A catalyst is consumed and sets the time taken; a reactant is "
                      "not consumed and sets the amount made", "correct": False,
             "why": "This has both halves the wrong way round, and a balance settles"
                    " it in a single weighing."},
        ],
        "figure": None,
    },
    {
        "id": "c6-07-h12",
        "band": "harder",
        "text": "Fresh liver froths faster than manganese dioxide on this bench. Does"
                " that make catalase the better choice for an industrial process?",
        "options": [
            {"text": "Yes, because the faster catalyst is always the better one to "
                      "choose", "correct": False,
             "why": "Speed on a cold bench is one factor. Industrial conditions "
                    "decide the rest."},
            {"text": "Yes, because a catalyst taken from a living thing is renewable "
                      "and so costs nothing", "correct": False,
             "why": "Cost is not the objection. Heat is, and an enzyme cannot "
                    "survive it."},
            {"text": "No, because an enzyme costs more than a mineral catalyst does "
                      "to obtain", "correct": False,
             "why": "Price is not the reason. Many industrial processes run hot, and"
                    " heat wrecks an enzyme's shape."},
            {"text": "No, because heat destroys an enzyme's shape and many industrial"
                      " reactions run hot", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c6-07-h13",
        "band": "harder",
        "text": "Hydrogen peroxide decomposes on its own even with nothing added to "
                "it. Why does that matter when calling manganese dioxide a catalyst?",
        "options": [
            {"text": "Because it shows the reaction was always possible, so the "
                      "powder changed only the rate", "correct": True},
            {"text": "Because it shows the powder must have been present in the "
                      "bottle all along", "correct": False,
             "why": "The sealed bottle contains no manganese dioxide. It decomposes "
                    "without any."},
            {"text": "Because it shows how long a catalyst takes to be used up "
                      "completely", "correct": False,
             "why": "Nothing is used up at all. The catalyst weighs the same after "
                    "every run."},
            {"text": "Because it shows the powder started a reaction that could not "
                      "otherwise occur", "correct": False,
             "why": "It was already happening, just too slowly to watch. The slow "
                    "decomposition is what tells you so."},
        ],
        "figure": None,
    },
    {
        "id": "c6-07-h14",
        "band": "harder",
        "text": "A student suggests warming the flask instead of adding a catalyst. "
                "Compare the two ways of speeding the reaction up.",
        "options": [
            {"text": "Warming gives a greater volume of oxygen in total, while a "
                      "catalyst only changes the time taken", "correct": False,
             "why": "Neither changes the total. That is set by how much peroxide "
                    "there is."},
            {"text": "Only the catalyst works, because warming has no effect on the "
                      "speed of a reaction", "correct": False,
             "why": "Warming speeds reactions up in general. The comparison is about"
                    " what each one costs."},
            {"text": "Both are faster, but warming costs fuel every time while the "
                      "catalyst is recovered and reused", "correct": True},
            {"text": "Both are faster, and both are used up, so each of them has to "
                      "be replaced before the next run", "correct": False,
             "why": "A catalyst is not used up. It is filtered out and used again."},
        ],
        "figure": None,
    },
    {
        "id": "c6-07-h15",
        "band": "harder",
        "text": "After 60 seconds the five flasks read 2, 2, 48, 55 and 2 cm³ of "
                "oxygen. What do the three readings of 2 cm³ support?",
        "options": [
            {"text": "That three of the five flasks contained no hydrogen peroxide at"
                      " all", "correct": False,
             "why": "All five held the same peroxide. That is what makes the "
                    "comparison fair."},
            {"text": "That three of the five additions changed nothing", "correct": True},
            {"text": "That three of the five flasks were leaking, so their readings "
                      "cannot be used", "correct": False,
             "why": "A reading matching the control is exactly what a flask with no "
                    "catalyst should give."},
            {"text": "That three of the five substances were used up before the "
                      "minute was over", "correct": False,
             "why": "The sand and the acid are both still there at the end. Neither "
                    "was consumed."},
        ],
        "figure": None,
    },
    {
        "id": "c6-07-h16",
        "band": "harder",
        "text": "A student says that because a catalyst is never used up, one spatula"
                " of it could run a factory for ever. Evaluate.",
        "options": [
            {"text": "Correct, because nothing that is not consumed can ever stop "
                      "working", "correct": False,
             "why": "It can stop working without being consumed, which is the whole "
                    "distinction."},
            {"text": "Correct, because a catalyst is recovered at the end of every "
                      "single run it takes part in", "correct": False,
             "why": "Recovery is real, but it is not the only thing that can happen "
                    "to a catalyst over years."},
            {"text": "Wrong, because a catalyst is slowly consumed over thousands of "
                      "runs", "correct": False,
             "why": "It is not consumed at all. A balance says so after every run."},
            {"text": "Wrong, because it can be poisoned, clogged or damaged by heat "
                      "without being consumed", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c6-07-e22",
        "band": "easier",
        "text": "Five flasks are each given the same amount of hydrogen peroxide, and"
                " only the substance stirred into them is changed. What is an"
                " experiment arranged like that called?",
        "options": [
            {"text": "A fair test", "correct": True},
            {"text": "A repeat reading", "correct": False,
             "why": "A repeat is the same trial run a second time; here five "
                    "different additions are being compared once each."},
            {"text": "An estimate", "correct": False,
             "why": "An estimate is a judgement made without measuring, and every "
                    "flask here is measured."},
            {"text": "A prediction", "correct": False,
             "why": "A prediction is what you expect before the run, not the way "
                    "the run itself is arranged."},
        ],
        "figure": None,
    },
    {
        "id": "c6-07-e23",
        "band": "easier",
        "text": "The recovered manganese dioxide is left to dry before it goes back"
                " on the balance. Why?",
        "options": [
            {"text": "Because warming the powder up makes it work better in the next run",
             "correct": False,
             "why": "Drying is not warming, and a catalyst does not need "
                    "preparing before it is reused."},
            {"text": "Because the balance cannot weigh a black powder wet",
             "correct": False,
             "why": "A balance weighs whatever is put on it; the trouble is what "
                    "else is being weighed with the powder."},
            {"text": "Because any liquid left on it would be weighed as well",
             "correct": True},
            {"text": "Because drying turns it back into a catalyst again",
             "correct": False,
             "why": "It never stopped being one, so there is nothing to turn it "
                    "back into."},
        ],
        "figure": None,
    },
    {
        "id": "c6-07-e24",
        "band": "easier",
        "text": "Goggles are worn for the whole of this practical. What is the reason"
                " that matters most here?",
        "options": [
            {"text": "The black powder could splash up and stain a school shirt badly",
             "correct": False,
             "why": "A stained shirt is a nuisance, not the hazard goggles are "
                    "worn against."},
            {"text": "Hydrogen peroxide would damage an eye it splashed into",
             "correct": True},
            {"text": "The oxygen given off is poisonous to breathe",
             "correct": False,
             "why": "Oxygen is the gas you are breathing now, and goggles would "
                    "not help with a gas in any case."},
            {"text": "The flask becomes cold enough to hurt bare skin",
             "correct": False,
             "why": "The flask does not become dangerously cold, and goggles "
                    "protect eyes rather than hands."},
        ],
        "figure": None,
    },
    {
        "id": "c6-07-e25",
        "band": "easier",
        "text": "On the five-flask bench, what has to be the same in every flask if"
                " the readings are to be worth comparing?",
        "options": [
            {"text": "The colour of the substance that is stirred into each flask", "correct": False,
             "why": "Colour has nothing to do with it: a black powder works and a "
                    "pale one does not."},
            {"text": "The mass of the substance stirred in", "correct": False,
             "why": "That is the thing being varied from flask to flask, so it is "
                    "the one quantity that cannot be fixed."},
            {"text": "The length of the delivery tube only", "correct": False,
             "why": "The tube matters far less than what is in the flask, and on "
                    "its own it settles nothing."},
            {"text": "The volume and strength of the hydrogen peroxide",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c6-07-e26",
        "band": "easier",
        "text": "Five flasks are run. How many of the five substances stirred in turn"
                " out to be catalysts?",
        "options": [
            {"text": "One", "correct": False,
             "why": "One flask is the control with nothing added; of the four "
                    "substances tried, more than one speeds the reaction up."},
            {"text": "Four", "correct": False,
             "why": "Only one flask is left untouched, and two of the remaining "
                    "four change nothing at all."},
            {"text": "Two", "correct": True},
            {"text": "Five", "correct": False,
             "why": "One flask has nothing added to it at all, so five is not "
                    "even possible."},
        ],
        "figure": None,
    },
    {
        "id": "c6-07-e27",
        "band": "easier",
        "text": "The manganese dioxide can be separated from the liquid at the end by"
                " pouring the mixture through filter paper. What does that tell you"
                " about the powder?",
        "options": [
            {"text": "It does not dissolve in the liquid", "correct": True},
            {"text": "It has reacted with the hydrogen peroxide",
             "correct": False,
             "why": "A substance that had reacted would no longer be there to "
                    "collect on the paper."},
            {"text": "It dissolves and then comes back out", "correct": False,
             "why": "Anything dissolved would run straight through the paper with "
                    "the liquid."},
            {"text": "It is a liquid at room temperature", "correct": False,
             "why": "It is stirred in as a solid powder and is collected as one."},
        ],
        "figure": None,
    },
    {
        "id": "c6-07-e28",
        "band": "easier",
        "text": "Manganese dioxide is not written into the word equation for the"
                " reaction it speeds up. Why not?",
        "options": [
            {"text": "Because word equations only ever have two substances in them",
             "correct": False,
             "why": "Word equations carry as many substances as the reaction "
                    "needs, on either side of the arrow."},
            {"text": "Because it is used up and so cannot be shown", "correct": False,
             "why": "It is not used up; every milligram is still there at the end."},
            {"text": "Because its name is too long to fit on the line",
             "correct": False,
             "why": "Length has nothing to do with what goes into an equation."},
            {"text": "Because it is neither a reactant nor a product",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c6-07-e29",
        "band": "easier",
        "text": "Living cells make catalase. What is that enzyme there to do?",
        "options": [
            {"text": "Make hydrogen peroxide for the cell to use", "correct": False,
             "why": "It works on hydrogen peroxide rather than making it."},
            {"text": "Destroy hydrogen peroxide before it can harm the cell",
             "correct": True},
            {"text": "Store hydrogen peroxide safely inside the cell until it is needed",
             "correct": False,
             "why": "Nothing is stored: the peroxide is broken down as soon as it "
                    "meets the enzyme."},
            {"text": "Turn hydrogen peroxide into a stronger acid", "correct": False,
             "why": "No acid is made here, and acidity is not what the enzyme "
                    "changes."},
        ],
        "figure": None,
    },
    {
        "id": "c6-07-e30",
        "band": "easier",
        "text": "How much of what the chemical industry manufactures is made using a"
                " catalyst at some stage?",
        "options": [
            {"text": "Almost none of it", "correct": False,
             "why": "Catalysts are used across the industry precisely because "
                    "they save fuel on a scale nothing else can."},
            {"text": "About one process in twenty", "correct": False,
             "why": "That is far too few; catalysed steps are the rule rather "
                    "than the exception."},
            {"text": "The great majority of it", "correct": True},
            {"text": "Only reactions that involve a gas", "correct": False,
             "why": "Catalysts are used on reactions in solution and on solids "
                    "as well as on gases."},
        ],
        "figure": None,
    },
    {
        "id": "c6-07-e31",
        "band": "easier",
        "text": "A reaction cannot happen at all between two substances. What would"
                " adding a catalyst do?",
        "options": [
            {"text": "Nothing, because there is no reaction to speed up",
             "correct": True},
            {"text": "Start it off slowly, then let it run on its own",
             "correct": False,
             "why": "A catalyst changes the time a possible reaction takes; it "
                    "does not start an impossible one."},
            {"text": "Make it happen, as long as enough catalyst is added",
             "correct": False,
             "why": "Adding more of a catalyst never makes an impossible reaction "
                    "become possible."},
            {"text": "Make it happen, but only while the catalyst is present",
             "correct": False,
             "why": "A catalyst does not supply what a reaction lacks, however "
                    "long it stays in the flask."},
        ],
        "figure": None,
    },
    {
        "id": "c6-07-e32",
        "band": "easier",
        "text": "An enzyme is heated well above the temperature it normally works at."
                " What happens to it?",
        "options": [
            {"text": "It works faster and faster with every degree", "correct": False,
             "why": "Warming speeds most reactions up, but an enzyme is wrecked "
                    "once it is heated far enough."},
            {"text": "It turns into an ordinary chemical catalyst", "correct": False,
             "why": "Nothing turns into anything; the enzyme simply stops "
                    "working."},
            {"text": "It is used up, leaving nothing behind", "correct": False,
             "why": "The substance is all still in the flask afterwards — it just "
                    "no longer does anything."},
            {"text": "Its shape is wrecked and it stops working", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c6-07-s21",
        "band": "standard",
        "text": "A student stirs the powder in, watches the frothing start, and only"
                " then pushes the bung and delivery tube into the flask. Predict the"
                " effect on the volume of oxygen recorded.",
        "options": [
            {"text": "It will be higher, because the reaction had a head start",
             "correct": False,
             "why": "Gas made before the bung went in never reached the syringe, "
                    "so nothing was gained."},
            {"text": "It will be lower, because the first gas escaped into the room",
             "correct": True},
            {"text": "It will be unchanged, because the same peroxide is in the "
                      "flask", "correct": False,
             "why": "The same peroxide reacts, but only the gas made after the "
                    "bung is in gets counted."},
            {"text": "It will be lower, because the powder stops working once it "
                      "is wet", "correct": False,
             "why": "The powder keeps working throughout; the loss is gas, not "
                    "catalyst."},
        ],
        "figure": None,
    },
    {
        "id": "c6-07-s22",
        "band": "standard",
        "text": "Two students run the manganese dioxide flask under the same"
                " conditions and record 45 cm³ and 51 cm³. What should they do"
                " before quoting a figure?",
        "options": [
            {"text": "Quote the larger one, since gas is easily lost",
             "correct": False,
             "why": "Choosing the reading you prefer is not a measurement, and "
                    "loss has not been shown to have happened."},
            {"text": "Quote the smaller one, since it is the safer claim",
             "correct": False,
             "why": "Caution is not a reason to throw away a reading that is just "
                    "as good."},
            {"text": "Throw both away and change the mass of powder",
             "correct": False,
             "why": "Changing the powder makes it a different trial rather than a "
                    "better measurement of this one."},
            {"text": "Run it again and take a mean of the readings",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c6-07-s23",
        "band": "standard",
        "text": "Manganese dioxide speeds up the decomposition of hydrogen peroxide."
                " A student stirs a spatula of it into magnesium and dilute"
                " hydrochloric acid, expecting the same effect. Predict what happens.",
        "options": [
            {"text": "The magnesium reacts at about the speed it would anyway",
             "correct": True},
            {"text": "The magnesium reacts far faster, as the peroxide did",
             "correct": False,
             "why": "A catalyst is not a general accelerator; one that works on "
                    "one reaction need not touch another."},
            {"text": "The magnesium stops reacting while the powder is present",
             "correct": False,
             "why": "The powder does not block the acid from reaching the metal."},
            {"text": "A different salt is made, because the powder joins in",
             "correct": False,
             "why": "The salt is set by the acid used, and the powder takes no "
                    "part in the reaction."},
        ],
        "figure": None,
    },
    {
        "id": "c6-07-s24",
        "band": "standard",
        "text": "The same mass of manganese dioxide is used twice: once as a single"
                " lump and once ground to a fine powder. Which flask froths sooner,"
                " and why?",
        "options": [
            {"text": "The lump, because all of the mass is in one place",
             "correct": False,
             "why": "Keeping the mass together hides most of it inside, where the "
                    "liquid cannot reach."},
            {"text": "Neither, because the mass of catalyst is the same",
             "correct": False,
             "why": "Mass is not what the liquid meets; the exposed outside is."},
            {"text": "The powder, because far more of it is in contact with the "
                      "liquid", "correct": True},
            {"text": "The powder, because grinding it makes each particle work "
                      "harder", "correct": False,
             "why": "Grinding changes nothing about a particle itself, only how "
                    "many of them the liquid can reach."},
        ],
        "figure": None,
    },
    {
        "id": "c6-07-s25",
        "band": "standard",
        "text": "In the same 60 seconds, the flask with the black powder gives 48 cm³"
                " of oxygen and the untouched flask gives 2 cm³. How many times as"
                " much oxygen did the catalysed flask make?",
        "options": [
            {"text": "46 times as much", "correct": False,
             "why": "46 is the difference between the two readings, not how many "
                    "times bigger one is than the other."},
            {"text": "24 times as much", "correct": True},
            {"text": "2.4 times as much", "correct": False,
             "why": "That is the right division with the decimal point in the "
                    "wrong place."},
            {"text": "96 times as much", "correct": False,
             "why": "That doubles the answer instead of dividing one reading by "
                    "the other."},
        ],
        "figure": None,
    },
    {
        "id": "c6-07-s26",
        "band": "standard",
        "text": "A flask gives 48 cm³ of oxygen in 60 seconds. Calculate the mean rate"
                " at which oxygen was produced.",
        "options": [
            {"text": "1.25 cm³ per second", "correct": False,
             "why": "That divides the time by the volume, which gives seconds per "
                    "cm³ instead."},
            {"text": "48 cm³ per second", "correct": False,
             "why": "That is the whole volume, as though it had all arrived in "
                    "one second."},
            {"text": "8.0 cm³ per second", "correct": False,
             "why": "That divides by 6 rather than by 60, dropping a power of ten."},
            {"text": "0.8 cm³ per second", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c6-07-s27",
        "band": "standard",
        "text": "The catalysed trial is repeated with 100 cm³ of the same hydrogen"
                " peroxide instead of 50 cm³, and the same spatula of powder. Compare"
                " the total volume of oxygen collected once both have finished.",
        "options": [
            {"text": "About twice as much, because there is twice as much peroxide",
             "correct": True},
            {"text": "The same, because the mass of catalyst has not changed",
             "correct": False,
             "why": "The catalyst sets the time taken; the peroxide sets how much "
                    "oxygen there can be."},
            {"text": "Less, because the powder is spread through more liquid",
             "correct": False,
             "why": "Spreading the powder out slows the start, but every bit of "
                    "peroxide still decomposes in the end."},
            {"text": "Four times as much, because both the volume and the rate are doubled",
             "correct": False,
             "why": "Rate does not enter a total at all, and doubling one "
                    "quantity cannot quadruple another."},
        ],
        "figure": None,
    },
    {
        "id": "c6-07-s28",
        "band": "standard",
        "text": "A student says the black powder is where the oxygen comes from."
                " Explain what is wrong with that.",
        "options": [
            {"text": "The powder is a solid, and a solid cannot release a gas of its own",
             "correct": False,
             "why": "Plenty of solids release gases; the reason this one does not "
                    "is that it takes no part at all."},
            {"text": "The powder is too small in mass to hold that much gas",
             "correct": False,
             "why": "It is not a question of how much it could hold: none of the "
                    "gas comes from it."},
            {"text": "The powder weighs the same at the end, so nothing has left it",
             "correct": True},
            {"text": "The powder only releases oxygen once it has been warmed",
             "correct": False,
             "why": "Warming it changes nothing, because the oxygen is not coming "
                    "from the powder at any temperature."},
        ],
        "figure": None,
    },
    {
        "id": "c6-07-s29",
        "band": "standard",
        "text": "Every trial on the bench uses a flask and gas syringe of the same"
                " size. Explain why that matters.",
        "options": [
            {"text": "Because a bigger flask would make the reaction go faster",
             "correct": False,
             "why": "The size of the glassware does not change how fast the "
                    "chemistry runs."},
            {"text": "Because any difference in the readings must come from what "
                      "was added", "correct": True},
            {"text": "Because a smaller syringe would read a larger volume",
             "correct": False,
             "why": "A syringe reads the gas that reaches it, whatever its own "
                    "capacity."},
            {"text": "Because using the same glassware every time makes the catalyst last longer",
             "correct": False,
             "why": "The catalyst is not consumed in any apparatus, so nothing "
                    "makes it last longer."},
        ],
        "figure": None,
    },
    {
        "id": "c6-07-s30",
        "band": "standard",
        "text": "A company says its new catalyst raises the amount of product each"
                " batch makes by a fifth. Evaluate that claim.",
        "options": [
            {"text": "Sound, because a faster reaction gets further in the time "
                      "allowed", "correct": False,
             "why": "Left to finish, a catalysed batch reaches the same total; "
                    "speed is not extra product."},
            {"text": "Sound, because catalysts add to the products as they work",
             "correct": False,
             "why": "A catalyst contributes nothing to the products; it is not "
                    "consumed and nothing of it appears in them."},
            {"text": "Unsound, because a catalyst cannot work on a reaction that "
                      "already runs", "correct": False,
             "why": "A catalyst works on precisely those reactions that already "
                    "run, which is the only kind it can act on."},
            {"text": "Unsound, because a catalyst changes the time taken and not "
                      "the amount", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c6-07-s31",
        "band": "standard",
        "text": "1.00 g of manganese dioxide is stirred in, and 1.05 g is on the"
                " balance at the end. Suggest why.",
        "options": [
            {"text": "Some liquid was still on the powder when it was weighed",
             "correct": True},
            {"text": "The powder gained mass by taking oxygen from the peroxide",
             "correct": False,
             "why": "Nothing joins the catalyst; it ends the reaction chemically "
                    "untouched."},
            {"text": "The reaction made new catalyst as it went along",
             "correct": False,
             "why": "A catalyst is neither made nor destroyed by the reaction it "
                    "speeds up."},
            {"text": "Catalysts always end a little heavier than they began",
             "correct": False,
             "why": "The mass at the end matches the mass at the start, which is "
                    "half the definition."},
        ],
        "figure": None,
    },
    {
        "id": "c6-07-s32",
        "band": "standard",
        "text": "A technician is told never to drop a spatula of manganese dioxide"
                " into the stock bottle of hydrogen peroxide. Explain why.",
        "options": [
            {"text": "Because the powder would dissolve and spoil the solution",
             "correct": False,
             "why": "It does not dissolve, and the trouble it causes is not about "
                    "purity."},
            {"text": "Because the bottle would turn into an acid", "correct": False,
             "why": "No acid is formed; the peroxide breaks down into water and a "
                    "gas."},
            {"text": "Because the whole bottle would froth over and be lost",
             "correct": True},
            {"text": "Because the powder would stop the peroxide reacting later",
             "correct": False,
             "why": "It speeds the reaction up rather than holding it back, which "
                    "is the opposite trouble."},
        ],
        "figure": None,
    },
    {
        "id": "c6-07-h17",
        "band": "harder",
        "text": "The manganese dioxide flask and the fresh liver flask are both warmed"
                " to 80 °C before the reaction is started. Predict how each behaves.",
        "options": [
            {"text": "Both go faster, because warming speeds every reaction up",
             "correct": False,
             "why": "Warming does speed reactions up, but it also wrecks the "
                    "enzyme the liver depends on."},
            {"text": "The powder flask goes faster; the liver flask does almost "
                      "nothing", "correct": True},
            {"text": "Both stop, because heat destroys any catalyst at all",
             "correct": False,
             "why": "Heat destroys an enzyme's shape, but a mineral powder is "
                    "untroubled by 80 °C."},
            {"text": "The liver flask goes faster; the powder flask does almost "
                      "nothing", "correct": False,
             "why": "That has the two the wrong way round: the living catalyst is "
                    "the fragile one."},
        ],
        "figure": None,
    },
    {
        "id": "c6-07-h18",
        "band": "harder",
        "text": "A supplier offers a substance that makes a reaction finish in half"
                " the time but leaves only half as much product. Evaluate the claim"
                " that it is a catalyst.",
        "options": [
            {"text": "It is, because finishing a batch sooner is the whole point of a catalyst",
             "correct": False,
             "why": "Speed is only half the test, and the halved product fails "
                    "the other half."},
            {"text": "It is, because a catalyst trades product for time",
             "correct": False,
             "why": "No such trade exists: a catalysed reaction gives exactly the "
                    "product an uncatalysed one would."},
            {"text": "It is not, because a catalyst has to be a solid powder",
             "correct": False,
             "why": "Catalysts are not restricted to powders; liver works and it "
                    "is no powder at all."},
            {"text": "It is not, because a catalyst leaves the amount of product "
                      "alone", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c6-07-h19",
        "band": "harder",
        "text": "A student wants a catalyst that will make silver react with dilute"
                " sulfuric acid to give silver sulfate and hydrogen. Explain why no"
                " such catalyst can be found.",
        "options": [
            {"text": "Silver sits below hydrogen, so there is no reaction to speed "
                      "up", "correct": True},
            {"text": "Silver is far too expensive for a reaction like this to be worth doing",
             "correct": False,
             "why": "Cost decides whether a reaction is worth running, not "
                    "whether it can happen."},
            {"text": "Silver sulfate would decompose as fast as it was made",
             "correct": False,
             "why": "Nothing is made in the first place, so there is nothing to "
                    "decompose."},
            {"text": "Sulfuric acid can only make hydrogen with a carbonate",
             "correct": False,
             "why": "A carbonate gives carbon dioxide, and hydrogen comes from "
                    "acids meeting reactive metals."},
        ],
        "figure": None,
    },
    {
        "id": "c6-07-h20",
        "band": "harder",
        "text": "A student writes that manganese dioxide is a general catalyst, so it"
                " will speed up any reaction it is added to. Evaluate.",
        "options": [
            {"text": "Sound, because it worked on a reaction that was extremely "
                      "slow", "correct": False,
             "why": "Working on one slow reaction says nothing about the next "
                    "one."},
            {"text": "Sound, because any solid with a large surface area speeds "
                      "reactions up", "correct": False,
             "why": "Sand has a large surface area and changes nothing at all."},
            {"text": "Unsound, because a catalyst works on particular reactions "
                      "only", "correct": True},
            {"text": "Unsound, because a catalyst works only while it is being "
                      "stirred", "correct": False,
             "why": "Stirring spreads it out; it keeps working once the stirring "
                    "stops."},
        ],
        "figure": None,
    },
    {
        "id": "c6-07-h21",
        "band": "harder",
        "text": "One flask gets 1.00 g of the catalyst as a single lump and another"
                " gets 1.00 g of it ground fine. Both are left overnight. Compare the"
                " volumes of oxygen in the two syringes the next morning.",
        "options": [
            {"text": "The ground flask holds more, because it worked for longer",
             "correct": False,
             "why": "It worked faster, not for longer; both had all night to "
                    "finish."},
            {"text": "The two hold the same volume, because the peroxide was the "
                      "same", "correct": True},
            {"text": "The lump flask holds more, because its catalyst lasted the "
                      "night", "correct": False,
             "why": "Neither catalyst is consumed, so neither runs out overnight."},
            {"text": "The ground flask holds twice as much, because it was twice "
                      "as fast", "correct": False,
             "why": "Speed sets when a flask finishes, never how much it finishes "
                    "with."},
        ],
        "figure": None,
    },
    {
        "id": "c6-07-h22",
        "band": "harder",
        "text": "A catalysed flask reads far less oxygen than the class average."
                " Suggest how you would decide between a leaking bung and a catalyst"
                " that did not work.",
        "options": [
            {"text": "Warm the flask and see whether the reading rises",
             "correct": False,
             "why": "Warming speeds the chemistry up in both cases, so the "
                    "reading rises either way."},
            {"text": "Add more powder and see whether the reading rises",
             "correct": False,
             "why": "More powder cannot tell you where the gas that was already "
                    "made has gone."},
            {"text": "Compare the reading with the flask that had nothing added",
             "correct": False,
             "why": "A low reading matches the control on either explanation, so "
                    "it separates nothing."},
            {"text": "Look for frothing in a flask whose syringe barely moves",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c6-07-h23",
        "band": "harder",
        "text": "Four runs of the same catalysed flask give 46, 48, 47 and 12 cm³ in"
                " 60 seconds. How should the 12 cm³ be treated?",
        "options": [
            {"text": "Left out of the mean, and the run investigated",
             "correct": True},
            {"text": "Included, because every reading taken must go into a mean",
             "correct": False,
             "why": "A reading that plainly went wrong drags a mean away from the "
                    "value being measured."},
            {"text": "Included, because catalysts get weaker with every run",
             "correct": False,
             "why": "A catalyst is not consumed and does not weaken from one run "
                    "to the next."},
            {"text": "Used on its own, because the lowest reading is the safest",
             "correct": False,
             "why": "The odd reading is the one least likely to be right, not the "
                    "most."},
        ],
        "figure": None,
    },
    {
        "id": "c6-07-h24",
        "band": "harder",
        "text": "A student puts 100 cm³ of peroxide in the catalysed flask and 50 cm³"
                " in the flask with nothing added, then says the powder made four"
                " times as much oxygen. Evaluate.",
        "options": [
            {"text": "Sound, because both flasks were run for the same time",
             "correct": False,
             "why": "Equal timing does not rescue a comparison in which the "
                    "starting amounts differ."},
            {"text": "Sound, because the catalyst is the only thing that was added",
             "correct": False,
             "why": "It is not the only difference: one flask began with twice "
                    "the peroxide."},
            {"text": "Unsound, because the two flasks did not start with the same "
                      "peroxide", "correct": True},
            {"text": "Unsound, because oxygen volumes cannot be compared between different flasks", "correct": False,
             "why": "Volumes compare perfectly well when everything else has been "
                    "kept the same."},
        ],
        "figure": None,
    },
    {
        "id": "c6-07-h25",
        "band": "harder",
        "text": "A catalysed flask holding 50 cm³ of peroxide gives 48 cm³ of oxygen"
                " in the first 60 seconds. A student predicts 96 cm³ after 120"
                " seconds. Evaluate that prediction.",
        "options": [
            {"text": "Sound, because the catalyst keeps working at the same rate",
             "correct": False,
             "why": "The catalyst does keep working, but it cannot decompose "
                    "peroxide that has already gone."},
            {"text": "Unsound, because there is only so much peroxide to decompose",
             "correct": True},
            {"text": "Unsound, because the catalyst is half used up by then",
             "correct": False,
             "why": "The catalyst is not used up at all, in the first minute or "
                    "the second."},
            {"text": "Sound, because doubling the time doubles everything",
             "correct": False,
             "why": "Doubling time cannot double a total that is fixed by the "
                    "amount of starting material."},
        ],
        "figure": None,
    },
    {
        "id": "c6-07-h26",
        "band": "harder",
        "text": "The catalysed trial is repeated with the same volume of a more"
                " concentrated hydrogen peroxide. Compare the speed and the final"
                " volume of oxygen with the first run.",
        "options": [
            {"text": "Faster, and the same oxygen in the end", "correct": False,
             "why": "More concentrated peroxide holds more to decompose, so the "
                    "total cannot be the same."},
            {"text": "The same speed, and more oxygen in the end", "correct": False,
             "why": "A more crowded solution reacts faster as well as giving "
                    "more."},
            {"text": "Slower, and more oxygen in the end", "correct": False,
             "why": "Nothing here slows the reaction down; there is more to react "
                    "in the same space."},
            {"text": "Faster, and more oxygen in the end", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c6-07-h27",
        "band": "harder",
        "text": "A works runs the same catalysed reaction as twenty separate batches a"
                " year. Explain how the catalyst bill compares with the bill for the"
                " reactants.",
        "options": [
            {"text": "The catalyst is bought once and recovered; the reactants are "
                      "bought every batch", "correct": True},
            {"text": "Both are bought fresh for every batch, so both bills are "
                      "paid twenty times", "correct": False,
             "why": "Only the reactants are consumed; the catalyst is collected "
                    "and used again."},
            {"text": "The catalyst is bought every batch and the reactants once, "
                      "as they are recycled", "correct": False,
             "why": "That reverses the two: reactants are what a reaction "
                    "consumes."},
            {"text": "Neither is bought again, because a catalysed reaction feeds "
                      "itself", "correct": False,
             "why": "No reaction supplies its own starting materials, catalysed "
                    "or not."},
        ],
        "figure": None,
    },
    {
        "id": "c6-07-h28",
        "band": "harder",
        "text": "A car fitted with a converter is run on leaded petrol for a year."
                " Describe what happens to the exhaust gases over that year, and to"
                " the mass of platinum.",
        "options": [
            {"text": "The gases are cleaned as well as ever, and the platinum mass "
                      "falls", "correct": False,
             "why": "It is the cleaning that fails, and the platinum that stays "
                    "where it is."},
            {"text": "The gases are cleaned less and less, and the platinum mass "
                      "falls with them", "correct": False,
             "why": "Nothing of the platinum leaves; a balance would find all of "
                    "it still there."},
            {"text": "The gases are cleaned less and less, while the platinum mass "
                      "stays the same", "correct": True},
            {"text": "The gases are cleaned better, and the platinum mass rises as "
                      "lead joins it", "correct": False,
             "why": "Lead settling on the surface stops the converter working "
                    "rather than improving it."},
        ],
        "figure": None,
    },
    {
        "id": "c6-07-h29",
        "band": "harder",
        "text": "One trial reaches 55 cm³ in 60 seconds and another reaches 48 cm³."
                " A student concludes that the first catalyst is far better than the"
                " second. Evaluate.",
        "options": [
            {"text": "Sound, because a higher reading in the same time is a better "
                      "catalyst", "correct": False,
             "why": "It is faster, but seven cm³ on illustrative figures does not "
                    "carry the word far."},
            {"text": "Overstated, because the gap is small and both end with the "
                      "same oxygen", "correct": True},
            {"text": "Unsound, because the two readings cannot be compared at all",
             "correct": False,
             "why": "They can be compared: the flasks differ only in what was "
                    "stirred into them."},
            {"text": "Sound, because the slower catalyst must be partly poisoned",
             "correct": False,
             "why": "Nothing suggests poisoning, and a poisoned catalyst would "
                    "match the untouched flask."},
        ],
        "figure": None,
    },
    {
        "id": "c6-07-h30",
        "band": "harder",
        "text": "An uncatalysed reaction takes 2000 hours to finish. A catalyst makes"
                " it 400 times faster. Calculate how long the catalysed reaction"
                " takes.",
        "options": [
            {"text": "400 hours", "correct": False,
             "why": "That quotes the factor as though it were the answer, with no "
                    "division done."},
            {"text": "50 hours", "correct": False,
             "why": "That divides by 40 rather than by 400, dropping a power of "
                    "ten."},
            {"text": "1600 hours", "correct": False,
             "why": "That subtracts the factor from the time instead of dividing "
                    "by it."},
            {"text": "5 hours", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c6-07-h31",
        "band": "harder",
        "text": "A plant saves a large fuel bill every hour with a catalyst that has"
                " to be replaced every three years. Evaluate whether the catalyst is"
                " worth using.",
        "options": [
            {"text": "Worth it, because the saving is made every hour the plant "
                      "runs", "correct": True},
            {"text": "Not worth it, because the catalyst has to be bought again",
             "correct": False,
             "why": "One purchase every three years is set against a saving made "
                    "around the clock."},
            {"text": "Not worth it, because a catalyst that fails was never a "
                      "catalyst", "correct": False,
             "why": "Being poisoned or clogged in service does not stop something "
                    "having been a catalyst."},
            {"text": "Worth it, because the catalyst also raises the amount of "
                      "product", "correct": False,
             "why": "The amount of product is untouched; the saving is fuel and "
                    "nothing else."},
        ],
        "figure": None,
    },
    {
        "id": "c6-07-h32",
        "band": "harder",
        "text": "A substance makes a reaction run ten times faster, is recovered"
                " weighing exactly what it did at the start, but only works once the"
                " mixture is above 40 °C. Is it a catalyst?",
        "options": [
            {"text": "No, because a catalyst has to work at any temperature",
             "correct": False,
             "why": "Nothing in the definition sets a temperature it must work "
                    "across."},
            {"text": "No, because the warming rather than the substance sped the "
                      "reaction up", "correct": False,
             "why": "The comparison is with the same mixture at the same "
                    "temperature, so warming is not the difference."},
            {"text": "Yes, because it is faster and its mass is unchanged",
             "correct": True},
            {"text": "Yes, but only while the mixture stays above 40 °C, after "
                      "which it is consumed", "correct": False,
             "why": "Cooling it stops it working; it does not begin consuming it."},
        ],
        "figure": None,
    },
]
