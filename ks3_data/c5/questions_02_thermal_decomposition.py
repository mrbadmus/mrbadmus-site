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
            {"text": "It gives energy out into the room around it for the "
                     "whole time that it runs",
             "correct": False,
             "why": "That is the opposite, and it is what combustion and "
                    "displacement do"},
            {"text": "It uses up all of the oxygen that happened to be left "
                     "inside the tube first",
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
            {"text": "That the reaction taking place inside the tube was not a "
                     "decomposition of any kind at all",
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
            {"text": "The whole of the tube's contents at the end of the "
                     "heating, all taken together",
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
            {"text": "Because the compound makes its own supply of air the "
                     "moment it begins to heat up inside the tube",
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
            {"text": "The water in the batter turning into steam in the heat "
                     "of the oven itself",
             "correct": False,
             "why": "That is a change of state and it does help the rise. No "
                    "compound has been broken down"},
            {"text": "The baking powder breaking down and releasing carbon "
                     "dioxide",
             "correct": True},
            {"text": "The sugar on the top of the cake browning as it cooks "
                     "through in the oven",
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

    # ── easier · MRB-338 night-3 top-up ─────────────────────────────────
    #
    # The first thirty rows work almost entirely on the copper carbonate run.
    # These twenty open the other two substances out — limestone's missing
    # colour change, baking soda's third product and the water that condenses
    # in the cool part of the tube — and pick up the terms the page defines in
    # its vocabulary list and then never asks about.
    {
        "id": "c5-02-e11",
        "band": "easier",
        "text": "How would you test a gas to find out whether it is carbon "
                "dioxide?",
        "options": [
            {"text": "Bubble it through limewater and see if it goes milky",
             "correct": True},
            {"text": "Hold it against a cold surface and see if it condenses",
             "correct": False,
             "why": "That would show water vapour. Carbon dioxide stays a gas "
                    "on a cold surface"},
            {"text": "Weigh it and compare the reading with air",
             "correct": False,
             "why": "Plenty of gases are heavier than air. A weighing does not "
                    "name one"},
            {"text": "Smell it carefully from a short distance away from the tube",
             "correct": False,
             "why": "Carbon dioxide has no smell, and smelling a gas in a lab "
                    "identifies nothing"},
        ],
        "figure": None,
    },
    {
        "id": "c5-02-e12",
        "band": "easier",
        "text": "What is limewater?",
        "options": [
            {"text": "Water with quicklime powder floating in it",
             "correct": False,
             "why": "It is a clear liquid with nothing floating in it. The "
                    "cloudiness appears when the gas arrives"},
            {"text": "A clear liquid used to test for carbon dioxide",
             "correct": True},
            {"text": "The water left in the top of a tube after heating",
             "correct": False,
             "why": "That water came out of the substance being heated. "
                    "Limewater is put there on purpose"},
            {"text": "Another name for the gas that comes off a carbonate",
             "correct": False,
             "why": "The gas is carbon dioxide. Limewater is the liquid you "
                    "bubble it through"},
        ],
        "figure": None,
    },
    {
        "id": "c5-02-e13",
        "band": "easier",
        "text": "What colour is copper carbonate before it is heated?",
        "options": [
            {"text": "Black",
             "correct": False,
             "why": "Black is the colour of the copper oxide it leaves behind"},
            {"text": "White",
             "correct": False,
             "why": "White is limestone and baking soda. The copper compound "
                    "is coloured"},
            {"text": "Green",
             "correct": True},
            {"text": "Blue",
             "correct": False,
             "why": "Copper compounds are often blue in solution. This powder "
                    "is green"},
        ],
        "figure": None,
    },
    {
        "id": "c5-02-e14",
        "band": "easier",
        "text": "Copper carbonate is heated until the colour change is "
                "complete. What solid is left in the tube?",
        "options": [
            {"text": "Copper metal",
             "correct": False,
             "why": "The copper does not come out on its own. It is still "
                    "joined to oxygen"},
            {"text": "Copper carbonate that has been darkened by the flame",
             "correct": False,
             "why": "It is not the same substance darkened. It is a different "
                    "compound"},
            {"text": "Soot from the burning gas underneath",
             "correct": False,
             "why": "Nothing from the Bunsen gets inside the tube. The black "
                    "came out of the powder"},
            {"text": "Copper oxide",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c5-02-e15",
        "band": "easier",
        "text": "What do limestone, chalk and marble have in common?",
        "options": [
            {"text": "They are all calcium carbonate",
             "correct": True},
            {"text": "They are all mixtures of several different carbonates",
             "correct": False,
             "why": "They are one compound, which is why all three behave the "
                    "same way on heating"},
            {"text": "They all contain copper too",
             "correct": False,
             "why": "None of them holds any copper. Copper carbonate is a "
                    "different substance"},
            {"text": "They are all formed by heating quicklime strongly",
             "correct": False,
             "why": "Quicklime is what limestone becomes when it is heated, "
                    "not the other way round"},
        ],
        "figure": None,
    },
    {
        "id": "c5-02-e16",
        "band": "easier",
        "text": "Roughly what temperature does a kiln reach to decompose "
                "limestone?",
        "options": [
            {"text": "Around 100 °C",
             "correct": False,
             "why": "That is the boiling point of water. Limestone needs far "
                    "more than that"},
            {"text": "Around 900 °C",
             "correct": True},
            {"text": "Around 300 °C",
             "correct": False,
             "why": "An oven reaches a few hundred degrees and does nothing to "
                    "limestone"},
            {"text": "Around 20 °C",
             "correct": False,
             "why": "That is room temperature. Limestone buildings would not "
                    "last long if so"},
        ],
        "figure": None,
    },
    {
        "id": "c5-02-e17",
        "band": "easier",
        "text": "Which gas is given off when a carbonate is decomposed by "
                "heating?",
        "options": [
            {"text": "Oxygen",
             "correct": False,
             "why": "No oxygen is released. The oxygen in the carbonate stays "
                    "joined to the metal or leaves in the gas"},
            {"text": "Hydrogen",
             "correct": False,
             "why": "There is no hydrogen in a carbonate such as the copper "
                    "one"},
            {"text": "Carbon dioxide",
             "correct": True},
            {"text": "Nitrogen from the air",
             "correct": False,
             "why": "Nitrogen is in the air rather than in the compound, and "
                    "it takes no part"},
        ],
        "figure": None,
    },
    {
        "id": "c5-02-e18",
        "band": "easier",
        "text": "What is a compound?",
        "options": [
            {"text": "Two or more substances stirred together in a jar but never "
                     "joined up",
             "correct": False,
             "why": "That is a mixture, and it can be separated without a "
                    "reaction"},
            {"text": "Anything at all that can be broken down by heating it",
             "correct": False,
             "why": "Plenty of compounds do not decompose on heating, and a "
                    "mixture separates without being one"},
            {"text": "A substance that always gives off a gas when heated",
             "correct": False,
             "why": "Whether it gives off a gas is not what makes it a "
                    "compound"},
            {"text": "A substance made of two or more kinds of atom joined "
                     "together",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c5-02-e19",
        "band": "easier",
        "text": "What is a reactant?",
        "options": [
            {"text": "A substance you start with",
             "correct": True},
            {"text": "A substance you are left with at the end",
             "correct": False,
             "why": "That is a product. Reactants are on the left of the "
                    "equation"},
            {"text": "The energy that has to be supplied to make it go",
             "correct": False,
             "why": "Energy is a condition rather than a substance, and it is "
                    "never a reactant"},
            {"text": "The container the reaction is carried out inside",
             "correct": False,
             "why": "The tube takes no part in the reaction at all"},
        ],
        "figure": None,
    },
    {
        "id": "c5-02-e20",
        "band": "easier",
        "text": "Baking soda is heated in an oven. What does it become?",
        "options": [
            {"text": "Calcium oxide and carbon dioxide, with no water",
             "correct": False,
             "why": "That is what limestone gives, and it gives no water "
                    "either. Baking soda holds sodium rather than calcium"},
            {"text": "Sodium carbonate, carbon dioxide and water",
             "correct": True},
            {"text": "Sodium and carbon dioxide only",
             "correct": False,
             "why": "The sodium stays joined to other atoms. Pure sodium metal "
                    "is not a product"},
            {"text": "Copper oxide and carbon dioxide, as the green powder gives",
             "correct": False,
             "why": "There is no copper anywhere in baking soda, so neither "
                    "of those can form"},
        ],
        "figure": None,
    },
    {
        "id": "c5-02-e21",
        "band": "easier",
        "text": "Why does a thermal decomposition stop as soon as the flame is "
                "taken away?",
        "options": [
            {"text": "Because the tube cools too fast for the products to form",
             "correct": False,
             "why": "It is not about speed of cooling. The reaction has no "
                    "energy supply once the flame goes"},
            {"text": "Because the gas stops escaping once the tube is cool",
             "correct": False,
             "why": "The gas leaves because it is being made. It stops being "
                    "made first"},
            {"text": "Because it needs energy put in the whole time it runs",
             "correct": True},
            {"text": "Because the two products join back together again as it "
                     "cools",
             "correct": False,
             "why": "They do not rejoin. That is the whole point of the "
                    "cooling stage"},
        ],
        "figure": None,
    },
    {
        "id": "c5-02-e22",
        "band": "easier",
        "text": "Which of these substances gives THREE products when it is "
                "decomposed?",
        "options": [
            {"text": "Copper carbonate",
             "correct": False,
             "why": "That gives two: a black solid and a gas"},
            {"text": "Limestone",
             "correct": False,
             "why": "That gives two as well: quicklime and a gas"},
            {"text": "Quicklime",
             "correct": False,
             "why": "Quicklime is a product rather than a starting substance "
                    "here"},
            {"text": "Baking soda",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c5-02-e23",
        "band": "easier",
        "text": "What happens to the mass of the solid in the tube during a "
                "decomposition?",
        "options": [
            {"text": "It falls, because a gas leaves the tube",
             "correct": True},
            {"text": "It rises, because something from the air joins the solid",
             "correct": False,
             "why": "Nothing is added. That is what happens in an oxidation"},
            {"text": "It stays the same, because mass cannot change",
             "correct": False,
             "why": "Mass is conserved overall, and the balance can only weigh "
                    "what stayed in the tube"},
            {"text": "It falls, because the heat itself has a mass of its own",
             "correct": False,
             "why": "Heat weighs nothing. The mass that left did so as a gas"},
        ],
        "figure": None,
    },
    {
        "id": "c5-02-e24",
        "band": "easier",
        "text": "Quicklime is made in kilns in enormous quantities. What is it "
                "used to make?",
        "options": [
            {"text": "Glass",
             "correct": False,
             "why": "Glass is made mainly from sand. Quicklime goes into "
                    "something else"},
            {"text": "Cement",
             "correct": True},
            {"text": "Plastic",
             "correct": False,
             "why": "Plastics are made from oil rather than from rock"},
            {"text": "Steel",
             "correct": False,
             "why": "Steel is made from iron. Quicklime is not what it is "
                    "built from"},
        ],
        "figure": None,
    },
    {
        "id": "c5-02-e25",
        "band": "easier",
        "text": "Baking soda is heated in a test tube and drops of liquid "
                "appear near the open end. What are they?",
        "options": [
            {"text": "Limewater that has been drawn back up the tube",
             "correct": False,
             "why": "Liquid drawn back is a hazard and is not what this is. "
                    "This appears before the flame comes off"},
            {"text": "Melted baking soda that has run up the glass",
             "correct": False,
             "why": "The powder does not melt and run upwards. What travels up "
                    "the tube is a gas"},
            {"text": "Water, condensing where the tube is cool",
             "correct": True},
            {"text": "Carbon dioxide that has turned liquid on the cold glass",
             "correct": False,
             "why": "Carbon dioxide stays a gas at these temperatures. This "
                    "decomposition makes water as well"},
        ],
        "figure": None,
    },
    {
        "id": "c5-02-e26",
        "band": "easier",
        "text": "Limestone stays white the whole way through its "
                "decomposition. What does that show about colour changes?",
        "options": [
            {"text": "That a reaction with no colour change must be a physical "
                     "change",
             "correct": False,
             "why": "Limestone stays white and still makes two new "
                    "substances. Colour decides nothing either way"},
            {"text": "That the limestone has not really decomposed in the kiln "
                     "at all",
             "correct": False,
             "why": "The gas turns limewater milky and the mass falls. It has "
                    "decomposed"},
            {"text": "That colour changes only happen to copper compounds",
             "correct": False,
             "why": "Plenty of substances change colour on heating. The point "
                    "is that a reaction need not"},
            {"text": "That a reaction can happen with no colour change to see",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c5-02-e27",
        "band": "easier",
        "text": "An airbag holds a solid that decomposes in about thirty "
                "milliseconds. Which gas does it make?",
        "options": [
            {"text": "Nitrogen",
             "correct": True},
            {"text": "Carbon dioxide",
             "correct": False,
             "why": "Carbon dioxide is what the carbonates in this lesson "
                    "give. The airbag solid is a different compound"},
            {"text": "Oxygen",
             "correct": False,
             "why": "A bag full of oxygen inside a crashing car would be a "
                    "poor idea, and it is not what forms"},
            {"text": "Hydrogen",
             "correct": False,
             "why": "Hydrogen is flammable, and it is not what the solid "
                    "breaks down into"},
        ],
        "figure": None,
    },
    {
        "id": "c5-02-e28",
        "band": "easier",
        "text": "Why does a cake steam as it comes out of the oven?",
        "options": [
            {"text": "Because the oven air trapped inside it is escaping",
             "correct": False,
             "why": "Air escaping would not be visible. What you can see is "
                    "water vapour"},
            {"text": "Because water is one of the products of the raising "
                     "agent decomposing",
             "correct": True},
            {"text": "Because the carbon dioxide inside it turns white as soon as "
                     "it begins to cool",
             "correct": False,
             "why": "Carbon dioxide stays colourless whatever its temperature"},
            {"text": "Because the sugar in it is boiling away",
             "correct": False,
             "why": "Sugar does not boil out of a cake. The steam is water"},
        ],
        "figure": None,
    },
    {
        "id": "c5-02-e29",
        "band": "easier",
        "text": "In the word equation for a decomposition, how many substances "
                "are written on the left?",
        "options": [
            {"text": "Two, with heat counted as the second of them",
             "correct": False,
             "why": "Heat is a condition rather than a substance and is never "
                    "written in"},
            {"text": "Two, because every reaction has two reactants",
             "correct": False,
             "why": "Having one is exactly what makes a decomposition unusual"},
            {"text": "One",
             "correct": True},
            {"text": "Three, one for each product",
             "correct": False,
             "why": "Three is a count of products rather than reactants. A "
                    "decomposition starts with one substance"},
        ],
        "figure": None,
    },
    {
        "id": "c5-02-e30",
        "band": "easier",
        "text": "How does the heat needed to decompose limestone compare with "
                "the heat needed for copper carbonate?",
        "options": [
            {"text": "About the same, since both are carbonates",
             "correct": False,
             "why": "Both are carbonates and they need very different "
                    "temperatures"},
            {"text": "Less, because limestone is a softer rock",
             "correct": False,
             "why": "How hard a rock is has nothing to do with the "
                    "temperature its compound decomposes at"},
            {"text": "Slightly less than copper carbonate needs",
             "correct": False,
             "why": "It needs far more rather than slightly less, and its "
                    "colour is no guide to the temperature"},
            {"text": "Much more",
             "correct": True},
        ],
        "figure": None,
    },

    # ── standard · MRB-338 night-3 top-up ───────────────────────────────
    {
        "id": "c5-02-s11",
        "band": "standard",
        "text": "4.00 g of limestone is heated in a kiln until it stops losing "
                "mass, and 2.24 g of white solid is left. What mass of gas "
                "escaped?",
        "options": [
            {"text": "1.76 g",
             "correct": True},
            {"text": "2.24 g",
             "correct": False,
             "why": "That is the solid still in the kiln, which escaped "
                    "nowhere"},
            {"text": "6.24 g",
             "correct": False,
             "why": "That adds the two figures. The 2.24 g is part of the "
                    "4.00 g rather than extra to it"},
            {"text": "4.00 g",
             "correct": False,
             "why": "That is everything you started with, and most of it is "
                    "still there as quicklime"},
        ],
        "figure": None,
    },
    {
        "id": "c5-02-s12",
        "band": "standard",
        "text": "Why is the delivery tube lifted out of the limewater BEFORE "
                "the Bunsen is turned off?",
        "options": [
            {"text": "Because the limewater would go milky a second time and "
                     "spoil the result",
             "correct": False,
             "why": "The result is already recorded. What the rule prevents is "
                    "damage to the apparatus"},
            {"text": "Because cold liquid would be drawn back into the hot "
                     "tube and crack it",
             "correct": True},
            {"text": "Because the gas would carry on coming off and be wasted",
             "correct": False,
             "why": "The reaction stops when the heating does, so nothing is "
                    "wasted"},
            {"text": "Because the limewater would boil once the flame stopped",
             "correct": False,
             "why": "Taking the flame away cools things. The danger runs the "
                    "other way, towards the tube"},
        ],
        "figure": None,
    },
    {
        "id": "c5-02-s13",
        "band": "standard",
        "text": "Green copper carbonate in a tube darkens from the bottom "
                "upwards rather than all at once. Why?",
        "options": [
            {"text": "The gas coming off pushes the unreacted powder upwards "
                     "as it goes",
             "correct": False,
             "why": "The powder stays where it is. What moves up the tube is "
                    "the heat"},
            {"text": "The powder at the bottom is a different compound from "
                     "the powder at the top",
             "correct": False,
             "why": "It is all one substance. Only its temperature differs"},
            {"text": "The colour change follows the heat, and the top is not "
                     "hot enough yet",
             "correct": True},
            {"text": "The flame burns the bottom of the powder before the rest",
             "correct": False,
             "why": "Nothing burns. The flame heats the glass, and the heat "
                    "spreads upwards through the powder"},
        ],
        "figure": None,
    },
    {
        "id": "c5-02-s14",
        "band": "standard",
        "text": "Water dropped onto the white solid left after heating "
                "limestone makes it hiss and get hot. What does that show?",
        "options": [
            {"text": "That the white solid is still hot from the kiln and is "
                     "boiling the water off",
             "correct": False,
             "why": "A sample left to go cold for a week does exactly the "
                    "same thing. The heat comes from a reaction"},
            {"text": "That the solid left behind is a new substance, quicklime",
             "correct": True},
            {"text": "That the limestone never decomposed and is still there",
             "correct": False,
             "why": "Water dropped on limestone does nothing at all. This "
                    "solid behaves differently because it IS different"},
            {"text": "That some of the carbon dioxide is still trapped inside "
                     "it",
             "correct": False,
             "why": "The gas left during the heating. The hiss comes from the "
                    "new solid reacting with the water"},
        ],
        "figure": None,
    },
    {
        "id": "c5-02-s15",
        "band": "standard",
        "text": "Baking soda raises a cake inside a closed tin, with no air "
                "reaching the mixture. Why does that work?",
        "options": [
            {"text": "Because the oven air gets in through the cake mixture "
                     "itself",
             "correct": False,
             "why": "Nothing has to get in. The compound comes apart on its "
                    "own once it is hot"},
            {"text": "Because the tin holds enough air inside it to start the "
                     "reaction off",
             "correct": False,
             "why": "No air is needed, however much of it there is"},
            {"text": "Because the reaction needs nothing added, only heat",
             "correct": True},
            {"text": "Because the tin itself supplies oxygen",
             "correct": False,
             "why": "The tin takes no part in the reaction at all"},
        ],
        "figure": None,
    },
    {
        "id": "c5-02-s16",
        "band": "standard",
        "text": "A student heats a carbonate but forgets to set up the "
                "limewater. Which observation still shows a gas came off?",
        "options": [
            {"text": "The mass of the tube and its contents falls",
             "correct": True},
            {"text": "The powder changes colour as it is heated",
             "correct": False,
             "why": "A colour change shows something happened, and it does not "
                    "show that anything left"},
            {"text": "The tube gets hot where the flame is under it",
             "correct": False,
             "why": "The tube would get hot whether anything reacted or not"},
            {"text": "The flame needs to be kept on the whole time",
             "correct": False,
             "why": "That shows the reaction absorbs energy rather than that a "
                    "gas escaped"},
        ],
        "figure": None,
    },
    {
        "id": "c5-02-s17",
        "band": "standard",
        "text": "When baking soda is heated, water condenses in the cool upper "
                "part of the tube AND the limewater goes milky. What does that "
                "tell you?",
        "options": [
            {"text": "That the limewater has been contaminated by the water "
                     "vapour",
             "correct": False,
             "why": "Water added to limewater does nothing you could see. Both "
                    "observations are real"},
            {"text": "That this decomposition gives off two gases rather than "
                     "one",
             "correct": True},
            {"text": "That the tube was wet before the powder went into it",
             "correct": False,
             "why": "A dry tube gives the same result. The water is made by "
                    "the reaction"},
            {"text": "That the carbon dioxide has turned into water further up "
                     "the tube",
             "correct": False,
             "why": "One gas does not turn into another. They are two separate "
                    "products"},
        ],
        "figure": None,
    },
    {
        "id": "c5-02-s18",
        "band": "standard",
        "text": "Copper carbonate decomposes on an ordinary school Bunsen, but "
                "limestone needs a roaring blue flame and a long wait. Why?",
        "options": [
            {"text": "Because limestone is a rock, and a rock conducts heat far "
                     "too badly to be decomposed quickly",
             "correct": False,
             "why": "Grind it to powder and it still needs the higher "
                    "temperature. The compound itself is what differs"},
            {"text": "Because limestone has more carbon dioxide locked inside "
                     "it",
             "correct": False,
             "why": "How much gas comes out does not set the temperature "
                    "needed to start"},
            {"text": "Because the copper compound burns and the limestone does "
                     "not",
             "correct": False,
             "why": "Neither of them burns. Both are broken apart by heat with "
                    "nothing added"},
            {"text": "Because the two compounds need different temperatures to "
                     "come apart",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c5-02-s19",
        "band": "standard",
        "text": "4.00 g of baking soda is heated to constant mass and 2.52 g "
                "of white solid is left. What mass left the tube?",
        "options": [
            {"text": "1.48 g",
             "correct": True},
            {"text": "2.52 g",
             "correct": False,
             "why": "That is the sodium carbonate still in the tube"},
            {"text": "6.52 g",
             "correct": False,
             "why": "That adds the two readings together instead of taking one "
                    "from the other"},
            {"text": "1.48 g of carbon dioxide and nothing else",
             "correct": False,
             "why": "The total is right and the naming is not: water vapour "
                    "left the tube as well"},
        ],
        "figure": None,
    },
    {
        "id": "c5-02-s20",
        "band": "standard",
        "text": "Which is the better signal that a decomposition has finished: "
                "the colour settling, or the mass settling?",
        "options": [
            {"text": "The colour, because you can watch it happen without any "
                     "apparatus",
             "correct": False,
             "why": "Easy to watch is not the same as reliable. Limestone "
                    "never changes colour"},
            {"text": "Neither, because a decomposition carries on for as long "
                     "as it is heated",
             "correct": False,
             "why": "It stops when the compound runs out, which is why the "
                    "mass settles"},
            {"text": "The mass, because it works even where there is no colour "
                     "change",
             "correct": True},
            {"text": "The colour, because the mass keeps falling even after "
                     "the reaction ends",
             "correct": False,
             "why": "Once the reaction ends nothing more leaves, so the "
                    "reading holds steady"},
        ],
        "figure": None,
    },
    {
        "id": "c5-02-s21",
        "band": "standard",
        "text": "A cement works releases carbon dioxide from the limestone "
                "itself. Where does the REST of its carbon dioxide come from?",
        "options": [
            {"text": "From the quicklime reacting with the air as it cools",
             "correct": False,
             "why": "Cooling quicklime is not where the extra gas comes from. "
                    "Look at what heats the kiln"},
            {"text": "From the fuel burned to heat the kilns",
             "correct": True},
            {"text": "From the cement giving the gas back off as it sets",
             "correct": False,
             "why": "Setting cement releases no carbon dioxide. The emissions "
                    "happen at the kiln"},
            {"text": "From quarrying and crushing the rock",
             "correct": False,
             "why": "Crushing is a physical change and makes no gas of its "
                    "own"},
        ],
        "figure": None,
    },
    {
        "id": "c5-02-s22",
        "band": "standard",
        "text": "Why does a thermal decomposition take energy IN, when "
                "combustion gives energy out?",
        "options": [
            {"text": "Because the tube is cold and has to be warmed before "
                     "anything can happen inside it",
             "correct": False,
             "why": "Warming the glass is not the reaction. Energy goes on "
                    "being absorbed after everything is hot"},
            {"text": "Because the gas produced carries the energy away with it "
                     "as it leaves",
             "correct": False,
             "why": "The energy is used inside the reaction. It is not being "
                    "carried off by a product"},
            {"text": "Because energy has to be supplied to break the compound "
                     "apart",
             "correct": True},
            {"text": "Because the products are colder than the reactant was",
             "correct": False,
             "why": "Everything in the tube is at the same temperature. The "
                    "energy goes into breaking joins"},
        ],
        "figure": None,
    },
    {
        "id": "c5-02-s23",
        "band": "standard",
        "text": "One tube of a carbonate and one tube of water are both "
                "heated, and a gas comes off each. Why is only one of them a "
                "decomposition?",
        "options": [
            {"text": "Because the water was already a liquid and a "
                     "decomposition needs a solid to start with",
             "correct": False,
             "why": "The state of the reactant does not decide it. Nothing new "
                    "is made when water boils"},
            {"text": "Because the gas from the water leaves no solid behind in "
                     "the tube",
             "correct": False,
             "why": "A decomposition need not leave a solid. What matters is "
                    "whether new substances were made"},
            {"text": "Because the carbonate needed a hotter flame than the "
                     "water did",
             "correct": False,
             "why": "How much heat is needed is a fact about the substance, "
                    "not about the kind of change"},
            {"text": "Because the water only changed state, so no new "
                     "substance was made",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c5-02-s24",
        "band": "standard",
        "text": "Chalk from a cliff, marble from a statue and limestone from a "
                "quarry are each heated to 900 °C. What do you predict?",
        "options": [
            {"text": "All three decompose to quicklime and carbon dioxide",
             "correct": True},
            {"text": "Only the limestone, because kilns are built for it",
             "correct": False,
             "why": "A kiln is fed limestone because it is cheap to quarry, "
                    "not because the others behave differently"},
            {"text": "Only the chalk decomposes, because it is the softest of "
                     "the three",
             "correct": False,
             "why": "Hardness is a physical property and does not decide what "
                    "heat does to a compound"},
            {"text": "None of them decomposes, because they are natural rocks "
                     "rather than laboratory chemicals",
             "correct": False,
             "why": "Where a substance came from changes nothing about its "
                    "chemistry"},
        ],
        "figure": None,
    },
    {
        "id": "c5-02-s25",
        "band": "standard",
        "text": "Two unlabelled jars hold copper carbonate and copper oxide. "
                "How could you tell which is which without heating either?",
        "options": [
            {"text": "Weigh equal volumes and take the heavier one as the "
                     "oxide",
             "correct": False,
             "why": "You have nothing to compare a reading against, and the "
                    "difference is not what the eye is for here"},
            {"text": "Bubble the air above each one through limewater",
             "correct": False,
             "why": "Neither gives off any gas while it sits in a jar"},
            {"text": "Look at them: the carbonate is green and the oxide is "
                     "black",
             "correct": True},
            {"text": "Add water and see which one dissolves",
             "correct": False,
             "why": "Neither dissolves, so nothing separates them that way"},
        ],
        "figure": None,
    },
    {
        "id": "c5-02-s26",
        "band": "standard",
        "text": "A tube of copper carbonate is heated briefly and the mass "
                "falls by about half of what was expected. What is the most "
                "likely reason?",
        "options": [
            {"text": "Some of the mass was destroyed by the heat",
             "correct": False,
             "why": "Nothing is ever destroyed. Every atom is still somewhere"},
            {"text": "The balance was reading low before the tube was heated",
             "correct": False,
             "why": "A balance reading low at the start would make the loss "
                    "look bigger rather than smaller"},
            {"text": "Half of the carbon dioxide dissolved in the limewater "
                     "and half did not",
             "correct": False,
             "why": "Where the gas ends up does not change how much left the "
                    "tube"},
            {"text": "Only part of the powder has decomposed so far",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c5-02-s27",
        "band": "standard",
        "text": "Both copper carbonate and calcium carbonate are carbonates, "
                "yet one decomposes far more easily than the other. What does "
                "that tell you?",
        "options": [
            {"text": "That different compounds need different amounts of "
                     "energy to come apart",
             "correct": True},
            {"text": "That only one of the two is really a carbonate at all",
             "correct": False,
             "why": "Both are carbonates, and both give off carbon dioxide"},
            {"text": "That the easier one of the two is a mixture rather than a "
                     "compound, which is why it comes apart",
             "correct": False,
             "why": "Both are compounds. A mixture would separate without any "
                    "reaction"},
            {"text": "That the harder one is being heated the wrong way",
             "correct": False,
             "why": "It decomposes perfectly well in a kiln. It simply needs a "
                    "higher temperature"},
        ],
        "figure": None,
    },
    {
        "id": "c5-02-s28",
        "band": "standard",
        "text": "4.00 g of copper carbonate leaves 2.58 g of copper oxide. "
                "What mass of copper oxide would 6.00 g leave?",
        "options": [
            {"text": "2.58 g, because that is what this reaction always gives",
             "correct": False,
             "why": "More carbonate gives more oxide. The figure is not fixed"},
            {"text": "3.87 g",
             "correct": True},
            {"text": "4.42 g",
             "correct": False,
             "why": "That adds the extra 2.00 g of carbonate straight on as "
                    "though none of it left as gas"},
            {"text": "6.00 g, because mass is conserved in every reaction",
             "correct": False,
             "why": "Mass is conserved, and some of it leaves the tube as "
                    "carbon dioxide"},
        ],
        "figure": None,
    },
    {
        "id": "c5-02-s29",
        "band": "standard",
        "text": "Thermal decomposition is described as running BACKWARDS "
                "compared with the other reaction types. What does that "
                "mean?",
        "options": [
            {"text": "That it can be reversed simply by cooling the tube down "
                     "again afterwards",
             "correct": False,
             "why": "It does not reverse at all. Backwards here describes the "
                    "shape of the equation"},
            {"text": "That the products are written on the left of the arrow",
             "correct": False,
             "why": "Products are always on the right. What differs is how "
                    "many there are"},
            {"text": "That one substance comes apart instead of substances "
                     "joining",
             "correct": True},
            {"text": "That it gives out energy instead of taking energy in",
             "correct": False,
             "why": "It takes energy in. That is the opposite of what this "
                    "option says"},
        ],
        "figure": None,
    },
    {
        "id": "c5-02-s30",
        "band": "standard",
        "text": "Copper carbonate, limestone and baking soda all decompose "
                "on heating. Which is the best choice for showing a class in "
                "one lesson, and why?",
        "options": [
            {"text": "Limestone, because it is the one used industrially",
             "correct": False,
             "why": "Being important is not the same as being practical. It "
                    "needs a temperature a school Bunsen struggles to reach"},
            {"text": "Baking soda, because everyone has seen it in a kitchen",
             "correct": False,
             "why": "It works, and it gives nothing to watch: a white powder "
                    "stays a white powder"},
            {"text": "Any of the three, because the apparatus and the method are "
                     "identical whichever one you choose",
             "correct": False,
             "why": "The apparatus is the same and the temperature needed is "
                    "not"},
            {"text": "Copper carbonate, because an ordinary Bunsen decomposes "
                     "it and the colour change is easy to see",
             "correct": True},
        ],
        "figure": None,
    },

    # ── harder · MRB-338 night-3 top-up ─────────────────────────────────
    {
        "id": "c5-02-h11",
        "band": "harder",
        "text": "4.00 g of copper carbonate leaves 2.58 g of solid, and 4.00 g "
                "of limestone leaves 2.24 g. Which loses the greater share of "
                "its mass, and what does that suggest?",
        "options": [
            {"text": "The limestone, so a larger share of its mass was carbon "
                     "dioxide",
             "correct": True},
            {"text": "The copper carbonate, because copper is the heavier "
                     "metal of the two",
             "correct": False,
             "why": "It loses 1.42 g against the limestone's 1.76 g, so it "
                    "loses less from the same starting mass"},
            {"text": "Both the same, because both started at 4.00 g",
             "correct": False,
             "why": "They started the same and finished differently, which is "
                    "the whole comparison"},
            {"text": "The copper carbonate, because it changes colour while the "
                     "limestone does not",
             "correct": False,
             "why": "A colour change says nothing about mass. The losses are "
                    "1.42 g against 1.76 g from the same 4.00 g"},
        ],
        "figure": None,
    },
    {
        "id": "c5-02-h12",
        "band": "harder",
        "text": "An airbag must fire in a crash and must not fire in a car "
                "parked in the sun. What does that require of the solid inside "
                "it?",
        "options": [
            {"text": "That it decomposes slowly, so a hot afternoon is not "
                     "long enough to set it off",
             "correct": False,
             "why": "A slow reaction would be useless in a crash. It has to be "
                    "extremely fast when it goes"},
            {"text": "That it stays put at any temperature a parked car reaches",
             "correct": True},
            {"text": "That it needs oxygen, kept out until the crash",
             "correct": False,
             "why": "A decomposition needs nothing added. That is part of why "
                    "it was chosen"},
            {"text": "That it reverses on cooling, so any gas made in the heat "
                     "goes back in",
             "correct": False,
             "why": "A decomposition does not reverse. If it fired once it "
                    "would stay fired"},
        ],
        "figure": None,
    },
    {
        "id": "c5-02-h13",
        "band": "harder",
        "text": "A student heats baking soda and finds the tube has lost more "
                "mass than the carbon dioxide alone could account for. "
                "Explain.",
        "options": [
            {"text": "Some of the solid was blown out of the tube by the gas "
                     "escaping",
             "correct": False,
             "why": "Nothing is blown out of a tube heated gently. There is a "
                    "second product"},
            {"text": "The balance drifts a little when it is weighing something "
                     "hot",
             "correct": False,
             "why": "The tube is weighed cool. The extra loss is a real "
                    "product"},
            {"text": "Water vapour left the tube as well as carbon dioxide",
             "correct": True},
            {"text": "Some of the mass was converted into the energy the "
                     "reaction absorbed",
             "correct": False,
             "why": "This reaction takes energy in, and energy is not made of "
                    "matter in any case"},
        ],
        "figure": None,
    },
    {
        "id": "c5-02-h14",
        "band": "harder",
        "text": "Limestone shows no colour change at all as it decomposes. "
                "What evidence is there that anything happened?",
        "options": [
            {"text": "The lump glows while it is in the flame",
             "correct": False,
             "why": "Anything glows if it is hot enough. Glowing is not "
                    "evidence of a reaction"},
            {"text": "The flame has to be kept under the lump for a very long "
                     "time before anything changes",
             "correct": False,
             "why": "That shows energy is being supplied, and a lump of iron "
                    "would take a long time too"},
            {"text": "The lump crumbles slightly as it is heated",
             "correct": False,
             "why": "Plenty of rocks crumble when heated without any reaction "
                    "at all"},
            {"text": "The gas coming off turns limewater milky and the mass "
                     "falls",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c5-02-h15",
        "band": "harder",
        "text": "Quicklime is delivered in sealed bags and spoils if the bags "
                "are left open in a damp shed. Suggest why.",
        "options": [
            {"text": "It reacts with water, and there is water in damp air",
             "correct": True},
            {"text": "It decomposes further once it is out of the kiln",
             "correct": False,
             "why": "It is already the product of a decomposition and does not "
                    "carry on breaking down in a shed"},
            {"text": "It absorbs the carbon monoxide given off by machinery",
             "correct": False,
             "why": "Carbon monoxide is not what spoils it, and a shed is not "
                    "full of it"},
            {"text": "It turns back into limestone as it cools",
             "correct": False,
             "why": "The decomposition does not reverse on cooling. What "
                    "reaches it in a damp shed is water"},
        ],
        "figure": None,
    },
    {
        "id": "c5-02-h16",
        "band": "harder",
        "text": "A combustion and a decomposition can both be run with a "
                "Bunsen and both can give off a gas. Name the one test that "
                "separates them every time.",
        "options": [
            {"text": "Whether the reaction gives off a gas that turns "
                     "limewater milky",
             "correct": False,
             "why": "Burning a hydrocarbon gives carbon dioxide too, so the "
                    "test cannot separate them"},
            {"text": "Whether anything had to be added to the substance being "
                     "heated",
             "correct": True},
            {"text": "Whether the substance changes colour while it is being "
                     "heated",
             "correct": False,
             "why": "Limestone decomposes with no colour change, and plenty of "
                    "things char when they burn"},
            {"text": "Whether a flame can be seen coming from the substance "
                     "itself",
             "correct": False,
             "why": "Charcoal burns with hardly any flame, and no decomposition "
                    "here gives one"},
        ],
        "figure": None,
    },
    {
        "id": "c5-02-h17",
        "band": "harder",
        "text": "Baking soda gives three products and copper carbonate gives "
                "two. Does that break the rule that a decomposition gives two "
                "or more?",
        "options": [
            {"text": "Yes, because three products means two separate reactions "
                     "have run",
             "correct": False,
             "why": "One compound came apart once. How many pieces it came "
                    "apart into is not a count of reactions"},
            {"text": "Yes, because the rule describes exactly two products and "
                     "no more",
             "correct": False,
             "why": "It says two OR MORE, which is what makes room for the "
                    "third"},
            {"text": "No, because two or more includes three",
             "correct": True},
            {"text": "No, the water is just a leftover",
             "correct": False,
             "why": "The water is made by the reaction, so it is a product "
                    "like the others"},
        ],
        "figure": None,
    },
    {
        "id": "c5-02-h18",
        "band": "harder",
        "text": "A student says a reaction cannot be a thermal decomposition "
                "unless a gas comes off. Is that right?",
        "options": [
            {"text": "Yes, because a gas escaping is what makes the mass fall",
             "correct": False,
             "why": "The mass falling is a consequence in these three cases "
                    "rather than part of the definition"},
            {"text": "Yes, because every decomposition you have met gave one off",
             "correct": False,
             "why": "Three examples do not make a rule. All three happen to be "
                    "carbonates"},
            {"text": "No, because a decomposition producing no gas would be far "
                     "too slow for anybody to notice it happening",
             "correct": False,
             "why": "Speed has nothing to do with it. The definition simply "
                    "does not mention a gas"},
            {"text": "No, because the definition asks only for one compound "
                     "broken into two or more substances",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c5-02-h19",
        "band": "harder",
        "text": "Copper carbonate is decomposed inside a sealed tube that had "
                "its air pumped out, and the pressure inside rises. Explain.",
        "options": [
            {"text": "A gas is being made from a solid, and it has nowhere to "
                     "go",
             "correct": True},
            {"text": "The air pumped out is leaking slowly back in as the tube "
                     "heats",
             "correct": False,
             "why": "A sealed tube does not refill itself. The gas inside was "
                    "made by the reaction"},
            {"text": "Heating always raises the pressure, whatever is in the "
                     "tube",
             "correct": False,
             "why": "Heating an empty sealed tube raises it barely at all. "
                    "Here a new gas is appearing"},
            {"text": "The black solid takes up more room than the green powder "
                     "did",
             "correct": False,
             "why": "A solid changing volume slightly would not build "
                    "pressure. A gas being made does"},
        ],
        "figure": None,
    },
    {
        "id": "c5-02-h20",
        "band": "harder",
        "text": "Baking soda thrown onto a small pan fire helps to put it "
                "out. Explain how.",
        "options": [
            {"text": "It melts into a layer that seals the surface of the pan",
             "correct": False,
             "why": "It decomposes rather than melting, and the gas it makes "
                    "is what does the work"},
            {"text": "It decomposes in the heat, and the carbon dioxide it "
                     "releases keeps air off the fuel",
             "correct": True},
            {"text": "It absorbs the heat of the fire until the fuel is too "
                     "cool to burn",
             "correct": False,
             "why": "It does absorb energy, and a spoonful could not cool a "
                    "pan fire. The gas is what matters"},
            {"text": "It reacts with the burning oil and turns it into a "
                     "substance that cannot catch fire again",
             "correct": False,
             "why": "It does not react with the oil at all. It comes apart on "
                    "its own"},
        ],
        "figure": None,
    },
    {
        "id": "c5-02-h21",
        "band": "harder",
        "text": "Two students heat identical masses of the same carbonate, one "
                "for two minutes and one for ten. Their final masses differ. "
                "Whose result should the class use?",
        "options": [
            {"text": "The two-minute one, because a shorter heating leaves less "
                     "chance of anything going wrong with it",
             "correct": False,
             "why": "A short heating leaves the reaction unfinished, which is "
                    "the error"},
            {"text": "Neither, because two results that differ cannot be "
                     "trusted at all",
             "correct": False,
             "why": "They differ for a reason you can name, and naming it is "
                    "what settles which to use"},
            {"text": "The average of the two, because that is what you do with "
                     "repeats",
             "correct": False,
             "why": "These are not repeats. One reaction finished and one did "
                    "not"},
            {"text": "The ten-minute one, because heating to constant mass is "
                     "what shows the reaction has finished",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c5-02-h22",
        "band": "harder",
        "text": "The reaction does not reverse on cooling. What would have to "
                "be true for it to reverse?",
        "options": [
            {"text": "The products would have to meet and react together "
                     "again, and one of them has left the tube",
             "correct": True},
            {"text": "The tube would have to be cooled a very long way below "
                     "room temperature and then left there",
             "correct": False,
             "why": "Cooling further puts no energy in and brings nothing "
                    "back. Temperature is not the obstacle"},
            {"text": "The reaction would have to have been a physical change "
                     "in the first place",
             "correct": False,
             "why": "Then it would not have been this reaction at all. The "
                    "question is what reversing would need"},
            {"text": "The flame would have to be left on for longer before it "
                     "was removed",
             "correct": False,
             "why": "More heating drives it further forwards rather than "
                    "backwards"},
        ],
        "figure": None,
    },
    {
        "id": "c5-02-h23",
        "band": "harder",
        "text": "Suppose a cake rose because the air in the mixture expanded "
                "in the heat, rather than because of a decomposition. What "
                "would you expect as it cooled?",
        "options": [
            {"text": "It would sink back down again",
             "correct": True},
            {"text": "It would rise further still",
             "correct": False,
             "why": "Cooling air contracts. Nothing would go on expanding once "
                    "the heat was removed"},
            {"text": "It would stay exactly as it was, because air that has "
                     "expanded cannot contract again",
             "correct": False,
             "why": "Air contracts as it cools, in just the way it expanded "
                    "as it was heated"},
            {"text": "It would collapse and then rise a second time as it "
                     "reached room temperature",
             "correct": False,
             "why": "There is nothing to make it rise a second time once it is "
                    "cooling"},
        ],
        "figure": None,
    },
    {
        "id": "c5-02-h24",
        "band": "harder",
        "text": "A student writes: copper carbonate + heat makes copper oxide "
                "+ carbon dioxide. What is wrong with that equation?",
        "options": [
            {"text": "The arrow is pointing the wrong way for a decomposition",
             "correct": False,
             "why": "The arrow is the right way round. The reactant is on the "
                    "left and the products on the right"},
            {"text": "Heat is not a substance, so it does not belong on the "
                     "left",
             "correct": True},
            {"text": "Copper oxide and carbon dioxide should be on the left "
                     "together",
             "correct": False,
             "why": "They are the products, so the right is where they go"},
            {"text": "Nothing is wrong, because the heat has to be shown "
                     "somewhere",
             "correct": False,
             "why": "It is shown by saying the mixture is heated, never as a "
                    "reactant in the equation"},
        ],
        "figure": None,
    },
    {
        "id": "c5-02-h25",
        "band": "harder",
        "text": "A company wants a reaction for a hand-warmer that gets hot "
                "when it is squeezed. Why is a thermal decomposition the wrong "
                "choice?",
        "options": [
            {"text": "Because it would need a gas supply, which a packet "
                     "cannot carry",
             "correct": False,
             "why": "It needs nothing added at all. The problem is the energy, "
                    "not the reactants"},
            {"text": "Because it would reverse as soon as the packet started "
                     "to cool",
             "correct": False,
             "why": "A decomposition does not reverse. The problem is which "
                    "way the energy goes"},
            {"text": "Because it takes energy in, so it would make the packet "
                     "colder",
             "correct": True},
            {"text": "Because it would be far too slow to be any use in a "
                     "pocket",
             "correct": False,
             "why": "An airbag decomposition runs in thirty milliseconds. "
                    "Speed is not the obstacle"},
        ],
        "figure": None,
    },
    {
        "id": "c5-02-h26",
        "band": "harder",
        "text": "A student says a decomposition LOSES mass. Which rewording "
                "makes the claim correct?",
        "options": [
            {"text": "The reaction loses mass, and the gas gains it back",
             "correct": False,
             "why": "A gas gaining what a reaction lost is still saying mass "
                    "moved into and out of existence"},
            {"text": "The tube loses mass, because one of the products leaves "
                     "it",
             "correct": True},
            {"text": "The compound loses mass as it is broken apart by the "
                     "heat",
             "correct": False,
             "why": "The atoms that were in the compound are all still there, "
                    "spread between two products"},
            {"text": "The mass is lost to the energy the reaction takes in",
             "correct": False,
             "why": "Energy is not made of matter and cannot account for a "
                    "balance reading"},
        ],
        "figure": None,
    },
    {
        "id": "c5-02-h27",
        "band": "harder",
        "text": "4.00 g of copper carbonate leaves 2.58 g of copper oxide. A "
                "technician needs 5.16 g of copper oxide. What mass of "
                "carbonate should be weighed out?",
        "options": [
            {"text": "5.16 g, because the oxide and the carbonate weigh the "
                     "same",
             "correct": False,
             "why": "They do not. The carbonate is heavier, because it still "
                    "holds the gas"},
            {"text": "2.58 g",
             "correct": False,
             "why": "That is the oxide from a 4.00 g sample, so it is half of "
                    "what is wanted"},
            {"text": "8.00 g",
             "correct": True},
            {"text": "10.32 g, which is 5.16 g doubled to allow for the gas",
             "correct": False,
             "why": "Doubling overshoots. 5.16 g is twice 2.58 g, so twice "
                    "4.00 g of carbonate is needed"},
        ],
        "figure": None,
    },
    {
        "id": "c5-02-h28",
        "band": "harder",
        "text": "A jar holds a mixture of green copper carbonate and black "
                "copper oxide. The whole mixture is heated and turns entirely "
                "black. What has happened?",
        "options": [
            {"text": "Both substances have decomposed, leaving one black solid "
                     "behind",
             "correct": False,
             "why": "The oxide is already a product of the decomposition and "
                    "has nothing left to lose"},
            {"text": "The oxide has coated the carbonate and hidden its "
                     "colour",
             "correct": False,
             "why": "A powder does not coat another powder. The green has gone "
                    "because it reacted"},
            {"text": "Only the carbonate decomposed; the oxide was already a "
                     "product",
             "correct": True},
            {"text": "The two have joined to make a single new black compound",
             "correct": False,
             "why": "Nothing joined. One of the two came apart and the other "
                    "sat there"},
        ],
        "figure": None,
    },
    {
        "id": "c5-02-h29",
        "band": "harder",
        "text": "A melted chocolate bar sets again as it cools, but a baked "
                "cake never becomes batter. Explain the difference.",
        "options": [
            {"text": "The cake is hotter than the chocolate, so it cannot go "
                     "back",
             "correct": False,
             "why": "Both cool to the same room. Temperature is not what "
                    "decides it"},
            {"text": "The chocolate never changed in any lasting way, and the "
                     "cake was simply damaged by the heat of the oven",
             "correct": False,
             "why": "Damaged is not a chemical description. The cake's raising "
                    "agent decomposed, which is a reaction"},
            {"text": "The cake lost a gas to the air and the chocolate did "
                     "not",
             "correct": False,
             "why": "Losing a gas is part of it and not the heart of it. The "
                    "chocolate only melted"},
            {"text": "Melting is a physical change and the cake's raising "
                     "agent decomposed, which is a chemical one",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c5-02-h30",
        "band": "harder",
        "text": "Why can a cement works not simply keep the carbon dioxide "
                "inside the rock and make quicklime anyway?",
        "options": [
            {"text": "Because the gas leaving is what turns the limestone into "
                     "quicklime",
             "correct": True},
            {"text": "Because the gas would build up pressure and burst the "
                     "kiln",
             "correct": False,
             "why": "Kilns are open. The real point is that keeping the gas in "
                    "means keeping the limestone"},
            {"text": "Because the gas has to be sold to make the process pay "
                     "for itself",
             "correct": False,
             "why": "That is an argument about money rather than about the "
                    "reaction"},
            {"text": "Because quicklime is made from the gas rather than from "
                     "the solid",
             "correct": False,
             "why": "Quicklime is the solid left behind. The gas is what goes "
                    "away"},
        ],
        "figure": None,
    },
]
