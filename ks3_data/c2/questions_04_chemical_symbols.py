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

    # ── easier · MRB-335 top-up ─────────────────────────────────────────
    {
        "id": "c2-04-e05",
        "band": "easier",
        "text": "What is a chemical symbol?",
        "options": [
            {"text": "The short set of letters and numbers that says which "
                     "elements are in a substance and how many of each",
             "correct": False,
             "why": "That is a formula. A formula is built out of symbols, "
                    "but it is not one"},
            {"text": "The number that says where an element sits on the "
                     "periodic table",
             "correct": False,
             "why": "That is its number, not its symbol. The symbol is the "
                    "letters"},
            {"text": "A shortened version of an element's English name",
             "correct": False,
             "why": "Sometimes it looks like that, and Fe, Na, Pb, Au and Cu "
                    "show it is not the rule"},
            {"text": "The one or two letters that stand for an element",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c2-04-e06",
        "band": "easier",
        "text": "A chemical symbol has two letters. What must be true of the "
                "second one?",
        "options": [
            {"text": "It must be lower case",
             "correct": True},
            {"text": "It must be a capital, so that the symbol is easy to "
                     "pick out in the middle of a long formula",
             "correct": False,
             "why": "A capital always starts a NEW element, so a second "
                    "capital would split the symbol into two"},
            {"text": "It must be the second letter of the element's name",
             "correct": False,
             "why": "Chlorine is Cl and magnesium is Mg — both use the first "
                    "letter and the third. The rule is looser than that"},
            {"text": "It must be a vowel",
             "correct": False,
             "why": "Mg, Cl and Zn all have a consonant there. Nothing about "
                    "the rule mentions vowels"},
        ],
        "figure": None,
    },
    {
        "id": "c2-04-e07",
        "band": "easier",
        "text": "Which of these is the correct symbol for sodium?",
        "options": [
            {"text": "So",
             "correct": False,
             "why": "That is the name shortened, which is exactly what a "
                    "symbol need not be. Sodium's comes from natrium"},
            {"text": "Na",
             "correct": True},
            {"text": "NA",
             "correct": False,
             "why": "Two capitals means two elements. This says nitrogen "
                    "followed by something starting with A"},
            {"text": "Sd",
             "correct": False,
             "why": "Invented from the English name. No element has this "
                    "symbol"},
        ],
        "figure": None,
    },
    {
        "id": "c2-04-e08",
        "band": "easier",
        "text": "Gold's symbol is Au. Where do those letters come from?",
        "options": [
            {"text": "From the first and last letters of the English name, a "
                     "rule used whenever the first two are already taken",
             "correct": False,
             "why": "There is no such rule, and gold has neither an a nor a u "
                    "in it. Au comes from a different language"},
            {"text": "From the name of the chemist who first purified it",
             "correct": False,
             "why": "No symbol is taken from a person's name in this way. "
                    "The odd-looking ones are Latin"},
            {"text": "From aurum, an older name for gold",
             "correct": True},
            {"text": "From the Australian mines where most of it was found",
             "correct": False,
             "why": "Gold has been worked for thousands of years, long "
                    "before those mines. The letters are Latin"},
        ],
        "figure": None,
    },
    {
        "id": "c2-04-e09",
        "band": "easier",
        "text": "What is a formula?",
        "options": [
            {"text": "The one or two letters that stand for a single element",
             "correct": False,
             "why": "That is a symbol. A formula is what you get when symbols "
                    "and numbers are written together"},
            {"text": "The list of every element a substance could be broken "
                     "down into",
             "correct": False,
             "why": "A formula gives counts as well as names, and the order "
                    "is not the table's"},
            {"text": "The recipe for making a substance in a laboratory",
             "correct": False,
             "why": "A formula says what the substance IS, not how to make "
                    "it"},
            {"text": "Symbols written together, saying which elements are in "
                     "a substance and how many atoms of each",
             "correct": True},
        ],
        "figure": None,
    },

    # ── standard · MRB-335 top-up ───────────────────────────────────────
    {
        "id": "c2-04-s05",
        "band": "standard",
        "text": "A student says a symbol is simply the element's English name "
                "shortened. Which pair of symbols shows that is wrong?",
        "options": [
            {"text": "Mg and Cl, because neither of them uses the first two "
                     "letters of the name it belongs to",
             "correct": False,
             "why": "Both are still taken from the English name, just not "
                    "from its first two letters. Something stronger is "
                    "needed"},
            {"text": "H and C",
             "correct": False,
             "why": "Both are exactly the first letter of the English name, "
                    "so they support the student rather than refuting them"},
            {"text": "Ca and Cl",
             "correct": False,
             "why": "Both come from the English names calcium and chlorine. "
                    "Neither is a counter-example"},
            {"text": "Fe and Na",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c2-04-s06",
        "band": "standard",
        "text": "Four students write the formula of magnesium oxide. Which "
                "one has written it correctly?",
        "options": [
            {"text": "MgO",
             "correct": True},
            {"text": "MGO",
             "correct": False,
             "why": "Three capitals, so three elements. It says magnesium is "
                    "not there at all and names something beginning with G "
                    "instead"},
            {"text": "mgo",
             "correct": False,
             "why": "No capital at all, so nothing starts an element. The "
                    "case is not decoration"},
            {"text": "Mgo",
             "correct": False,
             "why": "One capital, so one element — and Mgo is not an element. "
                    "The oxygen has been swallowed by the magnesium"},
        ],
        "figure": None,
    },
    {
        "id": "c2-04-s07",
        "band": "standard",
        "text": "No two elements are allowed to share a symbol. Why does that "
                "matter so much?",
        "options": [
            {"text": "Because the periodic table is arranged in alphabetical "
                     "order of symbol, and a repeat would leave two elements "
                     "with one place",
             "correct": False,
             "why": "The table is not in alphabetical order at all. The "
                    "reason is about reading formulae, not about the "
                    "layout"},
            {"text": "Because a formula has to name exactly one substance, "
                     "whoever reads it and whatever language they speak",
             "correct": True},
            {"text": "Because there are only enough letters for about a "
                     "hundred elements",
             "correct": False,
             "why": "Two letters give hundreds of combinations. Running out "
                    "is not the problem"},
            {"text": "Because chemists would otherwise argue about who chose "
                     "it first",
             "correct": False,
             "why": "The reason is practical rather than about credit: a "
                    "shared symbol would make a formula ambiguous"},
        ],
        "figure": None,
    },
    {
        "id": "c2-04-s08",
        "band": "standard",
        "text": "A packet of baking soda gives its contents as NaHCO₃. How "
                "many different elements does that name?",
        "options": [
            {"text": "Three",
             "correct": False,
             "why": "The lower-case a does belong to the N, but H and C and O "
                    "are three more capitals. Count the capitals and you get "
                    "four"},
            {"text": "Five",
             "correct": False,
             "why": "The 3 is a count of oxygen atoms, not an element. Only "
                    "capital letters start elements"},
            {"text": "Four",
             "correct": True},
            {"text": "Six",
             "correct": False,
             "why": "Lower-case letters belong to the capital in front of "
                    "them, and numbers are counts"},
        ],
        "figure": None,
    },
    {
        "id": "c2-04-s09",
        "band": "standard",
        "text": "In a formula, which part tells you how many ATOMS there are "
                "rather than how many elements?",
        "options": [
            {"text": "The capital letters, since one capital always stands "
                     "for one atom of the element it begins",
             "correct": False,
             "why": "A capital counts elements, not atoms. One capital can "
                    "have any small number after it"},
            {"text": "The lower-case letters",
             "correct": False,
             "why": "A lower-case letter is part of a symbol. It counts "
                    "nothing at all"},
            {"text": "The order the symbols are written in",
             "correct": False,
             "why": "The order says nothing about how many. It is a "
                    "convention about how the formula is set out"},
            {"text": "The small numbers",
             "correct": True},
        ],
        "figure": None,
    },

    # ── harder · MRB-335 top-up ─────────────────────────────────────────
    {
        "id": "c2-04-h05",
        "band": "harder",
        "text": "A table in a book you cannot read lists CoO. Reading only "
                "the letters, what does it name?",
        "options": [
            {"text": "Carbon and two oxygens, because the lower-case o counts "
                     "a second oxygen atom after the capital one",
             "correct": False,
             "why": "A lower-case letter is never a count. It belongs to the "
                    "capital in front of it, making Co"},
            {"text": "Carbon and oxygen",
             "correct": False,
             "why": "Carbon on its own is C. The lower-case o joins it into "
                    "Co, which is cobalt"},
            {"text": "Three elements, one for each letter",
             "correct": False,
             "why": "Only capitals start elements, and there are two of "
                    "them"},
            {"text": "Cobalt and oxygen",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c2-04-h06",
        "band": "harder",
        "text": "A new element needs a symbol and Fe, Nh and N are all "
                "already taken. Which proposal obeys the rule and is still "
                "free?",
        "options": [
            {"text": "Nq",
             "correct": True},
            {"text": "nh, which uses letters nobody has claimed in that order "
                     "and is easy to tell apart from Nh at a glance",
             "correct": False,
             "why": "The first letter must be a capital. Lower case at the "
                    "start starts no element at all"},
            {"text": "NH",
             "correct": False,
             "why": "Two capitals, so this reads as two elements — nitrogen "
                    "and hydrogen — rather than one new one"},
            {"text": "Fe",
             "correct": False,
             "why": "Already iron's. No two elements may share a symbol, "
                    "which is the whole point of the system"},
        ],
        "figure": None,
    },
    {
        "id": "c2-04-h07",
        "band": "harder",
        "text": "Sodium's compounds have been called soda for centuries, and "
                "its symbol is Na. What connects those two facts?",
        "options": [
            {"text": "Both come from the English word sodium, which was "
                     "shortened one way for the symbol and another way for "
                     "the everyday name",
             "correct": False,
             "why": "Neither comes from the English name. Soda and Na are "
                    "both older than it"},
            {"text": "Both come from natrium, an older name for the element",
             "correct": True},
            {"text": "Soda is a compound of sodium, so it took the first two "
                     "letters of the symbol",
             "correct": False,
             "why": "The word came first and the symbol was chosen to match "
                    "it, both from the same older name"},
            {"text": "It is a coincidence — the letters happen to line up",
             "correct": False,
             "why": "The shared root natrium is exactly why they line up. "
                    "Nothing here is accidental"},
        ],
        "figure": None,
    },
    {
        "id": "c2-04-h08",
        "band": "harder",
        "text": "A student proposes writing cobalt as Cob and carbon "
                "monoxide as CarMon, arguing that it would be clearer. What "
                "does the real notation do that theirs could not?",
        "options": [
            {"text": "It would take up less room on a page, which matters "
                     "when a long formula has to be fitted into a table or "
                     "onto a label",
             "correct": False,
             "why": "Being shorter is a convenience. It is not the reason the "
                    "one- or two-letter rule exists"},
            {"text": "It makes every symbol match its English name exactly, "
                     "so a reader who knows the name can write the symbol "
                     "straight off",
             "correct": False,
             "why": "The opposite: several symbols come from Latin and do not "
                    "match the English name at all"},
            {"text": "It lets symbols be strung into a formula that can be "
                     "read apart again, because a capital always starts a new "
                     "element",
             "correct": True},
            {"text": "It stops two elements being confused with each other, "
                     "which longer names like Cob and CarMon could not do",
             "correct": False,
             "why": "Cob and CarMon would be distinguishable too. What they "
                    "could not do is be strung together and read back"},
        ],
        "figure": None,
    },
    {
        "id": "c2-04-h09",
        "band": "harder",
        "text": "How many atoms altogether are there in one particle of "
                "NaHCO₃?",
        "options": [
            {"text": "Four",
             "correct": False,
             "why": "Four is the number of ELEMENTS. The small 3 means three "
                    "oxygen atoms rather than one"},
            {"text": "Seven",
             "correct": False,
             "why": "The a belongs to the N, making sodium. It counts "
                    "nothing"},
            {"text": "Three",
             "correct": False,
             "why": "A symbol with no number after it already means one atom. "
                    "Na, H and C are one each"},
            {"text": "Six",
             "correct": True},
        ],
        "figure": None,
    },

    # ── easier · MRB-338 night 3 ────────────────────────────────────────
    {
        "id": "c2-04-e10",
        "band": "easier",
        "text": "Which of these is written the way a chemical symbol has to "
                "be written?",
        "options": [
            {"text": "CU",
             "correct": False,
             "why": "Two capitals, so this reads as two elements rather than "
                    "one"},
            {"text": "cu",
             "correct": False,
             "why": "No capital at all, so nothing here starts an element"},
            {"text": "Cu",
             "correct": True},
            {"text": "cU",
             "correct": False,
             "why": "The capital has to come first. A lower-case letter never "
                    "opens a symbol"},
        ],
        "figure": None,
    },
    {
        "id": "c2-04-e11",
        "band": "easier",
        "text": "How many letters is a chemical symbol allowed to have?",
        "options": [
            {"text": "One or two",
             "correct": True},
            {"text": "Exactly two, so every symbol takes the same space",
             "correct": False,
             "why": "Hydrogen is H and carbon is C, one letter each, and both "
                    "are correct"},
            {"text": "Two or three, depending on the name",
             "correct": False,
             "why": "No symbol runs to three letters. One or two is the whole "
                    "rule"},
            {"text": "As many as the element's name needs",
             "correct": False,
             "why": "A symbol is not the name written out. Sodium's is Na, two "
                    "letters for a six-letter word"},
        ],
        "figure": None,
    },
    {
        "id": "c2-04-e12",
        "band": "easier",
        "text": "A person who fits water pipes is called a plumber. Which "
                "element's older name is that word built from?",
        "options": [
            {"text": "Iron, whose older name is ferrum",
             "correct": False,
             "why": "Ferrum gives iron the symbol Fe, and gives English the "
                    "word farrier rather than plumber"},
            {"text": "Copper, whose older name is cuprum",
             "correct": False,
             "why": "Cuprum gives copper the symbol Cu. The pipes the word "
                    "comes from were not copper ones"},
            {"text": "Lead, whose older name is plumbum",
             "correct": True},
            {"text": "Tin, whose symbol comes from its English name",
             "correct": False,
             "why": "Tin's symbol is Sn, which is not from English either, and "
                    "no English word is built on it"},
        ],
        "figure": None,
    },
    {
        "id": "c2-04-e13",
        "band": "easier",
        "text": "The symbol Co stands for which element?",
        "options": [
            {"text": "Carbon",
             "correct": False,
             "why": "Carbon is C on its own. A lower-case o after it makes a "
                    "different symbol"},
            {"text": "Cobalt",
             "correct": True},
            {"text": "Copper",
             "correct": False,
             "why": "Copper is Cu. Co and Cu belong to two different elements"},
            {"text": "Carbon monoxide",
             "correct": False,
             "why": "That is CO, two capitals and two elements joined. Co is a "
                    "single element"},
        ],
        "figure": None,
    },
    {
        "id": "c2-04-e14",
        "band": "easier",
        "text": "Where would you look up the symbol of an element you had "
                "never met before?",
        "options": [
            {"text": "The periodic table",
             "correct": True},
            {"text": "A dictionary",
             "correct": False,
             "why": "A dictionary gives you the element's name, and several "
                    "names share no letters with their symbol"},
            {"text": "The formula of a compound it is in",
             "correct": False,
             "why": "A formula is written in symbols already, so you would "
                    "need the symbol before you could read it"},
            {"text": "Its Latin name, cut to two letters",
             "correct": False,
             "why": "That works for a handful of elements and fails for most "
                    "of them"},
        ],
        "figure": None,
    },
    {
        "id": "c2-04-e15",
        "band": "easier",
        "text": "The first letter of a chemical symbol is written in which "
                "case?",
        "options": [
            {"text": "Lower case, leaving capitals free for formulae",
             "correct": False,
             "why": "Capitals are what a formula is built from: each one opens "
                    "a symbol"},
            {"text": "Whichever case the element's own name uses",
             "correct": False,
             "why": "Element names are written in lower case in a sentence, "
                    "and their symbols still open with a capital"},
            {"text": "A capital for a metal, lower case for a non-metal",
             "correct": False,
             "why": "Chlorine is a non-metal and its symbol is Cl. The rule "
                    "has nothing to do with metals"},
            {"text": "A capital, every time",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c2-04-e16",
        "band": "easier",
        "text": "Why can you tell how many elements a formula names without "
                "knowing any chemistry at all?",
        "options": [
            {"text": "Because every capital letter in it opens a new element",
             "correct": True},
            {"text": "Because the symbols are set out in alphabetical order",
             "correct": False,
             "why": "They are not. Chemists write a formula in a fixed order "
                    "that has nothing to do with the alphabet"},
            {"text": "Because a number separates each element from the next",
             "correct": False,
             "why": "Plenty of formulae carry no numbers, and CO names two "
                    "elements without one"},
            {"text": "Because each element takes exactly one letter",
             "correct": False,
             "why": "Many take two — Na, Fe, Mg, Cl — so counting letters "
                    "gives the wrong answer"},
        ],
        "figure": None,
    },
    {
        "id": "c2-04-e17",
        "band": "easier",
        "text": "Which element does the symbol Fe stand for?",
        "options": [
            {"text": "Fluorine",
             "correct": False,
             "why": "Fluorine is F, a single letter. Adding a lower-case e "
                    "names a different element"},
            {"text": "Francium",
             "correct": False,
             "why": "Francium is Fr. The second letter decides which element a "
                    "symbol belongs to"},
            {"text": "Iron",
             "correct": True},
            {"text": "Iron oxide",
             "correct": False,
             "why": "That is a compound, and a compound needs more than one "
                    "symbol to write it"},
        ],
        "figure": None,
    },
    {
        "id": "c2-04-e18",
        "band": "easier",
        "text": "Potassium's symbol is K, and there is no k in the word "
                "potassium. Where does the letter come from?",
        "options": [
            {"text": "From kalium, an older name for the element",
             "correct": True},
            {"text": "From the German name for the element",
             "correct": False,
             "why": "No living language settles a symbol. K is the first "
                    "letter of kalium"},
            {"text": "From the mineral it was first taken from",
             "correct": False,
             "why": "Symbols are not named after minerals. K stands for "
                    "kalium"},
            {"text": "From the only letter nobody else had claimed",
             "correct": False,
             "why": "Letters are not handed out from whatever is left over. K "
                    "is kalium's first letter"},
        ],
        "figure": None,
    },
    {
        "id": "c2-04-e19",
        "band": "easier",
        "text": "Which of these is the symbol for carbon?",
        "options": [
            {"text": "Ca",
             "correct": False,
             "why": "That is calcium. Carbon had the single letter C first, so "
                    "calcium took two"},
            {"text": "C",
             "correct": True},
            {"text": "Cn",
             "correct": False,
             "why": "A lower-case n after the C makes a different symbol "
                    "belonging to a different element"},
            {"text": "Cb",
             "correct": False,
             "why": "Carbon is a single capital C, with no second letter at "
                    "all"},
        ],
        "figure": None,
    },
    {
        "id": "c2-04-e20",
        "band": "easier",
        "text": "Magnesium's symbol is Mg. Which letter of the word magnesium "
                "is that g?",
        "options": [
            {"text": "The second",
             "correct": False,
             "why": "The second letter is an a. Ma was not free, so the g was "
                    "taken instead"},
            {"text": "The third",
             "correct": True},
            {"text": "The last",
             "correct": False,
             "why": "The last letter is m. No symbol is built from the end of "
                    "a name"},
            {"text": "It does not appear in the word at all",
             "correct": False,
             "why": "It does — magnesium has a g third. Pb is the symbol with "
                    "no letters from its English name"},
        ],
        "figure": None,
    },
    {
        "id": "c2-04-e21",
        "band": "easier",
        "text": "An element is called sodium in English and natrium in "
                "German. What happens to its symbol at the border?",
        "options": [
            {"text": "It stays Na",
             "correct": True},
            {"text": "It changes to match whichever name is being used",
             "correct": False,
             "why": "A symbol belongs to the element rather than to a "
                    "language, so it does not change at a border"},
            {"text": "Each country writes its own version of it",
             "correct": False,
             "why": "There is one symbol per element everywhere, which is the "
                    "reason symbols were agreed"},
            {"text": "It is Na in German and So in English",
             "correct": False,
             "why": "So is not sodium's symbol anywhere. Na comes from natrium "
                    "and is used in every country"},
        ],
        "figure": None,
    },
    {
        "id": "c2-04-e22",
        "band": "easier",
        "text": "Copper's symbol Cu comes from an older name, cuprum. What "
                "does a symbol like that tell you about an element?",
        "options": [
            {"text": "That people had been working with it for thousands of "
                     "years",
             "correct": True},
            {"text": "That a Roman chemist was the first to purify it",
             "correct": False,
             "why": "Nobody in Rome purified elements. The Latin survives "
                    "because the metal was already in use"},
            {"text": "That it is rarer than the elements with English symbols",
             "correct": False,
             "why": "Copper, iron and lead are among the commonest metals in "
                    "use. Rarity decides nothing here"},
            {"text": "That its English name is too long to shorten",
             "correct": False,
             "why": "Copper is a short word. The symbol is old rather than "
                    "short"},
        ],
        "figure": None,
    },
    {
        "id": "c2-04-e23",
        "band": "easier",
        "text": "Which of these symbols uses letters that appear nowhere in "
                "the element's English name?",
        "options": [
            {"text": "Ca, for calcium",
             "correct": False,
             "why": "Both letters are the first two of calcium, so nothing is "
                    "borrowed from elsewhere"},
            {"text": "Cl, for chlorine",
             "correct": False,
             "why": "Both letters are in chlorine — the first and the third. "
                    "It skips a letter, it does not import one"},
            {"text": "Pb, for lead",
             "correct": True},
            {"text": "Mg, for magnesium",
             "correct": False,
             "why": "Both letters are in magnesium, the first and the third, "
                    "exactly as chlorine's are"},
        ],
        "figure": None,
    },
    {
        "id": "c2-04-e24",
        "band": "easier",
        "text": "Hydrogen's symbol is a single letter, H. Why did it get one "
                "letter when magnesium needs two?",
        "options": [
            {"text": "No other element had claimed H",
             "correct": True},
            {"text": "Hydrogen is the lightest element, and the lightest "
                     "elements are the ones given a single letter",
             "correct": False,
             "why": "Mass decides nothing. Lead is heavy and takes two "
                    "letters; carbon is light and takes one"},
            {"text": "Hydrogen is a gas, and gases take one letter",
             "correct": False,
             "why": "Chlorine is a gas and takes two. Being a gas has nothing "
                    "to do with it"},
            {"text": "Hydrogen was discovered first",
             "correct": False,
             "why": "Gold and lead were known long before hydrogen, and both "
                    "take two letters"},
        ],
        "figure": None,
    },
    {
        "id": "c2-04-e25",
        "band": "easier",
        "text": "In a formula, the small numbers written low down are not "
                "elements. What are they?",
        "options": [
            {"text": "Counts of elements",
             "correct": False,
             "why": "Elements are counted by the capital letters instead"},
            {"text": "Counts of atoms",
             "correct": True},
            {"text": "The order the elements react in",
             "correct": False,
             "why": "A formula records what is in a substance, never what "
                    "happens to it"},
            {"text": "Their places on the periodic table",
             "correct": False,
             "why": "An element's place on the table is never written into a "
                    "formula"},
        ],
        "figure": None,
    },
    {
        "id": "c2-04-e26",
        "band": "easier",
        "text": "A student writes cobalt's symbol as co. What is wrong with "
                "it?",
        "options": [
            {"text": "The first letter must be a capital",
             "correct": True},
            {"text": "The second letter must be a capital too",
             "correct": False,
             "why": "A second capital opens a second element, turning one "
                    "symbol into two"},
            {"text": "Cobalt's symbol has three letters",
             "correct": False,
             "why": "No symbol has three letters. Cobalt's is Co"},
            {"text": "Nothing is wrong, since case is only a style choice",
             "correct": False,
             "why": "Case is the whole notation. Co, CO and co say three "
                    "different things"},
        ],
        "figure": None,
    },
    {
        "id": "c2-04-e27",
        "band": "easier",
        "text": "One chemical symbol stands for how many elements?",
        "options": [
            {"text": "Exactly one",
             "correct": True},
            {"text": "One, unless two elements have similar names",
             "correct": False,
             "why": "Similar names are why second letters exist. No two "
                    "elements share a symbol"},
            {"text": "Any number, since the formula makes it clear",
             "correct": False,
             "why": "A formula can be read apart precisely because each symbol "
                    "means one element"},
            {"text": "One in each language it is used in",
             "correct": False,
             "why": "The same symbol means the same element everywhere, which "
                    "is the reason for having symbols"},
        ],
        "figure": None,
    },
    {
        "id": "c2-04-e28",
        "band": "easier",
        "text": "How many different elements does the formula ZnO name?",
        "options": [
            {"text": "One",
             "correct": False,
             "why": "One element would mean one capital. There are two here"},
            {"text": "Two",
             "correct": True},
            {"text": "Three",
             "correct": False,
             "why": "The lower-case n belongs to the Z, so Zn is one symbol "
                    "rather than two"},
            {"text": "It depends on how much of it there is",
             "correct": False,
             "why": "A formula says what a substance is, never how much of it "
                    "you have"},
        ],
        "figure": None,
    },
    {
        "id": "c2-04-e29",
        "band": "easier",
        "text": "What is the periodic table?",
        "options": [
            {"text": "The list of all the known elements, each with its name "
                     "and its symbol",
             "correct": True},
            {"text": "A list of every compound chemists have made, with the "
                     "formula and the melting point of each one",
             "correct": False,
             "why": "Compounds are not on it. It lists the elements compounds "
                    "are built from"},
            {"text": "A table of the formulae of common substances, arranged "
                     "by how many atoms each one contains",
             "correct": False,
             "why": "Formulae are not listed on it. It gives each element a "
                    "name and a symbol"},
            {"text": "A list of the symbols still free for chemists to give "
                     "to any element discovered from now on",
             "correct": False,
             "why": "It shows the symbols that are taken. A free symbol is one "
                    "that is absent from it"},
        ],
        "figure": None,
    },
    {
        "id": "c2-04-e30",
        "band": "easier",
        "text": "Before 1813 alchemists drew silver as a crescent and gold as "
                "a circle with a dot. What did Berzelius put in their place?",
        "options": [
            {"text": "Numbers, one for each element",
             "correct": False,
             "why": "An element is not written as a number. He chose letters"},
            {"text": "Simpler pictures that anyone could copy",
             "correct": False,
             "why": "He dropped pictures altogether, because letters can be "
                    "written and printed by anybody"},
            {"text": "Letters taken from the elements' Latin names",
             "correct": True},
            {"text": "Names spelled out in full in Latin",
             "correct": False,
             "why": "Spelling names out is what the symbols replaced. He used "
                    "one or two letters"},
        ],
        "figure": None,
    },

    # ── standard · MRB-338 night 3 ──────────────────────────────────────
    {
        "id": "c2-04-s10",
        "band": "standard",
        "text": "Tungsten's symbol is W, and there is no w anywhere in the "
                "word tungsten. What is the most likely reason?",
        "options": [
            {"text": "The symbol comes from an older name for the metal, "
                     "wolfram",
             "correct": True},
            {"text": "W was the only letter still unclaimed when tungsten was "
                     "named",
             "correct": False,
             "why": "Symbols are not handed out from the letters left over. "
                    "The odd ones are old names"},
            {"text": "The English name was changed after the symbol had been "
                     "fixed",
             "correct": False,
             "why": "Tungsten has been tungsten in English throughout. It is "
                    "the symbol that is from elsewhere"},
            {"text": "It is a printing error that was never put right",
             "correct": False,
             "why": "Every table prints W. A symbol in use worldwide is not a "
                    "mistake nobody noticed"},
        ],
        "figure": None,
    },
    {
        "id": "c2-04-s11",
        "band": "standard",
        "text": "Tin's symbol is Sn, taken from an older name, stannum. What "
                "does that suggest about tin?",
        "options": [
            {"text": "It is a rare metal, and rare metals were always named "
                     "late in the language's history",
             "correct": False,
             "why": "Rarity has nothing to do with it, and tin is not "
                    "especially rare"},
            {"text": "People were working with it long before English "
                     "existed",
             "correct": True},
            {"text": "It was named by the chemist who first isolated and "
                     "purified it in a laboratory",
             "correct": False,
             "why": "Nobody discovered tin. It was in use for thousands of "
                    "years before chemistry began"},
            {"text": "Its English name was too short to make a usable "
                     "one- or two-letter symbol",
             "correct": False,
             "why": "Three letters is plenty. Carbon manages on one, and the "
                    "length of a name settles nothing"},
        ],
        "figure": None,
    },
    {
        "id": "c2-04-s12",
        "band": "standard",
        "text": "How many different elements does the formula FeS2 name, and "
                "how can you be sure?",
        "options": [
            {"text": "Two, because there are two capital letters",
             "correct": True},
            {"text": "Three, because there are three characters that are not "
                     "the lower-case e",
             "correct": False,
             "why": "The 2 is a count, not an element, and only capitals open "
                    "an element"},
            {"text": "Four, because there are four characters altogether",
             "correct": False,
             "why": "Characters are not elements. Two of these four are a "
                    "lower-case letter and a number"},
            {"text": "Two, because the 2 says how many kinds of atom there "
                     "are",
             "correct": False,
             "why": "The right answer by the wrong route: the 2 counts sulfur "
                    "atoms, and the capitals count elements"},
        ],
        "figure": None,
    },
    {
        "id": "c2-04-s13",
        "band": "standard",
        "text": "Sodium and sulfur are both English names, but only one of "
                "those two elements has a symbol built from its English name. "
                "Which, and why?",
        "options": [
            {"text": "Sodium, because Na is made from its first and third "
                     "letters read together",
             "correct": False,
             "why": "Sodium's first and third letters are s and d. Na has no "
                    "letters from the English word at all"},
            {"text": "Sulfur, because S is its first letter and sodium's Na "
                     "comes from natrium",
             "correct": True},
            {"text": "Both, because every symbol in the periodic table starts "
                     "from the element's English name",
             "correct": False,
             "why": "Several do not. Na, Fe, Pb, Au and Cu are all taken from "
                    "older names instead"},
            {"text": "Neither, because both symbols come from an older name "
                     "for the element rather than the modern English one",
             "correct": False,
             "why": "Sulfur's S is simply the first letter of the English "
                    "word, which was free"},
        ],
        "figure": None,
    },
    {
        "id": "c2-04-s14",
        "band": "standard",
        "text": "A student proposes rewriting every symbol so that it matches "
                "the element's English name. Which elements would have to "
                "change?",
        "options": [
            {"text": "The one-letter ones, which are too short to match a "
                     "name",
             "correct": False,
             "why": "H, C, O and N already open their English names. They need "
                    "no change at all"},
            {"text": "The two-letter ones, since one letter is enough for "
                     "anything",
             "correct": False,
             "why": "One letter is not enough: carbon, calcium and chlorine "
                    "would all want C"},
            {"text": "None, because every symbol matches its name already",
             "correct": False,
             "why": "Na, K, Fe, Pb, Au and Cu share no letters with their "
                    "English names"},
            {"text": "The ones taken from older names — Na, K, Fe, Pb, Au and "
                     "Cu",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c2-04-s15",
        "band": "standard",
        "text": "A student says Na, Fe, Ca and Cu must all be metals because "
                "each of them has two letters. Where does that reasoning "
                "break?",
        "options": [
            {"text": "Chlorine is Cl, two letters, and it is a poisonous "
                     "gas",
             "correct": True},
            {"text": "Some metals have one-letter symbols, so the rule would "
                     "miss them",
             "correct": False,
             "why": "True of potassium, K — but it shows the rule is "
                    "incomplete, not that a two-letter symbol proves nothing"},
            {"text": "Two of those four are not really metals",
             "correct": False,
             "why": "Sodium, iron, calcium and copper are all metals. The "
                    "four examples are not the problem"},
            {"text": "A symbol has nothing to do with the element it names",
             "correct": False,
             "why": "It names exactly one element. What it cannot tell you is "
                    "whether that element is a metal"},
        ],
        "figure": None,
    },
    {
        "id": "c2-04-s16",
        "band": "standard",
        "text": "What single change to the symbol Mg would turn it into a "
                "claim about two elements?",
        "options": [
            {"text": "Making the g a capital",
             "correct": True},
            {"text": "Writing the M in lower case",
             "correct": False,
             "why": "That leaves no capital at all, so nothing opens an "
                    "element and the pair names none"},
            {"text": "Swapping the two letters round",
             "correct": False,
             "why": "gM still has one capital, so it still claims one element "
                    "— and it is not a symbol anybody uses"},
            {"text": "Adding a small 2 after it",
             "correct": False,
             "why": "A small number counts atoms of the element in front of "
                    "it. It adds no second element"},
        ],
        "figure": None,
    },
    {
        "id": "c2-04-s17",
        "band": "standard",
        "text": "Magnesium is Mg and manganese is Mn. What does that pair "
                "show about why second letters exist?",
        "options": [
            {"text": "They mark which of the two elements is a metal and "
                     "which one is a non-metal",
             "correct": False,
             "why": "Both are metals. A second letter does not report what "
                    "kind of element it is"},
            {"text": "They are needed whenever two elements would otherwise "
                     "claim the same first letter",
             "correct": True},
            {"text": "They show which of the two elements was found or named "
                     "earlier in the history of chemistry",
             "correct": False,
             "why": "Nothing in a symbol records a date. The second letter is "
                    "there to keep two names apart"},
            {"text": "They are added to any element whose name is longer than "
                     "six letters",
             "correct": False,
             "why": "Hydrogen has eight letters and a one-letter symbol. Name "
                    "length settles nothing"},
        ],
        "figure": None,
    },
    {
        "id": "c2-04-s18",
        "band": "standard",
        "text": "A label is printed as NaCL, with a capital L on the end. "
                "Reading only the letters, how many elements does that claim?",
        "options": [
            {"text": "Two, since NaCL and NaCl look near enough the same",
             "correct": False,
             "why": "Looking similar is not being the same. The capital L "
                    "opens an element of its own"},
            {"text": "One, because a run of capitals is read as one name",
             "correct": False,
             "why": "Capitals are never read as a name. Each one opens an "
                    "element"},
            {"text": "Three",
             "correct": True},
            {"text": "Four, one for each letter on the label",
             "correct": False,
             "why": "The lower-case a belongs to the N in front of it, so Na "
                    "is a single symbol"},
        ],
        "figure": None,
    },
    {
        "id": "c2-04-s19",
        "band": "standard",
        "text": "Carbon, calcium, chlorine, cobalt and copper all begin with "
                "c. Why can only one of them have the symbol C?",
        "options": [
            {"text": "Because a symbol has to name exactly one element, so "
                     "the other four take a second letter",
             "correct": True},
            {"text": "Because C was reserved by international agreement for "
                     "whichever of the five turned out to be most common",
             "correct": False,
             "why": "Nothing is reserved by how common an element is. Carbon "
                    "simply took the letter first"},
            {"text": "Because the other four are metals, and every metal's "
                     "symbol has to take two letters to show that",
             "correct": False,
             "why": "Chlorine is a gas and still takes two letters. Being a "
                    "metal is not the reason"},
            {"text": "Because a one-letter symbol is only ever given to a "
                     "non-metal, never to a metal",
             "correct": False,
             "why": "Potassium is a metal with the one-letter symbol K"},
        ],
        "figure": None,
    },
    {
        "id": "c2-04-s20",
        "band": "standard",
        "text": "Explain why the case of a letter in a formula is not a style "
                "choice.",
        "options": [
            {"text": "Because capitals are easier to read, and a formula has "
                     "to be legible at a glance",
             "correct": False,
             "why": "Legibility is not what case does here. It decides where "
                    "one element ends and the next begins"},
            {"text": "Because case decides where one element ends and the "
                     "next one begins",
             "correct": True},
            {"text": "Because lower-case letters are used for metals and "
                     "capitals for non-metals",
             "correct": False,
             "why": "Every symbol opens with a capital, metal or not. Case "
                    "carries no information about the type"},
            {"text": "Because a capital shows that the element is present in "
                     "a large amount",
             "correct": False,
             "why": "Amounts are carried by the numbers. A capital says "
                    "nothing about how much there is"},
        ],
        "figure": None,
    },
    {
        "id": "c2-04-s21",
        "band": "standard",
        "text": "Which of these changes would stop a formula being read apart "
                "into its elements?",
        "options": [
            {"text": "Writing a small number after a symbol",
             "correct": False,
             "why": "A number is not a letter, so it can never be mistaken for "
                    "the start of an element"},
            {"text": "Putting two symbols next to each other with nothing "
                     "written in between them",
             "correct": False,
             "why": "That is what a formula is. The capitals still show where "
                    "each symbol begins"},
            {"text": "Using a symbol that was taken from a Latin name rather "
                     "than from the English one",
             "correct": False,
             "why": "Na and Fe read apart exactly like Ca and Cl. Where the "
                    "letters came from changes nothing"},
            {"text": "Writing the second letter of a symbol as a capital",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c2-04-s22",
        "band": "standard",
        "text": "Berzelius took his letters from Latin names rather than from "
                "any language people were speaking. What advantage did that "
                "have?",
        "options": [
            {"text": "No country's own language was favoured over anybody "
                     "else's",
             "correct": True},
            {"text": "Latin was the language most Europeans spoke, so all of "
                     "them could read it",
             "correct": False,
             "why": "Hardly anyone spoke Latin by 1813, and the symbols work "
                    "for readers who know none of it"},
            {"text": "Latin words are shorter, so the symbols came out "
                     "shorter",
             "correct": False,
             "why": "Plumbum is no shorter than lead. Symbols are cut to two "
                    "letters whatever the word"},
            {"text": "Latin names cannot be changed, so the symbols could "
                     "never shift",
             "correct": False,
             "why": "What keeps a symbol steady is agreement among chemists, "
                    "not the language it came from"},
        ],
        "figure": None,
    },
    {
        "id": "c2-04-s23",
        "band": "standard",
        "text": "Suppose an element's English name were changed but its "
                "symbol were left alone. What would happen to every formula "
                "already printed?",
        "options": [
            {"text": "Nothing — the formulae would still name the same "
                     "elements",
             "correct": True},
            {"text": "They would have to be reprinted with the new letters in "
                     "them",
             "correct": False,
             "why": "The letters have not moved. A formula is written in "
                    "symbols, not in names"},
            {"text": "They would become ambiguous until the new name was "
                     "agreed",
             "correct": False,
             "why": "A symbol still points at one element whatever people call "
                    "it out loud"},
            {"text": "They would name one element fewer than before",
             "correct": False,
             "why": "Renaming an element does not remove it. The capitals in "
                    "the formula are unchanged"},
        ],
        "figure": None,
    },
    {
        "id": "c2-04-s24",
        "band": "standard",
        "text": "Why can the symbol Cl not be read as carbon followed by "
                "another element?",
        "options": [
            {"text": "Because the l is lower case, so it belongs to the C in "
                     "front of it",
             "correct": True},
            {"text": "Because there is no element whose symbol is a single l",
             "correct": False,
             "why": "There is no such symbol, but that is not what settles it: "
                    "a capital L would still open an element"},
            {"text": "Because carbon and chlorine are two elements that "
                     "cannot be joined together in any compound",
             "correct": False,
             "why": "They can, and they are in many compounds. The reason is "
                    "the case of the letter"},
            {"text": "Because a two-letter symbol is always read as the same "
                     "single letter written twice in a row",
             "correct": False,
             "why": "It is read as one symbol, once. A lower-case letter never "
                    "opens an element"},
        ],
        "figure": None,
    },
    {
        "id": "c2-04-s25",
        "band": "standard",
        "text": "Suppose two different elements had both been given the "
                "symbol Cu. What could a formula containing Cu no longer do?",
        "options": [
            {"text": "Be written down at all",
             "correct": False,
             "why": "It could still be written. What it could not do is be "
                    "read back with one meaning"},
            {"text": "Say which of the two elements it meant",
             "correct": True},
            {"text": "Be read in a language other than English",
             "correct": False,
             "why": "The ambiguity would follow the formula into every "
                    "language, because it is in the symbol itself"},
            {"text": "Count how many elements it contained",
             "correct": False,
             "why": "The capitals would still count the elements. What is lost "
                    "is which element one of them is"},
        ],
        "figure": None,
    },
    {
        "id": "c2-04-s26",
        "band": "standard",
        "text": "A new element is named after the town it was made in. Does "
                "that change the rule for writing its symbol?",
        "options": [
            {"text": "Yes — a symbol built from a place name is written as "
                     "two capital letters side by side, unlike other symbols",
             "correct": False,
             "why": "Two capitals would read as two elements. The rule does "
                    "not bend for where a name came from"},
            {"text": "Yes — place names are usually too long, so elements "
                     "named after a place are given three letters instead of "
                     "two",
             "correct": False,
             "why": "No symbol has three letters. A long name is cut down like "
                    "any other"},
            {"text": "No — a capital first, any second letter lower case, and "
                     "not already taken",
             "correct": True},
            {"text": "No — the symbol is taken from the Latin name of the "
                     "town",
             "correct": False,
             "why": "Latin symbols are a fossil of elements known in ancient "
                    "times, not a rule for new ones"},
        ],
        "figure": None,
    },
    {
        "id": "c2-04-s27",
        "band": "standard",
        "text": "Why is it fair to call a symbol like Pb a fossil?",
        "options": [
            {"text": "Because it preserves an older name that the language "
                     "has since dropped",
             "correct": True},
            {"text": "Because lead is dug out of rock, where fossils are "
                     "found",
             "correct": False,
             "why": "Where the metal comes from is beside the point. The "
                    "fossil is the word, not the ore"},
            {"text": "Because it is a symbol that working chemists no longer "
                     "use in laboratories today",
             "correct": False,
             "why": "Pb is in current use everywhere. What is out of use is "
                    "the word plumbum"},
            {"text": "Because it was the very first chemical symbol that "
                     "anyone ever wrote down on paper",
             "correct": False,
             "why": "Berzelius proposed the whole set together in 1813. No one "
                    "symbol came first"},
        ],
        "figure": None,
    },
    {
        "id": "c2-04-s28",
        "band": "standard",
        "text": "A student reads the formula MnO2 and says the n is an "
                "element in its own right. Correct them.",
        "options": [
            {"text": "The n is a count, so it belongs with the 2 rather than "
                     "with a symbol",
             "correct": False,
             "why": "Counts are digits. The n is a letter, and it belongs to "
                    "the capital M in front of it"},
            {"text": "The n is lower case, so it joins the M to make Mn",
             "correct": True},
            {"text": "The n is an element, but it is the same one as the M",
             "correct": False,
             "why": "It is not an element at all. Only a capital letter opens "
                    "one"},
            {"text": "The n is a printing error and should be a capital N",
             "correct": False,
             "why": "MNO2 would claim three elements. The lower-case n is "
                    "correct as printed"},
        ],
        "figure": None,
    },
    {
        "id": "c2-04-s29",
        "band": "standard",
        "text": "Two symbols are proposed for a newly made element: Nc and "
                "NC. Only one of them obeys the rule. Which, and what is wrong "
                "with the other?",
        "options": [
            {"text": "NC obeys it, and Nc puts a lower-case letter where a "
                     "capital belongs",
             "correct": False,
             "why": "The second letter is exactly where a lower-case letter "
                    "belongs. It is NC that breaks the rule"},
            {"text": "Both obey it, since the letters are the same either "
                     "way",
             "correct": False,
             "why": "Case is not decoration. NC reads as two elements and Nc "
                    "as one"},
            {"text": "Neither obeys it, because N is already nitrogen's",
             "correct": False,
             "why": "N alone is nitrogen. Nc is a different symbol, and it is "
                    "free"},
            {"text": "Nc obeys it, and NC reads as two elements rather than "
                     "one",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c2-04-s30",
        "band": "standard",
        "text": "If chemistry is written in symbols, a student argues, the "
                "element names do not matter. Give one job the names still do.",
        "options": [
            {"text": "They are what people say out loud and write in prose",
             "correct": True},
            {"text": "They decide which symbol the element is given",
             "correct": False,
             "why": "For Na, K, Fe, Pb, Au and Cu the English name decided "
                    "nothing at all"},
            {"text": "They record the order the elements were discovered in",
             "correct": False,
             "why": "A name carries no date. Gold and hydrogen are named on no "
                    "such scheme"},
            {"text": "They say how many letters the symbol will need",
             "correct": False,
             "why": "Hydrogen is long and takes one letter; tin is short and "
                    "takes two"},
        ],
        "figure": None,
    },

    # ── harder · MRB-338 night 3 ────────────────────────────────────────
    {
        "id": "c2-04-h10",
        "band": "harder",
        "text": "A museum label says a Roman pipe is made of plumbum and a "
                "Roman coin of aurum. What would a chemist write for those two "
                "metals today?",
        "options": [
            {"text": "Pl and Au",
             "correct": False,
             "why": "Lead's symbol is Pb, taking the first and the third "
                    "letters of plumbum rather than the first two"},
            {"text": "Pb and Au",
             "correct": True},
            {"text": "Pb and Ar",
             "correct": False,
             "why": "Ar is argon, a gas. Gold takes the first two letters of "
                    "aurum"},
            {"text": "Le and Go",
             "correct": False,
             "why": "Those are the English names shortened, which is exactly "
                    "what these two symbols are not"},
        ],
        "figure": None,
    },
    {
        "id": "c2-04-h11",
        "band": "harder",
        "text": "A student claims that every element known in ancient times "
                "has a two-letter symbol from an older language. Which fact "
                "tests that claim hardest?",
        "options": [
            {"text": "Carbon has been used since people first made fire, and "
                     "its symbol is the single letter C",
             "correct": True},
            {"text": "Copper, iron, lead and gold all have two-letter symbols "
                     "from older names",
             "correct": False,
             "why": "Those four agree with the claim, so they cannot test it. "
                    "A test needs a case that might break it"},
            {"text": "Magnesium has a two-letter symbol and was not one of "
                     "the elements known to people in ancient times",
             "correct": False,
             "why": "The claim is about ancient elements having such symbols, "
                    "not about modern ones lacking them"},
            {"text": "Hydrogen was completely unknown until the eighteenth "
                     "century, and its symbol is only one letter long",
             "correct": False,
             "why": "A modern element with a short symbol is consistent with "
                    "the claim and leaves it standing"},
        ],
        "figure": None,
    },
    {
        "id": "c2-04-h12",
        "band": "harder",
        "text": "A new element is made, and two laboratories propose the "
                "symbols Er and Eb. Er already belongs to erbium. What has to "
                "happen?",
        "options": [
            {"text": "Er is used anyway, and erbium moves to a new symbol",
             "correct": False,
             "why": "An element in use does not give up its symbol, because "
                    "every book already printed would be wrong"},
            {"text": "Both are used, and the context says which element is "
                     "meant",
             "correct": False,
             "why": "Context is exactly what a symbol is supposed to make "
                    "unnecessary. One symbol, one element"},
            {"text": "The new element takes Eb, because no two elements may "
                     "share a symbol",
             "correct": True},
            {"text": "Neither is used, since a proposed symbol has to come "
                     "from a Latin name",
             "correct": False,
             "why": "New elements take their letters from their new names. "
                    "Latin symbols belong to the ancient metals"},
        ],
        "figure": None,
    },
    {
        "id": "c2-04-h13",
        "band": "harder",
        "text": "A book prints CoCl2 on one line and COCl2 on the next. A "
                "student says it is the same substance typed twice. Evaluate "
                "that.",
        "options": [
            {"text": "They are the same: the case of a letter cannot change "
                     "what a formula holds",
             "correct": False,
             "why": "Case is the one thing that does change it. A capital O "
                    "opens an element that a lower-case o does not"},
            {"text": "They are different: one holds cobalt, the other holds "
                     "carbon and oxygen",
             "correct": True},
            {"text": "They are different, because the second has more "
                     "chlorine in it",
             "correct": False,
             "why": "Both have the same 2 after the Cl. The difference is in "
                    "the letters before it"},
            {"text": "Only the first is a real formula; the second breaks the "
                     "capital rule",
             "correct": False,
             "why": "COCl2 obeys the rule perfectly. It names three elements "
                    "instead of two"},
        ],
        "figure": None,
    },
    {
        "id": "c2-04-h14",
        "band": "harder",
        "text": "A student argues that capitals alone could separate the "
                "elements in a formula, so lower-case letters are pointless. "
                "Evaluate that.",
        "options": [
            {"text": "It is right: every formula could be written in capitals "
                     "with spaces between the symbols",
             "correct": False,
             "why": "Spaces would separate them, but there are only 26 "
                    "capitals for more than a hundred elements"},
            {"text": "It is wrong, because a lower-case letter is what lets "
                     "several elements share a first letter",
             "correct": True},
            {"text": "It is wrong, because capitals are reserved for metals",
             "correct": False,
             "why": "Every symbol opens with a capital whether it is a metal "
                    "or not"},
            {"text": "It is right, since a formula's numbers would still "
                     "separate the symbols",
             "correct": False,
             "why": "Many symbols carry no number after them, so nothing would "
                    "mark where one ended"},
        ],
        "figure": None,
    },
    {
        "id": "c2-04-h15",
        "band": "harder",
        "text": "Silver's symbol is Ag, from the older word argentum, and the "
                "country Argentina was named after the metal. What does that "
                "chain of words suggest?",
        "options": [
            {"text": "That silver was known and valued long before either "
                     "word was written in English",
             "correct": True},
            {"text": "That the symbol Ag was taken directly from the name of "
                     "the country rather than from an older word",
             "correct": False,
             "why": "The country was named from the metal, not the other way "
                    "about, and the symbol is older than the country"},
            {"text": "That silver was first mined in South America",
             "correct": False,
             "why": "Silver was worked in Europe and Asia for thousands of "
                    "years beforehand"},
            {"text": "That an element's symbol is always chosen from the "
                     "name of wherever that element happens to be found",
             "correct": False,
             "why": "No symbol records a place. Ag is the opening of an older "
                    "name for the metal"},
        ],
        "figure": None,
    },
    {
        "id": "c2-04-h16",
        "band": "harder",
        "text": "An old laboratory notebook uses the symbol Cb, which appears "
                "on no modern periodic table. What is the most likely "
                "explanation?",
        "options": [
            {"text": "It is a compound of carbon and boron, written as one "
                     "symbol",
             "correct": False,
             "why": "A compound needs two capitals. Cb has one, so whatever it "
                    "was, it was a single element"},
            {"text": "It is a slip of the pen for Ca",
             "correct": False,
             "why": "Possible once, but not through a whole notebook. A "
                    "consistent symbol is a used symbol"},
            {"text": "It is an older symbol for an element that has since "
                     "been renamed",
             "correct": True},
            {"text": "It is a symbol for an element later shown not to exist",
             "correct": False,
             "why": "An element that turned out not to exist would leave no "
                    "trace on any table under any name. A renaming does"},
        ],
        "figure": None,
    },
    {
        "id": "c2-04-h17",
        "band": "harder",
        "text": "Asked for the formula of iron sulfide, one student writes "
                "FeS and another writes FES. What does the second one claim, "
                "and why can it not be right?",
        "options": [
            {"text": "It claims F, E and S, and E is not an element at all",
             "correct": True},
            {"text": "It claims iron and sulfur twice over, which no formula "
                     "does",
             "correct": False,
             "why": "Nothing is written twice. Capitalising the e removes iron "
                    "from the formula completely"},
            {"text": "It claims the same two elements, just written in "
                     "capitals",
             "correct": False,
             "why": "Capitalising the e ends Fe and opens a new element, so "
                    "iron is no longer named"},
            {"text": "It claims a compound of fluorine and sulfur, which "
                     "cannot form",
             "correct": False,
             "why": "Fluorine and sulfur do form compounds. The problem is the "
                    "E standing between them"},
        ],
        "figure": None,
    },
    {
        "id": "c2-04-h18",
        "band": "harder",
        "text": "The word ferrous means containing iron, and iron's symbol is "
                "Fe. What does that pair of facts show about when the older "
                "name was in use?",
        "options": [
            {"text": "That ferrum was in use before either the English word "
                     "or the symbol was fixed",
             "correct": True},
            {"text": "That the word ferrous was itself built directly from "
                     "letters taken out of the symbol Fe",
             "correct": False,
             "why": "Words are not built from symbols. Both were built from "
                    "the older name ferrum"},
            {"text": "That the symbol Fe was deliberately chosen to match "
                     "the English word ferrous",
             "correct": False,
             "why": "Berzelius took his letters from the Latin names, not from "
                    "English words already in use"},
            {"text": "That iron itself was actually called ferrous in "
                     "everyday English until quite recently",
             "correct": False,
             "why": "Ferrous describes what a substance contains. It has never "
                    "been the English name of the metal"},
        ],
        "figure": None,
    },
    {
        "id": "c2-04-h19",
        "band": "harder",
        "text": "A periodic table printed in 1850 carries several symbols "
                "nobody uses now. Does that show symbols are not universal "
                "after all?",
        "options": [
            {"text": "Yes — a notation that changes at all over time cannot "
                     "possibly be the same everywhere in the world at once",
             "correct": False,
             "why": "Changing over two centuries is not the same as differing "
                    "between two countries at one moment"},
            {"text": "Yes, because a symbol has to stay fixed forever, never "
                     "once changing, to be worth anything to chemists",
             "correct": False,
             "why": "What makes a symbol worth having is that everyone uses "
                    "the same one now, not that it can never be revised"},
            {"text": "No, because the symbols printed in 1850 were only ever "
                     "used within the borders of one single country",
             "correct": False,
             "why": "They were used widely. The point is that they were "
                    "replaced, not that they were local"},
            {"text": "No — symbols are agreed rather than natural, so they "
                     "can be revised, and at any one time one set is in use",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c2-04-h20",
        "band": "harder",
        "text": "Reading a formula you have never seen, the capital rule "
                "tells you which elements are in the substance. What can the "
                "letters still not tell you?",
        "options": [
            {"text": "How many different elements it holds",
             "correct": False,
             "why": "That is exactly what the capitals do tell you: one "
                    "capital, one element"},
            {"text": "Whether any one of the elements present happens to be "
                     "a metal rather than a non-metal",
             "correct": False,
             "why": "You can look each symbol up on the table, which is where "
                    "the metals are marked"},
            {"text": "What the substance looks like or how it behaves",
             "correct": True},
            {"text": "Which particular elements the symbols in the formula "
                     "actually stand for",
             "correct": False,
             "why": "Every symbol names one element, and the table says which "
                    "one, whatever language you read"},
        ],
        "figure": None,
    },
    {
        "id": "c2-04-h21",
        "band": "harder",
        "text": "A student says Na must be a compound, because it contains "
                "the symbol N. What would the formula need before it could be "
                "a compound?",
        "options": [
            {"text": "A second capital letter, opening a second element",
             "correct": True},
            {"text": "A small number after the N",
             "correct": False,
             "why": "A number counts atoms of one element. Counting more "
                    "nitrogen would not add a second kind"},
            {"text": "A lower-case letter after the a",
             "correct": False,
             "why": "Lower-case letters belong to the capital in front, so "
                    "another one would still leave one element"},
            {"text": "Nothing — Na already holds nitrogen and something else",
             "correct": False,
             "why": "The a is lower case, so it joins the N. Na is one symbol "
                    "for sodium"},
        ],
        "figure": None,
    },
    {
        "id": "c2-04-h22",
        "band": "harder",
        "text": "Because Au means gold everywhere, a student concludes that "
                "chemistry has no translation problem at all. Evaluate that.",
        "options": [
            {"text": "It is right: a chemistry paper can be read by anyone "
                     "without being translated",
             "correct": False,
             "why": "Only the formulae travel. The method, the reasoning and "
                    "the safety notes are ordinary prose"},
            {"text": "It goes too far: the formulae travel, but the method and "
                     "the reasoning around them still have to be translated",
             "correct": True},
            {"text": "It is wrong, because in reality each individual "
                     "country writes the symbol for gold in its own way",
             "correct": False,
             "why": "Au is gold in every country. That part of the student's "
                    "claim is sound"},
            {"text": "It is wrong, because a symbol on its own means nothing "
                     "until the element's actual name is separately known",
             "correct": False,
             "why": "You can count the elements in a formula and look each "
                    "symbol up without knowing any name for it"},
        ],
        "figure": None,
    },
    {
        "id": "c2-04-h23",
        "band": "harder",
        "text": "A notebook lists three formulae: CO, CuO and CoO. Put them "
                "in order of how many elements each one names.",
        "options": [
            {"text": "CO first with one element only, then CuO and CoO with "
                     "two elements each",
             "correct": False,
             "why": "CO has two capitals, C and O, so it names two elements "
                    "like the others"},
            {"text": "CO and CoO tied with two elements each, then CuO last "
                     "with three elements",
             "correct": False,
             "why": "The lower-case u belongs to the C, so CuO is Cu and O — "
                    "two elements"},
            {"text": "CuO first with three, then CoO with two, then CO with "
                     "one",
             "correct": False,
             "why": "Counting letters rather than capitals gives this order. "
                    "Only capitals open an element"},
            {"text": "They cannot be put in order, because all three name two "
                     "elements",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c2-04-h24",
        "band": "harder",
        "text": "Lead is Pb and zinc is Zn. Using the symbols alone, which of "
                "the two metals has probably been known for longer, and why?",
        "options": [
            {"text": "Zinc, because its symbol uses letters from its own "
                     "English name",
             "correct": False,
             "why": "A symbol built from the English name means the element "
                    "was named in English times, so it is the younger one"},
            {"text": "Lead, because its symbol takes no letters from the "
                     "English word at all",
             "correct": True},
            {"text": "Zinc, because a symbol beginning with a later letter of "
                     "the alphabet was given out later",
             "correct": False,
             "why": "Symbols are not handed out in alphabetical order, so "
                    "where a letter sits tells you nothing"},
            {"text": "Neither, because a symbol says nothing about when an "
                     "element became known",
             "correct": False,
             "why": "A symbol with no letters from the English name is a "
                    "fossil of an older word, and that is a real clue"},
        ],
        "figure": None,
    },
    {
        "id": "c2-04-h25",
        "band": "harder",
        "text": "Sorting symbols into those built from the English name and "
                "those from somewhere else, a student puts Cl in the second "
                "pile. Why is that wrong?",
        "options": [
            {"text": "Cl is a Latin symbol, but it belongs with Na and Fe "
                     "rather than on its own",
             "correct": False,
             "why": "Cl is not Latin at all. Both its letters come from the "
                    "English word chlorine"},
            {"text": "Cl comes from chlorine, taking the first letter and the "
                     "third rather than the first two",
             "correct": True},
            {"text": "Cl belongs in neither pile, because chlorine is a gas "
                     "rather than a metal",
             "correct": False,
             "why": "Where a symbol came from has nothing to do with whether "
                    "the element is a metal"},
            {"text": "Cl was taken from the older name chlorum, which is "
                     "where the l comes from",
             "correct": False,
             "why": "The l is the third letter of chlorine. No older name is "
                    "needed to explain it"},
        ],
        "figure": None,
    },
    {
        "id": "c2-04-h26",
        "band": "harder",
        "text": "The notation needs both the capital rule and the periodic "
                "table. What does each one do that the other cannot?",
        "options": [
            {"text": "The rule says how to write a symbol; the table says "
                     "which symbols are already taken",
             "correct": True},
            {"text": "The rule alone names every element; the table's only "
                     "job is to count how many there are",
             "correct": False,
             "why": "The table names the elements. Counting is done by the "
                    "capitals in a formula"},
            {"text": "The rule only works for metals; the table has to cover "
                     "every single other kind of element instead",
             "correct": False,
             "why": "Both cover every element. Neither one is limited to a "
                    "kind of element"},
            {"text": "The rule is only ever used in English; the table is "
                     "used in every other language around the world",
             "correct": False,
             "why": "Both are used everywhere. That is the whole point of "
                    "agreeing on them"},
        ],
        "figure": None,
    },
    {
        "id": "c2-04-h27",
        "band": "harder",
        "text": "A student says that because formulae can be read in any "
                "country, chemical symbols are a language of their own. "
                "Evaluate that.",
        "options": [
            {"text": "It is right: symbols have their own words and their own "
                     "grammar, so they are a language",
             "correct": False,
             "why": "A language can say anything. Symbols can only name "
                    "elements and how many atoms of each"},
            {"text": "It is wrong, because a formula has to be read out loud "
                     "in a real language",
             "correct": False,
             "why": "It can be read out in any language, which is a point in "
                    "the student's favour rather than against"},
            {"text": "It is wrong, because the symbols were taken from Latin "
                     "and Latin is a language already",
             "correct": False,
             "why": "Where the letters came from does not settle what the "
                    "notation is now"},
            {"text": "It goes too far: symbols are a shared notation, able to "
                     "name substances and nothing else",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c2-04-h28",
        "band": "harder",
        "text": "Iodine has the symbol I. Someone proposes giving a new "
                "element the symbol l, a lower-case L. What is wrong with the "
                "proposal?",
        "options": [
            {"text": "Nothing, as long as readers are careful to tell the two "
                     "apart",
             "correct": False,
             "why": "Care is not what the notation runs on. A symbol that "
                    "breaks the rule cannot be read by rule"},
            {"text": "A symbol has to open with a capital, so a lower-case "
                     "letter cannot be one",
             "correct": True},
            {"text": "L is already taken by another element",
             "correct": False,
             "why": "No element has the single symbol L. The problem is the "
                    "case, not the letter"},
            {"text": "A symbol cannot be a single letter once a hundred "
                     "elements are known",
             "correct": False,
             "why": "Single-letter symbols are still in use — H, C, N, O, K. "
                    "There is no such limit"},
        ],
        "figure": None,
    },
    {
        "id": "c2-04-h29",
        "band": "harder",
        "text": "Phosphorus is P and lead is Pb. Explain how a reader tells "
                "which of the two a formula means.",
        "options": [
            {"text": "By the lower-case b: with it the symbol is lead, "
                     "without it the capital P stands alone as phosphorus",
             "correct": True},
            {"text": "By whether the letter P happens to be followed by a "
                     "small number written after it",
             "correct": False,
             "why": "Either symbol can carry a number after it. The number "
                    "counts atoms and names nothing"},
            {"text": "By whichever order the two symbols happen to appear in "
                     "within the whole formula",
             "correct": False,
             "why": "Order is a convention about how a formula is set out. It "
                    "never decides which element a symbol is"},
            {"text": "By checking whether the rest of the formula also holds "
                     "a metal somewhere else in it",
             "correct": False,
             "why": "A symbol means one element wherever it appears, with no "
                    "help from its neighbours"},
        ],
        "figure": None,
    },
    {
        "id": "c2-04-h30",
        "band": "harder",
        "text": "Someone proposes replacing every symbol that does not look "
                "like its English name, so that Na becomes So and Pb becomes "
                "Le. Give the strongest objection.",
        "options": [
            {"text": "The new symbols would be longer, and formulae would "
                     "take up more room on the page",
             "correct": False,
             "why": "So and Le are two letters each, exactly like Na and Pb. "
                    "Nothing would get longer"},
            {"text": "Every book, label and paper printed until now would "
                     "stop matching the symbols in use",
             "correct": True},
            {"text": "The English name would then decide the symbol, and "
                     "English speakers would be favoured",
             "correct": False,
             "why": "A real objection, and the weaker one: a symbol is looked "
                    "up on the table rather than guessed from a name"},
            {"text": "There would be no way to tell which elements were known "
                     "in ancient times",
             "correct": False,
             "why": "Losing a historical clue is a pity rather than a problem "
                    "for reading chemistry"},
        ],
        "figure": None,
    },
]
