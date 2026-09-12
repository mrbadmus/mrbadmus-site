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
    # ── easier · appended MRB-338 ───────────────────────────────────────
    {
        "id": "c8-05-e08",
        "band": "easier",
        "text": "Group 7 holds four elements you need at this level. Which "
                "list gives them in order, starting at the top of the "
                "group?",
        "options": [
            {"text": "Fluorine, chlorine, bromine, iodine", "correct": True},
            {"text": "Iodine, bromine, chlorine, fluorine",
             "correct": False,
             "why": "That is the column read upwards; fluorine is the one "
                    "at the top"},
            {"text": "Chlorine, fluorine, bromine, iodine",
             "correct": False,
             "why": "Fluorine sits above chlorine in the group, not below it"},
            {"text": "Fluorine, bromine, chlorine, iodine",
             "correct": False,
             "why": "Chlorine comes before bromine going down the group"},
        ],
        "figure": None,
    },
    {
        "id": "c8-05-e09",
        "band": "easier",
        "text": "Chlorine is a gas at room temperature. What colour is it?",
        "options": [
            {"text": "Colourless",
             "correct": False,
             "why": "Chlorine has an obvious colour; it is the halide "
                    "solutions that are colourless"},
            {"text": "Green", "correct": True},
            {"text": "Red-brown",
             "correct": False,
             "why": "Red-brown is bromine, the liquid two places below "
                    "chlorine"},
            {"text": "Grey-black",
             "correct": False,
             "why": "Grey-black is solid iodine, further down the group "
                    "again"},
        ],
        "figure": None,
    },
    {
        "id": "c8-05-e10",
        "band": "easier",
        "text": "The halogens are which group of the periodic table?",
        "options": [
            {"text": "Group 1",
             "correct": False,
             "why": "Group 1 is the alkali metals, on the far left of the "
                    "table"},
            {"text": "Group 0",
             "correct": False,
             "why": "Group 0 is the noble gases, the column on the other "
                    "side of the halogens"},
            {"text": "Group 7", "correct": True},
            {"text": "Group 2",
             "correct": False,
             "why": "Group 2 is a column of metals, and the halogens are "
                    "non-metals"},
        ],
        "figure": None,
    },
    {
        "id": "c8-05-e11",
        "band": "easier",
        "text": "Iodine is warmed gently and turns straight into a vapour. "
                "What colour is that vapour?",
        "options": [
            {"text": "Pale green",
             "correct": False,
             "why": "Pale green is chlorine water in a tube, not iodine "
                    "vapour"},
            {"text": "Orange",
             "correct": False,
             "why": "Orange is the vapour above red-brown liquid bromine"},
            {"text": "Colourless",
             "correct": False,
             "why": "Iodine vapour is strongly coloured, which is how it is "
                    "spotted"},
            {"text": "Violet", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c8-05-e12",
        "band": "easier",
        "text": "How does the colour of the halogens change from the top of "
                "group 7 to the bottom?",
        "options": [
            {"text": "They get paler",
             "correct": False,
             "why": "The trend runs the other way, from pale yellow at the "
                    "top to grey-black at the bottom"},
            {"text": "They get darker", "correct": True},
            {"text": "They stay the same colour all the way down",
             "correct": False,
             "why": "Fluorine is pale yellow and iodine is grey-black, "
                    "which is not the same colour"},
            {"text": "They lose their colour",
             "correct": False,
             "why": "Every halogen is coloured, and the lower ones most "
                    "strongly of all"},
        ],
        "figure": None,
    },
    {
        "id": "c8-05-e13",
        "band": "easier",
        "text": "Which is more reactive, chlorine or iodine?",
        "options": [
            {"text": "Iodine, because it is lower down group 7",
             "correct": False,
             "why": "Reactivity falls going down group 7, so sitting lower "
                    "makes iodine the milder of the two"},
            {"text": "Iodine, because it is a solid and chlorine is a gas",
             "correct": False,
             "why": "State at room temperature is about melting point and "
                    "says nothing about how readily an element reacts"},
            {"text": "Chlorine, because it is higher up group 7",
             "correct": True},
            {"text": "Neither, because a group reacts as one",
             "correct": False,
             "why": "A group has a trend, and chlorine displaces iodine "
                    "from its salt while iodine can do nothing back"},
        ],
        "figure": None,
    },
    {
        "id": "c8-05-e14",
        "band": "easier",
        "text": "Which halogen is used in household bleach and added to tap "
                "water to make it safe to drink?",
        "options": [
            {"text": "Fluorine",
             "correct": False,
             "why": "Fluorine is far too reactive to put into a water "
                    "supply; it is its compound that goes into toothpaste"},
            {"text": "Iodine",
             "correct": False,
             "why": "Iodine is used on skin as an antiseptic, not in the "
                    "mains supply"},
            {"text": "Astatine",
             "correct": False,
             "why": "Astatine is far too rare and radioactive to be used "
                    "for anything at all"},
            {"text": "Chlorine", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c8-05-e15",
        "band": "easier",
        "text": "A cut is dabbed with a brown solution that kills bacteria "
                "on the skin. Which halogen is in it?",
        "options": [
            {"text": "Iodine", "correct": True},
            {"text": "Fluorine",
             "correct": False,
             "why": "Fluorine is the most reactive element in the table and "
                    "could never be put on a wound"},
            {"text": "Chlorine",
             "correct": False,
             "why": "Chlorine is a green gas used in water supplies, not a "
                    "brown solution for skin"},
            {"text": "Bromine",
             "correct": False,
             "why": "Bromine water burns skin rather than treating it"},
        ],
        "figure": None,
    },
    {
        "id": "c8-05-e16",
        "band": "easier",
        "text": "Toothpaste contains a compound of a group 7 element. Which "
                "element is it?",
        "options": [
            {"text": "Chlorine, as chloride",
             "correct": False,
             "why": "Chlorine goes into tap water and bleach, not into "
                    "toothpaste"},
            {"text": "Iodine, as iodide",
             "correct": False,
             "why": "Iodine is the antiseptic of the group, used on skin"},
            {"text": "Fluorine, as fluoride", "correct": True},
            {"text": "Bromine, as bromide",
             "correct": False,
             "why": "No bromine compound is put into toothpaste"},
        ],
        "figure": None,
    },
    {
        "id": "c8-05-e17",
        "band": "easier",
        "text": "PTFE, the non-stick coating on a frying pan, is a chain of "
                "carbon wrapped in one other element. Which one?",
        "options": [
            {"text": "Chlorine",
             "correct": False,
             "why": "Chlorine is not the element in a non-stick coating"},
            {"text": "Astatine",
             "correct": False,
             "why": "Astatine is the rarest of the halogens and coats "
                    "nothing"},
            {"text": "Bromine",
             "correct": False,
             "why": "Bromine is a corrosive liquid and coats nothing"},
            {"text": "Fluorine", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c8-05-e18",
        "band": "easier",
        "text": "Which halogen is a red-brown liquid at room temperature?",
        "options": [
            {"text": "Bromine", "correct": True},
            {"text": "Fluorine",
             "correct": False,
             "why": "Fluorine is a pale yellow gas at the top of the group"},
            {"text": "Iodine",
             "correct": False,
             "why": "Iodine is a dark, brittle solid rather than a liquid"},
            {"text": "Astatine",
             "correct": False,
             "why": "Astatine sits below iodine and is predicted to be a "
                    "solid as well"},
        ],
        "figure": None,
    },
    {
        "id": "c8-05-e19",
        "band": "easier",
        "text": "Are the halogens metals or non-metals?",
        "options": [
            {"text": "Metals",
             "correct": False,
             "why": "The halogens are coloured, poisonous non-metals; the "
                    "metals sit on the left of the table"},
            {"text": "Non-metals", "correct": True},
            {"text": "Transition metals",
             "correct": False,
             "why": "The transition metals are the block between groups 2 "
                    "and 3"},
            {"text": "Half metal, half non-metal",
             "correct": False,
             "why": "All four halogens are non-metals; the group is not "
                    "split down the middle"},
        ],
        "figure": None,
    },
    {
        "id": "c8-05-e20",
        "band": "easier",
        "text": "The halogens exist as pairs of atoms joined together. What "
                "is the formula of a chlorine molecule?",
        "options": [
            {"text": "Cl",
             "correct": False,
             "why": "A lone chlorine atom is not how the element exists; "
                    "the atoms go about in pairs"},
            {"text": "Cl₃",
             "correct": False,
             "why": "The pair is two atoms, not three"},
            {"text": "KCl",
             "correct": False,
             "why": "KCl is potassium chloride, a compound of chlorine with "
                    "a metal"},
            {"text": "Cl₂", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c8-05-e21",
        "band": "easier",
        "text": "Which element sits directly below iodine in group 7?",
        "options": [
            {"text": "Astatine", "correct": True},
            {"text": "Bromine",
             "correct": False,
             "why": "Bromine is one place above iodine, not below it"},
            {"text": "Argon",
             "correct": False,
             "why": "Argon is a noble gas in group 0, not a halogen at all"},
            {"text": "Tellurium",
             "correct": False,
             "why": "Tellurium is not in group 7"},
        ],
        "figure": None,
    },
    {
        "id": "c8-05-e22",
        "band": "easier",
        "text": "What happens to the melting points of the halogens going "
                "down the group?",
        "options": [
            {"text": "They fall",
             "correct": False,
             "why": "They rise, which is why the top of the group is a gas "
                    "and the bottom is a solid"},
            {"text": "They rise", "correct": True},
            {"text": "They stay the same",
             "correct": False,
             "why": "One member is a gas and another a solid at the same "
                    "room temperature, so they cannot match"},
            {"text": "They rise and then fall",
             "correct": False,
             "why": "There is no turning point; the rise runs steadily all "
                    "the way down"},
        ],
        "figure": None,
    },
    {
        "id": "c8-05-e23",
        "band": "easier",
        "text": "Why are the halogen solutions kept in a fume cupboard?",
        "options": [
            {"text": "They evaporate too fast to be used on an open bench",
             "correct": False,
             "why": "Keeping the vapour away from the class is the reason, "
                    "not the speed of evaporation"},
            {"text": "They have to be kept cold",
             "correct": False,
             "why": "A fume cupboard draws air away; it does not chill "
                    "anything"},
            {"text": "Their vapours are toxic", "correct": True},
            {"text": "Daylight would make them react",
             "correct": False,
             "why": "They are shut away from people, not from light"},
        ],
        "figure": None,
    },
    {
        "id": "c8-05-e24",
        "band": "easier",
        "text": "Bromine water is added to potassium iodide solution and "
                "the orange darkens to brown. Which element has been pushed "
                "out of its salt?",
        "options": [
            {"text": "Iodine", "correct": True},
            {"text": "Bromine",
             "correct": False,
             "why": "Bromine is the halogen that was added; it is the one "
                    "doing the pushing"},
            {"text": "Potassium",
             "correct": False,
             "why": "Potassium is the metal in the salt and stays in "
                    "solution throughout"},
            {"text": "Chlorine",
             "correct": False,
             "why": "There is no chlorine in this tube"},
        ],
        "figure": None,
    },
    {
        "id": "c8-05-e25",
        "band": "easier",
        "text": "Which is the least reactive of chlorine, bromine and "
                "iodine?",
        "options": [
            {"text": "Chlorine",
             "correct": False,
             "why": "Chlorine is the highest of the three in group 7, so it "
                    "is the most reactive"},
            {"text": "Iodine", "correct": True},
            {"text": "Bromine",
             "correct": False,
             "why": "Bromine sits between the other two and is neither the "
                    "most nor the least reactive"},
            {"text": "All three react equally",
             "correct": False,
             "why": "Chlorine displaces both the others, which they cannot "
                    "do to it"},
        ],
        "figure": None,
    },
    {
        "id": "c8-05-e26",
        "band": "easier",
        "text": "Chlorine in tap water kills the bacteria that cause which "
                "two diseases?",
        "options": [
            {"text": "Measles and mumps",
             "correct": False,
             "why": "Both are caused by viruses, and neither is carried in "
                    "a water supply"},
            {"text": "Malaria and influenza",
             "correct": False,
             "why": "Neither is a bacterium that chlorination is used "
                    "against"},
            {"text": "Cholera and typhoid", "correct": True},
            {"text": "Asthma and eczema",
             "correct": False,
             "why": "Neither is an infection caught from drinking water"},
        ],
        "figure": None,
    },
    {
        "id": "c8-05-e27",
        "band": "easier",
        "text": "Several chemists were killed or injured trying to isolate "
                "fluorine. Who finally succeeded, in 1886?",
        "options": [
            {"text": "Dmitri Mendeleev",
             "correct": False,
             "why": "Mendeleev built the periodic table and isolated no new "
                    "element himself"},
            {"text": "Humphry Davy",
             "correct": False,
             "why": "Davy isolated the group 1 metals by electricity, not "
                    "fluorine"},
            {"text": "John Newlands",
             "correct": False,
             "why": "Newlands published an early pattern in the elements "
                    "and isolated nothing"},
            {"text": "Henri Moissan", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c8-05-e28",
        "band": "easier",
        "text": "Which of these compounds is a halide?",
        "options": [
            {"text": "Potassium iodide", "correct": True},
            {"text": "Sodium oxide",
             "correct": False,
             "why": "An oxide is a compound with oxygen, not with a group 7 "
                    "element"},
            {"text": "Calcium carbonate",
             "correct": False,
             "why": "A carbonate holds carbon and oxygen and no halogen"},
            {"text": "Magnesium hydroxide",
             "correct": False,
             "why": "A hydroxide holds oxygen and hydrogen, not a halogen"},
        ],
        "figure": None,
    },
    {
        "id": "c8-05-e29",
        "band": "easier",
        "text": "What does the word antiseptic mean?",
        "options": [
            {"text": "A substance that kills the bacteria in a public water "
                     "supply",
             "correct": False,
             "why": "That is disinfecting water; an antiseptic is used on "
                    "the body"},
            {"text": "A substance that kills bacteria on skin or a wound",
             "correct": True},
            {"text": "A substance that stops a cut from bleeding any further",
             "correct": False,
             "why": "That is what a dressing does; an antiseptic acts on "
                    "bacteria"},
            {"text": "A substance that takes the pain out of a cut or a "
                     "graze",
             "correct": False,
             "why": "Nothing in an antiseptic is a painkiller"},
        ],
        "figure": None,
    },
    {
        "id": "c8-05-e30",
        "band": "easier",
        "text": "The halogens react with metals to make what kind of "
                "compound?",
        "options": [
            {"text": "Acids",
             "correct": False,
             "why": "An acid is not what a metal and a halogen make together"},
            {"text": "Oxides",
             "correct": False,
             "why": "An oxide needs oxygen, and no oxygen is involved here"},
            {"text": "Salts", "correct": True},
            {"text": "Alkalis",
             "correct": False,
             "why": "An alkali is a soluble base; a metal and a halogen "
                    "give a salt"},
        ],
        "figure": None,
    },
    {
        "id": "c8-05-e31",
        "band": "easier",
        "text": "Put chlorine, bromine and iodine in order of increasing "
                "density.",
        "options": [
            {"text": "Iodine, then bromine, then chlorine",
             "correct": False,
             "why": "Density rises going down group 7, and iodine is the "
                    "lowest of these three"},
            {"text": "Bromine, then chlorine, then iodine",
             "correct": False,
             "why": "Chlorine sits above bromine, so it is the less dense "
                    "of that pair"},
            {"text": "All three have the same density",
             "correct": False,
             "why": "The halogens get steadily denser going down the column"},
            {"text": "Chlorine, then bromine, then iodine", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c8-05-e32",
        "band": "easier",
        "text": "Table salt is a compound of chlorine, and chlorine itself "
                "is a poisonous green gas. What does that show?",
        "options": [
            {"text": "That chlorine stops being poisonous the moment it is "
                     "bottled",
             "correct": False,
             "why": "Bottling changes nothing; joining with a metal makes a "
                    "different substance"},
            {"text": "That an element and its compounds are different "
                     "substances",
             "correct": True},
            {"text": "That an element keeps every one of its own properties "
                     "inside a compound",
             "correct": False,
             "why": "If that were so, table salt would be a poisonous green "
                    "gas"},
            {"text": "That table salt contains no chlorine at all",
             "correct": False,
             "why": "It does contain chlorine, joined to sodium"},
        ],
        "figure": None,
    },
    # ── standard · appended MRB-338 ─────────────────────────────────────
    {
        "id": "c8-05-s08",
        "band": "standard",
        "text": "Complete the word equation: chlorine + potassium bromide → "
                "what?",
        "options": [
            {"text": "potassium bromide + chlorine",
             "correct": False,
             "why": "Nothing has changed; both starting substances are "
                    "simply written out again"},
            {"text": "potassium chloride + bromide",
             "correct": False,
             "why": "Bromide is the compound form; what is set free is the "
                    "element bromine"},
            {"text": "potassium chloride + bromine", "correct": True},
            {"text": "potassium + chlorine + bromine",
             "correct": False,
             "why": "The potassium stays joined to a halogen and is never "
                    "released as the metal"},
        ],
        "figure": None,
    },
    {
        "id": "c8-05-s09",
        "band": "standard",
        "text": "Which of these word equations describes a reaction that "
                "actually happens?",
        "options": [
            {"text": "iodine + potassium chloride → potassium iodide + "
                     "chlorine",
             "correct": False,
             "why": "Iodine is well below chlorine, so it is the milder of "
                    "the two and cannot take chlorine's place"},
            {"text": "iodine + potassium bromide → potassium iodide + "
                     "bromine",
             "correct": False,
             "why": "Iodine is the least reactive of the three and "
                    "displaces neither of the others"},
            {"text": "bromine + potassium chloride → potassium bromide + "
                     "chlorine",
             "correct": False,
             "why": "Bromine sits below chlorine, so it cannot push "
                    "chlorine out of its own salt"},
            {"text": "chlorine + potassium iodide → potassium chloride + "
                     "iodine",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c8-05-s10",
        "band": "standard",
        "text": "Chlorine, bromine and iodine are each added to potassium "
                "chloride, potassium bromide and potassium iodide, making "
                "nine tubes. Which of them change colour?",
        "options": [
            {"text": "Chlorine into the bromide and the iodide, and bromine "
                     "into the iodide",
             "correct": True},
            {"text": "Every tube in which the halogen and the salt are "
                     "different",
             "correct": False,
             "why": "Bromine into potassium chloride is a different pair "
                    "and still gives no change at all"},
            {"text": "Iodine into the chloride and the bromide, and bromine "
                     "into the chloride as well",
             "correct": False,
             "why": "That is the order reversed; the lower halogen never "
                    "displaces the higher one"},
            {"text": "All nine, because every halogen attacks every halide",
             "correct": False,
             "why": "Six of the nine show no change, including all three in "
                    "which an element meets its own salt"},
        ],
        "figure": None,
    },
    {
        "id": "c8-05-s11",
        "band": "standard",
        "text": "Chlorine water added to potassium bromide solution turns "
                "it orange. Where must chlorine sit relative to bromine in "
                "group 7, and why?",
        "options": [
            {"text": "Below it, because the halogen that is added is always "
                     "the weaker of the two",
             "correct": False,
             "why": "The halogen that does the displacing is the more "
                    "reactive of the two, not the weaker"},
            {"text": "Above it, because reactivity falls going down the "
                     "group",
             "correct": True},
            {"text": "Below it, because reactivity rises going down the "
                     "group",
             "correct": False,
             "why": "Group 7 runs the opposite way from group 1; its "
                    "reactivity falls going down"},
            {"text": "Beside it, because displacement compares a period",
             "correct": False,
             "why": "This compares two members of the same group, one above "
                    "the other in the column"},
        ],
        "figure": None,
    },
    {
        "id": "c8-05-s12",
        "band": "standard",
        "text": "Fluorine, chlorine, bromine and iodine boil at −188 °C, "
                "−34 °C, 59 °C and 184 °C. Which of them are gases in a "
                "room at 20 °C?",
        "options": [
            {"text": "Iodine only, because it boils at the highest "
                     "temperature of the four",
             "correct": False,
             "why": "A high boiling point means it is the last to become a "
                    "gas, not the first"},
            {"text": "All four, because every halogen is a gas at room "
                     "temperature",
             "correct": False,
             "why": "Only the two at the top of the group boil below room "
                    "temperature"},
            {"text": "Fluorine and chlorine, because both boil below 20 °C",
             "correct": True},
            {"text": "None of them, because all four of these boil well "
                     "above 20 °C",
             "correct": False,
             "why": "Fluorine boils at −188 °C and chlorine at −34 °C, both "
                    "far below 20 °C"},
        ],
        "figure": None,
    },
    {
        "id": "c8-05-s13",
        "band": "standard",
        "text": "A group 7 atom reacts by gaining one electron. Why does an "
                "atom further down the group do that less readily?",
        "options": [
            {"text": "It already has a full outer shell, so there is no room "
                     "for another electron to arrive",
             "correct": False,
             "why": "A group 7 atom is one electron short of a full shell "
                    "wherever it sits in the column"},
            {"text": "It has more outer electrons than the ones above it, so "
                     "its shell is nearer to full",
             "correct": False,
             "why": "Every group 7 atom has seven outer electrons; that is "
                    "what puts it in group 7"},
            {"text": "It is heavier, and a heavier atom always reacts more "
                     "slowly than a lighter one",
             "correct": False,
             "why": "Mass is not the cause; what changes is how far the "
                    "outer shell sits from the nucleus"},
            {"text": "Its outer shell is further from the nucleus, so an "
                     "incoming electron is pulled in less strongly",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c8-05-s14",
        "band": "standard",
        "text": "Chlorine is added to tap water at about one part per "
                "million by mass. About how much water would hold 1 g of "
                "chlorine?",
        "options": [
            {"text": "1 000 000 g of water, or 1000 litres", "correct": True},
            {"text": "1000 g of water, or 1 litre",
             "correct": False,
             "why": "That is one part per thousand, a thousand times more "
                    "concentrated than tap water"},
            {"text": "1 000 000 000 g of water, or a million litres",
             "correct": False,
             "why": "That is one part per billion, a thousand times more "
                    "dilute than tap water"},
            {"text": "100 g of water, or a tenth of a litre",
             "correct": False,
             "why": "That is one part per hundred, ten thousand times more "
                    "concentrated than tap water"},
        ],
        "figure": None,
    },
    {
        "id": "c8-05-s15",
        "band": "standard",
        "text": "A student wants to find out whether bromine is more "
                "reactive than iodine. Which single tube would settle it?",
        "options": [
            {"text": "Bromine water added to potassium bromide solution",
             "correct": False,
             "why": "An element cannot displace itself, so this tube "
                    "compares nothing at all"},
            {"text": "Bromine water added to potassium iodide solution",
             "correct": True},
            {"text": "Iodine solution added to a tube of potassium chloride "
                     "solution",
             "correct": False,
             "why": "This tube sets iodine against chlorine and says "
                    "nothing about bromine"},
            {"text": "Bromine water added to iodine solution",
             "correct": False,
             "why": "Displacement needs the other halogen held in a salt, "
                    "not loose as an element"},
        ],
        "figure": None,
    },
    {
        "id": "c8-05-s16",
        "band": "standard",
        "text": "Why is a halogen added to a solution of a halide rather "
                "than to another halogen?",
        "options": [
            {"text": "Because two halogens mixed together would explode",
             "correct": False,
             "why": "Nothing here explodes on mixing; the point is that "
                    "there would be nothing to take"},
            {"text": "Because halogens will not dissolve in one another",
             "correct": False,
             "why": "Solubility is not the issue; there is simply no place "
                    "for one element to take from the other"},
            {"text": "Because a more reactive halogen can only take the "
                     "place of one already held in a compound",
             "correct": True},
            {"text": "Because a halogen will only ever react with a metal, "
                     "and a halide already has its metal joined on",
             "correct": False,
             "why": "Chlorine reacts with the halide dissolved in the "
                    "water, and no metal changes hands"},
        ],
        "figure": None,
    },
    {
        "id": "c8-05-s17",
        "band": "standard",
        "text": "Bromine water burns skin, and iodine solution is mild "
                "enough to dab on a wound. Both are halogens. What does "
                "that difference show?",
        "options": [
            {"text": "That bromine happens to be a liquid at room "
                     "temperature while iodine is a solid",
             "correct": False,
             "why": "State at room temperature is a melting point fact and "
                    "does not decide how fiercely a substance attacks skin"},
            {"text": "That reactivity rises going down group 7",
             "correct": False,
             "why": "Bromine sits above iodine, and group 7 reactivity "
                    "falls going down the column"},
            {"text": "That the two elements are in different groups",
             "correct": False,
             "why": "Both are in group 7; what differs is their position "
                    "within it"},
            {"text": "That reactivity falls going down group 7, and bromine "
                     "is above iodine",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c8-05-s18",
        "band": "standard",
        "text": "Astatine sits below iodine in group 7. What appearance "
                "would you predict for it?",
        "options": [
            {"text": "An almost black solid", "correct": True},
            {"text": "A pale yellow gas, like fluorine",
             "correct": False,
             "why": "That is fluorine at the top of the group; the colours "
                    "darken and the states harden going down"},
            {"text": "A colourless liquid that mixes with water",
             "correct": False,
             "why": "Every halogen is coloured, and the lowest ones most "
                    "strongly of all"},
            {"text": "A shiny silver metal that conducts heat",
             "correct": False,
             "why": "The halogens are non-metals, and astatine is one of "
                    "them"},
        ],
        "figure": None,
    },
    {
        "id": "c8-05-s19",
        "band": "standard",
        "text": "Explain why a school prep room could never keep a cylinder "
                "of fluorine.",
        "options": [
            {"text": "It would turn to a liquid on the shelf",
             "correct": False,
             "why": "Fluorine is a gas at room temperature, and its state "
                    "is not what rules it out"},
            {"text": "It is the most reactive element in the table and "
                     "attacks almost everything it touches",
             "correct": True},
            {"text": "It is a metal, and metals are stored under oil",
             "correct": False,
             "why": "Fluorine is a non-metal; it is the group 1 metals that "
                    "are kept under oil"},
            {"text": "It is radioactive, and a cylinder of it would need a "
                     "lead container heavier than the gas inside",
             "correct": False,
             "why": "Fluorine is not radioactive; it is its reactivity that "
                    "rules it out"},
        ],
        "figure": None,
    },
    {
        "id": "c8-05-s20",
        "band": "standard",
        "text": "Nine tubes are made from three halogens and three halide "
                "solutions, and the tubes that react all fall on one side "
                "of the grid. Why does it come out that shape?",
        "options": [
            {"text": "Because the tubes were set out in the order they were "
                     "run",
             "correct": False,
             "why": "The order of running cannot decide which tubes change "
                    "colour"},
            {"text": "Because only the tubes where halogen and salt match "
                     "give a change",
             "correct": False,
             "why": "Those three tubes are precisely the ones in which "
                    "nothing happens"},
            {"text": "Because a reaction happens only when the added "
                     "halogen is higher up the group than the one in the "
                     "salt",
             "correct": True},
            {"text": "Because a reaction happens only when the added "
                     "halogen is lower down the group than the one held in "
                     "the salt",
             "correct": False,
             "why": "That is the rule reversed; the lower halogen is the "
                    "milder and displaces nothing"},
        ],
        "figure": None,
    },
    {
        "id": "c8-05-s21",
        "band": "standard",
        "text": "The bottles of chlorine water and iodine solution may have "
                "been swapped. Which single observation would prove it?",
        "options": [
            {"text": "The bottle labelled chlorine is pale green",
             "correct": False,
             "why": "Pale green is what chlorine water should look like, so "
                    "this shows the label is right"},
            {"text": "The bottle labelled iodine leaves the potassium "
                     "chloride solution unchanged",
             "correct": False,
             "why": "Iodine does leave potassium chloride unchanged, so "
                    "this is the label behaving properly"},
            {"text": "Both bottles leave potassium iodide unchanged",
             "correct": False,
             "why": "Chlorine turns potassium iodide brown, so this would "
                    "mean neither bottle held chlorine at all"},
            {"text": "The bottle labelled iodine turns potassium bromide "
                     "orange",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c8-05-s22",
        "band": "standard",
        "text": "Iodine melts at 114 °C and boils at 184 °C. Why is it a "
                "solid on a laboratory bench at 20 °C?",
        "options": [
            {"text": "20 °C is well below its melting point of 114 °C",
             "correct": True},
            {"text": "20 °C sits between its melting point and its boiling "
                     "point",
             "correct": False,
             "why": "That range runs from 114 °C to 184 °C, and 20 °C is "
                    "below all of it"},
            {"text": "20 °C is above its boiling point of 184 °C",
             "correct": False,
             "why": "A bench at 20 °C is far below 184 °C, not above it"},
            {"text": "Iodine has no melting point, so it cannot melt",
             "correct": False,
             "why": "Its melting point is 114 °C; heat it that far and it "
                    "melts like anything else"},
        ],
        "figure": None,
    },
    {
        "id": "c8-05-s23",
        "band": "standard",
        "text": "Iodine turns straight from a grey-black solid into a "
                "violet vapour when warmed gently. Why is that a reason to "
                "keep it stoppered?",
        "options": [
            {"text": "The solid would dissolve into the air if the bottle "
                     "were left open on a bench",
             "correct": False,
             "why": "Solids do not dissolve in air; this one leaves the "
                    "bottle as a vapour"},
            {"text": "Toxic vapour can leave the bottle without the solid "
                     "ever melting",
             "correct": True},
            {"text": "The vapour would turn back into a liquid on a cool "
                     "storeroom shelf",
             "correct": False,
             "why": "The change runs from solid straight to vapour, with no "
                    "liquid stage at all"},
            {"text": "Iodine would react with the glass of the bottle",
             "correct": False,
             "why": "Iodine does not attack glass; it is the escaping "
                    "vapour that matters"},
        ],
        "figure": None,
    },
    {
        "id": "c8-05-s24",
        "band": "standard",
        "text": "Why are the nine halogen tubes shown as a demonstration "
                "rather than handed to a class?",
        "options": [
            {"text": "All three reactions are far too slow to finish within a "
                     "single lesson",
             "correct": False,
             "why": "The colour changes appear almost at once; speed is not "
                    "the problem"},
            {"text": "All three solutions cost far too much to share around a "
                     "class",
             "correct": False,
             "why": "Cost is not what keeps them in the fume cupboard; "
                    "their vapours are"},
            {"text": "All three halogens are toxic and their vapours are "
                     "harmful",
             "correct": True},
            {"text": "All three colour changes are far too faint to be seen "
                     "from a bench",
             "correct": False,
             "why": "Orange and brown appearing in a colourless solution "
                    "are among the clearest changes there are"},
        ],
        "figure": None,
    },
    {
        "id": "c8-05-s25",
        "band": "standard",
        "text": "The rule says a more reactive halogen displaces a less "
                "reactive one, never the other way round. Why does the "
                "second half of that sentence matter?",
        "options": [
            {"text": "It makes the rule a great deal easier for a student "
                     "to remember",
             "correct": False,
             "why": "Ease of memory is not what the clause adds; what it "
                    "adds is direction"},
            {"text": "It shows every one of the reactions can be reversed "
                     "by heating",
             "correct": False,
             "why": "Nothing here reverses, which is exactly what the "
                    "clause rules out"},
            {"text": "It shows displacement works only between two halogens "
                     "that are neighbours in the group",
             "correct": False,
             "why": "Chlorine displaces iodine with bromine in between, so "
                    "neighbours are not required"},
            {"text": "It turns the results into an order rather than a list",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c8-05-s26",
        "band": "standard",
        "text": "A colourless halide solution is shaken with a halogen and "
                "a colour appears. How does the colour alone name the "
                "element that has been set free?",
        "options": [
            {"text": "Orange means bromine and brown means iodine",
             "correct": True},
            {"text": "Orange means iodine and brown means bromine",
             "correct": False,
             "why": "The two are the wrong way round; bromine is the orange "
                    "one"},
            {"text": "Any colour at all means chlorine has been set free",
             "correct": False,
             "why": "Chlorine is the halogen being added, so it is never "
                    "the one pushed out here"},
            {"text": "The colour shows only that something reacted",
             "correct": False,
             "why": "Each halogen has its own colour, and that is what "
                    "names it"},
        ],
        "figure": None,
    },
    {
        "id": "c8-05-s27",
        "band": "standard",
        "text": "Colour, melting point and reactivity all change steadily "
                "going down group 7. Which of the three runs in the "
                "opposite direction from the other two?",
        "options": [
            {"text": "Colour, which pales while the other two rise",
             "correct": False,
             "why": "The colours darken going down, so colour rises with "
                    "melting point"},
            {"text": "Reactivity, which falls while the other two rise",
             "correct": True},
            {"text": "Melting point, which falls going down while the other "
                     "two rise",
             "correct": False,
             "why": "Melting point rises going down, which is why the "
                    "bottom of the group is a solid"},
            {"text": "None of the three; they all rise together",
             "correct": False,
             "why": "Reactivity falls going down group 7 while the other "
                    "two rise"},
        ],
        "figure": None,
    },
    {
        "id": "c8-05-s28",
        "band": "standard",
        "text": "A student says astatine must be a gas, because fluorine "
                "and chlorine are gases. What is the fault in that?",
        "options": [
            {"text": "Fluorine and chlorine are liquids, not gases",
             "correct": False,
             "why": "Both are gases at room temperature, so that part of "
                    "the claim is right"},
            {"text": "Astatine is not in group 7 at all, so the trend "
                     "running down the group cannot apply to it",
             "correct": False,
             "why": "Astatine is the halogen below iodine and the group "
                    "trends do apply to it"},
            {"text": "The states run gas to liquid to solid going down, so "
                     "astatine would be a solid",
             "correct": True},
            {"text": "Nothing is wrong; the two gases at the top settle it",
             "correct": False,
             "why": "Bromine is a liquid and iodine a solid, so the group "
                    "does not stay gaseous"},
        ],
        "figure": None,
    },
    {
        "id": "c8-05-s29",
        "band": "standard",
        "text": "Potassium chloride, potassium bromide and potassium iodide "
                "solutions are all colourless. Why is that useful in this "
                "experiment?",
        "options": [
            {"text": "Any difference between the three must be a difference in "
                     "concentration",
             "correct": False,
             "why": "Being colourless says nothing about how much salt is "
                    "dissolved in the water"},
            {"text": "Any of the three will sit unreacted whatever is added to "
                     "it",
             "correct": False,
             "why": "Two of the three give up their halogen readily when "
                    "the right halogen is added"},
            {"text": "Any halogen will dissolve in them far more easily",
             "correct": False,
             "why": "Colour has nothing to do with how well anything "
                    "dissolves"},
            {"text": "Any colour that appears must be a halogen set free",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c8-05-s30",
        "band": "standard",
        "text": "PTFE, a compound of carbon and fluorine, is the surface of "
                "a pan that is heated every day. What does that use tell "
                "you about the compound?",
        "options": [
            {"text": "It is unreactive, unlike the element it is made from",
             "correct": True},
            {"text": "It is every bit as reactive as the fluorine it is "
                     "made from",
             "correct": False,
             "why": "A surface that food is cooked on could not be as "
                    "reactive as the fiercest element in the table"},
            {"text": "It must contain no fluorine at all once the pan is "
                     "made",
             "correct": False,
             "why": "The fluorine is still there, joined along the carbon "
                    "chain"},
            {"text": "It is a halide of a metal, which is why it stands up "
                     "to the heat of a hob",
             "correct": False,
             "why": "PTFE contains no metal at all; it is carbon and "
                    "fluorine"},
        ],
        "figure": None,
    },
    {
        "id": "c8-05-s31",
        "band": "standard",
        "text": "Why is one word, halogen, used for the element and "
                "another, halide, for the compound?",
        "options": [
            {"text": "They mean the same thing and either will do",
             "correct": False,
             "why": "One names a reactive element and the other a salt; "
                    "they are different substances"},
            {"text": "A halogen is a solid halide, and a halide is nothing "
                     "more than that same element once dissolved",
             "correct": False,
             "why": "State and solution have nothing to do with it; the "
                    "difference is element against compound"},
            {"text": "The halogen is the element itself, and a halide is "
                     "what it becomes joined to a metal",
             "correct": True},
            {"text": "A halide is a halogen made safe by heating",
             "correct": False,
             "why": "Heating changes nothing; the halogen has to join with "
                    "a metal"},
        ],
        "figure": None,
    },
    # ── harder · appended MRB-338 ───────────────────────────────────────
    {
        "id": "c8-05-h08",
        "band": "harder",
        "text": "An unknown halogen displaces iodine from potassium iodide "
                "solution but leaves potassium bromide solution unchanged. "
                "Which halogen is it?",
        "options": [
            {"text": "Chlorine",
             "correct": False,
             "why": "Chlorine is above bromine and would have turned the "
                    "potassium bromide orange"},
            {"text": "Iodine",
             "correct": False,
             "why": "Iodine cannot displace itself, so the potassium iodide "
                    "tube would have shown nothing"},
            {"text": "Astatine",
             "correct": False,
             "why": "Astatine sits below iodine and is the mildest halogen "
                    "of all; it would have displaced nothing"},
            {"text": "Bromine", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c8-05-h09",
        "band": "harder",
        "text": "A technician has chlorine water, bromine water and iodine "
                "solution, but the only halide left in the prep room is "
                "potassium iodide. Can the order of the three halogens "
                "still be worked out?",
        "options": [
            {"text": "No — chlorine and bromine would both displace iodine, "
                     "so nothing separates those two",
             "correct": True},
            {"text": "Yes — three halogens into the one solution gives "
                     "three separate results, and three is enough",
             "correct": False,
             "why": "Two of the three results would look the same, and "
                    "identical results cannot rank the elements that caused "
                    "them"},
            {"text": "No — reactivity cannot be ranked without weighing the "
                     "elements first",
             "correct": False,
             "why": "Reactivity here is ranked by what displaces what, and "
                    "no balance comes into it"},
            {"text": "Yes — the colours of the three halogens give the "
                     "order on their own",
             "correct": False,
             "why": "Colour darkens going down the group but proves nothing "
                    "about which element displaces which"},
        ],
        "figure": None,
    },
    {
        "id": "c8-05-h10",
        "band": "harder",
        "text": "Astatine is intensely radioactive and the largest sample "
                "ever made was too small to see. How can a book still "
                "describe its colour and its reactivity?",
        "options": [
            {"text": "By measuring a sample held in a sealed laboratory "
                     "somewhere — the description is an observation",
             "correct": False,
             "why": "No visible sample has ever existed, so nothing about "
                    "it has been measured that way"},
            {"text": "By carrying the group's trends one step further down "
                     "— the description is a prediction, not an observation",
             "correct": True},
            {"text": "By assuming it behaves exactly like iodine above it — "
                     "the description is copied, not predicted",
             "correct": False,
             "why": "A trend gives a direction of change, not a copy of the "
                    "element above"},
            {"text": "By reading off its mass — a radioactive element's "
                     "properties follow from how heavy it is",
             "correct": False,
             "why": "Mass gives neither colour nor reactivity; the group "
                    "trends do"},
        ],
        "figure": None,
    },
    {
        "id": "c8-05-h11",
        "band": "harder",
        "text": "Why is saying that fluorine is the most reactive element "
                "in the periodic table a bigger claim than saying it is the "
                "most reactive halogen?",
        "options": [
            {"text": "It is the same claim made twice over, since the "
                     "halogens are the reactive part of the table",
             "correct": False,
             "why": "The group 1 metals are fiercely reactive too, and they "
                    "sit in a different column"},
            {"text": "It is the smaller claim, since a group holds fewer "
                     "rivals to beat",
             "correct": False,
             "why": "Beating fewer rivals is the easier claim, so the "
                    "group-only version is the smaller one"},
            {"text": "It sets fluorine against every element in the table, "
                     "not only against its own column",
             "correct": True},
            {"text": "It is bigger because fluorine is the lightest halogen",
             "correct": False,
             "why": "Mass is not what the claim is about; reactivity is"},
        ],
        "figure": None,
    },
    {
        "id": "c8-05-h12",
        "band": "harder",
        "text": "A student runs nine tubes with three halogens and three "
                "halides and concludes that chlorine is the most reactive "
                "element in the periodic table. What is wrong with that?",
        "options": [
            {"text": "Nothing — chlorine displaced both of the others",
             "correct": False,
             "why": "It displaced two halogens, which ranks it among those "
                    "three and no further"},
            {"text": "Chlorine displaced nothing in any of the nine tubes, "
                     "so it cannot be ranked",
             "correct": False,
             "why": "Chlorine displaced both bromine and iodine, which is "
                    "what puts it at the top of the three"},
            {"text": "Reactivity cannot be compared between elements",
             "correct": False,
             "why": "Comparing reactivity is exactly what a displacement "
                    "reaction does"},
            {"text": "The tubes held three halogens only, and say nothing "
                     "about any other element",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c8-05-h13",
        "band": "harder",
        "text": "Six of nine halogen tubes showed no change. A student "
                "proposes repeating only the three that reacted. Why is "
                "that a poor plan?",
        "options": [
            {"text": "The six that did nothing are half the evidence that "
                     "the order runs one way only",
             "correct": True},
            {"text": "Repeating a reaction that has already worked once is "
                     "never worth doing in a science lesson",
             "correct": False,
             "why": "Repeating results is exactly how they are checked; the "
                    "fault is in leaving six of them out"},
            {"text": "The six tubes would react if they were left longer",
             "correct": False,
             "why": "They are not slow reactions; they are reactions that "
                    "cannot happen at all"},
            {"text": "Three results are too few to be worth repeating",
             "correct": False,
             "why": "The number is not the problem; dropping the results "
                    "that fix the direction is"},
        ],
        "figure": None,
    },
    {
        "id": "c8-05-h14",
        "band": "harder",
        "text": "Orange bromine water is shaken with a colourless potassium "
                "iodide solution and the tube goes brown. How can you be "
                "sure the brown is not simply more concentrated bromine "
                "water?",
        "options": [
            {"text": "The tube was shaken, and shaking a solution will "
                     "always deepen whatever colour is in it",
             "correct": False,
             "why": "Shaking mixes the contents; it does not create a new "
                    "colour"},
            {"text": "Bromine water is orange at any strength, and brown is "
                     "iodine's own colour",
             "correct": True},
            {"text": "Bromine water goes colourless whenever it reacts",
             "correct": False,
             "why": "Bromine water is orange before and after; the colour "
                    "that matters is the new one"},
            {"text": "You cannot tell, because orange and brown are the "
                     "same colour",
             "correct": False,
             "why": "They are different colours belonging to two different "
                    "elements"},
        ],
        "figure": None,
    },
    {
        "id": "c8-05-h15",
        "band": "harder",
        "text": "Chlorine gas is toxic, yet chlorine is deliberately added "
                "to drinking water. Explain how both statements can be "
                "true.",
        "options": [
            {"text": "Chlorine stops being chlorine once it is in water, so "
                     "nothing toxic is left in the supply",
             "correct": False,
             "why": "It is still chlorine; what changes is how much of it "
                    "there is"},
            {"text": "Water is a compound, so anything dissolved in it at one "
                     "part per million stops being toxic",
             "correct": False,
             "why": "Many toxic substances dissolve in water and stay every "
                    "bit as toxic"},
            {"text": "At about one part per million there is enough to kill "
                     "bacteria and far too little to harm a person",
             "correct": True},
            {"text": "Chlorine harms bacteria and never harms people, whatever "
                     "amount of it is used",
             "correct": False,
             "why": "Chlorine harms people too, which is why the amount "
                    "used is kept so small"},
        ],
        "figure": None,
    },
    {
        "id": "c8-05-h16",
        "band": "harder",
        "text": "A student writes that iodine is the least reactive halogen "
                "and is therefore safe. Evaluate that.",
        "options": [
            {"text": "Correct, because the mildest member of any group is "
                     "harmless to use",
             "correct": False,
             "why": "The mildest member of a poisonous group is still "
                    "poisonous"},
            {"text": "Most reactive of the four halogens is what iodine is, "
                     "not least",
             "correct": False,
             "why": "Iodine is near the bottom of group 7 and is the "
                    "mildest of the four"},
            {"text": "Wrong, because iodine is not a halogen at all",
             "correct": False,
             "why": "Iodine is a group 7 element and one of the four "
                    "halogens"},
            {"text": "Least reactive of four poisonous elements is not the "
                     "same as safe",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c8-05-h17",
        "band": "harder",
        "text": "Why does a grid of tubes give an order of three halogens "
                "when a single tube gives only a comparison of two?",
        "options": [
            {"text": "Each tube ranks one pair, and every pair together "
                     "ranks all three",
             "correct": True},
            {"text": "A grid uses more solution, and that makes every "
                     "result more reliable",
             "correct": False,
             "why": "How much solution is used does not decide what can be "
                    "ranked"},
            {"text": "A grid can be read in either direction, which is what "
                     "settles the order of the three",
             "correct": False,
             "why": "Reading direction changes nothing; the number of pairs "
                    "compared does"},
            {"text": "One tube on its own cannot show a reaction at all",
             "correct": False,
             "why": "A single tube shows a reaction perfectly well; it just "
                    "compares only two elements"},
        ],
        "figure": None,
    },
    {
        "id": "c8-05-h18",
        "band": "harder",
        "text": "Fluorine attacks almost everything it touches, yet a "
                "compound of fluorine is chosen as the surface of a pan "
                "that must not react with food. Explain.",
        "options": [
            {"text": "The fluorine in the pan was made unreactive by heating, "
                     "so it lost the properties of the element",
             "correct": False,
             "why": "Heat does not tame an element; joining it into a "
                    "compound does"},
            {"text": "The fluorine is already joined to carbon, so the "
                     "compound is a different substance with its own "
                     "properties",
             "correct": True},
            {"text": "The pan holds too little fluorine to react, so the "
                     "amount present is what makes it safe",
             "correct": False,
             "why": "The amount is not the point; the compound is "
                    "unreactive at any thickness"},
            {"text": "Fluorine is only reactive when it is cold, so a pan on a "
                     "hob is never in any danger",
             "correct": False,
             "why": "Fluorine is the most reactive element there is at "
                    "ordinary temperatures"},
        ],
        "figure": None,
    },
    {
        "id": "c8-05-h19",
        "band": "harder",
        "text": "Fluorine is handled in metal vessels that have "
                "deliberately been coated with their own fluoride. Explain "
                "how that protects the vessel.",
        "options": [
            {"text": "The coating keeps the metal too cold to be attacked, and "
                     "cold metal is what fluorine leaves alone",
             "correct": False,
             "why": "Temperature is not what stops the attack; a layer of "
                    "compound is"},
            {"text": "The coating is thicker than the metal underneath it, and "
                     "thickness is what holds the fluorine off",
             "correct": False,
             "why": "Thickness is not the reason; the layer works because "
                    "it is a compound that no longer reacts"},
            {"text": "The surface reacts once to make a fluoride layer, and "
                     "that layer is unreactive and seals what is underneath",
             "correct": True},
            {"text": "The fluoride coating reacts with the fluorine and uses "
                     "it up before it can reach the metal",
             "correct": False,
             "why": "A coating that kept reacting would be eaten away; it "
                    "protects because it does not react"},
        ],
        "figure": None,
    },
    {
        "id": "c8-05-h20",
        "band": "harder",
        "text": "A student ranks the halogens by melting point and calls "
                "the list a reactivity series. Why does the list come out "
                "wrong?",
        "options": [
            {"text": "Melting point and reactivity both fall going down, so "
                     "the list is right",
             "correct": False,
             "why": "Melting point rises going down group 7; it is only "
                    "reactivity that falls"},
            {"text": "Melting point cannot be measured for a gas, so the "
                     "list is incomplete",
             "correct": False,
             "why": "Fluorine and chlorine both have melting points, well "
                    "below room temperature"},
            {"text": "A reactivity series can only ever be built from metals",
             "correct": False,
             "why": "The nine tubes build one for three non-metals, which "
                    "is what the grid is for"},
            {"text": "Melting point rises going down group 7 while "
                     "reactivity falls, so the list runs backwards",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c8-05-h21",
        "band": "harder",
        "text": "Chlorine kills bacteria in a reservoir and iodine kills "
                "bacteria on skin. What does that pair of uses show about "
                "the group?",
        "options": [
            {"text": "The reactivity that makes the halogens dangerous is "
                     "what makes them useful",
             "correct": True},
            {"text": "The halogens are harmless enough, since both of these "
                     "are used on or near people every day",
             "correct": False,
             "why": "Both elements are toxic; they are used at a strength "
                    "that suits the job"},
            {"text": "Chlorine and iodine are the only halogens with a use",
             "correct": False,
             "why": "Fluorine compounds are in toothpaste and on non-stick "
                    "pans"},
            {"text": "Reactivity has nothing to do with what a halogen is "
                     "used for",
             "correct": False,
             "why": "Both of these uses depend on the element attacking "
                    "something living"},
        ],
        "figure": None,
    },
    {
        "id": "c8-05-h22",
        "band": "harder",
        "text": "Chlorine water added to potassium chloride gives no "
                "change, and iodine solution added to potassium iodide "
                "gives none either. What do those two tubes have in common?",
        "options": [
            {"text": "In each one the halogen that was added is the more "
                     "reactive of the two in the tube",
             "correct": False,
             "why": "There are not two halogens in either tube; there is "
                    "one element, twice over"},
            {"text": "In each one the halogen added is the same element as "
                     "the one in the salt",
             "correct": True},
            {"text": "In each one the solution was much too dilute to show "
                     "any change of colour",
             "correct": False,
             "why": "Dilution would slow a reaction that could happen; "
                    "neither of these can happen"},
            {"text": "In each one the potassium was displaced instead",
             "correct": False,
             "why": "Potassium stays where it is, and nothing is displaced "
                    "in either tube"},
        ],
        "figure": None,
    },
    {
        "id": "c8-05-h23",
        "band": "harder",
        "text": "Suppose iodine solution added to potassium chloride had "
                "turned the tube pale green. What would that single result "
                "do to the conclusion about group 7?",
        "options": [
            {"text": "Nothing much, since one odd result can usually be set "
                     "aside and the order left standing",
             "correct": False,
             "why": "A result that contradicts the rule is the most "
                    "important one there is"},
            {"text": "It would prove at once that reactivity rises down group "
                     "7, and the trend could be rewritten there and then",
             "correct": False,
             "why": "It would have to be checked first; one tube does not "
                    "overturn a rule"},
            {"text": "It would contradict the order, so it would have to be "
                     "checked and, if real, the trend rewritten",
             "correct": True},
            {"text": "It would prove the potassium had reacted, and nothing "
                     "about the halogens would be touched",
             "correct": False,
             "why": "Pale green is chlorine's colour, so it is chlorine "
                    "that would have been set free"},
        ],
        "figure": None,
    },
    {
        "id": "c8-05-h24",
        "band": "harder",
        "text": "Three tubes hold the same halide solution and three "
                "different halogens, and only one tube changes colour. What "
                "makes that a fair comparison?",
        "options": [
            {"text": "Nothing — three tubes are too few to compare anything",
             "correct": False,
             "why": "Three tubes with one thing changed between them is "
                    "exactly a fair comparison"},
            {"text": "The halide was changed each time, and changing the "
                     "thing you measure is what makes a test fair",
             "correct": False,
             "why": "The halide was kept the same; changing two things at "
                    "once would spoil the test"},
            {"text": "The three halogens were added in alphabetical order",
             "correct": False,
             "why": "The order of adding cannot affect which tube changes "
                    "colour"},
            {"text": "Only the halogen differs, so the difference in result "
                     "must be down to the halogen",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c8-05-h25",
        "band": "harder",
        "text": "Chlorine water is added to a solution of potassium "
                "astatide. Predict the result and name the products.",
        "options": [
            {"text": "A colour change, giving potassium chloride and "
                     "astatine",
             "correct": True},
            {"text": "No change, because astatine is too far below chlorine",
             "correct": False,
             "why": "Sitting further down the group makes a displacement "
                    "more certain, not less"},
            {"text": "A colour change, giving potassium astatide and "
                     "chlorine",
             "correct": False,
             "why": "Those are the two starting substances; nothing has "
                    "changed hands"},
            {"text": "No change, because a halogen cannot displace a "
                     "radioactive element",
             "correct": False,
             "why": "Radioactivity has nothing to do with where an element "
                    "sits in a reactivity order"},
        ],
        "figure": None,
    },
    {
        "id": "c8-05-h26",
        "band": "harder",
        "text": "No indicator is used anywhere in the nine halogen tubes. "
                "Why is none needed?",
        "options": [
            {"text": "The tubes are kept sealed, so nothing further can be "
                     "added to any of them",
             "correct": False,
             "why": "The tubes are open and shaken; adding something would "
                    "be easy"},
            {"text": "Each halogen has its own colour, so an element set "
                     "free announces itself",
             "correct": True},
            {"text": "Indicators do not work properly inside a fume "
                     "cupboard while the air is moving past",
             "correct": False,
             "why": "A fume cupboard changes nothing about how an indicator "
                    "behaves"},
            {"text": "The reactions are too fast for an indicator",
             "correct": False,
             "why": "An indicator responds instantly; the point is that "
                    "none is needed here"},
        ],
        "figure": None,
    },
    {
        "id": "c8-05-h27",
        "band": "harder",
        "text": "The halogens get darker, denser and less reactive going "
                "down the group. Which of those three can a tube of halide "
                "solution actually test?",
        "options": [
            {"text": "Density, because the element that is displaced sinks "
                     "to the bottom of the tube",
             "correct": False,
             "why": "Nothing sinks in these tubes; both elements stay in "
                    "the solution"},
            {"text": "All three at once, because the tube shows everything "
                     "about an element",
             "correct": False,
             "why": "A tube shows one thing: whether one halogen can take "
                    "another's place"},
            {"text": "Reactivity, because a displacement either happens or "
                     "it does not",
             "correct": True},
            {"text": "None of them, since a colour change is not a "
                     "measurement of anything",
             "correct": False,
             "why": "Whether a displacement happens is a real result, and "
                    "it is what ranks the three"},
        ],
        "figure": None,
    },
    {
        "id": "c8-05-h28",
        "band": "harder",
        "text": "Why is the rule that a more reactive halogen displaces a "
                "less reactive one worth more than a list of which nine "
                "tubes changed colour?",
        "options": [
            {"text": "The list is longer, and a longer answer in science is "
                     "always worth more marks than a rule",
             "correct": False,
             "why": "Length is not worth; the rule does work that the list "
                    "cannot"},
            {"text": "The rule is a great deal quicker to write down than "
                     "nine separate results",
             "correct": False,
             "why": "Brevity is not the gain here; prediction is"},
            {"text": "The list is wrong, since only three tubes reacted",
             "correct": False,
             "why": "The list is perfectly correct; it simply cannot reach "
                    "past the nine tubes"},
            {"text": "The rule predicts tubes nobody has run, including "
                     "ones holding astatine",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c8-05-h29",
        "band": "harder",
        "text": "A bottle labelled only halogen solution holds a brown "
                "liquid. Added to potassium bromide solution it gives no "
                "change. Identify the contents and justify it.",
        "options": [
            {"text": "Iodine solution, because it is brown and cannot "
                     "displace bromine",
             "correct": True},
            {"text": "Chlorine water, because it is brown and can displace "
                     "nothing at all",
             "correct": False,
             "why": "Chlorine water is pale green, and it displaces bromine "
                    "readily"},
            {"text": "Bromine water, because brown is the colour bromine "
                     "has in solution",
             "correct": False,
             "why": "Bromine water is orange rather than brown; brown is "
                    "iodine"},
            {"text": "Potassium bromide solution, since a bromide is itself "
                     "a brown halide in water",
             "correct": False,
             "why": "Potassium bromide solution is colourless, and it is "
                    "not a halogen"},
        ],
        "figure": None,
    },
    {
        "id": "c8-05-h30",
        "band": "harder",
        "text": "Would astatine displace iodine from potassium iodide "
                "solution? Predict the result and say why.",
        "options": [
            {"text": "A colour change, because astatine is below iodine and "
                     "so reacts harder",
             "correct": False,
             "why": "Reactivity falls going down group 7, so sitting lower "
                    "makes astatine the milder one"},
            {"text": "No change, because astatine is below iodine and so is "
                     "the milder of the two",
             "correct": True},
            {"text": "A colour change, because the heavier halogen always "
                     "wins",
             "correct": False,
             "why": "Mass does not decide a displacement; position in the "
                    "group does"},
            {"text": "No change, because astatine and iodine are the same "
                     "element",
             "correct": False,
             "why": "They are different elements, one place apart in group 7"},
        ],
        "figure": None,
    },
    {
        "id": "c8-05-h31",
        "band": "harder",
        "text": "Table salt is a halide and is eaten every day; chlorine is "
                "a halogen and is poisonous. A student concludes that "
                "compounds are always safer than their elements. Evaluate.",
        "options": [
            {"text": "Correct, because a compound can never be poisonous",
             "correct": False,
             "why": "Plenty of compounds are poisonous; joining atoms up is "
                    "no guarantee of safety"},
            {"text": "Wrong, because table salt is really just chlorine",
             "correct": False,
             "why": "Table salt is a compound of sodium and chlorine and "
                    "behaves like neither of them"},
            {"text": "Too far — an element and its compound are different "
                     "substances, which is not the same as safer",
             "correct": True},
            {"text": "Correct, because a compound holds fewer atoms than an "
                     "element",
             "correct": False,
             "why": "A compound holds more kinds of atom, not fewer, and "
                    "the count says nothing about safety"},
        ],
        "figure": None,
    },
    {
        "id": "c8-05-h32",
        "band": "harder",
        "text": "A student has two results: chlorine into potassium iodide "
                "reacts, and iodine into potassium chloride does not. Is "
                "the second result needed, given the first?",
        "options": [
            {"text": "Yes — an order predicts the non-reaction too, and "
                     "finding one would break it",
             "correct": True},
            {"text": "No — a reaction that does not happen is not a result",
             "correct": False,
             "why": "A tube that stays unchanged is a real observation, and "
                    "half the argument rests on six of them"},
            {"text": "Yes — because two results are always better than one",
             "correct": False,
             "why": "Number is not the reason; what the second tube tests is"},
            {"text": "No — the two tubes hold different salts as well as "
                     "different halogens, so they cannot be compared",
             "correct": False,
             "why": "Comparing them is the point: each tests the same order "
                    "from a different side"},
        ],
        "figure": None,
    },
]
