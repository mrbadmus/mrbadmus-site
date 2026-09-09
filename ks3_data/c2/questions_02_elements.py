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

    # ── easier · MRB-335 top-up ─────────────────────────────────────────
    {
        "id": "c2-02-e05",
        "band": "easier",
        "text": "What is a mixture?",
        "options": [
            {"text": "Two or more elements that have been joined together in "
                     "one fixed proportion by a reaction",
             "correct": False,
             "why": "That is a compound. The giveaway is the fixed "
                    "proportion — a mixture can be any proportion you like"},
            {"text": "Two or more substances in the same place, not "
                     "chemically joined",
             "correct": True},
            {"text": "A substance made of one kind of atom that has been "
                     "ground up finely",
             "correct": False,
             "why": "Grinding an element leaves you with the element. A "
                    "mixture needs more than one substance in it"},
            {"text": "Anything that is not pure enough to have its own entry "
                     "on the periodic table",
             "correct": False,
             "why": "Compounds have no entry either, and they are not "
                    "mixtures. The test is whether anything is joined"},
        ],
        "figure": None,
    },
    {
        "id": "c2-02-e06",
        "band": "easier",
        "text": "What does the word metal describe?",
        "options": [
            {"text": "A substance that appears on the periodic table and "
                     "cannot be broken down",
             "correct": False,
             "why": "That describes an element. Brass behaves as a metal and "
                    "has no entry at all"},
            {"text": "A substance made of only one kind of atom",
             "correct": False,
             "why": "That is an element. Metal is how a substance behaves; "
                    "element is what it is made of"},
            {"text": "A substance that is shiny when freshly cut, conducts "
                     "electricity, and can be bent or hammered",
             "correct": True},
            {"text": "Any substance that has been dug out of the ground",
             "correct": False,
             "why": "Coal and chalk are dug up and neither is a metal. Where "
                    "it came from is not the test"},
        ],
        "figure": None,
    },
    {
        "id": "c2-02-e07",
        "band": "easier",
        "text": "Brass is checked against the periodic table and no entry is "
                "found. What does that tell you?",
        "options": [
            {"text": "That brass is too rare a substance for the table to "
                     "have got round to listing it yet",
             "correct": False,
             "why": "Brass is everywhere. The table lists elements, and brass "
                    "is not one"},
            {"text": "That brass has not yet been broken down, so nobody "
                     "knows what is in it",
             "correct": False,
             "why": "Everyone knows what is in it — copper and zinc. That is "
                    "exactly why it has no entry"},
            {"text": "That brass is a compound rather than a mixture",
             "correct": False,
             "why": "Compounds have no entry either, so a missing entry "
                    "cannot tell the two apart. Brass is in fact a mixture"},
            {"text": "That brass is not an element",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c2-02-e08",
        "band": "easier",
        "text": "The key note says one thing proves nothing about whether a "
                "substance is an element. What is it?",
        "options": [
            {"text": "What it looks like",
             "correct": True},
            {"text": "Whether anything simpler can be got out of it by "
                     "heating, electrolysis or acid",
             "correct": False,
             "why": "That is the one test that settles it, so it proves a "
                    "great deal rather than nothing"},
            {"text": "Whether it has its own entry on the periodic table",
             "correct": False,
             "why": "The table gives the answer straight away. It is looking "
                    "it up rather than finding it out, but it is not "
                    "useless"},
            {"text": "What its atoms are",
             "correct": False,
             "why": "One kind of atom is the whole definition of an element. "
                    "Nothing settles it more completely"},
        ],
        "figure": None,
    },
    {
        "id": "c2-02-e09",
        "band": "easier",
        "text": "Ninety-nine per cent of your body is made of just six "
                "elements. Which two of them are almost all present as "
                "water?",
        "options": [
            {"text": "Carbon and hydrogen, the two elements that every food "
                     "you eat is largely built out of",
             "correct": False,
             "why": "Carbon is in the six and is not in water at all. Water "
                    "is hydrogen and oxygen"},
            {"text": "Oxygen and hydrogen",
             "correct": True},
            {"text": "Calcium and phosphorus",
             "correct": False,
             "why": "Both are in the six and both are locked mostly in your "
                    "bones. Neither is part of water"},
            {"text": "Oxygen and carbon",
             "correct": False,
             "why": "Both are in the six, and together they make up most of "
                    "your mass — but carbon is not in water"},
        ],
        "figure": None,
    },

    # ── standard · MRB-335 top-up ───────────────────────────────────────
    {
        "id": "c2-02-s05",
        "band": "standard",
        "text": "You have eight tests for six samples. Which spend is the "
                "best use of them?",
        "options": [
            {"text": "Look closely at all six, then use the last two tests on "
                     "the ones still unclear",
             "correct": False,
             "why": "Looking settles nothing on any of the six. Six of the "
                    "eight tests would have bought you no information"},
            {"text": "Try to break down each of the six, and use the two "
                     "spare tests wherever the result is unclear",
             "correct": True},
            {"text": "Test all six for conducting electricity, then look up "
                     "the two that conduct",
             "correct": False,
             "why": "Conducting is shared by copper, brass, steel and salt "
                    "water, so it separates nothing. Two of those are not "
                    "elements"},
            {"text": "Look up all six on the periodic table and spend the "
                     "other two tests looking at them",
             "correct": False,
             "why": "Looking up works, but it answers by lookup rather than "
                    "by evidence — and the two spare tests are then wasted "
                    "on looking"},
        ],
        "figure": None,
    },
    {
        "id": "c2-02-s06",
        "band": "standard",
        "text": "Pure water barely conducts electricity, but tap water does. "
                "What does that difference tell you?",
        "options": [
            {"text": "That water is an element when pure and a mixture when "
                     "it comes out of a tap somewhere in a building",
             "correct": False,
             "why": "Water is a compound in both cases. What changes is what "
                    "else is in the jug with it"},
            {"text": "That conducting electricity is a good test for being an "
                     "element",
             "correct": False,
             "why": "It is a poor test. It fails on copper and brass alike, "
                    "and here it fails on two samples of the same compound"},
            {"text": "That tap water has substances dissolved in it, so it is "
                     "a mixture",
             "correct": True},
            {"text": "That pure water contains no ions and therefore no atoms "
                     "at all",
             "correct": False,
             "why": "Pure water is made of atoms like everything else. What "
                    "it lacks is dissolved substances"},
        ],
        "figure": None,
    },
    {
        "id": "c2-02-s07",
        "band": "standard",
        "text": "A silvery solid is heated strongly, treated with acid and "
                "electrolysed, and nothing simpler ever comes out of it. What "
                "can you now say?",
        "options": [
            {"text": "That it is a metal, since only metals survive all three "
                     "of those treatments without being changed",
             "correct": False,
             "why": "Sulfur survives plenty and is not a metal, and many "
                    "metals react readily with acid. The result is not about "
                    "being a metal"},
            {"text": "That it is definitely an element, and no future method "
                     "could ever change that",
             "correct": False,
             "why": "Soda was called an element until electricity took it "
                    "apart. A verdict is as good as the methods behind it"},
            {"text": "That it is a compound whose parts are held together "
                     "unusually strongly",
             "correct": False,
             "why": "Nothing here points that way. The evidence is that "
                    "nothing simpler came out"},
            {"text": "That it is an element, as far as those methods can "
                     "show",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c2-02-s08",
        "band": "standard",
        "text": "Brass is 70% copper in one sample and 60% in another, and "
                "both are sold as brass. Which conclusion follows?",
        "options": [
            {"text": "That brass is a mixture, because its proportions can be "
                     "varied",
             "correct": True},
            {"text": "That one of the two samples has been made badly and is "
                     "not really brass at all, whatever the label says",
             "correct": False,
             "why": "Both are brass. Being able to choose the recipe is the "
                    "point, not a fault in the manufacture"},
            {"text": "That brass is a compound with two different formulae",
             "correct": False,
             "why": "A compound has one fixed proportion and one formula. Two "
                    "recipes rules a compound out"},
            {"text": "That brass is an element that comes in two grades",
             "correct": False,
             "why": "An element is one kind of atom, and brass holds two. "
                    "Grades of anything are a sign of a mixture"},
        ],
        "figure": None,
    },
    {
        "id": "c2-02-s09",
        "band": "standard",
        "text": "Bright yellow sulfur powder conducts nothing at all, snaps "
                "rather than bending, and looks nothing like a metal. Is it an "
                "element?",
        "options": [
            {"text": "No — an element has to conduct electricity, and this "
                     "one does not conduct at all",
             "correct": False,
             "why": "Conducting is a property of metals, and most elements "
                    "are not metals. It has nothing to do with the "
                    "definition"},
            {"text": "Yes — nothing simpler can be got out of it, and that is "
                     "the whole test",
             "correct": True},
            {"text": "No — a powder is made of separate grains, so it must be "
                     "a mixture of something",
             "correct": False,
             "why": "Grinding an element gives grains of that element. Being "
                    "a powder says nothing about what it is made of"},
            {"text": "It cannot be decided without knowing where the sample "
                     "came from originally",
             "correct": False,
             "why": "Where it came from is never the test. Several elements "
                    "are made artificially and are still elements"},
        ],
        "figure": None,
    },

    # ── harder · MRB-335 top-up ─────────────────────────────────────────
    {
        "id": "c2-02-h05",
        "band": "harder",
        "text": "Before electricity was available, chemists listed soda as an "
                "element. Electrolysis then split it. Were they wrong to have "
                "listed it?",
        "options": [
            {"text": "Yes — they should have waited until every method had "
                     "been invented",
             "correct": False,
             "why": "No list could ever be published on that rule, because "
                    "there is always another method to come"},
            {"text": "No — they reported what their methods could show, and a "
                     "new method moved it off the list",
             "correct": True},
            {"text": "Yes — soda is obviously a compound, and careful work "
                     "would have shown it",
             "correct": False,
             "why": "Nothing available to them could take it apart. It was "
                    "not carelessness but the limit of the technique"},
            {"text": "No — soda really was an element then and became a "
                     "compound later",
             "correct": False,
             "why": "The substance never changed. What changed was what could "
                    "be found out about it"},
        ],
        "figure": None,
    },
    {
        "id": "c2-02-h06",
        "band": "harder",
        "text": "Steel conducts, is shiny and can be hammered flat, and it "
                "has no entry on the periodic table. Iron has an entry and "
                "does all three too. What separates them?",
        "options": [
            {"text": "Iron is magnetic and steel is not, which is the "
                     "property that decides whether something is an element",
             "correct": False,
             "why": "Most steel is magnetic, and being magnetic is not part "
                    "of the definition of an element in any case"},
            {"text": "Steel is harder than iron, and hardness is what the "
                     "table records",
             "correct": False,
             "why": "The table records elements, not hardness. Diamond is "
                    "harder than any metal and carbon still has one entry"},
            {"text": "Steel has carbon added, in an amount the steelmaker "
                     "chooses, so it is more than one kind of atom",
             "correct": True},
            {"text": "Steel is manufactured and iron is found in the ground",
             "correct": False,
             "why": "Iron has to be smelted out of its ore, so it is "
                    "manufactured too. Origin is never the test"},
        ],
        "figure": None,
    },
    {
        "id": "c2-02-h07",
        "band": "harder",
        "text": "Every atom in your body except the hydrogen was made inside "
                "a star. What does that tell you about the atoms you are made "
                "of?",
        "options": [
            {"text": "That your atoms are steadily being replaced by newly "
                     "made ones as you grow older and older",
             "correct": False,
             "why": "Atoms move between substances constantly, but no new "
                    "ones are being made. There is no such thing as a fresh "
                    "atom"},
            {"text": "That your body must contain elements not found "
                     "elsewhere on Earth",
             "correct": False,
             "why": "Every element in you is common on Earth. Being made in a "
                    "star is true of the rock under your feet as well"},
            {"text": "That living things can make their own atoms out of "
                     "food",
             "correct": False,
             "why": "Food supplies atoms; nothing in biology makes one. "
                    "Living things rearrange what they take in"},
            {"text": "That they are extremely old, and were used by something "
                     "else before they were used by you",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c2-02-h08",
        "band": "harder",
        "text": "Two samples both fail to break down under every test on the "
                "bench. One is on the periodic table and the other is not "
                "listed anywhere. What is the most likely explanation?",
        "options": [
            {"text": "The unlisted one is a compound so strongly joined that "
                     "no method on this bench has been able to separate it",
             "correct": True},
            {"text": "The unlisted one is an element that nobody has "
                     "discovered yet",
             "correct": False,
             "why": "Possible in principle, and far less likely. New elements "
                    "are made one at a time in specialised laboratories"},
            {"text": "The table must have an entry missing, since anything "
                     "that refuses to break down is an element",
             "correct": False,
             "why": "That assumes the bench's tests are complete, which is "
                    "exactly the assumption soda punished"},
            {"text": "The unlisted one is a mixture whose parts happen to be "
                     "identical",
             "correct": False,
             "why": "A mixture of identical substances is just that "
                    "substance. There is nothing there to separate"},
        ],
        "figure": None,
    },
    {
        "id": "c2-02-h09",
        "band": "harder",
        "text": "Sodium fizzes across water and catches fire; gold sits in "
                "acid unchanged. Both are elements. What does that pair show "
                "about the definition?",
        "options": [
            {"text": "That reacting violently is a sign of an element, and "
                     "gold must be an exception to a rule that usually "
                     "holds",
             "correct": False,
             "why": "There is no such rule. Compounds react violently too, "
                    "and plenty of elements do almost nothing"},
            {"text": "That an element is defined by what it is made of, not "
                     "by how strongly it reacts",
             "correct": True},
            {"text": "That the definition only works for metals that behave "
                     "themselves",
             "correct": False,
             "why": "It works for every substance. Neither sodium's fizzing "
                    "nor gold's stillness touches it"},
            {"text": "That sodium is being broken down by the water, which is "
                     "why the definition needs care here",
             "correct": False,
             "why": "The reaction builds something more complicated out of "
                    "the sodium. Nothing simpler comes out of it"},
        ],
        "figure": None,
    },
    # ── MRB-338 expansion · easier ──────────────────────────────────────
    {
        "id": "c2-02-e10",
        "band": "easier",
        "text": "Copper is made of copper atoms and nothing else, with no "
                "other kind of atom anywhere in it. Which word describes a "
                "substance like that?",
        "options": [
            {"text": "An element, because every atom in it is the same kind",
             "correct": True},
            {"text": "A compound, because the atoms are all joined together",
             "correct": False,
             "why": "A compound needs at least two DIFFERENT kinds of atom "
                    "joined. One kind joined to itself is still an element."},
            {"text": "A mixture, because there is a great deal of it in one place",
             "correct": False,
             "why": "A mixture holds two or more substances in the same place. "
                    "How much there is of one substance changes nothing."},
            {"text": "A molecule, because that is what a lump of metal is called",
             "correct": False,
             "why": "A molecule is a small group of atoms joined together, not "
                    "a name for a lump of anything."},
        ],
        "figure": None,
    },
    {
        "id": "c2-02-e11",
        "band": "easier",
        "text": "Every known element has its own entry on one organised list. "
                "What is that list called?",
        "options": [
            {"text": "The reactivity series, which orders substances by how they react",
             "correct": False,
             "why": "The reactivity series ranks some metals by how vigorously "
                    "they react. It leaves out most of the elements entirely."},
            {"text": "The periodic table, which has an entry for every element",
             "correct": True},
            {"text": "The formula list, which gives the formula of every substance",
             "correct": False,
             "why": "Formulae describe compounds. The table lists the elements "
                    "themselves, not the substances they build."},
            {"text": "The particle model, which explains solids, liquids and gases",
             "correct": False,
             "why": "The particle model explains how matter behaves. It is not "
                    "a list of anything."},
        ],
        "figure": None,
    },
    {
        "id": "c2-02-e12",
        "band": "easier",
        "text": "Sulfur, copper, aluminium and zinc are all elements. Which "
                "one of them is a non-metal?",
        "options": [
            {"text": "Sulfur", "correct": True},
            {"text": "Copper", "correct": False,
             "why": "Copper is a metal element: orange, shiny when cut, and it "
                    "conducts electricity well."},
            {"text": "Aluminium", "correct": False,
             "why": "Aluminium is a metal element. It is light, shiny and rolls "
                    "into foil without snapping."},
            {"text": "Zinc", "correct": False,
             "why": "Zinc is a metal element, and one of the two metals mixed "
                    "together to make brass."},
        ],
        "figure": None,
    },
    {
        "id": "c2-02-e13",
        "band": "easier",
        "text": "Which of these four elements is a metal: oxygen, carbon, "
                "aluminium or chlorine?",
        "options": [
            {"text": "Oxygen", "correct": False,
             "why": "Oxygen is a non-metal element and a colourless gas at room "
                    "temperature."},
            {"text": "Carbon", "correct": False,
             "why": "Carbon is a non-metal element. Soot, charcoal and diamond "
                    "are all carbon."},
            {"text": "Aluminium", "correct": True},
            {"text": "Chlorine", "correct": False,
             "why": "Chlorine is a non-metal element and a green gas on its "
                    "own."},
        ],
        "figure": None,
    },
    {
        "id": "c2-02-e14",
        "band": "easier",
        "text": "Iron, copper and gold are all metal elements. Which pair of "
                "properties would you expect all three of them to have?",
        "options": [
            {"text": "Dull to look at, and easy to snap in half by hand",
             "correct": False,
             "why": "Being dull and brittle is typical of non-metal solids such "
                    "as sulfur, not of metals."},
            {"text": "Shiny when cut, but unable to conduct electricity",
             "correct": False,
             "why": "Every one of these three conducts electricity. That is one "
                    "of the properties that makes them metals."},
            {"text": "Conducts electricity well, but snaps when bent",
             "correct": False,
             "why": "Metals can be bent and hammered into shape. Snapping "
                    "instead of bending is a non-metal habit."},
            {"text": "Shiny when freshly cut, and able to conduct electricity",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c2-02-e15",
        "band": "easier",
        "text": "Sulfur is a typical non-metal solid. Which set of "
                "properties fits it best?",
        "options": [
            {"text": "Dull, brittle, and it does not conduct electricity",
             "correct": True},
            {"text": "Shiny, bendable, and it conducts electricity well",
             "correct": False,
             "why": "That is the metal set of properties. Copper and iron fit "
                    "it; sulfur fits none of it."},
            {"text": "Shiny, brittle, and it conducts electricity well",
             "correct": False,
             "why": "Conducting is a metal property, and metals bend rather "
                    "than snap. This mixes the two lists up."},
            {"text": "Dull, bendable, and it does not conduct electricity",
             "correct": False,
             "why": "Non-metal solids snap rather than bend. Bendability goes "
                    "with the metals."},
        ],
        "figure": None,
    },
    {
        "id": "c2-02-e16",
        "band": "easier",
        "text": "Helium is used to fill party balloons and it will not burn. "
                "Which description of helium is correct?",
        "options": [
            {"text": "It is a metal element, because industry makes such heavy use of it",
             "correct": False,
             "why": "Being useful in industry is not a property of metals. "
                    "Helium is a gas that conducts nothing."},
            {"text": "It is a non-metal element, and a gas at room temperature",
             "correct": True},
            {"text": "It is a compound of two lighter gases joined together",
             "correct": False,
             "why": "Helium has its own entry on the periodic table, so it is "
                    "one kind of atom, not two joined."},
            {"text": "It is a mixture of gases, which is why it is so light",
             "correct": False,
             "why": "A balloon of helium holds helium atoms and nothing else. "
                    "Air is the mixture, not helium."},
        ],
        "figure": None,
    },
    {
        "id": "c2-02-e17",
        "band": "easier",
        "text": "A particle of oxygen gas is two oxygen atoms bonded to each "
                "other. Is oxygen an element?",
        "options": [
            {"text": "No, because an element has to be single atoms on their own",
             "correct": False,
             "why": "Nothing in the definition says the atoms must be separate. "
                    "It says they must all be the same kind."},
            {"text": "No, because two atoms joined make a compound every time",
             "correct": False,
             "why": "A compound needs two DIFFERENT kinds of atom. Two oxygen "
                    "atoms joined are still only oxygen."},
            {"text": "Yes, because every atom in it is the same kind of atom",
             "correct": True},
            {"text": "Yes, but only while the pairs stay joined together",
             "correct": False,
             "why": "Separate oxygen atoms would still be oxygen. Joining "
                    "makes no difference to what kind they are."},
        ],
        "figure": None,
    },
    {
        "id": "c2-02-e18",
        "band": "easier",
        "text": "Which element makes up the largest share of the Earth's "
                "crust by mass?",
        "options": [
            {"text": "Iron, because the crust is full of iron ore",
             "correct": False,
             "why": "Iron is about 5% of the crust. There is a great deal of "
                    "it, but three elements beat it."},
            {"text": "Silicon, because sand and most kinds of rock contain silicon",
             "correct": False,
             "why": "Silicon is about 28% and comes second. Sand contains "
                    "oxygen as well as silicon."},
            {"text": "Aluminium, because it is the commonest metal in rocks",
             "correct": False,
             "why": "Aluminium is about 8%. It is the commonest metal in the "
                    "crust, but not the commonest element."},
            {"text": "Oxygen, because it is locked into almost every rock",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c2-02-e19",
        "band": "easier",
        "text": "By mass, there is more of one particular element in you "
                "than of any other. Which element is it?",
        "options": [
            {"text": "Oxygen, because most of your body is water",
             "correct": True},
            {"text": "Carbon, because living things are carbon based",
             "correct": False,
             "why": "Carbon comes second, at roughly 18%. Living things are "
                    "built round carbon, but water outweighs it."},
            {"text": "Calcium, because your bones are the heaviest part",
             "correct": False,
             "why": "Calcium is a small percentage. Bone is not most of your "
                    "mass, and it holds water too."},
            {"text": "Iron, because your blood carries oxygen around",
             "correct": False,
             "why": "Iron is well under 1% of you. It is essential, but there "
                    "is only a few grams of it."},
        ],
        "figure": None,
    },
    {
        "id": "c2-02-e20",
        "band": "easier",
        "text": "A teacher says an element cannot be broken down into "
                "anything simpler by chemical means. Which result would "
                "therefore be impossible for an element?",
        "options": [
            {"text": "Melting it into a liquid and then boiling it into a gas",
             "correct": False,
             "why": "Melting and boiling are physical changes. The same atoms "
                    "are there afterwards, spread further apart."},
            {"text": "Splitting it with electricity into two other substances",
             "correct": True},
            {"text": "Dissolving it in acid so that a new compound is made",
             "correct": False,
             "why": "Reacting with acid builds something more complicated out "
                    "of the element. It does not take it apart."},
            {"text": "Hammering it flat until it is a thin sheet of the same stuff",
             "correct": False,
             "why": "Hammering changes the shape and nothing else. No new "
                    "substance appears."},
        ],
        "figure": None,
    },
    {
        "id": "c2-02-e21",
        "band": "easier",
        "text": "Which one of these four substances is an element?",
        "options": [
            {"text": "Steel", "correct": False,
             "why": "Steel is iron with a little carbon added, so it holds two "
                    "kinds of atom."},
            {"text": "Rust", "correct": False,
             "why": "Rust is iron joined to oxygen, which makes it a compound "
                    "of two elements."},
            {"text": "Iron", "correct": True},
            {"text": "Air", "correct": False,
             "why": "Air is a mixture of nitrogen, oxygen, argon and other "
                    "gases, and the proportions vary."},
        ],
        "figure": None,
    },
    {
        "id": "c2-02-e22",
        "band": "easier",
        "text": "A bar of pure gold is cut in half, and then one half is cut "
                "in half again. What is inside every piece?",
        "options": [
            {"text": "Gold atoms, and a few atoms of whatever it was cut with",
             "correct": False,
             "why": "Cutting shapes the metal; it does not put the blade into "
                    "it. The pieces are still pure gold."},
            {"text": "Gold atoms mixed with traces of other metals",
             "correct": False,
             "why": "Pure gold means gold atoms only. A bar with other atoms "
                    "in it would not be called pure."},
            {"text": "Atoms that become gold only when there are enough of them",
             "correct": False,
             "why": "A gold atom is a gold atom on its own. Identity does not "
                    "depend on how many are gathered."},
            {"text": "Gold atoms, and nothing but gold atoms",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c2-02-e23",
        "band": "easier",
        "text": "On the periodic table, whereabouts are most of the metal "
                "elements found?",
        "options": [
            {"text": "On the left-hand side, and in the middle of the table",
             "correct": True},
            {"text": "On the right-hand side, above all of the non-metals",
             "correct": False,
             "why": "The right-hand side is where the non-metals sit, ending "
                    "with the unreactive gases."},
            {"text": "Along the bottom row only, underneath the gases",
             "correct": False,
             "why": "The rows are not sorted into metals and non-metals like "
                    "that. Metals fill most of the table."},
            {"text": "Scattered evenly, with no pattern to where they sit",
             "correct": False,
             "why": "The whole point of the table is that it is organised. "
                    "Metals and non-metals sit in separate regions."},
        ],
        "figure": None,
    },
    {
        "id": "c2-02-e24",
        "band": "easier",
        "text": "Nearly every element is a solid at room temperature. Which "
                "one of these is a liquid at room temperature?",
        "options": [
            {"text": "Chlorine", "correct": False,
             "why": "Chlorine is a green gas at room temperature. It has to be "
                    "cooled hard before it liquefies."},
            {"text": "Mercury", "correct": True},
            {"text": "Sodium", "correct": False,
             "why": "Sodium is a soft solid kept under oil. It melts at about "
                    "98 °C, well above room temperature."},
            {"text": "Sulfur", "correct": False,
             "why": "Sulfur is a yellow solid at room temperature and melts at "
                    "about 115 °C."},
        ],
        "figure": None,
    },
    {
        "id": "c2-02-e25",
        "band": "easier",
        "text": "Copper is used for the wires inside a plug. Which property "
                "of copper is the reason for that choice?",
        "options": [
            {"text": "It is orange, so the wires are easy to spot",
             "correct": False,
             "why": "Colour has nothing to do with it. Wires are covered in "
                    "coloured plastic anyway."},
            {"text": "It is heavy, so the wire stays where it is put",
             "correct": False,
             "why": "Density is not the reason. A heavy wire that would not "
                    "conduct would be useless."},
            {"text": "It conducts electricity well and can be bent",
             "correct": True},
            {"text": "It has its own entry on the periodic table",
             "correct": False,
             "why": "Being an element does not make a substance conduct. "
                    "Sulfur has an entry and conducts nothing."},
        ],
        "figure": None,
    },
    {
        "id": "c2-02-e26",
        "band": "easier",
        "text": "A jar of pure sugar holds one substance with nothing else "
                "mixed into it. Is sugar an element?",
        "options": [
            {"text": "Yes, because pure and element mean the same thing",
             "correct": False,
             "why": "Pure means nothing else is mixed in. Element means one "
                    "kind of atom. They are different questions."},
            {"text": "Yes, because nothing else was added to the jar",
             "correct": False,
             "why": "What has been added is not the test. The test is what "
                    "kinds of atom the sugar itself is made of."},
            {"text": "It cannot be decided without weighing the sugar",
             "correct": False,
             "why": "Mass settles nothing here. A gram and a kilogram of sugar "
                    "are made of exactly the same atoms."},
            {"text": "No, because sugar is made of more than one kind of atom",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c2-02-e27",
        "band": "easier",
        "text": "Chlorine is added to swimming pool water to kill bacteria. "
                "What is chlorine?",
        "options": [
            {"text": "A non-metal element, and a green gas on its own",
             "correct": True},
            {"text": "A compound of chlorine joined to oxygen atoms",
             "correct": False,
             "why": "Chlorine is one kind of atom, with its own entry on the "
                    "periodic table. Nothing is joined to it."},
            {"text": "A mixture of gases sold under a single name",
             "correct": False,
             "why": "Chlorine gas holds chlorine atoms only, so it is one "
                    "substance rather than several mixed."},
            {"text": "A metal element, because industry uses so much of it",
             "correct": False,
             "why": "How much industry uses is not a property. Chlorine is a "
                    "gas that conducts nothing."},
        ],
        "figure": None,
    },
    {
        "id": "c2-02-e28",
        "band": "easier",
        "text": "Magnesium's entry on the periodic table is written Mg. A "
                "student says that two letters must mean two elements joined "
                "together. Are they right?",
        "options": [
            {"text": "Yes, because the M and the g stand for different atoms",
             "correct": False,
             "why": "The two letters belong to one name. They are not two "
                    "separate entries pushed together."},
            {"text": "No, because Mg is one entry standing for one element",
             "correct": True},
            {"text": "Yes, because only single letters are used for elements",
             "correct": False,
             "why": "Plenty of elements have two-letter entries — Fe, Na, Al, "
                    "He — and every one of them is a single element."},
            {"text": "It depends on whether the second letter is a capital",
             "correct": False,
             "why": "The lower-case letter is part of one element's entry. It "
                    "does not turn one element into two."},
        ],
        "figure": None,
    },
    {
        "id": "c2-02-e29",
        "band": "easier",
        "text": "Magnesium ribbon is burned in air and a white powder is "
                "left behind. What has happened to the magnesium atoms?",
        "options": [
            {"text": "They have been destroyed, which is why the ribbon has gone",
             "correct": False,
             "why": "No chemical reaction destroys atoms. The ribbon has "
                    "changed into something else, not vanished."},
            {"text": "They have turned into a different element in the powder",
             "correct": False,
             "why": "Chemistry rearranges atoms and joins them up. It never "
                    "changes what kind of atom they are."},
            {"text": "They are all still there, now joined to oxygen atoms",
             "correct": True},
            {"text": "They have escaped into the air as a magnesium gas",
             "correct": False,
             "why": "The magnesium atoms are in the white powder, which is why "
                    "the powder weighs more than the ribbon did."},
        ],
        "figure": None,
    },
    {
        "id": "c2-02-e30",
        "band": "easier",
        "text": "A laboratory invents a brand new plastic that has never "
                "existed before. What must that plastic be made from?",
        "options": [
            {"text": "Brand new kinds of atom, invented alongside the plastic",
             "correct": False,
             "why": "Chemistry makes new substances. It has never made a new "
                    "kind of atom."},
            {"text": "One single element that nobody had thought of using",
             "correct": False,
             "why": "A plastic holds several elements joined together, carbon "
                    "and hydrogen among them."},
            {"text": "Nothing at all, because the plastic is entirely artificial",
             "correct": False,
             "why": "Artificial says who made it, not what it is made of. "
                    "Everything is built from atoms."},
            {"text": "Elements that are already on the periodic table",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c2-02-e31",
        "band": "easier",
        "text": "Aluminium can be rolled into a thin sheet of kitchen foil "
                "without snapping. What is that property called?",
        "options": [
            {"text": "Malleable", "correct": True},
            {"text": "Brittle", "correct": False,
             "why": "Brittle means the opposite: it snaps rather than changing "
                    "shape. Sulfur is brittle."},
            {"text": "Conducting", "correct": False,
             "why": "Conducting is about letting electricity or heat pass "
                    "through, not about being shaped."},
            {"text": "Sonorous", "correct": False,
             "why": "Sonorous means it rings when it is struck. That is another "
                    "metal property, but not this one."},
        ],
        "figure": None,
    },
    {
        "id": "c2-02-e32",
        "band": "easier",
        "text": "Which one of these is a list of three elements?",
        "options": [
            {"text": "Water, salt and sugar", "correct": False,
             "why": "All three are compounds. Each one holds at least two "
                    "different kinds of atom joined together."},
            {"text": "Carbon, oxygen and iron", "correct": True},
            {"text": "Air, brass and steel", "correct": False,
             "why": "All three are mixtures, and the proportions in each of "
                    "them can be varied."},
            {"text": "Rust, chalk and water", "correct": False,
             "why": "All three are compounds, each made of more than one kind "
                    "of atom."},
        ],
        "figure": None,
    },
    # ── MRB-338 expansion · standard ────────────────────────────────────
    {
        "id": "c2-02-s10",
        "band": "standard",
        "text": "Neon gas is made of single atoms drifting on their own, and "
                "nitrogen gas is made of atoms joined in pairs. Decide, for "
                "each of the two gases, whether it is an element.",
        "options": [
            {"text": "Only neon, because an element has to be single atoms",
             "correct": False,
             "why": "The definition asks what kind of atoms are present, not "
                    "whether they are joined to each other."},
            {"text": "Only nitrogen, because the atoms have to be joined up",
             "correct": False,
             "why": "Joining is not required either. Neon's separate atoms are "
                    "all neon, so neon is an element."},
            {"text": "Both, because each gas holds only one kind of atom in it",
             "correct": True},
            {"text": "Neither, because a gas in a jar is a mixture of some kind",
             "correct": False,
             "why": "A jar can hold one gas and nothing else. Air is a mixture; "
                    "a jar of pure neon is not."},
        ],
        "figure": None,
    },
    {
        "id": "c2-02-s11",
        "band": "standard",
        "text": "A solid substance is dull, snaps when it is bent and does "
                "not conduct electricity. Nothing simpler can be got out of "
                "it. What is the best conclusion?",
        "options": [
            {"text": "It is a metal element that has been left to go dull",
             "correct": False,
             "why": "A dull metal still bends and still conducts. This one "
                    "does neither."},
            {"text": "It is a compound, because elements always conduct",
             "correct": False,
             "why": "Many elements conduct nothing at all — sulfur, iodine and "
                    "carbon as soot among them."},
            {"text": "It cannot be an element with properties like those",
             "correct": False,
             "why": "Sulfur and iodine are elements and fit this description "
                    "exactly. Non-metal elements behave like this."},
            {"text": "It is a non-metal element, such as sulfur or iodine",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c2-02-s12",
        "band": "standard",
        "text": "Rock is a hard solid and oxygen is a gas, yet oxygen is the "
                "commonest element in rock. What does that tell you about the "
                "oxygen in a piece of rock?",
        "options": [
            {"text": "It is chemically joined to other elements inside compounds",
             "correct": True},
            {"text": "It is trapped as tiny bubbles of gas in the gaps between the rock grains",
             "correct": False,
             "why": "Air caught in cracks is not what the figure counts. The "
                    "oxygen is part of the minerals themselves."},
            {"text": "It has turned into a different element inside the solid rock",
             "correct": False,
             "why": "Atoms keep their identity. Oxygen atoms in rock are still "
                    "oxygen atoms, just joined to others."},
            {"text": "It is mixed in as a fine powder that was once a gas long ago",
             "correct": False,
             "why": "Nothing here is merely mixed. The oxygen is bonded, which "
                    "is why it cannot escape as a gas."},
        ],
        "figure": None,
    },
    {
        "id": "c2-02-s13",
        "band": "standard",
        "text": "Iodine is far less than one thousandth of your body mass, "
                "yet without it a child does not grow properly. What does "
                "that show?",
        "options": [
            {"text": "That the mass of an element decides how important it is",
             "correct": False,
             "why": "This is the opposite of what the example shows. Iodine "
                    "has almost no mass and matters enormously."},
            {"text": "That an element can matter enormously in a tiny amount",
             "correct": True},
            {"text": "That iodine must really be present in a much larger amount",
             "correct": False,
             "why": "The measurement is not wrong. A very small mass of it is "
                    "all the body needs and all it holds."},
            {"text": "That elements below one per cent are not part of the body",
             "correct": False,
             "why": "They are part of it, and several of them are essential — "
                    "iron and iodine among them."},
        ],
        "figure": None,
    },
    {
        "id": "c2-02-s14",
        "band": "standard",
        "text": "Aircraft bodies are built from aluminium rather than iron. "
                "Suggest the property of aluminium that decides it.",
        "options": [
            {"text": "Aluminium is shinier, so the aircraft is much easier to see",
             "correct": False,
             "why": "Shine is not a design consideration here, and aircraft are "
                    "painted anyway."},
            {"text": "Aluminium is an element and iron is not, so it is the purer of the two",
             "correct": False,
             "why": "Iron is an element too. Both have their own entry on the "
                    "periodic table."},
            {"text": "Aluminium melts at a lower temperature than iron does",
             "correct": False,
             "why": "That is true and it is a disadvantage, not a reason to "
                    "choose it."},
            {"text": "Aluminium is much less dense, so the aircraft is lighter",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c2-02-s15",
        "band": "standard",
        "text": "Copper is used for electrical wiring and sulfur is not, "
                "although both of them are elements. Explain the difference.",
        "options": [
            {"text": "Copper conducts electricity and sulfur does not conduct at all",
             "correct": True},
            {"text": "Copper is an element and sulfur is only a compound made from it",
             "correct": False,
             "why": "Sulfur is an element in its own right, with its own entry "
                    "on the periodic table."},
            {"text": "Copper is always pure and sulfur always arrives mixed in with something else",
             "correct": False,
             "why": "Sulfur can be obtained pure. Purity is not what decides "
                    "whether something conducts."},
            {"text": "Copper has an entry on the periodic table and sulfur has none at all",
             "correct": False,
             "why": "Sulfur's entry is S. Every element has one, conductor or "
                    "not."},
        ],
        "figure": None,
    },
    {
        "id": "c2-02-s16",
        "band": "standard",
        "text": "Mercury is a liquid at room temperature while every other "
                "metal in the laboratory is a solid. Does that stop mercury "
                "being an element?",
        "options": [
            {"text": "Yes, because elements are solids apart from a few gases",
             "correct": False,
             "why": "There is no rule about state in the definition. Elements "
                    "come as solids, liquids and gases."},
            {"text": "No, because its state has nothing to do with its atoms",
             "correct": True},
            {"text": "Yes, because a liquid metal must be a mixture of two metals",
             "correct": False,
             "why": "Mercury holds mercury atoms only. Being runny does not "
                    "mean two things are mixed."},
            {"text": "No, but only because mercury freezes if it is cooled enough",
             "correct": False,
             "why": "Freezing is beside the point. Mercury would be an element "
                    "even if it never froze at all."},
        ],
        "figure": None,
    },
    {
        "id": "c2-02-s17",
        "band": "standard",
        "text": "One sealed jar holds neon only. A second jar holds neon and "
                "argon mixed together. Which jar holds an element, and what "
                "settles it?",
        "options": [
            {"text": "Both, because neon and argon are each elements themselves",
             "correct": False,
             "why": "Each gas is an element, but the jar holding both holds two "
                    "kinds of atom, so its contents are a mixture."},
            {"text": "Neither, because a gas in a jar is always mixed with air",
             "correct": False,
             "why": "A jar can be filled with one gas and sealed. The first one "
                    "here holds neon and nothing else."},
            {"text": "The first, because everything in it is the same kind of atom",
             "correct": True},
            {"text": "The second, because it holds more kinds of atom than the first",
             "correct": False,
             "why": "More kinds of atom is exactly what an element does not "
                    "have. That jar holds a mixture."},
        ],
        "figure": None,
    },
    {
        "id": "c2-02-s18",
        "band": "standard",
        "text": "Sulfur is a yellow powder that snaps, and iron is a grey "
                "metal that bends. Explain what makes both of them elements.",
        "options": [
            {"text": "Both of them are found in the ground rather than being made in a factory",
             "correct": False,
             "why": "Where a substance came from is not the test. Several "
                    "elements are made artificially and are still elements."},
            {"text": "Both of them are pure, and every pure substance must be an element",
             "correct": False,
             "why": "Pure water is pure and is not an element. Purity and "
                    "elementhood are different questions."},
            {"text": "Both are solids, and every solid element behaves in the same way",
             "correct": False,
             "why": "These two behave nothing like each other, and elements "
                    "come as gases and liquids too."},
            {"text": "Each is one kind of atom, and nothing simpler comes out of it",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c2-02-s19",
        "band": "standard",
        "text": "A grey solid survives strong heating, acid and electrolysis "
                "unchanged. A student concludes that it must be a metal. "
                "Explain the error in that reasoning.",
        "options": [
            {"text": "The evidence shows it is an element, not that it is a metal",
             "correct": True},
            {"text": "The evidence shows nothing at all, so a great many more tests are needed",
             "correct": False,
             "why": "It is strong evidence for one thing: nothing simpler came "
                    "out, which is the test for an element."},
            {"text": "The student is right, because only metals survive acid",
             "correct": False,
             "why": "Sulfur survives acid and is not a metal. Surviving acid "
                    "sorts nothing into metals."},
            {"text": "The student is right, because a grey solid is always a metal",
             "correct": False,
             "why": "Colour decides nothing. Graphite is grey, and it is a "
                    "non-metal."},
        ],
        "figure": None,
    },
    {
        "id": "c2-02-s20",
        "band": "standard",
        "text": "Chlorine is a green gas, bromine is a red liquid and iodine "
                "is a dark grey solid. All three are non-metal elements. What "
                "does the state of a substance tell you about being an element?",
        "options": [
            {"text": "That gases are elements and solids usually are not",
             "correct": False,
             "why": "Iodine is a solid element and air is a gaseous mixture. "
                    "State sorts nothing."},
            {"text": "Nothing at all, because all three states are found in elements",
             "correct": True},
            {"text": "That an element can only be a gas if it is coloured",
             "correct": False,
             "why": "Oxygen and nitrogen are colourless gases and both are "
                    "elements."},
            {"text": "That all three must really be mixtures, not elements",
             "correct": False,
             "why": "Each has its own entry on the periodic table and holds one "
                    "kind of atom."},
        ],
        "figure": None,
    },
    {
        "id": "c2-02-s21",
        "band": "standard",
        "text": "In 1869 about sixty elements were known and today about a "
                "hundred and twenty are. Explain how that list can grow when "
                "a chemical reaction cannot make a new element.",
        "options": [
            {"text": "Chemists split compounds until brand new atoms appeared",
             "correct": False,
             "why": "Splitting a compound only releases atoms that were in it "
                    "already. Nothing new is made that way."},
            {"text": "The extra entries are compounds that were added to the list later",
             "correct": False,
             "why": "The table lists elements only. No compound has ever been "
                    "given an entry."},
            {"text": "Elements were discovered, and some were made in nuclear reactions",
             "correct": True},
            {"text": "The earlier chemists had simply miscounted the entries they had",
             "correct": False,
             "why": "The count was right for what was known then. New elements "
                    "were found afterwards."},
        ],
        "figure": None,
    },
    {
        "id": "c2-02-s22",
        "band": "standard",
        "text": "The Earth's crust is about 46% oxygen, 28% silicon, 8% "
                "aluminium and 5% iron by mass. Calculate the percentage that "
                "is every other element put together.",
        "options": [
            {"text": "87%", "correct": False,
             "why": "That is the total of the four named elements, not what is "
                    "left over after them."},
            {"text": "26%", "correct": False,
             "why": "That is what is left after subtracting only oxygen and "
                    "silicon. Aluminium and iron have to come off too."},
            {"text": "5%", "correct": False,
             "why": "5% is iron's own share, which is one of the four already "
                    "counted."},
            {"text": "13%", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c2-02-s23",
        "band": "standard",
        "text": "A person has a mass of 60 kg, and about 65% of that mass is "
                "the element oxygen. Calculate the mass of oxygen in them.",
        "options": [
            {"text": "39 kg", "correct": True},
            {"text": "3.9 kg", "correct": False,
             "why": "A power of ten has slipped. 65% of 60 kg is 39 kg, not "
                    "3.9 kg."},
            {"text": "21 kg", "correct": False,
             "why": "That is the 35% that is NOT oxygen. The question asks for "
                    "the oxygen itself."},
            {"text": "65 kg", "correct": False,
             "why": "The 65 is a percentage, not a mass — and it is more than "
                    "the whole person weighs."},
        ],
        "figure": None,
    },
    {
        "id": "c2-02-s24",
        "band": "standard",
        "text": "A heap of iron filings and a solid iron nail look completely "
                "different from one another. Explain what the two of them "
                "have in common.",
        "options": [
            {"text": "Nothing at all, because grinding a nail changes what it is made of",
             "correct": False,
             "why": "Grinding breaks a solid into smaller pieces. It does not "
                    "change any atom in it."},
            {"text": "Both are made only of iron atoms, so both are the element iron",
             "correct": True},
            {"text": "Both are compounds of iron with the oxygen in the air",
             "correct": False,
             "why": "Rust is such a compound, but clean iron is not. Both "
                    "samples here are the metal itself."},
            {"text": "Both are mixtures, because filings have air in between them",
             "correct": False,
             "why": "Air in the gaps is not part of the iron. The filings "
                    "themselves are one substance."},
        ],
        "figure": None,
    },
    {
        "id": "c2-02-s25",
        "band": "standard",
        "text": "Carbon is a non-metal, yet graphite, which is pure carbon, "
                "conducts electricity well. What does that show about the "
                "metal and non-metal descriptions?",
        "options": [
            {"text": "That graphite must really be a metal element after all",
             "correct": False,
             "why": "Graphite is carbon, and carbon sits among the non-metals. "
                    "One shared property does not move it."},
            {"text": "That carbon is a compound rather than an element",
             "correct": False,
             "why": "Carbon has its own entry on the periodic table and holds "
                    "one kind of atom."},
            {"text": "That the two sets of properties are typical, not absolute",
             "correct": True},
            {"text": "That conducting proves nothing unless a substance is shiny",
             "correct": False,
             "why": "Conducting is genuinely useful evidence. It is simply not "
                    "a rule without exceptions."},
        ],
        "figure": None,
    },
    {
        "id": "c2-02-s26",
        "band": "standard",
        "text": "A window frame has to stand outdoors for twenty years. "
                "Aluminium and iron are both metal elements. Which is the "
                "better choice, and why?",
        "options": [
            {"text": "Iron, because it is stronger than aluminium in every way",
             "correct": False,
             "why": "Strength is not what fails here. An iron frame rusts "
                    "through however strong it started."},
            {"text": "Iron, because rust forms a coat that protects the metal below",
             "correct": False,
             "why": "Rust flakes away and exposes fresh iron underneath, so "
                    "the rusting simply carries on."},
            {"text": "Aluminium, because it is an element and iron is a mixture",
             "correct": False,
             "why": "Both are elements. Iron only becomes a mixture once "
                    "carbon is added to make steel."},
            {"text": "Aluminium, because it does not rust away as iron does",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c2-02-s27",
        "band": "standard",
        "text": "Hydrogen is lighter than helium, but party balloons are "
                "filled with helium instead. Suggest why.",
        "options": [
            {"text": "Helium does not burn, and hydrogen catches fire very easily",
             "correct": True},
            {"text": "Helium is an element and hydrogen is a compound of two atoms",
             "correct": False,
             "why": "Hydrogen is an element as well. Two atoms of the same "
                    "kind joined are still one element."},
            {"text": "Helium is much cheaper to obtain than hydrogen is",
             "correct": False,
             "why": "Helium is the more expensive of the two. It is chosen "
                    "despite the cost, not because of it."},
            {"text": "Helium floats in air and hydrogen sinks towards the floor",
             "correct": False,
             "why": "Both are less dense than air, and hydrogen is the less "
                    "dense of the two."},
        ],
        "figure": None,
    },
    {
        "id": "c2-02-s28",
        "band": "standard",
        "text": "There are only about a hundred elements, yet millions of "
                "different substances exist. Explain how so few can give so "
                "many.",
        "options": [
            {"text": "Most substances are made of atoms that are not elements at all",
             "correct": False,
             "why": "Every atom is an atom of some element. There is no other "
                    "kind of atom to be made of."},
            {"text": "Elements join in different combinations and different ratios",
             "correct": True},
            {"text": "Each of the hundred elements comes in millions of slightly different forms",
             "correct": False,
             "why": "A few elements have more than one form, but that is a "
                    "handful of cases, not millions."},
            {"text": "New elements are made whenever a new substance is needed",
             "correct": False,
             "why": "Chemistry makes new substances and never new elements. "
                    "The list stays the same."},
        ],
        "figure": None,
    },
    {
        "id": "c2-02-s29",
        "band": "standard",
        "text": "A magnesium ribbon is dull grey on the outside and bright "
                "silver underneath. A student says magnesium cannot be an "
                "element because the ribbon is two different colours. Respond.",
        "options": [
            {"text": "They are right, because an element must look the same throughout",
             "correct": False,
             "why": "Appearance decides nothing about elements. The test is "
                    "what kinds of atom are present."},
            {"text": "They are right, because the coating proves it is a mixture",
             "correct": False,
             "why": "The coating formed by reacting with the air. Nothing was "
                    "mixed into the magnesium."},
            {"text": "They are wrong: the coating is magnesium joined to oxygen from the air",
             "correct": True},
            {"text": "They are wrong, but only because the coating rubs off easily",
             "correct": False,
             "why": "Rubbing it off is not the reason. The argument from "
                    "colour was never sound in the first place."},
        ],
        "figure": None,
    },
    {
        "id": "c2-02-s30",
        "band": "standard",
        "text": "A saucepan base is made from a metal element such as "
                "aluminium rather than a non-metal such as sulfur. Explain "
                "the choice.",
        "options": [
            {"text": "Aluminium is an element and sulfur is not, so it lasts longer",
             "correct": False,
             "why": "Sulfur is an element too. Being an element is not what "
                    "makes a good saucepan."},
            {"text": "Sulfur is far more expensive than aluminium to buy in bulk",
             "correct": False,
             "why": "Sulfur is cheap. Cost is not the reason it would make a "
                    "hopeless saucepan."},
            {"text": "Sulfur conducts heat better but melts at too high a temperature",
             "correct": False,
             "why": "Both halves are wrong: sulfur is a poor conductor of heat "
                    "and melts at about 115 °C."},
            {"text": "Aluminium conducts heat well and will not melt while cooking",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c2-02-s31",
        "band": "standard",
        "text": "A block of tin is melted into a liquid and poured into a "
                "mould. Is the liquid in the mould still the element tin?",
        "options": [
            {"text": "Yes, because melting moves the atoms without changing them",
             "correct": True},
            {"text": "No, because a liquid and a solid are different substances",
             "correct": False,
             "why": "State is a physical property. Ice and water are the same "
                    "substance, and so are solid and molten tin."},
            {"text": "No, because melting breaks the tin down into something simpler",
             "correct": False,
             "why": "Nothing simpler comes out. Melting takes energy but "
                    "produces no new substance."},
            {"text": "Yes, but it stops being an element once it sets again",
             "correct": False,
             "why": "It never stopped being tin at any point, molten or "
                    "solid."},
        ],
        "figure": None,
    },
    {
        "id": "c2-02-s32",
        "band": "standard",
        "text": "A bicycle has iron in the frame, aluminium in the wheels, "
                "carbon and other elements in the tyres and copper in the "
                "cables. No single part is a pure element. Explain how the "
                "whole bicycle still traces back to elements.",
        "options": [
            {"text": "The parts are made of substances that contain no elements at all",
             "correct": False,
             "why": "Every substance is built from elements. There is nothing "
                    "else for it to be built from."},
            {"text": "Every substance is built from elements, joined or mixed together",
             "correct": True},
            {"text": "Only the metal parts come from elements; the rubber does not",
             "correct": False,
             "why": "Rubber holds carbon and hydrogen atoms joined together, "
                    "so it comes from elements as well."},
            {"text": "The bicycle would only count if each part were a pure element",
             "correct": False,
             "why": "Compounds and mixtures are made of elements too. Being "
                    "pure is not what puts elements in a thing."},
        ],
        "figure": None,
    },
    # ── MRB-338 expansion · harder ──────────────────────────────────────
    {
        "id": "c2-02-h10",
        "band": "harder",
        "text": "About 28% of the Earth's crust by mass is the element "
                "silicon. A student concludes that the crust must therefore "
                "be mostly sand. Evaluate that conclusion.",
        "options": [
            {"text": "It is correct, because sand is the only substance that holds any silicon",
             "correct": False,
             "why": "Silicon is in clay, granite, quartz and thousands of "
                    "other minerals besides sand."},
            {"text": "It is correct, because 28% beats any other single substance",
             "correct": False,
             "why": "The 28% is a share of an ELEMENT, not of a substance. It "
                    "is spread across many substances at once."},
            {"text": "It is wrong: the silicon is spread through many different minerals",
             "correct": True},
            {"text": "It is wrong, because the silicon inside rock is not really silicon",
             "correct": False,
             "why": "The atoms are silicon atoms wherever they are. They are "
                    "joined to others, not changed into something else."},
        ],
        "figure": None,
    },
    {
        "id": "c2-02-h11",
        "band": "harder",
        "text": "A 2.4 g sample is decomposed completely and gives 1.4 g of "
                "one gas and 1.0 g of a different gas. Determine whether the "
                "original sample was an element, and justify your answer.",
        "options": [
            {"text": "It was an element, because the two gas masses add back up to the original 2.4 g",
             "correct": False,
             "why": "Mass is conserved in every reaction, so that adds nothing. "
                    "It is the two different products that matter."},
            {"text": "It was an element, because gases can never come out of a compound",
             "correct": False,
             "why": "Gases coming out of a compound is exactly what happens "
                    "when water is electrolysed."},
            {"text": "It cannot be decided until both of the two gases have been named",
             "correct": False,
             "why": "Naming them adds nothing. Two different substances coming "
                    "out has already settled it."},
            {"text": "It was not an element: two different substances came out of it",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c2-02-h12",
        "band": "harder",
        "text": "A student proposes a rule: any substance with a one-word "
                "name is an element. Test that rule against water and against "
                "sulfur.",
        "options": [
            {"text": "The rule fails: water has a one-word name and is a compound",
             "correct": True},
            {"text": "The rule works: sulfur has a one-word name and is an element",
             "correct": False,
             "why": "One case that fits does not establish a rule, and water "
                    "breaks it immediately."},
            {"text": "The rule fails: sulfur has a one-word name and is a compound",
             "correct": False,
             "why": "Sulfur is an element. The rule does fail, but not because "
                    "of sulfur."},
            {"text": "The rule works, because compounds always have two-word names",
             "correct": False,
             "why": "Ammonia, methane and sugar are all compounds with "
                    "one-word names."},
        ],
        "figure": None,
    },
    {
        "id": "c2-02-h13",
        "band": "harder",
        "text": "Ozone is made of oxygen atoms joined in threes and ordinary "
                "oxygen gas is made of the same atoms joined in pairs, and the "
                "two smell and behave differently. Does that break the rule "
                "that an element is one kind of atom?",
        "options": [
            {"text": "Yes, because two substances cannot both be the same element",
             "correct": False,
             "why": "They can. The rule fixes what kind of atom is present, not "
                    "how many are joined in each group."},
            {"text": "No, both are the element oxygen; only the arrangement differs",
             "correct": True},
            {"text": "Yes, because ozone must be a compound of oxygen with itself",
             "correct": False,
             "why": "A compound needs two DIFFERENT kinds of atom. Only oxygen "
                    "atoms are present in either."},
            {"text": "No, because ozone is really a mixture of oxygen and something",
             "correct": False,
             "why": "Nothing else is there. Ozone holds oxygen atoms and "
                    "nothing but oxygen atoms."},
        ],
        "figure": None,
    },
    {
        "id": "c2-02-h14",
        "band": "harder",
        "text": "A meteorite is analysed and found to hold nothing but iron "
                "atoms and nickel atoms, mixed together. Iron and nickel are "
                "both elements. Is the meteorite an element?",
        "options": [
            {"text": "Yes, because everything in it is a metal element already",
             "correct": False,
             "why": "Two kinds of atom are present, so the meteorite itself is "
                    "not one element however metallic it is."},
            {"text": "Yes, because the two elements sit next to each other on the table",
             "correct": False,
             "why": "Neighbouring entries stay separate elements. The table "
                    "does not merge them."},
            {"text": "No, because two different kinds of atom are present in it",
             "correct": True},
            {"text": "No, because a meteorite is a compound of iron and nickel",
             "correct": False,
             "why": "They are mixed rather than chemically joined, and the "
                    "proportions vary, so it is a mixture."},
        ],
        "figure": None,
    },
    {
        "id": "c2-02-h15",
        "band": "harder",
        "text": "A gold bar of mass 250 g is sold as 99.9% gold by mass. "
                "Calculate the mass that is not gold, and state what the bar "
                "is.",
        "options": [
            {"text": "2.50 g, and the bar is an element because it is nearly pure",
             "correct": False,
             "why": "That is 1%, not 0.1%. Being nearly pure does not make a "
                    "bar one single substance either."},
            {"text": "0.25 g, and the bar is an element because gold is an element",
             "correct": False,
             "why": "The mass is right, but a bar holding other atoms as well "
                    "is a mixture, not the element on its own."},
            {"text": "0.025 g, and the bar is a mixture of gold with other metals",
             "correct": False,
             "why": "0.1% of 250 g is 0.25 g. A power of ten has slipped in "
                    "the arithmetic."},
            {"text": "0.25 g, and the bar is a mixture of gold with other metals",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c2-02-h16",
        "band": "harder",
        "text": "A chemist mixes two known elements extremely thoroughly and "
                "claims to have discovered a new element. Evaluate the claim.",
        "options": [
            {"text": "It fails: mixing gives a mixture of two kinds of atom, not one",
             "correct": True},
            {"text": "It succeeds, because the mixture has properties neither one had",
             "correct": False,
             "why": "New properties genuinely can appear — that is why brass "
                    "exists — but two kinds of atom are still present."},
            {"text": "It succeeds, provided the two are mixed in one fixed ratio",
             "correct": False,
             "why": "A fixed ratio would point towards a compound, and a "
                    "compound is not an element either."},
            {"text": "It fails, because only nuclear reactions can mix two elements",
             "correct": False,
             "why": "Mixing two elements is easy. What mixing cannot do is "
                    "produce a single kind of atom."},
        ],
        "figure": None,
    },
    {
        "id": "c2-02-h17",
        "band": "harder",
        "text": "A helium balloon goes down over a week and a student says "
                "the helium has been used up. Explain what has actually "
                "happened to the helium atoms.",
        "options": [
            {"text": "They have been destroyed slowly by the rubber that the balloon is made of",
             "correct": False,
             "why": "No chemical or physical process on a shelf destroys "
                    "atoms. They have gone somewhere, not ceased to exist."},
            {"text": "They have escaped through the rubber and are still helium atoms",
             "correct": True},
            {"text": "They have turned into air atoms as they mixed with the whole room",
             "correct": False,
             "why": "There is no such thing as an air atom, and atoms never "
                    "change what kind they are."},
            {"text": "They have joined onto the rubber to make a new compound of helium",
             "correct": False,
             "why": "Helium reacts with nothing at all. That is one of the "
                    "reasons it is used in balloons."},
        ],
        "figure": None,
    },
    {
        "id": "c2-02-h18",
        "band": "harder",
        "text": "Mendeleev left gaps in his table for elements nobody had "
                "found, and predicted what they would be like. They were "
                "found later and matched. What does that show about the "
                "periodic table?",
        "options": [
            {"text": "That the table is simply a list written in the order the elements were found",
             "correct": False,
             "why": "Order of discovery is not how it is arranged. If it were, "
                    "a gap could not have been left at all."},
            {"text": "That the gaps were mistakes which later had to be filled in",
             "correct": False,
             "why": "The gaps were deliberate. Mendeleev predicted what would "
                    "belong in them before anyone had found it."},
            {"text": "That the table is organised by a pattern, not just a list of names",
             "correct": True},
            {"text": "That elements can be invented to fill in a gap once one has been left",
             "correct": False,
             "why": "The elements existed already. Finding one is not the same "
                    "as inventing it."},
        ],
        "figure": None,
    },
    {
        "id": "c2-02-h19",
        "band": "harder",
        "text": "One sealed jar holds pure nitrogen and another holds "
                "ordinary air. Both are colourless, have no smell and conduct "
                "nothing. Explain why those results cannot separate the two, "
                "and give one test that would.",
        "options": [
            {"text": "They cannot, and weighing the two jars would settle it at once",
             "correct": False,
             "why": "Air and nitrogen have very nearly the same density, so a "
                    "balance would not tell them apart."},
            {"text": "They cannot, and passing electricity through both would settle it",
             "correct": False,
             "why": "Neither gas conducts, so that is the third test that "
                    "gives the same answer for both."},
            {"text": "They can, because a mixture always looks cloudier than a pure gas",
             "correct": False,
             "why": "Air is perfectly clear, and so is nitrogen. Neither can "
                    "be seen at all."},
            {"text": "They cannot, and cooling both until they liquefy would settle it",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c2-02-h20",
        "band": "harder",
        "text": "Bromine and mercury are both liquids at room temperature. "
                "One is a metal element and one is a non-metal element. "
                "Suggest a single test that would tell you which is which, "
                "and give the result you would expect.",
        "options": [
            {"text": "Test whether each conducts electricity: only the metal will conduct",
             "correct": True},
            {"text": "Weigh equal volumes: the heavier liquid must be the non-metal",
             "correct": False,
             "why": "Mercury is far denser, and mercury is the metal. Density "
                    "does not sort metals from non-metals anyway."},
            {"text": "Look at the colour: the darker liquid is always the metal",
             "correct": False,
             "why": "Bromine is dark red and is the non-metal of the two. "
                    "Colour sorts nothing."},
            {"text": "Freeze both of them: only the non-metal will turn into a solid",
             "correct": False,
             "why": "Both freeze. Mercury freezes at about -39 °C and bromine "
                    "at about -7 °C."},
        ],
        "figure": None,
    },
    {
        "id": "c2-02-h21",
        "band": "harder",
        "text": "Aluminium is the commonest metal in the Earth's crust, yet "
                "ancient civilisations worked gold and copper and never used "
                "aluminium at all. Suggest why.",
        "options": [
            {"text": "Aluminium had not been created yet in the ancient world",
             "correct": False,
             "why": "Elements are not created. The aluminium atoms were in the "
                    "ground the whole time."},
            {"text": "Aluminium is locked into compounds that early methods could not split",
             "correct": True},
            {"text": "Aluminium was much rarer then than it is in the crust today",
             "correct": False,
             "why": "The crust has not changed its composition. The difficulty "
                    "is chemical, not geological."},
            {"text": "Aluminium is far too soft to be shaped into anything useful",
             "correct": False,
             "why": "Gold is softer still and was worked constantly. Softness "
                    "was never the obstacle."},
        ],
        "figure": None,
    },
    {
        "id": "c2-02-h22",
        "band": "harder",
        "text": "The definition says an element cannot be broken down into "
                "anything simpler by chemical means. Explain why the words "
                "'by chemical means' have to be in it.",
        "options": [
            {"text": "Because heating is not a chemical process and would break elements",
             "correct": False,
             "why": "Heating an element makes it melt or boil. Nothing simpler "
                    "comes out of it."},
            {"text": "Because dissolving an element in water counts as breaking it down",
             "correct": False,
             "why": "Dissolving makes a solution and takes nothing apart. The "
                    "atoms are unchanged and can be got back again."},
            {"text": "Because processes inside a nucleus can change one element to another",
             "correct": True},
            {"text": "Because chemists have not yet tried every possible chemical method",
             "correct": False,
             "why": "The phrase marks a boundary between kinds of process, not "
                    "a gap in the work that has been done."},
        ],
        "figure": None,
    },
    {
        "id": "c2-02-h23",
        "band": "harder",
        "text": "About 65% of your body mass is the element oxygen. A student "
                "concludes that you are therefore mostly made of gas. "
                "Evaluate that conclusion.",
        "options": [
            {"text": "It is correct, because oxygen is a gas wherever it happens to be found",
             "correct": False,
             "why": "Oxygen atoms joined to hydrogen make water, which is a "
                    "liquid. The atoms are not a gas when they are bonded."},
            {"text": "It is correct, but only for the oxygen that is carried in the blood",
             "correct": False,
             "why": "The oxygen dissolved and carried in blood is a tiny part "
                    "of the 65%. Nearly all of it is bonded in water."},
            {"text": "It is wrong, because that figure counts the oxygen by volume and not by mass",
             "correct": False,
             "why": "The figure is stated by mass, and it is correct. The "
                    "error is in what the student concludes from it."},
            {"text": "It is wrong: nearly all that oxygen is joined into water and tissue",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c2-02-h24",
        "band": "harder",
        "text": "Air is about 78% nitrogen by volume, and a room holds 60 m³ "
                "of air. Calculate the volume of nitrogen in the room, and "
                "state whether the room's air is an element.",
        "options": [
            {"text": "46.8 m³, and the air is not an element because it is a mixture",
             "correct": True},
            {"text": "46.8 m³, and the air is an element because nitrogen dominates it",
             "correct": False,
             "why": "The volume is right. A majority component does not make a "
                    "mixture into a single element."},
            {"text": "4.68 m³, and the air is not an element because it is a mixture",
             "correct": False,
             "why": "78% of 60 m³ is 46.8 m³. A power of ten has been lost in "
                    "the arithmetic."},
            {"text": "13.2 m³, and the air is not an element because it is a mixture",
             "correct": False,
             "why": "13.2 m³ is the 22% that is NOT nitrogen. The question "
                    "asks for the nitrogen itself."},
        ],
        "figure": None,
    },
    {
        "id": "c2-02-h25",
        "band": "harder",
        "text": "A £1 coin is made of copper mixed with nickel. Copper and "
                "nickel are both metal elements. Explain why the coin itself "
                "is not an element.",
        "options": [
            {"text": "Because the coin was shaped by a machine rather than being dug out of the ground",
             "correct": False,
             "why": "Shaping changes nothing about the atoms. A dug-up lump of "
                    "the same alloy would be no more an element."},
            {"text": "Because two kinds of atom are present in it, not one kind only",
             "correct": True},
            {"text": "Because the coin is a compound of copper chemically joined to nickel",
             "correct": False,
             "why": "The two metals are mixed while molten, not chemically "
                    "joined, and the proportions can be varied."},
            {"text": "Because copper and nickel stop being elements once mixed",
             "correct": False,
             "why": "Each metal's atoms are unchanged by mixing. It is the "
                    "coin that is not one element, not the metals."},
        ],
        "figure": None,
    },
    {
        "id": "c2-02-h26",
        "band": "harder",
        "text": "Silver and aluminium are both shiny, both conduct "
                "electricity and both can be hammered flat. Explain how "
                "chemists can still be certain they are different elements.",
        "options": [
            {"text": "Because one is far more expensive, and price separates elements",
             "correct": False,
             "why": "Price is set by how rare and how useful a metal is. It "
                    "says nothing about the atoms."},
            {"text": "Because silver is pure and aluminium is always found mixed",
             "correct": False,
             "why": "Both can be obtained pure. Both are also found combined "
                    "with other elements in the ground."},
            {"text": "Because their atoms are different kinds, with different masses",
             "correct": True},
            {"text": "Because two substances sharing properties must be compounds",
             "correct": False,
             "why": "Most metals share these properties, and nearly all of "
                    "them are elements."},
        ],
        "figure": None,
    },
    {
        "id": "c2-02-h27",
        "band": "harder",
        "text": "Two definitions are offered to a Year 7 class: an element is "
                "a substance with an entry on the periodic table, or an "
                "element is a substance made of one kind of atom. Which is "
                "the better definition, and why?",
        "options": [
            {"text": "The first, because a student can check it without needing any equipment at all",
             "correct": False,
             "why": "It is convenient, but it explains nothing about why the "
                    "entry is there in the first place."},
            {"text": "The first, because the periodic table has never once been wrong",
             "correct": False,
             "why": "The list has changed as methods improved. Soda was once "
                    "on it and electrolysis took it off."},
            {"text": "Neither, because an element cannot really be defined properly",
             "correct": False,
             "why": "It can be, and the second option does it. Difficulty is "
                    "not the same as impossibility."},
            {"text": "The second, because it says what an element is, not where to look",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c2-02-h28",
        "band": "harder",
        "text": "Hydrogen is the commonest element in the universe, yet it is "
                "only a small share of the Earth's crust by mass. Suggest why.",
        "options": [
            {"text": "Hydrogen atoms are destroyed by the pressure inside the Earth",
             "correct": False,
             "why": "Pressure does not destroy atoms. Nothing in ordinary "
                    "chemistry or geology does."},
            {"text": "Hydrogen atoms are very light, and most of Earth's escaped long ago",
             "correct": True},
            {"text": "Hydrogen exists only in stars and never reaches a rocky planet",
             "correct": False,
             "why": "Water is largely hydrogen by number of atoms, and there "
                    "is a great deal of water here."},
            {"text": "Hydrogen turns into helium once it is part of a rocky planet",
             "correct": False,
             "why": "That happens inside stars, at temperatures no planet "
                    "reaches. Atoms on Earth keep their kind."},
        ],
        "figure": None,
    },
    {
        "id": "c2-02-h29",
        "band": "harder",
        "text": "Element A melts at 1538 °C and conducts electricity. Element "
                "B melts at 115 °C and does not conduct at all. Predict which "
                "is the metal, and suggest one further test.",
        "options": [
            {"text": "B is the metal; test by seeing which of them dissolves in water",
             "correct": False,
             "why": "B's low melting point and lack of conduction are exactly "
                    "the non-metal pattern, and most metals do not dissolve."},
            {"text": "A is the metal; test by checking which one has a table entry",
             "correct": False,
             "why": "Both are elements, so both have entries. That test "
                    "separates nothing at all."},
            {"text": "A is the metal; test by hammering each to see which bends flat",
             "correct": True},
            {"text": "Neither can be judged; test by weighing equal volumes of each",
             "correct": False,
             "why": "The two results given already point clearly at A, and "
                    "density alone does not sort metals from non-metals."},
        ],
        "figure": None,
    },
    {
        "id": "c2-02-h30",
        "band": "harder",
        "text": "Helium reacts with nothing at all. A student argues that "
                "helium therefore cannot be shown to be an element, because "
                "nothing simpler ever comes out of a substance that never "
                "changes. Evaluate that argument.",
        "options": [
            {"text": "The student is right, so helium is listed purely by convention",
             "correct": False,
             "why": "Helium's place rests on evidence about its atoms, not on "
                    "an agreement to list it."},
            {"text": "The student is right, because an element must react to be tested",
             "correct": False,
             "why": "Reacting is not the test. Being one kind of atom is, and "
                    "that can be established without a reaction."},
            {"text": "The student is wrong, because helium reacts with fluorine",
             "correct": False,
             "why": "Helium does not react with fluorine or with anything "
                    "else. The stem is right about that."},
            {"text": "The student is wrong: helium's atoms are one kind, and that is the test",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c2-02-h31",
        "band": "harder",
        "text": "Argon makes up about 1% of the air and does almost nothing "
                "chemically, yet it is used to fill light bulbs. Suggest why "
                "an unreactive element is useful there.",
        "options": [
            {"text": "Because argon conducts electricity a great deal better than the filament does",
             "correct": False,
             "why": "The filament carries the current. Argon conducts nothing "
                    "under ordinary conditions."},
            {"text": "Because argon is heavy enough to hold the glass bulb in shape",
             "correct": False,
             "why": "The glass holds its own shape. Gas inside a bulb is not "
                    "supporting anything."},
            {"text": "Because argon will not react with the hot filament and burn it away",
             "correct": True},
            {"text": "Because argon glows very brightly when a current is passed through it",
             "correct": False,
             "why": "That is how neon signs work. In a filament bulb the light "
                    "comes from the hot wire, not the gas."},
        ],
        "figure": None,
    },
    {
        "id": "c2-02-h32",
        "band": "harder",
        "text": "A laboratory makes a substance that no known chemical method "
                "can break down. Explain what would still have to be shown "
                "before it could be added to the periodic table.",
        "options": [
            {"text": "That it is a great deal more useful than the elements already on the list",
             "correct": False,
             "why": "Usefulness is not a criterion. Several listed elements "
                    "have almost no use at all."},
            {"text": "That its atoms are all one new kind, not a mixture of known ones",
             "correct": True},
            {"text": "That it cannot be made again by any other laboratory in the world",
             "correct": False,
             "why": "Results are expected to be repeatable. Being impossible "
                    "to repeat would count against the claim."},
            {"text": "That it has a colour and a melting point that nobody has recorded",
             "correct": False,
             "why": "Unrecorded properties do not identify a new kind of atom. "
                    "A brand new mixture would have those too."},
        ],
        "figure": None,
    },
]
