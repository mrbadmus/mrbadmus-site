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

    # ── easier · MRB-335 top-up ─────────────────────────────────────────
    {
        "id": "c9-03-e05",
        "band": "easier",
        "text": "What is extraction?",
        "options": [
            {"text": "Digging an ore out of the ground and crushing it small "
                     "enough for the metal in it to be separated out by "
                     "sieving",
             "correct": False,
             "why": "Mining and crushing come first. Extraction is the "
                    "chemical step that frees the metal"},
            {"text": "Melting a rock until the metal runs out of it",
             "correct": False,
             "why": "Melting malachite gives molten malachite. The copper is "
                    "chemically joined"},
            {"text": "Getting a metal out of its ore as the metal itself",
             "correct": True},
            {"text": "Heating an ore to a high temperature",
             "correct": False,
             "why": "A temperature is not a reaction. Something has to take "
                    "the oxygen away"},
        ],
        "figure": None,
    },
    {
        "id": "c9-03-e06",
        "band": "easier",
        "text": "What is electrolysis?",
        "options": [
            {"text": "Passing electricity through a metal to make it hot "
                     "enough to melt",
             "correct": False,
             "why": "Heating is not what electrolysis does. It breaks the "
                    "compound apart chemically"},
            {"text": "Using electricity to weld two metals together",
             "correct": False,
             "why": "That is welding. Electrolysis takes a compound apart"},
            {"text": "Coating one metal with another",
             "correct": False,
             "why": "Electroplating does that, and it uses the same "
                    "equipment. The word here means splitting a compound"},
            {"text": "Splitting a compound apart by passing electricity "
                     "through it when molten or dissolved",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c9-03-e07",
        "band": "easier",
        "text": "Most ores are which kind of compound?",
        "options": [
            {"text": "Oxides",
             "correct": True},
            {"text": "Chlorides, which is why so many of the world's metals "
                     "are dug out of old sea beds where salt has been laid "
                     "down over millions of years",
             "correct": False,
             "why": "Salt deposits are real and are not where most metals "
                    "come from. Most ores are oxides or are roasted into "
                    "them"},
            {"text": "Sulfates",
             "correct": False,
             "why": "A few ores are sulfides, and they are roasted into "
                    "oxides before extraction"},
            {"text": "Pure metals",
             "correct": False,
             "why": "Then no extraction would be needed. Gold is the "
                    "exception rather than the rule"},
        ],
        "figure": None,
    },
    {
        "id": "c9-03-e08",
        "band": "easier",
        "text": "Which of these metals CAN be obtained from its oxide by "
                "heating with carbon?",
        "options": [
            {"text": "Aluminium",
             "correct": False,
             "why": "Aluminium is above carbon, so carbon cannot take its "
                    "oxygen at any temperature"},
            {"text": "Lead",
             "correct": True},
            {"text": "Calcium",
             "correct": False,
             "why": "Calcium is well above carbon in the series"},
            {"text": "Sodium, which sits at the top of the series and is "
                     "therefore the easiest of all the metals to free from "
                     "whatever it happens to be joined to",
             "correct": False,
             "why": "Being at the top makes a metal the HARDEST to free. It "
                    "holds its partner most tightly"},
        ],
        "figure": None,
    },
    {
        "id": "c9-03-e09",
        "band": "easier",
        "text": "Reduction is the opposite of which process?",
        "options": [
            {"text": "Neutralisation, since one of them adds something to a "
                     "compound and the other takes something away from it",
             "correct": False,
             "why": "Neutralisation is an acid and a base. Reduction is "
                    "removing oxygen"},
            {"text": "Displacement",
             "correct": False,
             "why": "A displacement can BE a reduction. They are not "
                    "opposites"},
            {"text": "Oxidation",
             "correct": True},
            {"text": "Dissolving",
             "correct": False,
             "why": "Dissolving is a physical change. Reduction is a "
                    "chemical one"},
        ],
        "figure": None,
    },
    {
        "id": "c9-03-e10",
        "band": "easier",
        "text": "Which metal is obtained by passing electricity through its "
                "molten compound rather than by heating with carbon?",
        "options": [
            {"text": "Copper",
             "correct": False,
             "why": "Copper is below carbon, so a furnace with coke in it "
                    "does the job far more cheaply"},
            {"text": "Lead",
             "correct": False,
             "why": "Lead is below carbon. Carbon takes its oxygen"},
            {"text": "Iron, which is smelted in blast furnaces so large and "
                     "so hot that only electricity could ever supply the "
                     "energy that they need",
             "correct": False,
             "why": "Blast furnaces burn coke. Iron is below carbon and needs "
                    "no electricity"},
            {"text": "Aluminium",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c9-03-e11",
        "band": "easier",
        "text": "Bauxite is the ore of which metal?",
        "options": [
            {"text": "Aluminium",
             "correct": True},
            {"text": "Iron, which is smelted out of it in blast furnaces and "
                     "is the metal produced in far the largest quantity of "
                     "any in the world",
             "correct": False,
             "why": "Iron's ores are different rocks, and iron comes out of "
                    "them with carbon. Bauxite needs electricity"},
            {"text": "Copper",
             "correct": False,
             "why": "Malachite is an ore of copper. Bauxite is not"},
            {"text": "Lead",
             "correct": False,
             "why": "Lead has ores of its own, and bauxite is not one of "
                    "them"},
        ],
        "figure": None,
    },
    {
        "id": "c9-03-e12",
        "band": "easier",
        "text": "Which metals are found in the ground as the metal itself?",
        "options": [
            {"text": "The most reactive ones, such as potassium, because a "
                     "reactive metal breaks free of whatever it is joined to "
                     "and ends up on its own",
             "correct": False,
             "why": "Exactly backwards. A reactive metal joins things and "
                    "stays joined"},
            {"text": "The least reactive ones, such as gold",
             "correct": True},
            {"text": "The commonest ones",
             "correct": False,
             "why": "Aluminium is the commonest metal in the crust and is "
                    "never found uncombined"},
            {"text": "The densest ones",
             "correct": False,
             "why": "Density has nothing to do with it. Reactivity does"},
        ],
        "figure": None,
    },
    {
        "id": "c9-03-e13",
        "band": "easier",
        "text": "What has to happen to a metal oxide before the metal can be "
                "used?",
        "options": [
            {"text": "The oxide has to be melted, so that the metal in it can "
                     "be poured off and the oxygen left behind as a gas above "
                     "the surface",
             "correct": False,
             "why": "Melting keeps the compound whole. Something has to take "
                    "the oxygen chemically"},
            {"text": "More oxygen has to be added",
             "correct": False,
             "why": "That would be oxidation, and it goes the wrong way"},
            {"text": "The oxygen has to be removed",
             "correct": True},
            {"text": "It has to be dissolved in water",
             "correct": False,
             "why": "Most metal oxides barely dissolve, and dissolving would "
                    "not free the metal"},
        ],
        "figure": None,
    },

    # ── standard · MRB-335 top-up ───────────────────────────────────────
    {
        "id": "c9-03-s05",
        "band": "standard",
        "text": "Why is it CARBON that is used in a furnace, rather than "
                "another metal?",
        "options": [
            {"text": "Because carbon is the only substance that will take "
                     "oxygen away from a metal oxide, so no other element "
                     "could be used for the job whatever it cost",
             "correct": False,
             "why": "Aluminium does it too, in thermite. Carbon is used "
                    "because it is cheap"},
            {"text": "Because carbon burns, and the heat is what frees the "
                     "metal",
             "correct": False,
             "why": "The heat helps and the freeing is a displacement. Carbon "
                    "takes the oxygen"},
            {"text": "Because it is cheap and plentiful, and it sits high "
                     "enough in the series to free the metals below it",
             "correct": True},
            {"text": "Because carbon is a non-metal",
             "correct": False,
             "why": "Being a non-metal is not the qualification. Its POSITION "
                    "is"},
        ],
        "figure": None,
    },
    {
        "id": "c9-03-s06",
        "band": "standard",
        "text": "Zinc oxide is heated with carbon and zinc appears. Which "
                "element has been oxidised, and which reduced?",
        "options": [
            {"text": "The zinc has been oxidised and the carbon reduced, "
                     "since the zinc is the one that ends up changed into a "
                     "different substance from the one it started as",
             "correct": False,
             "why": "The zinc has LOST oxygen, which is reduction. The carbon "
                    "gained it"},
            {"text": "Both have been reduced",
             "correct": False,
             "why": "One gains what the other loses. They cannot both be "
                    "reduced"},
            {"text": "Neither — this is a decomposition",
             "correct": False,
             "why": "Two reactants go in, and the carbon takes the oxygen. A "
                    "decomposition has one reactant"},
            {"text": "The carbon has been oxidised and the zinc oxide "
                     "reduced",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c9-03-s07",
        "band": "standard",
        "text": "Zinc oxide is heated with carbon in a furnace. Name what "
                "goes in and what comes out.",
        "options": [
            {"text": "Zinc oxide and carbon go in; zinc and carbon dioxide "
                     "come out",
             "correct": True},
            {"text": "Zinc oxide and carbon go in; zinc and oxygen come out, "
                     "since the oxygen has been driven off the zinc and has "
                     "nowhere else to go but into the air above the furnace",
             "correct": False,
             "why": "The oxygen leaves joined to the carbon. That is the "
                    "whole reason the carbon is there"},
            {"text": "Zinc and oxygen go in; zinc oxide comes out",
             "correct": False,
             "why": "That is the reaction backwards — an oxidation rather "
                    "than an extraction"},
            {"text": "Zinc oxide goes in alone; zinc and oxygen come out",
             "correct": False,
             "why": "Zinc oxide heated alone gives nothing. Something has to "
                    "take the oxygen"},
        ],
        "figure": None,
    },
    {
        "id": "c9-03-s08",
        "band": "standard",
        "text": "Two ores are heated with carbon. One gives a metal and one "
                "does not. What separates them?",
        "options": [
            {"text": "Whether the furnace reached a high enough temperature "
                     "for the second one, since every oxide gives up its "
                     "oxygen if it is heated far enough with carbon",
             "correct": False,
             "why": "That is the misconception this lesson names. Aluminium "
                    "oxide resists carbon at any temperature"},
            {"text": "Whether the metal is below carbon in the reactivity "
                     "series",
             "correct": True},
            {"text": "How much carbon was used",
             "correct": False,
             "why": "More carbon cannot start a reaction the order rules "
                    "out"},
            {"text": "How long they were heated",
             "correct": False,
             "why": "Time changes nothing for a reaction that cannot "
                    "happen"},
        ],
        "figure": None,
    },
    {
        "id": "c9-03-s09",
        "band": "standard",
        "text": "Why is electrolysis so much more expensive than a furnace?",
        "options": [
            {"text": "Because the equipment has to be built out of materials "
                     "that will not themselves be broken apart by the current "
                     "passing through the cell",
             "correct": False,
             "why": "Electrodes are a real cost and a small one. The "
                    "electricity itself is the expense"},
            {"text": "Because it is slower",
             "correct": False,
             "why": "Speed is not the main cost. Energy is"},
            {"text": "Because it needs a great deal of electricity, and "
                     "electricity costs more than coke",
             "correct": True},
            {"text": "Because the compound has to be melted first",
             "correct": False,
             "why": "Melting is part of the energy cost, and the current is "
                    "the larger part"},
        ],
        "figure": None,
    },
    {
        "id": "c9-03-s10",
        "band": "standard",
        "text": "Recycling aluminium uses about a twentieth of the "
                "electricity that extraction does. Which step is being "
                "skipped?",
        "options": [
            {"text": "Mining and transporting the ore, which is the part of "
                     "the process that uses most of the energy in making a "
                     "new tonne of aluminium",
             "correct": False,
             "why": "Mining is a real cost and a much smaller one. The "
                    "electrolysis is where the energy goes"},
            {"text": "Melting the metal",
             "correct": False,
             "why": "Recycling still melts it. That is the twentieth that IS "
                    "spent"},
            {"text": "Purifying the metal",
             "correct": False,
             "why": "Recycled aluminium is cleaned up too. The saving is the "
                    "oxygen"},
            {"text": "Prising the oxygen off, which has already been paid "
                     "for once",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c9-03-s11",
        "band": "standard",
        "text": "A student says a metal high in the series must be easy to "
                "extract, because it is so reactive. What is wrong?",
        "options": [
            {"text": "A reactive metal holds its partner MORE tightly, so it "
                     "is harder to free",
             "correct": True},
            {"text": "Reactivity has nothing to do with extraction, which is "
                     "decided by how deep the ore lies and how much of it a "
                     "given rock happens to contain",
             "correct": False,
             "why": "Reactivity decides the method entirely. It is the "
                    "direction of the student's rule that is wrong"},
            {"text": "Nothing is wrong — reactive metals are easy to "
                     "extract",
             "correct": False,
             "why": "Aluminium is reactive and cost more than gold until "
                    "electricity arrived"},
            {"text": "Reactive metals are never found in ores",
             "correct": False,
             "why": "They are found in ores and nowhere else, because they "
                    "are always combined"},
        ],
        "figure": None,
    },
    {
        "id": "c9-03-s12",
        "band": "standard",
        "text": "A blast furnace turns out to work mostly through carbon "
                "MONOXIDE rather than solid carbon. What does that change "
                "about the rule you learned?",
        "options": [
            {"text": "The rule is wrong, and position does not decide it "
                     "after all",
             "correct": False,
             "why": "The positions still decide it. What the detail changes "
                    "is the mechanism"},
            {"text": "Nothing about WHICH metals — the rule is right about "
                     "that and simple about how",
             "correct": True},
            {"text": "Aluminium could be extracted in a furnace after all",
             "correct": False,
             "why": "Carbon monoxide cannot take oxygen from aluminium "
                    "either. The order still holds"},
            {"text": "Carbon is not really in the reactivity series",
             "correct": False,
             "why": "It is, and its position is what the whole method rests "
                    "on"},
        ],
        "figure": None,
    },
    {
        "id": "c9-03-s13",
        "band": "standard",
        "text": "Which pair of facts explains why gold was worked thousands "
                "of years before aluminium?",
        "options": [
            {"text": "Gold is much commoner than aluminium, and a metal that "
                     "is easy to find is one that people learn to work with "
                     "long before a rare one",
             "correct": False,
             "why": "Aluminium is far commoner. Availability is not what "
                    "separated them"},
            {"text": "Gold melts at a lower temperature",
             "correct": False,
             "why": "Aluminium's melting point is lower still. Melting was "
                    "never the difficulty"},
            {"text": "Gold is found uncombined; aluminium had to wait for "
                     "electricity",
             "correct": True},
            {"text": "Gold is softer, so it could be worked with stone tools",
             "correct": False,
             "why": "True and secondary. The first problem is having any "
                    "metal at all to work"},
        ],
        "figure": None,
    },

    # ── harder · MRB-335 top-up ─────────────────────────────────────────
    {
        "id": "c9-03-h05",
        "band": "harder",
        "text": "Explain why extraction with carbon counts as a DISPLACEMENT "
                "rather than as a separate kind of reaction.",
        "options": [
            {"text": "Because the metal is displaced from the rock it was "
                     "sitting in, which is what the word displacement means "
                     "when it is used about mining",
             "correct": False,
             "why": "Nothing is moved out of a rock physically. What is "
                    "swapped is which element the oxygen is joined to"},
            {"text": "Because the carbon burns and the heat frees the metal",
             "correct": False,
             "why": "Heat alone frees almost nothing. The carbon takes the "
                    "oxygen chemically"},
            {"text": "Because carbon is higher in the series than the metal, "
                     "and takes the oxygen in its place",
             "correct": True},
            {"text": "Because a solid is produced",
             "correct": False,
             "why": "A solid product is common to many reaction types. The "
                    "swap is what makes it a displacement"},
        ],
        "figure": None,
    },
    {
        "id": "c9-03-h06",
        "band": "harder",
        "text": "A new metal M has an oxide unchanged by heating alone AND "
                "unchanged by heating with carbon. Which TWO things does that "
                "establish?",
        "options": [
            {"text": "M is above carbon in the series, and its ore must "
                     "therefore be rare, since the metals highest in the "
                     "series are the ones least often found in the crust",
             "correct": False,
             "why": "Aluminium is the commonest metal in the crust and is "
                    "high in the series. Rarity does not follow"},
            {"text": "M is below carbon, and it needs electrolysis",
             "correct": False,
             "why": "Below carbon means carbon WOULD have worked. The two "
                    "halves contradict each other"},
            {"text": "M is at the very bottom of the series",
             "correct": False,
             "why": "A metal at the bottom would come out on heating alone, "
                    "as silver oxide does"},
            {"text": "M is above carbon in the series, and it is not one of "
                     "the very unreactive metals",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c9-03-h07",
        "band": "harder",
        "text": "Aluminium cost more than gold in the 1850s. What single "
                "change made it cheap?",
        "options": [
            {"text": "A practical way of using electricity on an industrial "
                     "scale",
             "correct": True},
            {"text": "The discovery of bauxite, which is the ore aluminium is "
                     "extracted from and which nobody had identified as being "
                     "worth digging until then",
             "correct": False,
             "why": "Bauxite was known. What was missing was a way of getting "
                    "the metal out of it"},
            {"text": "Hotter furnaces",
             "correct": False,
             "why": "No furnace of any temperature frees aluminium with "
                    "carbon"},
            {"text": "Cheaper labour in the mines",
             "correct": False,
             "why": "Mining was never the expensive part. The extraction "
                    "was"},
        ],
        "figure": None,
    },
    {
        "id": "c9-03-h08",
        "band": "harder",
        "text": "Silver oxide gives silver when it is simply heated, with "
                "nothing added. What does that tell you about silver?",
        "options": [
            {"text": "That it is high in the series, since only a reactive "
                     "metal will take part in a reaction that has had nothing "
                     "at all added to help it along",
             "correct": False,
             "why": "Reactive metals hold their oxygen tightly. Giving it up "
                    "easily is what being low in the series means"},
            {"text": "That it is very low in the series, holding its oxygen "
                     "so weakly that heat alone is enough",
             "correct": True},
            {"text": "That silver oxide is not really a compound",
             "correct": False,
             "why": "It is a compound, and one that comes apart readily"},
            {"text": "That heating is the general method for all metals",
             "correct": False,
             "why": "It works for the very lowest few and nothing else. Most "
                    "need carbon or electricity"},
        ],
        "figure": None,
    },
    {
        "id": "c9-03-h09",
        "band": "harder",
        "text": "Three metals sit below carbon in the series and one of them "
                "is found uncombined in the ground. Why does the position not "
                "predict that on its own?",
        "options": [
            {"text": "Being found uncombined depends on where in the world "
                     "the rock is",
             "correct": False,
             "why": "It depends on reactivity everywhere. Gold is uncombined "
                    "on every continent"},
            {"text": "The series says nothing about ores",
             "correct": False,
             "why": "It says a great deal about them. It just does not draw "
                    "the line at carbon"},
            {"text": "Below carbon covers a wide range, and only the very "
                     "least reactive stay uncombined",
             "correct": True},
            {"text": "Because carbon is not a metal",
             "correct": False,
             "why": "Carbon's position works perfectly well for extraction. "
                    "It is simply not where the uncombined line falls"},
        ],
        "figure": None,
    },
    {
        "id": "c9-03-h10",
        "band": "harder",
        "text": "A works can extract a metal either with carbon or by "
                "electrolysis, and both work. Which does it choose, and why?",
        "options": [
            {"text": "Electrolysis, because it gives a purer metal in the end",
             "correct": False,
             "why": "Purity can be dealt with afterwards. The energy cost "
                    "dominates the decision"},
            {"text": "Whichever is faster",
             "correct": False,
             "why": "Speed matters less than running cost over the life of a "
                    "plant"},
            {"text": "It cannot choose — the series decides",
             "correct": False,
             "why": "The series decides what is POSSIBLE. Where both are "
                    "possible, cost decides"},
            {"text": "Carbon, because a furnace with coke in it costs far "
                     "less than the electricity would",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c9-03-h11",
        "band": "harder",
        "text": "Why is recycling aluminium described as an ENERGY decision "
                "rather than a tidiness one?",
        "options": [
            {"text": "Because the hard part of making it — removing the "
                     "oxygen — has already been paid for once",
             "correct": True},
            {"text": "Because a recycled can is chemically identical to a new "
                     "one, so the only reason anybody would prefer one over "
                     "the other is how much waste is left lying about",
             "correct": False,
             "why": "They are identical, and that is why recycling wins on "
                    "energy rather than losing on quality"},
            {"text": "Because bauxite is running out",
             "correct": False,
             "why": "Bauxite is abundant. The saving is in electricity"},
            {"text": "Because melting aluminium is difficult",
             "correct": False,
             "why": "Melting is the easy part, and it is the twentieth that "
                    "recycling still spends"},
        ],
        "figure": None,
    },
    {
        "id": "c9-03-h12",
        "band": "harder",
        "text": "A student proposes extracting sodium by heating its "
                "compound with aluminium powder instead of carbon. Would that "
                "work?",
        "options": [
            {"text": "Yes — aluminium is above carbon, so anything carbon "
                     "cannot free, aluminium can, which is exactly why "
                     "thermite works where a furnace does not",
             "correct": False,
             "why": "Aluminium reaches further down than carbon and not past "
                    "sodium. Sodium is above both"},
            {"text": "No — sodium is above aluminium in the series, so "
                     "aluminium cannot take its place",
             "correct": True},
            {"text": "Yes, but only at a very high temperature",
             "correct": False,
             "why": "Temperature cannot reverse the order. The reaction is "
                    "impossible"},
            {"text": "No, because aluminium is a metal and only non-metals "
                     "can reduce an oxide",
             "correct": False,
             "why": "Aluminium reduces iron oxide in thermite. The objection "
                    "is the position, not the kind of element"},
        ],
        "figure": None,
    },
    {
        "id": "c9-03-h13",
        "band": "harder",
        "text": "Copper's ore is roasted to an oxide before it is heated with "
                "carbon. Why does the roasting step exist?",
        "options": [
            {"text": "Because roasting drives the water out of the rock first",
             "correct": False,
             "why": "Drying happens and is a side effect. The point is to "
                    "turn the compound into an oxide"},
            {"text": "Because roasting makes the rock easier to crush",
             "correct": False,
             "why": "Crushing is done before roasting. The chemistry is what "
                    "matters here"},
            {"text": "Because the method removes OXYGEN, so the compound has "
                     "to be an oxide before it can be used",
             "correct": True},
            {"text": "Because the copper has to be melted first",
             "correct": False,
             "why": "The copper is still joined at that stage. Nothing metal "
                    "exists yet to melt"},
        ],
        "figure": None,
    },
]
