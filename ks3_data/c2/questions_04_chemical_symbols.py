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
                     "order of symbol",
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
            {"text": "Three, because the lower-case letters and the small "
                     "number are all part of the symbols in front of them",
             "correct": False,
             "why": "The lower-case a does belong to the N, but H and C and O "
                    "are three more capitals. Count the capitals and you get "
                    "four"},
            {"text": "Five, counting the small 3 as one more",
             "correct": False,
             "why": "The 3 is a count of oxygen atoms, not an element. Only "
                    "capital letters start elements"},
            {"text": "Four",
             "correct": True},
            {"text": "Six, one for every letter and number written down",
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
            {"text": "It makes every symbol match its English name exactly",
             "correct": False,
             "why": "The opposite: several symbols come from Latin and do not "
                    "match the English name at all"},
            {"text": "It lets symbols be strung into a formula that can be "
                     "read apart again, because a capital always starts a new "
                     "element",
             "correct": True},
            {"text": "It stops two elements being confused with each other",
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
            {"text": "Four, one for each of the different elements the "
                     "formula names between its capital letters",
             "correct": False,
             "why": "Four is the number of ELEMENTS. The small 3 means three "
                    "oxygen atoms rather than one"},
            {"text": "Seven, counting the lower-case a as an atom of its own",
             "correct": False,
             "why": "The a belongs to the N, making sodium. It counts "
                    "nothing"},
            {"text": "Three, because only the small number counts atoms",
             "correct": False,
             "why": "A symbol with no number after it already means one atom. "
                    "Na, H and C are one each"},
            {"text": "Six",
             "correct": True},
        ],
        "figure": None,
    },
]
