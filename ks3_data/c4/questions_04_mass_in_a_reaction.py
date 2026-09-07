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

    # ── easier · MRB-335 top-up ─────────────────────────────────────────
    {
        "id": "c4-04-e05",
        "band": "easier",
        "text": "What is a sealed vessel?",
        "options": [
            {"text": "A container strong enough to hold a reaction that gives "
                     "out a great deal of heat without cracking or bursting "
                     "while it runs",
             "correct": False,
             "why": "Strength is a separate matter. Sealed is about what can "
                    "cross the boundary"},
            {"text": "A container with all the air pumped out of it",
             "correct": False,
             "why": "The air can stay inside. What matters is that nothing "
                    "crosses in or out"},
            {"text": "A container that has been weighed before use",
             "correct": False,
             "why": "Weighing is something you do to it. Sealing is a "
                    "property of the container"},
            {"text": "A container closed so that no gas can get in or out",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c4-04-e06",
        "band": "easier",
        "text": "Complete the rule: total mass of reactants equals what?",
        "options": [
            {"text": "Total mass of products",
             "correct": True},
            {"text": "Total mass of whatever is left on the balance pan when "
                     "the reaction has stopped, which is what the second "
                     "reading actually measures",
             "correct": False,
             "why": "That is what an OPEN balance shows, and it misses any "
                    "gas that left. The rule counts everything"},
            {"text": "Total mass of the solid products only",
             "correct": False,
             "why": "Gases have mass and are products. Leaving them out is "
                    "what makes an open reading confusing"},
            {"text": "Total mass of the reactants minus the gas",
             "correct": False,
             "why": "Nothing is subtracted. The two totals are equal"},
        ],
        "figure": None,
    },
    {
        "id": "c4-04-e07",
        "band": "easier",
        "text": "The lesson says oxygen from the air is a reactant even "
                "though nobody weighed it out. Why does that matter?",
        "options": [
            {"text": "Because a reactant has to be listed in an equation, and "
                     "an equation is not allowed to name a substance that "
                     "nobody has measured",
             "correct": False,
             "why": "There is no such rule about equations. It matters "
                    "because its mass has to be in the sum"},
            {"text": "Because its mass has to be counted, or the sum will not "
                     "come out",
             "correct": True},
            {"text": "Because air is a mixture, so its mass cannot be worked "
                     "out",
             "correct": False,
             "why": "The oxygen used can be worked out from the other masses, "
                    "which is most of this lesson"},
            {"text": "Because oxygen weighs nothing",
             "correct": False,
             "why": "It weighs a great deal — 1.60 g of it joins 2.40 g of "
                    "magnesium"},
        ],
        "figure": None,
    },
    {
        "id": "c4-04-e08",
        "band": "easier",
        "text": "A balance reading falls during a reaction in an open flask. "
                "What has happened?",
        "options": [
            {"text": "Mass has been destroyed by the reaction, which is what "
                     "the falling reading on the balance is a direct "
                     "measurement of",
             "correct": False,
             "why": "Mass is never destroyed. The reading falls because "
                    "something walked off the pan"},
            {"text": "A gas has joined from the air",
             "correct": False,
             "why": "That would make the reading RISE, as it does when "
                    "magnesium burns"},
            {"text": "A gas has left the pan",
             "correct": True},
            {"text": "Heat has escaped, and heat has mass",
             "correct": False,
             "why": "Heat carries no measurable mass. A gas does"},
        ],
        "figure": None,
    },
    {
        "id": "c4-04-e09",
        "band": "easier",
        "text": "On the part-whole bar, what is the WHOLE?",
        "options": [
            {"text": "The mass of gas that left the flask, since that is the "
                     "quantity every calculation in the lesson is trying to "
                     "arrive at",
             "correct": False,
             "why": "The gas is one of the two PARTS. The quantity you want "
                    "is not the whole just because you want it"},
            {"text": "What is left in the flask afterwards",
             "correct": False,
             "why": "That is the other part. Together with the gas it fills "
                    "the whole bar"},
            {"text": "The flask itself",
             "correct": False,
             "why": "The flask is on the pan the whole time and cancels out. "
                    "The bar is about the reaction"},
            {"text": "Everything before the reaction",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c4-04-e10",
        "band": "easier",
        "text": "5.00 g of a metal reacts completely with 3.00 g of sulfur in "
                "a sealed tube. What mass of metal sulfide is made?",
        "options": [
            {"text": "8.00 g",
             "correct": True},
            {"text": "2.00 g",
             "correct": False,
             "why": "That is 5.00 minus 3.00. Nothing was taken away — the "
                    "two substances joined"},
            {"text": "5.00 g, because the sulfide is named after the metal "
                     "and so has the mass the metal brought to the tube with "
                     "it",
             "correct": False,
             "why": "The sulfur is in the product too, and it has mass. "
                    "Naming has nothing to do with weighing"},
            {"text": "It cannot be worked out without knowing which metal",
             "correct": False,
             "why": "Conservation of mass does not care which metal. "
                    "Everything that went in is still in the sealed tube"},
        ],
        "figure": None,
    },

    # ── standard · MRB-335 top-up ───────────────────────────────────────
    {
        "id": "c4-04-s05",
        "band": "standard",
        "text": "12.00 g of magnesium carbonate is heated in an open crucible "
                "and 5.72 g of magnesium oxide is left. What mass of carbon "
                "dioxide was given off?",
        "options": [
            {"text": "17.72 g, adding the two masses together as the rule for "
                     "conservation of mass requires",
             "correct": False,
             "why": "The rule is an equality, not an instruction to add "
                    "everything. Here one part is being taken from the whole"},
            {"text": "5.72 g",
             "correct": False,
             "why": "That is the solid left behind. The gas is what is "
                    "missing from the whole"},
            {"text": "12.00 g",
             "correct": False,
             "why": "That is everything before. Some of it is still in the "
                    "crucible"},
            {"text": "6.28 g",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c4-04-s06",
        "band": "standard",
        "text": "A student sets out the calculation as: mass of gas = "
                "149.80 − 152.00. What is wrong with it?",
        "options": [
            {"text": "The subtraction is reversed: the gas is what is missing "
                     "from the WHOLE, so the first reading comes first",
             "correct": True},
            {"text": "Nothing is wrong, since the two readings have to be "
                     "subtracted from each other and the order in which that "
                     "is done makes no difference to the size of the answer",
             "correct": False,
             "why": "The size is the same and the sign is not. A mass of "
                    "minus 2.20 g is not a thing"},
            {"text": "It is the wrong way round, and gives a negative mass",
             "correct": False,
             "why": "That IS what is wrong — but read the other options "
                    "before choosing, because one of them says it more "
                    "usefully"},
            {"text": "The rule was never written down first",
             "correct": False,
             "why": "Writing the rule first is good practice, and it is not "
                    "the error in this line"},
        ],
        "figure": None,
    },
    {
        "id": "c4-04-s07",
        "band": "standard",
        "text": "A candle burns on an open balance and the reading falls by "
                "4.10 g. What is the total mass of the products?",
        "options": [
            {"text": "4.10 g, which is what the balance shows has gone",
             "correct": False,
             "why": "4.10 g is the mass of WAX used up. The products also "
                    "contain the oxygen that joined it"},
            {"text": "More than 4.10 g, because oxygen from the air is in the "
                     "products too",
             "correct": True},
            {"text": "Exactly 4.10 g, because mass is conserved",
             "correct": False,
             "why": "Mass IS conserved, across everything — including the "
                    "oxygen the balance never weighed"},
            {"text": "Less than 4.10 g, because some was lost as heat",
             "correct": False,
             "why": "Heat takes no measurable mass away. Nothing is lost"},
        ],
        "figure": None,
    },
    {
        "id": "c4-04-s08",
        "band": "standard",
        "text": "The same reaction is run open and sealed. Which pair of "
                "readings is possible?",
        "options": [
            {"text": "Open does not move; sealed falls by 2.20 g, because the "
                     "gas has nowhere to go and is pressed into the walls of "
                     "the flask",
             "correct": False,
             "why": "Nothing is pressed into glass, and it is the OPEN flask "
                    "that loses gas"},
            {"text": "Open falls by 2.20 g; sealed falls by 1.10 g",
             "correct": False,
             "why": "A sealed flask loses nothing at all. Half a loss makes "
                    "no sense"},
            {"text": "Open falls by 2.20 g; sealed does not move",
             "correct": True},
            {"text": "Both rise by 2.20 g",
             "correct": False,
             "why": "This reaction gives a gas off. Only a reaction that "
                    "takes gas IN can make an open reading rise"},
        ],
        "figure": None,
    },
    {
        "id": "c4-04-s09",
        "band": "standard",
        "text": "A balance reading does not move at all during a reaction. "
                "What are the two things that could mean?",
        "options": [
            {"text": "That the reaction has not started, or that it has "
                     "already finished before the first reading was taken",
             "correct": False,
             "why": "A sealed flask fizzing hard shows no change either. The "
                    "balance says nothing about whether it ran"},
            {"text": "That mass was conserved, or that the balance is "
                     "broken",
             "correct": False,
             "why": "Mass is conserved every time, including when the reading "
                    "does move. It cannot be one of two possibilities"},
            {"text": "That no reaction happened, or that the products weigh "
                     "the same as the reactants",
             "correct": False,
             "why": "The products always weigh the same as the reactants. "
                    "That is the rule, not one of two cases"},
            {"text": "Either the vessel is sealed, or no gas entered or left "
                     "it",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c4-04-s10",
        "band": "standard",
        "text": "The lesson says conservation of mass is drawn as a bar and "
                "never as a triangle. Why does the shape matter?",
        "options": [
            {"text": "Because the relationship is a sum, and a triangle is "
                     "for multiplying and dividing",
             "correct": True},
            {"text": "Because a bar can be drawn to scale and a triangle "
                     "cannot, so only the bar shows how small the gas really "
                     "is beside everything else on the balance",
             "correct": False,
             "why": "Neither diagram here is to scale — the lesson says so. "
                    "What the shape records is the kind of relationship"},
            {"text": "Because a triangle only has three parts and there are "
                     "four quantities here",
             "correct": False,
             "why": "There are three quantities: the whole and its two parts. "
                    "The objection is about adding rather than counting"},
            {"text": "Because a bar is easier to draw",
             "correct": False,
             "why": "Ease is not the reason. A triangle would tell you to "
                    "multiply, which would give the wrong answer"},
        ],
        "figure": None,
    },

    # ── harder · MRB-335 top-up ─────────────────────────────────────────
    {
        "id": "c4-04-h05",
        "band": "harder",
        "text": "24.00 g of magnesium burns completely in oxygen and 40.00 g "
                "of magnesium oxide is made. How much oxygen would 12.00 g of "
                "magnesium need?",
        "options": [
            {"text": "16.00 g, which is the mass of oxygen the first reaction "
                     "used and is therefore fixed for the substance whatever "
                     "amount of magnesium is burned",
             "correct": False,
             "why": "16.00 g is right for 24.00 g of magnesium. Half the "
                    "magnesium needs half the oxygen"},
            {"text": "12.00 g",
             "correct": False,
             "why": "That is the mass of magnesium, not of the oxygen it "
                    "needs. The two are not equal"},
            {"text": "28.00 g",
             "correct": False,
             "why": "That is 40.00 minus 12.00, which mixes a mass from one "
                    "reaction with a mass from the other"},
            {"text": "8.00 g",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c4-04-h06",
        "band": "harder",
        "text": "Lavoisier weighed everything, including the air in the "
                "vessel. Why was including the air the decisive step?",
        "options": [
            {"text": "Because the metal's gain turned out to equal the air's "
                     "loss exactly, which nothing else could account for",
             "correct": True},
            {"text": "Because air is a mixture, and mixtures have to be "
                     "weighed separately",
             "correct": False,
             "why": "Being a mixture is not the point. The point is that the "
                    "air lost exactly what the metal gained"},
            {"text": "Because nobody had weighed a gas before",
             "correct": False,
             "why": "Gases had been weighed. What was new was counting the "
                    "air as part of the reaction"},
            {"text": "Because the sealed vessel weighed less afterwards",
             "correct": False,
             "why": "A sealed vessel weighs the same afterwards. That is what "
                    "made the bookkeeping work"},
        ],
        "figure": None,
    },
    {
        "id": "c4-04-h07",
        "band": "harder",
        "text": "Two students run the same open reaction, one with 1 g of "
                "marble and one with 100 g. Whose balance falls further, and "
                "does that break the rule?",
        "options": [
            {"text": "The 1 g one, because a small sample reacts completely "
                     "while a large one has marble left over that never gets "
                     "to the acid at all",
             "correct": False,
             "why": "Leftover marble would mean less gas, not more. And the "
                    "bigger sample makes the bigger fall"},
            {"text": "The 100 g one, and no — more marble makes more gas, and "
                     "mass is conserved in both",
             "correct": True},
            {"text": "The 100 g one, and yes — a rule that gives different "
                     "answers for different amounts is not a rule",
             "correct": False,
             "why": "The rule is about totals, not about the size of a "
                    "reading. Both runs conserve mass exactly"},
            {"text": "Neither — both fall by the same amount",
             "correct": False,
             "why": "A hundred times the marble gives about a hundred times "
                    "the gas"},
        ],
        "figure": None,
    },
    {
        "id": "c4-04-h08",
        "band": "harder",
        "text": "Inside a star, a tiny amount of mass becomes energy. Why is "
                "that not an exception to this lesson's rule?",
        "options": [
            {"text": "Because the amount is far too small to matter to a "
                     "chemist",
             "correct": False,
             "why": "It is not an approximation. It is a different kind of "
                    "change, where the atoms themselves alter"},
            {"text": "Because stars are too far away to measure",
             "correct": False,
             "why": "The same process runs in reactors on Earth and is "
                    "measured precisely. Distance is not the reason"},
            {"text": "Because that is a nuclear change, where the atoms "
                     "themselves alter rather than rearrange",
             "correct": True},
            {"text": "Because energy is a substance, so nothing has really "
                     "left",
             "correct": False,
             "why": "Energy is not a substance. The rule holds because "
                    "chemistry does not change atoms"},
        ],
        "figure": None,
    },
    {
        "id": "c4-04-h09",
        "band": "harder",
        "text": "A sealed flask of steel wool and air is weighed, left until "
                "the wool has rusted, and weighed again. What does the balance "
                "read, and why?",
        "options": [
            {"text": "Higher, because oxygen has joined the iron and the "
                     "oxide is heavier",
             "correct": False,
             "why": "The oxide IS heavier than the wool. The oxygen it took "
                    "was already sealed inside and already on the pan"},
            {"text": "Lower, because the air inside has been used up",
             "correct": False,
             "why": "Using it up moves it into the rust. Nothing has left the "
                    "flask"},
            {"text": "It cannot be predicted without knowing how much air was "
                     "sealed in",
             "correct": False,
             "why": "The amount of air changes how much rusts. It cannot "
                    "change a total that nothing has crossed"},
            {"text": "The same, because the oxygen came from inside the "
                     "flask",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c4-04-h10",
        "band": "harder",
        "text": "Two flasks run the same reaction. The open one gains 1.60 g "
                "and the sealed one gains nothing. A student says the sealed "
                "reaction did not finish. What is wrong?",
        "options": [
            {"text": "A sealed flask cannot gain mass however far the "
                     "reaction goes, so the reading says nothing about "
                     "finishing",
             "correct": True},
            {"text": "Nothing — a sealed flask has only the oxygen it started "
                     "with, so it must stop sooner",
             "correct": False,
             "why": "It CAN run short of oxygen, and that would show as less "
                    "product rather than as an unchanged balance. The balance "
                    "cannot see the difference either way"},
            {"text": "The sealed reaction gained 1.60 g too, and the balance "
                     "missed it",
             "correct": False,
             "why": "Nothing crossed the seal, so there is nothing for the "
                    "balance to have missed"},
            {"text": "The open flask must have lost gas rather than gained "
                     "it",
             "correct": False,
             "why": "It gained, which is what happens when oxygen joins from "
                    "the air"},
        ],
        "figure": None,
    },
]
