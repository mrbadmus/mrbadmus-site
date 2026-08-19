"""C2 lesson 04 — Chemical symbols: twelve questions (MRB-269).

These probe the two ideas the lesson turns on — a symbol is not the English
name shortened, and a capital letter is the thing that starts an element — and
they probe them where students actually go wrong. The distractors are built
from the lesson's declared misconception ATOM-08 (the symbol is just a short
version of the name, so sodium should be So and writing NA hardly matters),
from the lesson's own admitted exception (Cl and Mg are the first and third
letters, not the first two), and from the two counting errors the READS panel
exists to correct: counting letters instead of capitals, and reading a small
subscript as another element. The `harder` band takes the rules somewhere the
lesson never goes — a formula in a textbook you cannot read, a Bronze Age
metals list, and the German word Natriumchlorid — and joins the Berzelius
stretch layer to the hook's point that a notation only matters if other people
can read it.
"""

UNIT = "C2"
LESSON = "chemical-symbols"
LESSON_NUMBER = 4

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "c2-04-e01",
        "band": "easier",
        "text": "A student copies four symbols into their book: Na, Cl, MG, "
                "Fe. One of them breaks the rule for writing a symbol. Which "
                "one?",
        "options": [
            {"text": "Na — sodium",
             "correct": False,
             "why": "Na is written correctly: capital N, lower-case a. It "
                    "comes from natrium, the Latin name, which is why it is "
                    "not So."},
            {"text": "Cl — chlorine",
             "correct": False,
             "why": "Cl is written correctly. It is not the first two letters "
                    "of chlorine — it is the first and the third — but the "
                    "capital-then-lower-case rule is still obeyed."},
            {"text": "MG — magnesium",
             "correct": True},
            {"text": "Fe — iron",
             "correct": False,
             "why": "Fe is written correctly, and it comes from ferrum, the "
                    "Latin for iron. None of the English name appears in the "
                    "symbol at all."},
        ],
        "figure": None,
    },
    {
        "id": "c2-04-e02",
        "band": "easier",
        "text": "Lead's symbol is Pb. Where do those two letters come from?",
        "options": [
            {"text": "From plumbum, the Latin name for lead.",
             "correct": True},
            {"text": "From an older English spelling of lead, cut down to two "
                     "letters.",
             "correct": False,
             "why": "A symbol is not the English name shortened. If it were, "
                    "lead would be L or Le. Pb comes from the Latin plumbum, "
                    "which is also why a plumber is called a plumber."},
            {"text": "From the first and third letters of lead, the way Mg "
                     "works.",
             "correct": False,
             "why": "There is no p and no b in lead. Mg really is built from "
                    "magnesium's own letters; Pb is not built from lead's at "
                    "all."},
            {"text": "It was picked at random when the periodic table was "
                     "drawn up.",
             "correct": False,
             "why": "A symbol that looks wrong is usually a fossil of an older "
                    "name. Pb is Latin, and lead is one of the metals people "
                    "were working with first."},
        ],
        "figure": None,
    },
    {
        "id": "c2-04-e03",
        "band": "easier",
        "text": "You are handed a formula you have never seen before. Which "
                "part of it tells you how many different elements it "
                "contains?",
        "options": [
            {"text": "The total number of letters.",
             "correct": False,
             "why": "Letters are not elements. NaCl has four letters and two "
                    "elements, because a lower-case letter belongs to the "
                    "capital in front of it."},
            {"text": "The number of capital letters.",
             "correct": True},
            {"text": "The small numbers written low down.",
             "correct": False,
             "why": "Those are counts, not elements. The small 3 in CaCO₃ "
                    "counts oxygen; it does not add a fourth kind of atom."},
            {"text": "The number of lower-case letters.",
             "correct": False,
             "why": "A lower-case letter never starts an element. CO has no "
                    "lower-case letters at all and still names two."},
        ],
        "figure": None,
    },
    {
        "id": "c2-04-e04",
        "band": "easier",
        "text": "Which pair of symbols both come from an older Latin name?",
        "options": [
            {"text": "H and C",
             "correct": False,
             "why": "Both are simply the first letter of the English name — "
                    "hydrogen and carbon. Neither has a Latin name behind it."},
            {"text": "Mg and Na",
             "correct": False,
             "why": "Na does come from natrium — but Mg is built from "
                    "magnesium's own letters, the first and the third. Only "
                    "half the pair is Latin."},
            {"text": "Ca and Cl",
             "correct": False,
             "why": "Both come from the English names. Ca is the first two "
                    "letters of calcium; Cl is the first and third of "
                    "chlorine."},
            {"text": "Fe and Au",
             "correct": True},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "c2-04-s01",
        "band": "standard",
        "text": "In a rush, a student writes sodium chloride as NACL. Reading "
                "only what those letters say, how many elements have they "
                "written down?",
        "options": [
            {"text": "Two — the capitals are just untidy handwriting, so it "
                     "still says sodium and chlorine.",
             "correct": False,
             "why": "There is no untidy in this notation. A capital always "
                    "opens a new element, so capitalising the a and the l "
                    "changes what the letters say."},
            {"text": "Four — every letter is a capital, so every letter "
                     "starts a new element.",
             "correct": True},
            {"text": "One — a run of capitals is read as the name of a single "
                     "compound.",
             "correct": False,
             "why": "Capitals are never a name. Each one opens an element, so "
                    "NACL claims four of them where you meant two."},
            {"text": "Three — CL counts as one element, and N and A as one "
                     "each.",
             "correct": False,
             "why": "A capital L cannot belong to the C in front of it. Only "
                    "a lower-case letter does that, which is exactly why "
                    "chlorine must be written Cl with a small l."},
        ],
        "figure": None,
    },
    {
        "id": "c2-04-s02",
        "band": "standard",
        "text": "Carbon is C and calcium is Ca. Why did calcium not get the "
                "single letter C?",
        "options": [
            {"text": "Because calcium's name is longer, and longer names get "
                     "longer symbols.",
             "correct": False,
             "why": "Length has nothing to do with it. Hydrogen is a long "
                    "word with a one-letter symbol, and iron is a short one "
                    "with two."},
            {"text": "Because calcium is a metal, and metals are given two "
                     "letters.",
             "correct": False,
             "why": "Potassium is a metal and its symbol is K. Calcium's "
                    "second letter is about a clash, not about being a metal."},
            {"text": "Because Ca comes from an older Latin name rather than "
                     "from calcium.",
             "correct": False,
             "why": "Ca is taken straight from the English word calcium. The "
                    "Latin ones in this lesson are Na, Fe, Pb and Au."},
            {"text": "Because carbon had C first, so calcium takes the first "
                     "two letters of its name.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c2-04-s03",
        "band": "standard",
        "text": "Chlorine's symbol is Cl, not Ch. A student concludes that a "
                "two-letter symbol is always the first two letters of the "
                "name. What is wrong with that?",
        "options": [
            {"text": "Cl is the first letter and the third — and so is Mg. "
                     "The rule is looser than it looks.",
             "correct": True},
            {"text": "Nothing is wrong — Ch is the real symbol and Cl is just "
                     "how it gets printed.",
             "correct": False,
             "why": "Ch is not chlorine's symbol anywhere. Cl is, and it skips "
                    "the h: a second letter does not have to be the second "
                    "letter of the name."},
            {"text": "Two-letter symbols always come from Latin, so the "
                     "English name never matters.",
             "correct": False,
             "why": "Ca, Cl and Mg are all built from their English names. "
                    "Only some two-letter symbols are Latin — Na, Fe, Pb, Au."},
            {"text": "The rule holds; chlorine is the single exception in the "
                     "whole periodic table.",
             "correct": False,
             "why": "Magnesium does the same thing in this lesson: Ma would "
                    "have clashed, so Mg uses the first and third. It is a "
                    "pattern, not a one-off."},
        ],
        "figure": None,
    },
    {
        "id": "c2-04-s04",
        "band": "standard",
        "text": "Water is written H₂O. How many different elements is that, "
                "and what is the small 2 doing?",
        "options": [
            {"text": "Three elements — the H, the 2 and the O each count as "
                     "one.",
             "correct": False,
             "why": "A number is never an element. Only capital letters start "
                    "elements, and there are two capitals here."},
            {"text": "One element, because the formula names one single "
                     "substance.",
             "correct": False,
             "why": "One substance, yes — but built from two elements. H and "
                    "O are two capitals, so two kinds of atom."},
            {"text": "Two elements, hydrogen and oxygen. The 2 is a count, "
                     "not an element.",
             "correct": True},
            {"text": "Two elements, and the 2 says the water is twice as "
                     "strong.",
             "correct": False,
             "why": "Small numbers count atoms inside the formula, like the 3 "
                    "in CaCO₃. They say nothing about how strong or weak "
                    "anything is."},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "c2-04-h01",
        "band": "harder",
        "text": "You open a chemistry textbook in a language you cannot read "
                "and find CuO in a table. Without translating a single word, "
                "what can you say for certain?",
        "options": [
            {"text": "Nothing — a book in another language will use that "
                     "country's own symbols.",
             "correct": False,
             "why": "That is exactly what symbols prevent. CuO means the same "
                    "thing in Osaka, Lagos and São Paulo; only the words "
                    "around it change."},
            {"text": "That it names three elements, one for each letter in "
                     "it.",
             "correct": False,
             "why": "The lower-case u belongs to the C in front of it. Two "
                    "capitals, two elements — Cu and O."},
            {"text": "That it is copper on its own, since Cu is the only bit "
                     "you recognise.",
             "correct": False,
             "why": "The O is a second capital, so a second element: oxygen. "
                    "Copper on its own would be written Cu and nothing else."},
            {"text": "That it names two elements, because it has two capital "
                     "letters.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c2-04-h02",
        "band": "harder",
        "text": "A historian is listing the metals that Bronze Age smiths "
                "could already work. Judging by the symbols alone, which set "
                "would you expect that list to be full of?",
        "options": [
            {"text": "Fe, Pb, Au, Cu — symbols you cannot get from the "
                     "English name at all.",
             "correct": True},
            {"text": "H, C, N, O — the one-letter symbols, because they are "
                     "the simplest.",
             "correct": False,
             "why": "A one-letter symbol only means nobody had claimed that "
                    "letter yet. It says nothing about how long people have "
                    "known the element."},
            {"text": "Ca, Mg, Cl — two-letter symbols taken from the English "
                     "name.",
             "correct": False,
             "why": "Two letters on its own is not the clue. The giveaway is "
                    "a symbol whose letters are not in the English name, "
                    "because that means it is Latin and therefore ancient."},
            {"text": "A mixture — a symbol tells you nothing about when an "
                     "element was found.",
             "correct": False,
             "why": "A symbol that looks wrong is usually a fossil. The Latin "
                    "ones — gold, iron, lead, copper, sodium, potassium — are "
                    "the elements people had worked for thousands of years."},
        ],
        "figure": None,
    },
    {
        "id": "c2-04-h03",
        "band": "harder",
        "text": "Alchemists wrote silver as a crescent and gold as a circle "
                "with a dot, and kept their notation deliberately obscure. "
                "Berzelius replaced the pictures with letters from the Latin "
                "names in 1813. Why did that change chemistry rather than "
                "just tidy it?",
        "options": [
            {"text": "Letters are faster to put on paper than a drawing, so "
                     "chemists got more done.",
             "correct": False,
             "why": "Saving effort is the least of it. What changed was that "
                    "someone else could read the notes afterwards."},
            {"text": "Latin was the language everyone in Europe spoke in "
                     "1813, so everyone could follow it.",
             "correct": False,
             "why": "The symbols work precisely because you do not need "
                    "Latin — or English, or Japanese. Na means sodium to "
                    "someone who has never met the word natrium."},
            {"text": "Anyone could read and copy a result, so chemistry "
                     "could be shared and checked.",
             "correct": True},
            {"text": "The pictures were ambiguous, so alchemists kept "
                     "confusing silver with gold.",
             "correct": False,
             "why": "Their pictures were clear enough to them — they were "
                    "kept obscure on purpose, so rivals could not read them. "
                    "The problem was secrecy, not confusion."},
        ],
        "figure": None,
    },
    {
        "id": "c2-04-h04",
        "band": "harder",
        "text": "In German, sodium chloride is Natriumchlorid; in French it "
                "is chlorure de sodium. Both are written NaCl. What does the "
                "German word tell you about the symbol Na?",
        "options": [
            {"text": "That German chemists chose the symbol, so it follows "
                     "the German word.",
             "correct": False,
             "why": "No country owns a symbol. German kept the old name, "
                    "English swapped to sodium, and the symbol stayed where "
                    "it started — with natrium."},
            {"text": "That natrium, the old Latin name, survives in some "
                     "languages — and Na comes from it.",
             "correct": True},
            {"text": "That Na is the German symbol, and English chemists "
                     "write So instead.",
             "correct": False,
             "why": "There is one symbol per element, in every language — "
                    "that is the whole reason symbols exist. So is not sodium "
                    "anywhere."},
            {"text": "That Na is the first and third letters of sodium, and "
                     "the German word is a coincidence.",
             "correct": False,
             "why": "The first and third letters of sodium are s and d. The "
                    "first-and-third trick belongs to Mg and Cl; Na is not "
                    "built from the English name at all."},
        ],
        "figure": None,
    },
]
