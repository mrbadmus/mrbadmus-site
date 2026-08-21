"""C6 lesson 06 — Making a pure dry salt: twelve questions (MRB-269).

The lesson's argument has two halves: a salt's NAME tells you what made it, and
a pure sample is a sequence of decisions rather than a reaction. These twelve
probe the angles the mastery ladder leaves alone.

The distractors are built from the lesson's declared misconception.

`ACID-09` (boiling a solution dry gives the best crystals) drives e04, s03,
h01 and h04. h01 is the one that matters: it asks what is WRONG with the powder
you get, so "it worked, it was just faster" has to account for a product that
is neither crystalline nor pure.

A second strand, everywhere on the page and in no register entry, is that
EXCESS IS WASTE. e03, s01 and h02 are built on it: adding too much on purpose
is the decision the whole method turns on, and a student who reads excess as
carelessness cannot explain why the filter step exists.

A third strand is the naming rule read backwards. e01, e02 and s02 ask what
made a named salt rather than what a named pair makes, which is the harder
direction and the one an exam asks.

A fourth strand is that soluble and insoluble are interchangeable. s04 and h03
turn on the fact that a base which dissolves cannot be filtered off, which is
the whole reason the sodium chloride preparation is a different method.

Every question here is new prose, and the bar is §13's. No correct answer is
strictly the longest in its set by four words or by 1.4x, and the twelve are
authored level across the four answer positions — three apiece (MRB-278).
"""

UNIT = "C6"
LESSON = "making-a-pure-dry-salt"
LESSON_NUMBER = 6

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "c6-06-e01",
        "band": "easier",
        "text": "Sulfuric acid is neutralised with copper oxide. What salt is "
                "made?",
        "options": [
            {"text": "Copper sulfate", "correct": True},
            {"text": "Copper chloride", "correct": False,
             "why": "Chlorides come from hydrochloric acid. The acid decides "
                    "the ending."},
            {"text": "Sulfur copperate", "correct": False,
             "why": "The metal always comes first and the acid supplies the "
                    "ending. There is no such compound."},
            {"text": "Copper oxide sulfate", "correct": False,
             "why": "The oxide is used up in the reaction — its oxygen leaves "
                    "as part of the water."},
        ],
        "figure": None,
    },
    {
        "id": "c6-06-e02",
        "band": "easier",
        "text": "A jar is labelled magnesium nitrate. Which two things must "
                "have made it?",
        "options": [
            {"text": "Magnesium and sulfuric acid", "correct": False,
             "why": "Sulfuric acid would have given a sulfate. The ending "
                    "names the acid and this one says nitric."},
            {"text": "Magnesium and nitric acid", "correct": True},
            {"text": "Nitrogen and magnesium oxide", "correct": False,
             "why": "Nitrogen gas is not an acid and makes no salt. The "
                    "nitrate came from nitric acid."},
            {"text": "Magnesium and hydrochloric acid", "correct": False,
             "why": "Hydrochloric acid gives chlorides. The name would have "
                    "been magnesium chloride."},
        ],
        "figure": None,
    },
    {
        "id": "c6-06-e03",
        "band": "easier",
        "text": "Why is copper oxide added until no more will dissolve?",
        "options": [
            {"text": "To use up every last bit of the acid", "correct": True},
            {"text": "To make as much copper sulfate as possible",
             "correct": False,
             "why": "Once the acid is used up, extra oxide makes nothing "
                    "more. The yield is set by the acid."},
            {"text": "To make the solution a deeper blue colour",
             "correct": False,
             "why": "The colour is a side effect. What matters is that no "
                    "acid survives into the product."},
            {"text": "To make sure the reaction happens quickly enough",
             "correct": False,
             "why": "Warming is what speeds it up. The excess is about "
                    "purity, not speed."},
        ],
        "figure": None,
    },
    {
        "id": "c6-06-e04",
        "band": "easier",
        "text": "Which step grows large, regular crystals?",
        "options": [
            {"text": "Boiling the solution until every drop of water has "
                     "gone", "correct": False,
             "why": "Boiling dry throws thousands of tiny crystals out at "
                    "once and leaves a caked powder."},
            {"text": "Pouring the hot solution into a dish of cold water",
             "correct": False,
             "why": "That is even faster cooling than a boil. Fast means "
                    "small, every time."},
            {"text": "Leaving the concentrated solution to cool slowly",
             "correct": True},
            {"text": "Filtering the solution a second time while it is still "
                     "hot", "correct": False,
             "why": "Filtering removes solids and grows nothing. The crystals "
                    "have not formed yet at that stage."},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "c6-06-s01",
        "band": "standard",
        "text": "What is the leftover copper oxide at the bottom of the "
                "beaker actually FOR?",
        "options": [
            {"text": "It is waste and should have been avoided by weighing "
                     "carefully", "correct": False,
             "why": "It is deliberate. Weighing exactly would leave you "
                    "guessing whether any acid survived."},
            {"text": "It is the signal that the acid has all been used up",
             "correct": True},
            {"text": "It is a catalyst that keeps the reaction going to the "
                     "end", "correct": False,
             "why": "No catalyst is involved. It is a reactant that has been "
                    "supplied in excess on purpose."},
            {"text": "It is what will be filtered out and sold on as the "
                     "product", "correct": False,
             "why": "The product is dissolved in the liquid that passes "
                    "through. The solid on the paper is thrown away."},
        ],
        "figure": None,
    },
    {
        "id": "c6-06-s02",
        "band": "standard",
        "text": "Calcium carbonate is added to hydrochloric acid and the "
                "mixture fizzes. What are all three products?",
        "options": [
            {"text": "Calcium chloride, water and hydrogen", "correct": False,
             "why": "Hydrogen comes from an acid with a METAL. A carbonate "
                    "gives off carbon dioxide instead."},
            {"text": "Calcium sulfate, water and carbon dioxide",
             "correct": False,
             "why": "Sulfates come from sulfuric acid. This one is "
                    "hydrochloric, so the salt is a chloride."},
            {"text": "Calcium chloride, water and carbon dioxide",
             "correct": True},
            {"text": "Calcium chloride and carbon dioxide only",
             "correct": False,
             "why": "Water is made as well, in every neutralisation. The "
                    "carbonate simply adds a third product."},
        ],
        "figure": None,
    },
    {
        "id": "c6-06-s03",
        "band": "standard",
        "text": "How do you know when to stop heating the filtrate?",
        "options": [
            {"text": "When the last of the liquid has boiled away",
             "correct": False,
             "why": "That is too far. Stopping there gives powder rather than "
                    "crystals."},
            {"text": "When the solution changes colour in the basin",
             "correct": False,
             "why": "The colour deepens gradually as it concentrates and "
                    "names no particular moment."},
            {"text": "When the basin has been on the heat for ten minutes",
             "correct": False,
             "why": "A time depends on the heat and the volume. The test is "
                    "what the solution does, not the clock."},
            {"text": "When a drop on a cold glass rod forms crystals",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c6-06-s04",
        "band": "standard",
        "text": "Why can this method not be used with sodium hydroxide "
                "instead of copper oxide?",
        "options": [
            {"text": "Because sodium hydroxide dissolves, so excess cannot be "
                     "filtered off", "correct": True},
            {"text": "Because sodium hydroxide is not a base and will not "
                     "react", "correct": False,
             "why": "It is a base and it reacts perfectly well. The problem "
                    "is what happens to any excess."},
            {"text": "Because sodium salts do not form crystals at all",
             "correct": False,
             "why": "Sodium chloride crystallises beautifully. Getting to a "
                    "pure solution is the hard part, not the crystals."},
            {"text": "Because the reaction would be far too slow to be "
                     "practical", "correct": False,
             "why": "It is fast — faster than with a solid. Speed is not what "
                    "rules the method out."},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "c6-06-h01",
        "band": "harder",
        "text": "A student boils their solution to dryness and gets a white "
                "cake instead of crystals. What is wrong with it?",
        "options": [
            {"text": "It is the wrong compound, made by the heat of boiling",
             "correct": False,
             "why": "It is the right salt. What is wrong is its form and what "
                    "is trapped inside it."},
            {"text": "It is thousands of tiny crystals with impurities "
                     "trapped in them", "correct": True},
            {"text": "It is nothing at all — the salt evaporated with the "
                     "water", "correct": False,
             "why": "A solid salt does not evaporate. It is all still in the "
                    "basin, in the wrong shape."},
            {"text": "It is pure but simply looks less impressive than "
                     "crystals", "correct": False,
             "why": "It is not pure. Anything else dissolved in the water was "
                    "thrown out of solution with it."},
        ],
        "figure": None,
    },
    {
        "id": "c6-06-h02",
        "band": "harder",
        "text": "Why would leaving excess ACID be a much worse mistake than "
                "leaving excess base?",
        "options": [
            {"text": "Because acid reacts with the filter paper and destroys "
                     "it", "correct": False,
             "why": "Filter paper survives dilute acid. The problem is that "
                    "the acid never reaches the paper."},
            {"text": "Because acid is more expensive than the base being used",
             "correct": False,
             "why": "Cost decides nothing here. The reason is that one can be "
                    "removed and the other cannot."},
            {"text": "Because the acid is dissolved, so filtering cannot take "
                     "it out", "correct": True},
            {"text": "Because excess acid would stop the crystals from ever "
                     "forming", "correct": False,
             "why": "Crystals would still form. They would form with acid in "
                    "the solution around them, which is the contamination."},
        ],
        "figure": None,
    },
    {
        "id": "c6-06-h03",
        "band": "harder",
        "text": "How is sodium chloride made pure from acid and alkali, given "
                "that neither excess can be filtered off?",
        "options": [
            {"text": "By adding the alkali slowly until the mixture in the "
                     "beaker stops fizzing", "correct": False,
             "why": "An acid with an alkali gives no gas at all, so there is "
                    "nothing to stop. That test belongs to carbonates."},
            {"text": "By filtering the finished solution through a much finer "
                     "grade of paper", "correct": False,
             "why": "Filtering separates a solid from a liquid. Everything "
                    "here is dissolved and passes straight through."},
            {"text": "By adding excess alkali and then boiling the extra away "
                     "at the end", "correct": False,
             "why": "Sodium hydroxide does not boil away and would be left "
                    "behind with the salt, which is worse."},
            {"text": "By using a titration to find the exact volume, then "
                     "repeating it without indicator", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c6-06-h04",
        "band": "harder",
        "text": "Two students make copper sulfate. One gets large blue "
                "crystals, one gets blue powder. What did the second do "
                "differently?",
        "options": [
            {"text": "They used a different acid, so the salt came out "
                     "differently", "correct": False,
             "why": "A different acid would give a different salt with a "
                    "different name. Both made copper sulfate."},
            {"text": "They filtered before the reaction had finished",
             "correct": False,
             "why": "Filtering early would lose yield rather than change the "
                    "crystal size. The shape is decided at the cooling step."},
            {"text": "They did not add enough copper oxide to use up the acid",
             "correct": False,
             "why": "Leftover acid contaminates the product without turning "
                    "crystals into powder. The form comes from the cooling."},
            {"text": "They cooled the solution too fast, or dried it out "
                     "completely", "correct": True},
        ],
        "figure": None,
    },
]
