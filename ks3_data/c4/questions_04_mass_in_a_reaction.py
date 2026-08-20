"""C4 lesson 04 — Mass in a reaction: twelve questions (MRB-246).

The lesson's argument is one line long — total mass of reactants = total mass
of products — and everything else on the page is either what a balance can and
cannot see, or that line with one of its numbers missing. These twelve probe
the angles the mastery ladder leaves alone: the ARITHMETIC when the unknown is
the whole rather than a part, which side of the arrow decides whether a mass is
added or subtracted, what "not measured" means beside a real 0.00 g, the limit
of the instrument, and the nature-of-science half that the ladder never asks
about at all.

The distractors are built from the lesson's declared misconception and from
three unregistered strands the page confronts in passing.

`REACT-07` — gases have no mass, so a gas escaping cannot change a balance
reading — drives the wrong options in e01, e04, s03 and h03. Each of those
treats a gas as something that is not there once you cannot see it, and each
is the belief that makes a falling reading look like destruction. It is
`ATOM-11` and `PART-05` in a chemical costume and the chain is deliberately
not re-minted here.

Three further strands, none of them in the register and all of them on the
page. **Mass is created or destroyed by burning** drives e02 and h04, where
the reaction itself is imagined to make or unmake matter. **Heat is a
substance with mass** drives e02 and s03 — the belief the hook's third option
and the ladder's first rung both catch, and the one that survives being told
"mass is conserved" because it agrees with it. And **the reading is the
answer** — that a number off a balance can be quoted as it stands, without a
unit, without a subtraction, or as though the instrument saw everything —
drives e03, s01, s02, s04 and h02, which is the largest strand of the twelve
because it is the one a QUANTITATIVE lesson exists to break.

⚑ Every number here is exact and checked. e01 and s02 use the page's own
152.00 / 149.80 / 2.20 g. s01 uses 2.40 g Mg → 4.00 g MgO (exact for Mg 24,
MgO 40). e03 uses 8.00 g CaCO₃ → 4.48 g CaO (exact for CaCO₃ 100, CaO 56),
leaving 3.52 g. h02 uses 6.00 g of carbon → 22.00 g of carbon dioxide, which
needs 16.00 g of oxygen (C 12, O₂ 32, CO₂ 44: 0.500 mol throughout). Two
decimal places everywhere, because that is what a school three-figure balance
gives.

Every question here is new prose — a question bank is the one place in these
two files where that is true — and the bar is §13's: every distractor is a
WRONG RULE in the correct answer's own shape, and every one is a mistake a
real student in a real lab actually makes. Option lengths were counted on
every set, in the gate's own tokens, before this file was handed back; the
correct option is the longest in three of the twelve and clears the longest
distractor by one token in each of those.
"""

UNIT = "C4"
LESSON = "mass-in-a-reaction"
LESSON_NUMBER = 4

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "c4-04-e01",
        "band": "easier",
        "text": "Marble chips and acid are put in an open flask on a balance. "
                "The reading is 152.00 g at the start and 149.80 g when the "
                "fizzing stops. What mass of gas left the flask?",
        "options": [
            {"text": "2.20 g — the first reading minus the second",
             "correct": True},
            {"text": "3.20 g — the first reading minus the second",
             "correct": False,
             "why": "The rule is right and the arithmetic is not. Line the "
                    "two up and subtract column by column: 152.00 − 149.80 "
                    "is 2.20, not 3.20."},
            {"text": "149.80 g — the second reading is the gas",
             "correct": False,
             "why": "149.80 g is what is still on the pan — the flask, the "
                    "acid and everything left in it. The gas is the "
                    "difference between the two readings, never one of them."},
            {"text": "0.00 g — a gas cannot change a reading",
             "correct": False,
             "why": "It just did: the reading fell by 2.20 g and the only "
                    "thing that left was gas. Seal the same flask and the "
                    "reading does not move at all, which is how you know the "
                    "gas was being weighed the whole time."},
        ],
        "figure": None,
    },
    {
        "id": "c4-04-e02",
        "band": "easier",
        "text": "A dish of steel wool is burned on a balance in the open air. "
                "The reading rises. Why?",
        "options": [
            {"text": "Burning makes new matter, and the new matter is heavier "
                     "than the old", "correct": False,
             "why": "Burning makes new substances out of atoms that were "
                    "already there. It never makes new matter — every gram of "
                    "the gain can be traced to oxygen that was in the air "
                    "before the wool was lit."},
            {"text": "Oxygen from the air has joined the steel wool and is "
                     "now on the pan", "correct": True},
            {"text": "The heat put into the steel wool has stayed in it and "
                     "has mass", "correct": False,
             "why": "Heat carries no mass a balance can measure. Let the wool "
                    "cool right down and weigh it again: it is still heavier, "
                    "because what it gained was oxygen, not heat."},
            {"text": "The steel wool has swollen, and a bigger object presses "
                     "down harder", "correct": False,
             "why": "Size is not mass. A balance reads how much matter is on "
                    "the pan, and a bigger object made of the same matter "
                    "reads exactly the same."},
                   ],
        "figure": None,
    },
    {
        "id": "c4-04-e03",
        "band": "easier",
        "text": "A balance reads 8.00 g before heating and 4.48 g after. A "
                "student works out the mass of gas given off and writes the "
                "answer as \"3.52\". What is missing?",
        "options": [
            {"text": "Nothing — a balance reading never needs a unit written "
                     "after it", "correct": False,
             "why": "A number on its own does not say what it measures. 3.52 "
                    "could be grams, kilograms or seconds; only the unit "
                    "settles it, and it is part of the answer rather than "
                    "decoration on the end of it."},
            {"text": "The sign — a mass that is lost should be written as a "
                     "negative", "correct": False,
             "why": "The question asks for the mass of the gas, and there is "
                    "3.52 g of it — a real, positive mass, now in the room. "
                    "The reading fell; the gas did not become negative."},
            {"text": "The unit — the answer is 3.52 g, and grams belong to "
                     "the number", "correct": True},
            {"text": "The rounding — an answer from a balance is always given "
                     "to one place", "correct": False,
             "why": "You give the answer to the same precision the balance "
                    "gave you, which here is two decimal places. Rounding to "
                    "3.5 g throws away a digit the instrument actually "
                    "measured."},
                   ],
        "figure": None,
    },
    {
        "id": "c4-04-e04",
        "band": "easier",
        "text": "The same fizzing reaction is run again in a sealed flask. "
                "This time the balance does not move at all. What does that "
                "tell you?",
        "options": [
            {"text": "The reaction did not happen, because a sealed flask "
                     "stops it starting", "correct": False,
             "why": "Sealing the flask changes nothing about the reaction — "
                    "the chips still fizz and still disappear. It only stops "
                    "the gas leaving the pan."},
            {"text": "The reaction happened, but it made no gas because the "
                     "flask was shut", "correct": False,
             "why": "The same reaction makes the same gas either way. You can "
                    "see it bubbling. What the lid changes is whether the gas "
                    "is still being weighed when you read the balance."},
            {"text": "The balance is broken, because every reaction changes "
                     "the mass a little", "correct": False,
             "why": "No reaction changes the total mass at all. A reading "
                    "that does not move is the balance working perfectly and "
                    "telling you the truth."},
            {"text": "The reaction still happened, and everything it made is "
                     "still on the pan", "correct": True},
                   ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "c4-04-s01",
        "band": "standard",
        "text": "2.40 g of magnesium reacts with oxygen from the air to make "
                "4.00 g of magnesium oxide. Which line finds the mass of "
                "oxygen that joined in?",
        "options": [
            {"text": "mass of oxygen = 4.00 − 2.40, because the oxygen is a "
                     "reactant", "correct": True},
            {"text": "mass of oxygen = 4.00 + 2.40, because both of the "
                     "masses are reactants", "correct": False,
             "why": "Only the magnesium and the oxygen are reactants. The "
                    "4.00 g is the PRODUCT, and it already contains the "
                    "magnesium — adding the magnesium again counts it twice."},
            {"text": "mass of oxygen = 2.40 − 4.00, because the magnesium "
                     "came first", "correct": False,
             "why": "Which substance you met first does not decide the order "
                    "of a subtraction. The whole is 4.00 g, one part is 2.40 "
                    "g, and a part is always the whole take away the other "
                    "part."},
            {"text": "mass of oxygen = 4.00, because the product holds all of "
                     "the mass", "correct": False,
             "why": "The product does hold all of it — including the "
                    "magnesium. Take the magnesium out and what is left, 1.60 "
                    "g, is the oxygen."},
        ],
        "figure": None,
    },
    {
        "id": "c4-04-s02",
        "band": "standard",
        "text": "On a part-whole bar, \"everything before\" is the whole and "
                "\"left in the flask\" and \"the gas\" are the two parts. You "
                "cover \"left in the flask\". What calculation are you left "
                "looking at?",
        "options": [
            {"text": "Add the gas to the mass of everything before the "
                     "reaction", "correct": False,
             "why": "Adding is what you do when the WHOLE is covered and both "
                    "parts are showing. Here the whole is showing, so you "
                    "take away."},
            {"text": "Take the gas away from the mass of everything before "
                     "the reaction", "correct": True},
            {"text": "Take everything before away from the mass of the gas "
                     "that left", "correct": False,
             "why": "That is the same subtraction upside down, and it gives a "
                    "negative mass. The whole always comes first: you take a "
                    "part off the whole, never the whole off a part."},
            {"text": "Multiply the gas by the mass of everything before the "
                     "reaction", "correct": False,
             "why": "Two masses never multiply together to give a third — "
                    "that is why this is drawn as a bar and not as a "
                    "triangle. The parts of a bar add up to the whole."},
                   ],
        "figure": None,
    },
    {
        "id": "c4-04-s03",
        "band": "standard",
        "text": "Which of these is the best evidence that a gas really does "
                "have mass?",
        "options": [
            {"text": "A balloon full of air floats gently downwards instead "
                     "of falling fast", "correct": False,
             "why": "That is about how the air around it slows the balloon "
                    "down, not about what is inside it. An empty balloon "
                    "falls slowly too."},
            {"text": "A gas spreads out to fill any container it is put into",
             "correct": False,
             "why": "True, and it says nothing about mass. Spreading out is "
                    "what makes a gas hard to notice the weight of — the "
                    "same amount of matter is simply in a much bigger space."},
            {"text": "A football weighs more after it has been pumped up hard "
                     "with air", "correct": True},
            {"text": "A sealed jar of air feels no heavier than the same jar "
                     "empty", "correct": False,
             "why": "You cannot empty a jar of air by opening it — you swap "
                    "air for air. Feeling is not measuring either: the air "
                    "around you pushes up on everything, which is exactly why "
                    "gases never feel heavy. Force air IN under pressure, as "
                    "in the football, and the reading rises."},
                   ],
        "figure": None,
    },
    {
        "id": "c4-04-s04",
        "band": "standard",
        "text": "A reaction gives off half a milligram of gas into the room. "
                "A school balance reads to a hundredth of a gram. What does "
                "the balance show?",
        "options": [
            {"text": "No change, because a loss that small is not really a "
                     "loss at all", "correct": False,
             "why": "It is a real loss — half a milligram of gas really did "
                    "leave. What is small is the instrument's ability to see "
                    "it, and that is a fact about the balance rather than "
                    "about the reaction."},
            {"text": "A drop of one hundredth of a gram, because that is the "
                     "smallest step", "correct": False,
             "why": "The smallest step is what the balance can show, not what "
                    "it must show. Half a milligram is twenty times smaller "
                    "than that step, so the display does not move."},
            {"text": "A drop of half a milligram, because a balance shows "
                     "whatever happened", "correct": False,
             "why": "No instrument shows whatever happened — it shows what it "
                    "can measure. This one cannot see anything below a "
                    "hundredth of a gram, so half a milligram is invisible "
                    "to it."},
            {"text": "No change, because the loss is far smaller than the "
                     "balance can read", "correct": True},
                   ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "c4-04-h01",
        "band": "harder",
        "text": "Metals burned in sealed vessels came out heavier. "
                "Supporters of the phlogiston theory answered that phlogiston "
                "had negative mass. What was wrong with that answer?",
        "options": [
            {"text": "It was invented only to save the theory, and it "
                     "predicted nothing new", "correct": True},
            {"text": "It was wrong because a substance that escapes must "
                     "always be a gas", "correct": False,
             "why": "That is a rule about gases and it is not the problem "
                    "here. The problem is the shape of the answer: negative "
                    "mass was added for one purpose only, which was to make "
                    "an awkward measurement stop being awkward."},
            {"text": "It was wrong because the metals were heavier before "
                     "they were burned", "correct": False,
             "why": "They were lighter before. That is the whole difficulty — "
                    "the metal gained mass, which a substance leaving it "
                    "cannot explain."},
            {"text": "It was fine, because a theory is allowed to be changed "
                     "by new evidence", "correct": False,
             "why": "A theory changed by evidence makes new predictions you "
                    "can go and test. This change made none: it only "
                    "explained away the one result that threatened it, which "
                    "is the difference between mending a theory and "
                    "protecting it."},
        ],
        "figure": None,
    },
    {
        "id": "c4-04-h02",
        "band": "harder",
        "text": "6.00 g of carbon is burned in a sealed container and 22.00 g "
                "of carbon dioxide is made. What mass of oxygen was used?",
        "options": [
            {"text": "28.00 g, the mass of the product plus the mass of the "
                     "carbon", "correct": False,
             "why": "The 22.00 g of carbon dioxide already contains the "
                    "carbon. Adding the carbon on top counts it a second "
                    "time, and gives more product than there is."},
            {"text": "16.00 g, the mass of the product minus the mass of the "
                     "carbon", "correct": True},
            {"text": "22.00 g, because the product is the mass of the oxygen "
                     "used", "correct": False,
             "why": "The product is the carbon AND the oxygen joined "
                    "together. Take the carbon out of it and what is left is "
                    "the oxygen."},
            {"text": "6.00 g, because equal masses of carbon and oxygen "
                     "always react", "correct": False,
             "why": "There is no rule that equal masses react. Here 6.00 g of "
                    "carbon takes 16.00 g of oxygen, and the ratio is "
                    "different for every reaction."},
                   ],
        "figure": None,
    },
    {
        "id": "c4-04-h03",
        "band": "harder",
        "text": "Two identical flasks run the same reaction. The open one "
                "loses 1.75 g; the sealed one loses nothing. A student "
                "concludes that the sealed flask made less gas. What is wrong "
                "with that?",
        "options": [
            {"text": "Nothing is wrong; a sealed flask really does make less "
                     "gas than an open one", "correct": False,
             "why": "The lid is not part of the reaction. Both flasks hold "
                    "the same substances in the same amounts, so both make "
                    "the same 1.75 g of gas — one of them keeps it."},
            {"text": "Both made gas, but only the sealed one's gas has any "
                     "mass to weigh", "correct": False,
             "why": "All gas has mass, wherever it is. The 1.75 g that left "
                    "the open flask still has that mass; it is simply in the "
                    "room now instead of on the pan."},
            {"text": "Both made the same gas; only one of them let it off the "
                     "pan", "correct": True},
            {"text": "The open flask made more gas, because an open flask "
                     "reacts faster", "correct": False,
             "why": "Even if it did react faster, speed changes how long it "
                    "takes and not how much is made. The open flask lost gas; "
                    "it did not make extra."},
                   ],
        "figure": None,
    },
    {
        "id": "c4-04-h04",
        "band": "harder",
        "text": "Why can the total mass never change in a chemical reaction?",
        "options": [
            {"text": "The reaction always makes exactly as many new "
                     "substances as it uses", "correct": False,
             "why": "The number of substances has nothing to do with it — one "
                    "substance often becomes two, or two become one. It is "
                    "the ATOMS that are counted, and they are all still "
                    "there."},
            {"text": "Whatever is created somewhere is destroyed somewhere "
                     "else at the same time", "correct": False,
             "why": "Nothing is created and nothing is destroyed anywhere, so "
                    "there is nothing to cancel out. A reaction only "
                    "rearranges what it already has."},
            {"text": "Nothing is allowed to leave the flask while a reaction "
                     "is going on", "correct": False,
             "why": "Plenty leaves an open flask — that is why the reading "
                    "falls. The total is still unchanged; the balance has "
                    "simply stopped weighing part of it."},
            {"text": "Every atom that goes in comes out again, just joined up "
                     "differently", "correct": True},
                   ],
        "figure": None,
    },
]
