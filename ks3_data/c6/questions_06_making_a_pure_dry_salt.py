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

    # ── easier · MRB-335 top-up ─────────────────────────────────────────
    {
        "id": "c6-06-e05",
        "band": "easier",
        "text": "In this method, what does adding a base in excess mean?",
        "options": [
            {"text": "Adding more than enough of it, so that none of the acid "
                     "can be left",
             "correct": True},
            {"text": "Adding exactly the amount the acid needs, measured out "
                     "carefully beforehand so that nothing at all is wasted "
                     "and nothing is left over",
             "correct": False,
             "why": "That is the opposite of excess. The point is to add MORE "
                    "than enough"},
            {"text": "Adding it very quickly",
             "correct": False,
             "why": "It goes in a spatula at a time, with stirring. Excess is "
                    "about amount, not speed"},
            {"text": "Adding a second base as well as the first",
             "correct": False,
             "why": "One base is used. Excess means more of that one"},
        ],
        "figure": None,
    },
    {
        "id": "c6-06-e06",
        "band": "easier",
        "text": "Which salt does hydrochloric acid make with magnesium "
                "oxide?",
        "options": [
            {"text": "Magnesium hydrochloride, taking its name from the metal "
                     "and then the whole name of the acid that was used",
             "correct": False,
             "why": "The acid supplies an ENDING rather than its whole name. "
                    "Hydrochloric acid gives chlorides"},
            {"text": "Magnesium chloride",
             "correct": True},
            {"text": "Magnesium sulfate",
             "correct": False,
             "why": "Sulfates come from sulfuric acid"},
            {"text": "Magnesium oxide chloride",
             "correct": False,
             "why": "The oxide is used up in the reaction — its oxygen leaves "
                    "as part of the water"},
        ],
        "figure": None,
    },
    {
        "id": "c6-06-e07",
        "band": "easier",
        "text": "Why is the filtrate not boiled all the way to dryness?",
        "options": [
            {"text": "Because the last of the water carries the impurities "
                     "with it as it goes, so stopping early leaves a purer "
                     "solid in the dish",
             "correct": False,
             "why": "Nothing leaves with the water. The reason is the size "
                    "and quality of the crystals"},
            {"text": "Because the salt would be destroyed by the heat",
             "correct": False,
             "why": "The salt survives. What is lost is the chance for it to "
                    "grow into crystals"},
            {"text": "Because boiling to dryness gives powder rather than "
                     "crystals",
             "correct": True},
            {"text": "Because less salt would be recovered",
             "correct": False,
             "why": "The same mass is recovered either way. It is the form "
                    "that differs"},
        ],
        "figure": None,
    },
    {
        "id": "c6-06-e08",
        "band": "easier",
        "text": "A jar is labelled copper sulfate. Which acid must have made "
                "it?",
        "options": [
            {"text": "Hydrochloric acid",
             "correct": False,
             "why": "Hydrochloric acid makes chlorides. This one is a "
                    "sulfate"},
            {"text": "Nitric acid",
             "correct": False,
             "why": "Nitric acid makes nitrates"},
            {"text": "Any of the three, since the acid decides only how fast "
                     "the reaction goes and the metal decides what the salt "
                     "will be called",
             "correct": False,
             "why": "The metal gives the first word and the acid gives the "
                    "ending. A sulfate can only have come from sulfuric "
                    "acid"},
            {"text": "Sulfuric acid",
             "correct": True},
        ],
        "figure": None,
    },

    # ── standard · MRB-335 top-up ───────────────────────────────────────
    {
        "id": "c6-06-s05",
        "band": "standard",
        "text": "Why is the acid warmed gently at the start rather than "
                "boiled?",
        "options": [
            {"text": "Warming speeds the reaction up; boiling would drive "
                     "acid off before it had reacted",
             "correct": True},
            {"text": "Because boiling would decompose the salt as fast as it "
                     "was formed, so nothing would be left in the beaker to "
                     "crystallise afterwards",
             "correct": False,
             "why": "The salt is stable in the beaker. Boiling would drive "
                    "acid off before it had reacted"},
            {"text": "Because a hot solution cannot be filtered",
             "correct": False,
             "why": "A warm solution filters perfectly well, and often better "
                    "than a cold one"},
            {"text": "Because copper oxide only dissolves in cold acid",
             "correct": False,
             "why": "Warming is what makes it react faster. Cold acid would "
                    "be slower, not better"},
        ],
        "figure": None,
    },
    {
        "id": "c6-06-s06",
        "band": "standard",
        "text": "A student filters the blue solution and leaves it on a "
                "windowsill to cool, without heating it first. What do they "
                "get?",
        "options": [
            {"text": "Large crystals, and more of them than heating would "
                     "have given, because nothing has been lost to the air as "
                     "steam along the way",
             "correct": False,
             "why": "Nothing is lost by heating either — the salt cannot "
                    "leave the beaker. The problem is that the solution is "
                    "too dilute"},
            {"text": "Very little, because the solution is too dilute for "
                     "crystals to come out of it",
             "correct": True},
            {"text": "A white powder instead of blue crystals",
             "correct": False,
             "why": "White powder is what over-heating gives. Under-heating "
                    "gives almost nothing at all"},
            {"text": "The same crystals, a few days later",
             "correct": False,
             "why": "Some water does evaporate from an open beaker, and a "
                    "windowsill is a slow way to reach a concentration that "
                    "heating reaches in minutes"},
        ],
        "figure": None,
    },
    {
        "id": "c6-06-s07",
        "band": "standard",
        "text": "What is being removed when the mixture is filtered?",
        "options": [
            {"text": "The salt, which stays in the paper as crystals while "
                     "the water and the unreacted solid run through into the "
                     "flask below",
             "correct": False,
             "why": "The salt is dissolved, so it goes THROUGH with the "
                    "water. It is recovered later, by crystallising"},
            {"text": "The water",
             "correct": False,
             "why": "The water passes through as part of the filtrate. It is "
                    "removed later, by evaporating"},
            {"text": "The leftover base that did not react",
             "correct": True},
            {"text": "The acid",
             "correct": False,
             "why": "There is no acid left — that is the whole point of "
                    "adding the base in excess"},
        ],
        "figure": None,
    },
    {
        "id": "c6-06-s08",
        "band": "standard",
        "text": "A student adds an exactly measured amount of copper oxide "
                "instead of an excess, and gets it slightly wrong. Which way "
                "round is the mistake worse?",
        "options": [
            {"text": "Either way is equally bad, because whatever is left "
                     "over ends up dried into the crystals at the end of the "
                     "method",
             "correct": False,
             "why": "Only one of the two can be removed. Leftover solid "
                    "filters out; leftover acid does not"},
            {"text": "Too much copper oxide is worse, because the extra ends "
                     "up in the crystals",
             "correct": False,
             "why": "The extra is filtered off before the crystals are grown. "
                    "That is why excess is safe"},
            {"text": "Too much copper oxide is worse, because it uses up the "
                     "salt",
             "correct": False,
             "why": "It reacts with nothing once the acid has gone. It simply "
                    "sits there waiting to be filtered"},
            {"text": "Too little copper oxide is worse, because leftover acid "
                     "cannot be filtered out",
             "correct": True},
        ],
        "figure": None,
    },

    # ── harder · MRB-335 top-up ─────────────────────────────────────────
    {
        "id": "c6-06-h05",
        "band": "harder",
        "text": "Copper carbonate can be used instead of copper oxide to make "
                "copper sulfate. What is different about the method?",
        "options": [
            {"text": "It fizzes, because carbon dioxide is given off as well",
             "correct": True},
            {"text": "The salt produced is a carbonate rather than a sulfate, "
                     "because the base now supplies the ending as well as the "
                     "metal",
             "correct": False,
             "why": "The ACID always supplies the ending. Sulfuric acid gives "
                    "a sulfate whichever copper compound is used"},
            {"text": "Nothing is different at all",
             "correct": False,
             "why": "An acid and a carbonate give three products rather than "
                    "two. You can see the third one leaving"},
            {"text": "No filtering is needed, because copper carbonate "
                     "dissolves",
             "correct": False,
             "why": "It is insoluble too, which is exactly why it can be used "
                    "in excess and filtered off"},
        ],
        "figure": None,
    },
    {
        "id": "c6-06-h06",
        "band": "harder",
        "text": "A student uses twice as much copper oxide as before, with "
                "the same acid. How much copper sulfate do they get?",
        "options": [
            {"text": "Twice as much, since doubling one of the two things "
                     "that react always doubles the amount of product that "
                     "comes out of the reaction",
             "correct": False,
             "why": "Doubling helps only while the other is still available. "
                    "The acid ran out first"},
            {"text": "The same amount, because the acid sets the yield",
             "correct": True},
            {"text": "Half as much, because the extra oxide gets in the way",
             "correct": False,
             "why": "The excess solid does nothing at all. It is filtered "
                    "off"},
            {"text": "None, because the mixture is now unbalanced",
             "correct": False,
             "why": "There is no such thing as an unbalanced mixture here. "
                    "The reaction runs until the acid is used up"},
        ],
        "figure": None,
    },
    {
        "id": "c6-06-h07",
        "band": "harder",
        "text": "Making sodium chloride from hydrochloric acid and sodium "
                "hydroxide needs the reaction done TWICE. Why?",
        "options": [
            {"text": "Because one run is never accurate enough, so it is done "
                     "again and the two volumes are averaged before the "
                     "crystals are grown from the second beaker",
             "correct": False,
             "why": "The second run is not a repeat for accuracy. It is done "
                    "without indicator, so the crystals are not stained"},
            {"text": "Because sodium hydroxide reacts too slowly to finish in "
                     "one go",
             "correct": False,
             "why": "It reacts instantly. The difficulty is knowing when to "
                    "stop"},
            {"text": "Because the first run uses indicator to find the "
                     "volume, and the second repeats it with no dye in the "
                     "product",
             "correct": True},
            {"text": "Because the salt has to be dissolved and recrystallised "
                     "to purify it",
             "correct": False,
             "why": "That is a different technique altogether, and it is not "
                    "what the two runs are for"},
        ],
        "figure": None,
    },
    {
        "id": "c6-06-h08",
        "band": "harder",
        "text": "A jar of sodium sulfate is handed to you. The acid that made "
                "it can be named for certain; the base cannot. Why not?",
        "options": [
            {"text": "Because the base is used up completely in the reaction "
                     "and leaves nothing of itself behind in the salt for "
                     "anybody to identify afterwards",
             "correct": False,
             "why": "The metal from the base is in the salt and names it. "
                    "What is missing is which sodium compound supplied it"},
            {"text": "Because sulfates can be made without a base at all",
             "correct": False,
             "why": "A salt needs a metal from somewhere, and that somewhere "
                    "is a base or a metal itself"},
            {"text": "Because sodium is not a base",
             "correct": False,
             "why": "Sodium hydroxide and sodium carbonate are both bases. "
                    "That is exactly the difficulty — there is more than one"},
            {"text": "Because the acid gives the ending and the base only "
                     "gives the metal, and several sodium compounds are bases",
             "correct": True},
        ],
        "figure": None,
    },
]
