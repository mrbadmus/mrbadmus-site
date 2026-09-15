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

    # ── MRB-338 top-up · easier e14–e30 ─────────────────────────────────
    {
        "id": "c9-01-e14",
        "band": "easier",
        "text": "Which metal sits second in the reactivity series, "
                "immediately below potassium?",
        "options": [
            {"text": "Calcium", "correct": False,
             "why": "Calcium is third, below sodium"},
            {"text": "Sodium", "correct": True},
            {"text": "Magnesium", "correct": False,
             "why": "Magnesium is fourth, below calcium"},
            {"text": "Aluminium", "correct": False,
             "why": "Aluminium is fifth, below magnesium"},
        ],
        "figure": None,
    },
    {
        "id": "c9-01-e15",
        "band": "easier",
        "text": "A metal from the top of the series is put into cold water "
                "and a gas comes off. What are the two products?",
        "options": [
            {"text": "A metal hydroxide, and hydrogen", "correct": True},
            {"text": "A metal oxide, and hydrogen", "correct": False,
             "why": "The metal joins the whole water molecule, not oxygen "
                    "alone. What is left dissolved is a hydroxide"},
            {"text": "A metal chloride, and hydrogen", "correct": False,
             "why": "A chloride comes from hydrochloric acid. There is no "
                    "chlorine in water at all"},
            {"text": "A metal hydroxide, and oxygen", "correct": False,
             "why": "Both tests in this lesson give off hydrogen, which pops "
                    "with a lit splint"},
        ],
        "figure": None,
    },
    {
        "id": "c9-01-e16",
        "band": "easier",
        "text": "Magnesium fizzes in dilute hydrochloric acid. Name the two "
                "products.",
        "options": [
            {"text": "Magnesium oxide and hydrogen", "correct": False,
             "why": "An oxide would need oxygen. The acid supplies chlorine, "
                    "so a chloride is what forms"},
            {"text": "Magnesium hydroxide and hydrogen", "correct": False,
             "why": "A hydroxide is what cold water gives. An acid gives a "
                    "salt named after the acid"},
            {"text": "Magnesium chloride and oxygen", "correct": False,
             "why": "Hydrogen is the gas from a metal and an acid. No oxygen "
                    "is released"},
            {"text": "Magnesium chloride and hydrogen", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c9-01-e17",
        "band": "easier",
        "text": "Potassium on cold water gives off a gas that catches fire. "
                "What colour is that flame?",
        "options": [
            {"text": "Bright white", "correct": False,
             "why": "Bright white is burning magnesium ribbon"},
            {"text": "Orange", "correct": False,
             "why": "Orange is the colour a sodium compound gives a flame"},
            {"text": "Lilac", "correct": True},
            {"text": "Green", "correct": False,
             "why": "Green flames come from copper compounds"},
        ],
        "figure": None,
    },
    {
        "id": "c9-01-e18",
        "band": "easier",
        "text": "A lump of calcium is dropped into cold water. What happens "
                "to the water itself?",
        "options": [
            {"text": "It turns bright blue", "correct": False,
             "why": "Blue is a copper sulfate solution. Calcium hydroxide is "
                    "white"},
            {"text": "It turns a pale green colour", "correct": False,
             "why": "Pale green is an iron sulfate solution, not a calcium "
                    "one"},
            {"text": "It stays completely clear", "correct": False,
             "why": "Calcium hydroxide is only slightly soluble, so what will "
                    "not dissolve clouds the water"},
            {"text": "It turns cloudy white", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c9-01-e19",
        "band": "easier",
        "text": "The second test on the bench uses DILUTE acid. What does "
                "dilute mean?",
        "options": [
            {"text": "An acid with a lot of water in it", "correct": True},
            {"text": "An acid that has been warmed up before it is used",
             "correct": False,
             "why": "Dilute says nothing about temperature. It describes how "
                    "much water has been mixed in"},
            {"text": "An acid that is safe to touch with bare hands",
             "correct": False,
             "why": "A dilute acid still needs care. Dilute describes the "
                    "amount of water, not the hazard"},
            {"text": "An acid that has been left open to the air for a while",
             "correct": False,
             "why": "Leaving an acid standing does not dilute it. Water has "
                    "to be added"},
        ],
        "figure": None,
    },
    {
        "id": "c9-01-e20",
        "band": "easier",
        "text": "Which metal sits between iron and copper in the reactivity "
                "series?",
        "options": [
            {"text": "Zinc", "correct": False,
             "why": "Zinc is above iron, not below it"},
            {"text": "Lead", "correct": True},
            {"text": "Silver", "correct": False,
             "why": "Silver is below copper, not between iron and copper"},
            {"text": "Carbon", "correct": False,
             "why": "Carbon is placed above zinc, which is well above iron"},
        ],
        "figure": None,
    },
    {
        "id": "c9-01-e21",
        "band": "easier",
        "text": "Silver is used for mirror backing and for electrical "
                "contacts because it stays as it is. What does that suggest?",
        "options": [
            {"text": "It is high in the series and reacts readily",
             "correct": False,
             "why": "A metal high in the series reacts readily. Silver "
                    "staying unchanged points the other way"},
            {"text": "It is the hardest metal in the list", "correct": False,
             "why": "Hardness is not reactivity, and silver is a soft metal"},
            {"text": "It is low in the reactivity series, so it stays as it "
                     "is in ordinary use", "correct": True},
            {"text": "It is a non-metal, like carbon", "correct": False,
             "why": "Silver is a metal. Carbon is the only non-metal in the "
                    "list"},
        ],
        "figure": None,
    },
    {
        "id": "c9-01-e22",
        "band": "easier",
        "text": "Zinc does nothing in cold water but reacts steadily in "
                "dilute acid. Which band of the bench does it belong to?",
        "options": [
            {"text": "The metals that fizz in cold water", "correct": False,
             "why": "Zinc gave nothing in cold water, so it cannot be in that "
                    "band"},
            {"text": "The metals that need acid before much happens",
             "correct": True},
            {"text": "The metals that neither liquid touches",
             "correct": False,
             "why": "Acid gets a steady reaction from zinc, so that band is "
                    "the wrong one"},
            {"text": "The metals that react with neither liquid but rust "
                     "quickly in damp air", "correct": False,
             "why": "Rusting is iron, and zinc reacted with the acid anyway"},
        ],
        "figure": None,
    },
    {
        "id": "c9-01-e23",
        "band": "easier",
        "text": "A cleaned magnesium ribbon is left standing in cold water "
                "for several minutes. What is seen?",
        "options": [
            {"text": "A few tiny bubbles clinging to the ribbon",
             "correct": True},
            {"text": "A fast stream of bubbles and a warm tube",
             "correct": False,
             "why": "That is magnesium in dilute acid. Cold water gives "
                    "almost nothing"},
            {"text": "Nothing whatever, now or ever", "correct": False,
             "why": "The reaction is real but far too slow to watch, so "
                    "'nothing ever' is too strong"},
            {"text": "The ribbon disappears and the water goes cloudy",
             "correct": False,
             "why": "A disappearing ribbon is the acid tube, and cloudy water "
                    "is calcium"},
        ],
        "figure": None,
    },
    {
        "id": "c9-01-e24",
        "band": "easier",
        "text": "Where does aluminium sit in the reactivity series?",
        "options": [
            {"text": "Between zinc and iron", "correct": False,
             "why": "Aluminium is above carbon, which is itself above zinc"},
            {"text": "Somewhere between copper and silver", "correct": False,
             "why": "That is the bottom of the list. Aluminium is high in it"},
            {"text": "Below gold, at the very bottom", "correct": False,
             "why": "Nothing sits below gold, and aluminium is near the top"},
            {"text": "Between magnesium and carbon", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c9-01-e25",
        "band": "easier",
        "text": "Potassium in water is a teacher demonstration only. Which "
                "precautions go with it?",
        "options": [
            {"text": "A safety screen, and the smallest piece that can be cut",
             "correct": True},
            {"text": "Gloves, and a piece about the size of a fist so that "
                     "the class at the back can see it", "correct": False,
             "why": "The piece is kept as small as can be cut; a large one "
                    "would be dangerous"},
            {"text": "A fume cupboard, and the acid warmed first",
             "correct": False,
             "why": "Potassium is never put into acid at any concentration"},
            {"text": "No special precautions, as the piece is small",
             "correct": False,
             "why": "A screen and a teacher demonstration are both required"},
        ],
        "figure": None,
    },
    {
        "id": "c9-01-e26",
        "band": "easier",
        "text": "Carbon is placed in the reactivity series between which two?",
        "options": [
            {"text": "Iron and lead, low in the list", "correct": False,
             "why": "Carbon is well above iron"},
            {"text": "Aluminium and zinc", "correct": True},
            {"text": "Copper and silver", "correct": False,
             "why": "That is the bottom of the list, and carbon is in the "
                    "upper half"},
            {"text": "Potassium and sodium", "correct": False,
             "why": "Those are the top two, and nothing is placed between "
                    "them"},
        ],
        "figure": None,
    },
    {
        "id": "c9-01-e27",
        "band": "easier",
        "text": "Which observation shows that a metal has reacted with dilute "
                "acid?",
        "options": [
            {"text": "The acid staying exactly as it was", "correct": False,
             "why": "No change at all is the result copper gives, and copper "
                    "does not react"},
            {"text": "The metal becoming shinier in the tube", "correct": False,
             "why": "A shine can come from cleaning. Bubbles are the sign of "
                    "a reaction"},
            {"text": "Bubbles of gas coming off the metal", "correct": True},
            {"text": "The acid turning a deeper colour while the metal is "
                     "left completely unchanged", "correct": False,
             "why": "The metal has to change for a reaction with it to have "
                    "happened"},
        ],
        "figure": None,
    },
    {
        "id": "c9-01-e28",
        "band": "easier",
        "text": "Why is a magnesium ribbon rubbed clean before it is tested?",
        "options": [
            {"text": "To take off the dull oxide layer, so that the metal "
                     "itself meets the liquid", "correct": True},
            {"text": "To make it thinner, so that the acid has less metal to "
                     "work through and reacts faster", "correct": False,
             "why": "Cleaning is about the surface, not about the thickness"},
            {"text": "To warm it up before the reaction starts",
             "correct": False,
             "why": "Rubbing warms it barely at all, and warmth is not the "
                    "reason"},
            {"text": "To make it weigh less, so the result is fairer",
             "correct": False,
             "why": "The point is a clean surface, not a particular mass"},
        ],
        "figure": None,
    },
    {
        "id": "c9-01-e29",
        "band": "easier",
        "text": "A freshly cut piece of sodium goes dull within seconds on "
                "the bench. What is it reacting with?",
        "options": [
            {"text": "The knife", "correct": False,
             "why": "The knife does not attack it. The dullness spreads over "
                    "the whole cut face"},
            {"text": "The air", "correct": True},
            {"text": "The oil it was stored in", "correct": False,
             "why": "The oil is there to keep air off; it does not attack the "
                    "metal"},
            {"text": "Nothing — it is simply drying", "correct": False,
             "why": "A new substance is forming on the surface, so it is a "
                    "chemical change"},
        ],
        "figure": None,
    },
    {
        "id": "c9-01-e30",
        "band": "easier",
        "text": "Which metal on the bench reacted violently with cold water?",
        "options": [
            {"text": "Magnesium", "correct": False,
             "why": "Magnesium barely touches cold water and needs acid"},
            {"text": "Zinc granules", "correct": False,
             "why": "Zinc does nothing at all in cold water"},
            {"text": "Potassium", "correct": True},
            {"text": "Copper", "correct": False,
             "why": "Copper does nothing in either liquid"},
        ],
        "figure": None,
    },

    # ── MRB-338 top-up · standard s14–s30 ───────────────────────────────
    {
        "id": "c9-01-s14",
        "band": "standard",
        "text": "Calcium reacts with cold water and also fizzes in dilute "
                "acid. What does the acid result add to its position?",
        "options": [
            {"text": "Nothing new — the water test had already placed it near "
                     "the top", "correct": True},
            {"text": "It moves calcium above potassium, because it reacted in "
                     "two liquids", "correct": False,
             "why": "Reacting twice does not move a metal up. Potassium's "
                    "water reaction is far more violent"},
            {"text": "It moves calcium into the middle band with magnesium "
                     "and zinc", "correct": False,
             "why": "The middle band is for metals that give nothing in cold "
                    "water, and calcium fizzes in it"},
            {"text": "It shows the series was built the wrong way up",
             "correct": False,
             "why": "Every metal that reacts with cold water reacts with acid "
                    "too, so nothing is upside down"},
        ],
        "figure": None,
    },
    {
        "id": "c9-01-s15",
        "band": "standard",
        "text": "A metal reacts with cold water. Can you say in advance what "
                "dilute acid will do to it?",
        "options": [
            {"text": "No — the two liquids are unrelated, so either result is "
                     "possible", "correct": False,
             "why": "Both tests measure the same property, and the top of the "
                    "series passes both"},
            {"text": "Yes — anything that manages cold water manages acid as "
                     "well", "correct": True},
            {"text": "Yes — it will do nothing, because the water has used "
                     "the metal up", "correct": False,
             "why": "A fresh piece is used for each test, and reactivity is a "
                    "property of the element"},
            {"text": "No — acid only works on metals that ignore cold water",
             "correct": False,
             "why": "Acid reacts with the top of the series too, and more "
                    "violently than water does"},
        ],
        "figure": None,
    },
    {
        "id": "c9-01-s16",
        "band": "standard",
        "text": "In the middle band, the fizzing in acid gets weaker the "
                "further down the list you go. Why?",
        "options": [
            {"text": "Because the acid is used up by the metals above them in "
                     "the tube", "correct": False,
             "why": "Each metal is tested in its own tube with its own fresh "
                    "acid"},
            {"text": "Because the lower metals are heavier, so they sink out "
                     "of the acid", "correct": False,
             "why": "Density has nothing to do with it, and the pieces are "
                    "covered either way"},
            {"text": "Because those metals are less reactive the lower they "
                     "sit", "correct": True},
            {"text": "Because the lower metals are harder, so the acid cannot "
                     "get into them", "correct": False,
             "why": "Hardness is not reactivity. Sodium is soft and sits near "
                    "the top"},
        ],
        "figure": None,
    },
    {
        "id": "c9-01-s17",
        "band": "standard",
        "text": "Calcium leaves the water cloudy white, while potassium "
                "leaves a clear solution behind. What explains the "
                "difference?",
        "options": [
            {"text": "Calcium hydroxide is only slightly soluble, so most of "
                     "it stays as a white solid in the water", "correct": True},
            {"text": "Calcium reacts more violently, and violence makes a "
                     "solution cloudy", "correct": False,
             "why": "Potassium's reaction is far more violent and its "
                    "solution is clear"},
            {"text": "Calcium is a different colour from potassium",
             "correct": False,
             "why": "Both are silvery. The cloudiness comes from the compound "
                    "that forms"},
            {"text": "Potassium reacts with the glass and cleans it",
             "correct": False,
             "why": "Potassium does not attack the glass. The difference is "
                    "in the hydroxide"},
        ],
        "figure": None,
    },
    {
        "id": "c9-01-s18",
        "band": "standard",
        "text": "The same gas is given off in the water test and in the acid "
                "test. Why is that a useful clue?",
        "options": [
            {"text": "It shows the water and the acid are the same substance",
             "correct": False,
             "why": "Dilute acid is mostly water, but it is the acid that "
                    "gets the middle metals going"},
            {"text": "It shows the gas comes out of the metal, which had been "
                     "storing it", "correct": False,
             "why": "The hydrogen comes from the water or from the acid, not "
                    "from inside the metal"},
            {"text": "It shows the two tests must give the same answer for "
                     "every metal, so only one of them is ever needed",
             "correct": False,
             "why": "Magnesium gives nothing in water and a fast reaction in "
                    "acid, so the answers differ"},
            {"text": "It suggests the two tests are doing the same kind of "
                     "job, so one order can cover both", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c9-01-s19",
        "band": "standard",
        "text": "An unknown metal fizzes only gently in dilute acid and the "
                "tube barely warms. Magnesium in the same acid fizzes fast "
                "and gets hot. What follows?",
        "options": [
            {"text": "The unknown metal is below magnesium in the series",
             "correct": True},
            {"text": "The unknown metal is above magnesium, because a gentle "
                     "reaction runs for longer and so gives more in total",
             "correct": False,
             "why": "A gentler reaction means a less reactive metal, whatever "
                    "it adds up to in the end"},
            {"text": "The two metals are in the same place, because both of "
                     "them fizzed", "correct": False,
             "why": "Both reacting puts them in the same band; how hard they "
                    "react separates them within it"},
            {"text": "Nothing can be said until the unknown is tried in cold "
                     "water as well", "correct": False,
             "why": "The acid result already places it below magnesium; water "
                    "would add to that, not replace it"},
        ],
        "figure": None,
    },
    {
        "id": "c9-01-s20",
        "band": "standard",
        "text": "Lead barely reacts with dilute acid; copper does not react "
                "with it at all. Which test separates the two?",
        "options": [
            {"text": "The cold water test, because lead reacts with it and "
                     "copper does not", "correct": False,
             "why": "Neither lead nor copper reacts with cold water, so that "
                    "test separates nothing"},
            {"text": "Neither test, because 'barely' and 'not at all' are the "
                     "same result", "correct": False,
             "why": "A small reaction and no reaction are different results, "
                    "and the difference is the evidence"},
            {"text": "The acid test — just, because lead gives a little and "
                     "copper gives none", "correct": True},
            {"text": "Both tests, because lead reacts in both and copper in "
                     "neither", "correct": False,
             "why": "Lead does not react with cold water; only the acid tube "
                    "tells them apart"},
        ],
        "figure": None,
    },
    {
        "id": "c9-01-s21",
        "band": "standard",
        "text": "One student scrapes a fresh surface on a piece of aluminium "
                "and another does not. Both pieces go into dilute acid. Whose "
                "reacts faster?",
        "options": [
            {"text": "The unscraped one, because its surface is smoother and "
                     "the acid can spread over it more evenly", "correct": False,
             "why": "The oxide layer keeps the acid off the metal, and "
                    "smoothness does not help"},
            {"text": "They react at the same rate, because both pieces are "
                     "aluminium", "correct": False,
             "why": "Both are aluminium, but only one of them has the metal "
                    "itself exposed"},
            {"text": "Neither reacts, because aluminium is below copper in "
                     "the series", "correct": False,
             "why": "Aluminium is high in the series, just below magnesium"},
            {"text": "The scraped one, because the oxide layer has been taken "
                     "off", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c9-01-s22",
        "band": "standard",
        "text": "A cut piece of sodium goes dull in seconds in air, while "
                "copper turnings sit in an open jar for years. What does the "
                "pair establish?",
        "options": [
            {"text": "Sodium is softer than copper, and soft metals go dull "
                     "faster", "correct": False,
             "why": "Softness is not reactivity. Gold is soft and does not "
                    "tarnish at all"},
            {"text": "Sodium is far higher in the reactivity series than "
                     "copper", "correct": True},
            {"text": "Copper has been treated with something that protects "
                     "it", "correct": False,
             "why": "Plain copper turnings need no treatment; they simply do "
                    "not react much"},
            {"text": "Sodium is stored wrongly, and copper is stored "
                     "properly", "correct": False,
             "why": "Sodium is kept under oil for exactly this reason. The "
                    "dulling is its own chemistry"},
        ],
        "figure": None,
    },
    {
        "id": "c9-01-s23",
        "band": "standard",
        "text": "Zinc granules and iron granules of the same size are each "
                "put into the same dilute acid. Which observation orders "
                "them?",
        "options": [
            {"text": "Which one sinks first, since the more reactive metal is "
                     "the denser", "correct": False,
             "why": "Density is a separate property and says nothing about "
                    "reactivity"},
            {"text": "Which one is the darker grey, since colour follows the "
                     "series", "correct": False,
             "why": "Colour is not part of the series, and both of them are "
                    "grey"},
            {"text": "How fast the bubbles come off", "correct": True},
            {"text": "Neither — both of them fizz", "correct": False,
             "why": "Both fizz, and how hard they fizz is the evidence that "
                    "orders them"},
        ],
        "figure": None,
    },
    {
        "id": "c9-01-s24",
        "band": "standard",
        "text": "Potassium is cut fresh from under the oil immediately before "
                "use. Why would a piece left out on the bench give a poor "
                "result?",
        "options": [
            {"text": "It would have dried out, and a dry metal cannot react "
                     "with water", "correct": False,
             "why": "The reaction is with the water in the beaker, not with "
                    "any dampness on the metal"},
            {"text": "It would have got warmer where it lay on the bench, and "
                     "a warm metal reacts less than a cold one",
             "correct": False,
             "why": "Warming speeds a reaction up rather than slowing it. The "
                    "problem is the coating"},
            {"text": "It would have got heavier, which changes the amount of "
                     "metal being used", "correct": False,
             "why": "Any mass change is tiny. What matters is that the "
                    "surface has already changed"},
            {"text": "Its surface would already have reacted with the air, so "
                     "it is no longer clean metal", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c9-01-s25",
        "band": "standard",
        "text": "Calcium is put into dilute hydrochloric acid. Name both "
                "products.",
        "options": [
            {"text": "Calcium hydroxide and hydrogen", "correct": False,
             "why": "A hydroxide is what cold water gives. An acid gives a "
                    "salt named after the acid"},
            {"text": "Calcium chloride and hydrogen", "correct": True},
            {"text": "Calcium oxide and hydrogen gas", "correct": False,
             "why": "There is no oxygen to take. The chlorine from the acid "
                    "joins the calcium"},
            {"text": "Calcium chloride and oxygen", "correct": False,
             "why": "Hydrogen is the gas from a metal and an acid, and it "
                    "pops with a lit splint"},
        ],
        "figure": None,
    },
    {
        "id": "c9-01-s26",
        "band": "standard",
        "text": "Why is dilute acid a better test than cold water for sorting "
                "the MIDDLE of the list?",
        "options": [
            {"text": "Because acid is more dangerous, and a more dangerous "
                     "test is a more accurate one", "correct": False,
             "why": "How hazardous a test is has nothing to do with what it "
                    "can show"},
            {"text": "Because cold water gives nothing for all of them, so it "
                     "cannot tell them apart", "correct": True},
            {"text": "Because acid dissolves every metal, so every one of "
                     "them gives a result", "correct": False,
             "why": "Copper, silver and gold all give nothing in dilute acid"},
            {"text": "Because cold water reacts with all of them equally",
             "correct": False,
             "why": "Cold water gives nothing at all for the middle of the "
                    "list, which is the problem"},
        ],
        "figure": None,
    },
    {
        "id": "c9-01-s27",
        "band": "standard",
        "text": "Silver is chosen for mirror backing and for electrical "
                "contacts. Which property of silver is being used?",
        "options": [
            {"text": "That it is the most reactive metal available at a "
                     "sensible price", "correct": False,
             "why": "A reactive metal would tarnish away. Silver is chosen "
                    "for the opposite reason"},
            {"text": "That it reacts with air to form a hard protective coat",
             "correct": False,
             "why": "That describes aluminium's oxide layer. Silver is chosen "
                    "because it stays unchanged"},
            {"text": "That it is the hardest metal, so a contact does not "
                     "wear", "correct": False,
             "why": "Silver is soft. It is its lack of reaction that matters "
                    "here"},
            {"text": "That it stays as it is, because it is near the bottom "
                     "of the series", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c9-01-s28",
        "band": "standard",
        "text": "A student tests an unknown metal in WARM water instead of "
                "cold and sees bubbles. Can they place it with potassium and "
                "calcium?",
        "options": [
            {"text": "Yes, because bubbles in water are bubbles in water "
                     "whatever the temperature", "correct": False,
             "why": "Warming can start a reaction cold water would not, so "
                    "the comparison is unfair"},
            {"text": "Yes, because warm water is just cold water that has "
                     "been heated a little", "correct": False,
             "why": "The other metals were all given cold water, and the test "
                    "has to be the same for each"},
            {"text": "No — that is a different test, so the result cannot be "
                     "compared with theirs", "correct": True},
            {"text": "No, because warm water never reacts with any metal",
             "correct": False,
             "why": "Warm water reacts with more metals than cold water does, "
                    "not fewer"},
        ],
        "figure": None,
    },
    {
        "id": "c9-01-s29",
        "band": "standard",
        "text": "Calcium fizzes in cold water. How would you identify the gas "
                "coming off, and what result would you expect?",
        "options": [
            {"text": "Hold a lit splint to it and expect a squeaky pop",
             "correct": True},
            {"text": "Hold a lit splint to it and expect the flame to go out",
             "correct": False,
             "why": "A flame going out suggests carbon dioxide, and this gas "
                    "burns instead"},
            {"text": "Bubble it through limewater and expect the limewater to "
                     "go cloudy", "correct": False,
             "why": "Cloudy limewater means carbon dioxide, which a metal and "
                    "water do not give"},
            {"text": "Hold damp indicator paper in it and expect the paper to "
                     "bleach white", "correct": False,
             "why": "Bleaching indicates chlorine, and nothing in this test "
                    "produces chlorine"},
        ],
        "figure": None,
    },
    {
        "id": "c9-01-s30",
        "band": "standard",
        "text": "The bench places six of the twelve metals in the reference "
                "list. How were the other six placed?",
        "options": [
            {"text": "By looking at how much each of them costs to buy",
             "correct": False,
             "why": "Price is a fact about people. The order came from "
                    "reactions"},
            {"text": "By the same two tests, run on those metals",
             "correct": True},
            {"text": "By putting them in order of melting point",
             "correct": False,
             "why": "Melting point is a separate property and gives a "
                    "different order"},
            {"text": "By guessing, since just six of them can be tested",
             "correct": False,
             "why": "Every metal in the list was placed by evidence, as the "
                    "six on the bench were"},
        ],
        "figure": None,
    },

    # ── MRB-338 top-up · harder h14–h30 ─────────────────────────────────
    {
        "id": "c9-01-h14",
        "band": "harder",
        "text": "A student claims the reactivity series is simply the order "
                "in which the metals were discovered. Which pair of facts "
                "refutes that?",
        "options": [
            {"text": "Gold has been known for thousands of years and is at "
                     "the bottom; aluminium was isolated recently and is near "
                     "the top", "correct": True},
            {"text": "Potassium and sodium were discovered in the same year "
                     "and sit next to each other", "correct": False,
             "why": "That fits the claim rather than contradicting it, so it "
                    "refutes nothing"},
            {"text": "Copper and iron were both known in ancient times and "
                     "are both low in the list", "correct": False,
             "why": "Two ancient metals both sitting low is consistent with "
                    "the claim"},
            {"text": "Carbon is a non-metal, so it was never discovered as a "
                     "metal", "correct": False,
             "why": "Carbon's place is decided by its chemistry, which says "
                    "nothing about discovery dates"},
        ],
        "figure": None,
    },
    {
        "id": "c9-01-h15",
        "band": "harder",
        "text": "Dilute acid is mostly water. Why then does it get a reaction "
                "from magnesium when cold water barely does?",
        "options": [
            {"text": "The acid attacks a metal far more readily than water "
                     "does", "correct": True},
            {"text": "There is more water in dilute acid than there is in a "
                     "beaker of cold water", "correct": False,
             "why": "A beaker of water is all water. It is the acid that "
                    "makes the difference"},
            {"text": "Dilute acid comes out of the bottle warm, and the "
                     "warmth starts it off", "correct": False,
             "why": "Dilute acid is at room temperature, and warming is not "
                    "what starts it"},
            {"text": "Magnesium sits above the metals that react with cold "
                     "water", "correct": False,
             "why": "Magnesium is below them, which is exactly why cold water "
                    "gives it so little"},
        ],
        "figure": None,
    },
    {
        "id": "c9-01-h16",
        "band": "harder",
        "text": "A student puts iron filings and copper wire into dilute acid "
                "and records 'both slow'. What is wrong with that record?",
        "options": [
            {"text": "Nothing — both are low in the series, so 'both slow' is "
                     "a fair summary", "correct": False,
             "why": "Iron reacts and copper does not, and that difference is "
                    "what places them"},
            {"text": "Iron is fast rather than slow, so only the iron half is "
                     "wrong", "correct": False,
             "why": "Iron in dilute acid is genuinely slow. It is the copper "
                    "half that is wrong"},
            {"text": "Copper gives nothing at all, and no reaction is a "
                     "different result from a slow one", "correct": True},
            {"text": "Copper is faster than iron, so the record has the two "
                     "of them the wrong way round", "correct": False,
             "why": "Copper does not react with dilute acid at any speed"},
        ],
        "figure": None,
    },
    {
        "id": "c9-01-h17",
        "band": "harder",
        "text": "A metal's oxide can be broken down by heating it with "
                "carbon. What does that fix about the metal's position, with "
                "no water or acid test at all?",
        "options": [
            {"text": "That the metal sits below carbon", "correct": True},
            {"text": "That the metal sits above carbon, since carbon was able "
                     "to reach it", "correct": False,
             "why": "Carbon can only take oxygen from the metals below it"},
            {"text": "That the metal reacts with cold water, since heat was "
                     "involved", "correct": False,
             "why": "Heating a mixture says nothing about how a metal behaves "
                    "in cold water"},
            {"text": "That the metal is one of the three at the very bottom "
                     "of the list", "correct": False,
             "why": "Below carbon covers a wide range, from zinc all the way "
                    "down to gold"},
        ],
        "figure": None,
    },
    {
        "id": "c9-01-h18",
        "band": "harder",
        "text": "Magnesium ribbon left in cold water for twenty minutes has a "
                "few tiny bubbles on it. Which conclusion does that evidence "
                "support?",
        "options": [
            {"text": "Magnesium does not react with cold water, and the "
                     "bubbles are dissolved air coming out", "correct": False,
             "why": "The bubbles collect on the ribbon rather than anywhere "
                    "else, which points to a reaction"},
            {"text": "Magnesium does react with cold water, far too slowly "
                     "for the test to place it that way", "correct": True},
            {"text": "Magnesium belongs with potassium and calcium in the top "
                     "band", "correct": False,
             "why": "A few bubbles in twenty minutes is nothing like calcium "
                    "streaming bubbles at once"},
            {"text": "The water must have been contaminated, since magnesium "
                     "cannot react with it", "correct": False,
             "why": "The reaction is real and known to be very slow, so no "
                    "contamination is needed"},
        ],
        "figure": None,
    },
    {
        "id": "c9-01-h19",
        "band": "harder",
        "text": "An unknown metal X does nothing in cold water, fizzes fast "
                "in dilute acid, and the tube warms quickly. Which bench "
                "metal is X most like?",
        "options": [
            {"text": "Calcium", "correct": False,
             "why": "Calcium reacts with cold water, and X did not"},
            {"text": "Iron", "correct": False,
             "why": "Iron fizzes only sparsely in acid and the tube barely "
                    "warms"},
            {"text": "Copper", "correct": False,
             "why": "Copper does nothing in either liquid"},
            {"text": "Magnesium", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c9-01-h20",
        "band": "harder",
        "text": "A student orders four metals using dilute acid alone and "
                "says cold water was unnecessary. When would that claim fail?",
        "options": [
            {"text": "As soon as two of the metals had the same density, "
                     "because the acid could not then tell them apart",
             "correct": False,
             "why": "Density plays no part in the test or in the order"},
            {"text": "As soon as one of them was a non-metal, because acid "
                     "does not react with those at all", "correct": False,
             "why": "Carbon's place is settled another way, and that is not "
                    "where acid ordering fails"},
            {"text": "As soon as one metal was high enough to react with cold "
                     "water, because acid would then be too violent to "
                     "compare", "correct": True},
            {"text": "Never — dilute acid separates every metal in the list "
                     "on its own", "correct": False,
             "why": "Copper, silver and gold all give nothing in it, so acid "
                    "cannot order them"},
        ],
        "figure": None,
    },
    {
        "id": "c9-01-h21",
        "band": "harder",
        "text": "A metal does nothing in either liquid, and it is used for "
                "coins that stay in circulation for decades. Which of those "
                "two facts is the EVIDENCE for its position?",
        "options": [
            {"text": "The tube results", "correct": True},
            {"text": "The coins", "correct": False,
             "why": "A use follows from a property. The tests are what "
                    "measured the property"},
            {"text": "Both equally, since neither changes", "correct": False,
             "why": "The coins are a consequence of the position, not the "
                    "measurement that fixed it"},
            {"text": "Neither — evidence must be a number", "correct": False,
             "why": "Observing that nothing happened is evidence, as this "
                    "lesson insists"},
        ],
        "figure": None,
    },
    {
        "id": "c9-01-h22",
        "band": "harder",
        "text": "The bench used a magnesium ribbon, zinc granules, iron "
                "filings and a copper coil. Why does using different shapes "
                "not spoil the comparison?",
        "options": [
            {"text": "Because all four shapes were cut to exactly the same "
                     "surface area, so the rates can be compared directly",
             "correct": False,
             "why": "They plainly were not, and the bench does not depend on "
                    "their being equal"},
            {"text": "Because shape changes how fast a reaction goes, and the "
                     "bench is sorting by which metals react at all",
             "correct": True},
            {"text": "Because the shapes were chosen so that each metal "
                     "reacts equally fast", "correct": False,
             "why": "The rates differ widely, and that is part of what the "
                    "bench shows"},
            {"text": "Because shape has no effect on a reaction at all",
             "correct": False,
             "why": "Powdered zinc fizzes much faster than a lump of it, so "
                    "shape changes the rate"},
        ],
        "figure": None,
    },
    {
        "id": "c9-01-h23",
        "band": "harder",
        "text": "Iron left damp for days rusts. Explain why the bench does "
                "not count that as iron reacting with cold water.",
        "options": [
            {"text": "Rusting is a physical change, so it does not count as a "
                     "reaction", "correct": False,
             "why": "Rusting forms a new substance, which makes it a chemical "
                    "change"},
            {"text": "Rusting takes days, and only reactions that finish "
                     "inside a lesson count", "correct": False,
             "why": "How long a reaction takes does not decide whether it is "
                    "one"},
            {"text": "Rusting needs water and air together, so it is a "
                     "different reaction from the one being tested",
             "correct": True},
            {"text": "Rusting happens to steel rather than to pure iron, so "
                     "the filings on the bench could never have rusted "
                     "anyway", "correct": False,
             "why": "Iron rusts, and steel rusts precisely because it is "
                    "mostly iron"},
        ],
        "figure": None,
    },
    {
        "id": "c9-01-h24",
        "band": "harder",
        "text": "How could chemists be sure that an order built from two "
                "liquids would hold for reactions nobody had tried?",
        "options": [
            {"text": "They proved it in advance from the position each metal "
                     "already held in the series, before any liquid was used",
             "correct": False,
             "why": "The series was the thing being tested, so it cannot be "
                    "the proof of itself"},
            {"text": "They could not be sure; the order was checked against "
                     "new reactions and kept holding", "correct": True},
            {"text": "They could be sure, because an order once written down "
                     "cannot be wrong", "correct": False,
             "why": "Any order can be overturned by a result that disagrees "
                    "with it"},
            {"text": "They could be sure, because reactivity is measured on a "
                     "scale with units", "correct": False,
             "why": "Reactivity has no units. The series is an order, not a "
                    "measurement scale"},
        ],
        "figure": None,
    },
    {
        "id": "c9-01-h25",
        "band": "harder",
        "text": "Which single result would be the strongest evidence that a "
                "newly found metal belongs ABOVE calcium?",
        "options": [
            {"text": "It melts at a lower temperature than calcium does",
             "correct": False,
             "why": "Melting point is a separate property and gives a "
                    "different order"},
            {"text": "It reacts with cold water more vigorously than calcium "
                     "does", "correct": True},
            {"text": "It reacts with dilute acid more vigorously than calcium "
                     "does", "correct": False,
             "why": "Both react hard with acid, and acid is too violent up "
                    "there to separate them"},
            {"text": "It is softer than calcium and can be cut with a knife",
             "correct": False,
             "why": "Softness has no place in the series. Gold is soft and "
                    "sits at the bottom"},
        ],
        "figure": None,
    },
    {
        "id": "c9-01-h26",
        "band": "harder",
        "text": "A metal fizzes in dilute acid and a gas is collected. A "
                "student says this proves the metal is reactive. What is the "
                "careful version?",
        "options": [
            {"text": "It proves the metal is one of the three that react with "
                     "cold water", "correct": False,
             "why": "Cold water was not tested, and the middle band fizzes in "
                    "acid too"},
            {"text": "It proves nothing, because collecting a gas is not a "
                     "chemical test", "correct": False,
             "why": "The gas is a product of the reaction, so its appearance "
                    "is real evidence"},
            {"text": "It places the metal above the ones acid does not touch, "
                     "and says nothing about how high", "correct": True},
            {"text": "It proves the metal is at the very top of the series, "
                     "because only the top three give off hydrogen at all",
             "correct": False,
             "why": "Every metal that reacts with an acid gives hydrogen, all "
                    "the way down to lead"},
        ],
        "figure": None,
    },
    {
        "id": "c9-01-h27",
        "band": "harder",
        "text": "The same metal is put into dilute hydrochloric acid and into "
                "dilute sulfuric acid. Would you expect the same gas?",
        "options": [
            {"text": "Yes — hydrogen", "correct": True},
            {"text": "No — chlorine", "correct": False,
             "why": "The chlorine stays in the salt. The gas a metal and an "
                    "acid give is hydrogen"},
            {"text": "No — sulfur dioxide", "correct": False,
             "why": "The sulfur stays in the salt, and the gas is hydrogen "
                    "from both acids"},
            {"text": "Only in the top band", "correct": False,
             "why": "Every metal that reacts with an acid gives hydrogen, "
                    "wherever it sits"},
        ],
        "figure": None,
    },
    {
        "id": "c9-01-h28",
        "band": "harder",
        "text": "Which single result from the bench would most upset the "
                "order potassium, calcium, magnesium, zinc, iron, copper?",
        "options": [
            {"text": "Iron fizzing more slowly in dilute acid than zinc "
                     "granules of the same size do", "correct": False,
             "why": "That is exactly what the order predicts, so it supports "
                    "it"},
            {"text": "Copper giving nothing in either liquid", "correct": False,
             "why": "That is the result the order predicts for the bottom of "
                    "the list"},
            {"text": "Magnesium fizzing in cold water as hard as calcium "
                     "does", "correct": True},
            {"text": "Potassium's hydrogen catching fire", "correct": False,
             "why": "That is what puts potassium at the top, so it fits the "
                    "order"},
        ],
        "figure": None,
    },
    {
        "id": "c9-01-h29",
        "band": "harder",
        "text": "The reference list has twelve entries and the bench tests "
                "six of them. Why were those six chosen?",
        "options": [
            {"text": "Because they are the six cheapest metals for a school "
                     "to buy", "correct": False,
             "why": "Potassium is neither cheap nor easy to keep, and it is "
                    "on the bench"},
            {"text": "Because they are the six that react with dilute acid",
             "correct": False,
             "why": "Copper is on the bench and does not react with dilute "
                    "acid"},
            {"text": "Because they are spread across the whole list, so all "
                     "three bands appear", "correct": True},
            {"text": "Because they are the six metals from the top half of "
                     "the reference list, where the reactions are easiest to "
                     "see", "correct": False,
             "why": "Copper and iron are in the bottom half, and both are on "
                    "the bench"},
        ],
        "figure": None,
    },
    {
        "id": "c9-01-h30",
        "band": "harder",
        "text": "Sodium is kept under oil; magnesium ribbon is kept in an "
                "open drawer. Both are in the upper half of the list. Explain "
                "the difference.",
        "options": [
            {"text": "Magnesium is a non-metal, so it does not need "
                     "protecting", "correct": False,
             "why": "Magnesium is a metal. The difference is how quickly each "
                    "one reacts with air"},
            {"text": "Sodium is more expensive, so it is stored more "
                     "carefully", "correct": False,
             "why": "The oil is there for chemistry rather than for value. It "
                    "keeps air and damp off"},
            {"text": "Magnesium is below carbon, and nothing below carbon "
                     "reacts with air", "correct": False,
             "why": "Magnesium is above carbon, and plenty of metals below "
                    "carbon tarnish in air"},
            {"text": "Sodium reacts with air and damp fast enough to matter "
                     "within seconds, while magnesium's reaction is slow "
                     "enough for a drawer to be fine", "correct": True},
        ],
        "figure": None,
    },
]
