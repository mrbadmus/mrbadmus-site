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
        "text": "Baking soda in a cake mixture is heated in an oven and the "
                "cake rises. Why is this a thermal decomposition?",
        "options": [
            {"text": "The oven air reacted with the powder and made bubbles "
                     "of gas", "correct": False,
             "why": "Nothing from the oven joins in. The baking soda comes "
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

    # ── easier · MRB-335 top-up ─────────────────────────────────────────
    {
        "id": "c5-02-e05",
        "band": "easier",
        "text": "How many reactants does a thermal decomposition have?",
        "options": [
            {"text": "Two, because heat is supplied throughout and anything a "
                     "reaction cannot proceed without has to count as one of "
                     "the things reacting",
             "correct": False,
             "why": "Heat is a condition rather than a substance. It never "
                    "counts as a reactant"},
            {"text": "Two or more, like every other reaction",
             "correct": False,
             "why": "Having only one is exactly what makes decomposition "
                    "unusual"},
            {"text": "It depends how many products there are",
             "correct": False,
             "why": "There are two or more products and always one reactant. "
                    "That is the shape of it"},
            {"text": "One",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c5-02-e06",
        "band": "easier",
        "text": "What is quicklime?",
        "options": [
            {"text": "The everyday name for calcium oxide, the white solid "
                     "left when limestone is decomposed",
             "correct": True},
            {"text": "Limestone that has been ground very finely before it is "
                     "spread",
             "correct": False,
             "why": "Grinding is a physical change. Quicklime is a different "
                    "substance, made by decomposing limestone"},
            {"text": "The gas given off when limestone is heated",
             "correct": False,
             "why": "That gas is carbon dioxide. Quicklime is the solid left "
                    "behind"},
            {"text": "Another name for limewater",
             "correct": False,
             "why": "Limewater is a clear solution used to test a gas. "
                    "Quicklime is a white solid"},
        ],
        "figure": None,
    },
    {
        "id": "c5-02-e07",
        "band": "easier",
        "text": "What does it mean to say a reaction ABSORBS energy?",
        "options": [
            {"text": "It stores the energy it is given and releases it again "
                     "later on, once the flame has been taken away and the "
                     "tube has begun to cool",
             "correct": False,
             "why": "Nothing is released back. Take the flame away and the "
                    "reaction simply stops"},
            {"text": "It takes energy in, which is why the heating has to "
                     "keep going",
             "correct": True},
            {"text": "It gives energy out to the room",
             "correct": False,
             "why": "That is the opposite, and it is what combustion and "
                    "displacement do"},
            {"text": "It uses up the oxygen in the tube",
             "correct": False,
             "why": "Absorbing energy is nothing to do with oxygen. A "
                    "decomposition works with no air at all"},
        ],
        "figure": None,
    },

    # ── standard · MRB-335 top-up ───────────────────────────────────────
    {
        "id": "c5-02-s05",
        "band": "standard",
        "text": "A green powder is heated in a tube and turns black, and the "
                "flame is then taken away. What happens next?",
        "options": [
            {"text": "It turns green again as it cools, because the two "
                     "products join back together once there is no longer "
                     "enough energy to keep them apart",
             "correct": False,
             "why": "A decomposition does not reverse on cooling. One of the "
                    "products has left the tube entirely"},
            {"text": "It goes on decomposing until it is all gone",
             "correct": False,
             "why": "The reaction absorbs energy, so it stops when the "
                    "heating does"},
            {"text": "It stays black",
             "correct": True},
            {"text": "It catches fire",
             "correct": False,
             "why": "Nothing here burns, and there may be no air in the tube "
                    "at all"},
        ],
        "figure": None,
    },
    {
        "id": "c5-02-s06",
        "band": "standard",
        "text": "An airbag holds a solid that decomposes to nitrogen gas in "
                "about thirty milliseconds. Why was a decomposition chosen for "
                "the job?",
        "options": [
            {"text": "Because a decomposition is the only kind of reaction "
                     "fast enough to finish in that time, whatever substances "
                     "are used",
             "correct": False,
             "why": "Plenty of reactions are fast. What matters is that one "
                    "solid becomes an enormous volume of gas"},
            {"text": "Because it needs no oxygen, and a car may be "
                     "upside down",
             "correct": False,
             "why": "Needing no oxygen is a genuine advantage of a "
                    "decomposition, and the reason a bag inflates is the "
                    "volume of gas"},
            {"text": "Because it absorbs energy, so the bag stays cool",
             "correct": False,
             "why": "The bag gets warm. Cooling is not what it was chosen "
                    "for"},
            {"text": "Because one solid becomes a large volume of gas, on "
                     "command",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c5-02-s07",
        "band": "standard",
        "text": "6.00 g of a carbonate is heated to constant mass and 3.60 g "
                "of solid is left. What mass of gas escaped?",
        "options": [
            {"text": "2.40 g",
             "correct": True},
            {"text": "9.60 g, which is the two masses added together as "
                     "conservation of mass requires",
             "correct": False,
             "why": "The 3.60 g is part of the 6.00 g rather than extra to "
                    "it. The gas is what is missing"},
            {"text": "3.60 g",
             "correct": False,
             "why": "That is the solid still in the tube, which did not "
                    "escape anywhere"},
            {"text": "6.00 g",
             "correct": False,
             "why": "That is everything you started with. Most of it is still "
                    "in the tube"},
        ],
        "figure": None,
    },
    {
        "id": "c5-02-s08",
        "band": "standard",
        "text": "A limewater test on the gas from a heated tube comes back "
                "CLEAR. What can you say?",
        "options": [
            {"text": "That no gas was given off at all, since a gas that "
                     "reaches limewater and does nothing to it cannot have "
                     "been there in the first place",
             "correct": False,
             "why": "A clear result is a result ABOUT the gas. Plenty of "
                    "gases leave limewater clear"},
            {"text": "That the gas is not carbon dioxide, so the solid was "
                     "probably not a carbonate",
             "correct": True},
            {"text": "That the limewater has gone off",
             "correct": False,
             "why": "Possible and not the honest first conclusion. A clear "
                    "result rules carbon dioxide out"},
            {"text": "That the reaction was not a decomposition",
             "correct": False,
             "why": "Plenty of decompositions give other gases. What the test "
                    "rules out is carbon dioxide"},
        ],
        "figure": None,
    },

    # ── harder · MRB-335 top-up ─────────────────────────────────────────
    {
        "id": "c5-02-h05",
        "band": "harder",
        "text": "Cement production accounts for something like 8% of the "
                "world's carbon dioxide. Why can that not be fixed by changing "
                "the fuel in the kilns?",
        "options": [
            {"text": "Because the kilns have to reach 900 °C, and only a "
                     "fossil fuel does",
             "correct": False,
             "why": "Electricity and hydrogen both reach it. The gas that "
                    "cannot be avoided comes from the ROCK"},
            {"text": "Because cement burns as it sets",
             "correct": False,
             "why": "Setting is a different process and releases no carbon "
                    "dioxide. The emission happens in the kiln"},
            {"text": "Because carbon dioxide is needed to make the cement "
                     "work",
             "correct": False,
             "why": "It is a waste product rather than an ingredient. It "
                    "simply cannot be left out of the reaction"},
            {"text": "Because the decomposition of the limestone itself "
                     "releases carbon dioxide, whatever heats the kiln",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c5-02-h06",
        "band": "harder",
        "text": "A student says any reaction that gives off a gas must be a "
                "thermal decomposition. Which example deals with that?",
        "options": [
            {"text": "Magnesium dropped into dilute acid, which fizzes hard "
                     "and gives off hydrogen",
             "correct": True},
            {"text": "Copper carbonate heated in a tube with no air in it",
             "correct": False,
             "why": "That IS a decomposition, so it supports the student "
                    "rather than refuting them"},
            {"text": "Limestone heated in a kiln",
             "correct": False,
             "why": "Another decomposition. To break the rule you need a gas "
                    "from a reaction with two reactants"},
            {"text": "Baking soda heated in an oven",
             "correct": False,
             "why": "Also a decomposition, and one the lesson names"},
        ],
        "figure": None,
    },
    {
        "id": "c5-02-h07",
        "band": "harder",
        "text": "Two tubes are heated. One holds a carbonate and loses mass; "
                "one holds a metal and gains it. Both changed colour. What "
                "separates them?",
        "options": [
            {"text": "The colour change, since a decomposition always darkens "
                     "a solid",
             "correct": False,
             "why": "Copper goes black on oxidising and copper carbonate goes "
                    "black on decomposing. Colour separates nothing here"},
            {"text": "The direction the mass moved: gaining oxygen makes it "
                     "heavier, losing a gas makes it lighter",
             "correct": True},
            {"text": "Whether a flame was needed",
             "correct": False,
             "why": "Both were heated. The heating is the same in each"},
            {"text": "Which of them happened faster",
             "correct": False,
             "why": "Speed is not what names a reaction. What went in and "
                    "what came out is"},
        ],
        "figure": None,
    },
    {
        "id": "c5-02-h08",
        "band": "harder",
        "text": "The gas from a decomposing carbonate is caught in a balloon "
                "over the tube and the whole apparatus is weighed. It reads "
                "the same as before. What has that PROVED?",
        "options": [
            {"text": "That no reaction happened, since the balance did not "
                     "move",
             "correct": False,
             "why": "The solid changed colour and a balloon inflated. Plenty "
                    "happened — none of it crossed the boundary"},
            {"text": "That carbon dioxide weighs nothing",
             "correct": False,
             "why": "It weighs exactly what the open tube lost. That is why "
                    "the sealed total holds"},
            {"text": "That mass is conserved, and that the tube's loss was "
                     "the gas leaving rather than anything being destroyed",
             "correct": True},
            {"text": "That the balloon was airtight",
             "correct": False,
             "why": "That is a condition of the experiment rather than its "
                    "result"},
        ],
        "figure": None,
    },

    {
        "id": "c5-02-e08",
        "band": "easier",
        "text": "What is a product, in a decomposition?",
        "options": [
            {"text": "The substance you put into the tube at the start, which "
                     "is the only thing the reaction has to work with and so "
                     "the only thing it can produce anything from",
             "correct": False,
             "why": "That is the reactant. The products are what comes out"},
            {"text": "The heat given off",
             "correct": False,
             "why": "A decomposition takes heat IN, and heat is not a "
                    "substance in any case"},
            {"text": "One of the two or more substances the single reactant "
                     "breaks into",
             "correct": True},
            {"text": "The tube's contents at the end, taken together",
             "correct": False,
             "why": "Each product is named separately, and one of them has "
                    "usually left the tube"},
        ],
        "figure": None,
    },
    {
        "id": "c5-02-e09",
        "band": "easier",
        "text": "Which of these is a thermal decomposition?",
        "options": [
            {"text": "Magnesium burning in air to leave a white powder",
             "correct": False,
             "why": "Two reactants, and the mass goes up. That is an "
                    "oxidation"},
            {"text": "Iron left in the rain until it goes orange",
             "correct": False,
             "why": "Oxygen and water join the iron. Nothing has been broken "
                    "down"},
            {"text": "Zinc dropped into copper sulfate solution, where it "
                     "takes the copper's place and leaves it as a brown solid "
                     "on the bottom of the tube",
             "correct": False,
             "why": "That is displacement — two reactants, and a swap rather "
                    "than a breakdown"},
            {"text": "Limestone heated in a kiln to give quicklime and a gas",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c5-02-e10",
        "band": "easier",
        "text": "Why does a thermal decomposition still work in a tube with "
                "all the air pumped out?",
        "options": [
            {"text": "Because the reaction needs nothing added — the heat "
                     "does the work on one compound",
             "correct": True},
            {"text": "Because there is enough oxygen left in the tube even "
                     "after it has been pumped out, and a decomposition needs "
                     "only a trace of it to get going",
             "correct": False,
             "why": "It needs no oxygen at all, which is exactly what the "
                    "empty tube shows"},
            {"text": "Because the compound makes its own air as it heats",
             "correct": False,
             "why": "It makes a gas, and that gas is a product rather than "
                    "something the reaction needed"},
            {"text": "Because pumping the air out makes it hotter",
             "correct": False,
             "why": "Pumping changes nothing about the temperature. The "
                    "Bunsen supplies that"},
        ],
        "figure": None,
    },
    {
        "id": "c5-02-s09",
        "band": "standard",
        "text": "A cake rises in the oven. Which part of that is the "
                "decomposition?",
        "options": [
            {"text": "The batter setting solid as the heat reaches it, which "
                     "is the change that holds the risen shape in place once "
                     "the cake comes out",
             "correct": False,
             "why": "The setting matters and it is not the decomposition. "
                    "What decomposes is the raising agent"},
            {"text": "The water in the batter turning to steam",
             "correct": False,
             "why": "That is a change of state and it does help the rise. No "
                    "compound has been broken down"},
            {"text": "The baking powder breaking down and releasing carbon "
                     "dioxide",
             "correct": True},
            {"text": "The sugar browning on the top",
             "correct": False,
             "why": "That is a chemical change of its own, and it is not a "
                    "decomposition of one compound into two"},
        ],
        "figure": None,
    },
    {
        "id": "c5-02-s10",
        "band": "standard",
        "text": "Why is the mass of the tube's CONTENTS a good test for "
                "whether a decomposition has happened?",
        "options": [
            {"text": "Because a decomposition always makes a gas, and a gas "
                     "always weighs less than the solid it came out of",
             "correct": False,
             "why": "The gas weighs exactly what the tube lost. The useful "
                    "point is that it LEAVES"},
            {"text": "Because mass is not conserved in a decomposition",
             "correct": False,
             "why": "Mass is conserved in every reaction. Catch the gas and "
                    "the total holds"},
            {"text": "Because the solid left behind is always lighter than "
                     "air",
             "correct": False,
             "why": "The solid stays in the tube because it is a solid. "
                    "Nothing here is lighter than air"},
            {"text": "Because one of the products usually escapes, so the "
                     "reading falls — while an oxidation makes it rise",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c5-02-h09",
        "band": "harder",
        "text": "A decomposition is described as endothermic. What would you "
                "expect a thermometer in the tube to show if the flame were "
                "removed mid-reaction?",
        "options": [
            {"text": "A rise, because the reaction goes on for a while under "
                     "its own energy and gives that energy out as it "
                     "finishes",
             "correct": False,
             "why": "It gives nothing out. Without the flame it has no energy "
                    "supply and simply stops"},
            {"text": "No change at all, because the reaction supplies its own "
                     "heat",
             "correct": False,
             "why": "That is a combustion. This one needs energy put in "
                    "continuously"},
            {"text": "A rise and then a fall",
             "correct": False,
             "why": "There is no burst of energy to cause the rise. The "
                    "reaction is taking energy in throughout"},
            {"text": "A fall, as the tube cools and the reaction stops",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c5-02-h10",
        "band": "harder",
        "text": "A carbonate is heated and stops changing colour after five "
                "minutes, though the flame stays on. What is the best "
                "explanation?",
        "options": [
            {"text": "All of the carbonate has decomposed, so there is "
                     "nothing left to react",
             "correct": True},
            {"text": "The tube has reached the temperature at which the "
                     "decomposition stops running, and heating it further "
                     "would only reverse what has already been done",
             "correct": False,
             "why": "A decomposition does not reverse on more heat. What has "
                    "happened is that the carbonate has run out"},
            {"text": "The reaction has become exothermic and no longer needs "
                     "the flame",
             "correct": False,
             "why": "A reaction does not change type partway through. It has "
                    "simply finished"},
            {"text": "The carbon dioxide in the tube is blocking it",
             "correct": False,
             "why": "The gas escapes as it forms. Nothing is blocked"},
        ],
        "figure": None,
    },
]
