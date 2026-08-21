"""C5 lesson 02 — Thermal decomposition: twelve questions (MRB-246).

The lesson's argument is one shape: one compound in, two or more substances
out, nothing added, and no way back on cooling. The page teaches it by running
the same four stages on three different substances, so these twelve probe the
angles the mastery ladder leaves alone — the gas test as evidence rather than
as a ritual, the mass as evidence rather than as a number, and the two
reactions this one is most often mistaken for.

The distractors are built from the lesson's two declared misconceptions.

`REACT-12` (a substance that goes black when heated has burnt) drives the wrong
options in e01, e02, s01 and h01. Each treats the flame as the reactant. e02
and h01 are the two that matter: e02 offers three OTHER reasons burning can be
ruled out — no ash, not a fuel, the mass — and only one of them is the reason,
and h01 removes the air altogether so that the belief has nowhere left to
stand.

`REACT-13` (a decomposition reverses when it cools) drives e04, s03 and h02,
where cooling, or time, or reversibility is treated as the thing that decides
what kind of change happened. e04 is the register's own case put as a question
about tomorrow morning, which is where a student actually meets it.

A third strand, everywhere on the page and in neither register entry, is that
a falling balance means matter was destroyed — or that a gas weighs nothing.
s02 and h03 are built on it: h03 catches the gas in a balloon so that the mass
does NOT fall, and three of its four options explain a change that has not
happened.

A fourth strand is that heat is the reaction. Every one of e01, s01, s04 and
h04 offers an answer in which the flame, the oven or the kiln is doing the
chemistry, because that is the mistake a real student in a real lab makes when
four reaction types have all been demonstrated with a Bunsen burner.

Every question here is new prose — a question bank is the one place in these
two files where that is true — and the bar is §13's: each distractor is a
WRONG RULE in the correct answer's own shape, at the correct answer's own
length, and each is a mistake a real student actually makes. Every option set
below was counted; no correct answer is strictly the longest in its set by
four words or by 1.4×.
"""

UNIT = "C5"
LESSON = "thermal-decomposition"
LESSON_NUMBER = 2

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "c5-02-e01",
        "band": "easier",
        "text": "Green copper carbonate is heated in a tube on its own. It "
                "turns black and gives off a gas. What kind of reaction is "
                "this?",
        "options": [
            {"text": "Thermal decomposition, because heat broke one compound "
                     "into two substances", "correct": True},
            {"text": "Combustion, because the powder burnt in the heat of the "
                     "flame", "correct": False,
             "why": "Burning needs oxygen as a reactant, and nothing at all "
                    "was added to the tube. The reaction works just as well "
                    "with no air in it."},
            {"text": "Oxidation, because the black solid gained oxygen from "
                     "the air", "correct": False,
             "why": "The oxygen in the copper oxide came out of the carbonate "
                    "itself. Nothing joined the powder — the tube got "
                    "lighter, not heavier."},
            {"text": "A physical change, because only the colour of the "
                     "powder changed", "correct": False,
             "why": "A gas came off and a new black solid was left behind. "
                    "Two new substances is a chemical change, whatever the "
                    "colour did."},
        ],
        "figure": None,
    },
    {
        "id": "c5-02-e02",
        "band": "easier",
        "text": "A student says the copper carbonate went black because it "
                "burnt. Which reason shows they are wrong?",
        "options": [
            {"text": "Burning always leaves ash, and no ash was left in the "
                     "tube", "correct": False,
             "why": "Plenty of things burn and leave no ash at all — a candle "
                    "leaves none. What rules burning out here is that there "
                    "was no oxygen for it to burn in."},
            {"text": "Burning needs oxygen, and nothing at all was added to "
                     "the tube", "correct": True},
            {"text": "Burning only happens to fuels, and this powder is not a "
                     "fuel", "correct": False,
             "why": "Magnesium and iron wool burn and neither is a fuel. The "
                    "reason nothing burnt is that burning needs oxygen and "
                    "none was there."},
            {"text": "Burning would have made the tube heavier, and it stayed "
                     "the same", "correct": False,
             "why": "The tube did not stay the same — it got lighter, because "
                    "a gas left it. The mass falling is evidence, and it is "
                    "evidence against burning."},
        ],
        "figure": None,
    },
    {
        "id": "c5-02-e03",
        "band": "easier",
        "text": "The gas coming off the heated tube is bubbled through "
                "limewater, and the limewater turns milky. What does that "
                "tell you?",
        "options": [
            {"text": "Oxygen was given off, because limewater goes milky in "
                     "any gas", "correct": False,
             "why": "Limewater is a test, not a detector. It goes milky for "
                    "carbon dioxide and stays clear for oxygen, nitrogen and "
                    "the rest."},
            {"text": "The solid dissolved in the limewater, because the "
                     "milkiness is powder", "correct": False,
             "why": "Only the gas reaches the limewater; the black solid "
                    "stays in the tube. The milkiness is a new solid that the "
                    "gas made in the liquid."},
            {"text": "Carbon dioxide was given off, because only that gas "
                     "turns limewater milky", "correct": True},
            {"text": "Water vapour was given off, because limewater is mostly "
                     "water itself", "correct": False,
             "why": "Adding water to limewater does nothing you could see. "
                    "The milky change is the test for carbon dioxide and for "
                    "nothing else."},
        ],
        "figure": None,
    },
    {
        "id": "c5-02-e04",
        "band": "easier",
        "text": "The black powder is left in the tube to cool overnight. What "
                "is in the tube the next morning?",
        "options": [
            {"text": "Green copper carbonate again, because the change "
                     "reverses as it cools", "correct": False,
             "why": "Cooling puts no energy in and joins nothing back "
                    "together. A decomposition is a chemical change and it "
                    "does not run backwards on its own."},
            {"text": "Green copper carbonate again, because the gas comes "
                     "back into the tube", "correct": False,
             "why": "The gas left the tube and went into the limewater. It is "
                    "not sitting above the powder waiting to rejoin it."},
            {"text": "A mixture of both, because only half of the powder ever "
                     "changed", "correct": False,
             "why": "The colour change was watched spreading all the way up "
                    "the tube. Once every bit of it is black, every bit of it "
                    "has decomposed."},
            {"text": "Black copper oxide still, because the change does not "
                     "reverse on cooling", "correct": True},
                   ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "c5-02-s01",
        "band": "standard",
        "text": "Magnesium ribbon is heated in air and leaves a white powder "
                "that weighs more than the ribbon did. Is this a thermal "
                "decomposition?",
        "options": [
            {"text": "No, because the mass went up, so something joined the "
                     "magnesium", "correct": True},
            {"text": "Yes, because heating turned one substance into a "
                     "different one", "correct": False,
             "why": "Heat alone does not make it decomposition. The magnesium "
                    "joined with oxygen from the air, so two reactants went "
                    "in rather than one."},
            {"text": "Yes, because the ribbon came apart into a powder and a "
                     "gas", "correct": False,
             "why": "Nothing came apart and no gas came off. The white powder "
                    "is magnesium oxide, and it holds everything the ribbon "
                    "held plus oxygen."},
            {"text": "No, because a decomposition has to give off a gas you "
                     "can test", "correct": False,
             "why": "The verdict is right and the rule is not. Not every "
                    "decomposition gives off a gas — what rules this one out "
                    "is the mass going up."},
                   ],
        "figure": None,
    },
    {
        "id": "c5-02-s02",
        "band": "standard",
        "text": "4.00 g of copper carbonate is heated until the colour change "
                "is complete. The tube now holds 2.58 g. Where has the "
                "missing 1.42 g gone?",
        "options": [
            {"text": "It was destroyed by the heat of the flame under the "
                     "tube", "correct": False,
             "why": "Mass is never destroyed. Every atom that was in the "
                    "carbonate is still somewhere, and 1.42 g of them are in "
                    "the gas that left."},
            {"text": "It left the tube as carbon dioxide and went into the "
                     "limewater", "correct": True},
            {"text": "It turned into the heat and light the reaction gave "
                     "out", "correct": False,
             "why": "This reaction takes heat in rather than giving it out, "
                    "and heat weighs nothing in any case. Energy is not made "
                    "of matter."},
            {"text": "It is still in the tube, but the black powder takes "
                     "less room", "correct": False,
             "why": "A balance weighs mass, not room. A powder that took up "
                    "less space and had lost nothing would read exactly what "
                    "it read before."},
                   ],
        "figure": None,
    },
    {
        "id": "c5-02-s03",
        "band": "standard",
        "text": "Ice in a beaker is heated until it melts. Copper carbonate "
                "in a tube is heated until it goes black. What is the real "
                "difference between the two changes?",
        "options": [
            {"text": "The ice needed less heat than the copper carbonate in "
                     "the tube", "correct": False,
             "why": "How much heat a change needs does not tell you what kind "
                    "it is. Limestone needs far more heat than copper "
                    "carbonate and both are decompositions."},
            {"text": "The ice changed state and the copper carbonate changed "
                     "colour instead", "correct": False,
             "why": "Colour is a clue and not the test. Limestone decomposes "
                    "and stays white the whole way through, and it is the "
                    "same reaction."},
            {"text": "The ice comes back on cooling and the black powder does "
                     "not", "correct": True},
            {"text": "The ice was in a beaker and the powder was in a test "
                     "tube", "correct": False,
             "why": "The container decides nothing. Melt ice in a tube and it "
                    "is still physical; heat the carbonate in a dish and it "
                    "still decomposes."},
                   ],
        "figure": None,
    },
    {
        "id": "c5-02-s04",
        "band": "standard",
        "text": "Baking powder in a cake mixture is heated in an oven and the "
                "cake rises. Why is this a thermal decomposition?",
        "options": [
            {"text": "The oven air reacted with the powder and made bubbles "
                     "of gas", "correct": False,
             "why": "Nothing from the oven joins in. The baking powder comes "
                    "apart on its own once it is hot enough, which is why it "
                    "works inside a sealed tin."},
            {"text": "The heat boiled the water in the mixture and the steam "
                     "rose", "correct": False,
             "why": "Boiling is a physical change and it makes nothing new. "
                    "The gas that raises a cake is carbon dioxide from a "
                    "compound breaking apart."},
            {"text": "The mixture expanded because everything gets bigger "
                     "when you heat it", "correct": False,
             "why": "Expansion is far too small to raise a cake, and it would "
                    "go back down again on cooling. A risen cake stays "
                    "risen."},
            {"text": "One compound broke down and the carbon dioxide it made "
                     "was trapped", "correct": True},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "c5-02-h01",
        "band": "harder",
        "text": "A teacher heats copper carbonate in a tube that has had all "
                "the air pumped out of it. It still turns black and a gas "
                "still comes off. What does that show?",
        "options": [
            {"text": "Nothing burnt, because burning needs oxygen and there "
                     "was none there", "correct": True},
            {"text": "The powder burnt using the oxygen that was inside the "
                     "compound", "correct": False,
             "why": "Burning means reacting with oxygen from outside. Oxygen "
                    "that was already part of the compound is not a second "
                    "reactant — it is part of the first."},
            {"text": "Nothing happened, because a reaction cannot run without "
                     "air around it", "correct": False,
             "why": "Something clearly happened — the powder went black and a "
                    "gas came off. Plenty of reactions need no air at all, "
                    "and this is one of them."},
            {"text": "The tube leaked, because a gas cannot appear where "
                     "there is none", "correct": False,
             "why": "The gas did not appear from nowhere. It was locked up "
                    "inside the solid compound, and heating the compound let "
                    "it out."},
                   ],
        "figure": None,
    },
    {
        "id": "c5-02-h02",
        "band": "harder",
        "text": "A substance is heated and something changes. Which of these "
                "is the best evidence that a chemical change happened rather "
                "than a physical one?",
        "options": [
            {"text": "The substance changed colour clearly while the flame "
                     "was under it", "correct": False,
             "why": "Colour appears on both sides of the line. Limestone "
                    "decomposes and never changes colour, and a block of ice "
                    "goes cloudy as it melts."},
            {"text": "What was left behind had different properties and "
                     "stayed that way afterwards", "correct": True},
            {"text": "The substance took a very long time to change under the "
                     "flame", "correct": False,
             "why": "Time settles nothing. Limestone takes a long time and "
                    "decomposes; a large block of ice takes a long time and "
                    "only melts."},
            {"text": "A great deal of heat was needed before anything "
                     "happened at all", "correct": False,
             "why": "How much heat is needed is a fact about the substance, "
                    "not about the kind of change. Melting iron needs a great "
                    "deal of heat and makes nothing new."},
                   ],
        "figure": None,
    },
    {
        "id": "c5-02-h03",
        "band": "harder",
        "text": "A student catches the gas from a decomposing carbonate in a "
                "balloon fitted over the tube, and weighs the whole apparatus "
                "before and after. What does the balance read afterwards?",
        "options": [
            {"text": "Less than before, because a gas weighs less than a "
                     "solid does", "correct": False,
             "why": "A gas weighs less for its size, not less in total. "
                    "Nothing has left the apparatus, so nothing has been lost "
                    "from the balance."},
            {"text": "Less than before, because the balloon holds the gas up "
                     "in the air", "correct": False,
             "why": "The balloon holds carbon dioxide, which is heavier than "
                    "air and lifts nothing. Even a balloon that did float "
                    "would still be pulling on the tube."},
            {"text": "The same as before, because everything that left is "
                     "still in the balloon", "correct": True},
            {"text": "More than before, because the gas takes up far more "
                     "room now", "correct": False,
             "why": "Room is not mass. The same atoms are on the balance "
                    "whether they are packed into a solid or spread out "
                    "inside a balloon."},
        ],
        "figure": None,
    },
    {
        "id": "c5-02-h04",
        "band": "harder",
        "text": "A cement works plans to heat its limestone kilns with "
                "electricity from wind turbines instead of by burning fuel. "
                "Why will it still release carbon dioxide?",
        "options": [
            {"text": "The wind turbines give off carbon dioxide while they "
                     "are being built", "correct": False,
             "why": "That is true of any building project and it is not the "
                    "reason here. The gas comes out of the rock every single "
                    "time the kiln runs."},
            {"text": "The kiln has to be started with a fuel before the "
                     "electricity takes over", "correct": False,
             "why": "A kiln can be heated entirely by electricity. One that "
                    "never burned a thing would still release the gas locked "
                    "inside the limestone."},
            {"text": "Electricity from wind turbines is not hot enough to "
                     "reach 900 °C", "correct": False,
             "why": "Electric furnaces reach far higher temperatures than "
                    "that. The problem is not the heat source — it is what "
                    "the reaction itself produces."},
            {"text": "The decomposition of the limestone itself gives off "
                     "carbon dioxide", "correct": True},
                   ],
        "figure": None,
    },
]
