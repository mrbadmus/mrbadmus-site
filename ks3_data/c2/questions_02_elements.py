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
]
