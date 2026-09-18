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
    # ── easier · MRB-338 top-up ─────────────────────────────────────────
    {
        "id": "c5-05-e11",
        "band": "easier",
        "text": "Ethanol burns in a spirit burner with a clean blue flame "
                "until the fuel in it has all gone. Which type is it?",
        "options": [
            {"text": "Combustion, because a fuel is reacting with oxygen",
             "correct": True},
            {"text": "Thermal decomposition, because the ethanol is broken "
                     "apart",
             "correct": False,
             "why": "Two reactants go in here, ethanol and oxygen. A "
                    "decomposition starts with one substance"},
            {"text": "Displacement, because the flame takes the fuel's place",
             "correct": False,
             "why": "Displacement is one metal taking another metal's place in "
                    "a compound. A flame is not a reactant"},
            {"text": "None of the four, because a burner is equipment rather "
                     "than chemistry",
             "correct": False,
             "why": "What the fuel is burned in changes nothing. The reactants "
                    "are ethanol and oxygen"},
        ],
        "figure": None,
    },
    {
        "id": "c5-05-e12",
        "band": "easier",
        "text": "Silver oxide is heated in a tube. Silver metal is left behind "
                "and a gas comes off. Which type is it?",
        "options": [
            {"text": "Oxidation, because the silver gains oxygen while the "
                     "tube is hot",
             "correct": False,
             "why": "The silver is LOSING oxygen here. The oxygen started "
                    "inside the compound and has come off as gas"},
            {"text": "Displacement, because the gas pushes the silver out of "
                     "the compound",
             "correct": False,
             "why": "Displacement needs a metal and a different metal's "
                    "compound going in. Only one substance was in the tube"},
            {"text": "Thermal decomposition, because one substance has been "
                     "broken apart by heat",
             "correct": True},
            {"text": "Combustion, because heating something until it changes "
                     "is burning",
             "correct": False,
             "why": "Combustion needs oxygen as a reactant and a flame. "
                    "Heating is how this was done, not what it is"},
        ],
        "figure": None,
    },
    {
        "id": "c5-05-e13",
        "band": "easier",
        "text": "Aluminium foil is left in copper chloride solution. The foil "
                "pits and thins, and orange-brown specks gather at the bottom "
                "of the beaker. Which type is it?",
        "options": [
            {"text": "Oxidation, because the aluminium takes oxygen out of the "
                     "liquid",
             "correct": False,
             "why": "No oxygen is a reactant. The aluminium is taking the "
                    "copper's place, not its oxygen"},
            {"text": "Displacement, because a more reactive metal takes "
                     "copper's place",
             "correct": True},
            {"text": "Thermal decomposition, because the copper chloride "
                     "splits into two",
             "correct": False,
             "why": "Nothing was heated and two reactants went in. A "
                    "decomposition begins with one"},
            {"text": "Combustion, because the specks are what is left after "
                     "burning",
             "correct": False,
             "why": "Nothing burns in a cold beaker, and no oxygen is "
                    "involved"},
        ],
        "figure": None,
    },
    {
        "id": "c5-05-e14",
        "band": "easier",
        "text": "A hand-warmer packet holds iron powder that slowly joins with "
                "oxygen from the air, and the packet gets warm. Which type is "
                "it?",
        "options": [
            {"text": "Combustion, because the packet gives out heat the way a "
                     "fire does",
             "correct": False,
             "why": "Giving out heat is not what names it. Combustion burns "
                    "with a flame, and nothing here is alight"},
            {"text": "Thermal decomposition, because the iron powder is broken "
                     "down by the warmth",
             "correct": False,
             "why": "Nothing is broken down, and the warmth is produced rather "
                    "than supplied"},
            {"text": "Displacement, because the oxygen takes the place of the "
                     "air in the packet",
             "correct": False,
             "why": "Displacement is a metal taking a metal's place in a "
                    "compound, not air being pushed aside"},
            {"text": "Oxidation, because iron is gaining oxygen with no flame",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c5-05-e15",
        "band": "easier",
        "text": "In a word equation, which side are the reactants written on?",
        "options": [
            {"text": "The right, because that is the side a reaction runs "
                     "towards",
             "correct": False,
             "why": "The right is where the products go. Reactants are what "
                    "you start with"},
            {"text": "Either side, as long as they are all written down",
             "correct": False,
             "why": "The sides have fixed meanings. Swapping them would say "
                    "the reaction ran the other way"},
            {"text": "Neither, because reactants are not written in a word "
                     "equation",
             "correct": False,
             "why": "They are the first thing written, and counting them is "
                    "what names the reaction"},
            {"text": "The left",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c5-05-e16",
        "band": "easier",
        "text": "What is neutralisation?",
        "options": [
            {"text": "A reaction that leaves neither a solid nor a gas behind",
             "correct": False,
             "why": "Marble in acid gives off a gas and is still a "
                    "neutralisation. What went in is what names it"},
            {"text": "A reaction that gives out no energy in either direction",
             "correct": False,
             "why": "Neutralisation gives out heat. Energy is a separate cut "
                    "across the types"},
            {"text": "An acid reacting with a base, a carbonate included",
             "correct": True},
            {"text": "A metal taking the place of another metal in its "
                     "compound",
             "correct": False,
             "why": "That is displacement, and it is one of the four. "
                    "Neutralisation is not"},
        ],
        "figure": None,
    },
    {
        "id": "c5-05-e17",
        "band": "easier",
        "text": "A jet of hydrogen is lit at the mouth of a jar of oxygen. It "
                "burns with a pale flame and the only product is water. Which "
                "type is it?",
        "options": [
            {"text": "Thermal decomposition",
             "correct": False,
             "why": "Two reactants went in, hydrogen and oxygen. A "
                    "decomposition begins with one substance"},
            {"text": "Combustion",
             "correct": True},
            {"text": "Displacement",
             "correct": False,
             "why": "No metal and no metal compound are involved, so there is "
                    "nothing to displace"},
            {"text": "None of the four",
             "correct": False,
             "why": "A fuel and oxygen, with a flame and energy out, is "
                    "exactly what combustion names"},
        ],
        "figure": None,
    },
    {
        "id": "c5-05-e18",
        "band": "easier",
        "text": "Sulfur is burned in a gas jar of oxygen with a bright blue "
                "flame. Which type is it?",
        "options": [
            {"text": "Thermal decomposition, because the sulfur is broken "
                     "apart by the heat",
             "correct": False,
             "why": "Sulfur and oxygen both go in, so there are two reactants. "
                    "A decomposition has one"},
            {"text": "Combustion, because a fuel and oxygen are reacting with "
                     "a flame",
             "correct": True},
            {"text": "Displacement, because the oxygen displaces the air in "
                     "the jar",
             "correct": False,
             "why": "Air being pushed out of a jar is not a chemical change at "
                    "all"},
            {"text": "None of the four, because sulfur is neither a metal nor "
                     "a fuel",
             "correct": False,
             "why": "Sulfur behaves as a fuel here: it burns in oxygen and "
                    "gives out energy"},
        ],
        "figure": None,
    },
    {
        "id": "c5-05-e19",
        "band": "easier",
        "text": "Nitrogen and hydrogen are combined in a reactor and ammonia "
                "is the only product. Which type is it?",
        "options": [
            {"text": "Synthesis, because two substances have joined into one "
                     "compound",
             "correct": True},
            {"text": "Thermal decomposition, because the reactor has to be "
                     "heated before anything happens",
             "correct": False,
             "why": "Heating is how it is done, not what it is. Two reactants "
                    "rule a decomposition out"},
            {"text": "Oxidation, because one gas is being joined to another",
             "correct": False,
             "why": "Oxidation is a gain of oxygen in particular, and there is "
                    "no oxygen here"},
            {"text": "Combustion, because the reaction gives out heat",
             "correct": False,
             "why": "Nothing burns and no oxygen is a reactant. Heat out does "
                    "not make a reaction a combustion"},
        ],
        "figure": None,
    },
    {
        "id": "c5-05-e20",
        "band": "easier",
        "text": "A reaction's word equation has three substances written on "
                "the left. Which of the four types does that rule out at "
                "once?",
        "options": [
            {"text": "Oxidation, because an oxidation has exactly two "
                     "reactants",
             "correct": False,
             "why": "Rusting is written with three on the left — iron, water "
                    "and oxygen — and is an oxidation"},
            {"text": "Displacement, because its equation holds a metal on each "
                     "side and nothing else",
             "correct": False,
             "why": "A displacement equation carries the compound's partner "
                    "too. Counting to three does not rule it out"},
            {"text": "Thermal decomposition, which has one reactant and no "
                     "more",
             "correct": True},
            {"text": "None of them, because the number of reactants tells you "
                     "nothing",
             "correct": False,
             "why": "It is the first thing the decision rule asks, and one "
                    "reactant settles the answer"},
        ],
        "figure": None,
    },
    {
        "id": "c5-05-e21",
        "band": "easier",
        "text": "Zinc is left in colourless silver nitrate solution and grey "
                "needles grow on it. Which type is it?",
        "options": [
            {"text": "Oxidation, because the grey needles are an oxide of zinc",
             "correct": False,
             "why": "No oxygen is involved. The needles are silver metal that "
                    "has come out of the solution"},
            {"text": "Displacement, because zinc is taking the silver's place",
             "correct": True},
            {"text": "Thermal decomposition, because the nitrate is broken "
                     "into parts",
             "correct": False,
             "why": "Nothing was heated and two reactants went in. A "
                    "decomposition starts from one"},
            {"text": "None of the four, because no colour change was seen at "
                     "the start",
             "correct": False,
             "why": "A metal and a compound of a different metal is exactly "
                    "displacement, colour or no colour"},
        ],
        "figure": None,
    },
    {
        "id": "c5-05-e22",
        "band": "easier",
        "text": "Which of these is NOT one of the four reaction types in this "
                "unit?",
        "options": [
            {"text": "Displacement",
             "correct": False,
             "why": "Displacement is one of the four: a metal and a compound "
                    "of another metal"},
            {"text": "Thermal decomposition",
             "correct": False,
             "why": "Thermal decomposition is one of the four, and the only "
                    "one with a single reactant"},
            {"text": "Oxidation",
             "correct": False,
             "why": "Oxidation is one of the four, and combustion sits inside "
                    "it"},
            {"text": "Neutralisation",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c5-05-e23",
        "band": "easier",
        "text": "A solid is heated in an open dish and what is left weighs "
                "more than what went in. What does the mass tie-breaker say "
                "has happened?",
        "options": [
            {"text": "Oxygen from the air has joined it, so it is an oxidation",
             "correct": True},
            {"text": "A gas has escaped from it, so it is a thermal "
                     "decomposition",
             "correct": False,
             "why": "Letting a gas go makes what is left lighter. This dish "
                    "got heavier"},
            {"text": "Nothing joined or left, so the extra mass came from the "
                     "heat",
             "correct": False,
             "why": "Heat has no mass. Something material has been added"},
            {"text": "A metal has been displaced into it, so it is a "
                     "displacement",
             "correct": False,
             "why": "Nothing went into the dish but heat and the air. "
                    "Displacement needs a metal compound as a reactant"},
        ],
        "figure": None,
    },
    {
        "id": "c5-05-e24",
        "band": "easier",
        "text": "Table salt is stirred into water until it disappears. Which "
                "of the four types names what happened?",
        "options": [
            {"text": "Thermal decomposition, because the salt has been broken "
                     "apart",
             "correct": False,
             "why": "The salt is still salt, spread through the water. "
                    "Evaporate the water and it comes back"},
            {"text": "Displacement, because the water takes the place of the "
                     "salt",
             "correct": False,
             "why": "Nothing takes a place in a compound here, and no metal is "
                    "pushed out"},
            {"text": "None of them, because nothing new was made at all",
             "correct": True},
            {"text": "Oxidation, because water contains oxygen",
             "correct": False,
             "why": "Oxygen has to be a reactant that joins on. Dissolving "
                    "joins nothing"},
        ],
        "figure": None,
    },
    {
        "id": "c5-05-e25",
        "band": "easier",
        "text": "Which type is named by this pair of reactants: a metal, and a "
                "compound containing a different metal?",
        "options": [
            {"text": "Oxidation",
             "correct": False,
             "why": "Oxidation needs oxygen itself as one of the reactants"},
            {"text": "Displacement",
             "correct": True},
            {"text": "Combustion",
             "correct": False,
             "why": "Combustion needs a fuel and oxygen, and it burns with a "
                    "flame"},
            {"text": "Synthesis",
             "correct": False,
             "why": "Synthesis ends with one compound. This pair leaves two "
                    "substances"},
        ],
        "figure": None,
    },
    {
        "id": "c5-05-e26",
        "band": "easier",
        "text": "Black copper oxide is heated with carbon powder and "
                "orange-brown copper appears. Which type is it?",
        "options": [
            {"text": "Thermal decomposition, because heating the black powder "
                     "broke it up",
             "correct": False,
             "why": "Two reactants were mixed before the heating. A "
                    "decomposition begins with one substance"},
            {"text": "Combustion, because the carbon is burning in the tube",
             "correct": False,
             "why": "No oxygen gas goes in and there is no flame. The oxygen "
                    "here is locked inside the copper oxide"},
            {"text": "Oxidation, because the copper is gaining oxygen",
             "correct": False,
             "why": "The copper is losing its oxygen. It is the carbon that "
                    "gains it"},
            {"text": "Displacement, because the carbon has taken the copper's "
                     "oxygen",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c5-05-e27",
        "band": "easier",
        "text": "Zinc carbonate is heated in a tube and gives a solid and a "
                "gas that turns limewater milky. Which type is it?",
        "options": [
            {"text": "Thermal decomposition",
             "correct": True},
            {"text": "Combustion",
             "correct": False,
             "why": "Nothing burns and no oxygen goes in. The heat is supplied "
                    "rather than produced"},
            {"text": "Displacement",
             "correct": False,
             "why": "Only one substance was in the tube, and no metal was "
                    "added to it"},
            {"text": "Oxidation",
             "correct": False,
             "why": "Nothing gains oxygen. The carbonate is losing a gas that "
                    "contains it"},
        ],
        "figure": None,
    },
    {
        "id": "c5-05-e28",
        "band": "easier",
        "text": "A sparkler burns with orange sparks as the iron filings in it "
                "react with oxygen from the air. Which type is it?",
        "options": [
            {"text": "Thermal decomposition, because the sparkler breaks down "
                     "as it burns",
             "correct": False,
             "why": "Two reactants go in, the iron and the oxygen. Nothing "
                    "starts as a single substance"},
            {"text": "Displacement, because the oxygen displaces the iron from "
                     "the stick",
             "correct": False,
             "why": "Being held on a stick is not being in a compound. Nothing "
                    "is displaced"},
            {"text": "Combustion, because iron is reacting with oxygen and "
                     "burning",
             "correct": True},
            {"text": "None of the four, because a firework is a mixture rather "
                     "than a substance",
             "correct": False,
             "why": "A mixture reacts perfectly well. Iron and oxygen are the "
                    "reactants here"},
        ],
        "figure": None,
    },
    {
        "id": "c5-05-e29",
        "band": "easier",
        "text": "A synthesis joins two or more substances together. How many "
                "products does it leave?",
        "options": [
            {"text": "Two",
             "correct": False,
             "why": "Two or more go in. One compound comes out"},
            {"text": "One",
             "correct": True},
            {"text": "Three",
             "correct": False,
             "why": "However many substances join, they join into a single "
                    "compound"},
            {"text": "It depends how many substances joined",
             "correct": False,
             "why": "It does not. Three reactants joining still leave one "
                    "product"},
        ],
        "figure": None,
    },
    {
        "id": "c5-05-e30",
        "band": "easier",
        "text": "Sherbet holds citric acid and a hydrogencarbonate. On the "
                "tongue it fizzes and feels cold. Which of the four types is "
                "it?",
        "options": [
            {"text": "Thermal decomposition, because the cold shows energy is "
                     "being taken in",
             "correct": False,
             "why": "Energy taken in does not name a type, and two reactants "
                    "rule a decomposition out"},
            {"text": "Combustion, because a fizz is a gas coming off quickly",
             "correct": False,
             "why": "Nothing burns and no oxygen is a reactant. A gas coming "
                    "off names nothing on its own"},
            {"text": "Displacement, because the acid takes the "
                     "hydrogencarbonate's place",
             "correct": False,
             "why": "Displacement needs a metal and a compound of another "
                    "metal. An acid is not a metal"},
            {"text": "None of them, because an acid reacting with a carbonate "
                     "is outside the four",
             "correct": True},
        ],
        "figure": None,
    },

    # ── standard · MRB-338 top-up ───────────────────────────────────────
    {
        "id": "c5-05-s12",
        "band": "standard",
        "text": "A tube holds one green solid. It is heated, a gas comes off "
                "and the tube gets lighter. Which observation settles the "
                "type, and what is the type?",
        "options": [
            {"text": "The gas coming off settles it, and what it names is a "
                     "thermal decomposition",
             "correct": False,
             "why": "Right name, wrong evidence. Marble in acid gives off a "
                    "gas and is not a decomposition"},
            {"text": "The single reactant settles it, and it is a thermal "
                     "decomposition",
             "correct": True},
            {"text": "The mass the tube has lost settles it, and what it names "
                     "is a combustion",
             "correct": False,
             "why": "A combustion needs oxygen going in, and only one "
                    "substance was in the tube"},
            {"text": "The colour settles it, and it is an oxidation",
             "correct": False,
             "why": "Colour names nothing, and an oxidation gains mass rather "
                    "than losing it"},
        ],
        "figure": None,
    },
    {
        "id": "c5-05-s13",
        "band": "standard",
        "text": "Hydrogen burns in oxygen and water is the only product. One "
                "student calls it a combustion and another calls it a "
                "synthesis. Which is right?",
        "options": [
            {"text": "Only combustion, because a synthesis is something done "
                     "in a flask and never in a flame",
             "correct": False,
             "why": "Nothing about synthesis forbids a flame. It is about "
                    "substances joining into one"},
            {"text": "Only synthesis, because a combustion has to produce "
                     "carbon dioxide",
             "correct": False,
             "why": "The carbon dioxide comes from carbon in the fuel, and "
                    "hydrogen has none. It still burns"},
            {"text": "Both: two substances have joined into one, and the "
                     "joining burned in oxygen",
             "correct": True},
            {"text": "Neither, because a reaction with one product has no type",
             "correct": False,
             "why": "One product is perfectly normal. Every reaction can be "
                    "named from what went in"},
        ],
        "figure": None,
    },
    {
        "id": "c5-05-s14",
        "band": "standard",
        "text": "Hydrochloric acid is added to sodium hydroxide solution. The "
                "mixture warms, nothing burns, no metal is present and no gas "
                "comes off. Which of the four is it?",
        "options": [
            {"text": "None of them, because no member of the four names an "
                     "acid and an alkali reacting",
             "correct": True},
            {"text": "Oxidation, because warmth is the sign that oxygen from "
                     "the air has joined on to something",
             "correct": False,
             "why": "Warmth is not evidence of oxygen, and no oxygen goes in "
                    "here at all"},
            {"text": "Displacement, because the sodium in the alkali takes the "
                     "hydrogen's place inside the acid",
             "correct": False,
             "why": "Displacement needs a metal as a reactant. The sodium here "
                    "is already inside a compound"},
            {"text": "Combustion, because energy is being given out",
             "correct": False,
             "why": "Combustion needs a fuel, oxygen and a flame. Energy out "
                    "is not enough on its own"},
        ],
        "figure": None,
    },
    {
        "id": "c5-05-s15",
        "band": "standard",
        "text": "In a leaf, water and the carbon dioxide in the air are turned "
                "into glucose, with oxygen given off, using light energy. "
                "Which of the four types is that?",
        "options": [
            {"text": "Oxidation, because oxygen is one of the substances "
                     "involved",
             "correct": False,
             "why": "Oxidation means gaining oxygen as a reactant. Here the "
                    "oxygen is a product"},
            {"text": "Thermal decomposition, because the water is broken apart",
             "correct": False,
             "why": "Two reactants go in and nothing is heated. Light is not "
                    "heat"},
            {"text": "Combustion, because it is respiration backwards and "
                     "respiration is a kind of burning",
             "correct": False,
             "why": "Running a reaction backwards does not keep its name, and "
                    "nothing burns in a leaf"},
            {"text": "None of them, because nothing gains oxygen, breaks apart "
                     "on heating or displaces a metal",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c5-05-s16",
        "band": "standard",
        "text": "A reaction runs to completion inside a sealed jar holding no "
                "air at all. Which of the four types can it NOT be?",
        "options": [
            {"text": "Thermal decomposition, because heating needs air around "
                     "the tube",
             "correct": False,
             "why": "A decomposition works with no air at all; the heat "
                    "travels through the glass"},
            {"text": "Combustion or oxidation, because both need oxygen as a "
                     "reactant",
             "correct": True},
            {"text": "Displacement, because a metal cannot react without air",
             "correct": False,
             "why": "Displacement needs a metal and a metal compound, and "
                    "neither of them is air"},
            {"text": "None of them can be ruled out, because air is not a "
                     "reactant in any reaction",
             "correct": False,
             "why": "Oxygen from the air is the reactant in every oxidation, "
                    "burning included"},
        ],
        "figure": None,
    },
    {
        "id": "c5-05-s17",
        "band": "standard",
        "text": "Three reactions are described by their reactants only: one "
                "heats a single substance, one has a metal and a different "
                "metal's compound, one has a fuel and oxygen with a flame. "
                "Name them in that order.",
        "options": [
            {"text": "Thermal decomposition, displacement, combustion",
             "correct": True},
            {"text": "Thermal decomposition, combustion, displacement",
             "correct": False,
             "why": "The metal with a metal compound is the displacement, and "
                    "it is the second one described"},
            {"text": "Displacement, thermal decomposition, combustion",
             "correct": False,
             "why": "The single substance heated is the decomposition, and it "
                    "is described first"},
            {"text": "Combustion, displacement, thermal decomposition",
             "correct": False,
             "why": "The fuel and oxygen with a flame is the combustion, and "
                    "it is described last"},
        ],
        "figure": None,
    },
    {
        "id": "c5-05-s18",
        "band": "standard",
        "text": "Two students both name a reaction as an oxidation. One's "
                "evidence is that there was a flame; the other's is that the "
                "product weighed more than the substance did. Whose evidence "
                "settles it?",
        "options": [
            {"text": "The flame, because only a reaction with oxygen can "
                     "produce one",
             "correct": False,
             "why": "A displacement can reach 2500 °C with no oxygen gas going "
                    "in. A flame shows heat, not what joined"},
            {"text": "Neither, because a type can only be settled from the "
                     "products",
             "correct": False,
             "why": "The reactants settle it, and knowing that oxygen joined "
                    "is exactly what names an oxidation"},
            {"text": "The mass gain, because it shows that oxygen has joined "
                     "on",
             "correct": True},
            {"text": "Both equally, because a flame and a mass gain always go "
                     "together",
             "correct": False,
             "why": "Rusting gains mass with no flame anywhere. The two do not "
                    "travel together"},
        ],
        "figure": None,
    },
    {
        "id": "c5-05-s19",
        "band": "standard",
        "text": "Carbon dioxide comes off when ethanol burns, when zinc "
                "carbonate is heated and when marble meets acid. What does "
                "that show about using a gas test to name a type?",
        "options": [
            {"text": "That the gas cannot name the type, because the same gas "
                     "comes out of different reactions",
             "correct": True},
            {"text": "That all three must really be the same type of reaction "
                     "underneath, whatever their reactants look like",
             "correct": False,
             "why": "One is a combustion, one a decomposition, and one is "
                    "outside the four altogether"},
            {"text": "That the test for carbon dioxide is unreliable and ought "
                     "not to be trusted with naming anything",
             "correct": False,
             "why": "The test for carbon dioxide is reliable. What it cannot "
                    "do is name the reaction"},
            {"text": "That only the reaction giving off the most gas of the "
                     "three can safely be given a name from it",
             "correct": False,
             "why": "How much gas comes off names nothing. The reactants do"},
        ],
        "figure": None,
    },
    {
        "id": "c5-05-s20",
        "band": "standard",
        "text": "Zinc added to copper sulfate reacts; copper added to zinc "
                "sulfate does nothing at all. Does the tube where nothing "
                "happened have a type?",
        "options": [
            {"text": "Yes, it is a displacement that stopped before anything "
                     "showed, because one of its reactants had run out",
             "correct": False,
             "why": "Neither reactant ran out. The reaction had no way to run "
                    "in that direction"},
            {"text": "Yes, it is an oxidation that has not had long enough to "
                     "show itself",
             "correct": False,
             "why": "No oxygen is involved and nothing has happened. Waiting "
                    "longer changes nothing"},
            {"text": "No, and the tube should be written off as a failed "
                     "experiment and set up again with fresh solution",
             "correct": False,
             "why": "A negative result is evidence. It puts copper below zinc"},
            {"text": "No: with no reaction there is nothing to name, though "
                     "the result still tells you the order",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c5-05-s21",
        "band": "standard",
        "text": "Water is added to calcium oxide. It hisses, gets hot, and "
                "calcium hydroxide is the only product. Which type is it?",
        "options": [
            {"text": "Synthesis, because two substances have made a single "
                     "compound",
             "correct": True},
            {"text": "Thermal decomposition, because the heat shows something "
                     "breaking apart",
             "correct": False,
             "why": "The heat is given out rather than supplied, and two "
                    "reactants went in"},
            {"text": "Oxidation, because the calcium oxide has oxygen in it "
                     "already",
             "correct": False,
             "why": "Oxygen already inside a compound is not oxygen joining on "
                    "as a reactant"},
            {"text": "Displacement, because the water takes the place of the "
                     "oxygen",
             "correct": False,
             "why": "Displacement needs a metal and a compound of a different "
                    "metal. Water is neither"},
        ],
        "figure": None,
    },
    {
        "id": "c5-05-s22",
        "band": "standard",
        "text": "Of these three — sulfur burning in oxygen, zinc carbonate "
                "heated, and zinc put into copper sulfate — which can "
                "correctly be given TWO of the four names?",
        "options": [
            {"text": "Zinc carbonate heated, which is a decomposition and an "
                     "oxidation",
             "correct": False,
             "why": "Nothing gains oxygen when a carbonate decomposes, so only "
                    "one name fits"},
            {"text": "Zinc in copper sulfate, which is a displacement and a "
                     "combustion",
             "correct": False,
             "why": "Nothing burns and no oxygen goes in, so combustion is "
                    "ruled out"},
            {"text": "Sulfur burning, which is a combustion and an oxidation",
             "correct": True},
            {"text": "None of them, because each reaction has exactly one "
                     "name",
             "correct": False,
             "why": "Combustion sits inside oxidation, so anything burning in "
                    "oxygen carries both names"},
        ],
        "figure": None,
    },
    {
        "id": "c5-05-s23",
        "band": "standard",
        "text": "A student names a reaction as a displacement because a solid "
                "appeared. Why is that not enough?",
        "options": [
            {"text": "Because a displacement leaves both of its products "
                     "dissolved and never leaves a solid behind",
             "correct": False,
             "why": "It usually does — the less reactive metal comes out as a "
                    "solid. That is not the objection"},
            {"text": "Because solids appear in other types too; a displacement "
                     "is named by its reactants",
             "correct": True},
            {"text": "Because a solid only counts as evidence of a reaction "
                     "when it comes out with a colour",
             "correct": False,
             "why": "A white solid is evidence of a new substance just as much "
                    "as a coloured one"},
            {"text": "Because a solid appearing always means a synthesis "
                     "instead",
             "correct": False,
             "why": "A synthesis can leave a solid, and so can an oxidation. "
                    "No product names a type by itself"},
        ],
        "figure": None,
    },
    {
        "id": "c5-05-s24",
        "band": "standard",
        "text": "Explain why a reaction with exactly one reactant can never "
                "also be called an oxidation.",
        "options": [
            {"text": "Because an oxidation has to produce a gas, and a "
                     "reaction with one reactant has nothing to make one from",
             "correct": False,
             "why": "An oxidation often produces a solid oxide and no gas at "
                    "all"},
            {"text": "Because oxidation is a slower process than decomposition "
                     "ever is",
             "correct": False,
             "why": "Speed does not decide it. Burning is an oxidation and is "
                    "over in seconds"},
            {"text": "Because one reactant means the reaction gives out no "
                     "energy",
             "correct": False,
             "why": "Energy does not decide it either, and a decomposition "
                    "takes energy in"},
            {"text": "Because an oxidation needs oxygen as a second reactant, "
                     "and there is no second reactant",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c5-05-s25",
        "band": "standard",
        "text": "Magnesium is heated in a jar of nitrogen, with no oxygen "
                "present, and a pale yellow solid forms. Which type is it?",
        "options": [
            {"text": "Oxidation, because the magnesium is burning",
             "correct": False,
             "why": "Burning in nitrogen adds no oxygen, and oxidation is a "
                    "gain of oxygen in particular"},
            {"text": "Synthesis, because two substances have joined into a "
                     "single compound",
             "correct": True},
            {"text": "Thermal decomposition, because the magnesium is heated "
                     "throughout",
             "correct": False,
             "why": "Heating is how it was started. Two reactants went in, so "
                    "a decomposition is out"},
            {"text": "Displacement, because the nitrogen takes the place of "
                     "the air",
             "correct": False,
             "why": "Air being pushed out of a jar is not a chemical change. "
                    "Displacement swaps metals inside a compound"},
        ],
        "figure": None,
    },
    {
        "id": "c5-05-s26",
        "band": "standard",
        "text": "One reaction stops the moment the Bunsen is taken away; "
                "another keeps going once it has been lit. Which two types are "
                "those most likely to be?",
        "options": [
            {"text": "A combustion and a displacement, since both give out "
                     "energy",
             "correct": False,
             "why": "One of the two described stops when the heat stops, so "
                    "they cannot both be giving energy out"},
            {"text": "An oxidation and a decomposition, with the oxidation the "
                     "one that stops the moment the heat goes",
             "correct": False,
             "why": "It is the decomposition that stops. An oxidation gives "
                    "energy out"},
            {"text": "Two decompositions running at different speeds",
             "correct": False,
             "why": "A decomposition stops when the heating stops, so the "
                    "second one cannot be a decomposition"},
            {"text": "A thermal decomposition and a combustion: one takes "
                     "energy in, the other gives it out",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c5-05-s27",
        "band": "standard",
        "text": "A reaction's only products are water and carbon dioxide, and "
                "a student concludes it must be a combustion. Give the "
                "strongest objection.",
        "options": [
            {"text": "Carbon dioxide and water are not really the products of "
                     "burning at all",
             "correct": False,
             "why": "They are exactly what a hydrocarbon burned in plenty of "
                    "air produces"},
            {"text": "A combustion has to give out light as well, and none was "
                     "mentioned",
             "correct": False,
             "why": "Light is not the test. What is missing is any information "
                    "about the reactants"},
            {"text": "Heating baking soda gives the same two products from a "
                     "single reactant",
             "correct": True},
            {"text": "The products prove it, so there is no objection to be "
                     "made",
             "correct": False,
             "why": "Different types can share products. Only the reactants "
                    "settle the name"},
        ],
        "figure": None,
    },
    {
        "id": "c5-05-s28",
        "band": "standard",
        "text": "If you could ask only one question to tell a displacement "
                "from an oxidation, which would it be?",
        "options": [
            {"text": "Is the second reactant oxygen, or a compound of a "
                     "different metal?",
             "correct": True},
            {"text": "Did the reaction give out heat while it was running?",
             "correct": False,
             "why": "Both types usually do. The energy does not separate them"},
            {"text": "Did a solid appear by the end of the reaction?",
             "correct": False,
             "why": "A displacement leaves a solid metal and an oxidation "
                    "leaves a solid oxide"},
            {"text": "Did the mixture change colour while you watched it?",
             "correct": False,
             "why": "Both can change colour and both can fail to. Colour "
                    "separates nothing"},
        ],
        "figure": None,
    },
    {
        "id": "c5-05-s29",
        "band": "standard",
        "text": "You are given only the word equation X + oxygen makes X "
                "oxide, with no description. Which two of the four types could "
                "fit, and what would decide between them?",
        "options": [
            {"text": "Oxidation or displacement, decided by whether X is a "
                     "metal",
             "correct": False,
             "why": "Displacement needs a compound of another metal going in, "
                    "and there is none here"},
            {"text": "Oxidation or combustion, decided by whether it burned "
                     "with a flame",
             "correct": True},
            {"text": "Oxidation or thermal decomposition, decided by the mass "
                     "change",
             "correct": False,
             "why": "Two reactants rule a decomposition out whatever the mass "
                    "does"},
            {"text": "Only oxidation, because combustion needs a fuel and X is "
                     "not one",
             "correct": False,
             "why": "Anything burning in oxygen is behaving as a fuel. "
                    "Magnesium burns, and it is a metal"},
        ],
        "figure": None,
    },
    {
        "id": "c5-05-s30",
        "band": "standard",
        "text": "Explain why the decision rule counts the reactants before it "
                "asks anything else.",
        "options": [
            {"text": "Because reactants are written before products in an "
                     "equation",
             "correct": False,
             "why": "Where they are written is not the reason. It is that the "
                    "count decides between the types"},
            {"text": "Because the number of reactants tells you how much "
                     "energy comes out",
             "correct": False,
             "why": "The count says nothing about energy, which is a separate "
                    "cut across the types"},
            {"text": "Because one reactant settles the answer at once and "
                     "rules the other three out",
             "correct": True},
            {"text": "Because a reaction with more reactants is always harder "
                     "to name",
             "correct": False,
             "why": "Rusting has three reactants and is straightforward. The "
                    "count is a tool, not a difficulty rating"},
        ],
        "figure": None,
    },
    # ── harder · MRB-338 top-up ─────────────────────────────────────────
    {
        "id": "c5-05-h11",
        "band": "harder",
        "text": "Water is broken into hydrogen and oxygen by an electric "
                "current, with nothing heated at any stage. Which of the four "
                "types is it?",
        "options": [
            {"text": "Thermal decomposition, because one substance has become "
                     "two and that is the whole of the definition",
             "correct": False,
             "why": "The rule names heat as the thing that does it, and "
                    "nothing here was heated"},
            {"text": "Displacement, because the current pushes the hydrogen "
                     "out of the water and leaves the oxygen",
             "correct": False,
             "why": "A current is not a reactant and not a metal. Nothing "
                    "takes a metal's place"},
            {"text": "None of them: it is a decomposition, but the four name "
                     "only the kind that heat does",
             "correct": True},
            {"text": "Oxidation, because oxygen is one of the two substances "
                     "the current produces from the water",
             "correct": False,
             "why": "Oxygen produced is the opposite of oxygen joining on as a "
                    "reactant"},
        ],
        "figure": None,
    },
    {
        "id": "c5-05-h12",
        "band": "harder",
        "text": "Hydrogen peroxide poured onto a catalyst fizzes into water "
                "and oxygen, with nothing heated. A student calls it a thermal "
                "decomposition. Which single word is wrong?",
        "options": [
            {"text": "Thermal, because nothing was heated and the four name "
                     "only the heated kind",
             "correct": True},
            {"text": "Decomposition, because two products came out rather than "
                     "one",
             "correct": False,
             "why": "Decomposition is one substance becoming two or more. That "
                    "word is the right one"},
            {"text": "Neither word is wrong, because the catalyst supplies the "
                     "heat",
             "correct": False,
             "why": "A catalyst speeds a reaction up without supplying energy. "
                    "The flask needs no heating"},
            {"text": "Both words are wrong, because a fizz means a "
                     "displacement",
             "correct": False,
             "why": "A fizz is a gas escaping, and gases escape from several "
                    "types. It names nothing"},
        ],
        "figure": None,
    },
    {
        "id": "c5-05-h13",
        "band": "harder",
        "text": "A burning magnesium ribbon lowered into a jar of carbon "
                "dioxide keeps burning, leaving white magnesium oxide and "
                "black specks of carbon. No oxygen gas was in the jar. Name "
                "the type.",
        "options": [
            {"text": "Combustion, because the ribbon carries on burning with a "
                     "bright flame, and burning is what the word combustion "
                     "means",
             "correct": False,
             "why": "Combustion needs oxygen itself as a reactant. Here the "
                    "oxygen is locked inside carbon dioxide before it starts"},
            {"text": "Displacement: magnesium has taken the oxygen from carbon "
                     "dioxide, and the carbon is what is left",
             "correct": True},
            {"text": "Thermal decomposition, because the carbon dioxide has "
                     "been broken apart",
             "correct": False,
             "why": "Two substances went in, magnesium and carbon dioxide. A "
                    "decomposition starts with one"},
            {"text": "None of the four, because carbon is not a metal",
             "correct": False,
             "why": "Magnesium is, and it is the one doing the taking. A "
                    "non-metal partner does not put it outside the four"},
        ],
        "figure": None,
    },
    {
        "id": "c5-05-h14",
        "band": "harder",
        "text": "A reaction gives out heat, has two reactants, neither of them "
                "oxygen, and no metal anywhere in it. Which of the four types "
                "does that leave?",
        "options": [
            {"text": "Combustion, because reactions that give out heat burn",
             "correct": False,
             "why": "Combustion needs oxygen as a reactant, and this reaction "
                    "has none"},
            {"text": "Displacement, because two reactants and energy out is "
                     "its signature",
             "correct": False,
             "why": "Displacement needs a metal and a compound of a different "
                    "metal, and there is no metal here"},
            {"text": "Thermal decomposition, because nothing else is left to "
                     "choose",
             "correct": False,
             "why": "A decomposition has one reactant. This has two, so it was "
                    "ruled out at the first question"},
            {"text": "None of them, and the elimination is what proves it",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c5-05-h15",
        "band": "harder",
        "text": "You are told only this about a reaction: two reactants, one "
                "product, heat given out, and neither reactant is oxygen. What "
                "can you name and what can you not?",
        "options": [
            {"text": "A combustion, and nothing more can be said about it",
             "correct": False,
             "why": "Combustion needs oxygen as a reactant, and this reaction "
                    "has none"},
            {"text": "A displacement, though not which two metals were used",
             "correct": False,
             "why": "A displacement leaves two products, not one, and needs a "
                    "metal going in"},
            {"text": "A synthesis, and that it is exothermic — but none of the "
                     "four types fits it",
             "correct": True},
            {"text": "Nothing at all, because two reactants could belong to "
                     "any type",
             "correct": False,
             "why": "One product rules most of them out, and it is exactly "
                    "what synthesis means"},
        ],
        "figure": None,
    },
    {
        "id": "c5-05-h16",
        "band": "harder",
        "text": "Why is oxidation almost always a safe answer when a substance "
                "burns in air, while combustion is not always safe when a "
                "substance gains oxygen?",
        "options": [
            {"text": "Because every combustion is an oxidation, but plenty of "
                     "oxidations never burn",
             "correct": True},
            {"text": "Because oxidation is the vaguer word, and a vague answer "
                     "is harder to mark wrong",
             "correct": False,
             "why": "It is not vagueness. Oxidation is the wider class and "
                    "burning genuinely falls inside it"},
            {"text": "Because combustion is used for fuels only, and most "
                     "substances are not fuels",
             "correct": False,
             "why": "Anything that burns in oxygen is behaving as a fuel, "
                    "metals included"},
            {"text": "Because gaining oxygen and burning are unrelated ideas",
             "correct": False,
             "why": "They are closely related: burning in air IS a gain of "
                    "oxygen, which is why one name sits inside the other"},
        ],
        "figure": None,
    },
    {
        "id": "c5-05-h17",
        "band": "harder",
        "text": "Copper can be obtained from copper oxide by heating it with "
                "carbon, but not by heating copper oxide on its own. Name what "
                "each of those would be, and say why only one works.",
        "options": [
            {"text": "With carbon it is a combustion and alone it is an "
                     "oxidation, and only a reaction that burns is ever hot "
                     "enough to free a metal from the oxide it sits in",
             "correct": False,
             "why": "No oxygen gas goes in either way, so neither of those "
                    "names fits"},
            {"text": "With carbon it is a displacement, which works; alone it "
                     "would be a decomposition, and copper oxide does not "
                     "decompose in a school tube",
             "correct": True},
            {"text": "Both would be displacements, and only the hotter of the "
                     "two runs",
             "correct": False,
             "why": "Heating copper oxide alone gives it no second reactant, "
                    "so there is nothing to do the displacing"},
            {"text": "Both would be decompositions, and the carbon simply "
                     "speeds one of them up",
             "correct": False,
             "why": "With carbon there are two reactants, which rules a "
                    "decomposition out. Carbon is a reactant, not a catalyst"},
        ],
        "figure": None,
    },
    {
        "id": "c5-05-h18",
        "band": "harder",
        "text": "One student says a reaction with three reactants cannot be "
                "any of the four types. Another says rusting is written with "
                "iron, water and oxygen and is an oxidation. Who is right?",
        "options": [
            {"text": "The first, because each of the four types has exactly "
                     "two reactants",
             "correct": False,
             "why": "Thermal decomposition has one and rusting has three. The "
                    "count is not fixed at two"},
            {"text": "The first, because rusting is written with three only to "
                     "be helpful",
             "correct": False,
             "why": "The water is genuinely needed. Take it away and the nail "
                    "does not rust"},
            {"text": "Neither, because rusting is a corrosion rather than one "
                     "of the four",
             "correct": False,
             "why": "Rusting is iron gaining oxygen, which is what oxidation "
                    "names"},
            {"text": "The second: the four are named from what the reactants "
                     "are, not from how many",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c5-05-h19",
        "band": "harder",
        "text": "A reaction is run in an open beaker standing on a balance, "
                "and the reading does not change from start to finish. Which "
                "of the four types does that fit best?",
        "options": [
            {"text": "Thermal decomposition, because the gas that comes off "
                     "stays inside the beaker with the solid",
             "correct": False,
             "why": "A gas given off in an open beaker leaves it, and the "
                    "reading falls"},
            {"text": "Combustion, because the fuel and the oxygen together "
                     "weigh exactly what the products weigh",
             "correct": False,
             "why": "The oxygen comes from the air outside the beaker, so the "
                    "reading would move"},
            {"text": "Displacement, because nothing is taken from the air and "
                     "nothing escapes into it",
             "correct": True},
            {"text": "Oxidation, because oxygen has no weight of its own",
             "correct": False,
             "why": "Oxygen has mass, which is exactly why an oxidised product "
                    "is heavier"},
        ],
        "figure": None,
    },
    {
        "id": "c5-05-h20",
        "band": "harder",
        "text": "A reaction is both a synthesis and a combustion. How many "
                "reactants and products must it have?",
        "options": [
            {"text": "Two reactants and one product",
             "correct": True},
            {"text": "One reactant and two products",
             "correct": False,
             "why": "That is a decomposition, which is synthesis run the other "
                    "way"},
            {"text": "Two reactants and two products",
             "correct": False,
             "why": "A synthesis makes a single compound, so only one product "
                    "comes out"},
            {"text": "It cannot be both, so the question has no answer",
             "correct": False,
             "why": "Hydrogen burning in oxygen to give water only is both at "
                    "once"},
        ],
        "figure": None,
    },
    {
        "id": "c5-05-h21",
        "band": "harder",
        "text": "Which of the four types could never be shown by a reaction "
                "between two gases?",
        "options": [
            {"text": "Combustion, because a gas cannot burn on its own without "
                     "a wick or a solid to sit on",
             "correct": False,
             "why": "Methane and hydrogen burn as gases with no wick at all"},
            {"text": "Displacement, because it needs a solid metal and another "
                     "metal's compound",
             "correct": True},
            {"text": "Oxidation, because a gas cannot gain oxygen",
             "correct": False,
             "why": "Hydrogen is a gas and gains oxygen when it burns to "
                    "water"},
            {"text": "Thermal decomposition, because a gas cannot be heated in "
                     "a tube the way a solid can",
             "correct": False,
             "why": "A gas can be heated and can decompose. Its state is not "
                    "the objection"},
        ],
        "figure": None,
    },
    {
        "id": "c5-05-h22",
        "band": "harder",
        "text": "An exam says only this: a white solid was heated, two new "
                "substances formed, and the mass fell. A student answers "
                "thermal decomposition. How confident should they be?",
        "options": [
            {"text": "Certain already, because a mass fall can only mean a "
                     "decomposition",
             "correct": False,
             "why": "Mass falls whenever a gas leaves, and gases leave in "
                    "reactions that are not decompositions"},
            {"text": "Not at all, because a white solid could be almost "
                     "anything",
             "correct": False,
             "why": "What the solid is does not matter. The shape of the "
                    "reaction is what names it"},
            {"text": "Certain already, because two products can only come from "
                     "one reactant",
             "correct": False,
             "why": "Two products come out of plenty of reactions that had two "
                    "reactants going in"},
            {"text": "Very confident, and certain once they know only one "
                     "substance was in the tube",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c5-05-h23",
        "band": "harder",
        "text": "Why does the decision rule still work for a reaction nobody "
                "in the room has ever seen before?",
        "options": [
            {"text": "Because it asks about the reactants, which every "
                     "reaction has, rather than about a remembered example",
             "correct": True},
            {"text": "Because every reaction anyone could meet in a school "
                     "laboratory turns out to be one of these four in the end",
             "correct": False,
             "why": "Marble in acid is not, and nor is the reaction in a leaf. "
                    "The set has edges"},
            {"text": "Because an unfamiliar reaction is usually a "
                     "decomposition of something",
             "correct": False,
             "why": "It could be any of them or none. Being unfamiliar points "
                    "at nothing"},
            {"text": "Because a new reaction will always look like one you "
                     "have already met",
             "correct": False,
             "why": "Appearance is what the rule deliberately ignores, and two "
                    "types can look identical"},
        ],
        "figure": None,
    },
    {
        "id": "c5-05-h24",
        "band": "harder",
        "text": "Aluminium is obtained from its ore using electricity rather "
                "than by reacting it with another metal. Which of the four "
                "types is that, if any?",
        "options": [
            {"text": "Displacement, because the electricity takes aluminium's "
                     "place in the compound",
             "correct": False,
             "why": "Electricity is not a substance and cannot take a place in "
                    "a compound"},
            {"text": "Thermal decomposition, because the compound is being "
                     "split into two",
             "correct": False,
             "why": "The rule names heat as what does the splitting, and here "
                    "it is a current"},
            {"text": "None of them, because nothing displaces the aluminium "
                     "and no heat breaks it apart",
             "correct": True},
            {"text": "Oxidation, because aluminium oxide is what is being "
                     "worked on",
             "correct": False,
             "why": "The aluminium is losing its oxygen rather than gaining "
                    "any"},
        ],
        "figure": None,
    },
    {
        "id": "c5-05-h25",
        "band": "harder",
        "text": "Two reactions each take energy in the whole time they run. "
                "One has a single reactant; the other has two. What can be "
                "said about each?",
        "options": [
            {"text": "Both are thermal decompositions, since thermal "
                     "decomposition is the endothermic one of the four",
             "correct": False,
             "why": "It is the endothermic one of the FOUR. Two reactants rule "
                    "the second one out"},
            {"text": "The first fits thermal decomposition; the second is "
                     "endothermic but outside the four",
             "correct": True},
            {"text": "Neither of them is a decomposition, because a "
                     "decomposition gives its energy out rather than taking it "
                     "in",
             "correct": False,
             "why": "A decomposition takes energy in, which is why it stops "
                    "when the flame is removed"},
            {"text": "Both are outside the four, because all four types give "
                     "energy out",
             "correct": False,
             "why": "Thermal decomposition is one of the four and takes energy "
                    "in"},
        ],
        "figure": None,
    },
    {
        "id": "c5-05-h26",
        "band": "harder",
        "text": "The mass tie-breaker is useless for a reaction run in a "
                "sealed flask. Explain why, and say what you would use "
                "instead.",
        "options": [
            {"text": "Because sealing a flask makes every reaction give off a "
                     "gas of its own, and that gas is what confuses the "
                     "balance",
             "correct": False,
             "why": "Sealing a flask changes no reaction. It only stops what "
                    "is made from leaving"},
            {"text": "Because a balance cannot be trusted once a stopper is in "
                     "the flask",
             "correct": False,
             "why": "The balance is fine. It is the system that has been "
                    "closed"},
            {"text": "Because mass is created inside a sealed flask and lost "
                     "outside one",
             "correct": False,
             "why": "Mass is neither created nor destroyed. It simply cannot "
                    "cross the seal"},
            {"text": "Because nothing can enter or leave, so the reading holds "
                     "whatever happens — count the reactants instead",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c5-05-h27",
        "band": "harder",
        "text": "Explain why none of the four is an answer about the SET of "
                "names rather than a fifth name inside it.",
        "options": [
            {"text": "Because it says no member of the set fits, which is a "
                     "statement about the set's edge",
             "correct": True},
            {"text": "Because it is the answer to write down when none of the "
                     "other four names can be remembered in time",
             "correct": False,
             "why": "It is a positive finding reached by checking all four, "
                    "not a gap where an answer should be"},
            {"text": "Because it is really a fifth type of reaction that has "
                     "simply not been taught to you yet",
             "correct": False,
             "why": "There is no fifth type. The reactions it covers have "
                    "names of their own, such as neutralisation"},
            {"text": "Because it means the reaction has no type anywhere in "
                     "chemistry",
             "correct": False,
             "why": "It has a type. The type is simply not one of these four"},
        ],
        "figure": None,
    },
    {
        "id": "c5-05-h28",
        "band": "harder",
        "text": "You are told only the products of a reaction: copper and "
                "carbon dioxide. Name the type, and say how that is possible "
                "without being told the reactants.",
        "options": [
            {"text": "Combustion, because carbon dioxide is what burning "
                     "always produces, so the gas on its own names the "
                     "reaction",
             "correct": False,
             "why": "Carbon dioxide also comes from a heated carbonate and "
                    "from acid on marble. It names nothing alone"},
            {"text": "Oxidation, because the copper has been oxidised to make "
                     "the gas",
             "correct": False,
             "why": "The copper is the metal that came OUT. The gas carries "
                    "the carbon, not the copper"},
            {"text": "Displacement: the copper must have come out of a "
                     "compound, and the carbon must have taken its oxygen",
             "correct": True},
            {"text": "It cannot be named, because only the reactants can name "
                     "a reaction",
             "correct": False,
             "why": "Working back from the products is allowed when they leave "
                    "one possibility"},
        ],
        "figure": None,
    },
    {
        "id": "c5-05-h29",
        "band": "harder",
        "text": "A student proposes a fifth type: reactions that give off a "
                "gas. Explain why that would be a worse way of classifying "
                "than the four.",
        "options": [
            {"text": "Because no reaction really gives off a gas unless it has "
                     "been heated first",
             "correct": False,
             "why": "Marble in acid gives off a gas cold. The objection is not "
                    "about the heating"},
            {"text": "Because it groups reactions by what they look like, so "
                     "it predicts nothing",
             "correct": True},
            {"text": "Because a gas is harder to weigh than a solid or a "
                     "liquid",
             "correct": False,
             "why": "How hard something is to measure is not what makes a "
                    "grouping useless"},
            {"text": "Because two different reactions must never be put in one "
                     "group",
             "correct": False,
             "why": "Grouping reactions is the whole point. The question is "
                    "whether the group tells you anything"},
        ],
        "figure": None,
    },
    {
        "id": "c5-05-h30",
        "band": "harder",
        "text": "A displacement and a combustion can both be started with a "
                "lit splint, both give out heat, and both leave a new solid. "
                "Which single fact decides the name?",
        "options": [
            {"text": "Whether the reaction gave out light as well as heat",
             "correct": False,
             "why": "Thermite glows white-hot and is a displacement. Light "
                    "does not decide it"},
            {"text": "Whether the solid left behind is heavier than the solid "
                     "that went in",
             "correct": False,
             "why": "Both can leave a heavier solid, so the balance does not "
                    "separate them"},
            {"text": "Whether a flame was visible from beginning to end",
             "correct": False,
             "why": "A flame shows how fast and how hot it is. What names it "
                    "is what went in"},
            {"text": "Whether the second reactant is oxygen or a compound of a "
                     "different metal",
             "correct": True},
        ],
        "figure": None,
    },
]
