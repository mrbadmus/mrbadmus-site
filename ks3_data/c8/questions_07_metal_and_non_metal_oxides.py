"""C8 lesson 07 — Metal and non-metal oxides: twelve questions (MRB-281).

The lesson's argument is one shape: which side of the periodic table an element
came from decides which way its oxide takes the water on the pH scale. The page
teaches it with a six-oxide bench and two beakers, and it spends most of its
length on the two places the famous version of that rule breaks.

These twelve probe the angles the mastery ladder leaves alone: what the word
`oxide` covers, what a pH reading is actually a measurement OF, what the acid
test can find that the water test cannot, and where the two-sided rule runs out.

The distractors are built from the lesson's three declared misconceptions.

`PTAB-11` (alkaline and basic mean the same thing) drives the wrong options in
e02, s01, s03 and h01. Each treats a pH reading as a verdict on what a substance
IS rather than a report on what is dissolved. h01 is the one that matters: it
puts the acid test and the water test side by side on the same solid, so the
belief has to explain why the two disagree and cannot.

`PTAB-12` (if it does not move the pH it is not a base) drives e03, s02 and h03,
where an unmoved reading is read as a negative result. h03 is the register's own
case put as a laboratory decision, which is where a student actually meets it.

`PTAB-13` (all oxides dissolve) drives e04, s04 and h04. The bench holds two
that dissolve completely, one that dissolves a little, one that does not
dissolve at all and two that are not solids in the first place, so the belief is
contradicted six ways on the page and is worth asking about directly.

A fourth strand, on the page and in none of the three register entries, is that
a rule can have a boundary without having a hole: e01 and h02 are built on the
staircase elements and on water, both of which qualify the two-sided rule
without overturning it (MRB-225).

⚠️ MRB-278 · ANSWER POSITION. The correct answer's index cycles 0, 1, 2, 3
through each band, so this file holds three of each.

⚠️ BAND VALUES ARE FULL WORDS — see `questions_01_metals_and_non_metals.py`.
"""

UNIT = "C8"
LESSON = "metal-and-non-metal-oxides"
LESSON_NUMBER = 7

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "c8-07-e01",
        "band": "easier",
        "text": "What is an oxide?",
        "options": [
            {"text": "An element that has joined with oxygen",
             "correct": True},
            {"text": "Any substance that turns universal indicator red",
             "correct": False,
             "why": "That describes an acid. Calcium oxide is an oxide and it "
                    "turns the indicator purple."},
            {"text": "A gas given off whenever something is burned",
             "correct": False,
             "why": "Magnesium oxide is a white solid. An oxide can be a "
                    "solid, a liquid or a gas."},
            {"text": "A metal that has been left out in the air too long",
             "correct": False,
             "why": "Non-metals form oxides too — carbon dioxide is one, and "
                    "so is water."},
        ],
        "figure": None,
    },
    {
        "id": "c8-07-e02",
        "band": "easier",
        "text": "Magnesium oxide is stirred into water and the pH reads 10. "
                "What word describes that solution?",
        "options": [
            {"text": "Acidic, because a solid was added to it",
             "correct": False,
             "why": "Adding a solid says nothing about the direction. It is "
                    "the reading that decides, and 10 is above 7."},
            {"text": "Alkaline, because the reading is above 7",
             "correct": True},
            {"text": "Neutral, because magnesium oxide is a metal oxide",
             "correct": False,
             "why": "Neutral is exactly 7. Metal oxides that dissolve go "
                    "above it."},
            {"text": "Acidic, because every oxide dissolves to give an acid",
             "correct": False,
             "why": "Only non-metal oxides do that. Magnesium is a metal."},
        ],
        "figure": None,
    },
    {
        "id": "c8-07-e03",
        "band": "easier",
        "text": "What does a base do to an acid?",
        "options": [
            {"text": "It makes the acid stronger",
             "correct": False,
             "why": "It does the opposite — it uses the acid up."},
            {"text": "It dissolves in it without changing at all",
             "correct": False,
             "why": "Something new is made. Copper oxide plus sulfuric acid "
                    "gives blue copper sulfate."},
            {"text": "It reacts with it to make a salt and water",
             "correct": True},
            {"text": "Nothing, unless the base has already dissolved in water",
             "correct": False,
             "why": "Copper oxide will not dissolve and still reacts with "
                    "acid. That is the whole of the lesson."},
        ],
        "figure": None,
    },
    {
        "id": "c8-07-e04",
        "band": "easier",
        "text": "Six oxides were put into water. Two dissolved completely, one "
                "dissolved a little, one did not dissolve at all and two were "
                "gases. What does that show about oxides?",
        "options": [
            {"text": "That only gases are really oxides",
             "correct": False,
             "why": "Calcium oxide and copper oxide are solids and both are "
                    "oxides."},
            {"text": "That an oxide has to dissolve before it is an oxide",
             "correct": False,
             "why": "Copper oxide dissolved in none of it and is still an "
                    "oxide."},
            {"text": "That water can only hold a certain number of oxides",
             "correct": False,
             "why": "Each beaker held one oxide. How much dissolves depends on "
                    "the substance, not on a limit."},
            {"text": "That being an oxide says nothing about whether it "
                     "dissolves",
             "correct": True},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "c8-07-s01",
        "band": "standard",
        "text": "What is a pH reading actually a measurement of?",
        "options": [
            {"text": "What is dissolved in the solution being tested",
             "correct": True},
            {"text": "How much solid was tipped into the beaker",
             "correct": False,
             "why": "A whole spatula of copper oxide moves the reading no "
                    "further than a pinch does, because almost none of it "
                    "goes in."},
            {"text": "Whether the substance is a metal or a non-metal",
             "correct": False,
             "why": "Copper oxide and water both read 7 and one is a metal "
                    "oxide."},
            {"text": "How strongly the substance would react with an acid",
             "correct": False,
             "why": "Copper oxide reacts readily with acid and its reading "
                    "never moves at all."},
        ],
        "figure": None,
    },
    {
        "id": "c8-07-s02",
        "band": "standard",
        "text": "A student says copper oxide cannot be a base because the pH "
                "stayed at 7. What is the one test that settles it?",
        "options": [
            {"text": "Leave it in the water overnight and read the pH again",
             "correct": False,
             "why": "Time does not make an insoluble solid dissolve. The "
                    "reading is the same in the morning."},
            {"text": "Add it to an acid and see whether a salt and water form",
             "correct": True},
            {"text": "Grind it finer, so more of it fits into the same beaker",
             "correct": False,
             "why": "Grinding speeds a reaction up; it does not make an "
                    "insoluble solid soluble."},
            {"text": "Warm the water, because a warm solution reads higher",
             "correct": False,
             "why": "Warming does not turn a solid that will not dissolve "
                    "into one that will."},
        ],
        "figure": None,
    },
    {
        "id": "c8-07-s03",
        "band": "standard",
        "text": "Copper oxide and water were both put into beakers and both "
                "read pH 7. Why is that the same number for two different "
                "reasons?",
        "options": [
            {"text": "Because the copper oxide beaker had not been stirred "
                     "enough",
             "correct": False,
             "why": "Stirring does not help. Copper oxide is insoluble however "
                    "long you stir it."},
            {"text": "Because both of them are neutral substances",
             "correct": False,
             "why": "Water is neutral. Copper oxide is a base, and the reading "
                    "simply cannot see it."},
            {"text": "Because water is neutral, and the copper oxide never "
                     "dissolved",
             "correct": True},
            {"text": "Because 7 is what any solid gives when it is added to "
                     "water",
             "correct": False,
             "why": "Calcium oxide is a solid and it took the same water to "
                    "12."},
        ],
        "figure": None,
    },
    {
        "id": "c8-07-s04",
        "band": "standard",
        "text": "Calcium oxide took the water to pH 12 and magnesium oxide "
                "took it only to pH 10. Both are metal oxides. What explains "
                "the difference?",
        "options": [
            {"text": "Magnesium oxide is an acidic oxide and calcium oxide is "
                     "not",
             "correct": False,
             "why": "Both are metal oxides and both are bases. Neither is "
                    "acidic."},
            {"text": "Calcium is further down group 2, so its oxide is a "
                     "stronger acid",
             "correct": False,
             "why": "Neither oxide is an acid. Position is not what is being "
                    "asked about here."},
            {"text": "Magnesium oxide was tested in colder water than the "
                     "calcium oxide",
             "correct": False,
             "why": "Both beakers held the same water. The difference is in "
                    "the substances."},
            {"text": "Much more of the calcium oxide dissolved, so there was "
                     "more of it in solution",
             "correct": True},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "c8-07-h01",
        "band": "harder",
        "text": "The same black powder leaves the pH at 7 in one test and "
                "produces a blue salt in another. Which pair of words describes "
                "it correctly?",
        "options": [
            {"text": "Basic, but never alkaline",
             "correct": True},
            {"text": "Alkaline, but never basic",
             "correct": False,
             "why": "It is the wrong way round. Alkaline describes a solution, "
                    "and this one never made one."},
            {"text": "Neutral, and therefore also a base",
             "correct": False,
             "why": "Neutral describes the solution the powder sat in, not the "
                    "powder. The two are not the same thing."},
            {"text": "Acidic in water and basic in acid",
             "correct": False,
             "why": "Nothing behaves as an acid in one beaker and a base in "
                    "the next. It was a base in both."},
        ],
        "figure": None,
    },
    {
        "id": "c8-07-h02",
        "band": "harder",
        "text": "Aluminium oxide reacts with acids the way a metal oxide "
                "should, and with alkalis the way a non-metal oxide should. "
                "What does that tell you about the rule in this lesson?",
        "options": [
            {"text": "That the rule was never supported by any evidence",
             "correct": False,
             "why": "Six oxides on the bench went exactly as the rule "
                    "predicts. That is evidence."},
            {"text": "That the rule has a boundary, where the table has one "
                     "too",
             "correct": True},
            {"text": "That aluminium has been placed in the wrong group",
             "correct": False,
             "why": "Aluminium sits on the staircase between the two sides, "
                    "which is exactly where its oxide behaves as it does."},
            {"text": "That every oxide is really both acidic and basic at once",
             "correct": False,
             "why": "Sulfur dioxide reacts with alkalis and not with acids. "
                    "Most oxides pick a side."},
        ],
        "figure": None,
    },
    {
        "id": "c8-07-h03",
        "band": "harder",
        "text": "A technician needs to know whether an unlabelled white powder "
                "is a metal oxide, and universal indicator in water gives 7. "
                "What should the technician conclude?",
        "options": [
            {"text": "It is not a metal oxide, because the reading did not "
                     "rise",
             "correct": False,
             "why": "That is the copper-oxide trap. An insoluble metal oxide "
                    "gives exactly this reading."},
            {"text": "It is a non-metal oxide, because only those leave water "
                     "at 7",
             "correct": False,
             "why": "Most non-metal oxides take the water below 7. Water "
                    "itself is the exception, not the rule."},
            {"text": "Nothing yet, and the powder should be tried with a "
                     "dilute acid",
             "correct": True},
            {"text": "It is a metal oxide, because non-metal oxides are all "
                     "gases",
             "correct": False,
             "why": "The reading supports neither answer, and plenty of "
                    "non-metal oxides are not gases."},
        ],
        "figure": None,
    },
    {
        "id": "c8-07-h04",
        "band": "harder",
        "text": "Rain that has fallen through clean country air is already "
                "slightly acidic, at about pH 6, before it touches anything. "
                "Why?",
        "options": [
            {"text": "Because rain water picks up acid from the clouds it "
                     "formed in",
             "correct": False,
             "why": "Cloud droplets are the same water. Something has to "
                    "dissolve in them to change the pH."},
            {"text": "Because sunlight breaks water down into an acid as it "
                     "falls",
             "correct": False,
             "why": "Water is not broken down by sunlight on the way to the "
                    "ground."},
            {"text": "Because dust in the air is acidic and dissolves in the "
                     "drops",
             "correct": False,
             "why": "Country air is not full of acidic dust, and the effect is "
                    "measured everywhere, including over the sea."},
            {"text": "Because carbon dioxide from the air dissolves in it",
             "correct": True},
        ],
        "figure": None,
    },

    # ── easier · MRB-335 top-up ─────────────────────────────────────────
    {
        "id": "c8-07-e05",
        "band": "easier",
        "text": "What is an alkali?",
        "options": [
            {"text": "A base that has dissolved in water, giving a solution "
                     "above pH 7",
             "correct": True},
            {"text": "Any substance that takes the pH of a solution away from "
                     "7, in whichever direction it happens to move it",
             "correct": False,
             "why": "Moving it DOWN is what an acid does. An alkali takes it "
                    "up"},
            {"text": "Any substance that reacts with an acid",
             "correct": False,
             "why": "That is a base. An alkali is the kind of base that "
                    "dissolves"},
            {"text": "Another word for a metal oxide",
             "correct": False,
             "why": "Copper oxide is a metal oxide and is not an alkali, "
                    "because it barely dissolves"},
        ],
        "figure": None,
    },
    {
        "id": "c8-07-e06",
        "band": "easier",
        "text": "Sulfur is burned in air and the product is shaken with "
                "water. What will the pH be?",
        "options": [
            {"text": "Above 7, because burning an element always gives a "
                     "product that dissolves to make an alkaline solution",
             "correct": False,
             "why": "That is what a METAL oxide does. Sulfur is a non-metal"},
            {"text": "Below 7",
             "correct": True},
            {"text": "Exactly 7",
             "correct": False,
             "why": "Sulfur dioxide dissolves readily and its solution is "
                    "acidic. It does not leave the water neutral"},
            {"text": "It cannot be predicted without knowing the "
                     "temperature",
             "correct": False,
             "why": "Temperature does not decide it. The side of the table "
                    "the element came from does"},
        ],
        "figure": None,
    },
    {
        "id": "c8-07-e07",
        "band": "easier",
        "text": "Water is itself a non-metal oxide. What pH does it read?",
        "options": [
            {"text": "Below 7, because every non-metal oxide gives an acidic "
                     "solution and water is no exception to a rule that has "
                     "no exceptions",
             "correct": False,
             "why": "Water is the exception, and it is the definition of "
                    "neutral. A rule with a known boundary is still a rule"},
            {"text": "Above 7",
             "correct": False,
             "why": "Above 7 is alkaline, which is what a dissolved METAL "
                    "oxide gives"},
            {"text": "Exactly 7",
             "correct": True},
            {"text": "Water has no pH, because pH is a property of what is "
                     "dissolved IN it",
             "correct": False,
             "why": "Pure water reads exactly 7, and that reading is the "
                    "anchor the whole scale is built around"},
        ],
        "figure": None,
    },

    # ── standard · MRB-335 top-up ───────────────────────────────────────
    {
        "id": "c8-07-s05",
        "band": "standard",
        "text": "Which pair of words describes magnesium oxide stirred into "
                "water?",
        "options": [
            {"text": "Basic and alkaline",
             "correct": True},
            {"text": "Basic, and never alkaline, because it is a solid and a "
                     "solid cannot be an alkali however much of it dissolves",
             "correct": False,
             "why": "That is copper oxide's description. Magnesium oxide "
                    "dissolves enough to take the pH to 10"},
            {"text": "Acidic and alkaline",
             "correct": False,
             "why": "Nothing is both. Magnesium is a metal, so its oxide is "
                    "on the base side"},
            {"text": "Neutral and basic",
             "correct": False,
             "why": "The reading is 10, which is not neutral"},
        ],
        "figure": None,
    },
    {
        "id": "c8-07-s06",
        "band": "standard",
        "text": "An unknown element is burned and its oxide, shaken with "
                "water, takes the pH to 11. What was the element?",
        "options": [
            {"text": "A non-metal, since a reading that far from neutral "
                     "shows the oxide dissolved readily and it is the "
                     "non-metal oxides that do that",
             "correct": False,
             "why": "How readily it dissolves is a separate question from "
                    "which WAY the pH moved. Up means a metal"},
            {"text": "A metal",
             "correct": True},
            {"text": "It cannot be told, because both kinds of oxide can "
                     "raise the pH",
             "correct": False,
             "why": "Only metal oxides raise it. Non-metal oxides bring it "
                    "down"},
            {"text": "A noble gas",
             "correct": False,
             "why": "Noble gases do not burn and make no oxides at all"},
        ],
        "figure": None,
    },
    {
        "id": "c8-07-s07",
        "band": "standard",
        "text": "Why can a pH test find magnesium oxide but not copper "
                "oxide, when both are bases?",
        "options": [
            {"text": "Because copper oxide is black and the colour of the "
                     "powder hides the colour the indicator turns",
             "correct": False,
             "why": "The powder sits on the bottom and the solution above it "
                    "is clear. The colour is readable"},
            {"text": "Because copper oxide is a weaker base",
             "correct": False,
             "why": "Strength is not the issue — it reacts with acid "
                    "perfectly well. Solubility is"},
            {"text": "Because almost none of the copper oxide dissolves, and "
                     "a pH reading only reports what is dissolved",
             "correct": True},
            {"text": "Because copper oxide reacts with the indicator",
             "correct": False,
             "why": "It reacts with nothing in the beaker, which is why the "
                    "reading does not move"},
        ],
        "figure": None,
    },

    # ── harder · MRB-335 top-up ─────────────────────────────────────────
    {
        "id": "c8-07-h05",
        "band": "harder",
        "text": "Powdered limestone is tipped into a lake that has been "
                "acidified by rain. Which two facts make that work?",
        "options": [
            {"text": "That the rain is acidic, and that limestone reacts with "
                     "acid",
             "correct": True},
            {"text": "That limestone is a metal oxide, and that metal oxides "
                     "dissolve readily enough to spread through a whole lake "
                     "within a few days of being tipped in",
             "correct": False,
             "why": "Limestone is calcium carbonate rather than an oxide, and "
                    "it is barely soluble. It works by reacting with the "
                    "acid"},
            {"text": "That limestone is neutral, so it dilutes the acid",
             "correct": False,
             "why": "Dilution is not what happens. The acid is used up in a "
                    "reaction"},
            {"text": "That limestone is heavier than water, so it sinks and "
                     "seals the bottom",
             "correct": False,
             "why": "Sealing the bottom would do nothing about the acid "
                    "already in the water"},
        ],
        "figure": None,
    },
    {
        "id": "c8-07-h06",
        "band": "harder",
        "text": "Clean country rain is already about pH 6 before it touches "
                "anything, and rain downwind of heavy industry can be near "
                "pH 4. What is the difference, in this lesson's terms?",
        "options": [
            {"text": "The first is a non-metal oxide dissolving and the "
                     "second is a metal oxide, blown out of the chimneys of "
                     "the works and carried downwind with the weather",
             "correct": False,
             "why": "A metal oxide would push the pH UP. Everything acidifying "
                    "the rain here is a non-metal oxide"},
            {"text": "Both are non-metal oxides dissolving in the rain — "
                     "carbon dioxide in the first case, sulfur and nitrogen "
                     "oxides added in the second",
             "correct": True},
            {"text": "The first is natural and the second is pollution, and "
                     "the chemistry is different",
             "correct": False,
             "why": "One is natural and one is not, and the chemistry is the "
                    "same. That is what makes the comparison useful"},
            {"text": "The second rain has picked up dust, which is acidic",
             "correct": False,
             "why": "Dust is not what does it. Gases dissolving in the "
                    "droplets are"},
        ],
        "figure": None,
    },
    {
        "id": "c8-07-h07",
        "band": "harder",
        "text": "Carbon dioxide is a non-metal oxide and a gas rather than a "
                "solid. Does the rule in this lesson still apply to it?",
        "options": [
            {"text": "No — the rule is about oxides you can weigh out, and a "
                     "gas cannot be stirred into water in the way the bench "
                     "does it",
             "correct": False,
             "why": "A gas dissolves in water perfectly well, and this one "
                    "does so in every raindrop that falls"},
            {"text": "No — carbon dioxide is neutral, like water",
             "correct": False,
             "why": "Water is the neutral non-metal oxide. Carbon dioxide "
                    "brings the pH down"},
            {"text": "Yes — dissolve it and the solution is acidic, which is "
                     "why clean rain is already below 7",
             "correct": True},
            {"text": "Yes, but only under pressure",
             "correct": False,
             "why": "Pressure changes how much dissolves rather than what the "
                    "solution then is. Rain at ordinary pressure is "
                    "acidic"},
        ],
        "figure": None,
    },
    {
        "id": "c8-07-e08",
        "band": "easier",
        "text": "A length of magnesium ribbon is burned in air. What is the "
                "white solid left behind?",
        "options": [
            {"text": "Magnesium oxide", "correct": True},
            {"text": "Magnesium hydroxide", "correct": False,
             "why": "A hydroxide contains hydrogen as well, and no hydrogen "
                    "was put into the flame"},
            {"text": "Magnesium sulfate", "correct": False,
             "why": "A sulfate needs sulfuric acid to form. Burning in air "
                    "supplies oxygen and nothing else"},
            {"text": "Magnesium carbonate", "correct": False,
             "why": "A carbonate needs carbon as well as oxygen, and none was "
                    "added to the flame"},
        ],
        "figure": None,
    },
    {
        "id": "c8-07-e09",
        "band": "easier",
        "text": "Complete the word equation: sulfur + oxygen → ?",
        "options": [
            {"text": "sulfur hydroxide", "correct": False,
             "why": "A hydroxide contains hydrogen, and burning in air joins "
                    "the sulfur to oxygen only"},
            {"text": "sulfur dioxide", "correct": True},
            {"text": "sulfuric acid", "correct": False,
             "why": "The acid appears only after the oxide has dissolved in "
                    "water. Burning gives the oxide itself"},
            {"text": "sulfate", "correct": False,
             "why": "A sulfate is a salt and needs an acid and a base to "
                    "form. Burning an element in air gives an oxide"},
        ],
        "figure": None,
    },
    {
        "id": "c8-07-e10",
        "band": "easier",
        "text": "Which of these is the formula of magnesium oxide?",
        "options": [
            {"text": "MnO", "correct": False,
             "why": "Mn is the symbol for manganese, which is a different "
                    "element altogether"},
            {"text": "MgO₂", "correct": False,
             "why": "That formula says two oxygen atoms to one magnesium. "
                    "Magnesium oxide has one of each"},
            {"text": "MgO", "correct": True},
            {"text": "Mg₂O", "correct": False,
             "why": "That formula says two magnesium atoms to one oxygen, "
                    "which is not the compound that forms"},
        ],
        "figure": None,
    },
    {
        "id": "c8-07-e11",
        "band": "easier",
        "text": "A solution is tested and the pH reads 3. What does that tell "
                "you about the solution?",
        "options": [
            {"text": "It is alkaline", "correct": False,
             "why": "Alkaline means a reading above 7, and 3 is well below it"},
            {"text": "It is neutral", "correct": False,
             "why": "Only a reading of exactly 7 is neutral"},
            {"text": "It has nothing dissolved in it", "correct": False,
             "why": "A reading of 3 is a report on what IS dissolved. Water "
                    "with nothing in it reads 7"},
            {"text": "It is acidic", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c8-07-e12",
        "band": "easier",
        "text": "Which pH value is exactly neutral?",
        "options": [
            {"text": "7", "correct": True},
            {"text": "0", "correct": False,
             "why": "Zero is the far acidic end of the scale"},
            {"text": "10", "correct": False,
             "why": "Ten is above 7, so a solution reading 10 is alkaline"},
            {"text": "14", "correct": False,
             "why": "Fourteen is the far alkaline end of the scale"},
        ],
        "figure": None,
    },
    {
        "id": "c8-07-e13",
        "band": "easier",
        "text": "Universal indicator is added to a solution and it turns red. "
                "What is the solution?",
        "options": [
            {"text": "Neutral", "correct": False,
             "why": "Green is the colour of a neutral solution"},
            {"text": "Strongly acidic", "correct": True},
            {"text": "Strongly alkaline", "correct": False,
             "why": "Purple is the strongly alkaline colour, at the far end "
                    "of the scale from red"},
            {"text": "Slightly alkaline", "correct": False,
             "why": "Blue is the slightly alkaline colour. Red sits at the "
                    "opposite end of the range"},
        ],
        "figure": None,
    },
    {
        "id": "c8-07-e14",
        "band": "easier",
        "text": "What colour does universal indicator show in an alkaline "
                "solution?",
        "options": [
            {"text": "Red or orange", "correct": False,
             "why": "Those are the acidic colours, for readings below 7"},
            {"text": "Green", "correct": False,
             "why": "Green is the neutral colour, at exactly 7"},
            {"text": "Blue or purple", "correct": True},
            {"text": "It stays colourless", "correct": False,
             "why": "Universal indicator always shows a colour once it is in "
                    "the solution"},
        ],
        "figure": None,
    },
    {
        "id": "c8-07-e15",
        "band": "easier",
        "text": "What is the name of the reaction between an acid and a base?",
        "options": [
            {"text": "Displacement", "correct": False,
             "why": "Displacement is one element pushing another out of its "
                    "compound, which is not what happens here"},
            {"text": "Combustion", "correct": False,
             "why": "Combustion is burning in oxygen, and no acid is needed "
                    "for it"},
            {"text": "Dissolving", "correct": False,
             "why": "Dissolving mixes a substance into water without making a "
                    "new one. Here a salt and water are made"},
            {"text": "Neutralisation", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c8-07-e16",
        "band": "easier",
        "text": "A metal oxide neutralises hydrochloric acid. What kind of "
                "salt is made?",
        "options": [
            {"text": "A chloride", "correct": True},
            {"text": "A sulfate", "correct": False,
             "why": "The second half of a salt's name comes from the acid, "
                    "and hydrochloric acid never gives sulfates"},
            {"text": "A nitrate", "correct": False,
             "why": "That salt comes from a different acid. Hydrochloric acid "
                    "gives chlorides"},
            {"text": "A hydroxide", "correct": False,
             "why": "A hydroxide is not a salt. Neutralisation gives a salt "
                    "and water"},
        ],
        "figure": None,
    },
    {
        "id": "c8-07-e17",
        "band": "easier",
        "text": "Which acid must be used to make a nitrate?",
        "options": [
            {"text": "Hydrochloric acid", "correct": False,
             "why": "Hydrochloric acid gives chlorides"},
            {"text": "Nitric acid", "correct": True},
            {"text": "Sulfuric acid", "correct": False,
             "why": "Sulfuric acid gives sulfates"},
            {"text": "Carbonic acid", "correct": False,
             "why": "Carbonic acid is what carbon dioxide makes in water, and "
                    "its salts are carbonates"},
        ],
        "figure": None,
    },
    {
        "id": "c8-07-e18",
        "band": "easier",
        "text": "SO₂ is the formula of which compound?",
        "options": [
            {"text": "Sodium oxide", "correct": False,
             "why": "The symbol for sodium is Na. S on its own is sulfur"},
            {"text": "Sulfur dioxide", "correct": True},
            {"text": "Silicon dioxide", "correct": False,
             "why": "Silicon's symbol is Si, so silicon dioxide is written "
                    "SiO₂"},
            {"text": "Sulfur trioxide", "correct": False,
             "why": "Trioxide would mean three oxygen atoms, and this formula "
                    "shows two"},
        ],
        "figure": None,
    },
    {
        "id": "c8-07-e19",
        "band": "easier",
        "text": "Which of these is a metal oxide?",
        "options": [
            {"text": "Carbon dioxide", "correct": False,
             "why": "Carbon is a non-metal, so its oxide is a non-metal oxide"},
            {"text": "Sulfur dioxide", "correct": False,
             "why": "Sulfur is a non-metal, so its oxide is a non-metal oxide"},
            {"text": "Calcium oxide", "correct": True},
            {"text": "Nitrogen dioxide", "correct": False,
             "why": "Nitrogen is a non-metal, so its oxide is a non-metal "
                    "oxide"},
        ],
        "figure": None,
    },
    {
        "id": "c8-07-e20",
        "band": "easier",
        "text": "Which of these oxides gives an acidic solution in water?",
        "options": [
            {"text": "Calcium oxide", "correct": False,
             "why": "Calcium is a metal, so its oxide is a base and takes the "
                    "reading up the scale"},
            {"text": "Magnesium oxide", "correct": False,
             "why": "Magnesium oxide is a base, and stirred into water it "
                    "gives a reading of about 10"},
            {"text": "Copper oxide", "correct": False,
             "why": "Copper oxide is a base, and so little of it dissolves "
                    "that the reading does not move at all"},
            {"text": "Sulfur dioxide", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c8-07-e21",
        "band": "easier",
        "text": "What does insoluble mean?",
        "options": [
            {"text": "It will not dissolve, so almost none of it gets into "
                     "the solution", "correct": True},
            {"text": "It will not react, so almost nothing can be made from it",
             "correct": False,
             "why": "An insoluble solid can still react. Copper oxide is "
                    "insoluble and it reacts with acids"},
            {"text": "It has no pH of its own, so no reading can be taken from "
                     "it", "correct": False,
             "why": "No solid has a pH of its own. The word is about "
                    "dissolving, not about readings"},
            {"text": "It is a solid rather than a gas, so it stays where it is "
                     "put", "correct": False,
             "why": "Plenty of solids dissolve freely. The word describes "
                    "dissolving, not what state a substance is in"},
        ],
        "figure": None,
    },
    {
        "id": "c8-07-e22",
        "band": "easier",
        "text": "Every alkali is a base. Is every base an alkali?",
        "options": [
            {"text": "Yes — the two words mean the same thing",
             "correct": False,
             "why": "They do not. One says what a substance does to an acid, "
                    "the other describes a solution"},
            {"text": "No — only a base that dissolves in water is an alkali",
             "correct": True},
            {"text": "No — only a base that is a metal oxide is an alkali",
             "correct": False,
             "why": "Being a metal oxide is not what decides it. Whether it "
                    "dissolves is"},
            {"text": "Yes — as soon as it is put into water",
             "correct": False,
             "why": "Putting copper oxide into water makes no alkali, because "
                    "almost none of it goes into solution"},
        ],
        "figure": None,
    },
    {
        "id": "c8-07-e23",
        "band": "easier",
        "text": "Coal contains sulfur. Which gas does burning that coal send "
                "up the chimney?",
        "options": [
            {"text": "Hydrogen", "correct": False,
             "why": "Burning joins a substance to oxygen. It does not release "
                    "hydrogen gas"},
            {"text": "Nitrogen", "correct": False,
             "why": "Nitrogen is already in the air and passes through a fire "
                    "unchanged unless it gets extremely hot"},
            {"text": "Sulfur dioxide", "correct": True},
            {"text": "Sulfuric acid", "correct": False,
             "why": "Sulfuric acid is not a gas, and it appears only once the "
                    "oxide has dissolved in water"},
        ],
        "figure": None,
    },
    {
        "id": "c8-07-e24",
        "band": "easier",
        "text": "Nitrogen oxides are made inside a very hot engine. Which two "
                "substances combine to make them?",
        "options": [
            {"text": "Nitrogen from the fuel and oxygen from the air",
             "correct": False,
             "why": "The nitrogen does not come from the fuel. It is already "
                    "in the air being drawn into the engine"},
            {"text": "Nitrogen and hydrogen", "correct": False,
             "why": "That pair contains no oxygen at all, so what it made "
                    "could not be an oxide"},
            {"text": "Carbon from the fuel and oxygen from the air",
             "correct": False,
             "why": "That pair gives carbon dioxide, which is a different "
                    "oxide entirely"},
            {"text": "Nitrogen and oxygen, both from the air", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c8-07-e25",
        "band": "easier",
        "text": "Four solutions were tested. Which reading is the most "
                "acidic?",
        "options": [
            {"text": "pH 3", "correct": True},
            {"text": "pH 5", "correct": False,
             "why": "Five is acidic, but three sits further down the scale "
                    "and so is more acidic"},
            {"text": "pH 7", "correct": False,
             "why": "Seven is neutral — neither acidic nor alkaline"},
            {"text": "pH 10", "correct": False,
             "why": "Ten is above 7, so that solution is alkaline rather than "
                    "acidic"},
        ],
        "figure": None,
    },
    {
        "id": "c8-07-e26",
        "band": "easier",
        "text": "Complete the word equation: copper oxide + sulfuric acid → "
                "copper sulfate + ?",
        "options": [
            {"text": "oxygen", "correct": False,
             "why": "No oxygen gas comes off. The oxygen from the oxide ends "
                    "up in the water that forms"},
            {"text": "water", "correct": True},
            {"text": "hydrogen", "correct": False,
             "why": "Hydrogen comes off when an acid meets a metal, not when "
                    "it meets a metal oxide"},
            {"text": "carbon dioxide", "correct": False,
             "why": "That comes off when an acid meets a carbonate, and there "
                    "is no carbon here"},
        ],
        "figure": None,
    },
    {
        "id": "c8-07-e27",
        "band": "easier",
        "text": "Which of these substances is an oxide?",
        "options": [
            {"text": "Magnesium chloride", "correct": False,
             "why": "It is magnesium joined with chlorine. An oxide is an "
                    "element joined with oxygen"},
            {"text": "Magnesium sulfate", "correct": False,
             "why": "A sulfate is a salt made from sulfuric acid, not an "
                    "element joined with oxygen"},
            {"text": "Magnesium oxide", "correct": True},
            {"text": "Magnesium hydroxide", "correct": False,
             "why": "A hydroxide has hydrogen in it as well, so it is not one "
                    "element joined with oxygen"},
        ],
        "figure": None,
    },
    {
        "id": "c8-07-e28",
        "band": "easier",
        "text": "Carbon dioxide dissolves in water. What is the acid that "
                "forms called?",
        "options": [
            {"text": "Carbon acid", "correct": False,
             "why": "No acid goes by that name. The acid from carbon dioxide "
                    "has a different one"},
            {"text": "Sulfuric acid", "correct": False,
             "why": "Sulfuric acid comes from sulfur dioxide, and there is no "
                    "sulfur here at all"},
            {"text": "Hydrochloric acid", "correct": False,
             "why": "Hydrochloric acid contains chlorine, and none is present "
                    "in this mixture"},
            {"text": "Carbonic acid", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c8-07-e29",
        "band": "easier",
        "text": "Warm sulfuric acid is poured onto black copper oxide and the "
                "solid disappears. Which salt has been made?",
        "options": [
            {"text": "Copper sulfate", "correct": True},
            {"text": "Copper chloride", "correct": False,
             "why": "A chloride would need hydrochloric acid, which is not "
                    "what was poured on"},
            {"text": "Copper oxide", "correct": False,
             "why": "That is the solid that was there at the start. The salt "
                    "is the new substance"},
            {"text": "Copper nitrate", "correct": False,
             "why": "A nitrate would need nitric acid, which is not what was "
                    "poured on"},
        ],
        "figure": None,
    },
    {
        "id": "c8-07-e30",
        "band": "easier",
        "text": "Which two gases are named as the main causes of unusually "
                "acidic rain?",
        "options": [
            {"text": "Carbon dioxide and oxygen", "correct": False,
             "why": "Oxygen dissolving in rain does not make it acidic at all"},
            {"text": "Sulfur dioxide and nitrogen oxides", "correct": True},
            {"text": "Hydrogen and helium", "correct": False,
             "why": "Neither of those is an oxide, and neither dissolves to "
                    "give an acid"},
            {"text": "Nitrogen and carbon monoxide", "correct": False,
             "why": "Nitrogen gas passes straight through the droplets, and "
                    "carbon monoxide barely dissolves in them"},
        ],
        "figure": None,
    },
    {
        "id": "c8-07-e31",
        "band": "easier",
        "text": "Limestone is calcium carbonate. Why does a carved limestone "
                "statue wear away faster in acidic rain?",
        "options": [
            {"text": "Because acidic rain is colder than ordinary rain",
             "correct": False,
             "why": "Temperature is not the difference. What the rain "
                    "contains is"},
            {"text": "Because acidic rain falls harder onto the stone",
             "correct": False,
             "why": "How hard it falls is not the difference. What is "
                    "dissolved in it is"},
            {"text": "Because the stone reacts with the acid in the rain",
             "correct": True},
            {"text": "Because limestone dissolves in any water at all",
             "correct": False,
             "why": "Limestone sits in ordinary rivers for centuries. It "
                    "needs the acid to be eaten away quickly"},
        ],
        "figure": None,
    },
    {
        "id": "c8-07-e32",
        "band": "easier",
        "text": "Which of these could be described as a base?",
        "options": [
            {"text": "Carbon dioxide", "correct": False,
             "why": "Carbon is a non-metal, so its oxide is acidic rather "
                    "than basic"},
            {"text": "Sulfur dioxide", "correct": False,
             "why": "Sulfur is a non-metal, so its oxide is acidic rather "
                    "than basic"},
            {"text": "Hydrochloric acid", "correct": False,
             "why": "An acid is the thing a base reacts with, so it cannot be "
                    "a base itself"},
            {"text": "Copper oxide", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c8-07-s08",
        "band": "standard",
        "text": "Carbon dioxide and sulfur dioxide are bubbled through "
                "separate beakers of water. One beaker settles at pH 5 and "
                "the other at pH 3. Which gas gave which reading?",
        "options": [
            {"text": "pH 5 was sulfur dioxide and pH 3 was carbon dioxide", "correct": False,
             "why": "That is the pair the wrong way round. Sulfur dioxide "
                    "dissolves readily, which is exactly why its reading goes "
                    "further down"},
            {"text": "pH 5 was carbon dioxide and pH 3 was sulfur dioxide",
             "correct": True},
            {"text": "It cannot be decided from the readings alone", "correct": False,
             "why": "Being on the same side of the table fixes the direction, "
                    "not how far the reading travels, so the two readings do "
                    "separate them"},
            {"text": "Both readings came from carbon dioxide, at two different "
                     "strengths", "correct": False,
             "why": "Two different gases were bubbled through two beakers, so "
                    "each reading belongs to one of them"},
        ],
        "figure": None,
    },
    {
        "id": "c8-07-s09",
        "band": "standard",
        "text": "Black copper oxide is warmed with dilute hydrochloric acid "
                "and the solid disappears. Name the two products.",
        "options": [
            {"text": "Copper sulfate and water", "correct": False,
             "why": "A sulfate would need sulfuric acid. The salt takes its "
                    "second name from the acid used"},
            {"text": "Copper chloride and hydrogen", "correct": False,
             "why": "Hydrogen comes off when an acid meets a metal. A metal "
                    "oxide gives water instead"},
            {"text": "Copper chloride and water", "correct": True},
            {"text": "Copper and chlorine", "correct": False,
             "why": "Neutralisation does not split a compound into its "
                    "elements. It makes a salt and water"},
        ],
        "figure": None,
    },
    {
        "id": "c8-07-s10",
        "band": "standard",
        "text": "Iron oxide is stirred into water and the pH stays at 7, but "
                "it dissolves away in warm dilute sulfuric acid. What is iron "
                "oxide?",
        "options": [
            {"text": "A neutral oxide that has nothing to react with",
             "correct": False,
             "why": "The reading did not move because so little dissolved, "
                    "and the acid then showed the substance is far from "
                    "neutral"},
            {"text": "An acidic oxide that reacts only with acids", "correct": False,
             "why": "Acidic oxides react with alkalis, not with acids. This "
                    "one reacts with the acid"},
            {"text": "Neither a base nor an acid, since the two tests disagree",
             "correct": False,
             "why": "The two tests do not disagree. Only one of them is "
                    "capable of finding a base that will not dissolve"},
            {"text": "A base that does not dissolve in water", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c8-07-s11",
        "band": "standard",
        "text": "Calcium oxide is added to nitric acid until the acid is "
                "used up. Name the salt that forms.",
        "options": [
            {"text": "Calcium nitrate", "correct": True},
            {"text": "Calcium oxide", "correct": False,
             "why": "That is what was added. A salt is the new substance "
                    "produced by the reaction"},
            {"text": "Calcium nitride", "correct": False,
             "why": "A nitride contains nitrogen with no oxygen, and is not "
                    "what an acid makes"},
            {"text": "Calcium hydroxide", "correct": False,
             "why": "A hydroxide is not a salt. Neutralising an acid gives a "
                    "salt and water"},
        ],
        "figure": None,
    },
    {
        "id": "c8-07-s12",
        "band": "standard",
        "text": "A gas is bubbled through water containing universal "
                "indicator, and the green turns orange. The gas is an oxide. "
                "What does that tell you about the element in it?",
        "options": [
            {"text": "It is a metal", "correct": False,
             "why": "Only metals burning well enough to make a gas is not the "
                    "test. A metal oxide is a base, so it would have taken the "
                    "colour the other way"},
            {"text": "It is a non-metal", "correct": True},
            {"text": "It is a metal whose oxide did not dissolve",
             "correct": False,
             "why": "Something plainly dissolved, because the colour moved. "
                    "An undissolved oxide leaves it green"},
            {"text": "Nothing can be said yet", "correct": False,
             "why": "Orange already places the solution below 7, which is all "
                    "the direction needed. A probe would add none"},
        ],
        "figure": None,
    },
    {
        "id": "c8-07-s13",
        "band": "standard",
        "text": "Sand is silicon dioxide, SiO₂, and silicon is a non-metal. "
                "Sand shaken with water leaves the pH at 7. Which statement "
                "fits both of those facts?",
        "options": [
            {"text": "Silicon dioxide must really be a metal oxide, because "
                     "it did not turn the water acidic", "correct": False,
             "why": "A metal oxide that dissolved would push the reading "
                    "above 7, and this one did not do that either"},
            {"text": "Silicon dioxide is neutral, so the rule about non-metal "
                     "oxides has an exception", "correct": False,
             "why": "The reading is neutral because nothing dissolved, which "
                    "is not the same as the substance being neutral"},
            {"text": "It is an acidic oxide that will not dissolve, so the "
                     "water test has nothing to report", "correct": True},
            {"text": "The sand was not stirred for long enough for the "
                     "reading to change", "correct": False,
             "why": "Stirring for longer will not dissolve a solid that does "
                    "not dissolve"},
        ],
        "figure": None,
    },
    {
        "id": "c8-07-s14",
        "band": "standard",
        "text": "Nitrogen dioxide, NO₂, dissolves in falling rain. What "
                "happens to the pH of that rain, and why?",
        "options": [
            {"text": "It rises above 7, because nitrogen is a gas found all "
                     "through the air", "correct": False,
             "why": "How common nitrogen is has nothing to do with it. Only a "
                    "dissolved base pushes a reading above 7"},
            {"text": "It stays at 7, because a gas cannot change a pH reading",
             "correct": False,
             "why": "A gas that dissolves changes the reading just as a solid "
                    "that dissolves does"},
            {"text": "It stays at 7, because nitrogen dioxide is neutral like "
                     "water", "correct": False,
             "why": "Water is the neutral non-metal oxide. Nitrogen dioxide "
                    "dissolves to give an acidic solution"},
            {"text": "It falls below 7, because nitrogen is a non-metal and "
                     "its oxide is acidic", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c8-07-s15",
        "band": "standard",
        "text": "Explain why burning coal that contains sulfur makes the rain "
                "downwind more acidic.",
        "options": [
            {"text": "The sulfur burns to sulfur dioxide, a non-metal oxide, "
                     "which dissolves in the raindrops", "correct": True},
            {"text": "Solid sulfur is carried up the chimney and falls into "
                     "the rain as a powder", "correct": False,
             "why": "The sulfur has burned and left as a gas. Solid sulfur is "
                    "not what reaches the cloud"},
            {"text": "The heat of the fire makes the rain evaporate and what "
                     "is left is more concentrated", "correct": False,
             "why": "Evaporation does not add an acid. Something acidic has "
                    "to dissolve in the water"},
            {"text": "The smoke removes the oxygen from the rain and that "
                     "lowers its pH", "correct": False,
             "why": "Dissolved oxygen has no effect on pH. Only a dissolved "
                    "oxide of a non-metal takes it down"},
        ],
        "figure": None,
    },
    {
        "id": "c8-07-s16",
        "band": "standard",
        "text": "Calcium oxide stirred into water gives a reading of pH 12. "
                "What colour would universal indicator show in that beaker?",
        "options": [
            {"text": "Green", "correct": False,
             "why": "Green means exactly 7, and this solution is five points "
                    "above that"},
            {"text": "Purple", "correct": True},
            {"text": "Red", "correct": False,
             "why": "Red is the strongly acidic colour, at the opposite end "
                    "of the scale from 12"},
            {"text": "Orange", "correct": False,
             "why": "Orange marks a solution below 7, and this one is well "
                    "above it"},
        ],
        "figure": None,
    },
    {
        "id": "c8-07-s17",
        "band": "standard",
        "text": "A bottle of fizzy water and a jar of rain collected in open "
                "country both read close to pH 6. What do the two liquids "
                "have in common?",
        "options": [
            {"text": "Both have been stored in plastic, which makes any "
                     "liquid slightly acidic", "correct": False,
             "why": "The container is not what does it. Something acidic is "
                    "dissolved in each"},
            {"text": "Both have picked up dust, and dust is acidic",
             "correct": False,
             "why": "Dust is not the cause. A dissolved gas is"},
            {"text": "Both have carbon dioxide dissolved in them, and it "
                     "gives an acidic solution", "correct": True},
            {"text": "Both are short of oxygen, and water with less oxygen in "
                     "it reads lower", "correct": False,
             "why": "Dissolved oxygen does not move a pH reading in either "
                    "direction"},
        ],
        "figure": None,
    },
    {
        "id": "c8-07-s18",
        "band": "standard",
        "text": "Copper oxide is added to warm dilute sulfuric acid a "
                "spatula at a time. Eventually some black solid stays on the "
                "bottom and will not react. Why is that a useful signal?",
        "options": [
            {"text": "It shows the acid has gone too cold to carry on, "
                     "since a neutralisation only ever runs in a warm "
                     "solution", "correct": False,
             "why": "Cooling would slow the reaction down, not stop it while "
                    "acid was still there"},
            {"text": "It shows the copper oxide has begun to dissolve in the "
                     "water rather than react", "correct": False,
             "why": "Copper oxide does not dissolve in water. Anything that "
                    "went in did so by reacting with the acid"},
            {"text": "It shows the solution has now turned alkaline and is "
                     "pushing the solid back out", "correct": False,
             "why": "A salt solution is left, not an alkaline one, and "
                    "nothing pushes an unreacted solid out"},
            {"text": "It shows all the acid has been used up, so there is "
                     "nothing left for the solid to react with",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c8-07-s19",
        "band": "standard",
        "text": "Copper oxide is a black powder and copper sulfate solution "
                "is blue. A student adds the powder to sulfuric acid and the "
                "liquid turns blue. What has the colour change shown?",
        "options": [
            {"text": "A new substance has been made, and it is dissolved in "
                     "the liquid", "correct": True},
            {"text": "A powder has simply dissolved without changing",
             "correct": False,
             "why": "If it had only dissolved, the solution would carry the "
                    "colour of the powder rather than a new one"},
            {"text": "An acid has been diluted enough to show its own colour", "correct": False,
             "why": "Dilute sulfuric acid is colourless however much water is "
                    "added to it"},
            {"text": "All of the copper oxide has turned into copper metal",
             "correct": False,
             "why": "Copper metal is a solid you could see and lift out, not "
                    "a blue solution"},
        ],
        "figure": None,
    },
    {
        "id": "c8-07-s20",
        "band": "standard",
        "text": "Exactly enough metal oxide is added to an acid to use all of "
                "it up. What is the pH of the mixture at the end?",
        "options": [
            {"text": "Below 7",
             "correct": False,
             "why": "Acid is not left over. Adding exactly enough base removes "
                    "all of it, which is what neutralising means"},
            {"text": "7", "correct": True},
            {"text": "Above 7", "correct": False,
             "why": "A metal oxide is a base, but it raises the reading only "
                    "once there is spare base left over. Here every bit of it "
                    "has reacted"},
            {"text": "14",
             "correct": False,
             "why": "Going all the way does not mean going to the end of the "
                    "scale. Fourteen is the far alkaline end, not what a "
                    "completed neutralisation gives"},
        ],
        "figure": None,
    },
    {
        "id": "c8-07-s21",
        "band": "standard",
        "text": "Three oxides were shaken with water and gave readings of "
                "pH 10, pH 5 and pH 3. Which of them was an oxide of a metal?",
        "options": [
            {"text": "The pH 3 one", "correct": False,
             "why": "Metals reacting the most strongly is not the point. A "
                    "dissolved metal oxide pushes the reading above 7"},
            {"text": "The pH 5 one",
             "correct": False,
             "why": "Being nearest neutral decides nothing. Five is still "
                    "below 7, so that solution is acidic"},
            {"text": "The pH 10 one", "correct": True},
            {"text": "None of them", "correct": False,
             "why": "A metal oxide leaving the reading at 7 is only true of "
                    "one that will not dissolve. One that dissolves reads well "
                    "above 7"},
        ],
        "figure": None,
    },
    {
        "id": "c8-07-s22",
        "band": "standard",
        "text": "Sulfur dioxide is called an acidic oxide even before any of "
                "it has touched water. Why is that description fair?",
        "options": [
            {"text": "Because the gas itself has a pH of 3", "correct": False,
             "why": "A gas has no pH. Only a solution has one"},
            {"text": "Because it was made by burning, and anything burned "
                     "becomes acidic", "correct": False,
             "why": "Burning magnesium gives a base, so burning does not "
                    "decide the direction"},
            {"text": "Because it is a gas, and all gases dissolve to give "
                     "acids", "correct": False,
             "why": "Ammonia is a gas and dissolves to give an alkaline "
                    "solution, so being a gas decides nothing"},
            {"text": "Because it reacts with an alkali to give a salt and "
                     "water, which is what an acidic oxide does",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c8-07-s23",
        "band": "standard",
        "text": "Magnesium burns in air and leaves a white powder. Which "
                "line gives both the word equation and what the powder does "
                "to the pH of water?",
        "options": [
            {"text": "magnesium + oxygen → magnesium oxide; the powder takes "
                     "the reading above 7", "correct": True},
            {"text": "magnesium + oxygen → magnesium oxide; the powder takes "
                     "the reading below 7", "correct": False,
             "why": "Magnesium is a metal, so its oxide is a base and the "
                    "reading goes up, not down"},
            {"text": "magnesium + air → magnesium nitride; the reading stays "
                     "at 7", "correct": False,
             "why": "It is the oxygen in the air that joins on, and the "
                    "product is an oxide"},
            {"text": "magnesium → magnesium oxide; the reading stays at 7 "
                     "because the powder is white", "correct": False,
             "why": "Nothing becomes an oxide without oxygen joining on, and "
                    "colour tells you nothing about pH"},
        ],
        "figure": None,
    },
    {
        "id": "c8-07-s24",
        "band": "standard",
        "text": "A salt called potassium sulfate was made by neutralising an "
                "alkali with an acid. Which acid was used?",
        "options": [
            {"text": "Nitric acid", "correct": False,
             "why": "Nitric acid would have given potassium nitrate instead"},
            {"text": "Sulfuric acid", "correct": True},
            {"text": "Hydrochloric acid", "correct": False,
             "why": "Hydrochloric acid would have given potassium chloride "
                    "instead"},
            {"text": "Potassium hydroxide", "correct": False,
             "why": "That is the alkali being neutralised, not the acid that "
                    "did the neutralising"},
        ],
        "figure": None,
    },
    {
        "id": "c8-07-s25",
        "band": "standard",
        "text": "A student writes that sulfur dioxide has a pH of 3. What is "
                "wrong with saying it that way?",
        "options": [
            {"text": "The number is too low; sulfur dioxide only reaches "
                     "about 5", "correct": False,
             "why": "The number is not the fault. Bubbled into water it does "
                    "reach about 3"},
            {"text": "Sulfur dioxide is a base like the other oxides on the "
                     "bench, so any number below 7 is the wrong way round",
             "correct": False,
             "why": "Sulfur is a non-metal, so its oxide is acidic. Below 7 "
                    "is the right direction"},
            {"text": "A pH describes a solution, so it is the water the gas "
                     "dissolved in that reads 3", "correct": True},
            {"text": "A pH can only be given for a solid, so no gas has one",
             "correct": False,
             "why": "Solids have no pH either. The reading always belongs to "
                    "a solution"},
        ],
        "figure": None,
    },
    {
        "id": "c8-07-s26",
        "band": "standard",
        "text": "Carved limestone weathers faster on a building in an "
                "industrial city than on one in open country. Explain why.",
        "options": [
            {"text": "More heat reaches the stone in a city, and warm stone "
                     "crumbles faster", "correct": False,
             "why": "Warmth is not the difference. What the rain is carrying "
                    "is"},
            {"text": "More dust falls in city rain, and it scratches away at "
                     "the carved surface", "correct": False,
             "why": "Scratching is not what removes it. The stone is being "
                    "reacted away"},
            {"text": "More dirt sits in city rain, and it holds water against "
                     "the stone for far longer", "correct": False,
             "why": "Wet stone alone is not eaten away. Limestone in a clean "
                    "river lasts for centuries"},
            {"text": "More non-metal oxides dissolve in city rain, so it is "
                     "more acidic and limestone reacts with acid",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c8-07-s27",
        "band": "standard",
        "text": "Burning sulfur is demonstrated inside a fume cupboard "
                "rather than on the open bench. Which product of the burning "
                "is the reason?",
        "options": [
            {"text": "Sulfur dioxide gas, which irritates the lungs",
             "correct": True},
            {"text": "Sulfuric acid, which is made straight away in the "
                     "flame", "correct": False,
             "why": "The acid only appears once the oxide has dissolved in "
                    "water. Burning gives the gas"},
            {"text": "Hydrogen gas, which could catch light", "correct": False,
             "why": "Burning sulfur in air makes no hydrogen at all"},
            {"text": "A sulfate powder, which is dangerous to breathe in",
             "correct": False,
             "why": "No sulfate is made here. A sulfate needs an acid and a "
                    "base to react together"},
        ],
        "figure": None,
    },
    {
        "id": "c8-07-s28",
        "band": "standard",
        "text": "Nitrogen and oxygen sit side by side in the air all day "
                "without reacting, yet nitrogen oxides pour out of a running "
                "engine. What has the engine supplied?",
        "options": [
            {"text": "Extra oxygen to make up what the open air lacks", "correct": False,
             "why": "The air already holds about a fifth oxygen, which is "
                    "plenty. What it lacks is the heat"},
            {"text": "A high enough temperature for the two to combine",
             "correct": True},
            {"text": "Water for the two gases to join in",
             "correct": False,
             "why": "No water is needed to make the oxide. Water only matters "
                    "later, when the oxide dissolves in rain"},
            {"text": "Extra nitrogen from the fuel to push the reaction along", "correct": False,
             "why": "The nitrogen is drawn in with the air, not supplied by "
                    "the fuel"},
        ],
        "figure": None,
    },
    {
        "id": "c8-07-s29",
        "band": "standard",
        "text": "A student writes: metal oxide + acid → salt. What is "
                "missing, and why does leaving it out matter?",
        "options": [
            {"text": "Hydrogen is missing, and it is the gas that proves the "
                     "reaction happened", "correct": False,
             "why": "Hydrogen comes off when an acid meets a metal. A metal "
                    "oxide gives no gas at all"},
            {"text": "Oxygen is missing, and it is released as the oxide "
                     "breaks apart", "correct": False,
             "why": "The oxide does not break apart to give off oxygen. Its "
                    "oxygen ends up in the water"},
            {"text": "Water is missing, and it is half of what neutralisation "
                     "produces", "correct": True},
            {"text": "The metal is missing, and it is left behind once the "
                     "acid has taken the oxygen", "correct": False,
             "why": "No metal is set free. The metal ends up inside the salt"},
        ],
        "figure": None,
    },
    {
        "id": "c8-07-s30",
        "band": "standard",
        "text": "Sodium oxide is a metal oxide that dissolves very freely in "
                "water. Predict the pH of the solution and give the reason.",
        "options": [
            {"text": "Around 7, because a metal oxide that dissolves has "
                     "nothing left to react with", "correct": False,
             "why": "A dissolved base gives an alkaline solution. Seven is "
                    "what an undissolved one leaves"},
            {"text": "Well below 7, because dissolving quickly releases a lot "
                     "of energy", "correct": False,
             "why": "Releasing energy does not set the direction. The side of "
                    "the table the element came from does"},
            {"text": "A little below 7, because sodium oxide is a gas once it "
                     "dissolves", "correct": False,
             "why": "Sodium oxide is a solid, and it is a base, so its "
                    "solution reads well above 7"},
            {"text": "Well above 7, because a base that dissolves gives an "
                     "alkaline solution", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c8-07-s31",
        "band": "standard",
        "text": "A gas is bubbled through a beaker of water until the "
                "reading falls to 3. A spatula of calcium oxide is then "
                "stirred in. What happens to the reading?",
        "options": [
            {"text": "It climbs back past 7, because the calcium oxide is a "
                     "base that dissolves", "correct": True},
            {"text": "It falls further, because anything added to water "
                     "lowers the reading", "correct": False,
             "why": "What is added decides the direction. A base takes the "
                    "reading up"},
            {"text": "It stays at 3, because a solid cannot undo what a gas "
                     "has done", "correct": False,
             "why": "A base neutralises an acid whichever way the acid "
                    "arrived in the water"},
            {"text": "It stops at exactly 7, because a base can never take a "
                     "solution past neutral", "correct": False,
             "why": "Only exactly enough base stops at 7. Spare dissolved "
                    "base carries on past it"},
        ],
        "figure": None,
    },
    {
        "id": "c8-07-s32",
        "band": "standard",
        "text": "Four elements were burned and each oxide was shaken with "
                "water, giving pH 12, pH 10, pH 5 and pH 3. How many of the "
                "four elements were metals?",
        "options": [
            {"text": "One", "correct": False,
             "why": "Two readings came out above 7, and each of those needed "
                    "a dissolved metal oxide"},
            {"text": "Two", "correct": True},
            {"text": "Three", "correct": False,
             "why": "Only two readings are above 7. A reading of 5 comes from "
                    "an acidic oxide"},
            {"text": "Four", "correct": False,
             "why": "Two of the four solutions are acidic, and no dissolved "
                    "metal oxide gives that"},
        ],
        "figure": None,
    },
    {
        "id": "c8-07-h08",
        "band": "harder",
        "text": "A lake measured at pH 4.5 is treated with powdered "
                "limestone and rises to pH 6.5 within a month. Over the "
                "following year it drifts back down to pH 5. What is the best "
                "explanation?",
        "options": [
            {"text": "The limestone slowly turned acidic itself once it had "
                     "been sitting in the cold lake water for a while",
             "correct": False,
             "why": "A carbonate does not become an acid by sitting in water. "
                    "It is used up by reacting"},
            {"text": "The pH probe drifted, and the lake was at 6.5 the whole "
                     "time", "correct": False,
             "why": "A steady drift over a year in one direction is the lake "
                    "changing, not an instrument fault"},
            {"text": "The limestone neutralised the acid already there, but "
                     "acidic rain kept arriving afterwards", "correct": True},
            {"text": "The fish that returned to the lake made it acidic "
                     "again", "correct": False,
             "why": "Fish returning is the aim of the treatment, and they do "
                    "not acidify the water"},
        ],
        "figure": None,
    },
    {
        "id": "c8-07-h09",
        "band": "harder",
        "text": "Two white powders are both metal oxides. One takes water to "
                "pH 12 and the other leaves it at 7. A student concludes the "
                "first is the stronger base. Why is that conclusion unsafe?",
        "options": [
            {"text": "Because neither powder is a base at all until it is put "
                     "into acid", "correct": False,
             "why": "A substance does not become a base by meeting an acid. "
                    "It was one before the acid arrived"},
            {"text": "Because two metal oxides can never be compared at "
                     "all, since every base behaves in its own way",
             "correct": False,
             "why": "They can be compared perfectly well — but by how they "
                    "react with acid, not by a water reading"},
            {"text": "Because the reading of 7 means that powder is neutral "
                     "and not a base", "correct": False,
             "why": "That repeats the student's mistake. A base that will not "
                    "dissolve still leaves the reading at 7"},
            {"text": "Because the reading compares how much dissolved, not "
                     "how well each reacts with acid", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c8-07-h10",
        "band": "harder",
        "text": "An oxide of a non-metal will not dissolve in water at all, "
                "so the pH stays at 7. How could you still show that it is an "
                "acidic oxide?",
        "options": [
            {"text": "React it with an alkali, and look for a salt and water "
                     "forming", "correct": True},
            {"text": "Stir it into water for far longer, until a reading "
                     "below 7 appears", "correct": False,
             "why": "Time does not dissolve a solid that will not dissolve. "
                    "The reading will not move"},
            {"text": "Grind it finer, since a powder always dissolves where a "
                     "lump does not", "correct": False,
             "why": "Grinding speeds up dissolving that would happen anyway. "
                    "It cannot make an insoluble solid soluble"},
            {"text": "React it with an acid, and look for a salt and water "
                     "forming", "correct": False,
             "why": "That is the test for a base. An acidic oxide is the "
                    "thing an alkali reacts with"},
        ],
        "figure": None,
    },
    {
        "id": "c8-07-h11",
        "band": "harder",
        "text": "Three unlabelled bottles hold calcium oxide, copper oxide "
                "and silicon dioxide. Only water, universal indicator and "
                "dilute hydrochloric acid are available. Which order of tests "
                "identifies all three?",
        "options": [
            {"text": "Acid first on all three, because the two that fizz are "
                     "the metal oxides", "correct": False,
             "why": "Neither metal oxide fizzes with acid. A gas comes off "
                    "from a carbonate, and none of these is one"},
            {"text": "Water and indicator first, then acid on the two that "
                     "gave 7", "correct": True},
            {"text": "Colour first, because the metal oxides are always "
                     "coloured and the non-metal oxide is white",
             "correct": False,
             "why": "Calcium oxide is white and so is silicon dioxide, so "
                    "colour separates nothing here"},
            {"text": "Water and indicator alone, because all three give "
                     "different readings", "correct": False,
             "why": "Two of the three leave the reading at 7, so water alone "
                    "cannot tell those two apart"},
        ],
        "figure": None,
    },
    {
        "id": "c8-07-h12",
        "band": "harder",
        "text": "A laboratory wants a solid on its benches that will "
                "neutralise spilt acid but will not make anything alkaline if "
                "it lands in water. Which of these oxides fits, and why?",
        "options": [
            {"text": "Sulfur dioxide, because a gas leaves nothing behind on "
                     "the bench", "correct": False,
             "why": "It is acidic, so it would add to a spill of acid rather "
                    "than neutralise it"},
            {"text": "Calcium oxide, because it is the strongest base on "
                     "the shelf and the only one that will touch an acid",
             "correct": False,
             "why": "It dissolves freely, so anything it landed in would turn "
                    "strongly alkaline"},
            {"text": "Copper oxide, because it is a base but will not "
                     "dissolve to give an alkaline solution", "correct": True},
            {"text": "Water, because it is an oxide and dilutes whatever it "
                     "meets", "correct": False,
             "why": "Diluting an acid is not neutralising it, and water makes "
                    "no salt with one"},
        ],
        "figure": None,
    },
    {
        "id": "c8-07-h13",
        "band": "harder",
        "text": "A student tests four oxides and records pH 12, 10, 7 and 3. "
                "They conclude that the more of an oxide you add, the further "
                "the reading moves. What single extra measurement would test "
                "that claim?",
        "options": [
            {"text": "Test four more oxides and see whether the pattern holds",
             "correct": False,
             "why": "More oxides vary two things at once. The claim is about "
                    "amount, so amount is what has to change on its own"},
            {"text": "Measure the temperature of each solution as well as its "
                     "pH", "correct": False,
             "why": "Temperature is not what the claim is about, so measuring "
                    "it settles nothing"},
            {"text": "Repeat the four readings on a different day to check "
                     "they are the same", "correct": False,
             "why": "Repeating shows the readings are reliable, but it never "
                    "changes the amount added"},
            {"text": "Test one of the oxides again at a larger mass and see "
                     "whether its reading moves", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c8-07-h14",
        "band": "harder",
        "text": "Copper oxide put into water does nothing, but put into "
                "sulfuric acid it disappears completely. A student says it "
                "dissolved in the acid. Why is that word doing two different "
                "jobs?",
        "options": [
            {"text": "In the acid it reacted and the new substance is what "
                     "went into solution", "correct": True},
            {"text": "In the acid it dissolved faster, because acid is a "
                     "better solvent than water", "correct": False,
             "why": "Nothing was dissolved in the ordinary sense. A reaction "
                    "made a different substance"},
            {"text": "In the water it also dissolved, but too little to see",
             "correct": False,
             "why": "Almost none of it dissolves, which is why the reading "
                    "does not move at all"},
            {"text": "In the acid the copper oxide melted rather than "
                     "dissolving", "correct": False,
             "why": "Melting needs great heat and gives a liquid oxide, not a "
                    "blue solution"},
        ],
        "figure": None,
    },
    {
        "id": "c8-07-h15",
        "band": "harder",
        "text": "Calcium oxide takes water to pH 12 and magnesium oxide to "
                "pH 10. An indigestion tablet uses magnesium oxide rather "
                "than calcium oxide. Suggest why.",
        "options": [
            {"text": "Calcium oxide is not a base, so it would not touch "
                     "stomach acid", "correct": False,
             "why": "Calcium is a metal, so calcium oxide is certainly a "
                    "base. That is not the reason"},
            {"text": "Both neutralise the acid, but magnesium oxide leaves a "
                     "far less alkaline solution behind", "correct": True},
            {"text": "Magnesium oxide dissolves far better than calcium "
                     "oxide does, so it works faster on the acid in a "
                     "stomach", "correct": False,
             "why": "Calcium oxide dissolves the more freely of the two, "
                    "which is why its reading is higher"},
            {"text": "Calcium oxide is acidic, so it would make the problem "
                     "worse", "correct": False,
             "why": "It takes water to pH 12, which is as far from acidic as "
                    "the bench gets"},
        ],
        "figure": None,
    },
    {
        "id": "c8-07-h16",
        "band": "harder",
        "text": "A student claims that any solution reading below 7 must "
                "have a non-metal oxide dissolved in it. Give a case that "
                "shows the claim is too strong.",
        "options": [
            {"text": "Copper oxide stirred into water, which reads 7 without "
                     "dissolving", "correct": False,
             "why": "That reading is 7, not below it, so it says nothing "
                    "about the claim"},
            {"text": "Rainwater, which reads about 6 and has nothing "
                     "dissolved in it at all", "correct": False,
             "why": "Rain reads about 6 precisely because carbon dioxide is "
                    "dissolved in it"},
            {"text": "Dilute hydrochloric acid, which reads well below 7 and "
                     "contains no oxide", "correct": True},
            {"text": "Sea water, which reads below 7 because of the salt in "
                     "it", "correct": False,
             "why": "Dissolved salt does not push a reading below 7, and sea "
                    "water is in fact slightly alkaline"},
        ],
        "figure": None,
    },
    {
        "id": "c8-07-h17",
        "band": "harder",
        "text": "Two lakes receive rain at pH 4. One lies on limestone "
                "bedrock and stays near pH 6.5; the other lies on granite and "
                "falls to pH 4.5. Explain the difference.",
        "options": [
            {"text": "Granite slowly releases an acid of its own into the "
                     "water, which adds to whatever the rain brought down",
             "correct": False,
             "why": "Granite is not adding acid. It simply does nothing to "
                    "the acid that arrives"},
            {"text": "The limestone lake is deeper, so the rain is diluted "
                     "more", "correct": False,
             "why": "Nothing in the description says either lake is deeper, "
                    "and dilution would slow the fall rather than stop it"},
            {"text": "Limestone dissolves and makes the water alkaline before "
                     "any rain arrives", "correct": False,
             "why": "Limestone barely dissolves. It works by reacting with "
                    "acid as the acid comes in"},
            {"text": "Limestone reacts with the acid as it arrives, so the "
                     "bedrock neutralises it continuously", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c8-07-h18",
        "band": "harder",
        "text": "A power station removes sulfur dioxide from its flue gas by "
                "spraying the gas with a slurry of powdered limestone. "
                "Explain why that works.",
        "options": [
            {"text": "The acidic gas is neutralised by the limestone before "
                     "it leaves the chimney", "correct": True},
            {"text": "The water in the slurry cools the gas so it condenses "
                     "into a liquid", "correct": False,
             "why": "Cooling a gas does not remove it, and sulfur dioxide "
                    "would simply escape once it warmed again"},
            {"text": "The limestone is a non-metal oxide, so like attracts "
                     "like and it holds the gas", "correct": False,
             "why": "Limestone is a carbonate of a metal, and substances do "
                    "not capture one another by being alike"},
            {"text": "The limestone dust makes the gas heavier so it falls "
                     "back down the chimney", "correct": False,
             "why": "Nothing falls back down a chimney, and weight is not "
                    "what removes the gas"},
        ],
        "figure": None,
    },
    {
        "id": "c8-07-h19",
        "band": "harder",
        "text": "A class measures local rainwater every week for a year. The "
                "readings range from pH 4.2 to pH 6.1 and never reach 7. What "
                "would be the wrong conclusion to draw from never reaching 7?",
        "options": [
            {"text": "That some weeks were more acidic than others",
             "correct": False,
             "why": "The range from 4.2 to 6.1 is exactly what that "
                    "conclusion rests on, so it is sound"},
            {"text": "That the whole area must be unusually polluted",
             "correct": True},
            {"text": "That the lowest readings are worth investigating "
                     "further", "correct": False,
             "why": "A reading of 4.2 is well below what clean rain gives, so "
                    "looking into it is reasonable"},
            {"text": "That the rain always has something acidic dissolved in "
                     "it", "correct": False,
             "why": "That much is true of all rain, because carbon dioxide "
                    "from the air dissolves in every drop"},
        ],
        "figure": None,
    },
    {
        "id": "c8-07-h20",
        "band": "harder",
        "text": "Two beakers of pure water are left open for a week. One is "
                "in a sealed room with a carbon dioxide supply running; the "
                "other is in ordinary fresh air. What will a pH probe find in "
                "each?",
        "options": [
            {"text": "Both stay at exactly 7, because nothing has been added "
                     "to either", "correct": False,
             "why": "A gas from the air counts as something added. Carbon "
                    "dioxide dissolves into both"},
            {"text": "The sealed one falls and the open one rises above 7",
             "correct": False,
             "why": "Nothing in ordinary air is a base, so the open beaker "
                    "has no way of going above 7"},
            {"text": "Both fall below 7, and the sealed one falls further",
             "correct": True},
            {"text": "The sealed one rises, because carbon dioxide is what "
                     "plants use and it is not acidic", "correct": False,
             "why": "What a gas is used for elsewhere says nothing about its "
                    "solution. Carbon dioxide dissolves to give an acid"},
        ],
        "figure": None,
    },
    {
        "id": "c8-07-h21",
        "band": "harder",
        "text": "A gas collected near a volcano is bubbled through water and "
                "the reading drops to 3. A second sample is passed over warm "
                "powdered calcium oxide and almost none comes out the far "
                "end. What has happened?",
        "options": [
            {"text": "The calcium oxide has cooled the gas until it turned "
                     "into a liquid", "correct": False,
             "why": "The powder is warm, and cooling would not hold a gas "
                    "back in any case"},
            {"text": "The gas is a metal oxide, and two metal oxides stick "
                     "together whenever one of them is warm", "correct": False,
             "why": "A metal oxide would have pushed the first reading above "
                    "7, not down to 3"},
            {"text": "The powder has filtered out the dust the gas was "
                     "carrying", "correct": False,
             "why": "Removing dust would not stop the gas itself coming "
                    "through"},
            {"text": "The gas is an acidic oxide and the calcium oxide, a "
                     "base, has reacted with it", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c8-07-h22",
        "band": "harder",
        "text": "Four oxides give pH 12, 10, 7 and 3 in water. A fifth oxide "
                "is tested and also gives 7. What can you be sure of, and "
                "what can you not decide?",
        "options": [
            {"text": "Sure the solution is neutral; undecided whether the "
                     "oxide is of a metal or a non-metal", "correct": True},
            {"text": "Sure the oxide itself is neutral; undecided how much "
                     "of it dissolved", "correct": False,
             "why": "The oxide itself may be a base that would not dissolve. "
                    "Only the solution is neutral"},
            {"text": "Sure the oxide is of a metal; undecided whether it "
                     "dissolved", "correct": False,
             "why": "Water is a non-metal oxide and reads 7 as well, so the "
                    "side of the table is not settled"},
            {"text": "Sure it did not dissolve; undecided whether it is a "
                     "base", "correct": False,
             "why": "Water reads 7 having dissolved nothing at all, so a "
                    "reading of 7 cannot prove a solid stayed out of "
                    "solution"},
        ],
        "figure": None,
    },
    {
        "id": "c8-07-h23",
        "band": "harder",
        "text": "The same metal oxide is neutralised once with hydrochloric "
                "acid and once with sulfuric acid, and two different salts "
                "come out. Explain how one base gives two salts.",
        "options": [
            {"text": "The base itself changes into a different substance, "
                     "depending on how strong the acid that is poured on it "
                     "is", "correct": False,
             "why": "The base is the same substance in both flasks. What "
                    "changes is what it is reacting with"},
            {"text": "The second half of a salt's name comes from the acid, "
                     "so a different acid gives a different salt",
             "correct": True},
            {"text": "One of the two reactions is not really neutralisation, "
                     "so it gives something else", "correct": False,
             "why": "Both are neutralisation, and both give a salt and water"},
            {"text": "The metal ends up in only one of the two salts, which "
                     "is why they differ", "correct": False,
             "why": "The metal is in both salts. It supplies the first half "
                    "of each name"},
        ],
        "figure": None,
    },
    {
        "id": "c8-07-h24",
        "band": "harder",
        "text": "A teacher wants to show a class that a non-metal oxide "
                "gives an acidic solution, without burning any sulfur. "
                "Suggest the simplest way.",
        "options": [
            {"text": "Stir magnesium oxide into water with indicator, and "
                     "point out that the colour changed", "correct": False,
             "why": "Magnesium is a metal, so that shows the opposite of what "
                    "is wanted"},
            {"text": "Warm some water with indicator, since heating drives "
                     "the reading down", "correct": False,
             "why": "Heating water does not add an oxide to it, so it "
                    "demonstrates nothing about oxides"},
            {"text": "Breathe out through a straw into water with indicator, "
                     "since breath carries carbon dioxide", "correct": True},
            {"text": "Add a spoonful of copper oxide to water with indicator "
                     "and wait", "correct": False,
             "why": "Copper is a metal, and its oxide does not dissolve, so "
                    "the colour will not move at all"},
        ],
        "figure": None,
    },
    {
        "id": "c8-07-h25",
        "band": "harder",
        "text": "An oxide is stirred into water. The reading does not move "
                "from 7, and nothing at all is left on the bottom of the "
                "beaker. What can you conclude?",
        "options": [
            {"text": "It is a metal oxide that would not dissolve, like "
                     "copper oxide", "correct": False,
             "why": "An oxide that would not dissolve would still be sitting "
                    "on the bottom where it was put"},
            {"text": "It is an acidic oxide too weak for the indicator to "
                     "pick up", "correct": False,
             "why": "An acidic oxide that had dissolved would move the "
                    "reading below 7"},
            {"text": "It must have evaporated, which is why nothing is left",
             "correct": False,
             "why": "An oxide stirred into cold water does not evaporate out "
                    "of the beaker"},
            {"text": "It went into solution and that solution is neutral",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c8-07-h26",
        "band": "harder",
        "text": "Copper oxide is added to warm dilute sulfuric acid until no "
                "more will react, and the mixture is filtered. What is on the "
                "filter paper, what is in the liquid, and what does that "
                "prove?",
        "options": [
            {"text": "Unreacted copper oxide on the paper, copper sulfate "
                     "solution in the liquid — a base made a salt and water",
             "correct": True},
            {"text": "Copper metal on the paper, sulfuric acid in the liquid "
                     "— the acid pulled the oxygen off the copper",
             "correct": False,
             "why": "No copper metal is set free. The copper ends up inside "
                    "the salt"},
            {"text": "Nothing on the paper, copper sulfate in the liquid — "
                     "all the copper oxide dissolved in the water as any "
                     "powder would", "correct": False,
             "why": "Copper oxide does not dissolve in water, and spare "
                    "powder is left because the acid ran out first"},
            {"text": "Copper sulfate on the paper, water in the liquid — the "
                     "salt is the solid product", "correct": False,
             "why": "Copper sulfate dissolves, so it passes through the paper "
                    "with the liquid"},
        ],
        "figure": None,
    },
    {
        "id": "c8-07-h27",
        "band": "harder",
        "text": "A student says sulfur dioxide acidifies rain more than "
                "carbon dioxide does because sulfur is the heavier element. "
                "Identify the flaw and give the real reason.",
        "options": [
            {"text": "Mass is not the reason; the real reason is that there "
                     "is far more sulfur dioxide in the air than carbon "
                     "dioxide", "correct": False,
             "why": "There is far more carbon dioxide in the air, and how "
                    "common a gas is does not set how acidic its solution "
                    "will be"},
            {"text": "Mass is not the reason; sulfur dioxide dissolves to "
                     "give a much more acidic solution", "correct": True},
            {"text": "There is no flaw, since heavier gases do dissolve more "
                     "in water", "correct": False,
             "why": "How heavy a gas is does not set how acidic its solution "
                    "will be"},
            {"text": "The flaw is the direction; carbon dioxide is in fact "
                     "the more acidic of the two", "correct": False,
             "why": "Carbon dioxide takes water to about 5 and sulfur dioxide "
                    "to about 3, so the direction was right"},
        ],
        "figure": None,
    },
    {
        "id": "c8-07-h28",
        "band": "harder",
        "text": "Nitrogen makes up most of the air and rain is not acidified "
                "by it, yet nitrogen oxides acidify rain badly. What has to "
                "happen to the nitrogen first, and where?",
        "options": [
            {"text": "It has to dissolve in the cloud, which happens only in "
                     "cold weather", "correct": False,
             "why": "Nitrogen dissolving in water changes no reading. It has "
                    "to become an oxide first"},
            {"text": "It has to be released by burning fuel, which happens in "
                     "the engine", "correct": False,
             "why": "The nitrogen is not in the fuel. It is drawn in with the "
                    "air"},
            {"text": "It has to join with oxygen, which needs the heat inside "
                     "an engine or a furnace", "correct": True},
            {"text": "It has to be split into single atoms, which happens in "
                     "sunlight high up", "correct": False,
             "why": "Single nitrogen atoms are not what falls in rain. An "
                    "oxide is what dissolves and acidifies it"},
        ],
        "figure": None,
    },
    {
        "id": "c8-07-h29",
        "band": "harder",
        "text": "A water tank has drifted to pH 5 and must be brought back "
                "to 7. Calcium oxide, copper oxide and powdered sulfur are on "
                "the shelf. Which should be used, and why do the others fail?",
        "options": [
            {"text": "Copper oxide — it is a base and dissolves gently, "
                     "while calcium oxide would overshoot and sulfur would do "
                     "nothing at all", "correct": False,
             "why": "Copper oxide barely dissolves, so it cannot move the "
                    "reading of a tank of water"},
            {"text": "Powdered sulfur — it is an element, so it neutralises "
                     "without adding a compound", "correct": False,
             "why": "Being an element neutralises nothing, and sulfur is on "
                    "the acidic side of the table"},
            {"text": "None of them — only an alkali bought as a solution can "
                     "move a pH reading", "correct": False,
             "why": "A metal oxide that dissolves makes an alkaline solution "
                    "in the tank itself"},
            {"text": "Calcium oxide — copper oxide will not dissolve enough "
                     "to move the reading, and sulfur burns to an acidic "
                     "oxide", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c8-07-h30",
        "band": "harder",
        "text": "School A, beside a motorway, records rain averaging pH 4.8 "
                "over a term. School B, in open country, records pH 5.9. Both "
                "report acidic rain. Which school has evidence of an unusual "
                "cause?",
        "options": [
            {"text": "School A, because nitrogen oxides from hot engines add "
                     "to the carbon dioxide every sample carries",
             "correct": True},
            {"text": "School B, because country air should give readings "
                     "above 7 and it did not", "correct": False,
             "why": "No rain reads above 7. Dissolved carbon dioxide keeps "
                    "every sample slightly acidic"},
            {"text": "Both of them, because any reading below 7 is evidence "
                     "of pollution, wherever in the country it was "
                     "collected", "correct": False,
             "why": "Clean rain is already about pH 6, so a reading below 7 "
                    "on its own is evidence of nothing"},
            {"text": "Neither, because a term is far too short a period for "
                     "rain to be measured at all", "correct": False,
             "why": "A term of weekly samples is plenty to show a difference "
                    "of more than a whole pH point"},
        ],
        "figure": None,
    },
    {
        "id": "c8-07-h31",
        "band": "harder",
        "text": "Magnesium burns with a brilliant white light and leaves a "
                "white powder. A student says the powder is just the "
                "magnesium that failed to burn. Which pair of results settles "
                "it?",
        "options": [
            {"text": "The powder is a different colour from the ribbon, and "
                     "it is a powder rather than a strip", "correct": False,
             "why": "Colour and shape both change when a metal is crushed or "
                    "heated, so neither proves a new substance"},
            {"text": "The powder weighs more than the ribbon did, and stirred "
                     "into water it takes the reading to 10", "correct": True},
            {"text": "The powder weighs less than the ribbon did, and it will "
                     "not conduct electricity", "correct": False,
             "why": "Oxygen has joined on, so the mass goes up rather than "
                    "down"},
            {"text": "The powder will not burn again, and it floats on water",
             "correct": False,
             "why": "Plenty of substances neither burn nor sink, so that pair "
                    "identifies nothing"},
        ],
        "figure": None,
    },
    {
        "id": "c8-07-h32",
        "band": "harder",
        "text": "One oxide gives pH 3 in water and another gives pH 12. "
                "Equal amounts of the two solutions are poured together. "
                "Predict the reading and explain it.",
        "options": [
            {"text": "Still 3, because an acid cannot be undone once it has "
                     "formed", "correct": False,
             "why": "An acid is undone by a base. That is what neutralisation "
                    "is"},
            {"text": "Still 12, because the stronger of the two readings "
                     "always wins", "correct": False,
             "why": "Neither reading wins. The acid and the base react with "
                    "each other"},
            {"text": "Near 7, because an acidic solution and an alkaline one "
                     "neutralise each other", "correct": True},
            {"text": "Near 15, because the two readings add together",
             "correct": False,
             "why": "Readings do not add, and the scale does not go that far "
                    "in any case"},
        ],
        "figure": None,
    },
]
