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
]
