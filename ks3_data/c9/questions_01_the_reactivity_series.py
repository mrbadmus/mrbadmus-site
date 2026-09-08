"""C9 lesson 01 — The reactivity series: twelve questions (MRB-281).

The lesson's argument is one shape: reactivity is a property of the element,
it is settled by evidence rather than by how a metal looks or feels, and the
order it produces holds for every reaction and not just the test that made it.
The page teaches it with twelve tubes — six metals against cold water and
dilute acid — and a bench that sorts them into three bands.

These twelve probe the angles the mastery ladder leaves alone: what a null
result is worth, why two tests are needed rather than one, and what carbon is
doing in a list of metals.

The distractors are built from the lesson's declared misconceptions.

`MATL-01` (a metal that does nothing in cold water is unreactive) drives the
wrong options in e02, s01 and h01. Each treats one liquid as a verdict. s01 is
the one that matters: it gives a metal that fails the water test and passes the
acid one, so the belief has to account for a result it has already seen.

`MATL-02` (reactivity is strength or hardness) drives e03, s03 and h02, where
a physical property is read as a chemical one.

`MATL-03` (carbon cannot belong in an order of metals) drives e04 and h04.

⚠️ **NO QUESTION ASKS A STUDENT TO PUT POTASSIUM IN ACID.** The lesson's own
bench declines that cell on safety grounds (§5 flag 2) and a question that
asked for the result would undo the decline.

⚠️ MRB-278 · ANSWER POSITION. The correct answer's index cycles 0, 1, 2, 3
through each band, so this file holds three of each.

⚠️ BAND VALUES ARE FULL WORDS — `easier`, `standard`, `harder`, never the
letters.
"""

UNIT = "C9"
LESSON = "the-reactivity-series"
LESSON_NUMBER = 1

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "c9-01-e01",
        "band": "easier",
        "text": "What does a metal's position in the reactivity series tell "
                "you?",
        "options": [
            {"text": "How readily it takes part in a chemical reaction",
             "correct": True},
            {"text": "How hard it is to scratch or cut with a knife",
             "correct": False,
             "why": "Sodium is soft enough to cut and near the top; steel is "
                    "hard and low down."},
            {"text": "How much one cubic centimetre of it weighs",
             "correct": False,
             "why": "Density is a separate property. Lithium floats and is "
                    "highly reactive."},
            {"text": "How long ago it was first discovered by chemists",
             "correct": False,
             "why": "Gold has been known for millennia and is the least "
                    "reactive metal on the list."},
        ],
        "figure": None,
    },
    {
        "id": "c9-01-e02",
        "band": "easier",
        "text": "Iron granules sit unchanged in cold water but fizz gently in "
                "dilute acid. What does that tell you?",
        "options": [
            {"text": "Iron is unreactive, because the water test showed "
                     "nothing",
             "correct": False,
             "why": "One liquid is not a verdict. The acid test shows iron "
                    "reacting perfectly well."},
            {"text": "Iron is in the middle of the series — below the metals "
                     "that manage water",
             "correct": True},
            {"text": "Iron is at the top of the series, because it reacted at "
                     "all",
             "correct": False,
             "why": "The top of the series reacts with cold water alone. Iron "
                    "needs acid."},
            {"text": "The water must have been contaminated in some way",
             "correct": False,
             "why": "Iron genuinely does almost nothing in cold water. The "
                    "result is real."},
        ],
        "figure": None,
    },
    {
        "id": "c9-01-e03",
        "band": "easier",
        "text": "Magnesium ribbon bends between your fingers. A steel nail "
                "does not. Which is higher in the reactivity series?",
        "options": [
            {"text": "Steel, because a stiffer metal holds itself together "
                     "better",
             "correct": False,
             "why": "Stiffness is a physical property. It says nothing about "
                    "reactions."},
            {"text": "Neither — bending has nothing to do with the series at "
                     "all",
             "correct": False,
             "why": "True that bending is irrelevant, but one of them IS "
                    "higher: magnesium is."},
            {"text": "Magnesium, and its softness is beside the point",
             "correct": True},
            {"text": "Steel, because iron is a stronger element than "
                     "magnesium",
             "correct": False,
             "why": "Strength and reactivity are different properties, and "
                    "magnesium is above iron."},
        ],
        "figure": None,
    },
    {
        "id": "c9-01-e04",
        "band": "easier",
        "text": "Carbon is a non-metal. Why is it in the reactivity series at "
                "all?",
        "options": [
            {"text": "Because it is found in the same rocks as many metals "
                     "are",
             "correct": False,
             "why": "Where an element is found does not put it in an order "
                    "of reactivity."},
            {"text": "Because it was discovered at the same time as the "
                     "metals were",
             "correct": False,
             "why": "Discovery dates have nothing to do with the order."},
            {"text": "Because it is a solid at room temperature, like most "
                     "metals",
             "correct": False,
             "why": "So is sulfur, and sulfur is not in the series."},
            {"text": "Because it can take oxygen away from the oxides of "
                     "metals below it",
             "correct": True},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "c9-01-s01",
        "band": "standard",
        "text": "A student concludes that zinc is unreactive because it does "
                "nothing in cold water. What is the flaw?",
        "options": [
            {"text": "Doing nothing in one liquid only rules out the top of "
                     "the series",
             "correct": True},
            {"text": "The zinc was probably coated and needed cleaning first",
             "correct": False,
             "why": "Even clean zinc does nothing in cold water. The result "
                    "is real and it is informative."},
            {"text": "There is no flaw — nothing happened, so zinc is "
                     "unreactive",
             "correct": False,
             "why": "Zinc fizzes steadily in dilute acid, which an unreactive "
                    "metal would not do."},
            {"text": "Cold water is not a valid test for any metal",
             "correct": False,
             "why": "It is the test that separates the top three of the "
                    "series from everything else."},
        ],
        "figure": None,
    },
    {
        "id": "c9-01-s02",
        "band": "standard",
        "text": "Why does the reactivity series need two tests rather than "
                "one?",
        "options": [
            {"text": "Because a single test might have been done incorrectly "
                     "the first time",
             "correct": False,
             "why": "Repeating a test checks the test. A DIFFERENT test is "
                    "what separates a different part of the list."},
            {"text": "Because water separates the top and acid separates the "
                     "middle",
             "correct": True},
            {"text": "Because acids react with every metal and water reacts "
                     "with none",
             "correct": False,
             "why": "Copper does nothing in acid, and potassium is violent in "
                    "water. Neither half is true."},
            {"text": "Because two results always give a more accurate average",
             "correct": False,
             "why": "These are not measurements being averaged. They are two "
                    "different questions."},
        ],
        "figure": None,
    },
    {
        "id": "c9-01-s03",
        "band": "standard",
        "text": "Gold is used for jewellery that is worn every day for "
                "decades. Which property makes it suitable?",
        "options": [
            {"text": "It is the hardest metal, so it resists scratching",
             "correct": False,
             "why": "Gold is notably soft — soft enough that it is usually "
                    "alloyed before use."},
            {"text": "It is the heaviest metal, so it feels substantial",
             "correct": False,
             "why": "It is dense, and that is not why it survives being "
                    "worn."},
            {"text": "It is at the bottom of the reactivity series and does "
                     "not react",
             "correct": True},
            {"text": "It conducts heat well, so it warms to the skin quickly",
             "correct": False,
             "why": "Every metal conducts heat well. That is not what keeps "
                    "it looking new."},
        ],
        "figure": None,
    },
    {
        "id": "c9-01-s04",
        "band": "standard",
        "text": "Potassium is not put into dilute acid on the bench in this "
                "lesson. Why not?",
        "options": [
            {"text": "Because potassium does not react with acids at all",
             "correct": False,
             "why": "It would react — far too fast. That is the reason it is "
                    "not done."},
            {"text": "Because the acid would be neutralised before anything "
                     "happened",
             "correct": False,
             "why": "Nothing here neutralises the acid, and the reaction "
                    "would begin at once."},
            {"text": "Because acid results cannot be compared with water "
                     "results",
             "correct": False,
             "why": "They are compared throughout — that is how the bands are "
                    "built."},
            {"text": "Because dilute acid is mostly water and potassium is "
                     "violent with water alone",
             "correct": True},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "c9-01-h01",
        "band": "harder",
        "text": "An unknown metal does nothing in cold water, does nothing in "
                "dilute acid, and is displaced from its sulfate by iron. "
                "Where does it sit?",
        "options": [
            {"text": "Below iron and near the bottom of the series",
             "correct": True},
            {"text": "Above iron, because it survived both liquid tests "
                     "unchanged",
             "correct": False,
             "why": "Surviving both tests puts it BELOW the metals that "
                    "react, not above them."},
            {"text": "At the very top, because nothing was able to change it",
             "correct": False,
             "why": "The top of the series is the most reactive part of it. "
                    "This metal reacted with nothing."},
            {"text": "Nowhere — three results that disagree cannot place a "
                     "metal",
             "correct": False,
             "why": "The three results agree perfectly. All of them put it "
                    "low."},
        ],
        "figure": None,
    },
    {
        "id": "c9-01-h02",
        "band": "harder",
        "text": "Aluminium is high in the reactivity series, yet an aluminium "
                "pan can be filled with water and boiled with nothing "
                "happening. Why?",
        "options": [
            {"text": "The series is wrong about aluminium and should place it "
                     "lower",
             "correct": False,
             "why": "The position is right and is confirmed by how hard "
                    "aluminium is to extract."},
            {"text": "An oxide layer forms in air and keeps the water off the "
                     "metal",
             "correct": True},
            {"text": "Aluminium only reacts once it has been heated well "
                     "above boiling",
             "correct": False,
             "why": "Fresh aluminium reacts at room temperature. The coating "
                    "is what prevents it."},
            {"text": "Pans are made from an alloy that contains no aluminium "
                     "at all",
             "correct": False,
             "why": "They are aluminium. The coating is the explanation, not "
                    "the composition."},
        ],
        "figure": None,
    },
    {
        "id": "c9-01-h03",
        "band": "harder",
        "text": "Why is “nothing happened” treated as evidence in "
                "this lesson rather than as a failed experiment?",
        "options": [
            {"text": "Because every experiment must be recorded whether it "
                     "worked or not",
             "correct": False,
             "why": "True as a habit, and it is not why this particular null "
                    "result is useful."},
            {"text": "Because a result that is repeated becomes reliable over "
                     "time",
             "correct": False,
             "why": "Repetition checks a result. It does not turn a null one "
                    "into information."},
            {"text": "Because it rules out part of the series and narrows "
                     "where the metal can be",
             "correct": True},
            {"text": "Because it shows the apparatus was working correctly "
                     "throughout",
             "correct": False,
             "why": "It shows nothing about the apparatus. It shows something "
                    "about the metal."},
        ],
        "figure": None,
    },
    {
        "id": "c9-01-h04",
        "band": "harder",
        "text": "Where does carbon's position in the series come from, given "
                "that it does not react with water or acid the way the metals "
                "do?",
        "options": [
            {"text": "From its atomic mass, which falls between magnesium's "
                     "and zinc's",
             "correct": False,
             "why": "Mass has no bearing on the order. Carbon is far lighter "
                    "than both."},
            {"text": "From an average of the metals on either side of it in "
                     "the list",
             "correct": False,
             "why": "A position cannot be averaged into existence. It has to "
                    "be earned by a result."},
            {"text": "From the fact that it is a solid, like the metals "
                     "around it",
             "correct": False,
             "why": "Sulfur is a solid too and has no place in the series."},
            {"text": "From which metal oxides it can and cannot take the "
                     "oxygen from",
             "correct": True},
        ],
        "figure": None,
    },

    # ── easier · MRB-335 top-up ─────────────────────────────────────────
    {
        "id": "c9-01-e05",
        "band": "easier",
        "text": "Which TWO liquids are used on the bench to place a metal in "
                "the series?",
        "options": [
            {"text": "Cold water and dilute acid",
             "correct": True},
            {"text": "Cold water and hot water, since the same liquid at two "
                     "temperatures separates the metals further down the list "
                     "than one temperature can on its own",
             "correct": False,
             "why": "Hot water reaches a little further and is not the "
                    "standard pair. Dilute acid is the second test"},
            {"text": "Dilute acid and concentrated acid",
             "correct": False,
             "why": "Concentration changes how fast a possible reaction goes. "
                    "It does not reach a different part of the series"},
            {"text": "Water and oil",
             "correct": False,
             "why": "Oil is what reactive metals are STORED under. It is not "
                    "a test"},
        ],
        "figure": None,
    },
    {
        "id": "c9-01-e06",
        "band": "easier",
        "text": "Which three metals from the series react with COLD WATER?",
        "options": [
            {"text": "Magnesium, zinc and iron",
             "correct": False,
             "why": "Those are the middle three — they need dilute acid "
                    "before much happens"},
            {"text": "Potassium, sodium and calcium",
             "correct": True},
            {"text": "Copper, silver and gold",
             "correct": False,
             "why": "Those are the bottom three, and they react with neither "
                    "water nor acid"},
            {"text": "Zinc, iron and lead, because these are the metals most "
                     "often found in pipes and tanks that hold water for "
                     "years at a time",
             "correct": False,
             "why": "Being used for water pipes shows the opposite — a metal "
                    "that reacted with water would be useless for it"},
        ],
        "figure": None,
    },
    {
        "id": "c9-01-e07",
        "band": "easier",
        "text": "Which gas is given off when a metal reacts with water, and "
                "also when it reacts with dilute acid?",
        "options": [
            {"text": "Oxygen, which is the gas the water and the acid both "
                     "hold and the one a reactive metal takes from them as it "
                     "reacts",
             "correct": False,
             "why": "The metal takes the oxygen in some other reactions, and "
                    "the gas that bubbles off here pops with a lit splint"},
            {"text": "Carbon dioxide",
             "correct": False,
             "why": "There is no carbon in either liquid or in the metal"},
            {"text": "Hydrogen",
             "correct": True},
            {"text": "A different gas each time",
             "correct": False,
             "why": "The same gas from both is a clue worth having — it comes "
                    "from the hydrogen in the water and in the acid"},
        ],
        "figure": None,
    },
    {
        "id": "c9-01-e08",
        "band": "easier",
        "text": "What is dilute acid used for on this bench?",
        "options": [
            {"text": "To clean the surface of each metal before it is tested, "
                     "so that any oxide layer already on it is removed and "
                     "the fresh metal is exposed",
             "correct": False,
             "why": "Cleaning is sometimes done, and the acid here is a TEST "
                    "in its own right"},
            {"text": "To dissolve the metals so they can be weighed",
             "correct": False,
             "why": "Nothing is weighed. What is watched for is whether a "
                    "reaction happens at all"},
            {"text": "To separate the top three metals from each other, since "
                     "cold water on its own cannot tell them apart",
             "correct": False,
             "why": "Water already separates the top. Acid reaches further "
                    "down the list"},
            {"text": "To separate the metals in the MIDDLE of the series, "
                     "where cold water gives nothing",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c9-01-e09",
        "band": "easier",
        "text": "Potassium and sodium are kept in jars under oil. What is the "
                "oil doing?",
        "options": [
            {"text": "Keeping air and water vapour off the metal",
             "correct": True},
            {"text": "Keeping the metal cool, since both of them react so "
                     "readily that they would warm up and eventually catch "
                     "fire on a shelf in an ordinary room",
             "correct": False,
             "why": "Neither warms up on its own. The oil is a barrier "
                    "against air and water vapour"},
            {"text": "Stopping the metal from evaporating",
             "correct": False,
             "why": "Neither evaporates at room temperature. What reaches "
                    "them is the air"},
            {"text": "Making them easier to cut",
             "correct": False,
             "why": "Both cut easily with a knife. The oil is there for "
                    "protection"},
        ],
        "figure": None,
    },
    {
        "id": "c9-01-e10",
        "band": "easier",
        "text": "Which metal is at the very BOTTOM of the reactivity series?",
        "options": [
            {"text": "Copper",
             "correct": False,
             "why": "Copper is low and there are two metals below it — silver "
                    "and gold"},
            {"text": "Gold",
             "correct": True},
            {"text": "Lead",
             "correct": False,
             "why": "Lead is low in the series and sits above copper, silver "
                    "and gold"},
            {"text": "Iron, because it is the metal used for almost "
                     "everything that has to last, and lasting is what being "
                     "low in the series means",
             "correct": False,
             "why": "Iron rusts readily, which is exactly what being in the "
                    "middle of the series looks like"},
        ],
        "figure": None,
    },
    {
        "id": "c9-01-e11",
        "band": "easier",
        "text": "Which of these does NOT react with dilute acid?",
        "options": [
            {"text": "Magnesium",
             "correct": False,
             "why": "Magnesium fizzes vigorously in dilute acid"},
            {"text": "Zinc",
             "correct": False,
             "why": "Zinc reacts steadily in dilute acid"},
            {"text": "Copper",
             "correct": True},
            {"text": "Iron, which sits so low in the series that nothing on "
                     "a school bench will make it react with anything at all",
             "correct": False,
             "why": "Iron is in the middle, not the bottom, and it fizzes "
                    "gently in dilute acid"},
        ],
        "figure": None,
    },
    {
        "id": "c9-01-e12",
        "band": "easier",
        "text": "What does the reactivity series let you do?",
        "options": [
            {"text": "Look up which metals were discovered first, since the "
                     "order they were found in follows the order they sit in "
                     "on the list",
             "correct": False,
             "why": "The two orders are loosely related and the series is not "
                    "a history. It predicts reactions"},
            {"text": "Work out how much a metal costs to buy, by reading its "
                     "price off the list",
             "correct": False,
             "why": "Cost depends on extraction and demand. The series says "
                    "nothing about price directly"},
            {"text": "Decide which metal is strongest",
             "correct": False,
             "why": "Strength is a separate property that the series does not "
                    "record at all"},
            {"text": "Predict how metals will behave in reactions you have "
                     "not run",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c9-01-e13",
        "band": "easier",
        "text": "Sodium reacts with cold water. What is left in the trough "
                "afterwards, besides the gas?",
        "options": [
            {"text": "An alkaline solution, because a metal hydroxide has "
                     "dissolved in the water",
             "correct": True},
            {"text": "Nothing at all — the sodium has been used up entirely "
                     "and the trough holds exactly the water it held before "
                     "the metal was dropped in",
             "correct": False,
             "why": "Every sodium atom is still there, dissolved as a "
                    "hydroxide. Test the water and it is alkaline"},
            {"text": "An acidic solution",
             "correct": False,
             "why": "The other way round. Universal indicator goes purple, "
                    "which is above 7"},
            {"text": "A layer of solid sodium oxide on the bottom, because the "
                     "sodium has combined with oxygen",
             "correct": False,
             "why": "The oxide forms in air. In water the product dissolves "
                    "as a hydroxide"},
        ],
        "figure": None,
    },

    # ── standard · MRB-335 top-up ───────────────────────────────────────
    {
        "id": "c9-01-s05",
        "band": "standard",
        "text": "How a metal has to be STORED is described as a clue to its "
                "position. What does needing oil tell you?",
        "options": [
            {"text": "That it reacts with air or water vapour readily, so it "
                     "sits near the top",
             "correct": True},
            {"text": "That it is valuable enough to be worth protecting, "
                     "which is why the least common metals are the ones kept "
                     "most carefully in a prep room",
             "correct": False,
             "why": "Gold is the most valuable and needs no oil at all. The "
                    "oil is about chemistry"},
            {"text": "That it is poisonous",
             "correct": False,
             "why": "Plenty of poisonous substances need no oil. The oil "
                    "keeps a REACTION from happening"},
            {"text": "That it melts at a low temperature, and so has to be "
                     "kept cool as well as covered up",
             "correct": False,
             "why": "Sodium does melt low, and that is not what the oil is "
                    "for"},
        ],
        "figure": None,
    },
    {
        "id": "c9-01-s06",
        "band": "standard",
        "text": "Two metals both sit unchanged in cold water. What would you "
                "do next to tell them apart?",
        "options": [
            {"text": "Leave both in the water for a week, since a slow "
                     "reaction will show itself given long enough and only "
                     "one of them is likely to be genuinely unreactive",
             "correct": False,
             "why": "Neither reacts with water at any speed. Waiting buys "
                    "nothing — a second test does"},
            {"text": "Put each into dilute acid and see which of them fizzes",
             "correct": True},
            {"text": "Weigh both of them carefully and compare the two masses "
                     "you record",
             "correct": False,
             "why": "Mass says nothing about reactivity"},
            {"text": "Heat the water",
             "correct": False,
             "why": "Hot water reaches a little further down, and it is not "
                    "the standard second test. Acid is"},
        ],
        "figure": None,
    },
    {
        "id": "c9-01-s07",
        "band": "standard",
        "text": "A metal does nothing in cold water but fizzes gently in "
                "dilute acid. Where does that place it?",
        "options": [
            {"text": "At the top, because reacting with acid is the more "
                     "demanding of the two tests and a metal that passes it "
                     "has shown itself to be highly reactive",
             "correct": False,
             "why": "Water is the more demanding test. Anything that reacts "
                    "with cold water reacts with acid violently"},
            {"text": "At the bottom",
             "correct": False,
             "why": "The bottom three react with neither. This one reacts "
                    "with one of them"},
            {"text": "In the middle — below the metals that manage water, "
                     "above the ones that manage neither",
             "correct": True},
            {"text": "It cannot be placed from only two results, because a "
                     "third test would be needed before deciding anything",
             "correct": False,
             "why": "Two results bracket it between two groups, which is "
                    "exactly what placing means"},
        ],
        "figure": None,
    },
    {
        "id": "c9-01-s08",
        "band": "standard",
        "text": "A gas collected from a metal-and-acid tube pops with a lit "
                "splint. What has that told you?",
        "options": [
            {"text": "That the metal is high in the series, since only the "
                     "most reactive metals produce enough hydrogen for the "
                     "pop to be heard at all",
             "correct": False,
             "why": "A gentle fizz gives a pop too. The test identifies the "
                    "gas rather than measuring the reactivity"},
            {"text": "That the gas is oxygen",
             "correct": False,
             "why": "Oxygen relights a GLOWING splint. It does not pop"},
            {"text": "That the acid was too concentrated, since a more dilute "
                     "one would not have given a pop",
             "correct": False,
             "why": "The pop happens at any concentration that reacts at "
                    "all"},
            {"text": "That the gas is hydrogen, which is what both tests in "
                     "this lesson produce",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c9-01-s09",
        "band": "standard",
        "text": "A metal is hard, dense and difficult to scratch. Where does "
                "that put it in the reactivity series?",
        "options": [
            {"text": "Nowhere — hardness says nothing about reactivity",
             "correct": True},
            {"text": "Near the bottom, because hard metals are the "
                     "unreactive ones and that is what makes them useful for "
                     "tools and machinery",
             "correct": False,
             "why": "Tungsten is very hard and fairly reactive; gold is soft "
                    "and the least reactive of all. There is no link"},
            {"text": "Near the top",
             "correct": False,
             "why": "There is no link in either direction. The series is "
                    "about chemical behaviour"},
            {"text": "In the middle, alongside the other hard and dense metals "
                     "there",
             "correct": False,
             "why": "Hardness gives no information about position at all, "
                    "middle included"},
        ],
        "figure": None,
    },
    {
        "id": "c9-01-s10",
        "band": "standard",
        "text": "You are handed an unknown metal and told to place it. Which "
                "test is worth running FIRST?",
        "options": [
            {"text": "Dilute acid, because it reaches further down the list "
                     "and so gives an answer for more of the metals you might "
                     "have been handed",
             "correct": False,
             "why": "Acid is the sensible SECOND test. Water first tells you "
                    "whether you are dealing with the violent end"},
            {"text": "Cold water, because a reaction there settles the top of "
                     "the series at once",
             "correct": True},
            {"text": "A displacement against copper sulfate, watching for "
                     "copper to settle out on the metal",
             "correct": False,
             "why": "A useful third test. It compares against one metal "
                    "rather than splitting the series"},
            {"text": "Heating it in air",
             "correct": False,
             "why": "Almost every metal reacts with air when hot, so it "
                    "separates very little"},
        ],
        "figure": None,
    },
    {
        "id": "c9-01-s11",
        "band": "standard",
        "text": "Potassium on water reacts hard enough to set fire to its own "
                "hydrogen. What does that add to what sodium already showed?",
        "options": [
            {"text": "That potassium produces a different gas from sodium, "
                     "which is what the flame over the surface of the water "
                     "is showing you",
             "correct": False,
             "why": "Both give hydrogen. The flame is that hydrogen burning, "
                    "lit by the heat of the reaction"},
            {"text": "That potassium is a non-metal",
             "correct": False,
             "why": "It is a metal, and one of the most reactive there is"},
            {"text": "That potassium is above sodium, because the same "
                     "reaction runs more violently",
             "correct": True},
            {"text": "Nothing — both of them react with water, so this test "
                     "cannot separate the two of them at all",
             "correct": False,
             "why": "HOW violently is exactly what separates two metals that "
                    "both react"},
        ],
        "figure": None,
    },
    {
        "id": "c9-01-s12",
        "band": "standard",
        "text": "Copper pipes carry cold water through houses for fifty years "
                "and do not change. What does that establish?",
        "options": [
            {"text": "That copper is completely unreactive, since fifty years "
                     "in contact with water is long enough for any reaction "
                     "at all to have shown itself",
             "correct": False,
             "why": "Copper reacts with plenty of things — it turns green on "
                    "a roof. What this rules out is water"},
            {"text": "That copper is at the very bottom of the series, below "
                     "every other metal",
             "correct": False,
             "why": "Silver and gold are below it. This test cannot separate "
                    "the bottom three"},
            {"text": "That water is not a good test for any metal",
             "correct": False,
             "why": "It is an excellent test for the top three. A negative "
                    "result is still a result"},
            {"text": "That copper is below the metals that react with cold "
                     "water",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c9-01-s13",
        "band": "standard",
        "text": "Why is a SERIES more useful than simply writing down what "
                "each metal did in each test?",
        "options": [
            {"text": "Because one order predicts every reaction the metals "
                     "take part in, not just the tests that built it",
             "correct": True},
            {"text": "Because a list is shorter than a table and easier to "
                     "learn",
             "correct": False,
             "why": "Brevity is not the point. A list of observations "
                    "predicts nothing new"},
            {"text": "Because the observations might have been recorded "
                     "wrongly",
             "correct": False,
             "why": "The series is built FROM those observations. It stands "
                    "or falls with them"},
            {"text": "Because a series can be memorised",
             "correct": False,
             "why": "It can, and that is a convenience. Its value is that it "
                    "predicts"},
        ],
        "figure": None,
    },

    # ── harder · MRB-335 top-up ─────────────────────────────────────────
    {
        "id": "c9-01-h05",
        "band": "harder",
        "text": "Caesium sits below potassium in group 1. What would you "
                "predict for caesium dropped into cold water?",
        "options": [
            {"text": "A reaction more violent than potassium's, giving the "
                     "same hydroxide and the same hydrogen",
             "correct": True},
            {"text": "A slower reaction than potassium's, because caesium is "
                     "a heavier metal and heavier metals hold their atoms "
                     "more tightly than light ones do",
             "correct": False,
             "why": "Mass does not set reactivity. Group 1 gets MORE reactive "
                    "going down"},
            {"text": "No reaction at all",
             "correct": False,
             "why": "Every group 1 metal reacts with water. That is what "
                    "makes them a family"},
            {"text": "A different set of products altogether, because caesium "
                     "is far enough down group 1 to behave unlike the rest",
             "correct": False,
             "why": "Same family, same reaction — a hydroxide and hydrogen. "
                    "Only the vigour changes"},
        ],
        "figure": None,
    },
    {
        "id": "c9-01-h06",
        "band": "harder",
        "text": "Powdered zinc fizzes far faster in acid than a lump of zinc "
                "does. Does that move zinc up the series?",
        "options": [
            {"text": "Yes — reacting faster is what being higher in the "
                     "series means, so the powder belongs above the lump",
             "correct": False,
             "why": "Then one metal would have two positions, which makes the "
                    "series useless. Surface area changes rate, not "
                    "reactivity"},
            {"text": "No — the surface area has changed, and the metal has "
                     "not",
             "correct": True},
            {"text": "Yes, but only while it is powdered",
             "correct": False,
             "why": "A position that changes with how the sample was cut is "
                    "not a position at all"},
            {"text": "No, because powder reacts more slowly than a lump of the "
                     "same metal",
             "correct": False,
             "why": "Right conclusion, wrong observation. Powder reacts "
                    "faster, and it still does not move the metal"},
        ],
        "figure": None,
    },
    {
        "id": "c9-01-h07",
        "band": "harder",
        "text": "An unknown metal reacts with cold water, but much less "
                "violently than sodium does. Where does it go?",
        "options": [
            {"text": "Below the metals that react with acid, because a "
                     "reaction that gentle shows it is closer to the "
                     "unreactive end than to the violent one",
             "correct": False,
             "why": "It reacted with WATER, which already puts it above "
                    "everything that needs acid"},
            {"text": "Above sodium",
             "correct": False,
             "why": "More violent means higher. This one is gentler than "
                    "sodium"},
            {"text": "In the top group, and below sodium",
             "correct": True},
            {"text": "It cannot be placed without an acid test",
             "correct": False,
             "why": "A water reaction places it in the top group already, and "
                    "its vigour places it within that group"},
        ],
        "figure": None,
    },
    {
        "id": "c9-01-h08",
        "band": "harder",
        "text": "Two metals both do nothing in cold water AND nothing in "
                "dilute acid. Can these two tests order them?",
        "options": [
            {"text": "Yes — both being unreactive puts them at the bottom, "
                     "and the order at the bottom is settled by which of them "
                     "is the rarer and therefore the more valuable metal",
             "correct": False,
             "why": "Value is not chemistry. Two identical results carry no "
                    "information about which is which"},
            {"text": "Yes, by looking at which is shinier",
             "correct": False,
             "why": "Appearance has no place in the series"},
            {"text": "No — two metals that behave identically must be the "
                     "same metal",
             "correct": False,
             "why": "Copper, silver and gold all do nothing in both tests and "
                    "are three different metals"},
            {"text": "No — both results are the same, so a third test is "
                     "needed",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c9-01-h09",
        "band": "harder",
        "text": "An aluminium pan boils water for years without changing, and "
                "aluminium sits just below magnesium. How would you SHOW that "
                "the position is right?",
        "options": [
            {"text": "Remove the oxide layer and expose fresh aluminium, and "
                     "the metal reacts as its position predicts",
             "correct": True},
            {"text": "Heat the pan far hotter, since a reactive metal reacts "
                     "eventually",
             "correct": False,
             "why": "The oxide layer survives heating too. What has to be "
                    "dealt with is the coating"},
            {"text": "Leave the pan in water for longer",
             "correct": False,
             "why": "The layer does not wear off with time. Years already "
                    "show that"},
            {"text": "Accept that the position is wrong",
             "correct": False,
             "why": "The position is about the element and the pan's "
                    "behaviour is about a coating on it"},
        ],
        "figure": None,
    },
    {
        "id": "c9-01-h10",
        "band": "harder",
        "text": "The series was built from water and acid tests, and it "
                "predicts displacement reactions it was never built from. Why "
                "should that work?",
        "options": [
            {"text": "Because displacement and the acid test are really one "
                     "reaction",
             "correct": False,
             "why": "They are different reactions with different products. "
                    "What they share is the property they depend on"},
            {"text": "Because reactivity is one property of the element, so "
                     "the same order shows up wherever it is tested",
             "correct": True},
            {"text": "Because chemists chose the order to fit both",
             "correct": False,
             "why": "The order came from the water and acid results. That it "
                    "then fitted displacement is the finding"},
            {"text": "It is a coincidence that nobody has explained",
             "correct": False,
             "why": "It has been explained. One property drives every one of "
                    "these reactions"},
        ],
        "figure": None,
    },
    {
        "id": "c9-01-h11",
        "band": "harder",
        "text": "Gold and copper are found in the ground as the metal itself, "
                "and potassium never is. What does that tell you?",
        "options": [
            {"text": "That gold and copper were formed later than potassium "
                     "was",
             "correct": False,
             "why": "All of them are as old as the Earth. What differs is how "
                    "readily they react"},
            {"text": "That potassium is rarer",
             "correct": False,
             "why": "Potassium is far commoner than gold. Being found "
                    "uncombined is about reactivity"},
            {"text": "That the unreactive metals have survived uncombined, "
                     "and the reactive ones combined long ago",
             "correct": True},
            {"text": "That gold and copper are not really elements",
             "correct": False,
             "why": "Both are elements. Being found uncombined is what an "
                    "unreactive element does"},
        ],
        "figure": None,
    },
    {
        "id": "c9-01-h12",
        "band": "harder",
        "text": "The lesson says reactivity is a property of the element, "
                "like a melting point. What follows from that comparison?",
        "options": [
            {"text": "It can be measured in degrees, so two metals' "
                     "reactivities can be subtracted from each other to give "
                     "a number for how far apart they are",
             "correct": False,
             "why": "There is no unit for it. The series is an ORDER rather "
                    "than a scale"},
            {"text": "It changes when the metal is heated, in exactly the way "
                     "that a melting point rises with heating",
             "correct": False,
             "why": "A melting point does not change when a substance is "
                    "heated. Both are fixed properties"},
            {"text": "It can be looked up rather than measured",
             "correct": False,
             "why": "It can be looked up BECAUSE somebody measured it. That "
                    "is true of a melting point too"},
            {"text": "It is fixed for that element, whatever shape or amount "
                     "of it you happen to have",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c9-01-h13",
        "band": "harder",
        "text": "Sodium is soft enough to cut and sits near the top; gold is "
                "soft too and sits at the bottom. What does that pair rule "
                "out?",
        "options": [
            {"text": "Any rule connecting softness with position in the "
                     "series",
             "correct": True},
            {"text": "Any rule connecting softness with position, but only "
                     "for metals that are found uncombined in the ground "
                     "rather than having to be extracted from an ore",
             "correct": False,
             "why": "No qualification is needed. Two soft metals at opposite "
                    "ends rule the connection out altogether"},
            {"text": "That gold is really at the bottom",
             "correct": False,
             "why": "Gold's position is established by its chemistry. The "
                    "pair rules out a rule, not a position"},
            {"text": "Nothing — two examples cannot rule anything out",
             "correct": False,
             "why": "Two examples at opposite ends of the series are exactly "
                    "what refutes a claimed connection"},
        ],
        "figure": None,
    },
]
