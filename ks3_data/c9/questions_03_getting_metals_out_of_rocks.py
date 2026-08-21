"""C9 lesson 03 — Getting metals out of rocks: twelve questions (MRB-281).

The lesson's argument is one shape: extraction is a reaction and not a
temperature, the reaction is reduction, and which method works is decided by
where the metal sits relative to CARBON. The page teaches it with six
deliveries, four methods and twenty-four authored verdicts.

These twelve probe the angles the mastery ladder leaves alone: why melting is
not extraction, what the carbon line predicts in both directions, and why a
method that works can still be the wrong one.

The distractors are built from the lesson's declared misconceptions.

`MATL-08` (metals are in the ground as metal; extraction is digging and
melting) drives the wrong options in e01, s01 and h01.

`MATL-09` (any oxide gives up its oxygen to carbon if the furnace is hot
enough) drives e03, s02, s04 and h02. Each treats heat as the active
ingredient. s04 is the one that matters: it puts a hotter furnace against a
metal above carbon, so the belief makes a concrete prediction and the carbon
line refutes it.

A third strand, in neither register entry, is that "it works" and "a works
would pay for it" are different verdicts — s03 and h04 are built on it, because
that distinction is the reason the bench asks a student to CHOOSE.

⚠️ MRB-278 · ANSWER POSITION. Cycles 0, 1, 2, 3 through each band.

⚠️ BAND VALUES ARE FULL WORDS.
"""

UNIT = "C9"
LESSON = "getting-metals-out-of-rocks"
LESSON_NUMBER = 3

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "c9-03-e01",
        "band": "easier",
        "text": "What is an ore?",
        "options": [
            {"text": "A rock with enough of a metal compound in it to be "
                     "worth extracting",
             "correct": True},
            {"text": "A lump of pure metal found lying in the ground",
             "correct": False,
             "why": "That is what gold does, and it is the exception rather "
                    "than what an ore is."},
            {"text": "Any rock that contains atoms of a metal anywhere in it",
             "correct": False,
             "why": "Almost every rock does. The word only applies when there "
                    "is enough to be worth the work."},
            {"text": "A metal that has been melted and poured into a mould",
             "correct": False,
             "why": "That is casting, and it happens long after extraction."},
        ],
        "figure": None,
    },
    {
        "id": "c9-03-e02",
        "band": "easier",
        "text": "What does reduction mean in this lesson?",
        "options": [
            {"text": "Making a lump of ore smaller by crushing it",
             "correct": False,
             "why": "Crushing changes the size and joins or separates "
                    "nothing."},
            {"text": "Removing oxygen from a compound",
             "correct": True},
            {"text": "Lowering the temperature of a furnace once it is "
                     "running",
             "correct": False,
             "why": "The everyday meaning of the word does not apply here."},
            {"text": "Reducing the amount of metal that is wasted in the "
                     "process",
             "correct": False,
             "why": "Efficiency is a separate matter. Reduction is a chemical "
                    "change."},
        ],
        "figure": None,
    },
    {
        "id": "c9-03-e03",
        "band": "easier",
        "text": "Which of these metals CANNOT be obtained from its oxide by "
                "heating with carbon?",
        "options": [
            {"text": "Iron", "correct": False,
             "why": "Iron is below carbon and is obtained exactly this way, "
                    "in a blast furnace."},
            {"text": "Zinc", "correct": False,
             "why": "Zinc is below carbon and is obtained this way too — it "
                    "leaves as a vapour."},
            {"text": "Magnesium", "correct": True},
            {"text": "Lead", "correct": False,
             "why": "Lead is well below carbon and was one of the first "
                    "metals ever smelted."},
        ],
        "figure": None,
    },
    {
        "id": "c9-03-e04",
        "band": "easier",
        "text": "Gold is usually found in the ground as the metal itself, "
                "not as a compound. Why?",
        "options": [
            {"text": "Because it is denser than the rock and sinks out of it",
             "correct": False,
             "why": "Density affects where gold collects, not whether it is "
                    "combined."},
            {"text": "Because its compounds dissolve away in rain over time",
             "correct": False,
             "why": "It never forms many compounds to dissolve in the first "
                    "place."},
            {"text": "Because it melts at a low enough temperature to "
                     "separate naturally",
             "correct": False,
             "why": "Gold melts at over 1000 °C, and melting would not "
                    "separate a compound anyway."},
            {"text": "Because it is at the bottom of the reactivity series "
                     "and barely reacts",
             "correct": True},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "c9-03-s01",
        "band": "standard",
        "text": "Why can copper not be obtained from malachite simply by "
                "melting the stone?",
        "options": [
            {"text": "Because the copper is chemically joined to other "
                     "elements",
             "correct": True},
            {"text": "Because malachite melts at a higher temperature than "
                     "copper does",
             "correct": False,
             "why": "Even if it melted easily, melting joins nothing and "
                    "separates nothing."},
            {"text": "Because the copper is spread through the stone in tiny "
                     "droplets",
             "correct": False,
             "why": "There are no droplets of copper in it. There is no "
                    "copper metal in it at all."},
            {"text": "Because the stone would burn away before the copper "
                     "melted",
             "correct": False,
             "why": "The problem is not what the heat destroys. It is that "
                    "heat alone is the wrong tool."},
        ],
        "figure": None,
    },
    {
        "id": "c9-03-s02",
        "band": "standard",
        "text": "Aluminium oxide is heated with carbon in a very hot furnace "
                "and no aluminium appears. Why not?",
        "options": [
            {"text": "The furnace was not hot enough and a hotter one would "
                     "work",
             "correct": False,
             "why": "No furnace is hot enough. Temperature is not what "
                    "decides this."},
            {"text": "Aluminium is above carbon, so carbon cannot take its "
                     "oxygen",
             "correct": True},
            {"text": "Aluminium oxide is not really an oxide and holds no "
                     "oxygen",
             "correct": False,
             "why": "It is an oxide and it holds its oxygen very tightly "
                    "indeed."},
            {"text": "The aluminium formed and then immediately reacted back "
                     "again",
             "correct": False,
             "why": "None forms. There is no reaction to reverse."},
        ],
        "figure": None,
    },
    {
        "id": "c9-03-s03",
        "band": "standard",
        "text": "Silver can be freed from its oxide by heating alone, and "
                "also by electrolysis. Why would a works choose heating?",
        "options": [
            {"text": "Because electrolysis would not actually work on silver "
                     "oxide",
             "correct": False,
             "why": "It would work. Working is not the same as being worth "
                    "doing."},
            {"text": "Because heating produces a purer metal than "
                     "electrolysis does",
             "correct": False,
             "why": "Electrolysis is generally the purer route. Purity is not "
                    "the deciding factor here."},
            {"text": "Because heating alone is far cheaper and both methods "
                     "work",
             "correct": True},
            {"text": "Because electrolysis only works on metals above carbon",
             "correct": False,
             "why": "It works on anything. It is simply an expensive way to "
                    "do an easy job."},
        ],
        "figure": None,
    },
    {
        "id": "c9-03-s04",
        "band": "standard",
        "text": "A student says a big enough furnace could extract any metal "
                "with carbon. What single example refutes this?",
        "options": [
            {"text": "Iron, which needs a blast furnace bigger than any "
                     "laboratory",
             "correct": False,
             "why": "Iron IS extracted with carbon. It supports the claim "
                    "rather than refuting it."},
            {"text": "Gold, which needs no furnace at all to obtain",
             "correct": False,
             "why": "Gold is easy for a different reason and says nothing "
                    "about carbon's limits."},
            {"text": "Zinc, which leaves the furnace as a vapour and must be "
                     "condensed",
             "correct": False,
             "why": "Awkward to collect, and carbon frees it perfectly well."},
            {"text": "Aluminium, which carbon cannot free at any temperature",
             "correct": True},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "c9-03-h01",
        "band": "harder",
        "text": "Aluminium is one of the commonest elements in the Earth's "
                "crust and was once more expensive than gold. What does that "
                "tell you about extraction?",
        "options": [
            {"text": "That the cost of a metal depends on how hard it is to "
                     "free, not how rare it is",
             "correct": True},
            {"text": "That aluminium ore was much rarer in the past than it "
                     "is today",
             "correct": False,
             "why": "Bauxite has always been abundant. Nothing about the "
                    "supply changed."},
            {"text": "That aluminium was more useful then and so people paid "
                     "more for it",
             "correct": False,
             "why": "It became far more useful once it was cheap, which is "
                    "the reverse of this."},
            {"text": "That the Earth's crust was measured wrongly at the "
                     "time",
             "correct": False,
             "why": "The abundance was known. The chemistry was the "
                    "obstacle."},
        ],
        "figure": None,
    },
    {
        "id": "c9-03-h02",
        "band": "harder",
        "text": "A newly made metal M has an oxide that is unchanged by "
                "heating alone AND unchanged by heating with carbon. What "
                "follows?",
        "options": [
            {"text": "M's oxide is not really an oxide, since both methods "
                     "failed",
             "correct": False,
             "why": "Both methods failing is what being high in the series "
                    "looks like, not evidence against the compound."},
            {"text": "M is above carbon in the series and needs electrolysis",
             "correct": True},
            {"text": "M is below carbon but the sample was contaminated",
             "correct": False,
             "why": "A metal below carbon would have been freed by the carbon "
                    "route."},
            {"text": "M cannot be extracted by any method at all",
             "correct": False,
             "why": "Electrolysis remains, and it is how every metal above "
                    "carbon is obtained."},
        ],
        "figure": None,
    },
    {
        "id": "c9-03-h03",
        "band": "harder",
        "text": "Recycling aluminium uses roughly a twentieth of the "
                "electricity that extracting it from bauxite does. Why is the "
                "saving so large?",
        "options": [
            {"text": "Because recycled aluminium is a different, softer "
                     "metal",
             "correct": False,
             "why": "It is the same element and the same metal."},
            {"text": "Because melting a solid always takes less energy than "
                     "heating a rock",
             "correct": False,
             "why": "Close, and it misses the point: the expensive step is "
                    "not heating, it is separating."},
            {"text": "Because the oxygen has already been prised off once and "
                     "does not come back",
             "correct": True},
            {"text": "Because collection and transport are counted in the "
                     "extraction figure",
             "correct": False,
             "why": "The figure compares the process energy, and transport "
                    "would not account for twenty times."},
        ],
        "figure": None,
    },
    {
        "id": "c9-03-h04",
        "band": "harder",
        "text": "Copper can be obtained from its oxide by heating with carbon "
                "and also by electrolysis. What makes carbon the route a "
                "works chooses?",
        "options": [
            {"text": "Electrolysis would leave the copper too impure for "
                     "wiring",
             "correct": False,
             "why": "Electrolysis is in fact used to PURIFY copper. Purity is "
                    "not the objection."},
            {"text": "Copper is above carbon, so electrolysis is the only "
                     "option available",
             "correct": False,
             "why": "Copper is well below carbon, which is why the cheap "
                    "route exists at all."},
            {"text": "Carbon is the only method that works on copper oxide",
             "correct": False,
             "why": "Both work. That is precisely what makes it a choice "
                    "rather than a necessity."},
            {"text": "Both work, and a furnace with coke in it is far cheaper "
                     "than the electricity",
             "correct": True},
        ],
        "figure": None,
    },
]
