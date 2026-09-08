"""C8 lesson 05 — Group 7, the halogens: twelve questions (MRB-281).

The lesson's argument is one shape: a group has a trend, and it is not always
the same trend. The page teaches it with nine tubes — three halogens against
three halide solutions — and the grid comes out triangular, which reads as an
order running the opposite way from group 1's.

These twelve probe the angles the mastery ladder leaves alone: what a
displacement that does NOT happen tells you, what the family resemblance is
when the members are a gas, a liquid and a solid, and why one idea about atom
size produces two opposite trends.

The distractors are built from the lesson's declared misconception.

`PTAB-08` (reactivity always increases going down a group) drives the wrong
options in e02, s01, s04, h01 and h03. Each carries group 1's trend across
unexamined. s04 is the one that matters: it offers a displacement that WOULD
happen if the trend ran downwards, so the belief makes a concrete prediction
and the grid refutes it.

A second strand is that a null result is a result — e04, s02 and h04 turn on a
tube in which nothing changes, which is the observation students discard.

⚠️ THE HALOGENS DO HAVE A DENSITY TREND and h02 uses it. That is not in
tension with c8-04's flag-11 ruling: group 1's densities are not monotonic,
group 7's rise steadily, and the difference is a fact about the two groups
rather than a policy about the word.

⚠️ MRB-278 · ANSWER POSITION. The correct answer's index cycles 0, 1, 2, 3
through each band, so this file holds three of each.

⚠️ BAND VALUES ARE FULL WORDS — see `questions_01_metals_and_non_metals.py`.
"""

UNIT = "C8"
LESSON = "group-7-the-halogens"
LESSON_NUMBER = 5

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "c8-05-e01",
        "band": "easier",
        # ⚑ Asks for the element at the END of the trend rather than for
        # the trend itself — the recall rung already asks the direction, and
        # check 6 is right that a bank restating a rung adds no depth.
        "text": "Which element is the most reactive in the whole periodic "
                "table?",
        "options": [
            {"text": "Fluorine, at the top of group 7",
             "correct": True},
            {"text": "Iodine, at the bottom of group 7",
             "correct": False,
             "why": "Iodine is the mildest of the halogens — mild enough to "
                    "be painted on skin."},
            {"text": "Argon, because it is in the last group of all",
             "correct": False,
             "why": "Argon is in group 0 and reacts with essentially "
                    "nothing."},
            {"text": "Carbon, because it is in the middle of the table",
             "correct": False,
             "why": "Carbon is unreactive enough to sit in a pencil for "
                    "years. Position in the middle predicts nothing."},
        ],
        "figure": None,
    },
    {
        "id": "c8-05-e02",
        "band": "easier",
        "text": "Chlorine water is added to colourless potassium bromide "
                "solution and the solution turns orange. What has happened?",
        "options": [
            {"text": "The chlorine has dissolved and made an orange solution "
                     "on its own",
             "correct": False,
             "why": "Chlorine water is pale green. The orange arrived with "
                    "the reaction."},
            {"text": "Chlorine has displaced bromine, and the orange is the "
                     "bromine",
             "correct": True},
            {"text": "Bromine has displaced chlorine, because bromine is "
                     "lower down",
             "correct": False,
             "why": "Lower down group 7 means LESS reactive. Bromine cannot "
                    "displace chlorine."},
            {"text": "The potassium has been displaced and turned the "
                     "solution orange",
             "correct": False,
             "why": "Potassium is a spectator here. The colour comes from the "
                    "halogen set free."},
        ],
        "figure": None,
    },
    {
        "id": "c8-05-e03",
        "band": "easier",
        "text": "Fluorine is a pale yellow gas, bromine a red-brown liquid "
                "and iodine a grey-black solid. Why are they in one group?",
        "options": [
            {"text": "Because they were all discovered by the same chemist",
             "correct": False,
             "why": "They were found by different people over eighty years."},
            {"text": "Because their atoms all weigh about the same amount",
             "correct": False,
             "why": "Their masses run from 19 to 127. Mass is what separates "
                    "them, not what unites them."},
            {"text": "Because they react in the same way and form the same "
                     "kind of compound",
             "correct": True},
            {"text": "Because they are all the same colour when they are "
                     "pure",
             "correct": False,
             "why": "They are four different colours, which is exactly what "
                    "makes the family resemblance surprising."},
        ],
        "figure": None,
    },
    {
        "id": "c8-05-e04",
        "band": "easier",
        "text": "Iodine solution is added to potassium bromide and nothing "
                "changes. What has that tube told you?",
        "options": [
            {"text": "Nothing — a tube with no change is a failed experiment",
             "correct": False,
             "why": "A null result is a result. It places iodine below "
                    "bromine, which is information."},
            {"text": "That the potassium bromide had not dissolved properly",
             "correct": False,
             "why": "Potassium bromide dissolves readily. The solution was "
                    "there; the reaction was not."},
            {"text": "That the iodine solution was too dilute to work",
             "correct": False,
             "why": "Concentration changes the speed of a reaction that CAN "
                    "happen. This one cannot happen at all."},
            {"text": "That iodine is less reactive than bromine",
             "correct": True},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "c8-05-s01",
        "band": "standard",
        "text": "Why does group 7 run the opposite way from group 1?",
        "options": [
            {"text": "Because group 7 atoms react by gaining an electron, not "
                     "losing one",
             "correct": True},
            {"text": "Because group 7 is on the other side of the periodic "
                     "table",
             "correct": False,
             "why": "Position is where the fact is written down, not why it "
                    "is true."},
            {"text": "Because group 7 elements are non-metals and non-metals "
                     "are all alike",
             "correct": False,
             "why": "Carbon and helium are both non-metals and could hardly "
                    "differ more."},
            {"text": "Because the atoms in group 7 get smaller going down the "
                     "column",
             "correct": False,
             "why": "They get bigger going down, exactly as group 1's do. "
                    "That is what makes one idea explain both."},
        ],
        "figure": None,
    },
    {
        "id": "c8-05-s02",
        "band": "standard",
        "text": "In a 3 × 3 grid of halogens against halide solutions, three "
                "of the nine tubes react. Why are the other six not wasted?",
        "options": [
            {"text": "They are wasted, and a better experiment would leave "
                     "them out",
             "correct": False,
             "why": "Leaving them out would remove the shape that makes the "
                    "grid readable as an order."},
            {"text": "They show which displacements do NOT happen, which "
                     "fixes the order",
             "correct": True},
            {"text": "They act as a control to prove the equipment was clean",
             "correct": False,
             "why": "That is not what they test. Each one is a real "
                    "chemistry question with the answer 'no'."},
            {"text": "They would react if the tubes were left long enough",
             "correct": False,
             "why": "Time does not help. A less reactive halogen cannot "
                    "displace a more reactive one at all."},
        ],
        "figure": None,
    },
    {
        "id": "c8-05-s03",
        "band": "standard",
        "text": "Chlorine is used to make tap water safe and was also "
                "released as a weapon in 1915. What does that pair of facts "
                "show?",
        "options": [
            {"text": "That chlorine is a dangerous element and should not be "
                     "used at all",
             "correct": False,
             "why": "Removing it from water supplies would cost far more "
                    "lives than it saved."},
            {"text": "That the chlorine used in water is a different "
                     "substance chemically",
             "correct": False,
             "why": "It is the same element in both cases. That is precisely "
                    "the point."},
            {"text": "That a substance is not good or evil — what is done "
                     "with it is",
             "correct": True},
            {"text": "That chemists in 1915 did not yet understand what "
                     "chlorine did",
             "correct": False,
             "why": "Its properties were well known. Knowledge was not what "
                    "was missing."},
        ],
        "figure": None,
    },
    {
        "id": "c8-05-s04",
        "band": "standard",
        "text": "A student predicts that iodine will displace chlorine from "
                "potassium chloride, “because reactivity increases down a "
                "group”. What does the grid show?",
        "options": [
            {"text": "The prediction is right, and the tube turns green",
             "correct": False,
             "why": "Nothing changes in that tube. The prediction is "
                    "refuted."},
            {"text": "The prediction is right for group 7 but not for group 1",
             "correct": False,
             "why": "It has the two groups exactly the wrong way round."},
            {"text": "The prediction cannot be tested with the tubes "
                     "available",
             "correct": False,
             "why": "It is one of the nine tubes, and it is run like the "
                    "rest."},
            {"text": "The prediction is wrong — nothing happens in that tube",
             "correct": True},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "c8-05-h01",
        "band": "harder",
        "text": "Astatine sits below iodine. How would you test whether it is "
                "the least reactive halogen, using only the solutions in this "
                "lesson?",
        "options": [
            {"text": "Add it to chloride, bromide and iodide solutions and "
                     "look for no change in any",
             "correct": True},
            {"text": "Add it to water and see whether it fizzes more than "
                     "iodine does",
             "correct": False,
             "why": "Fizzing in water is a group 1 test. Halogens are placed "
                    "by displacement."},
            {"text": "Compare its colour with iodine's, since darker means "
                     "less reactive",
             "correct": False,
             "why": "Colour runs alongside the trend without causing it, and "
                    "it would not distinguish two dark solids."},
            {"text": "Heat it and see whether it turns to vapour at a lower "
                     "temperature",
             "correct": False,
             "why": "Melting and boiling points describe the element, not how "
                    "readily it reacts."},
        ],
        "figure": None,
    },
    {
        "id": "c8-05-h02",
        "band": "harder",
        "text": "Going down group 7 the elements change from gas to liquid to "
                "solid. What does that tell you about their reactivity?",
        "options": [
            {"text": "That the solids are the most reactive, being most "
                     "concentrated",
             "correct": False,
             "why": "Iodine is the solid and the mildest of the four. State "
                    "does not set reactivity."},
            {"text": "Nothing directly — state and reactivity are separate "
                     "properties",
             "correct": True},
            {"text": "That the gases are the least reactive, being most "
                     "spread out",
             "correct": False,
             "why": "Fluorine is a gas and the most reactive element in the "
                    "table."},
            {"text": "That reactivity must fall, because melting points rise "
                     "downwards",
             "correct": False,
             "why": "Reactivity does fall, but not BECAUSE of the melting "
                    "points. Two trends running together are not a cause."},
        ],
        "figure": None,
    },
    {
        "id": "c8-05-h03",
        "band": "harder",
        "text": "A student learns “reactivity increases down a group” from "
                "group 1 and applies it everywhere. What is the safest "
                "correction?",
        "options": [
            {"text": "Tell them reactivity always decreases down a group "
                     "instead",
             "correct": False,
             "why": "That replaces one over-general rule with its mirror "
                    "image and fails group 1."},
            {"text": "Tell them each group has a trend and the direction has "
                     "to be checked",
             "correct": False,
             "why": "True, but it leaves the direction as something to "
                    "memorise per group — which is what goes wrong."},
            {"text": "Tell them to learn the reason, since one idea gives "
                     "both directions",
             "correct": True},
            {"text": "Tell them trends only apply to metals, so group 7 is "
                     "exempt",
             "correct": False,
             "why": "Group 7's trend is as real and as regular as group 1's. "
                    "It simply runs the other way."},
        ],
        "figure": None,
    },
    {
        "id": "c8-05-h04",
        "band": "harder",
        "text": "Bromine water is added to potassium bromide and nothing "
                "happens. Why is that tube on the grid at all?",
        "options": [
            {"text": "To check the bromine water has not gone off before the "
                     "real tests",
             "correct": False,
             "why": "It is not a control. It is a chemistry question with a "
                    "real answer."},
            {"text": "To give the student a rest between two harder "
                     "comparisons",
             "correct": False,
             "why": "Every tube on the grid carries the same demand as every "
                    "other."},
            {"text": "To show that bromine is the least reactive of the "
                     "three halogens",
             "correct": False,
             "why": "Bromine displaces iodine, so it is not the least "
                    "reactive. This tube says nothing about the order."},
            {"text": "To show that a halogen cannot displace itself from its "
                     "own salt",
             "correct": True},
        ],
        "figure": None,
    },

    # ── easier · MRB-335 top-up ─────────────────────────────────────────
    {
        "id": "c8-05-e05",
        "band": "easier",
        "text": "What does the name halogen mean?",
        "options": [
            {"text": "Poison-bringer, which is a fair description of a group "
                     "whose members are all poisonous and one of which has "
                     "been used as a weapon",
             "correct": False,
             "why": "They are poisonous, and the name is not about that. It "
                    "is about the compounds they make with metals"},
            {"text": "Coloured gas",
             "correct": False,
             "why": "They are coloured, and only some are gases. The name "
                    "records what they DO"},
            {"text": "Salt-maker",
             "correct": True},
            {"text": "Seventh family",
             "correct": False,
             "why": "They are group 7, and the name is older than the "
                    "numbering"},
        ],
        "figure": None,
    },
    {
        "id": "c8-05-e06",
        "band": "easier",
        "text": "What is a displacement reaction?",
        "options": [
            {"text": "A reaction in which two compounds exchange places in "
                     "solution, so that each of them ends up dissolved in the "
                     "other's water",
             "correct": False,
             "why": "Nothing swaps solvents. What is pushed out is an "
                    "element, out of a compound"},
            {"text": "A reaction that moves a solid out of one test tube and "
                     "across into a second one that is standing beside it",
             "correct": False,
             "why": "Nothing is moved between tubes. The word is about what "
                    "happens inside one"},
            {"text": "Any reaction at all that changes the colour of the "
                     "solution that it is taking place in, whatever it is",
             "correct": False,
             "why": "Plenty of colour changes are not displacements, and the "
                    "colour here is a sign rather than the definition"},
            {"text": "A reaction in which a more reactive element pushes a "
                     "less reactive one out of its compound",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c8-05-e07",
        "band": "easier",
        "text": "What is a halide?",
        "options": [
            {"text": "The compound a halogen makes with a metal — a chloride, "
                     "a bromide or an iodide",
             "correct": True},
            {"text": "A halogen that has been dissolved in water, which is "
                     "how it is supplied in a bottle for use on the bench",
             "correct": False,
             "why": "That is halogen WATER — chlorine water, bromine water. A "
                    "halide is a compound with a metal in it"},
            {"text": "Another word for a halogen",
             "correct": False,
             "why": "One is the element and the other is its compound. Mixing "
                    "them up is what makes the grid hard to read"},
            {"text": "A mixture of two halogens",
             "correct": False,
             "why": "No mixture is involved. A halide has a metal in it"},
        ],
        "figure": None,
    },

    # ── standard · MRB-335 top-up ───────────────────────────────────────
    {
        "id": "c8-05-s05",
        "band": "standard",
        "text": "Chlorine water is added to potassium iodide solution. What "
                "would you see, and what has been made?",
        "options": [
            {"text": "The solution stays colourless, because chlorine is "
                     "above iodine and a halogen higher up the group cannot "
                     "displace one below it",
             "correct": False,
             "why": "Higher up means MORE reactive in group 7, so chlorine "
                    "displaces iodine readily"},
            {"text": "It turns orange, and the orange is bromine",
             "correct": False,
             "why": "There is no bromine in either tube. Orange is what a "
                    "bromide gives"},
            {"text": "It turns brown, and the brown is iodine set free",
             "correct": True},
            {"text": "It fizzes and gives off a gas",
             "correct": False,
             "why": "Nothing is given off. A displacement here shows itself "
                    "as a colour"},
        ],
        "figure": None,
    },
    {
        "id": "c8-05-s06",
        "band": "standard",
        "text": "Iodine is mild enough to be used as an antiseptic on skin, "
                "and fluorine is not. Which idea explains that?",
        "options": [
            {"text": "That iodine is a solid and fluorine a gas, so only one "
                     "of them can be put into a bottle and carried to where "
                     "it is needed",
             "correct": False,
             "why": "State is not the reason. Bromine is a liquid and is no "
                    "safer than fluorine for the purpose"},
            {"text": "That iodine is not really a halogen",
             "correct": False,
             "why": "It is group 7 and behaves like one — it just sits low "
                    "down"},
            {"text": "That fluorine kills no bacteria",
             "correct": False,
             "why": "It would kill them, and everything else it touched. The "
                    "problem is that it is far too reactive"},
            {"text": "That reactivity falls going down group 7, so iodine is "
                     "by far the gentler of the two",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c8-05-s07",
        "band": "standard",
        "text": "Fluorine's compounds are in toothpaste and on non-stick "
                "pans, and fluorine itself injured the chemists who tried to "
                "isolate it. What does that show?",
        "options": [
            {"text": "That an element and its compounds are different "
                     "substances",
             "correct": True},
            {"text": "That fluorine becomes safe once it has been diluted "
                     "enough, which is what a toothpaste manufacturer is "
                     "doing when it adds a trace of it to the tube",
             "correct": False,
             "why": "There is no fluorine in toothpaste at all — there is "
                    "fluoride, which is a compound and a different "
                    "substance"},
            {"text": "That the early chemists were careless",
             "correct": False,
             "why": "They were working with the most reactive element there "
                    "is, before anyone knew how. Care was not the problem"},
            {"text": "That fluorine is not really that reactive",
             "correct": False,
             "why": "It is the most reactive element in the table. Its "
                    "compounds are a separate matter"},
        ],
        "figure": None,
    },

    # ── harder · MRB-335 top-up ─────────────────────────────────────────
    {
        "id": "c8-05-h05",
        "band": "harder",
        "text": "Group 1 gets more reactive going down and group 7 gets less. "
                "Which single idea gives both directions?",
        "options": [
            {"text": "That group 1 atoms get lighter going down while group 7 "
                     "atoms get heavier, so the two groups pull in opposite "
                     "directions as you read down them",
             "correct": False,
             "why": "Both groups get heavier going down. Mass is not what "
                    "drives either trend"},
            {"text": "That metals and non-metals always behave in opposite "
                     "ways",
             "correct": False,
             "why": "That is a restatement of the observation rather than a "
                    "reason for it"},
            {"text": "That the atoms get bigger going down, so the outer "
                     "electron is further out — easier to lose, and harder to "
                     "attract one in",
             "correct": True},
            {"text": "That group 7 has more electrons than group 1",
             "correct": False,
             "why": "True and not the reason. What matters is whether an atom "
                    "is losing an electron or gaining one"},
        ],
        "figure": None,
    },
    {
        "id": "c8-05-h06",
        "band": "harder",
        "text": "Chlorine at one part per million makes tap water safe and "
                "saved more lives than most medicines; the same element was "
                "released as a weapon. What is the lesson's conclusion?",
        "options": [
            {"text": "That chlorine should be replaced with something safer "
                     "wherever it is possible to do so, because a substance "
                     "with that history has no place in a water supply",
             "correct": False,
             "why": "The lesson draws the opposite conclusion, and "
                    "chlorination is one of the great public health "
                    "measures"},
            {"text": "That chlorine is safe at low concentrations and "
                     "dangerous at high ones",
             "correct": False,
             "why": "True of almost everything, and it is not what the pair "
                    "of facts is doing here"},
            {"text": "That chemistry should not be applied outside a "
                     "laboratory",
             "correct": False,
             "why": "The water supply IS chemistry applied outside a "
                    "laboratory, and it works"},
            {"text": "That a substance is not good or evil — what is done "
                     "with it is",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c8-05-h07",
        "band": "harder",
        "text": "Chlorine displaces bromine, and bromine displaces iodine. "
                "What follows about chlorine and iodine, without running that "
                "tube at all?",
        "options": [
            {"text": "That chlorine displaces iodine, because an order that "
                     "holds for each step holds all the way along it",
             "correct": True},
            {"text": "That chlorine and iodine do not react, because "
                     "displacement only works between elements that are next "
                     "to each other in the group",
             "correct": False,
             "why": "There is no such restriction. The order is an order, and "
                    "chlorine is above iodine in it"},
            {"text": "That iodine displaces chlorine, since two steps in one "
                     "direction reverse into one step in the other",
             "correct": False,
             "why": "Nothing reverses. Iodine is the least reactive of the "
                    "three and displaces neither"},
            {"text": "Nothing — the tube has to be run before anything can be "
                     "said",
             "correct": False,
             "why": "Running it is worth doing as a check, and the prediction "
                    "is exactly what an order is FOR"},
        ],
        "figure": None,
    },
]
