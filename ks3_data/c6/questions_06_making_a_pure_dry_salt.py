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

    # ── MRB-338 expansion ───────────
    {
        "id": "c6-06-e09",
        "band": "easier",
        "text": "Copper oxide is added to nitric acid. Name the salt that forms.",
        "options": [
            {"text": "Copper chloride", "correct": False,
             "why": "Chlorides come from hydrochloric acid, and none was used here."},
            {"text": "Sodium nitrate", "correct": False,
             "why": "There is no sodium in copper oxide. The metal in the salt is "
                    "the metal in the base."},
            {"text": "Copper nitrate", "correct": True},
            {"text": "Copper oxide nitrate", "correct": False,
             "why": "The oxide is used up in the reaction, and its oxygen leaves as "
                    "part of the water."},
        ],
        "figure": None,
    },
    {
        "id": "c6-06-e10",
        "band": "easier",
        "text": "Which of these bases dissolves in water?",
        "options": [
            {"text": "Copper oxide", "correct": False,
             "why": "Copper oxide barely dissolves, which is what makes it usable in"
                    " excess for this method."},
            {"text": "Magnesium oxide", "correct": False,
             "why": "Magnesium oxide is insoluble too, and it behaves the same way "
                    "in this preparation."},
            {"text": "Calcium carbonate", "correct": False,
             "why": "Calcium carbonate is chalk, and it sits on the bottom of the "
                    "beaker rather than dissolving."},
            {"text": "Sodium hydroxide", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c6-06-e11",
        "band": "easier",
        "text": "Which of these bases makes the mixture fizz when it is added to an "
                "acid?",
        "options": [
            {"text": "Calcium carbonate", "correct": True},
            {"text": "Magnesium hydroxide", "correct": False,
             "why": "A hydroxide gives a salt and water only. There is no carbon in "
                    "it, so no gas can come off."},
            {"text": "Magnesium oxide", "correct": False,
             "why": "Another oxide, and another two-product reaction with no gas at "
                    "all."},
            {"text": "Sodium hydroxide", "correct": False,
             "why": "A hydroxide gives a salt and water. Only a carbonate gives "
                    "carbon dioxide as well."},
        ],
        "figure": None,
    },
    {
        "id": "c6-06-e12",
        "band": "easier",
        "text": "What does insoluble mean?",
        "options": [
            {"text": "Will not react with acid", "correct": False,
             "why": "Copper oxide is insoluble and reacts with acid readily. The two"
                    " are different questions."},
            {"text": "Will not dissolve", "correct": True},
            {"text": "Will not melt when heated", "correct": False,
             "why": "Melting is about heat. Dissolving is about whether it goes into"
                    " a liquid."},
            {"text": "Will not mix with another solid", "correct": False,
             "why": "Solids mix perfectly well. The word is about what happens in "
                    "water."},
        ],
        "figure": None,
    },
    {
        "id": "c6-06-e13",
        "band": "easier",
        "text": "What is the filtrate?",
        "options": [
            {"text": "The solid caught on the filter paper", "correct": False,
             "why": "That is the residue. The filtrate is what got past the paper."},
            {"text": "The crystals grown at the end of the method", "correct": False,
             "why": "The crystals come several steps later, out of the filtrate "
                    "rather than being it."},
            {"text": "The paper itself, once it has been used", "correct": False,
             "why": "The paper is apparatus. The word names one of the two things "
                    "filtering separates."},
            {"text": "The liquid that passes through the filter paper", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c6-06-e14",
        "band": "easier",
        "text": "How are the finished crystals dried?",
        "options": [
            {"text": "Patted between filter papers", "correct": True},
            {"text": "Boiled in the evaporating basin", "correct": False,
             "why": "Boiling at this stage would cake the crystals together and "
                    "spoil their shape."},
            {"text": "Rinsed under the cold tap", "correct": False,
             "why": "Rinsing would dissolve the very crystals you spent the lesson "
                    "growing."},
            {"text": "Left in the sun on the windowsill", "correct": False,
             "why": "The solution clinging to them would dry on as a crust rather "
                    "than being taken away."},
        ],
        "figure": None,
    },
    {
        "id": "c6-06-e15",
        "band": "easier",
        "text": "What colour are copper sulfate crystals?",
        "options": [
            {"text": "Black", "correct": False,
             "why": "Black is copper oxide, the powder you started with rather than "
                    "the salt you made."},
            {"text": "Blue", "correct": True},
            {"text": "White", "correct": False,
             "why": "White crystals are what a sodium or magnesium salt gives. "
                    "Copper salts are coloured."},
            {"text": "Pale green", "correct": False,
             "why": "Pale green belongs to an iron salt, not a copper one."},
        ],
        "figure": None,
    },
    {
        "id": "c6-06-e16",
        "band": "easier",
        "text": "Which apparatus separates the leftover solid from the salt solution?",
        "options": [
            {"text": "A burette and stand", "correct": False,
             "why": "A burette measures a liquid out a drop at a time and separates "
                    "nothing."},
            {"text": "An evaporating basin", "correct": False,
             "why": "That drives water off a solution. It cannot take a solid out of"
                    " one."},
            {"text": "A filter funnel and paper", "correct": True},
            {"text": "A delivery tube and bung", "correct": False,
             "why": "Those carry a gas from one tube to another, which is not what "
                    "is needed here."},
        ],
        "figure": None,
    },
    {
        "id": "c6-06-e17",
        "band": "easier",
        "text": "Nitric acid is poured onto sodium hydroxide solution. Name the salt "
                "formed.",
        "options": [
            {"text": "Sodium chloride", "correct": False,
             "why": "Chlorides come from hydrochloric acid, which was not the acid "
                    "used."},
            {"text": "Sodium sulfate", "correct": False,
             "why": "Sulfates come from sulfuric acid. Nitric acid gives a different"
                    " family."},
            {"text": "Copper nitrate", "correct": False,
             "why": "The metal comes from the base, and there is no copper in sodium"
                    " hydroxide."},
            {"text": "Sodium nitrate", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c6-06-e18",
        "band": "easier",
        "text": "Ammonium nitrate and ammonium sulfate are made by neutralising acids"
                " with ammonia. What are they used for?",
        "options": [
            {"text": "As fertilisers", "correct": True},
            {"text": "As fuels for engines", "correct": False,
             "why": "They are not burnt for power. Their use is on the land rather "
                    "than in a tank."},
            {"text": "As indicators in school laboratories", "correct": False,
             "why": "Indicators are dyes. A salt has no colour change to offer."},
            {"text": "As building materials", "correct": False,
             "why": "Calcium sulfate goes into plasterboard, but these two are "
                    "spread on fields."},
        ],
        "figure": None,
    },
    {
        "id": "c6-06-e19",
        "band": "easier",
        "text": "Copper sulfate is sprayed onto vines. What is it doing there?",
        "options": [
            {"text": "Feeding the plant as a fertiliser", "correct": False,
             "why": "Ammonium salts are the fertilisers. This one is there to kill "
                    "something."},
            {"text": "Acting as a fungicide", "correct": True},
            {"text": "Colouring the fruit blue as it ripens", "correct": False,
             "why": "The salt is blue but the crop is not dyed by it. Its job is "
                    "protection."},
            {"text": "Neutralising the acid in the soil", "correct": False,
             "why": "A salt is already neutral. Lime is what is spread on acidic "
                    "ground."},
        ],
        "figure": None,
    },
    {
        "id": "c6-06-e20",
        "band": "easier",
        "text": "What is the first thing done to the acid in this method?",
        "options": [
            {"text": "It is warmed gently", "correct": True},
            {"text": "It is boiled hard", "correct": False,
             "why": "Boiling would drive acid off before it had reacted with "
                    "anything."},
            {"text": "It is cooled in ice", "correct": False,
             "why": "Cooling would slow the reaction down rather than help it along."},
            {"text": "It is filtered", "correct": False,
             "why": "There is nothing to filter out yet. Filtering comes after the "
                    "base has been added."},
        ],
        "figure": None,
    },
    {
        "id": "c6-06-e21",
        "band": "easier",
        "text": "How can you see that no more copper oxide will react?",
        "options": [
            {"text": "The solution stops being blue", "correct": False,
             "why": "The blue deepens as the salt forms and stays. It does not fade "
                    "away."},
            {"text": "The beaker becomes cold to the touch", "correct": False,
             "why": "The beaker is warmed on purpose, and temperature is not the "
                    "signal being watched."},
            {"text": "Black powder settles out instead of dissolving", "correct": True},
            {"text": "The mixture begins to fizz steadily", "correct": False,
             "why": "An oxide gives no gas at all. Fizzing would mean a carbonate "
                    "had been used instead."},
        ],
        "figure": None,
    },
    {
        "id": "c6-06-s09",
        "band": "standard",
        "text": "Calcium carbonate chips are added to dilute sulfuric acid and the "
                "fizzing stops almost at once. Explain why.",
        "options": [
            {"text": "The calcium sulfate formed barely dissolves and coats the chips", "correct": True},
            {"text": "Calcium carbonate is not a base, so the reaction was never "
                      "going to run", "correct": False,
             "why": "It is a base and it does react. Something stops it part-way "
                    "rather than preventing it."},
            {"text": "Sulfuric acid does not react with carbonates, only with oxides", "correct": False,
             "why": "It reacts with carbonates readily. The fizzing at the start "
                    "proves it began."},
            {"text": "The acid was used up within the first few seconds of the "
                      "reaction", "correct": False,
             "why": "Plenty of acid is left. What has changed is that it can no "
                    "longer reach the chips."},
        ],
        "figure": None,
    },
    {
        "id": "c6-06-s10",
        "band": "standard",
        "text": "Explain why a carbonate base makes the beaker fizz while an oxide "
                "base does not.",
        "options": [
            {"text": "A carbonate is a powder and an oxide is a lump", "correct": False,
             "why": "Both come as powders, and the shape of the solid does not "
                    "decide whether a gas is made."},
            {"text": "A carbonate gives carbon dioxide as well as salt and water", "correct": True},
            {"text": "A carbonate dissolves and an oxide does not, and dissolving is "
                      "what causes the bubbles", "correct": False,
             "why": "Calcium carbonate does not dissolve, and dissolving produces no"
                    " bubbles in any case."},
            {"text": "A carbonate makes hydrogen rather than carbon dioxide", "correct": False,
             "why": "Hydrogen comes from a metal. A carbonate gives carbon dioxide."},
        ],
        "figure": None,
    },
    {
        "id": "c6-06-s11",
        "band": "standard",
        "text": "A student filters the mixture while some acid is still unreacted. "
                "What is the consequence?",
        "options": [
            {"text": "Nothing, because filtering removes acid as well as solid", "correct": False,
             "why": "Acid is dissolved in the liquid and goes straight through the "
                    "paper with it."},
            {"text": "The reaction stops for good and no salt is made at all", "correct": False,
             "why": "The salt already made is in the filtrate. What is lost is the "
                    "guarantee of purity."},
            {"text": "The crystals grow larger, because there is more liquid to grow "
                      "in", "correct": False,
             "why": "Crystal size depends on cooling rate, and the real problem here"
                    " is what is dissolved in the liquid."},
            {"text": "Acid passes through with the filtrate and ends up in the "
                      "crystals", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c6-06-s12",
        "band": "standard",
        "text": "One student cools the concentrated solution slowly on a bench; "
                "another puts it straight in a freezer. Compare the crystals.",
        "options": [
            {"text": "The bench gives large regular crystals; the freezer gives a "
                      "mass of tiny ones", "correct": True},
            {"text": "The freezer gives larger crystals, because cold makes solids "
                      "grow faster", "correct": False,
             "why": "Fast cooling throws many crystals out at once, and each of them"
                    " stays small."},
            {"text": "Both give exactly the same crystals either way", "correct": False,
             "why": "The solution was the same; how it was cooled was not, and that "
                    "is what sets the size."},
            {"text": "The freezer gives no crystals at all, because the solution "
                      "freezes solid first", "correct": False,
             "why": "Crystals of the salt still separate out. They are simply small "
                    "and numerous."},
        ],
        "figure": None,
    },
    {
        "id": "c6-06-s13",
        "band": "standard",
        "text": "Magnesium oxide is used instead of copper oxide, with the same "
                "sulfuric acid. What changes?",
        "options": [
            {"text": "The method changes completely, because magnesium oxide "
                      "dissolves and cannot be filtered", "correct": False,
             "why": "Magnesium oxide is insoluble too, so excess can be added and "
                    "filtered exactly as before."},
            {"text": "The acid has to be changed as well, since magnesium will not "
                      "react with sulfuric acid", "correct": False,
             "why": "Magnesium oxide and sulfuric acid react perfectly well to give "
                    "magnesium sulfate."},
            {"text": "Nothing about the method; the salt is magnesium sulfate instead", "correct": True},
            {"text": "Nothing at all; both oxides give the same salt", "correct": False,
             "why": "The metal names the salt, so one gives copper sulfate and the "
                    "other magnesium sulfate."},
        ],
        "figure": None,
    },
    {
        "id": "c6-06-s14",
        "band": "standard",
        "text": "A student adds a carbonate base all at once and the mixture froths "
                "over the top of the beaker. Suggest the fix.",
        "options": [
            {"text": "Boil the acid first so that the gas comes off before the solid "
                      "goes in", "correct": False,
             "why": "The gas is made by the reaction, so it cannot be driven off in "
                    "advance."},
            {"text": "Use a stronger acid, which reacts faster and so is over before "
                      "it can froth", "correct": False,
             "why": "A faster reaction would froth more, not less."},
            {"text": "Add the base a little at a time, in a larger beaker", "correct": True},
            {"text": "Cool the acid in ice, which stops any gas forming at all", "correct": False,
             "why": "Cooling slows the reaction but the same gas is still produced, "
                    "so the froth only takes longer to arrive."},
        ],
        "figure": None,
    },
    {
        "id": "c6-06-s15",
        "band": "standard",
        "text": "The blue filtrate has been heated until about half the water has "
                "gone. What is in the basin at that moment?",
        "options": [
            {"text": "Dry copper sulfate crystals, ready to be patted dry", "correct": False,
             "why": "Crystals appear on cooling. At this point there is still plenty"
                    " of liquid."},
            {"text": "A more concentrated solution of copper sulfate", "correct": True},
            {"text": "Pure water, with the salt already driven off as steam", "correct": False,
             "why": "Only the water leaves as steam. The salt stays behind in the "
                    "basin."},
            {"text": "A mixture of copper oxide and acid, waiting to react", "correct": False,
             "why": "The oxide was filtered out and the acid was used up. Neither is"
                    " in the basin."},
        ],
        "figure": None,
    },
    {
        "id": "c6-06-s16",
        "band": "standard",
        "text": "Why is the last of the solution taken off the crystals before they "
                "are stored?",
        "options": [
            {"text": "Because the liquid clinging to them would dry on as a crust of "
                      "salt", "correct": True},
            {"text": "Because the liquid would dissolve the crystals completely if it"
                      " were left", "correct": False,
             "why": "There is far too little of it for that. What it does is dry "
                    "onto the surface."},
            {"text": "Because the crystals must be kept wet until they are weighed", "correct": False,
             "why": "The whole aim is a dry sample, which is why the liquid is taken"
                    " off at all."},
            {"text": "Because filter paper adds mass to the crystals and makes the "
                      "yield look better", "correct": False,
             "why": "Nothing from the paper joins the crystals. The paper takes "
                    "liquid away."},
        ],
        "figure": None,
    },
    {
        "id": "c6-06-s17",
        "band": "standard",
        "text": "One student warms the acid before adding the copper oxide and "
                "another does not. Compare their results.",
        "options": [
            {"text": "The warmed one gets a different salt, because heat changes what"
                      " is formed", "correct": False,
             "why": "The same two substances react to give the same salt whether "
                    "warmed or not."},
            {"text": "The unwarmed one gets nothing at all, because the reaction "
                      "needs heat to begin", "correct": False,
             "why": "It runs at room temperature too. Warming only makes it quicker."},
            {"text": "The warmed one gets more salt than the other", "correct": False,
             "why": "The amount of salt is set by how much acid there is, not by the"
                    " temperature."},
            {"text": "Both get copper sulfate; the warmed one is finished much sooner", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c6-06-s18",
        "band": "standard",
        "text": "The liquid collected below the funnel is a clear blue. Why is it "
                "blue?",
        "options": [
            {"text": "Because fine black copper oxide has coloured it as it went "
                      "through", "correct": False,
             "why": "Copper oxide is black and the solution is clear blue, so "
                    "nothing solid is colouring it."},
            {"text": "Because the copper sulfate made in the reaction is dissolved in"
                      " it", "correct": True},
            {"text": "Because the sulfuric acid left over is blue once it has been "
                      "warmed", "correct": False,
             "why": "Sulfuric acid is colourless, warmed or cold, and there should "
                    "be none left."},
            {"text": "Because the filter paper releases a blue dye into the liquid", "correct": False,
             "why": "Filter paper adds nothing. The colour arrived with the salt."},
        ],
        "figure": None,
    },
    {
        "id": "c6-06-s19",
        "band": "standard",
        "text": "After filtering, a few specks of black powder are visible in the "
                "blue filtrate. What should be done?",
        "options": [
            {"text": "Carry on, since a few specks will burn off during the "
                      "evaporation", "correct": False,
             "why": "Copper oxide does not burn off. It would stay and contaminate "
                    "the crystals."},
            {"text": "Add more acid, so that the specks are reacted away before "
                      "evaporating", "correct": False,
             "why": "That puts acid back into a solution you have just made acid-"
                    "free."},
            {"text": "Start the whole preparation again from the beginning", "correct": False,
             "why": "Nothing has been ruined. The mixture only needs separating "
                    "properly."},
            {"text": "Filter it again before going on", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c6-06-s20",
        "band": "standard",
        "text": "A student needs pure calcium nitrate crystals. Which acid and which "
                "base should they use?",
        "options": [
            {"text": "Sulfuric acid with calcium carbonate", "correct": False,
             "why": "That pair gives calcium sulfate, which barely dissolves and "
                    "stops the reaction almost at once."},
            {"text": "Hydrochloric acid with calcium carbonate", "correct": False,
             "why": "That pair gives calcium chloride. The acid decides the second "
                    "word of the name."},
            {"text": "Nitric acid with calcium carbonate", "correct": True},
            {"text": "Nitric acid with sodium hydroxide", "correct": False,
             "why": "That gives sodium nitrate, and the soluble base could not be "
                    "filtered off in any case."},
        ],
        "figure": None,
    },
    {
        "id": "c6-06-s21",
        "band": "standard",
        "text": "Why is the mixture stirred while the copper oxide is being added?",
        "options": [
            {"text": "So that the powder meets acid throughout instead of sitting in "
                      "a heap", "correct": True},
            {"text": "So that the mixture is kept warm without needing a flame under "
                      "it", "correct": False,
             "why": "Stirring does not heat anything noticeably. The flame does that"
                    " job."},
            {"text": "So that air is mixed in, which the reaction needs in order to "
                      "finish", "correct": False,
             "why": "No air is involved. The acid and the oxide are all the reaction"
                    " needs."},
            {"text": "So that the crystals start to form early and have longer to "
                      "grow", "correct": False,
             "why": "Crystals form much later, on cooling, and stirring then would "
                    "make them smaller."},
        ],
        "figure": None,
    },
    {
        "id": "c6-06-h09",
        "band": "harder",
        "text": "A student makes calcium sulfate from calcium carbonate and sulfuric "
                "acid and tries to filter the excess off. Explain why the filter "
                "paper is the wrong tool here.",
        "options": [
            {"text": "Because the product barely dissolves either, so it would be "
                      "caught on the paper with the excess", "correct": True},
            {"text": "Because the calcium sulfate dissolves so well that it goes "
                      "through the paper", "correct": False,
             "why": "It is the opposite: calcium sulfate hardly dissolves at all, "
                    "which is the root of the problem."},
            {"text": "Because the carbon dioxide given off would blow the paper out "
                      "of the funnel", "correct": False,
             "why": "The gas escapes from the beaker long before anything is "
                    "filtered."},
            {"text": "Because filtering only works on a solution that has already "
                      "been cooled", "correct": False,
             "why": "Warm mixtures are filtered routinely. The trouble here is what "
                    "the solid on the paper would be."},
        ],
        "figure": None,
    },
    {
        "id": "c6-06-h10",
        "band": "harder",
        "text": "A jar is labelled magnesium sulfate. Which starting materials could "
                "have made it?",
        "options": [
            {"text": "Sulfuric acid with magnesium, or with its oxide, hydroxide or "
                      "carbonate", "correct": True},
            {"text": "Only sulfuric acid with magnesium oxide, since that is the "
                      "method being taught here", "correct": False,
             "why": "The oxide is one route of several. The metal itself and the "
                    "carbonate both work as well."},
            {"text": "Magnesium with any acid at all, since the metal is what the "
                      "name records", "correct": False,
             "why": "The name records both. The sulfate half could only have come "
                    "from sulfuric acid."},
            {"text": "Any metal at all with sulfuric acid", "correct": False,
             "why": "The first word is magnesium, so the other reactant had to carry"
                    " magnesium in it."},
        ],
        "figure": None,
    },
    {
        "id": "c6-06-h11",
        "band": "harder",
        "text": "Warming the acid and adding the base in excess are two different "
                "kinds of decision. Explain the difference.",
        "options": [
            {"text": "Warming is about safety and excess is about how much salt is "
                      "produced in the end", "correct": False,
             "why": "Warming does not make the step safer, and excess base adds "
                    "nothing to the yield."},
            {"text": "Warming changes how long it takes; excess decides whether any "
                      "acid survives", "correct": True},
            {"text": "Warming decides the purity and excess decides the speed of the "
                      "whole preparation", "correct": False,
             "why": "This has the two the wrong way round in both halves."},
            {"text": "Both are about rate, since a warm mixture and an excess of "
                      "solid both speed it up", "correct": False,
             "why": "Excess is there so that the acid runs out completely. That is a"
                    " purity decision."},
        ],
        "figure": None,
    },
    {
        "id": "c6-06-h12",
        "band": "harder",
        "text": "Copper oxide is black and copper sulfate solution is blue. Explain "
                "how the colours let you follow the preparation.",
        "options": [
            {"text": "The blue fades as the reaction finishes, and black powder means"
                      " it has not started", "correct": False,
             "why": "The blue deepens rather than fading, and black powder settling "
                    "is the sign that it has finished."},
            {"text": "The black powder turns blue as it reacts, so a blue solid on "
                      "the bottom means it is over", "correct": False,
             "why": "The solid on the bottom stays black. What turns blue is the "
                    "liquid above it."},
            {"text": "The blue deepens as salt forms, and black powder settling shows"
                      " the acid has gone", "correct": True},
            {"text": "The colours cannot be used at all, because the mixture is too "
                      "dark to see through", "correct": False,
             "why": "The solution is a clear blue once the excess settles, and both "
                    "changes are easy to watch."},
        ],
        "figure": None,
    },
    {
        "id": "c6-06-h13",
        "band": "harder",
        "text": "A little unreacted base gets through the filter paper and is not "
                "noticed. Predict the effect on the finished crystals.",
        "options": [
            {"text": "They would be stained blue but chemically pure", "correct": False,
             "why": "The crystals are blue in any case, and the problem is what is "
                    "mixed in with them."},
            {"text": "They would react with the base and turn back into acid on the "
                      "bench", "correct": False,
             "why": "Nothing runs backwards. The base simply sits there among the "
                    "crystals."},
            {"text": "There would be no crystals at all, because the base stops them "
                      "forming", "correct": False,
             "why": "Crystals still grow from the solution. They would simply have "
                    "powder mixed through them."},
            {"text": "They would be contaminated with unreacted base", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c6-06-h14",
        "band": "harder",
        "text": "The process that makes the ammonia for ammonium fertilisers uses "
                "about one per cent of all the energy generated on Earth. What does "
                "that show?",
        "options": [
            {"text": "That making a salt is a wasteful process that ought to be "
                      "replaced", "correct": False,
             "why": "The energy buys the food supply of a large part of the world, "
                    "which is not waste."},
            {"text": "That salts are made on an enormous industrial scale, not just "
                      "in a beaker", "correct": True},
            {"text": "That neutralisation needs a great deal of energy before it will"
                      " run at all", "correct": False,
             "why": "Neutralisation gives energy out. The energy is spent making the"
                    " ammonia, not on the neutralising."},
            {"text": "That ammonium salts are far harder to make than any other salt", "correct": False,
             "why": "The neutralisation itself is straightforward. The difficulty is"
                    " obtaining the ammonia."},
        ],
        "figure": None,
    },
    {
        "id": "c6-06-h15",
        "band": "harder",
        "text": "A student proposes making sodium chloride by adding sodium hydroxide"
                " to the acid until no more will react. Explain why that instruction "
                "cannot be followed.",
        "options": [
            {"text": "Because sodium hydroxide will not react with hydrochloric acid "
                      "at all", "correct": False,
             "why": "The two react readily. The difficulty is knowing when to stop."},
            {"text": "Because the reaction is too slow to reach an end within a "
                      "lesson", "correct": False,
             "why": "It is immediate. Speed is not what makes the instruction "
                    "useless."},
            {"text": "Because sodium hydroxide dissolves, so nothing settles out to "
                      "show when enough has gone in", "correct": True},
            {"text": "Because sodium chloride cannot be made from an acid and a base "
                      "by any route", "correct": False,
             "why": "It can, and it is. The route simply needs a titration rather "
                    "than an excess."},
        ],
        "figure": None,
    },
    {
        "id": "c6-06-h16",
        "band": "harder",
        "text": "Explain why the filtrate is concentrated first rather than being "
                "left to cool as it is.",
        "options": [
            {"text": "Because a cold dilute solution would react backwards and give "
                      "the acid again", "correct": False,
             "why": "The reaction does not run backwards. The issue is how much "
                    "water is present."},
            {"text": "Because concentrating is what makes the crystals blue rather "
                      "than colourless", "correct": False,
             "why": "The colour belongs to the copper salt from the moment it forms."},
            {"text": "Because the dilute solution holds too much water to give "
                      "crystals as it cools", "correct": True},
            {"text": "Because the water has to be removed completely before any "
                      "crystals can appear", "correct": False,
             "why": "Removing all the water gives a caked powder. Some liquid has to"
                    " be left for crystals to grow in."},
        ],
        "figure": None,
    },
    {
        "id": "c6-06-e22",
        "band": "easier",
        "text": "The filtered solution is heated to drive some of the water off. Which"
                " piece of apparatus is it heated in?",
        "options": [
            {"text": "An evaporating basin", "correct": True},
            {"text": "A measuring cylinder", "correct": False,
             "why": "A measuring cylinder is for measuring a volume and is never "
                    "heated."},
            {"text": "A filter funnel", "correct": False,
             "why": "The funnel has already done its job of separating the "
                    "solid."},
            {"text": "A gas syringe", "correct": False,
             "why": "A syringe collects a gas, and no gas is being collected "
                    "here."},
        ],
        "figure": None,
    },
    {
        "id": "c6-06-e23",
        "band": "easier",
        "text": "What is the name for the solid left behind on the filter paper?",
        "options": [
            {"text": "The filtrate", "correct": False,
             "why": "The filtrate is the liquid that runs through, not the solid "
                    "held back."},
            {"text": "The residue", "correct": True},
            {"text": "The solution", "correct": False,
             "why": "A solution is a liquid with something dissolved in it."},
            {"text": "The solvent", "correct": False,
             "why": "The solvent is the liquid doing the dissolving, which passes "
                    "through."},
        ],
        "figure": None,
    },
    {
        "id": "c6-06-e24",
        "band": "easier",
        "text": "Which base would you add to sulfuric acid to make zinc sulfate?",
        "options": [
            {"text": "Sodium hydroxide", "correct": False,
             "why": "That would put sodium into the salt instead of zinc."},
            {"text": "Copper oxide", "correct": False,
             "why": "That would give copper sulfate, with the wrong metal in it."},
            {"text": "Zinc oxide", "correct": True},
            {"text": "Zinc chloride", "correct": False,
             "why": "Zinc chloride is already a salt rather than a base to "
                    "neutralise with."},
        ],
        "figure": None,
    },
    {
        "id": "c6-06-e25",
        "band": "easier",
        "text": "Which salt forms when copper carbonate meets nitric acid?",
        "options": [
            {"text": "Copper carbonate", "correct": False,
             "why": "That is the green solid added at the start rather than the "
                    "new substance."},
            {"text": "Copper sulfate", "correct": False,
             "why": "Sulfates come from sulfuric acid, and this preparation uses "
                    "nitric."},
            {"text": "Sodium nitrate", "correct": False,
             "why": "No sodium is present anywhere in this mixture."},
            {"text": "Copper nitrate", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c6-06-e26",
        "band": "easier",
        "text": "The solution is heated until it is saturated. What does saturated mean?",
        "options": [
            {"text": "It is holding as much dissolved salt as it can",
             "correct": True},
            {"text": "It has been heated until it boils", "correct": False,
             "why": "Boiling is about temperature; saturated is about how much is "
                    "dissolved."},
            {"text": "It has no salt dissolved in it at all", "correct": False,
             "why": "That is the opposite: a saturated solution is as full as it "
                    "can be."},
            {"text": "It has been filtered until it is completely clear", "correct": False,
             "why": "Filtering removes solid that never dissolved; it does not "
                    "change what is in solution."},
        ],
        "figure": None,
    },
    {
        "id": "c6-06-e27",
        "band": "easier",
        "text": "The blue solution is heated gently in a basin. What happens to the"
                " level of liquid in it?",
        "options": [
            {"text": "It rises as the salt comes out of solution", "correct": False,
             "why": "Salt coming out of solution adds no liquid to the basin."},
            {"text": "It falls as water evaporates away", "correct": True},
            {"text": "It stays exactly where it is until the salt appears",
             "correct": False,
             "why": "Water starts leaving as soon as the basin is warm."},
            {"text": "It falls as the salt evaporates away", "correct": False,
             "why": "The salt stays behind; it is the water that leaves as "
                    "vapour."},
        ],
        "figure": None,
    },
    {
        "id": "c6-06-e28",
        "band": "easier",
        "text": "Nitric acid is neutralised with ammonia. Which salt is produced?",
        "options": [
            {"text": "Ammonium sulfate", "correct": False,
             "why": "Sulfates come from sulfuric acid rather than from nitric."},
            {"text": "Ammonium chloride", "correct": False,
             "why": "Chlorides come from hydrochloric acid."},
            {"text": "Ammonium nitrate", "correct": True},
            {"text": "Nitrogen ammonate", "correct": False,
             "why": "There is no such compound, and salt names do not take that "
                    "shape."},
        ],
        "figure": None,
    },
    {
        "id": "c6-06-e29",
        "band": "easier",
        "text": "What is the name of the process in which a salt comes out of a"
                " solution as solid crystals?",
        "options": [
            {"text": "Filtration", "correct": False,
             "why": "Filtration separates a solid that never dissolved from a "
                    "liquid."},
            {"text": "Neutralisation", "correct": False,
             "why": "Neutralisation is the reaction that made the salt in the "
                    "first place."},
            {"text": "Crystallisation", "correct": True},
            {"text": "Condensation", "correct": False,
             "why": "Condensation is a gas turning back into a liquid, which is "
                    "not what happens in the basin."},
        ],
        "figure": None,
    },
    {
        "id": "c6-06-e30",
        "band": "easier",
        "text": "The salt made by this method is described as pure. What does pure mean"
                " here?",
        "options": [
            {"text": "That it has been made in a laboratory rather than bought",
             "correct": False,
             "why": "Where a substance was made says nothing about what is in "
                    "it."},
            {"text": "That it is safe to eat", "correct": False,
             "why": "Purity is not safety; copper sulfate is pure and must not be "
                    "swallowed."},
            {"text": "That it has been dried in an oven", "correct": False,
             "why": "Drying removes water, and purity is about everything else as "
                    "well."},
            {"text": "That nothing else is left in it but the salt",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c6-06-e31",
        "band": "easier",
        "text": "What is used to stir the mixture while the base is being added to the"
                " warm acid?",
        "options": [
            {"text": "A glass rod", "correct": True},
            {"text": "A thermometer", "correct": False,
             "why": "A thermometer is for reading a temperature and breaks easily "
                    "if used to stir."},
            {"text": "A spatula", "correct": False,
             "why": "A spatula carries the powder across; it is not left in the "
                    "beaker to stir with."},
            {"text": "A filter funnel", "correct": False,
             "why": "The funnel is used later, to separate the excess from the "
                    "liquid."},
        ],
        "figure": None,
    },
    {
        "id": "c6-06-e32",
        "band": "easier",
        "text": "For this preparation to work at all, what must be true of the salt"
                " being made?",
        "options": [
            {"text": "It must be coloured, so that it can be seen", "correct": False,
             "why": "Plenty of salts made this way are colourless and the method "
                    "still works."},
            {"text": "It must dissolve in water", "correct": True},
            {"text": "It must be heavier than the base it came from",
             "correct": False,
             "why": "Nothing in the method depends on comparing the two masses."},
            {"text": "It must give off a gas as it forms", "correct": False,
             "why": "An oxide base gives no gas at all, and the preparation runs "
                    "perfectly well."},
        ],
        "figure": None,
    },
    {
        "id": "c6-06-s22",
        "band": "standard",
        "text": "The basin is heated gently rather than on a roaring flame. Explain"
                " why.",
        "options": [
            {"text": "Because a hot flame would turn the salt back into acid",
             "correct": False,
             "why": "Heat does not undo the reaction that made the salt."},
            {"text": "Because hard boiling spits the hot solution out of the "
                      "basin", "correct": True},
            {"text": "Because the salt would dissolve again if it got too hot",
             "correct": False,
             "why": "The salt is dissolved already; the point of heating is to "
                    "remove water."},
            {"text": "Because a hot flame would stop the water evaporating at "
                      "all", "correct": False,
             "why": "More heat evaporates water faster, which is precisely the "
                    "difficulty."},
        ],
        "figure": None,
    },
    {
        "id": "c6-06-s23",
        "band": "standard",
        "text": "The acid is measured out carefully while the base is simply added"
                " until no more reacts. Explain why only one of them is measured.",
        "options": [
            {"text": "Because the base is too fine a powder to measure",
             "correct": False,
             "why": "A powder weighs out perfectly well; it is not measured "
                    "because it need not be."},
            {"text": "Because the base would be spoiled by being weighed out in "
                      "air", "correct": False,
             "why": "Nothing happens to an oxide sitting on a balance."},
            {"text": "Because the acid sets how much salt can be made",
             "correct": True},
            {"text": "Because the acid is the more expensive of the two",
             "correct": False,
             "why": "Cost is not what the measuring is for; the yield is."},
        ],
        "figure": None,
    },
    {
        "id": "c6-06-s24",
        "band": "standard",
        "text": "A few crystals stay stuck to the basin when the rest are collected."
                " Explain the effect on the mass the student reports.",
        "options": [
            {"text": "It is lower than the mass of salt made", "correct": True},
            {"text": "It is higher, because the basin is weighed with them",
             "correct": False,
             "why": "The crystals left behind are not collected, so they cannot "
                    "add to the mass reported."},
            {"text": "It is unchanged, because mass is always conserved",
             "correct": False,
             "why": "Mass is conserved in the reaction; it is the collecting that "
                    "loses some."},
            {"text": "It is lower, because some of the salt was destroyed",
             "correct": False,
             "why": "Nothing was destroyed; the missing salt is still in the "
                    "basin."},
        ],
        "figure": None,
    },
    {
        "id": "c6-06-s25",
        "band": "standard",
        "text": "The concentrated solution is left to cool and crystals appear "
                "in it. Explain why cooling brings them out.",
        "options": [
            {"text": "Because cooling drives the last of the water off", "correct": False,
             "why": "Evaporation is faster when warm, so cooling does the "
                    "opposite."},
            {"text": "Because cooling turns the water into crystals", "correct": False,
             "why": "The crystals are the salt; the water is still liquid "
                    "around them."},
            {"text": "Because the salt reacts with the water again as the "
                      "solution cools", "correct": False,
             "why": "No new reaction happens; the salt simply comes out of "
                    "solution."},
            {"text": "Because cool water holds less dissolved salt than warm "
                      "water", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c6-06-s26",
        "band": "standard",
        "text": "A student presses on the filter paper to push the last of the "
                "liquid through more quickly. Explain why that is a mistake.",
        "options": [
            {"text": "The liquid would be pushed back up into the funnel", "correct": False,
             "why": "Pressing does not send liquid upwards; the trouble is the "
                    "paper itself."},
            {"text": "The paper may tear and let the solid through", "correct": True},
            {"text": "The salt would be squeezed out of the solution", "correct": False,
             "why": "A dissolved salt cannot be squeezed out of its solution."},
            {"text": "The filtrate would become more concentrated than it "
                      "should", "correct": False,
             "why": "How hard the paper is pressed changes nothing about what "
                    "is dissolved."},
        ],
        "figure": None,
    },
    {
        "id": "c6-06-s27",
        "band": "standard",
        "text": "The same preparation is run with hydrochloric acid and copper oxide."
                " Name the salt, and state what changes about the method.",
        "options": [
            {"text": "Copper chloride, and nothing about the method changes",
             "correct": True},
            {"text": "Copper chloride, and the mixture now fizzes throughout",
             "correct": False,
             "why": "Fizzing comes from a carbonate; an oxide gives no gas with "
                    "any acid."},
            {"text": "Copper sulfate, and nothing about the method changes",
             "correct": False,
             "why": "The acid names the ending, so hydrochloric acid cannot give "
                    "a sulfate."},
            {"text": "Copper chloride, and the excess can no longer be filtered "
                      "off", "correct": False,
             "why": "Copper oxide stays insoluble whichever acid it is added to."},
        ],
        "figure": None,
    },
    {
        "id": "c6-06-s28",
        "band": "standard",
        "text": "Ammonium sulfate is made by neutralising ammonia with an acid. Which"
                " acid is it?",
        "options": [
            {"text": "Nitric acid", "correct": False,
             "why": "Nitric acid would give ammonium nitrate instead."},
            {"text": "Sulfuric acid", "correct": True},
            {"text": "Hydrochloric acid", "correct": False,
             "why": "Hydrochloric acid would give ammonium chloride."},
            {"text": "Ethanoic acid", "correct": False,
             "why": "Ethanoic acid is the acid in vinegar and would give an "
                    "ethanoate rather than a sulfate."},
        ],
        "figure": None,
    },
    {
        "id": "c6-06-s29",
        "band": "standard",
        "text": "A technician needs pure magnesium sulfate crystals. State the "
                "acid and the base, and say why that base suits the method.",
        "options": [
            {"text": "Nitric acid with magnesium carbonate, because it fizzes "
                      "visibly", "correct": False,
             "why": "Nitric acid gives a nitrate, so that is the wrong salt "
                    "altogether."},
            {"text": "Sulfuric acid with sodium hydroxide, because it "
                      "dissolves readily", "correct": False,
             "why": "That gives the wrong metal, and a base that dissolves "
                    "cannot be filtered off."},
            {"text": "Hydrochloric acid with magnesium oxide, because the "
                      "oxide is insoluble", "correct": False,
             "why": "The base is right but the acid would give a chloride "
                    "rather than a sulfate."},
            {"text": "Sulfuric acid with magnesium oxide, because the excess "
                      "can be filtered off", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c6-06-s30",
        "band": "standard",
        "text": "The mixture is poured through a filter rather than being left "
                "to settle and the liquid tipped carefully off. Explain the "
                "advantage.",
        "options": [
            {"text": "Filtering makes the solution more concentrated as it "
                      "goes through", "correct": False,
             "why": "Nothing about the solution changes as it passes the "
                    "paper."},
            {"text": "Filtering removes the acid that has not yet reacted", "correct": False,
             "why": "Dissolved acid runs straight through the paper with the "
                    "liquid."},
            {"text": "Filtering catches the finest powder as well as the lumps", "correct": True},
            {"text": "Filtering starts the crystals forming on the paper", "correct": False,
             "why": "Crystals form later, when the solution has been "
                    "concentrated and cooled."},
        ],
        "figure": None,
    },
    {
        "id": "c6-06-s31",
        "band": "standard",
        "text": "The filtrate is poured into a wide shallow basin for heating "
                "rather than left in the tall beaker. Suggest why.",
        "options": [
            {"text": "Because a beaker would react with the copper sulfate", "correct": False,
             "why": "Glass is untouched by the salt solution standing in it."},
            {"text": "Because a basin can be heated to a higher temperature "
                      "than glass", "correct": False,
             "why": "The temperature reached is not what the shape is chosen "
                    "for."},
            {"text": "Because crystals cannot form in a tall container", "correct": False,
             "why": "Crystals form wherever the solution is concentrated "
                    "enough and cools."},
            {"text": "Because a wide surface lets the water evaporate far "
                      "faster", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c6-06-s32",
        "band": "standard",
        "text": "A spatula of copper oxide is stirred into a beaker of warm water"
                " instead of warm acid. Predict what happens.",
        "options": [
            {"text": "It dissolves and gives a blue solution", "correct": False,
             "why": "Blue means the salt has been made, and no salt can be made "
                    "without the acid."},
            {"text": "It sits there undissolved", "correct": True},
            {"text": "It fizzes and gives off carbon dioxide", "correct": False,
             "why": "An oxide gives no gas, and there is no acid here to react "
                    "with in any case."},
            {"text": "It dissolves slowly and leaves a colourless solution",
             "correct": False,
             "why": "Copper oxide does not dissolve in water at all, slowly or "
                    "otherwise."},
        ],
        "figure": None,
    },
    {
        "id": "c6-06-h17",
        "band": "harder",
        "text": "A student repeats the preparation with twice the volume of the same"
                " acid, still adding base until no more reacts. Predict the mass of"
                " crystals.",
        "options": [
            {"text": "About twice as much as before", "correct": True},
            {"text": "The same as before, because the base was in excess both "
                      "times", "correct": False,
             "why": "The base being in excess means the acid decides, and there "
                    "is twice as much acid."},
            {"text": "About half as much, because the acid is spread more thinly",
             "correct": False,
             "why": "There is twice as much acid, not the same acid in more "
                    "water."},
            {"text": "The same as before, because a beaker can only hold so much "
                      "salt", "correct": False,
             "why": "Nothing about the beaker limits how much salt the reaction "
                    "makes."},
        ],
        "figure": None,
    },
    {
        "id": "c6-06-h18",
        "band": "harder",
        "text": "Copper sulfate can be made from copper oxide, copper "
                "hydroxide or copper carbonate with sulfuric acid. Explain why "
                "the crystals are identical in all three cases.",
        "options": [
            {"text": "Because all three of those bases are really one and the "
                      "same compound under different names", "correct": False,
             "why": "They are three different compounds, as their colours and "
                    "formulae show."},
            {"text": "Because the salt takes only the metal and the acid's "
                      "part, whichever base brought them", "correct": True},
            {"text": "Because the extra parts of each base stay in the "
                      "crystals as impurities", "correct": False,
             "why": "Those parts leave as water or as gas, which is why the "
                    "salt comes out pure."},
            {"text": "Because the acid is in excess and washes the differences "
                      "away", "correct": False,
             "why": "The base is the one added in excess here, and washing is "
                    "not what makes the salts match."},
        ],
        "figure": None,
    },
    {
        "id": "c6-06-h19",
        "band": "harder",
        "text": "Copper sulfate cannot be made by putting copper metal into "
                "sulfuric acid. Explain why the oxide is used instead.",
        "options": [
            {"text": "Because the metal would dissolve too fast to be "
                      "controlled", "correct": False,
             "why": "It does not dissolve in dilute acid at any speed."},
            {"text": "Because copper metal would give a different salt from "
                      "its oxide", "correct": False,
             "why": "Both routes would give copper sulfate, if the metal route "
                    "worked at all."},
            {"text": "Because copper metal is too expensive to use in a school "
                      "laboratory", "correct": False,
             "why": "Copper is cheap enough for a school; it is the chemistry "
                    "that rules it out."},
            {"text": "Because copper is below hydrogen and does not react with "
                      "the acid", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c6-06-h20",
        "band": "harder",
        "text": "Compare the excess-and-filter route with the titration route, and say"
                " what decides which one a chemist uses.",
        "options": [
            {"text": "Whether the base dissolves: an insoluble one can be "
                      "filtered off, a soluble one cannot", "correct": True},
            {"text": "Whether the acid is strong: a strong acid needs a titration "
                      "and a weak one does not", "correct": False,
             "why": "How fierce the acid is has nothing to do with how the excess "
                    "is removed."},
            {"text": "Whether the salt is coloured: a coloured salt can be "
                      "followed by eye and needs no filter", "correct": False,
             "why": "Colour helps you watch the preparation but does not decide "
                    "the method."},
            {"text": "Whether a gas is given off: a fizzing reaction has to be "
                      "done by titration", "correct": False,
             "why": "A carbonate fizzes and is still filtered off in the ordinary "
                    "way."},
        ],
        "figure": None,
    },
    {
        "id": "c6-06-h21",
        "band": "harder",
        "text": "A technician needs pure potassium nitrate crystals. Name an "
                "acid and a base that would make it, and say which route is "
                "needed.",
        "options": [
            {"text": "Nitric acid with potassium hydroxide, by excess and "
                      "filtering", "correct": False,
             "why": "Potassium hydroxide dissolves, so an excess of it could "
                    "never be caught on the paper."},
            {"text": "Nitric acid with potassium hydroxide, by titration", "correct": True},
            {"text": "Sulfuric acid with potassium hydroxide, by titration", "correct": False,
             "why": "Sulfuric acid gives a sulfate, so the salt would be the "
                    "wrong one."},
            {"text": "Nitric acid with potassium carbonate, by excess and "
                      "filtering", "correct": False,
             "why": "Potassium carbonate dissolves too, so again nothing "
                    "settles out to be filtered."},
        ],
        "figure": None,
    },
    {
        "id": "c6-06-h22",
        "band": "harder",
        "text": "A technician needs ten times as much copper sulfate as the "
                "school preparation makes. Describe how the method would "
                "change.",
        "options": [
            {"text": "A different method entirely, because this one cannot be "
                      "scaled", "correct": False,
             "why": "Nothing in these steps stops them being done with larger "
                    "quantities."},
            {"text": "The same apparatus, run ten times faster by heating "
                      "strongly", "correct": False,
             "why": "Heating harder makes powder rather than crystals and does "
                    "not increase how much salt there is."},
            {"text": "The same acid, with ten times the base added to it", "correct": False,
             "why": "Extra base makes no extra salt, because the acid sets the "
                    "yield."},
            {"text": "The same steps, with ten times the acid and larger "
                      "apparatus", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c6-06-h23",
        "band": "harder",
        "text": "A student follows every step correctly and still collects far "
                "fewer crystals than expected. Suggest where the missing salt "
                "has gone.",
        "options": [
            {"text": "It was destroyed by the heat of the evaporating basin", "correct": False,
             "why": "The salt is not destroyed by gentle heating; it is left "
                    "behind as the water goes."},
            {"text": "It is still dissolved in the liquid poured off the "
                      "crystals", "correct": True},
            {"text": "It escaped as a gas while the solution was heated", "correct": False,
             "why": "Only water leaves as vapour; a dissolved salt cannot "
                    "follow it."},
            {"text": "It was caught on the filter paper with the excess base", "correct": False,
             "why": "The salt is dissolved at that stage, so it passes "
                    "straight through the paper."},
        ],
        "figure": None,
    },
    {
        "id": "c6-06-h24",
        "band": "harder",
        "text": "Explain why slow cooling gives a few large crystals while fast cooling"
                " gives a great many small ones.",
        "options": [
            {"text": "Fast cooling makes the crystals softer, so they break into "
                      "pieces", "correct": False,
             "why": "Nothing breaks; the difference is in how many crystals start "
                    "growing."},
            {"text": "Slow cooling lets the salt build onto a few crystals that "
                      "started first", "correct": True},
            {"text": "Slow cooling lets more water evaporate, so there is more "
                      "salt to build with", "correct": False,
             "why": "The same salt is in the basin either way; it is how it is "
                    "shared out that differs."},
            {"text": "Fast cooling leaves some of the salt dissolved, so the "
                      "crystals are smaller", "correct": False,
             "why": "Cooling further brings more salt out, not less."},
        ],
        "figure": None,
    },
    {
        "id": "c6-06-h25",
        "band": "harder",
        "text": "The concentrated solution is left uncovered on a shelf for a month"
                " instead of a few days. Predict what is found.",
        "options": [
            {"text": "Nothing, because the crystals redissolve if they are left "
                      "too long", "correct": False,
             "why": "Crystals do not redissolve into a liquid that is itself "
                    "drying up."},
            {"text": "A single enormous crystal filling the whole basin",
             "correct": False,
             "why": "Once the liquid is gone the last of the salt comes out as "
                    "fine crystals, not one giant."},
            {"text": "A dry crust of crystals with no liquid left", "correct": True},
            {"text": "A blue liquid unchanged, because evaporation stops at room "
                      "temperature", "correct": False,
             "why": "Water evaporates at room temperature, which is why an open "
                    "basin dries out."},
        ],
        "figure": None,
    },
    {
        "id": "c6-06-h26",
        "band": "harder",
        "text": "State what is on the filter paper and what is in the liquid "
                "below it, and which of the two the preparation is after.",
        "options": [
            {"text": "Crystals on the paper, water below, and both are wanted", "correct": False,
             "why": "No crystals have formed yet when the mixture is filtered."},
            {"text": "Salt on the paper, excess acid below, and the paper is "
                      "wanted", "correct": False,
             "why": "The salt is dissolved at this stage and runs through; no "
                    "acid should be left."},
            {"text": "Excess base on the paper, salt solution below, and the "
                      "paper is wanted", "correct": False,
             "why": "The solid caught on the paper is the leftover that is "
                    "thrown away."},
            {"text": "Excess base on the paper, salt solution below, and the "
                      "solution is wanted", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c6-06-h27",
        "band": "harder",
        "text": "Explain why this preparation is described as making a PURE "
                "salt rather than simply making a salt.",
        "options": [
            {"text": "Because a salt made from an acid is pure by definition", "correct": False,
             "why": "A salt made carelessly carries leftover acid or base with "
                    "it."},
            {"text": "Because the reaction between an acid and a base can only "
                      "ever make one substance in the beaker", "correct": False,
             "why": "It makes water as well, and starts from a mixture that "
                    "has to be sorted out."},
            {"text": "Because each step after the reaction is there to remove "
                      "something that is not the salt", "correct": True},
            {"text": "Because the crystals are weighed at the end to check "
                      "them", "correct": False,
             "why": "Weighing reports a mass and says nothing about what else "
                    "is mixed in."},
        ],
        "figure": None,
    },
    {
        "id": "c6-06-h28",
        "band": "harder",
        "text": "Explain why the blue crystals are a compound rather than a "
                "mixture of the acid and the base that made them.",
        "options": [
            {"text": "Because the acid and the base are both liquids and the "
                      "crystals are solid", "correct": False,
             "why": "The base was a solid, and changing state would not make a "
                    "new substance in any case."},
            {"text": "Because the atoms have been rearranged into a new "
                      "substance with its own properties", "correct": True},
            {"text": "Because a mixture would have to take the same colour as "
                      "both of the starting materials", "correct": False,
             "why": "Mixtures take colours from what is in them, so colour "
                    "alone settles nothing."},
            {"text": "Because the crystals can be separated back into acid and "
                      "base by filtering", "correct": False,
             "why": "They cannot be separated that way, which is part of what "
                    "makes them a compound."},
        ],
        "figure": None,
    },
    {
        "id": "c6-06-h29",
        "band": "harder",
        "text": "Finished copper sulfate crystals are dissolved in water and the"
                " solution is evaporated again. Evaluate the claim that this makes new"
                " salt.",
        "options": [
            {"text": "Sound, because crystals that form are always newly made",
             "correct": False,
             "why": "Forming crystals again is a physical change, not a new "
                    "reaction."},
            {"text": "Sound, because the water reacts with the salt as it "
                      "dissolves", "correct": False,
             "why": "Dissolving separates the salt's particles; it does not react "
                    "with them."},
            {"text": "Unsound, because the same salt is simply recovered",
             "correct": True},
            {"text": "Unsound, because the salt cannot be dissolved a second "
                      "time", "correct": False,
             "why": "It dissolves as readily as it did the first time, which is "
                    "why the claim can be tested at all."},
        ],
        "figure": None,
    },
    {
        "id": "c6-06-h30",
        "band": "harder",
        "text": "A student proposes adding a few drops of indicator so that the end of"
                " the reaction can be seen. Evaluate.",
        "options": [
            {"text": "Sound, because an indicator is the only way to know the "
                      "acid has gone", "correct": False,
             "why": "Undissolved powder settling out already reports it, without "
                    "adding anything."},
            {"text": "Sound, because the dye is removed with the excess base at "
                      "the filter", "correct": False,
             "why": "The dye dissolves, so it passes through the paper with the "
                    "salt solution."},
            {"text": "Unsound, because the dye would be left in the finished "
                      "crystals", "correct": True},
            {"text": "Unsound, because indicator does not respond to a solution "
                      "of a salt", "correct": False,
             "why": "It responds perfectly well; the objection is where the dye "
                    "ends up."},
        ],
        "figure": None,
    },
    {
        "id": "c6-06-h31",
        "band": "harder",
        "text": "Zinc sulfate made from zinc metal and zinc sulfate made from "
                "zinc oxide are indistinguishable. Explain why.",
        "options": [
            {"text": "Because the salt keeps a trace of whichever route made "
                      "it", "correct": False,
             "why": "A pure compound carries no record of how it was made."},
            {"text": "Because the two routes give off the very same gas as "
                      "well as producing the same salt", "correct": False,
             "why": "Only the metal route gives a gas, and the salts still "
                    "match."},
            {"text": "Because zinc oxide turns into zinc metal before it "
                      "reacts", "correct": False,
             "why": "The oxide reacts with the acid directly; it is not "
                    "converted first."},
            {"text": "Because the metal and the acid's part are the same in "
                      "both, whatever else left", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c6-06-h32",
        "band": "harder",
        "text": "Two students start from the same volume of the same sulfuric "
                "acid. One uses excess copper oxide and the other excess "
                "copper carbonate. Compare the masses of crystals they "
                "collect.",
        "options": [
            {"text": "The oxide gives more, because none of its mass is lost "
                      "as gas", "correct": False,
             "why": "The gas comes out of the carbonate rather than out of the "
                    "salt, so the yields still match."},
            {"text": "The carbonate gives more, because it supplies carbon as "
                      "well", "correct": False,
             "why": "The carbon leaves as gas and reaches the crystals not at "
                    "all."},
            {"text": "About the same, because the acid sets how much salt "
                      "there can be", "correct": True},
            {"text": "The carbonate gives less, because the fizzing carries "
                      "salt away", "correct": False,
             "why": "Bubbles carry no dissolved salt out of the beaker."},
        ],
        "figure": None,
    },
]
