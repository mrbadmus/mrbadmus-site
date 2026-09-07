"""C5 lesson 05 — Which reaction is this?: twelve questions (MRB-246).

The lesson has one rule and two traps. The rule is that a reaction is named
from its REACTANTS — count them, then look for oxygen or for a metal — and
never from what it looked like. The first trap is that two of the four names
can be right at once, because combustion sits inside oxidation. The second is
that a reaction can fall outside all four, which is what reaction 8 on the
page does on purpose.

The distractors are built from the lesson's declared misconception and from
the wrong rule the whole page argues with. `REACT-18` (each reaction has
exactly one type, so two names cannot both be right) drives the wrong options
in s01, h02 and h04 — each of them treats the four names as four sealed boxes,
which is the belief `#s-think` exists to break. The appearance rule (name it
from the drama: the colour, the heat, the gas) drives e01, e02, e03, e04 and
h01, where a visible clue is taken to settle a question only the reactants can
reach.

A third strand runs through s02, h02 and h03 and is in neither of those: that
a classification must cover everything, so a case that fits nothing means the
STUDENT has failed. It is the wrong idea reaction 8 is built to elicit, and it
is invisible to `REACT-18` because a student who holds it is trying to obey
the rule rather than to break it. Those three carry a distractor that forces
the case into a box, and the `why` on each says what a scientist does instead.

⚠️ THERE IS NO FIFTH REACTION TYPE ANYWHERE IN THIS FILE. "None of the four"
is an answer about the SET, not a member of it, and no question here may be
read as offering a fifth name. The lesson's `covers` clause turns on that
distinction.

Every question here is new prose — a question bank is the one place in these
two files where that is true — and the bar is §13's: each distractor is a
WRONG RULE in the correct answer's own shape, and each is a mistake a real
student in a real lesson actually makes. Every set was measured: no correct
option is the strictly longest by four words or by 1.4×, and where a set came
close the fix was made AT THE DISTRACTOR.
"""

UNIT = "C5"
LESSON = "which-reaction-is-this"
LESSON_NUMBER = 5

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "c5-05-e01",
        "band": "easier",
        "text": "A reaction has one reactant and two products, and it needs "
                "heating the whole time. Which type is it?",
        "options": [
            {"text": "Thermal decomposition, because one reactant is broken "
                     "apart", "correct": True},
            {"text": "Combustion, because heating is what starts a fire",
             "correct": False,
             "why": "Combustion needs two reactants and one of them has to be "
                    "oxygen. Heat starts it, and after that it makes its own."},
            {"text": "Oxidation, because heating adds oxygen from the air",
             "correct": False,
             "why": "Heating does not add anything. Oxidation needs oxygen "
                    "written on the left of the equation as a reactant."},
            {"text": "Displacement, because heating frees one metal from "
                     "another", "correct": False,
             "why": "Displacement needs two reactants: a metal, and a "
                    "compound of a different metal. One reactant rules it "
                    "out."},
                   ],
        "figure": None,
    },
    {
        "id": "c5-05-e02",
        "band": "easier",
        "text": "Which of these tells you most reliably what type a reaction "
                "is?",
        "options": [
            {"text": "What colour the mixture went, and how quickly",
             "correct": False,
             "why": "Copper carbonate goes black and so does copper heated in "
                    "air, and they are different types. Colour is a clue and "
                    "never the test."},
            {"text": "What the reactants are, and how many of them",
             "correct": True},
            {"text": "How much heat and light it gave out", "correct": False,
             "why": "Thermite and a burning candle both give out a great "
                    "deal, and one is a displacement. Rusting gives out "
                    "almost none and is still a reaction."},
            {"text": "Whether a gas came off, and how much", "correct": False,
             "why": "A gas comes off a decomposing carbonate and off marble "
                    "in acid, and those are not even the same kind of thing."},
        ],
        "figure": None,
    },
    {
        "id": "c5-05-e03",
        "band": "easier",
        "text": "Petrol burns in a car engine with oxygen drawn in from the "
                "air. Which type is it?",
        "options": [
            {"text": "None of the four, because an engine only changes energy",
             "correct": False,
             "why": "An engine does change energy, and it does it BY running "
                    "a reaction. The petrol is gone afterwards and new "
                    "substances have come out of the exhaust."},
            {"text": "Displacement, because the petrol pushes the air out",
             "correct": False,
             "why": "Displacement is one metal taking another's place in a "
                    "compound. Pushing air along a pipe is not a chemical "
                    "reaction at all."},
            {"text": "Combustion, because a fuel reacts with oxygen and "
                     "burns", "correct": True},
            {"text": "Thermal decomposition, because the petrol is broken "
                     "apart", "correct": False,
             "why": "There are two reactants here, petrol and oxygen. "
                    "Decomposition is the one type that starts with a single "
                    "substance."},
        ],
        "figure": None,
    },
    {
        "id": "c5-05-e04",
        "band": "easier",
        "text": "Magnesium is added to blue copper sulfate solution and a "
                "brown solid appears. Which type is it?",
        "options": [
            {"text": "Combustion, because the magnesium is being used up",
             "correct": False,
             "why": "Nothing is burning and there is no oxygen reactant. A "
                    "reactant being used up happens in every reaction there "
                    "is."},
            {"text": "Oxidation, because the magnesium gains oxygen from the "
                     "sulfate", "correct": False,
             "why": "Oxygen has to be a reactant in its own right. The "
                    "magnesium is taking the copper's place in the compound, "
                    "not taking oxygen off it."},
            {"text": "Thermal decomposition, because the copper sulfate "
                     "splits up", "correct": False,
             "why": "Nothing was heated, and there are two reactants. The "
                    "copper sulfate has a partner here, which decomposition "
                    "never does."},
            {"text": "Displacement, because a more reactive metal takes "
                     "copper's place", "correct": True},
                   ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "c5-05-s01",
        "band": "standard",
        "text": "One student writes \"combustion\" for burning magnesium and "
                "another writes \"oxidation\". Which is right?",
        "options": [
            {"text": "Both names are right, and combustion is the more "
                     "specific one", "correct": True},
            {"text": "Only oxidation is right, because combustion is for "
                     "fuels alone", "correct": False,
             "why": "Magnesium behaves as a fuel here: it burns with a flame "
                    "and gives out energy. Combustion is not reserved for "
                    "things you put in an engine."},
            {"text": "Only combustion is right, because oxidation needs no "
                     "flame at all", "correct": False,
             "why": "Oxidation means gaining oxygen, whether there is a flame "
                    "or not. Magnesium gains oxygen, so it is unquestionably "
                    "an oxidation."},
            {"text": "Neither is right, because burning a metal has no name",
             "correct": False,
             "why": "Burning a metal has two names that both fit. A reaction "
                    "having more than one correct name is normal, not a sign "
                    "that neither works."},
        ],
        "figure": None,
    },
    {
        "id": "c5-05-s02",
        "band": "standard",
        "text": "Marble chips fizz in hydrochloric acid, giving off carbon "
                "dioxide. Which of the four types is it?",
        "options": [
            {"text": "Thermal decomposition, because the marble breaks apart "
                     "and a gas leaves", "correct": False,
             "why": "Decomposition has ONE reactant and needs heating. Here "
                    "there are two reactants and nothing was heated at all."},
            {"text": "None of them — it is a neutralisation, which the four "
                     "do not cover", "correct": True},
            {"text": "Displacement, because the acid takes the place of the "
                     "carbonate", "correct": False,
             "why": "Displacement needs a metal and a compound of a different "
                    "metal. An acid is not a metal, so there is nothing here "
                    "doing the displacing."},
            {"text": "Oxidation, because a gas containing oxygen comes off "
                     "the marble", "correct": False,
             "why": "Oxidation means a substance GAINS oxygen from oxygen as "
                    "a reactant. Oxygen atoms being carried away inside a "
                    "product is the opposite direction."},
                   ],
        "figure": None,
    },
    {
        "id": "c5-05-s03",
        "band": "standard",
        "text": "Two test tubes are weighed before and after heating. One "
                "gains mass and one loses mass. What does that tell you?",
        "options": [
            {"text": "The heavier one lost a gas; the lighter one gained "
                     "oxygen", "correct": False,
             "why": "Exactly the wrong way round. Joining oxygen on can only "
                    "add mass, and letting a gas escape can only take mass "
                    "away."},
            {"text": "Both must be decompositions, because heating always "
                     "drives gas off", "correct": False,
             "why": "Heating copper in air makes it heavier, not lighter. "
                    "Heat is what makes a reaction go, not what decides which "
                    "type it is."},
            {"text": "The heavier one gained oxygen; the lighter one lost a "
                     "gas", "correct": True},
            {"text": "Nothing useful, because mass changes in every reaction "
                     "anyway", "correct": False,
             "why": "In a sealed container the mass never changes at all. "
                    "What changes here is what has come in from the air or "
                    "gone out into it."},
                   ],
        "figure": None,
    },
    {
        "id": "c5-05-s04",
        "band": "standard",
        "text": "Glucose reacts with oxygen inside a cell, giving carbon "
                "dioxide, water and energy. Which type is it?",
        "options": [
            {"text": "Combustion, because the same products come out of "
                     "burning glucose", "correct": False,
             "why": "The products match and the conditions do not. Combustion "
                    "burns, with a flame, all at once; a cell releases the "
                    "same energy in small steps at 37 °C."},
            {"text": "None of the four, because it happens in a living thing",
             "correct": False,
             "why": "Where a reaction happens does not change what it is. The "
                    "same reactants and the same products get the same name "
                    "inside a cell as in a beaker."},
            {"text": "Thermal decomposition, because the glucose is broken "
                     "down inside", "correct": False,
             "why": "Oxygen is a reactant here, so there are two, and nothing "
                    "was heated. Decomposition starts with one substance and "
                    "needs heat."},
            {"text": "Oxidation, because the glucose gains oxygen and gives "
                     "out energy", "correct": True},
                   ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "c5-05-h01",
        "band": "harder",
        "text": "Thermite reaches 2500 °C and pours out molten iron. A "
                "student calls it combustion. Where does that go wrong?",
        "options": [
            {"text": "It judges by the drama; the reactants are a metal and a "
                     "metal oxide", "correct": True},
            {"text": "Nowhere — anything reaching 2500 °C counts as burning "
                     "by definition", "correct": False,
             "why": "Temperature is not a type. A reaction is named from what "
                    "went into it, and nothing here was burning in oxygen "
                    "from the air."},
            {"text": "It is right about the flame but wrong about the oxygen "
                     "involved", "correct": False,
             "why": "There is no flame and no oxygen reactant. The oxygen in "
                    "this reaction is already locked inside the iron oxide "
                    "before it starts."},
            {"text": "Nothing is wrong; combustion and displacement mean the "
                     "same thing here", "correct": False,
             "why": "They mean different things everywhere. Combustion needs "
                    "oxygen as a reactant; displacement needs a metal and "
                    "another metal's compound."},
        ],
        "figure": None,
    },
    {
        "id": "c5-05-h02",
        "band": "harder",
        "text": "Why is it worth knowing that a reaction is a displacement?",
        "options": [
            {"text": "It tells you how fast the reaction will go once it has "
                     "started", "correct": False,
             "why": "The type says what happens, not how quickly. Rusting and "
                    "burning iron wool are both oxidations and one takes a "
                    "year."},
            {"text": "It lets you predict the products from a reactivity "
                     "order you can look up", "correct": True},
            {"text": "It proves the reaction gives out heat rather than "
                     "taking it in", "correct": False,
             "why": "Most displacements do give out heat, and that is a "
                    "separate way of sorting reactions rather than part of "
                    "what displacement means."},
            {"text": "It is the name the marks are for, and names are what "
                     "gets you the marks", "correct": False,
             "why": "A name that lets you predict nothing would not be worth "
                    "learning or worth a mark. The marks follow the "
                    "prediction, not the other way round."},
                   ],
        "figure": None,
    },
    {
        "id": "c5-05-h03",
        "band": "harder",
        "text": "A student meets a reaction that fits none of the four types. "
                "What is the best thing to do?",
        "options": [
            {"text": "Pick the closest of the four, because one of them must "
                     "apply", "correct": False,
             "why": "None of them has to apply. The four were built to cover "
                    "four kinds of reaction, and there are more kinds than "
                    "four."},
            {"text": "Assume the observation is wrong and repeat until a type "
                     "fits", "correct": False,
             "why": "Repeating until the result agrees with you is the one "
                    "thing a scientist may never do. The observation is the "
                    "evidence; the rule is the guess."},
            {"text": "Describe accurately what happened and record that no "
                     "type fits", "correct": True},
            {"text": "Leave it out, because a reaction with no type is not "
                     "real chemistry", "correct": False,
             "why": "It is real chemistry with a name of its own that this "
                    "set of four does not include. A case that falls outside "
                    "a rule is information about the rule."},
                   ],
        "figure": None,
    },
    {
        "id": "c5-05-h04",
        "band": "harder",
        "text": "Iron wool burns in oxygen with orange sparks; an iron nail "
                "rusts over a year. How are the two related?",
        "options": [
            {"text": "Only the burning is oxidation; rusting is a separate "
                     "type entirely", "correct": False,
             "why": "Rusting is iron gaining oxygen, which is what oxidation "
                    "means. It is the slow one, not a different one."},
            {"text": "Both are combustion; rusting is burning that happens "
                     "very slowly", "correct": False,
             "why": "Rusting has no flame and gives out no light, so it is "
                    "not a combustion. It also needs water, which burning "
                    "does not."},
            {"text": "Neither is oxidation, because iron does not gain oxygen "
                     "either way", "correct": False,
             "why": "Both products contain oxygen that was not in the iron "
                    "before, and both are heavier than the iron was. That "
                    "gain is the oxidation."},
            {"text": "Both are oxidation; only the fast one is also a "
                     "combustion", "correct": True},
        ],
        "figure": None,
    },

    # ── easier · MRB-335 top-up ─────────────────────────────────────────
    {
        "id": "c5-05-e05",
        "band": "easier",
        "text": "Combustion sits inside which of the other types?",
        "options": [
            {"text": "Thermal decomposition, because the fuel is broken apart "
                     "by the heat of its own flame as it burns",
             "correct": False,
             "why": "A decomposition has one reactant and takes energy in. "
                    "Combustion has two and gives energy out"},
            {"text": "Oxidation",
             "correct": True},
            {"text": "Displacement",
             "correct": False,
             "why": "Displacement needs a metal and another metal's compound. "
                    "Burning needs a fuel and oxygen"},
            {"text": "None of them — it stands on its own",
             "correct": False,
             "why": "Every combustion is a gain of oxygen, so every "
                    "combustion is an oxidation"},
        ],
        "figure": None,
    },
    {
        "id": "c5-05-e06",
        "band": "easier",
        "text": "What is synthesis?",
        "options": [
            {"text": "A substance being made in a laboratory rather than "
                     "found in nature, which is what the word means when it "
                     "appears on a label",
             "correct": False,
             "why": "That is the everyday use. Here it names the shape of the "
                    "reaction: several in, one out"},
            {"text": "One compound breaking into two or more substances",
             "correct": False,
             "why": "That is decomposition. Synthesis is the same thing run "
                    "the other way"},
            {"text": "Two or more substances joining to make one compound",
             "correct": True},
            {"text": "A metal taking another metal's place",
             "correct": False,
             "why": "That is displacement, and nothing is joined into one "
                    "compound"},
        ],
        "figure": None,
    },
    {
        "id": "c5-05-e07",
        "band": "easier",
        "text": "What does exothermic mean?",
        "options": [
            {"text": "Happening quickly, which is why combustion is "
                     "exothermic and a reaction taking twenty years cannot be",
             "correct": False,
             "why": "Rusting is slow and exothermic. Speed and energy "
                    "direction are separate"},
            {"text": "Taking energy in from the surroundings",
             "correct": False,
             "why": "That is endothermic, and thermal decomposition is the "
                    "example in this unit"},
            {"text": "Producing a gas",
             "correct": False,
             "why": "Nothing about the word is to do with gases. It is about "
                    "energy"},
            {"text": "Giving out energy to the surroundings",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c5-05-e08",
        "band": "easier",
        "text": "Which of the four types is endothermic?",
        "options": [
            {"text": "Thermal decomposition",
             "correct": True},
            {"text": "Combustion",
             "correct": False,
             "why": "Combustion gives out a great deal of energy. It is the "
                    "most obviously exothermic reaction there is"},
            {"text": "Displacement",
             "correct": False,
             "why": "Displacement gives energy out — thermite reaches "
                    "2500 °C"},
            {"text": "Oxidation, because a substance taking oxygen in must "
                     "take energy in along with it",
             "correct": False,
             "why": "Taking a substance in is nothing to do with taking "
                    "energy in. Oxidations give energy out"},
        ],
        "figure": None,
    },
    {
        "id": "c5-05-e09",
        "band": "easier",
        "text": "Which type of reaction is synthesis run backwards?",
        "options": [
            {"text": "Combustion, since burning a fuel takes it apart into "
                     "the two products it was built from and synthesis puts "
                     "substances together",
             "correct": False,
             "why": "Burning JOINS the fuel to oxygen. Nothing is being taken "
                    "apart into what it was made of"},
            {"text": "Thermal decomposition",
             "correct": True},
            {"text": "Displacement",
             "correct": False,
             "why": "Displacement swaps a partner. Neither direction of it "
                    "joins several substances into one"},
            {"text": "Oxidation",
             "correct": False,
             "why": "Oxidation is a gain of oxygen. Reversing synthesis is "
                    "about breaking one compound into several"},
        ],
        "figure": None,
    },
    {
        "id": "c5-05-e10",
        "band": "easier",
        "text": "How many reactants does a displacement have?",
        "options": [
            {"text": "One, since the compound is the only thing being changed "
                     "and the metal is simply what it is changed by",
             "correct": False,
             "why": "The metal is used up and ends in the solution. Both are "
                    "reactants"},
            {"text": "Three",
             "correct": False,
             "why": "Two is enough. Nothing else has to be added"},
            {"text": "Two — a metal, and a compound of another metal",
             "correct": True},
            {"text": "It depends which metals are used",
             "correct": False,
             "why": "The shape is the same whichever pair you choose"},
        ],
        "figure": None,
    },

    # ── standard · MRB-335 top-up ───────────────────────────────────────
    {
        "id": "c5-05-s05",
        "band": "standard",
        "text": "Iron and sulfur are heated together and make iron sulfide. "
                "Which type is that?",
        "options": [
            {"text": "Synthesis — two substances joining to make one",
             "correct": True},
            {"text": "Thermal decomposition, because heat is what makes it "
                     "happen and the dish is heated until it glows",
             "correct": False,
             "why": "Two reactants go in and one substance comes out. A "
                    "decomposition is the other way round"},
            {"text": "Displacement",
             "correct": False,
             "why": "Nothing takes anything else's place. Sulfur is not a "
                    "metal compound"},
            {"text": "Oxidation",
             "correct": False,
             "why": "No oxygen is involved at all — the dish can be heated in "
                    "a sealed tube"},
        ],
        "figure": None,
    },
    {
        "id": "c5-05-s06",
        "band": "standard",
        "text": "A copper strip is heated in air until it is black, and it "
                "weighs more afterwards. Which type is it?",
        "options": [
            {"text": "Thermal decomposition, because the black solid was made "
                     "by heating and heat is what a decomposition needs",
             "correct": False,
             "why": "Heating is how it was done rather than what it is. A "
                    "decomposition LOSES mass"},
            {"text": "Oxidation",
             "correct": True},
            {"text": "Combustion",
             "correct": False,
             "why": "It is an oxidation and there is no flame. Combustion is "
                    "the burning kind"},
            {"text": "Displacement",
             "correct": False,
             "why": "There is no second metal's compound for the copper to "
                    "take anything from"},
        ],
        "figure": None,
    },
    {
        "id": "c5-05-s07",
        "band": "standard",
        "text": "Sodium hydrogencarbonate is heated and gives a solid, a gas "
                "and some water vapour. Which type?",
        "options": [
            {"text": "Oxidation, because the oxygen in the carbonate joins "
                     "the sodium as the tube is heated",
             "correct": False,
             "why": "Nothing gains oxygen from outside. One compound has "
                    "broken into several"},
            {"text": "Synthesis",
             "correct": False,
             "why": "That is several in and one out. This is one in and "
                    "several out"},
            {"text": "Thermal decomposition",
             "correct": True},
            {"text": "Combustion",
             "correct": False,
             "why": "Nothing burns and no oxygen is needed. It works in a "
                    "tube with no air"},
        ],
        "figure": None,
    },
    {
        "id": "c5-05-s08",
        "band": "standard",
        "text": "Zinc is dropped into copper sulfate and the tube gets warm. "
                "Name the type and say what the warmth tells you.",
        "options": [
            {"text": "Displacement, and the warmth shows the reaction needs "
                     "heat to run, which is why a cold tube reacts so much "
                     "more slowly than a warm one",
             "correct": False,
             "why": "The warmth is produced BY the reaction. Nothing was "
                    "heated"},
            {"text": "Oxidation, and it is exothermic",
             "correct": False,
             "why": "Right about the energy and wrong about the type. No "
                    "oxygen is involved"},
            {"text": "Thermal decomposition, and it is endothermic",
             "correct": False,
             "why": "Two reactants rules out a decomposition, and the tube is "
                    "getting warmer rather than cooler"},
            {"text": "Displacement, and it is exothermic",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c5-05-s09",
        "band": "standard",
        "text": "Which pair of types are both exothermic?",
        "options": [
            {"text": "Combustion and displacement",
             "correct": True},
            {"text": "Combustion and thermal decomposition",
             "correct": False,
             "why": "Decomposition is the endothermic one. It stops when the "
                    "flame comes off"},
            {"text": "Displacement and thermal decomposition",
             "correct": False,
             "why": "Displacement gives energy out and decomposition takes it "
                    "in, so the pair is split"},
            {"text": "All four of them, because every chemical reaction "
                     "releases energy as its new joins are made",
             "correct": False,
             "why": "New joins do give energy back, and breaking the old ones "
                    "costs energy. When the cost is larger the reaction is "
                    "endothermic"},
        ],
        "figure": None,
    },
    {
        "id": "c5-05-s10",
        "band": "standard",
        "text": "A reaction has two reactants, one of them oxygen, and no "
                "flame at any point. Which name fits?",
        "options": [
            {"text": "Combustion, because oxygen is a reactant and that is "
                     "what combustion means",
             "correct": False,
             "why": "Combustion is oxidation fast enough to BURN. No flame "
                    "means the more general name"},
            {"text": "Oxidation, but not combustion",
             "correct": True},
            {"text": "Neither, because oxidation always burns",
             "correct": False,
             "why": "Rusting is an oxidation and takes years without a "
                    "flame"},
            {"text": "Thermal decomposition",
             "correct": False,
             "why": "Two reactants rules that out at once"},
        ],
        "figure": None,
    },
    {
        "id": "c5-05-s11",
        "band": "standard",
        "text": "You are told only that a reaction is exothermic. How much "
                "does that narrow down its type?",
        "options": [
            {"text": "Completely — only combustion gives out energy",
             "correct": False,
             "why": "Displacement and rusting are exothermic too, and neither "
                    "burns"},
            {"text": "Not at all, because every reaction is exothermic",
             "correct": False,
             "why": "Thermal decomposition is not, which is why the word "
                    "narrows anything at all"},
            {"text": "A little — it rules out thermal decomposition and "
                     "leaves several possibilities",
             "correct": True},
            {"text": "Completely — it must be a displacement",
             "correct": False,
             "why": "Combustion and oxidation are exothermic as well. One "
                    "word cannot pick between them"},
        ],
        "figure": None,
    },

    # ── harder · MRB-335 top-up ─────────────────────────────────────────
    {
        "id": "c5-05-h05",
        "band": "harder",
        "text": "Rusting is an oxidation and is never called a combustion. "
                "What is the one feature that separates them?",
        "options": [
            {"text": "Whether oxygen is one of the reactants, since rusting "
                     "takes its oxygen out of the water rather than out of "
                     "the air around the nail",
             "correct": False,
             "why": "Rusting needs oxygen from the air as well as water. Both "
                    "have oxygen as a reactant"},
            {"text": "Whether oxygen is one of the reactants, since rusting "
                     "uses water",
             "correct": True},
            {"text": "Whether a metal is involved",
             "correct": False,
             "why": "Magnesium is a metal and burns. The metal is not what "
                    "decides it"},
            {"text": "Whether the product is heavier",
             "correct": False,
             "why": "Both products are heavier, because both gained oxygen"},
        ],
        "figure": None,
    },
    {
        "id": "c5-05-h06",
        "band": "harder",
        "text": "A reaction gives out energy, and its two reactants are a "
                "metal and a compound of a different metal. Name it, and say "
                "what you would see.",
        "options": [
            {"text": "Displacement, and both metals end up dissolved in the "
                     "solution together, which is why it changes colour as "
                     "the reaction runs",
             "correct": False,
             "why": "One goes IN to solution and one comes OUT of it. Only "
                    "one is dissolved at the end"},
            {"text": "Synthesis, and one new compound is formed",
             "correct": False,
             "why": "Two compounds exist at the end — the new sulfate, and "
                    "the metal that came out. Nothing joined into one"},
            {"text": "Displacement, and the less reactive metal appears as a "
                     "solid",
             "correct": True},
            {"text": "Oxidation, and a gas is given off",
             "correct": False,
             "why": "No oxygen is involved and no gas appears"},
        ],
        "figure": None,
    },
    {
        "id": "c5-05-h07",
        "band": "harder",
        "text": "Why does knowing a reaction is a COMBUSTION let you predict "
                "its products without being told them?",
        "options": [
            {"text": "Because every combustion gives the same two products "
                     "whatever the fuel, so the products can be written down "
                     "before anyone says what is burning",
             "correct": False,
             "why": "Burning hydrogen gives water only, and burning sulfur "
                    "gives sulfur dioxide. You need to know what is in the "
                    "fuel"},
            {"text": "Because combustion always releases the same amount of "
                     "energy",
             "correct": False,
             "why": "Different fuels release very different amounts. The "
                    "prediction is about the products"},
            {"text": "Because the products of a combustion are always gases",
             "correct": False,
             "why": "Magnesium burns to a solid oxide. The rule is about "
                    "where the carbon and hydrogen go"},
            {"text": "Because a fuel of carbon and hydrogen, with enough "
                     "oxygen, always gives carbon dioxide and water",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c5-05-h08",
        "band": "harder",
        "text": "A student is told a reaction is endothermic and concludes it "
                "must be a thermal decomposition. What is wrong with that?",
        "options": [
            {"text": "Exothermic and endothermic cut across the four types, "
                     "so other endothermic reactions exist as well",
             "correct": True},
            {"text": "Nothing — thermal decomposition is the only endothermic "
                     "reaction",
             "correct": False,
             "why": "It is the only endothermic one among the FOUR. Chemistry "
                    "has many others"},
            {"text": "Thermal decomposition is exothermic",
             "correct": False,
             "why": "It takes energy in, which is why it stops when the flame "
                    "comes off"},
            {"text": "Endothermic means the same as decomposition",
             "correct": False,
             "why": "One describes the energy and the other the shape of the "
                    "reaction. They are two different cuts"},
        ],
        "figure": None,
    },
    {
        "id": "c5-05-h09",
        "band": "harder",
        "text": "Marble chips fizz in acid. A student calls it a thermal "
                "decomposition because a gas came off. Where does that go "
                "wrong?",
        "options": [
            {"text": "It names the reaction from what came out, and the gas "
                     "is not carbon dioxide but hydrogen, so even that "
                     "observation has been misread",
             "correct": False,
             "why": "The gas IS carbon dioxide and turns limewater milky. The "
                    "error is in the reasoning rather than the observation"},
            {"text": "It names the reaction from what came OUT, and there are "
                     "two reactants going in",
             "correct": True},
            {"text": "Nothing is wrong — a gas coming off is what a "
                     "decomposition looks like",
             "correct": False,
             "why": "It is one thing a decomposition looks like. Plenty of "
                    "other reactions give off gases too"},
            {"text": "The reaction needed no heating, and every reaction "
                     "needs heat",
             "correct": False,
             "why": "The lack of heating is a real clue, and plenty of "
                    "reactions run cold. The decisive point is the two "
                    "reactants"},
        ],
        "figure": None,
    },
    {
        "id": "c5-05-h10",
        "band": "harder",
        "text": "The lesson says none of these classifications is a fact "
                "about nature. What are they for, then?",
        "options": [
            {"text": "For making chemistry easier to teach, by giving four "
                     "boxes to sort into",
             "correct": False,
             "why": "Teaching convenience is not the test. The test is "
                    "whether the name lets you say what will happen next"},
            {"text": "For deciding which reactions are allowed to happen",
             "correct": False,
             "why": "Nature is not consulting the classification. The names "
                    "describe rather than permit"},
            {"text": "For grouping reactions so that a prediction becomes "
                     "possible — a name that predicts nothing would not be "
                     "worth learning",
             "correct": True},
            {"text": "For nothing much — they are only labels",
             "correct": False,
             "why": "A label that lets you predict the products of a reaction "
                    "you have never seen is worth a great deal"},
        ],
        "figure": None,
    },
]
