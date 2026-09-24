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
        "text": "Magnesium burns in oxygen to make magnesium oxide. The bar "
                "model shows the masses. What mass of oxygen reacted?",
        "options": [
            {"text": "1.6 g",
             "correct": True},
            {"text": "6.4 g",
             "correct": False,
             "why": "That adds the two masses shown. The magnesium and the "
                    "oxygen together make the 4.0 g of product, so the oxygen "
                    "is what is left when 2.4 g is taken away."},
            {"text": "4.0 g",
             "correct": False,
             "why": "That is the whole bar, the magnesium oxide. The oxygen "
                    "is only the part of it that the magnesium does not fill."},
            {"text": "9.6 g",
             "correct": False,
             "why": "That multiplies the two masses, as a formula triangle "
                    "would tell you to. Mass is conserved by adding: the "
                    "parts add up to the whole."},
        ],
        "figure": "c4-bar-model-mg-oxide",
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

    # ── MRB-338 expansion ───────────────────────────────────────────
    {
        "id": "c4-04-e11",
        "band": "easier",
        "text": "Yeast and sugar solution are left to ferment in an open "
                "flask standing on a balance. Carbon dioxide bubbles steadily "
                "out of the neck. What happens to the balance reading?",
        "options": [
            {"text": "It falls, because the gas has left the pan",
             "correct": True},
            {"text": "It rises, because bubbles are being made",
             "correct": False,
             "why": "Bubbles are gas being made, not mass being made. That "
                    "gas comes out of the sugar that was already on the pan"},
            {"text": "It does not change, because a gas weighs nothing at all",
             "correct": False,
             "why": "A gas has mass like anything else. Once it is out of the "
                    "neck it is simply no longer on the pan"},
            {"text": "It falls, then rises back as the fizzing stops",
             "correct": False,
             "why": "Nothing brings the escaped gas back. The reading stays "
                    "down once the bubbling has finished"},
        ],
        "figure": None,
    },
    {
        "id": "c4-04-e12",
        "band": "easier",
        "text": "An indigestion tablet is dropped into water in an open "
                "beaker on a balance, and the reading falls by 1.30 g. Where "
                "is the missing 1.30 g now?",
        "options": [
            {"text": "Destroyed by the reaction",
             "correct": False,
             "why": "Nothing is destroyed by a reaction. The atoms are all "
                    "still there, joined up differently"},
            {"text": "Still dissolved in the water, which hides its mass",
             "correct": False,
             "why": "Anything still in the water is still on the pan, so it "
                    "could not be part of a fall in the reading"},
            {"text": "In the air of the room, as escaped gas",
             "correct": True},
            {"text": "Turned into the heat the beaker gave out",
             "correct": False,
             "why": "Heat carries no mass a balance can read. The missing "
                    "1.30 g is matter, and it went out as gas"},
        ],
        "figure": None,
    },
    {
        "id": "c4-04-e13",
        "band": "easier",
        "text": "Copper turnings are heated strongly in an open crucible "
                "until they have all turned into black copper oxide. The "
                "black powder has a greater mass than the copper did. What "
                "has been added to the copper?",
        "options": [
            {"text": "Heat from the Bunsen, which has mass",
             "correct": False,
             "why": "Heat starts the reaction off but adds no mass to the "
                    "crucible"},
            {"text": "Oxygen taken from the air",
             "correct": True},
            {"text": "Nitrogen from the air",
             "correct": False,
             "why": "Most of the air is nitrogen, but it takes no part here. "
                    "The product is copper OXIDE"},
            {"text": "Water vapour from the air",
             "correct": False,
             "why": "Copper oxide contains no hydrogen, so no water went into "
                    "it"},
        ],
        "figure": None,
    },
    {
        "id": "c4-04-e14",
        "band": "easier",
        "text": "A reaction in an open beaker gives off hydrogen gas. The "
                "beaker and everything in it have a mass of 86.40 g at the "
                "start and 86.20 g at the end. Calculate the mass of hydrogen "
                "given off.",
        "options": [
            {"text": "0.02 g",
             "correct": False,
             "why": "A place-value slip. 86.40 − 86.20 is 0.20, not 0.02"},
            {"text": "86.20 g",
             "correct": False,
             "why": "That is everything LEFT in the beaker, not the part that "
                    "escaped from it"},
            {"text": "172.60 g",
             "correct": False,
             "why": "The two readings have been added. The gas is the "
                    "difference between them"},
            {"text": "0.20 g",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c4-04-e15",
        "band": "easier",
        "text": "A student says that mass is only conserved when a reaction "
                "is carried out in a sealed flask. Is that right?",
        "options": [
            {"text": "Yes, because an open flask always loses mass to the "
                     "room",
             "correct": False,
             "why": "An open flask can gain instead, and either way the total "
                    "including the gas is unchanged"},
            {"text": "Yes, because sealing stops the gas being made in the "
                     "first place",
             "correct": False,
             "why": "Sealing changes nothing about the reaction. The gas is "
                    "still made; it just cannot leave"},
            {"text": "No — mass is conserved only when a flask is left open",
             "correct": False,
             "why": "This has the rule the wrong way round, and the rule has "
                    "no such condition on it at all"},
            {"text": "No — mass is always conserved; sealing only lets the "
                     "balance show it",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c4-04-e16",
        "band": "easier",
        "text": "A fizzing reaction is run in a flask with a balloon "
                "stretched tightly over its neck, so no gas can escape. The "
                "flask and balloon stay on the balance. What happens to the "
                "reading?",
        "options": [
            {"text": "It falls, because the gas is now in the balloon",
             "correct": False,
             "why": "The balloon is on the pan too, so the gas inside it is "
                    "still being weighed"},
            {"text": "It stays the same, because the gas is still on the pan",
             "correct": True},
            {"text": "It rises, because the balloon is bigger",
             "correct": False,
             "why": "Taking up more room is not the same as having more mass. "
                    "Nothing has joined from outside"},
            {"text": "It falls, because gas weighs less than liquid",
             "correct": False,
             "why": "The gas came out of what was already there, so the total "
                    "on the pan cannot have dropped"},
        ],
        "figure": None,
    },
    {
        "id": "c4-04-e17",
        "band": "easier",
        "text": "A flask of acid and a dish of marble chips are weighed "
                "together on a balance: 178.40 g in total. The chips are then "
                "tipped into the flask, which is left open while it fizzes. "
                "What is the final reading?",
        "options": [
            {"text": "Less than 178.40 g, because gas has left the flask",
             "correct": True},
            {"text": "Exactly 178.40 g, because mass is always conserved",
             "correct": False,
             "why": "Mass IS conserved, but the balance only weighs what is "
                    "left on the pan, and the gas is not"},
            {"text": "More than 178.40 g, because a new substance is made",
             "correct": False,
             "why": "New substances are made from the atoms already there, so "
                    "they add nothing to the total"},
            {"text": "More than 178.40 g, because the gas made inside adds "
                     "weight",
             "correct": False,
             "why": "The gas made inside pushes out of the open neck, and "
                    "filling a space adds no mass anyway"},
        ],
        "figure": None,
    },
    {
        "id": "c4-04-e18",
        "band": "easier",
        "text": "Which of these reactions, run in an open container on a "
                "balance, would make the reading go UP?",
        "options": [
            {"text": "A carbonate giving off carbon dioxide when heated",
             "correct": False,
             "why": "Gas leaves the dish here, so this reading goes down"},
            {"text": "An indigestion tablet fizzing hard in a beaker of warm "
                     "water",
             "correct": False,
             "why": "The fizzing is gas escaping from the beaker, so this "
                    "reading goes down"},
            {"text": "A metal burning and taking in oxygen from the air",
             "correct": True},
            {"text": "Zinc reacting with acid to give off hydrogen",
             "correct": False,
             "why": "Hydrogen bubbles away out of the dish, so this reading "
                    "goes down"},
        ],
        "figure": None,
    },
    {
        "id": "c4-04-e19",
        "band": "easier",
        "text": "Magnesium burns in oxygen to make magnesium oxide. In the "
                "conservation-of-mass sum for this reaction, which masses are "
                "added together on the reactant side?",
        "options": [
            {"text": "The magnesium oxide only, since it holds all of the "
                     "mass now",
             "correct": False,
             "why": "The oxide is the product. It belongs on the other side "
                    "of the equals sign"},
            {"text": "The magnesium and the oxygen it took from the air",
             "correct": True},
            {"text": "The magnesium only, since nobody weighed the oxygen",
             "correct": False,
             "why": "A reactant counts whether or not anybody weighed it out. "
                    "Leave the oxygen out and the sum will not balance"},
            {"text": "The magnesium oxide and the oxygen from the air",
             "correct": False,
             "why": "This puts a product and a reactant on the same side. The "
                    "oxide is what the other two became"},
        ],
        "figure": None,
    },
    {
        "id": "c4-04-e20",
        "band": "easier",
        "text": "In a sealed flask, 2.30 g of sodium reacts completely with "
                "3.55 g of chlorine to make sodium chloride and nothing else. "
                "What mass of sodium chloride is made?",
        "options": [
            {"text": "1.25 g",
             "correct": False,
             "why": "The two reactant masses have been subtracted. Both of "
                    "them ended up in the product, so they add"},
            {"text": "3.55 g",
             "correct": False,
             "why": "That is the chlorine alone. The sodium is in the product "
                    "too"},
            {"text": "5.85 g",
             "correct": True},
            {"text": "2.30 g",
             "correct": False,
             "why": "That is the sodium alone. The chlorine did not vanish "
                    "when it joined on"},
        ],
        "figure": None,
    },
    {
        "id": "c4-04-e21",
        "band": "easier",
        "text": "An empty crucible has a mass of 82.20 g. A 2.40 g strip of "
                "magnesium is put inside it. What does the balance read with "
                "the crucible and the magnesium both on the pan?",
        "options": [
            {"text": "2.40 g",
             "correct": False,
             "why": "A balance weighs everything on the pan, and the crucible "
                    "is on the pan too"},
            {"text": "82.20 g",
             "correct": False,
             "why": "That is the crucible on its own, before the magnesium "
                    "was added to it"},
            {"text": "79.80 g",
             "correct": False,
             "why": "Adding magnesium cannot make the reading smaller. These "
                    "two masses add, they do not subtract"},
            {"text": "84.60 g",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c4-04-e22",
        "band": "easier",
        "text": "Chemists say that mass is conserved in a chemical reaction. "
                "What does the word conserved mean here?",
        "options": [
            {"text": "The total stays exactly the same",
             "correct": True},
            {"text": 'It is stored up somewhere and given back later',
             "correct": False,
             "why": "Nothing is stored and returned. The total is the same at "
                    "every moment, not just at the end"},
            {"text": "The mass is used up slowly as it reacts",
             "correct": False,
             "why": "Reactants are used up, but their mass is not: it is in "
                    "the products"},
            {"text": 'It is shared out evenly between the products',
             "correct": False,
             "why": "Products can have very different masses. What is fixed "
                    "is the total, not the share"},
        ],
        "figure": None,
    },
    {
        "id": "c4-04-e23",
        "band": "easier",
        "text": "Green copper carbonate is heated in an open test tube. It "
                "turns black, and carbon dioxide is driven off into the room. "
                "How does the mass of solid left in the tube compare with the "
                "copper carbonate at the start?",
        "options": [
            {"text": "Greater, because a black solid is denser than a green "
                     "one",
             "correct": False,
             "why": "Density is about how tightly packed a substance is, not "
                    "how much of it there is"},
            {"text": "Smaller, because the carbon dioxide has gone",
             "correct": True},
            {"text": "The same — the solid stayed in the tube",
             "correct": False,
             "why": "The solid stayed, but part of what it was made of left "
                    "as a gas"},
            {"text": "Greater, because heating always adds energy, and energy "
                     "adds mass",
             "correct": False,
             "why": "Energy put in by a Bunsen adds no mass a balance can "
                    "read"},
        ],
        "figure": None,
    },
    {
        "id": "c4-04-e24",
        "band": "easier",
        "text": "A reaction gives off a gas. In which of these containers, "
                "standing on a balance, would the reading show the gas "
                "leaving?",
        "options": [
            {"text": "An open beaker",
             "correct": True},
            {"text": "A sealed flask",
             "correct": False,
             "why": "Nothing can cross a seal, so the gas stays on the pan "
                    "and the reading does not move"},
            {"text": "A flask with a balloon tied over the neck",
             "correct": False,
             "why": "The balloon holds the gas, and the balloon is on the pan "
                    "as well"},
            {"text": "A stoppered test tube",
             "correct": False,
             "why": "A stopper keeps the gas inside, so the balance has "
                    "nothing to report"},
        ],
        "figure": None,
    },
    {
        "id": "c4-04-e25",
        "band": "easier",
        "text": "A sealed flask holds 40 carbon atoms before a reaction "
                "starts. The reaction makes several new substances. How many "
                "carbon atoms are in the flask afterwards?",
        "options": [
            {"text": "Fewer than 40",
             "correct": False,
             "why": "Atoms are not used up in a reaction; they are joined "
                    "together differently"},
            {"text": "More than 40",
             "correct": False,
             "why": "A sealed flask cannot gain atoms, and a reaction cannot "
                    "make them"},
            {"text": "40",
             "correct": True},
            {"text": "It cannot be said",
             "correct": False,
             "why": "It can, and without knowing the reaction: in a sealed "
                    "flask the count of each kind of atom is fixed"},
        ],
        "figure": None,
    },
    {
        "id": "c4-04-e26",
        "band": "easier",
        "text": "Hydrogen peroxide solution in an open beaker slowly breaks "
                "down into water and oxygen gas. The beaker stands on a "
                "balance throughout. What happens to the reading?",
        "options": [
            {"text": "It rises, because two substances are made where there "
                     "was one",
             "correct": False,
             "why": "Splitting one substance into two shares the mass out; it "
                    "does not add any"},
            {"text": "It stays the same, because a liquid stays a liquid",
             "correct": False,
             "why": "Part of the liquid leaves as oxygen gas, and that gas is "
                    "off the pan"},
            {"text": "It rises, because oxygen joins from the air",
             "correct": False,
             "why": "The oxygen comes out of the hydrogen peroxide, not out "
                    "of the air"},
            {"text": "It falls, because the oxygen leaves the beaker",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c4-04-e27",
        "band": "easier",
        "text": "Two reactants are weighed into a sealed flask: 10.00 g of "
                "one and 6.00 g of the other. They react completely. What is "
                "the total mass of everything in the flask at the end?",
        "options": [
            {"text": "16.00 g",
             "correct": True},
            {"text": "4.00 g",
             "correct": False,
             "why": "The two masses have been subtracted. Both reactants are "
                    "still in the flask, as products"},
            {"text": "10.00 g",
             "correct": False,
             "why": "That is one reactant on its own. The other one did not "
                    "disappear when it reacted"},
            {"text": "Less than 16.00 g",
             "correct": False,
             "why": "Nothing can leave a sealed flask, so the total inside it "
                    "cannot drop"},
        ],
        "figure": None,
    },
    {
        "id": "c4-04-e28",
        "band": "easier",
        "text": "The air in an ordinary classroom has a mass of about 150 "
                "kilograms. Which idea does that fact support?",
        "options": [
            {"text": "Gases have no mass until they are squeezed into a "
                     "cylinder",
             "correct": False,
             "why": "Squeezing a gas puts more of it in a smaller space. It "
                    "does not give it mass it did not have"},
            {"text": "Gases have mass, even though you cannot feel it",
             "correct": True},
            {"text": "Only heavy gases such as carbon dioxide have any mass",
             "correct": False,
             "why": "Classroom air is mostly nitrogen and oxygen, and those "
                    "150 kilograms are nearly all of them"},
            {"text": "A gas gains mass when it is warmed up by a heater",
             "correct": False,
             "why": "Warming a gas spreads it out. The same gas, warm or "
                    "cold, has the same mass"},
        ],
        "figure": None,
    },
    {
        "id": "c4-04-e29",
        "band": "easier",
        "text": "Steel wool is burned in air. Which of these takes part in "
                "the reaction, and so has to be counted in the mass sum?",
        "options": [
            {"text": "The nitrogen in the air",
             "correct": False,
             "why": "Most of the air is nitrogen and it takes no part here, "
                    "so its mass is the same before and after"},
            {"text": "Heat from the flame",
             "correct": False,
             "why": "Heat is not a substance and has no mass to put in a sum"},
            {"text": "The oxygen in the air",
             "correct": True},
            {"text": "The tongs that hold the wool in the flame",
             "correct": False,
             "why": "The tongs are apparatus. They do not react, so they "
                    "belong in no part of the sum"},
        ],
        "figure": None,
    },
    {
        "id": "c4-04-e30",
        "band": "easier",
        "text": "A carbonate is heated in an open crucible until no more gas "
                "comes off. The crucible and its contents have a mass of "
                "12.50 g before heating and 7.30 g afterwards. What mass of "
                "gas escaped?",
        "options": [
            {"text": "19.80 g",
             "correct": False,
             "why": "The two readings have been added. The gas is what is "
                    "missing between them"},
            {"text": "5.20 g",
             "correct": True},
            {"text": "7.30 g",
             "correct": False,
             "why": "That is the crucible and what stayed in it, not the part "
                    "that left"},
            {"text": "12.50 g",
             "correct": False,
             "why": "That is everything before heating, gas included. Only "
                    "part of it escaped"},
        ],
        "figure": None,
    },
    {
        "id": "c4-04-e31",
        "band": "easier",
        "text": "A student says that when a firework burns there is less left "
                "afterwards, so burning must destroy matter. What is the "
                "correct reply?",
        "options": [
            {"text": "The products were gases, and they went into the air",
             "correct": True},
            {"text": "Burning really does destroy a little matter",
             "correct": False,
             "why": "No reaction destroys matter. Every atom in the firework "
                    "is still somewhere after it has gone off"},
            {"text": "The missing mass was turned into the light and sound "
                     "given out",
             "correct": False,
             "why": "Light and sound are not substances and carry no mass "
                    "away from the firework"},
            {"text": "Firework chemicals are too light for a balance to weigh",
             "correct": False,
             "why": "They weigh perfectly well. What escaped a weighing was "
                    "the gas, not the solid"},
        ],
        "figure": None,
    },
    {
        "id": "c4-04-e32",
        "band": "easier",
        "text": "A reaction has two reactants and one product. Which line "
                "writes the conservation-of-mass rule correctly for it?",
        "options": [
            {"text": "reactant 1 = reactant 2 + product",
             "correct": False,
             "why": "This puts one reactant on its own against the other "
                    "reactant plus the product, which is not what happened"},
            {"text": "reactant 1 × reactant 2 = product",
             "correct": False,
             "why": "Conservation of mass is a sum. Two masses are never "
                    "multiplied together"},
            {"text": "reactant 1 + reactant 2 + product = 0",
             "correct": False,
             "why": "A total mass is never zero. The reactants add up to the "
                    "product, not to nothing"},
            {"text": "reactant 1 + reactant 2 = product",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c4-04-s11",
        "band": "standard",
        "text": "A student heats 6.35 g of copper in air until it has all "
                "become 7.95 g of black copper oxide. Her partner repeats the "
                "experiment with twice as much copper. What mass of oxygen "
                "joins the copper in the partner's run?",
        "options": [
            {"text": "1.60 g",
             "correct": False,
             "why": "That is the oxygen for the first run. The partner used "
                    "twice as much copper, so twice as much oxygen joins"},
            {"text": "12.70 g",
             "correct": False,
             "why": "That is the partner's copper, not the oxygen that joined "
                    "it"},
            {"text": "3.20 g",
             "correct": True},
            {"text": "15.90 g",
             "correct": False,
             "why": "That is the partner's copper oxide. The oxygen is the "
                    "part of it that came out of the air"},
        ],
        "figure": None,
    },
    {
        "id": "c4-04-s12",
        "band": "standard",
        "text": "18.00 g of blue hydrated copper sulfate is heated in an open "
                "dish until 11.50 g of white powder is left. The rest was "
                "driven off as water vapour. What mass of water vapour was "
                "driven off, and where is it now?",
        "options": [
            {"text": "6.50 g, now in the air of the room",
             "correct": True},
            {"text": "6.50 g, destroyed by the heating",
             "correct": False,
             "why": "The arithmetic is right and the conclusion is not. "
                    "Heating drove the water off; it did not destroy it"},
            {"text": "29.50 g, now spread through the air of the room",
             "correct": False,
             "why": "The two readings have been added. What left is the "
                    "difference between them"},
            {"text": "11.50 g, now in the air of the room",
             "correct": False,
             "why": "That is the white powder still sitting in the dish, not "
                    "the part that went into the air"},
        ],
        "figure": None,
    },
    {
        "id": "c4-04-s13",
        "band": "standard",
        "text": "The marble-and-acid reaction is run in a conical flask "
                "plugged with cotton wool instead of a stopper. The balance "
                "reading still falls. Why?",
        "options": [
            {"text": "The cotton wool soaks up some of the acid",
             "correct": False,
             "why": "Soaked-up acid is still inside the flask and still on "
                    "the pan, so it cannot make a reading fall"},
            {"text": "Cotton wool lets gas through, so the flask is not "
                     "sealed",
             "correct": True},
            {"text": "The gas is destroyed as it passes through the cotton "
                     "wool",
             "correct": False,
             "why": "Cotton wool destroys nothing. The gas goes straight "
                    "through it and into the room"},
            {"text": "The cotton wool adds mass of its own, which hides the "
                     "real change",
             "correct": False,
             "why": "The plug is on the pan before and after, so its mass "
                    "cancels — and this reaction gains nothing anyway"},
        ],
        "figure": None,
    },
    {
        "id": "c4-04-s14",
        "band": "standard",
        "text": "Magnesium is burned in a crucible whose lid is lifted from "
                "time to time to let air in. The magnesium burns completely, "
                "but the measured gain in mass is smaller than it should be. "
                "Suggest why.",
        "options": [
            {"text": "Heat escaped through the gap, and heat has mass",
             "correct": False,
             "why": "Heat carries no mass a balance can read, so letting it "
                    "out changes no reading"},
            {"text": "The gap let oxygen out, so no oxide formed",
             "correct": False,
             "why": "The magnesium burned completely, so oxide plainly did "
                    "form. Lifting the lid lets air IN, which is the point"},
            {"text": "Some magnesium oxide smoke escaped and was not weighed",
             "correct": True},
            {"text": "The lid was on the pan at the start anyway",
             "correct": False,
             "why": "The lid is on the pan before and after, so its mass "
                    "cancels out and cannot explain a gain that came out too "
                    "small"},
        ],
        "figure": None,
    },
    {
        "id": "c4-04-s15",
        "band": "standard",
        "text": "In a sealed flask, 4.60 g of substance A reacts with an "
                "unknown mass of substance B. The reaction makes 5.40 g of "
                "one product and 1.90 g of another, and nothing is left over. "
                "What mass of B was used?",
        "options": [
            {"text": "7.30 g",
             "correct": False,
             "why": "That is both products together, which equals A and B "
                    "added. B is what is left when A is taken off it"},
            {"text": "0.80 g",
             "correct": False,
             "why": "Only one product has been used. Both of them came from A "
                    "and B, so both count"},
            {"text": "11.90 g",
             "correct": False,
             "why": "A has been added to the products instead of taken away "
                    "from them"},
            {"text": "2.70 g",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c4-04-s16",
        "band": "standard",
        "text": "Two students each burn 2.40 g of magnesium completely: one "
                "in an open crucible, one in a sealed tube holding plenty of "
                "air. Whose magnesium oxide has the greater mass?",
        "options": [
            {"text": "The open one, because it has an unlimited supply of air",
             "correct": False,
             "why": "Both had enough air to burn all the magnesium, and the "
                    "magnesium decides how much oxide there can be"},
            {"text": "The sealed one, because nothing at all can escape from "
                     "the tube",
             "correct": False,
             "why": "Sealing changes what the BALANCE sees, not how much "
                    "oxide the reaction makes"},
            {"text": "It cannot be told without the readings",
             "correct": False,
             "why": "It can: the same mass of magnesium burned completely "
                    "gives the same mass of oxide every time"},
            {"text": "Neither — both make 4.00 g of magnesium oxide",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c4-04-s17",
        "band": "standard",
        "text": "A student claims that any reaction giving off a gas must "
                "lose mass. Which case disproves the claim?",
        "options": [
            {"text": "The same reaction run in a sealed flask, which loses "
                     "nothing",
             "correct": True},
            {"text": "A reaction that makes no gas at all, so nothing can be "
                     "lost",
             "correct": False,
             "why": "The claim is only about reactions that DO give off a "
                    "gas, so this case never tests it"},
            {"text": 'Any hot reaction, because the heat given out replaces the '
                     'lost mass',
             "correct": False,
             "why": "Heat replaces nothing on a balance. A hot flask that has "
                    "lost gas still reads lower"},
            {"text": 'Any reaction giving off its gas very slowly indeed',
             "correct": False,
             "why": "Slow gas is still gas leaving. Wait long enough and the "
                    "reading falls by just as much"},
        ],
        "figure": None,
    },
    {
        "id": "c4-04-s18",
        "band": "standard",
        "text": "A student says that a reaction which gives out a lot of heat "
                "must lose mass, because energy has left the flask. What is "
                "the correct reply?",
        "options": [
            {"text": "A reaction that gets hot always loses some of its mass",
             "correct": False,
             "why": "Warm a sealed flask's reaction as much as you like: the "
                    "reading does not move"},
            {"text": "That is true, unless the flask has been sealed "
                     "beforehand",
             "correct": False,
             "why": "Sealing is not what saves the mass. Heat takes no "
                    "measurable mass out of an open flask either"},
            {"text": "Heat carries no mass a balance can read; the atoms all "
                     "stay",
             "correct": True},
            {"text": "The mass rises instead, because the heat is added to "
                     "the products",
             "correct": False,
             "why": "Heat is not a substance being added to anything, so it "
                    "cannot push a reading up"},
        ],
        "figure": None,
    },
    {
        "id": "c4-04-s19",
        "band": "standard",
        "text": "A student weighs a beaker holding the reactants: 24.00 g. "
                "The reaction is run in the open, and the reading falls to "
                "22.60 g. What mass of gas escaped, and does the beaker's own "
                "mass matter?",
        "options": [
            {"text": "1.40 g, and yes — the beaker has to be weighed on its "
                     "own first",
             "correct": False,
             "why": "The mass of gas is a difference, and any fixed mass in "
                    "both readings drops out of a difference"},
            {"text": "1.40 g, and no — the beaker's mass is in both readings",
             "correct": True},
            {"text": "22.60 g, and no — the beaker never needs weighing",
             "correct": False,
             "why": "22.60 g is what is still in the beaker. The gas is what "
                    "is missing between the two readings"},
            {"text": "46.60 g, and no — the two readings should be added up",
             "correct": False,
             "why": "Adding them gives a mass that was never on the pan. The "
                    "gas is the fall, not the sum"},
        ],
        "figure": None,
    },
    {
        "id": "c4-04-s20",
        "band": "standard",
        "text": "A candle in an open room burns away until almost nothing is "
                "left of it. Which substances make up the missing mass, and "
                "where are they now?",
        "options": [
            {"text": "Soot and ash, now sitting on the candle holder",
             "correct": False,
             "why": "A clean candle flame leaves almost no solid behind, and "
                    "anything on the holder was never missing"},
            {"text": "Heat and light, now spread out through the room",
             "correct": False,
             "why": "Heat and light are not substances and have no mass to "
                    "account for the wax that has gone"},
            {"text": "Nothing — the wax was destroyed as it burned",
             "correct": False,
             "why": "Every atom of the wax is still in the room, joined to "
                    "oxygen from the air"},
            {"text": "Carbon dioxide and water vapour, now in the air",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c4-04-s21",
        "band": "standard",
        "text": "A decomposition is run twice, starting with 10.00 g of the "
                "same solid each time. In an open crucible the contents end "
                "at 6.40 g; in a sealed tube they end at 10.00 g. What mass "
                "of gas was made in the SEALED tube?",
        "options": [
            {"text": "0.00 g, because the balance did not move",
             "correct": False,
             "why": "An unmoved balance means nothing crossed the seal, not "
                    "that nothing was made"},
            {"text": "10.00 g, because everything stayed inside",
             "correct": False,
             "why": "That is everything in the tube, solid included, not the "
                    "gas on its own"},
            {"text": "3.60 g — the same reaction makes the same gas",
             "correct": True},
            {"text": "It cannot be worked out from a sealed tube",
             "correct": False,
             "why": "It can, from the open run: the same solid decomposing "
                    "the same way makes the same mass of gas"},
        ],
        "figure": None,
    },
    {
        "id": "c4-04-s22",
        "band": "standard",
        "text": "6.00 g of a metal is heated in a sealed flask of air. "
                "Afterwards the flask holds 7.00 g of metal oxide and 2.00 g "
                "of metal that never reacted. What mass of oxygen joined the "
                "metal?",
        "options": [
            {"text": "3.00 g",
             "correct": True},
            {"text": "5.00 g",
             "correct": False,
             "why": "The unreacted metal has been taken off the oxide. Only "
                    "the 4.00 g that DID react is inside that oxide"},
            {"text": "1.00 g",
             "correct": False,
             "why": "This compares the oxide with all 6.00 g of metal, "
                    "including the 2.00 g that never took any oxygen"},
            {"text": "9.00 g",
             "correct": False,
             "why": "The leftover metal has been added instead of set aside. "
                    "It is not part of the oxide at all"},
        ],
        "figure": None,
    },
    {
        "id": "c4-04-s23",
        "band": "standard",
        "text": "A reaction gives off 0.004 g of gas into the room. Balance A "
                "reads to the nearest 0.01 g and balance B reads to the "
                "nearest 0.001 g. Which balance would show a change, and what "
                "does that tell you about the rule?",
        "options": [
            {"text": "A only, because a bigger step on the scale shows a "
                     "bigger loss",
             "correct": False,
             "why": "A bigger step hides small changes rather than showing "
                    "them. Balance A cannot resolve 0.004 g at all"},
            {"text": "B only — the rule is exact even when an instrument "
                     "cannot show it",
             "correct": True},
            {"text": "Both, because a balance always shows whatever has "
                     "happened",
             "correct": False,
             "why": "Every instrument has a smallest step it can read, and "
                    "anything under it is invisible to it"},
            {"text": "Neither, because a loss that small is not really a loss "
                     "at all",
             "correct": False,
             "why": "The gas is real and so is its mass. What is limited is "
                    "the balance, not the loss"},
        ],
        "figure": None,
    },
    {
        "id": "c4-04-s24",
        "band": "standard",
        "text": "The same reaction is run twice with the same masses of "
                "reactants: once at room temperature and once warmed so that "
                "it goes much faster. How do the total masses of the products "
                "compare?",
        "options": [
            {"text": "More in the warm one — it reacted faster",
             "correct": False,
             "why": "Speed changes how long it takes, not how much there is "
                    "to make it from"},
            {"text": "The same in both, because the same atoms are rearranged",
             "correct": True},
            {"text": "Less in the warm one, because heat carried some mass "
                     "away",
             "correct": False,
             "why": "Heat carries no mass a balance can read, warm reaction "
                    "or cold"},
            {"text": "More in the warm one, because the heat was added into "
                     "the products",
             "correct": False,
             "why": "Energy going in is not matter going in. The products "
                    "hold only the atoms the reactants brought"},
        ],
        "figure": None,
    },
    {
        "id": "c4-04-s25",
        "band": "standard",
        "text": "Why is a conservation-of-mass experiment usually run in a "
                "sealed flask rather than an open one?",
        "options": [
            {"text": "So that the reaction runs faster and finishes sooner",
             "correct": False,
             "why": "Sealing does not speed a reaction up. It changes what "
                    "can cross the neck, nothing else"},
            {"text": "So that no air can get in and slow the reaction down "
                     "midway",
             "correct": False,
             "why": "Air getting in would make some reactions go further, not "
                    "slower — and either way the point of the seal is the gas "
                    "leaving"},
            {"text": "So that any gas made stays on the pan and is weighed",
             "correct": True},
            {"text": "So that the heat cannot escape and change the mass",
             "correct": False,
             "why": "Escaping heat changes no reading, so there is nothing to "
                    "keep in"},
        ],
        "figure": None,
    },
    {
        "id": "c4-04-s26",
        "band": "standard",
        "text": "A student weighs 25.00 g of reactants into a sealed flask, "
                "runs the reaction, then unseals the flask and weighs it "
                "again, getting 23.80 g. Explain the two readings.",
        "options": [
            {"text": "The reaction destroyed 1.20 g once the flask was opened",
             "correct": False,
             "why": "Opening a flask does not start destroying anything. The "
                    "reaction had already finished"},
            {"text": "The balance must have drifted between the first and "
                     "second weighing",
             "correct": False,
             "why": "1.20 g is far too big for drift, and the same experiment "
                    "gives the same fall every time"},
            {"text": "1.20 g of air got in and then left again",
             "correct": False,
             "why": "Air moving in and out again would leave the reading "
                    "where it started"},
            {"text": "Mass was conserved; 1.20 g of gas escaped on opening",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c4-04-s27",
        "band": "standard",
        "text": "A sealed flask and its contents have a mass of 310.00 g. A "
                "reaction inside makes a gas, and the flask gets hot. What is "
                "the mass of the flask and contents while the reaction is "
                "still going on?",
        "options": [
            {"text": "310.00 g, because nothing has entered or left",
             "correct": True},
            {"text": "More than 310.00 g, because the gas takes up room",
             "correct": False,
             "why": "Taking up room is volume, not mass. The gas was made "
                    "from what was already in the flask"},
            {"text": "Less than 310.00 g, because heat is leaving the flask",
             "correct": False,
             "why": "Heat leaves through the glass all the time and takes no "
                    "measurable mass with it"},
            {"text": "310.00 g only once the reaction has finished",
             "correct": False,
             "why": "The total is unchanged at every moment, including "
                    "halfway through"},
        ],
        "figure": None,
    },
    {
        "id": "c4-04-s28",
        "band": "standard",
        "text": "Two flasks run the same gas-producing reaction, one open and "
                "one sealed. Which one can be used to measure the mass of gas "
                "given off, and why?",
        "options": [
            {"text": "The sealed one, because nothing is ever lost out of it "
                     "at all",
             "correct": False,
             "why": "Nothing lost means nothing to measure: its reading is "
                    "the same before and after"},
            {"text": "The sealed one — its reading is more accurate",
             "correct": False,
             "why": "Both readings are equally accurate. Only one of them "
                    "changes by the mass of the gas"},
            {"text": "The open one — the fall in its reading is the gas",
             "correct": True},
            {"text": "Neither, because a gas can never be weighed directly",
             "correct": False,
             "why": "A gas is weighed the same way as anything else: by the "
                    "difference it makes to a reading"},
        ],
        "figure": None,
    },
    {
        "id": "c4-04-s29",
        "band": "standard",
        "text": "In a sealed flask, 3.20 g of sulfur burns completely with "
                "3.20 g of oxygen to make sulfur dioxide. What mass of sulfur "
                "dioxide is made, and what would the same burn in an open "
                "dish have shown?",
        "options": [
            {"text": "6.40 g, and an open dish would have shown no change",
             "correct": False,
             "why": "In an open dish the sulfur dioxide drifts away, so the "
                    "reading drops"},
            {"text": "6.40 g, and an open dish would have shown a loss",
             "correct": True},
            {"text": "3.20 g, and an open dish would have shown a gain",
             "correct": False,
             "why": "Both reactants are in the product, so it is heavier than "
                    "either of them"},
            {"text": "0.00 g, and an open dish would have shown a loss",
             "correct": False,
             "why": "A sealed flask that does not change its reading is still "
                    "full of product"},
        ],
        "figure": None,
    },
    {
        "id": "c4-04-s30",
        "band": "standard",
        "text": "Iron filings and sulfur are heated together in a test tube "
                "open at the top. They make iron sulfide, and the mass on the "
                "balance hardly changes. Why is that what you would expect?",
        "options": [
            {"text": "Because iron sulfide weighs the same as the iron",
             "correct": False,
             "why": "The sulfur is in the sulfide too, so it is heavier than "
                    "the iron was"},
            {"text": "Because the tube is too narrow for gas to get out",
             "correct": False,
             "why": "A narrow tube is still open. A gas would leave it "
                    "perfectly well if one were made"},
            {"text": "Because solids never change mass when heated",
             "correct": False,
             "why": "Plenty of solids do — a carbonate loses mass and a metal "
                    "gains it. It depends on whether a gas crosses"},
            {"text": "Because no gas is made or used, so nothing crosses the "
                     "mouth",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c4-04-s31",
        "band": "standard",
        "text": "Conservation applies to the MASS of the reactants and "
                "products, and not to the space they take up. Why does the "
                "rule not work for volume?",
        "options": [
            {"text": "A gas takes up far more room than the solid it came "
                     "from",
             "correct": True},
            {"text": "Volume is conserved too, but it is harder to measure "
                     "well",
             "correct": False,
             "why": "It is not conserved at all: a carbonate the size of a "
                    "pea makes gas that fills a jar"},
            {"text": "The volume of a gas cannot be measured in a school lab",
             "correct": False,
             "why": "A gas syringe measures it easily. Measuring it is not "
                    "the problem; it simply is not conserved"},
            {"text": "Mass and volume are really the same thing for a gas",
             "correct": False,
             "why": "They are different quantities with different units, for "
                    "a gas as much as for anything else"},
        ],
        "figure": None,
    },
    {
        "id": "c4-04-s32",
        "band": "standard",
        "text": "The gas from a reaction is led into a syringe that was "
                "weighed empty and weighed again when full. The reaction "
                "flask loses 0.88 g and the syringe gains 0.88 g. What do the "
                "two measurements together show?",
        "options": [
            {"text": "The gas gained mass as it travelled along the rubber "
                     "tube",
             "correct": False,
             "why": "Travelling changes nothing. The syringe gained exactly "
                    "what the flask lost, with nothing added on the way"},
            {"text": "The syringe made the gas heavier by squashing it into a "
                     "smaller space",
             "correct": False,
             "why": "Squashing a gas changes the room it takes up, not its "
                    "mass"},
            {"text": "All the gas that left the flask is still there, so mass "
                     "is conserved",
             "correct": True},
            {"text": "The flask must have leaked, since two different masses "
                     "changed",
             "correct": False,
             "why": "A leak would mean the syringe gained LESS than the flask "
                    "lost. The two figures matching is the proof there was no "
                    "leak"},
        ],
        "figure": None,
    },
    {
        "id": "c4-04-h11",
        "band": "harder",
        "text": "A tree grows from a seedling into 400 kg of wood, while the "
                "soil in its tub loses only a few kilograms over the same "
                "years. Where has almost all of the tree's mass come from?",
        "options": [
            {"text": "From the soil, which rain replaces",
             "correct": False,
             "why": "The tub would have had to lose 400 kg of soil, and it "
                    "lost a few. Rain carries no soil into a tub"},
            {"text": "From carbon dioxide in the air, and from water",
             "correct": True},
            {"text": "From the sunlight the leaves took in",
             "correct": False,
             "why": "Light is the energy for the reaction, not the matter. "
                    "Light has no mass to build wood out of"},
            {"text": "From the water the roots draw up",
             "correct": False,
             "why": "Water supplies part of it, but most of the dry wood is "
                    "carbon, and that carbon came out of the air"},
        ],
        "figure": None,
    },
    {
        "id": "c4-04-h12",
        "band": "harder",
        "text": "A car airbag inflates when a solid inside it decomposes into "
                "a gas. The bag stays sealed all the way through. How does "
                "the mass of the inflated bag compare with the bag before it "
                "fired?",
        "options": [
            {"text": "The same, because the gas came from the solid inside",
             "correct": True},
            {"text": "Greater, because the gas fills a much larger volume",
             "correct": False,
             "why": "Volume is the space something takes up. Spreading the "
                    "same matter out further adds no mass"},
            {"text": "Greater, because air rushed in to fill the bag out",
             "correct": False,
             "why": "The bag is sealed, so no air can get in. The gas inside "
                    "it was made from the solid"},
            {"text": "Smaller, because a gas is lighter than a solid",
             "correct": False,
             "why": "A gas is less dense, not lighter overall. All of the "
                    "solid's atoms are still in the bag"},
        ],
        "figure": None,
    },
    {
        "id": "c4-04-h13",
        "band": "harder",
        "text": "A sealed flask and its contents have a mass of 96.00 g. A "
                "reaction inside makes a gas. The flask is then opened, all "
                "the gas escapes, and it reads 93.60 g. The whole experiment "
                "is repeated with half as much of every reactant. What mass "
                "of gas escapes the second time?",
        "options": [
            {"text": "2.40 g",
             "correct": False,
             "why": "That is the first run's gas. Half of everything makes "
                    "half as much gas"},
            {"text": "4.80 g",
             "correct": False,
             "why": "This doubles the first run instead of halving it"},
            {"text": "46.80 g",
             "correct": False,
             "why": "A balance reading has been halved rather than the mass "
                    "of gas, and most of that reading is the flask"},
            {"text": "1.20 g",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c4-04-h14",
        "band": "harder",
        "text": "Before Lavoisier, chemists weighed a burning candle and "
                "watched the mass fall, then weighed a burning metal and "
                "watched it rise. Why did those two results make burning so "
                "hard to explain with a single idea?",
        "options": [
            {"text": "Metals and candles are made of two completely different "
                     "elements",
             "correct": False,
             "why": "They are, but that is true of most pairs of substances "
                    "and explains neither reading"},
            {"text": "Nobody could weigh a candle accurately enough back then",
             "correct": False,
             "why": "Balances of the time managed it well. The readings were "
                    "real; it was the explanation that was missing"},
            {"text": "One looked like matter leaving and the other like "
                     "matter arriving",
             "correct": True},
            {"text": "A metal will not burn at all unless it is sealed in",
             "correct": False,
             "why": "Metals burn in open air perfectly well, and they gain "
                    "mass when they do"},
        ],
        "figure": None,
    },
    {
        "id": "c4-04-h15",
        "band": "harder",
        "text": "A rocket carries 3.0 tonnes of fuel and 12.0 tonnes of "
                "liquid oxygen, and its total mass on the launch pad is 20.0 "
                "tonnes. All the fuel and oxygen burn, and every bit of the "
                "exhaust leaves the rocket. What is the rocket's mass then?",
        "options": [
            {"text": "8.0 tonnes",
             "correct": False,
             "why": "Only the oxygen has been taken off. The fuel left as "
                    "part of the exhaust too"},
            {"text": "5.0 tonnes",
             "correct": True},
            {"text": "15.0 tonnes",
             "correct": False,
             "why": "That is the exhaust that left, not the rocket that "
                    "stayed"},
            {"text": "20.0 tonnes",
             "correct": False,
             "why": "That was the mass on the pad. Fifteen tonnes of it has "
                    "gone out of the nozzle"},
        ],
        "figure": None,
    },
    {
        "id": "c4-04-h16",
        "band": "harder",
        "text": "24.00 g of a metal is sealed in a tube with 16.00 g of "
                "sulfur and heated. Afterwards the tube holds 35.00 g of "
                "metal sulfide, along with whatever did not react. What mass "
                "of unreacted material is in the tube?",
        "options": [
            {"text": "5.00 g",
             "correct": True},
            {"text": "11.00 g",
             "correct": False,
             "why": "Only the metal has been compared with the sulfide. The "
                    "sulfur was sealed in as well"},
            {"text": "19.00 g",
             "correct": False,
             "why": "Only the sulfur has been compared with the sulfide, "
                    "leaving the metal out of the total"},
            {"text": "75.00 g",
             "correct": False,
             "why": "The sulfide has been added to the reactants. It is made "
                    "OF them, so it is part of the same 40.00 g"},
        ],
        "figure": None,
    },
    {
        "id": "c4-04-h17",
        "band": "harder",
        "text": "One open reaction makes a balance reading rise, and another "
                "makes it fall. State what is the same about the two "
                "reactions.",
        "options": [
            {"text": "In both, a gas has left the pan and gone into the room",
             "correct": False,
             "why": "That is true of the falling one only. In the rising one "
                    "a gas joined from the air"},
            {"text": "In both, oxygen from the air has taken part in the "
                     "reaction",
             "correct": False,
             "why": "A carbonate fizzing in acid takes no oxygen from the "
                    "air, and its reading still falls"},
            {"text": "In both, the products weigh more than the reactants did",
             "correct": False,
             "why": "Products never weigh more than the reactants. Counted "
                    "properly the two are equal"},
            {"text": "In both, the total mass of everything involved is "
                     "unchanged",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c4-04-h18",
        "band": "harder",
        "text": "A sealed flask on a balance reads 240.00 g. The reaction "
                "inside pushes the stopper out, gas escapes into the room, "
                "and the stopper lands on the pan beside the flask. What does "
                "the balance read now?",
        "options": [
            {"text": "240.00 g, because the stopper is still on the pan",
             "correct": False,
             "why": "The stopper is, and the gas is not. It is the gas "
                    "leaving that moves the reading"},
            {"text": "Less than 240.00 g, by the mass of the stopper",
             "correct": False,
             "why": "The stopper never left the pan, so its mass is still in "
                    "the reading"},
            {"text": "Less than 240.00 g, by the mass of gas that escaped",
             "correct": True},
            {"text": "More than 240.00 g, because the stopper now presses "
                     "down",
             "correct": False,
             "why": "Resting somewhere else on the pan does not change what "
                    "the pan is carrying"},
        ],
        "figure": None,
    },
    {
        "id": "c4-04-h19",
        "band": "harder",
        "text": "A hand warmer holds iron powder that rusts once the packet "
                "is opened to the air. The packet is weighed sealed, then "
                "opened and left on the balance until it stops giving out "
                "heat, then weighed again. Predict the two readings.",
        "options": [
            {"text": "The second is lower, because heat has been given out",
             "correct": False,
             "why": "Heat leaving takes no measurable mass with it, however "
                    "warm the packet gets"},
            {"text": "The second is higher, because oxygen has joined the "
                     "iron",
             "correct": True},
            {"text": "The second is the same, because it was sealed at the "
                     "start",
             "correct": False,
             "why": "It was opened before the rusting, so the oxygen that "
                    "joined came from outside the pan"},
            {"text": "The second is lower, because the iron has been used up",
             "correct": False,
             "why": "The iron is used up into rust, which is still in the "
                    "packet and is heavier than the iron was"},
        ],
        "figure": None,
    },
    {
        "id": "c4-04-h20",
        "band": "harder",
        "text": 'A manager argues that if 100 tonnes of raw material goes into '
                'a chemical works, 100 tonnes must come out of it, counting '
                'product and waste together. Evaluate the argument.',
        "options": [
            {"text": 'Right — the mass is all still there, though not all of it '
                     'is product',
             "correct": True},
            {"text": 'Wrong — whatever leaves as waste is lost from the total',
             "correct": False,
             "why": 'Waste is matter in the wrong place, not matter gone '
                    'missing. It still counts towards the 100 tonnes'},
            {"text": 'Wrong — the heat the works gives out carries away part of '
                     'the mass',
             "correct": False,
             "why": 'Heat carries no mass a balance can read, so nothing leaves '
                    'the total that way'},
            {"text": 'Right, but only for a works that makes no waste at all',
             "correct": False,
             "why": 'The total holds whether or not there is waste; waste is '
                    'simply part of what comes out'},
        ],
        "figure": None,
    },
    {
        "id": "c4-04-h21",
        "band": "harder",
        "text": "In a sealed flask, 5.00 g of A reacts with 8.00 g of B to "
                "give 9.00 g of C and a second product, D. The reaction is "
                "repeated with 10.00 g of A and 16.00 g of B. What mass of D "
                "is made the second time?",
        "options": [
            {"text": "4.00 g",
             "correct": False,
             "why": "That is D from the first run. Twice as much of "
                    "everything makes twice as much D"},
            {"text": "18.00 g",
             "correct": False,
             "why": "That is C for the second run, not D"},
            {"text": "26.00 g",
             "correct": False,
             "why": "That is everything put into the second flask, C included"},
            {"text": "8.00 g",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c4-04-h22",
        "band": "harder",
        "text": "The conservation-of-mass rule puts the word total on each "
                "side of the equals sign. Why is that word needed?",
        "options": [
            {"text": "Because the total is always larger than any single one "
                     "of the masses",
             "correct": False,
             "why": "Size is not the point. A reaction with one reactant and "
                    "one product still obeys the rule"},
            {"text": "Because a balance can only ever read one total at a "
                     "time",
             "correct": False,
             "why": "What a balance can read has nothing to do with how the "
                    "rule is written"},
            {"text": "Because there may be several reactants or products, and "
                     "all count",
             "correct": True},
            {"text": "Because the rule only works when there are exactly two "
                     "reactants",
             "correct": False,
             "why": "It works whatever the number. That is precisely why the "
                    "word total is there"},
        ],
        "figure": None,
    },
    {
        "id": "c4-04-h23",
        "band": "harder",
        "text": "3.00 g of magnesium is burned completely on an open balance, "
                "and some of the white smoke drifts off the pan. The measured "
                "mass of oxygen that joined in comes out at 1.40 g, when the "
                "true value is 2.00 g. Why is the measured value too low?",
        "options": [
            {"text": "Because the smoke was weighed twice",
             "correct": False,
             "why": "Weighing something twice would push the figure up, not "
                    "down, and the smoke was never weighed at all"},
            {"text": "Because some magnesium oxide left the pan as smoke",
             "correct": True},
            {"text": "Because some oxygen escaped before it could react with "
                     "the metal",
             "correct": False,
             "why": "The magnesium burned completely, so it got all the "
                    "oxygen it needed"},
            {"text": "Because the ash left behind is lighter than the oxide "
                     "is",
             "correct": False,
             "why": "What is left IS the oxide. There is simply less of it on "
                    "the pan than was made"},
        ],
        "figure": None,
    },
    {
        "id": "c4-04-h24",
        "band": "harder",
        "text": "A carbonate is heated in an open crucible, cooled and "
                "weighed: 9.40 g. It is heated, cooled and weighed a second "
                "time, and reads 9.40 g again. Why is the second weighing "
                "done, and what does the repeat tell you?",
        "options": [
            {"text": "To check the decomposition is finished — no more gas is "
                     "coming off",
             "correct": True},
            {"text": "To give the reaction a second chance to start",
             "correct": False,
             "why": "It had already started and run. The second heating tests "
                    "whether it had anything left to do"},
            {"text": "Because a hot crucible always has to be weighed twice "
                     "over",
             "correct": False,
             "why": "There is no such rule. What is repeated is the HEATING, "
                    "until two weighings agree, and that is about the "
                    "reaction rather than the crucible"},
            {"text": "To let the escaped gas find its way back in",
             "correct": False,
             "why": "Gas that has gone into the room does not come back, and "
                    "nobody would want it to"},
        ],
        "figure": None,
    },
    {
        "id": "c4-04-h25",
        "band": "harder",
        "text": "A bottle of fizzy water is weighed with its cap on: 520.00 "
                "g. The cap is taken off, the water goes flat over a day, and "
                "the bottle is weighed again: 519.30 g. The cap is screwed "
                "back on and it is weighed once more. What is the third "
                "reading?",
        "options": [
            {"text": "520.00 g, because the cap has been put back on",
             "correct": False,
             "why": "Replacing the cap keeps the rest in. It cannot bring "
                    "back gas that is already in the room"},
            {"text": "518.60 g, because more gas escapes each time",
             "correct": False,
             "why": "The water is flat, so there is no more gas to lose, and "
                    "the cap is on"},
            {"text": "It cannot be predicted until it is measured",
             "correct": False,
             "why": "It can: nothing has crossed the neck since the second "
                    "weighing"},
            {"text": "519.30 g, because the escaped gas cannot come back",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c4-04-h26",
        "band": "harder",
        "text": "Reaction X in an open flask makes a reading fall by 2.00 g. "
                "Reaction Y, in a separate open flask on another bench, makes "
                "a reading rise by 2.00 g. A student says the two reactions "
                "swapped 2.00 g between them. Evaluate.",
        "options": [
            {"text": "Correct, because the two changes must always balance "
                     "out",
             "correct": False,
             "why": "Nothing makes two unrelated flasks balance each other. "
                    "The match here is a coincidence"},
            {"text": "Correct, because gas moves from a falling flask to a "
                     "rising one",
             "correct": False,
             "why": "Y takes oxygen from the whole room's air, not from one "
                    "flask across the lab"},
            {"text": "Wrong — one lost gas to the room and the other took gas "
                     "from it",
             "correct": True},
            {"text": "Wrong — a balance reading cannot rise during a reaction "
                     "at all",
             "correct": False,
             "why": "It can, and Y just did. A metal taking oxygen from the "
                    "air gains mass on the pan"},
        ],
        "figure": None,
    },
    {
        "id": "c4-04-h27",
        "band": "harder",
        "text": "Three students run the same sealed reaction and record mass "
                "changes of 0.00 g, −0.01 g and +0.01 g. What do the results "
                "show?",
        "options": [
            {"text": "That mass was destroyed in one run and created in "
                     "another",
             "correct": False,
             "why": "A hundredth of a gram either way is the balance's last "
                    "digit wavering, not matter appearing"},
            {"text": "That mass was conserved, within what the balance can "
                     "read",
             "correct": True},
            {"text": "That the seal failed in two of the three runs",
             "correct": False,
             "why": "A failed seal loses gas, so it would show a fall — and a "
                    "much bigger one than this"},
            {"text": "That the results are too scattered to mean anything",
             "correct": False,
             "why": "They agree to a hundredth of a gram, which is as close "
                    "as these balances get"},
        ],
        "figure": None,
    },
    {
        "id": "c4-04-h28",
        "band": "harder",
        "text": "A gas cylinder is weighed full: 42.30 kg. After a heater has "
                "run for a while it weighs 38.10 kg. Burning that gas used "
                "16.80 kg of oxygen from the air. What mass of exhaust gases "
                "went up the flue?",
        "options": [
            {"text": "21.00 kg",
             "correct": True},
            {"text": "4.20 kg",
             "correct": False,
             "why": "That is the gas burned. The oxygen it burned with is in "
                    "the exhaust too"},
            {"text": "12.60 kg",
             "correct": False,
             "why": "The gas has been subtracted from the oxygen. Both of "
                    "them went into the exhaust, so they add"},
            {"text": "16.80 kg",
             "correct": False,
             "why": "That is the oxygen alone, leaving out the fuel it "
                    "combined with"},
        ],
        "figure": None,
    },
    {
        "id": "c4-04-h29",
        "band": "harder",
        "text": "In one experiment 7.00 g of iron combines with 4.00 g of "
                "sulfur and nothing is left over. A second experiment uses "
                "21.00 g of iron with plenty of sulfur. What mass of iron "
                "sulfide is made in the second experiment?",
        "options": [
            {"text": "25.00 g",
             "correct": False,
             "why": "The first experiment's sulfur has been used with the "
                    "second experiment's iron. Three times the iron takes "
                    "three times the sulfur"},
            {"text": "11.00 g",
             "correct": False,
             "why": "That is the first experiment's sulfide, not the second's"},
            {"text": "63.00 g",
             "correct": False,
             "why": "That is three times the iron alone, which is not a mass "
                    "of sulfide at all"},
            {"text": "33.00 g",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c4-04-h30",
        "band": "harder",
        "text": "A student argues that conservation of mass cannot really be "
                "tested in a school lab, because every reaction worth "
                "watching gives off a gas. Evaluate the argument.",
        "options": [
            {"text": "It is right: a school balance cannot weigh a gas at all",
             "correct": False,
             "why": "A balance weighs a gas as readily as anything else, so "
                    "long as the gas is on the pan"},
            {"text": "It is right: school glassware cannot be sealed properly",
             "correct": False,
             "why": "A bung seals a conical flask well enough for this, which "
                    "is why the sealed run works"},
            {"text": "It overstates the case: many good reactions make no gas "
                     "at all",
             "correct": True},
            {"text": "It is wrong: a gas leaving does not change a reading "
                     "anyway",
             "correct": False,
             "why": "A gas leaving is exactly what makes an open reading fall"},
        ],
        "figure": None,
    },
    {
        "id": "c4-04-h31",
        "band": "harder",
        "text": "The rule is written with an equals sign. What would chemists "
                "have to find before they gave it up?",
        "options": [
            {"text": "A reaction whose reading falls in an open flask",
             "correct": False,
             "why": "Readings fall in open flasks every day, and the rule "
                    "explains why"},
            {"text": "A sealed reaction whose total mass really changed, "
                     "again and again",
             "correct": True},
            {"text": "A reaction giving out much more heat than any other "
                     "known",
             "correct": False,
             "why": "How much heat comes out says nothing about how much "
                    "matter there is"},
            {"text": "A reaction making more products than reactants",
             "correct": False,
             "why": "The number of substances is free to change. It is the "
                    "total MASS that may not"},
        ],
        "figure": None,
    },
    {
        "id": "c4-04-h32",
        "band": "harder",
        "text": "In a sealed flask, 14.00 g of reactant A reacts completely "
                "with 6.00 g of reactant B. The products are 4.50 g of a "
                "solid, 9.00 g of a liquid and a gas. The flask is opened and "
                "all the gas escapes. By how much does the reading fall?",
        "options": [
            {"text": "6.50 g",
             "correct": True},
            {"text": "13.50 g",
             "correct": False,
             "why": "That is the solid and the liquid, which both stayed in "
                    "the flask"},
            {"text": "20.00 g",
             "correct": False,
             "why": "That is everything that was in the flask. Only the gas "
                    "left it"},
            {"text": "2.00 g",
             "correct": False,
             "why": "Only one reactant has been compared with one product. "
                    "All three products came from both reactants"},
        ],
        "figure": None,
    },
]
