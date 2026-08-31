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
]
