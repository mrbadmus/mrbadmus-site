"""C2 lesson 02 — Elements: twelve questions (MRB-269).

These probe the single argument the lesson is built on — an element is a
substance made of one kind of atom, and the only evidence that settles it is
whether anything simpler can be got out of it. Every other result the bench
sells is interesting and worthless. The distractors come from the lesson's
three declared misconceptions: ATOM-03 (brass is a metal, metals are elements,
so brass is an element), ATOM-04 (anything pure is an element) and ATOM-05
(reacting violently means being broken down). Three more are taken from the
bench itself — that the most convincing-looking sample is the mixture, that
conducting is shared by copper, brass and salt water alike, and that a definite
melting point belongs to compounds as readily as to elements. The `harder` band
takes the rule to two substances the lesson never puts on the bench (solder and
an 18 carat ring), sets air and water against each other so that separating and
being a mixture come apart, and turns the hook's own discarded fourth option
back on all six samples.
"""

UNIT = "C2"
LESSON = "elements"
LESSON_NUMBER = 2

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "c2-02-e01",
        "band": "easier",
        "text": "There are four tests you can spend on an unknown sample: "
                "look at it closely, test whether it conducts, look for it on "
                "the periodic table, or try to break it down. Which one finds "
                "out for yourself whether it is an element, rather than "
                "looking the answer up?",
        "options": [
            {"text": "Look at it closely, because an element has a look of "
                     "its own that a mixture cannot copy.",
             "correct": False,
             "why": "Appearance settles nothing. Brass is the most "
                    "convincing-looking sample on the bench and is not an "
                    "element; sulfur is a dull yellow powder and is."},
            {"text": "Try to break it down, because an element is a substance "
                     "nothing simpler can be got out of.",
             "correct": True},
            {"text": "Look for it on the periodic table, because that is the "
                     "list of all the elements there are.",
             "correct": False,
             "why": "The table does give you the answer, but you are reading "
                    "somebody else's result. Breaking the substance down is "
                    "how the entry got onto the table in the first place."},
            {"text": "Test whether it conducts, because conducting is what "
                     "separates the elements from everything else.",
             "correct": False,
             "why": "Copper conducts and is an element; brass conducts and is "
                    "not; salt water conducts and is neither. Conducting "
                    "sorts nothing on this bench."},
        ],
        "figure": None,
    },
    {
        "id": "c2-02-e02",
        "band": "easier",
        "text": "Every rock, gas, liquid, plastic, medicine and living thing "
                "is built from the same short list of kinds of atom. Roughly "
                "how many entries are on that list?",
        "options": [
            {"text": "About a hundred.",
             "correct": True},
            {"text": "About sixty.",
             "correct": False,
             "why": "That is roughly how many are in the phone in your "
                    "pocket — about two thirds of the list, not all of it."},
            {"text": "About a thousand.",
             "correct": False,
             "why": "There are millions of different substances, but all of "
                    "them are built from ninety-odd kinds of atom. The list "
                    "is far shorter than the number of things made from it."},
            {"text": "About twenty.",
             "correct": False,
             "why": "Fewer than thirty of them are needed by living things, "
                    "which may be where that number comes from. The whole "
                    "list is longer than the part life uses."},
        ],
        "figure": None,
    },
    {
        "id": "c2-02-e03",
        "band": "easier",
        "text": "A student looks at sample 3 — a bright yellow powder that "
                "does not conduct electricity at all — and says it cannot "
                "possibly be an element. What is wrong with that reasoning?",
        "options": [
            {"text": "Nothing is wrong with it. A substance that does not "
                     "conduct electricity cannot be an element.",
             "correct": False,
             "why": "Sulfur does not conduct and is an element; sugar does "
                    "not conduct and is not one. Conducting tells you nothing "
                    "either way."},
            {"text": "The powder would conduct perfectly well if it were "
                     "pressed into a single solid lump first.",
             "correct": False,
             "why": "Sulfur does not conduct however you shape it, and that "
                    "is not what would make it an element anyway. Only what "
                    "comes out of it settles that."},
            {"text": "Nothing on the list has to be a metal. Sulfur "
                     "conducts nothing at all, and it is an element.",
             "correct": True},
            {"text": "The colour is the real problem here — elements can be "
                     "any colour, but a powder is never one of them.",
             "correct": False,
             "why": "Being a powder is no bar to anything. What settles "
                    "sulfur is that nothing simpler comes out of it by "
                    "heating, dissolving or electrolysis."},
        ],
        "figure": None,
    },
    {
        "id": "c2-02-e04",
        "band": "easier",
        "text": "Sample 4 is hard, shiny, gold-coloured and rings when you "
                "tap it. You spend one of your eight tests looking for it on "
                "the periodic table. What do you find?",
        "options": [
            {"text": "An entry for brass, sitting on the table between copper "
                     "and zinc.",
             "correct": False,
             "why": "There is no such thing as a brass atom, so there is no "
                    "entry for brass. It is copper and zinc mixed while both "
                    "of them were molten."},
            {"text": "An entry for brass, because every metal on this bench "
                     "has one somewhere.",
             "correct": False,
             "why": "Metal describes how a substance behaves; element "
                    "describes what it is made of. Steel, bronze and solder "
                    "are metals with no entry either."},
            {"text": "No entry at all, because the periodic table only lists "
                     "the substances that are not metals.",
             "correct": False,
             "why": "Most of the table is metals — copper, zinc and sodium "
                    "all have entries. Brass is missing for a quite different "
                    "reason."},
            {"text": "No entry called brass — but there is an entry for "
                     "copper and an entry for zinc.",
             "correct": True},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "c2-02-s01",
        "band": "standard",
        "text": "You pass electricity through sample 2, a colourless liquid, "
                "and two different gases come off in a fixed ratio of two to "
                "one by volume. What has that result told you?",
        "options": [
            {"text": "The electricity has split some of its atoms into "
                     "smaller pieces than atoms.",
             "correct": False,
             "why": "Chemistry does not break atoms apart. Both kinds of atom "
                    "were in the liquid already; the electricity only "
                    "separated what was there."},
            {"text": "It was made of more than one kind of atom all along, so "
                     "it is not an element.",
             "correct": True},
            {"text": "It is a mixture, because two different things came out "
                     "of it when it was tested.",
             "correct": False,
             "why": "Something simpler came out either way, so it is not an "
                    "element. But the ratio is fixed at two to one every "
                    "time — air and brass can be mixed in any proportion you "
                    "like, and this cannot."},
            {"text": "Nothing yet. The gases were made by the electricity "
                     "rather than got out of the liquid.",
             "correct": False,
             "why": "Nothing new was made. Everything that came off had to be "
                    "in the liquid to begin with, which is exactly why it "
                    "cannot be one kind of atom."},
        ],
        "figure": None,
    },
    {
        "id": "c2-02-s02",
        "band": "standard",
        "text": "Pure water and pure copper are both pure — one substance, "
                "nothing dissolved in either of them. Only one of the two is "
                "an element. Which, and why?",
        "options": [
            {"text": "Both of them are. A pure substance is an element, "
                     "because that is what pure means.",
             "correct": False,
             "why": "Pure means nothing unwanted has been mixed in. It says "
                    "nothing about how many kinds of atom are there, and pure "
                    "water has two."},
            {"text": "Copper is, because copper is a metal and water is not a "
                     "metal at all.",
             "correct": False,
             "why": "Sulfur is not a metal and is still an element. Being a "
                    "metal is not what puts a substance on the list."},
            {"text": "Neither is, because a water sample would have to be "
                     "made purer still before you could say.",
             "correct": False,
             "why": "The water was already pure and it is still not an "
                    "element. Purity was never the test — what comes out of "
                    "it is."},
            {"text": "Copper is — it is copper atoms and nothing else, while "
                     "water has two kinds of atom.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c2-02-s03",
        "band": "standard",
        "text": "Sodium is kept under oil, and dropped into water it fizzes "
                "across the surface and catches fire. A student says that "
                "proves the sodium is coming apart, so it is not an element. "
                "Where does that go wrong?",
        "options": [
            {"text": "The reaction builds something more complicated out of "
                     "the sodium; it does not take it apart.",
             "correct": True},
            {"text": "It does not go wrong anywhere — a substance that reacts "
                     "that violently must be breaking down.",
             "correct": False,
             "why": "Reacting violently is not the same as being broken down. "
                    "A reaction that makes a new, more complicated substance "
                    "is going the opposite way."},
            {"text": "The conclusion is wrong because sodium is a metal, and "
                     "every metal is an element.",
             "correct": False,
             "why": "The conclusion is right but this is not the reason. "
                    "Brass is a metal and is not an element, so the next "
                    "sample would catch you out."},
            {"text": "The oil is the problem — the sodium is reacting with "
                     "the oil rather than with the water.",
             "correct": False,
             "why": "The oil is only there to keep air off it in storage. The "
                    "reaction with water is real; what matters is that it "
                    "makes something, rather than releasing something "
                    "simpler."},
        ],
        "figure": None,
    },
    {
        "id": "c2-02-s04",
        "band": "standard",
        "text": "You have eight tests to spend on six samples. A classmate "
                "opens by spending four of them looking closely at four "
                "different samples. Say what is wrong with that spend.",
        "options": [
            {"text": "It is a sensible opening, because a mixture always "
                     "looks less even than an element does.",
             "correct": False,
             "why": "Brass looks perfectly even, and it is copper and zinc "
                    "mixed while both were molten. A mixture does not have to "
                    "look mixed."},
            {"text": "There is nothing wrong with it, because looking is the "
                     "cheapest of the four tests on offer.",
             "correct": False,
             "why": "All four cost the same one test out of the eight. A "
                    "result that settles nothing is not a bargain at any "
                    "price."},
            {"text": "Looking separates nothing here. Brass looked the most "
                     "convincing and is not an element.",
             "correct": True},
            {"text": "The mistake is testing only four of the six samples "
                     "instead of covering every one of them.",
             "correct": False,
             "why": "The problem is which test, not how many samples. Looking "
                    "would have told them nothing on all six of them."},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "c2-02-h01",
        "band": "harder",
        "text": "Solder is a shiny silvery metal that melts at a low "
                "temperature and is used to join wires. Different tins of it "
                "hold different proportions of tin and lead. Is solder an "
                "element?",
        "options": [
            {"text": "Yes — it melts at one definite temperature, and that is "
                     "what elements do.",
             "correct": False,
             "why": "Water melts at exactly 0 °C and is not an element. A "
                    "definite melting point is a property of the substance, "
                    "not evidence about the atoms in it."},
            {"text": "Yes — it is shiny and it conducts, so it is a metal, "
                     "and metals are elements.",
             "correct": False,
             "why": "Metal describes how something behaves; element describes "
                    "what it is made of. Brass and bronze are metals and "
                    "neither one is an element."},
            {"text": "No — the proportions can be varied, so more than one "
                     "kind of atom is in it.",
             "correct": True},
            {"text": "It cannot be decided, because solder has no entry "
                     "anywhere on the periodic table.",
             "correct": False,
             "why": "Having no entry is the answer, not a reason you cannot "
                    "answer. There is tin and there is lead; there is no "
                    "solder atom."},
        ],
        "figure": None,
    },
    {
        "id": "c2-02-h02",
        "band": "harder",
        "text": "Cooled until it liquefies and then warmed slowly, air "
                "separates into nitrogen, oxygen and argon, and the "
                "proportions differ from place to place. Electrolysed, water "
                "separates into two gases in a fixed two-to-one ratio every "
                "time. What do the two results have in common?",
        "options": [
            {"text": "Something simpler came out of each, so neither can be "
                     "made of only one kind of atom.",
             "correct": True},
            {"text": "Both substances were taken apart by heating, which is "
                     "the standard test for an element.",
             "correct": False,
             "why": "Air had to be cooled to a liquid first, and water needed "
                    "electricity. Heating on its own would have separated "
                    "neither of them."},
            {"text": "Both are mixtures, because in each case more than one "
                     "gas came out at the end.",
             "correct": False,
             "why": "Air's proportions vary, so air is a mixture. Water's "
                    "ratio is fixed at two to one every time, and it is a "
                    "compound. Separating tells you it is not an element, not "
                    "which of the two it is."},
            {"text": "Neither result settles anything either way, because a "
                     "gas can never be an element.",
             "correct": False,
             "why": "Nitrogen, oxygen and argon are all gases and all "
                    "elements. What state a substance is in has nothing to do "
                    "with it."},
        ],
        "figure": None,
    },
    {
        "id": "c2-02-h03",
        "band": "harder",
        "text": "A ring is stamped 18 carat: it is 75% gold, and the rest is "
                "copper and silver. The shop calls it solid gold. A student "
                "says the ring must be an element, because gold has an entry "
                "on the periodic table. What would you say?",
        "options": [
            {"text": "They are right, and the entry for gold on the table is "
                     "what settles it.",
             "correct": False,
             "why": "The entry is for gold, not for whatever gold has been "
                    "mixed with. Copper has an entry too, and brass has "
                    "none."},
            {"text": "They are right, because solid gold means gold and "
                     "nothing else has been used.",
             "correct": False,
             "why": "Solid gold means the gold goes all the way through "
                    "rather than being a coating on top. It has never meant "
                    "one kind of atom."},
            {"text": "It cannot be decided at all until somebody tries to "
                     "break the ring down into something simpler.",
             "correct": False,
             "why": "You already know what is in it: three metals, in a "
                    "proportion that can be varied. That is more than one "
                    "kind of atom, which settles it."},
            {"text": "The ring is three kinds of atom mixed in a proportion "
                     "that can be changed, so it is not one.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c2-02-h04",
        "band": "harder",
        "text": "One of the choices in the hook was to weigh the sample and "
                "measure its melting point. Suppose that had been offered as "
                "a fifth test on the bench. How would it have done across the "
                "six samples?",
        "options": [
            {"text": "It would have settled the solids for you, though it "
                     "could do nothing with the gas.",
             "correct": False,
             "why": "It would have failed on the solids too. Brass has a mass "
                    "and a melting point, and brass is copper and zinc."},
            {"text": "It would have failed on all six — every substance has a "
                     "mass and a melting point.",
             "correct": True},
            {"text": "It would have settled the water at least, because water "
                     "melts at exactly 0 °C.",
             "correct": False,
             "why": "That is a famously definite value and water is still not "
                    "an element. Compounds have definite melting points as "
                    "readily as elements do."},
            {"text": "It would have worked on all six, but it is far too slow "
                     "to run eight times over.",
             "correct": False,
             "why": "Time is not the problem here. However carefully you "
                    "measured, the number would not tell you what kinds of "
                    "atom are in the sample."},
        ],
        "figure": None,
    },
]
