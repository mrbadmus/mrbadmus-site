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
        "text": "Why is coke — which is mostly carbon — loaded into a blast "
                "furnace along with the ore?",
        "options": [
            {"text": "To burn and supply the heat, since the reaction that "
                     "frees the iron needs a very high temperature and "
                     "nothing else in the furnace can provide one",
             "correct": False,
             "why": "It does burn and supply heat, and that is a second job. "
                    "Its main one is chemical — it takes the oxygen"},
            {"text": "To supply the carbon that takes the oxygen away from "
                     "the ore",
             "correct": True},
            {"text": "To keep the air out of the furnace",
             "correct": False,
             "why": "Air is blasted IN on purpose, which is where the name "
                    "comes from"},
            {"text": "To make the iron harder",
             "correct": False,
             "why": "Carbon in the finished iron does affect its hardness, "
                    "and that is a later step. In the furnace it takes the "
                    "oxygen"},
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

    # ── easier · MRB-338 night 3 top-up ─────────────────────────────────
    {
        "id": "c9-03-e14",
        "band": "easier",
        "text": "Zinc oxide used on the furnace bench is roasted from which "
                "ore?",
        "options": [
            {"text": "Zinc blende, a sulfide mineral of zinc",
             "correct": True},
            {"text": "Bauxite, which is aluminium's ore", "correct": False,
             "why": "Bauxite is aluminium's ore, not zinc's."},
            {"text": "Malachite", "correct": False,
             "why": "Malachite is copper's ore, and it is green rather "
                    "than white."},
            {"text": "Haematite", "correct": False,
             "why": "Not the ore named in this lesson. Zinc's ore here is "
                    "zinc blende."},
        ],
        "figure": None,
    },
    {
        "id": "c9-03-e15",
        "band": "easier",
        "text": "Which metal does malachite, the green stone in the hook, "
                "provide an ore of?",
        "options": [
            {"text": "Aluminium", "correct": False,
             "why": "Aluminium's ore is bauxite, a different rock "
                    "entirely."},
            {"text": "Zinc", "correct": False,
             "why": "Zinc's ore is zinc blende, not this green stone."},
            {"text": "Lead", "correct": False,
             "why": "Lead has its own ores, and malachite is not one of "
                    "them."},
            {"text": "Copper", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c9-03-e16",
        "band": "easier",
        "text": "Which pair of countries is named as a major source of "
                "bauxite?",
        "options": [
            {"text": "Canada and Chile", "correct": False,
             "why": "Real mining countries, and not the pair this lesson "
                    "names for bauxite."},
            {"text": "Australia and Guinea", "correct": True},
            {"text": "Wales and Cornwall, in the United Kingdom",
             "correct": False,
             "why": "Cornwall supplies the malachite in the hook, and "
                    "neither is a bauxite source here."},
            {"text": "Norway and Iceland", "correct": False,
             "why": "Not named in this lesson as bauxite sources."},
        ],
        "figure": None,
    },
    {
        "id": "c9-03-e17",
        "band": "easier",
        "text": "Which of these is NOT one of the four methods tested "
                "against a delivery on the bench?",
        "options": [
            {"text": "Melt it and pour it into a mould", "correct": True},
            {"text": "Crush it and wash it", "correct": False,
             "why": "One of the four — it is the method that works when "
                    "the metal is already uncombined."},
            {"text": "Heat it with carbon", "correct": False,
             "why": "One of the four — the route for every metal below "
                    "carbon."},
            {"text": "Pass electricity through it", "correct": False,
             "why": "One of the four — the route for every metal above "
                    "carbon."},
        ],
        "figure": None,
    },
    {
        "id": "c9-03-e18",
        "band": "easier",
        "text": "Copper oxide is heated with carbon and a gas is given off "
                "that turns limewater cloudy. What is the gas?",
        "options": [
            {"text": "Oxygen", "correct": False,
             "why": "Oxygen does not turn limewater cloudy, and the "
                    "oxygen here has left joined to the carbon."},
            {"text": "Hydrogen gas from the reaction", "correct": False,
             "why": "There is no hydrogen in this reaction to give off."},
            {"text": "Water vapour given off from the mixture",
             "correct": False,
             "why": "Water vapour does not turn limewater cloudy. Carbon "
                    "dioxide does."},
            {"text": "Carbon dioxide", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c9-03-e19",
        "band": "easier",
        "text": "Which group of metals sits ABOVE carbon in the reactivity "
                "series?",
        "options": [
            {"text": "Zinc, iron, lead and copper", "correct": False,
             "why": "That group sits below carbon, which is why carbon "
                    "can free them."},
            {"text": "Silver and gold", "correct": False,
             "why": "Those sit far below carbon, near the very bottom."},
            {"text": "Potassium, sodium, calcium, magnesium and aluminium",
             "correct": True},
            {"text": "Carbon itself, since it heads its own line",
             "correct": False,
             "why": "Carbon is the line, not a metal above it."},
        ],
        "figure": None,
    },
    {
        "id": "c9-03-e20",
        "band": "easier",
        "text": "Zinc, iron and lead can all be freed from their oxides "
                "with carbon. Which one of these four metals CANNOT join "
                "that list?",
        "options": [
            {"text": "Copper", "correct": False,
             "why": "Copper is below carbon too, and joins the list "
                    "readily."},
            {"text": "Aluminium", "correct": True},
            {"text": "Tin", "correct": False,
             "why": "Tin sits below carbon and has been smelted this way "
                    "for thousands of years."},
            {"text": "Nickel", "correct": False,
             "why": "Nickel sits below carbon as well, on the same side "
                    "as zinc, iron and lead."},
        ],
        "figure": None,
    },
    {
        "id": "c9-03-e21",
        "band": "easier",
        "text": "Which pair of metals sits far enough below carbon that heat "
                "alone can free one of them, and the other needs no "
                "chemistry at all?",
        "options": [
            {"text": "Iron and zinc", "correct": False,
             "why": "Both of those need carbon. Neither comes free with "
                    "heat alone or with nothing."},
            {"text": "Copper and lead", "correct": False,
             "why": "Both sit below carbon and both need the carbon "
                    "route."},
            {"text": "Silver and gold", "correct": True},
            {"text": "Aluminium and magnesium", "correct": False,
             "why": "Both of those sit above carbon and need electricity, "
                    "which is the opposite end of the series."},
        ],
        "figure": None,
    },
    {
        "id": "c9-03-e22",
        "band": "easier",
        "text": "Which element makes up almost all of the coke used in a "
                "blast furnace?",
        "options": [
            {"text": "Iron", "correct": False,
             "why": "Iron is what the furnace is trying to produce, not "
                    "what coke is made of."},
            {"text": "Oxygen", "correct": False,
             "why": "Oxygen is what coke takes away from the ore, not "
                    "what coke itself is."},
            {"text": "Silicon", "correct": False,
             "why": "Not the element coke is mostly made of."},
            {"text": "Carbon", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c9-03-e23",
        "band": "easier",
        "text": "What is the visible sign that copper oxide has been "
                "successfully reduced by carbon?",
        "options": [
            {"text": "The black powder turns bright blue", "correct": False,
             "why": "Blue is the colour of copper sulfate solution, not "
                    "of this reaction."},
            {"text": "Specks of pink-brown copper appear in the black "
                     "mixture", "correct": True},
            {"text": "The whole mixture turns to a colourless liquid",
             "correct": False,
             "why": "Nothing here melts into a colourless liquid."},
            {"text": "The black powder gives off a bright flame",
             "correct": False,
             "why": "No flame appears. The change is a colour change in "
                    "the solid."},
        ],
        "figure": None,
    },
    {
        "id": "c9-03-e24",
        "band": "easier",
        "text": "Which gas is given off when zinc oxide is reduced by "
                "heating with carbon?",
        "options": [
            {"text": "Carbon dioxide", "correct": True},
            {"text": "Sulfur dioxide, left over from the ore it was "
                     "roasted from", "correct": False,
             "why": "The sulfur leaves during the roasting, long before "
                    "the oxide reaches the furnace. No sulfur dioxide "
                    "comes off this reaction."},
            {"text": "Oxygen", "correct": False,
             "why": "The oxygen leaves joined to the carbon, as carbon "
                    "dioxide, rather than on its own."},
            {"text": "Nitrogen", "correct": False,
             "why": "Nitrogen plays no part in this reaction."},
        ],
        "figure": None,
    },
    {
        "id": "c9-03-e25",
        "band": "easier",
        "text": "Getting a metal out of its ore is a reaction, not a ___.",
        "options": [
            {"text": "Temperature", "correct": True},
            {"text": "The cost of extraction", "correct": False,
             "why": "Cost decides which method is chosen once a reaction "
                    "is possible. It is not the word this lesson "
                    "contrasts a reaction with."},
            {"text": "The starting compound", "correct": False,
             "why": "A compound is what the ore already is, not what "
                    "extraction is being contrasted with."},
            {"text": "The extracted metal", "correct": False,
             "why": "A metal is the product, not the wrong idea being "
                    "corrected here."},
        ],
        "figure": None,
    },
    {
        "id": "c9-03-e26",
        "band": "easier",
        "text": "The safety guidance for the copper oxide and carbon "
                "practical warns that something stays dangerous even after "
                "the flame is put out. What is it?",
        "options": [
            {"text": "The unused carbon powder", "correct": False,
             "why": "Cold carbon powder sitting in a jar is not the "
                    "hazard the warning is about."},
            {"text": "The hot residues left in the tube", "correct": True},
            {"text": "The limewater used to test the gas", "correct": False,
             "why": "Limewater is not what the warning names."},
            {"text": "The Bunsen burner's gas supply tap", "correct": False,
             "why": "Turning the gas off is what puts the flame out, not "
                    "the lingering hazard."},
        ],
        "figure": None,
    },
    {
        "id": "c9-03-e27",
        "band": "easier",
        "text": "Which substance is purified from bauxite before it is "
                "electrolysed to give aluminium?",
        "options": [
            {"text": "Aluminium chloride", "correct": False,
             "why": "The compound electrolysed here is an oxide, not a "
                    "chloride."},
            {"text": "Aluminium carbonate", "correct": False,
             "why": "Not the compound this lesson names as coming from "
                    "bauxite."},
            {"text": "Pure aluminium metal", "correct": False,
             "why": "If it were already the metal, electrolysis would "
                    "have nothing left to do."},
            {"text": "Aluminium oxide", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c9-03-e28",
        "band": "easier",
        "text": "Is carbon, the element that reduces metal oxides in a "
                "furnace, classed as a metal or a non-metal?",
        "options": [
            {"text": "A metal, since it takes the place of one in the "
                     "reaction", "correct": False,
             "why": "Doing a metal's job is not the same as being one. "
                    "Carbon is a non-metal."},
            {"text": "Neither — it is an alloy", "correct": False,
             "why": "An alloy is a mixture of metals. Carbon is a single "
                    "element."},
            {"text": "A non-metal", "correct": True},
            {"text": "A metalloid", "correct": False,
             "why": "Not the class this lesson places carbon in."},
        ],
        "figure": None,
    },
    {
        "id": "c9-03-e29",
        "band": "easier",
        "text": "Silver oxide decomposes on heating alone, with nothing "
                "added. Which gas is released?",
        "options": [
            {"text": "Carbon dioxide", "correct": False,
             "why": "There is no carbon in this reaction at all."},
            {"text": "Hydrogen", "correct": False,
             "why": "No hydrogen is involved in silver oxide breaking "
                    "apart."},
            {"text": "Oxygen", "correct": True},
            {"text": "Silver vapour", "correct": False,
             "why": "The silver is left behind as a solid. It is the gas "
                    "the question asks for."},
        ],
        "figure": None,
    },
    {
        "id": "c9-03-e30",
        "band": "easier",
        "text": "Which word equation correctly describes iron ore being "
                "reduced in a blast furnace?",
        "options": [
            {"text": "Iron oxide goes in alone; iron and oxygen come out",
             "correct": False,
             "why": "Iron oxide heated alone gives nothing. Something has "
                    "to take the oxygen."},
            {"text": "Iron and oxygen go in; iron oxide comes out",
             "correct": False,
             "why": "That is the reaction running backwards, an "
                    "oxidation rather than an extraction."},
            {"text": "Iron oxide and oxygen go in; iron and carbon dioxide "
                     "come out", "correct": False,
             "why": "Oxygen is not added to a blast furnace's ore charge. "
                    "Carbon is."},
            {"text": "Iron oxide and carbon go in; iron and carbon dioxide "
                     "come out", "correct": True},
        ],
        "figure": None,
    },

    # ── standard · MRB-338 night 3 top-up ─────────────────────────────
    {
        "id": "c9-03-s14",
        "band": "standard",
        "text": "Extracting one tonne of new aluminium from bauxite needs "
                "roughly 15,000 kWh of electricity. Recycling aluminium uses "
                "about a twentieth of that. Roughly how much electricity "
                "does recycling one tonne need?",
        "options": [
            {"text": "About 15,000 kWh — recycling still splits the same "
                     "oxide", "correct": False,
             "why": "Recycling melts metal rather than splitting a "
                    "compound, which is the whole reason it is so much "
                    "cheaper."},
            {"text": "About 7,500 kWh, since half the aluminium needs "
                     "reprocessing", "correct": False,
             "why": "A twentieth is the fraction given, not a half."},
            {"text": "About 750 kWh", "correct": True},
            {"text": "About 75 kWh, since melting takes almost no energy",
             "correct": False,
             "why": "That divides by two hundred rather than by twenty."},
        ],
        "figure": None,
    },
    {
        "id": "c9-03-s15",
        "band": "standard",
        "text": "A metal's oxide can be freed by heating alone AND by "
                "heating with carbon. What does having BOTH routes work "
                "tell you about its position?",
        "options": [
            {"text": "It sits very low in the series, near silver and gold",
             "correct": True},
            {"text": "It sits above carbon, like aluminium",
             "correct": False,
             "why": "A metal above carbon cannot be freed by carbon at "
                    "all, let alone by heat alone as well."},
            {"text": "It sits exactly level with carbon in the series",
             "correct": False,
             "why": "Carbon holds one position, not a metal sharing it."},
            {"text": "Its position cannot be worked out from this alone",
             "correct": False,
             "why": "Both routes working is itself strong evidence — only "
                    "the least reactive metals give up their oxygen this "
                    "easily."},
        ],
        "figure": None,
    },
    {
        "id": "c9-03-s16",
        "band": "standard",
        "text": "Zinc oxide reacts with carbon at the furnace's normal "
                "running temperature. If the furnace were run even hotter, "
                "what would happen to the AMOUNT of zinc produced from a "
                "fixed mass of ore?",
        "options": [
            {"text": "It would rise well beyond what the ore's zinc content "
                     "allows", "correct": False,
             "why": "No method produces more metal than the ore actually "
                    "contains."},
            {"text": "It would not increase — the reaction would simply run "
                     "faster", "correct": True},
            {"text": "It would fall, because heat above the normal running "
                     "temperature damages the zinc", "correct": False,
             "why": "Nothing about this reaction is harmed by extra heat. "
                    "The zinc itself is unaffected."},
            {"text": "It would double for every ten degrees the furnace "
                     "gets hotter", "correct": False,
             "why": "That rule applies to reaction RATE in some reactions, "
                    "never to the total amount a fixed mass of ore can "
                    "give."},
        ],
        "figure": None,
    },
    {
        "id": "c9-03-s17",
        "band": "standard",
        "text": "A student wants to find out quickly whether a new metal's "
                "oxide sits above or below carbon. What single test tells "
                "them?",
        "options": [
            {"text": "Heat the oxide with carbon and see if the metal "
                     "appears", "correct": True},
            {"text": "Weigh the oxide before and after leaving it in air "
                     "for a week", "correct": False,
             "why": "That tests how the metal reacts with the AIR, not "
                    "where it sits relative to carbon."},
            {"text": "Measure how hot the oxide has to get before it melts",
             "correct": False,
             "why": "Melting point says nothing about whether carbon can "
                    "take the oxygen."},
            {"text": "Dissolve the oxide in water and measure the pH",
             "correct": False,
             "why": "A pH change tells you about the oxide's chemistry as "
                    "a compound, not its position against carbon."},
        ],
        "figure": None,
    },
    {
        "id": "c9-03-s18",
        "band": "standard",
        "text": "Silver oxide is heated alone and nothing else is added. "
                "What would you expect to see happen?",
        "options": [
            {"text": "The dark powder gradually turns into a silvery solid, "
                     "and a gas is given off", "correct": True},
            {"text": "The dark powder melts into a silver liquid that "
                     "solidifies again on cooling", "correct": False,
             "why": "This is a chemical change into a new solid, not "
                    "melting and re-solidifying."},
            {"text": "Nothing changes, however long it is heated",
             "correct": False,
             "why": "Silver oxide is exactly the compound this lesson says "
                    "does come apart on heating alone."},
            {"text": "The powder catches fire and burns away completely",
             "correct": False,
             "why": "There is nothing here to burn. The change is the "
                    "oxide splitting apart."},
        ],
        "figure": None,
    },
    {
        "id": "c9-03-s19",
        "band": "standard",
        "text": "Iron and zinc are both freed from their oxides by heating "
                "with carbon, yet zinc's extraction needs an extra step "
                "iron's does not. What is it, and why?",
        "options": [
            {"text": "Zinc has to be re-melted afterwards, because it sets "
                     "solid the moment it forms", "correct": False,
             "why": "Iron also has to be cast into shape afterwards. That "
                    "is not what makes zinc different."},
            {"text": "Zinc boils at the furnace's temperature, so it is "
                     "condensed from a vapour", "correct": True},
            {"text": "Zinc has to be roasted twice, because one roasting "
                     "does not remove enough sulfur", "correct": False,
             "why": "Not a step this lesson describes for zinc."},
            {"text": "Zinc has to be cooled slowly, because it cracks if "
                     "it cools quickly", "correct": False,
             "why": "Cracking on cooling is not the extra step this "
                    "lesson gives for zinc."},
        ],
        "figure": None,
    },
    {
        "id": "c9-03-s20",
        "band": "standard",
        "text": "Why can one furnace loaded with carbon not extract both "
                "zinc and aluminium from their oxides?",
        "options": [
            {"text": "Because the two metals would alloy together inside "
                     "the furnace", "correct": False,
             "why": "The two ores are not being extracted at the same "
                    "time in the same furnace in the first place."},
            {"text": "Because zinc sits below carbon and aluminium sits "
                     "above it", "correct": True},
            {"text": "Because zinc and aluminium oxides need different "
                     "furnace shapes", "correct": False,
             "why": "Furnace shape is not what the reactivity series "
                    "rules on here."},
            {"text": "Because carbon runs out before it can free a second "
                     "metal", "correct": False,
             "why": "Running out of carbon is not the reason — aluminium "
                    "oxide would still resist carbon with an unlimited "
                    "supply of it."},
        ],
        "figure": None,
    },
    {
        "id": "c9-03-s21",
        "band": "standard",
        "text": "A student heats copper oxide with far too little carbon. "
                "What is the most likely result?",
        "options": [
            {"text": "Nothing reacts, because the amount of carbon has to "
                     "reach a minimum threshold first",
             "correct": False,
             "why": "Even a small amount of carbon reacts with some of "
                    "the oxide. There is no threshold below which nothing "
                    "happens."},
            {"text": "Some copper appears, but a good deal of black copper "
                     "oxide is left unreacted", "correct": True},
            {"text": "Leftover carbon is mixed in with the copper, so the "
                     "copper comes out sooty", "correct": False,
             "why": "Too LITTLE carbon means none of it is left over — "
                    "every speck reacts. What is left over here is the "
                    "black oxide that never got any carbon."},
            {"text": "The reaction happens exactly as normal, since carbon "
                     "is not used up in this reaction",
             "correct": False,
             "why": "Carbon is used up — it leaves as carbon dioxide — so "
                    "too little of it limits how much oxide can react."},
        ],
        "figure": None,
    },
    {
        "id": "c9-03-s22",
        "band": "standard",
        "text": "A student heats copper oxide and carbon powder that were "
                "never mixed properly — the carbon sits mostly on top. "
                "Why does this give a poor result?",
        "options": [
            {"text": "Because unmixed powders catch fire instead of "
                     "reacting", "correct": False,
             "why": "The powders do not catch fire either way. The problem "
                    "is contact, not combustion."},
            {"text": "Because carbon on top blocks the heat from reaching "
                     "the copper oxide underneath", "correct": False,
             "why": "Heat still reaches the oxide well enough. What is "
                    "missing is contact between the reacting substances."},
            {"text": "Because carbon that never touches copper oxide has "
                     "no oxide to take the oxygen from", "correct": True},
            {"text": "Because the reaction needs both powders to have "
                     "melted into a single liquid first",
             "correct": False,
             "why": "Neither powder needs to melt. The reaction happens "
                    "between the solids where they touch."},
        ],
        "figure": None,
    },
    {
        "id": "c9-03-s23",
        "band": "standard",
        "text": "Gold-bearing gravel needs no chemical method at all, while "
                "bauxite needs the most expensive method there is. What "
                "single fact about the two metals explains the enormous "
                "difference?",
        "options": [
            {"text": "Gold is denser than aluminium, so it settles out on "
                     "its own", "correct": False,
             "why": "Density explains why crushing and washing works for "
                    "gold. It says nothing about why bauxite is so hard "
                    "by comparison."},
            {"text": "Gold ore is far rarer than bauxite, so more care is "
                     "taken with it", "correct": False,
             "why": "Rarity affects value, not which method is needed to "
                    "free the metal."},
            {"text": "Gold and aluminium sit at opposite ends of the "
                     "series", "correct": True},
            {"text": "Aluminium has a far higher melting point than gold "
                     "does", "correct": False,
             "why": "Melting point plays no part in why carbon fails on "
                    "aluminium oxide."},
        ],
        "figure": None,
    },
    {
        "id": "c9-03-s24",
        "band": "standard",
        "text": "Lead is obtained from its oxide using a furnace with "
                "carbon, and never by electrolysis. What does that tell "
                "you about lead's position in the series?",
        "options": [
            {"text": "Lead sits above carbon", "correct": False,
             "why": "A metal above carbon could not be freed by carbon at "
                    "all. Lead can, so it must sit below it."},
            {"text": "Lead's position cannot be worked out from the method "
                     "used to extract it", "correct": False,
             "why": "The method used is exactly how a metal's position "
                    "relative to carbon is worked out."},
            {"text": "Lead sits below carbon", "correct": True},
            {"text": "Lead sits level with carbon in the series",
             "correct": False,
             "why": "Carbon occupies one position on its own, not one "
                    "shared with a metal."},
        ],
        "figure": None,
    },
    {
        "id": "c9-03-s25",
        "band": "standard",
        "text": "Why does a chemist decide which extraction method to use "
                "from a metal's position in the reactivity series, rather "
                "than simply trying each method in turn?",
        "options": [
            {"text": "Because trying a method on a metal that cannot use "
                     "it wastes fuel and time", "correct": True},
            {"text": "Because trying each method in turn is against the "
                     "law in an industrial furnace", "correct": False,
             "why": "Nothing here is a legal matter. The objection is "
                    "practical, not legal."},
            {"text": "Because the reactivity series was written down "
                     "before furnaces were ever invented", "correct": False,
             "why": "The order in which ideas were discovered is not why "
                    "the series is used to plan a method now."},
            {"text": "Because each method can be attempted once on any "
                     "given ore", "correct": False,
             "why": "A method can be tried more than once. The real cost "
                    "is the fuel and time wasted on one that cannot work."},
        ],
        "figure": None,
    },
    {
        "id": "c9-03-s26",
        "band": "standard",
        "text": "A newly identified metal reacts violently the moment it "
                "touches cold water. Based on this alone, would you expect "
                "carbon to free it from its oxide?",
        "options": [
            {"text": "Yes, because reacting with water shows it is a metal "
                     "and every metal's oxide can be freed with carbon",
             "correct": False,
             "why": "Aluminium is a metal too, and carbon cannot touch its "
                    "oxide. Being a metal is not enough."},
            {"text": "Yes, because a violent reaction with water shows the "
                     "metal is easy to react with in general",
             "correct": False,
             "why": "Reacting easily with water and giving up oxygen to "
                    "carbon are opposite ends of the series, not the same "
                    "thing."},
            {"text": "No information can be drawn from a water test about "
                     "an extraction method", "correct": False,
             "why": "The water test is exactly how the series orders "
                    "metals, and the series is what decides the method."},
            {"text": "No — reacting violently with cold water places it "
                     "high in the series, more likely above carbon than "
                     "below it", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c9-03-s27",
        "band": "standard",
        "text": "Why is it wrong to describe getting gold out of gravel as "
                "an “extraction”, in the strict sense this lesson uses the "
                "word?",
        "options": [
            {"text": "Because gold is too valuable for the word to apply "
                     "to it", "correct": False,
             "why": "Value has nothing to do with whether a process "
                    "counts as an extraction."},
            {"text": "Because the gravel is not technically an ore",
             "correct": False,
             "why": "It is an ore in the loose sense of a rock worth "
                    "processing, and that is not the objection here."},
            {"text": "Because the process takes minutes rather than the "
                     "hours a furnace needs", "correct": False,
             "why": "Speed is not what separates extraction from simple "
                    "separation."},
            {"text": "Because no chemical reaction happens — the gold is "
                     "only separated out", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c9-03-s28",
        "band": "standard",
        "text": "The copper oxide and carbon practical has been run safely "
                "in schools for decades. Why does the guidance still call "
                "for a written risk assessment every time it is done?",
        "options": [
            {"text": "Because the reaction becomes more dangerous the more "
                     "times it is repeated", "correct": False,
             "why": "The chemistry of the reaction does not change with "
                    "repetition."},
            {"text": "Because insurers require new paperwork for every "
                     "practical regardless of what it involves",
             "correct": False,
             "why": "Not the reason this lesson gives. The hazards named "
                    "are chemical ones."},
            {"text": "Because each class uses a different make of Bunsen "
                     "burner", "correct": False,
             "why": "The equipment is not what the risk assessment is "
                    "written around."},
            {"text": "Because it covers the specific hazards of strong "
                     "heating, a reducing mixture and hot residues",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c9-03-s29",
        "band": "standard",
        "text": "Silver oxide falls apart into silver and oxygen on heating "
                "alone. Copper oxide does not. Why does copper oxide need "
                "carbon added rather than simply decomposing the same way?",
        "options": [
            {"text": "Copper oxide is not a genuine compound, unlike "
                     "silver oxide", "correct": False,
             "why": "Copper oxide is a genuine compound, copper joined to "
                    "oxygen, just like silver oxide."},
            {"text": "Copper melts before it can decompose, which stops "
                     "the reaction happening", "correct": False,
             "why": "Melting is not what prevents copper oxide from "
                    "decomposing on heating alone."},
            {"text": "Silver oxide appears to decompose, though it is "
                     "being reduced by the crucible", "correct": False,
             "why": "The crucible plays no chemical part. Silver oxide "
                    "genuinely comes apart on its own."},
            {"text": "Copper holds its oxygen far more tightly than "
                     "silver does", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c9-03-s30",
        "band": "standard",
        "text": "A furnace reduces 80 kg of iron oxide and produces 56 kg "
                "of iron. What percentage of the iron oxide's mass ends up "
                "as iron?",
        "options": [
            {"text": "56%", "correct": False,
             "why": "That is simply the number 56 read as a percentage, "
                    "not 56 divided by 80."},
            {"text": "80%", "correct": False,
             "why": "That is the starting mass read as a percentage, not "
                    "the result of the division."},
            {"text": "24%", "correct": False,
             "why": "That is the mass LOST as carbon dioxide, expressed as "
                    "a percentage of the wrong starting figure."},
            {"text": "70%", "correct": True},
        ],
        "figure": None,
    },

    # ── harder · MRB-338 night 3 top-up ───────────────────────────────
    {
        "id": "c9-03-h14",
        "band": "harder",
        "text": "A recycling plant processes 500 tonnes of aluminium cans a "
                "year. New aluminium from bauxite needs about 15,000 kWh per "
                "tonne, and recycling needs about a twentieth of that. How "
                "much electricity does recycling 500 tonnes SAVE compared "
                "with extracting the same mass from bauxite?",
        "options": [
            {"text": "About 7,125,000 kWh", "correct": True},
            {"text": "About 7,500,000 kWh, since a twentieth of the total "
                     "is simply subtracted from it", "correct": False,
             "why": "A twentieth of the total is what recycling COSTS, not "
                    "what is saved."},
            {"text": "About 375,000 kWh", "correct": False,
             "why": "That treats 750 kWh as the saving per tonne rather "
                    "than as recycling's own cost per tonne."},
            {"text": "About 15,000,000 kWh, since recycling barely uses "
                     "any electricity", "correct": False,
             "why": "Recycling still uses a twentieth of the electricity, "
                    "which is not the same as using almost none of it."},
        ],
        "figure": None,
    },
    {
        "id": "c9-03-h15",
        "band": "harder",
        "text": "A start-up claims an extremely powerful electric arc "
                "furnace with carbon electrodes will finally let carbon "
                "free sodium, which sits high above carbon in the series. "
                "Evaluate the claim.",
        "options": [
            {"text": "The claim could well be true — this specific design "
                     "has not been tested on sodium oxide before",
             "correct": False,
             "why": "Sodium's position relative to carbon is already "
                    "established. No furnace was missing; the chemistry "
                    "was."},
            {"text": "The claim is wrong — sodium's position above carbon "
                     "does not change with the furnace's temperature",
             "correct": True},
            {"text": "The claim is right, because an electric arc furnace "
                     "counts as electrolysis rather than as a carbon "
                     "route", "correct": False,
             "why": "The furnace described relies on carbon electrodes "
                    "reducing the ore, not on splitting a molten "
                    "compound."},
            {"text": "The claim is wrong, though the objection given is "
                     "about licensing an arc furnace, not the chemistry",
             "correct": False,
             "why": "This lesson objects on chemical grounds. What is "
                    "permitted in a school or a works is a separate "
                    "matter."},
        ],
        "figure": None,
    },
    {
        "id": "c9-03-h16",
        "band": "harder",
        "text": "A geologist finds a lump of native platinum in a riverbed, "
                "combined with nothing else at all. Using the reasoning "
                "from this lesson, what does that suggest about platinum's "
                "position in the reactivity series?",
        "options": [
            {"text": "It is likely to sit above carbon, since the most "
                     "reactive metals survive best in a riverbed",
             "correct": False,
             "why": "A reactive metal combines with something long before "
                    "a river gets hold of it. Surviving uncombined points "
                    "the other way."},
            {"text": "Its position cannot be guessed from this, since a "
                     "river can carry any kind of rock", "correct": False,
             "why": "A river carrying any rock is beside the point. What "
                    "matters is what stays uncombined once it is there."},
            {"text": "It is likely to be very unreactive, sitting near the "
                     "bottom of the series", "correct": True},
            {"text": "It is likely to sit close to carbon, since carbon "
                     "itself is sometimes found native too",
             "correct": False,
             "why": "Carbon being found native is a fact about a "
                    "non-metal, and it says nothing about where a metal "
                    "sits."},
        ],
        "figure": None,
    },
    {
        "id": "c9-03-h17",
        "band": "harder",
        "text": "Metal X's oxide reacts with carbon only slowly, needing "
                "several hours of continuous heating at full furnace "
                "temperature, while iron's reaction under the same "
                "conditions is finished in minutes. Does this show that X "
                "sits above iron in the series?",
        "options": [
            {"text": "Yes — a slower reaction generally means a more "
                     "reactive metal, in every case", "correct": False,
             "why": "Rate and position are different measures. A slow "
                    "reaction that still finishes shows the metal is "
                    "below carbon."},
            {"text": "No — X is still below carbon, since carbon does "
                     "eventually free it; the slowness is about reaction "
                     "rate, not about position", "correct": True},
            {"text": "Yes — anything slower than iron must, by "
                     "definition, sit closer to aluminium", "correct": False,
             "why": "Slowness is not the test this lesson uses to compare "
                    "positions. Whether carbon can free the metal is."},
            {"text": "No conclusion of any kind can be drawn from a "
                     "reaction taking longer to finish", "correct": False,
             "why": "Something real follows — the reaction finishing at "
                    "all shows X is below carbon. It is the ranking "
                    "against iron that a slow finish leaves open."},
        ],
        "figure": None,
    },
    {
        "id": "c9-03-h18",
        "band": "harder",
        "text": "160 kg of iron oxide yields 112 kg of iron when it is "
                "fully reduced with carbon. A furnace processes 640 kg of "
                "iron oxide under the same conditions. How much iron is "
                "produced?",
        "options": [
            {"text": "448 kg", "correct": True},
            {"text": "112 kg, since the same 160-to-112 ratio applies "
                     "regardless of the starting mass", "correct": False,
             "why": "The ratio applies regardless of the starting mass, "
                    "but the mass it gives still scales up with it."},
            {"text": "640 kg, since the oxide converts to iron mass for "
                     "mass", "correct": False,
             "why": "Some of the mass leaves as carbon dioxide, so the "
                    "iron produced is less than the oxide that went in."},
            {"text": "914 kg", "correct": False,
             "why": "That comes from the ratio flipped the wrong way "
                    "round — 160 out of 112, rather than 112 out of 160."},
        ],
        "figure": None,
    },
    {
        "id": "c9-03-h19",
        "band": "harder",
        "text": "A metal could in theory be freed by carbon, but the "
                "reaction is so slow it would take a year to finish one "
                "batch, while electrolysis would finish the same batch in "
                "a day. Electrolysis costs roughly twenty times as much "
                "electricity. Which method should the works choose, and "
                "why?",
        "options": [
            {"text": "Carbon, because it is the cheaper route and cost is "
                     "what a works weighs above everything else",
             "correct": False,
             "why": "Cost is one factor, and a year-long batch makes the "
                    "cheap route commercially useless on its own."},
            {"text": "Neither — a method costing twenty times as much "
                     "cannot reasonably be justified", "correct": False,
             "why": "Cost alone does not settle it here. A method that "
                    "cannot deliver in a useful time is worth paying more "
                    "to avoid."},
            {"text": "Electrolysis, because a year-long batch time makes "
                     "the cheaper method uneconomic despite being "
                     "chemically possible", "correct": True},
            {"text": "Carbon, because chemical possibility is the single "
                     "thing that decides a works' choice of method",
             "correct": False,
             "why": "Chemical possibility decides what can be used. Cost "
                    "and time decide what a works chooses among the "
                    "possible methods."},
        ],
        "figure": None,
    },
    {
        "id": "c9-03-h20",
        "band": "harder",
        "text": "For every 44 kg of carbon dioxide a furnace produces while "
                "reducing copper oxide, 12 kg of that mass came from the "
                "carbon used. A furnace produces 275 kg of carbon dioxide "
                "reducing a batch of copper oxide. What mass of carbon did "
                "it use?",
        "options": [
            {"text": "100 kg, using a quarter of 275 kg as a rough match "
                     "for the ratio", "correct": False,
             "why": "A quarter is not the ratio given. 12 out of 44 is."},
            {"text": "75 kg", "correct": True},
            {"text": "12 kg, since that is the figure given in the "
                     "question", "correct": False,
             "why": "12 kg is the ratio's own figure for 44 kg of gas, not "
                    "the answer once the gas mass is 275 kg."},
            {"text": "263 kg, taking the given 12 kg straight off the "
                     "275 kg", "correct": False,
             "why": "That treats 12 kg as a fixed amount to subtract, "
                    "rather than as a ratio to scale up."},
        ],
        "figure": None,
    },
    {
        "id": "c9-03-h21",
        "band": "harder",
        "text": "Metal A is freed from its oxide by heating alone. Metal B "
                "needs heating with carbon. Metal C needs electrolysis. Put "
                "A, B and C in order from LEAST reactive to MOST reactive.",
        "options": [
            {"text": "C, then B, then A", "correct": False,
             "why": "That runs the order backwards — C, needing "
                    "electrolysis, is the most reactive of the three, not "
                    "the least."},
            {"text": "B, then A, then C", "correct": False,
             "why": "A needs nothing but heat, which makes it the least "
                    "reactive, not the middle one."},
            {"text": "The order cannot be worked out from the method used "
                     "on each one", "correct": False,
             "why": "The method used is exactly what this lesson uses to "
                    "order metals against carbon and against each other."},
            {"text": "A, then B, then C", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c9-03-h22",
        "band": "harder",
        "text": "A student argues that because carbon sits “in the "
                "middle” of the reactivity series, exactly half of all "
                "metals must be freed using it. What is wrong with this "
                "argument?",
        "options": [
            {"text": "Carbon's position splits metals into an above group "
                     "and a below group of no fixed size", "correct": True},
            {"text": "Nothing is wrong — the argument follows directly "
                     "from carbon's position", "correct": False,
             "why": "A position splitting a line into two sides does not "
                    "make the two sides equal in size."},
            {"text": "Carbon does not sit anywhere near the middle of the "
                     "series", "correct": False,
             "why": "Its rough position is not the flaw here. The flaw is "
                    "assuming a split must be equal."},
            {"text": "Carbon can free every metal below it, so the true "
                     "fraction should be closer to all metals overall",
             "correct": False,
             "why": "Carbon frees the metals below it. It has no route "
                    "to the ones above."},
        ],
        "figure": None,
    },
    {
        "id": "c9-03-h23",
        "band": "harder",
        "text": "Two students disagree about whether melting a freed metal "
                "to cast it into ingots should count as part of "
                "“extraction”. Using this lesson's own definition, who is "
                "right?",
        "options": [
            {"text": "The student who says it does count, since the metal "
                     "is not usable in its raw form", "correct": False,
             "why": "Usefulness is not what the definition turns on. "
                    "Extraction is the reaction that frees the metal from "
                    "its compound."},
            {"text": "The student who says it does not count, because "
                     "extraction is the reaction that frees the metal, and "
                     "casting happens afterward", "correct": True},
            {"text": "Neither, because this lesson gives no working "
                     "definition of “extraction” to settle it",
             "correct": False,
             "why": "A definition is given, and it is precise: getting a "
                    "metal out of its ore as the metal itself."},
            {"text": "Both, because melting and reduction are simply two "
                     "names for the same process", "correct": False,
             "why": "Melting is a physical change of state. Reduction is "
                    "a chemical change that removes oxygen."},
        ],
        "figure": None,
    },
    {
        "id": "c9-03-h24",
        "band": "harder",
        "text": "Aluminium powder mixed with iron oxide and lit with a "
                "spark can free molten iron — the thermite reaction — using "
                "nothing but aluminium. Does this contradict the rule that "
                "aluminium sits high in the series, above carbon?",
        "options": [
            {"text": "Yes — a metal that high in the series should be "
                     "unable to free anything on its own", "correct": False,
             "why": "Being high in the series is exactly what lets a "
                    "metal displace one below it. It is not a barrier to "
                    "doing so."},
            {"text": "No, though the real objection is that a spark counts "
                     "as electricity, making this electrolysis in "
                     "disguise", "correct": False,
             "why": "A spark here starts the reaction. The reaction "
                    "itself is a displacement, not electrolysis."},
            {"text": "No — it confirms it: sitting above iron lets "
                     "aluminium take iron's oxygen in a displacement",
             "correct": True},
            {"text": "Yes — aluminium sitting above carbon should stop it "
                     "reacting with any other metal's oxide too",
             "correct": False,
             "why": "Above carbon is about carbon specifically. Aluminium "
                    "can still displace metals below IT in the series."},
        ],
        "figure": None,
    },
    {
        "id": "c9-03-h25",
        "band": "harder",
        "text": "A school considers dropping its copper oxide and carbon "
                "practical in favour of an electrolysis demonstration, "
                "arguing electrolysis is “more advanced chemistry”. "
                "Evaluate this reasoning.",
        "options": [
            {"text": "It is sound reasoning — a more advanced method "
                     "teaches more chemistry than a simpler one does",
             "correct": False,
             "why": "The carbon route with copper teaches reduction, "
                    "displacement and observation just as directly as "
                    "electrolysis would."},
            {"text": "It is sound reasoning, because copper cannot be "
                     "extracted with carbon in a school laboratory",
             "correct": False,
             "why": "Copper oxide and carbon is the practical this lesson "
                    "names as the one a class is most likely to run."},
            {"text": "It is poor reasoning, though the real objection is "
                     "that electrolysis equipment is too expensive for "
                     "schools", "correct": False,
             "why": "Cost of equipment is not what this lesson's own "
                    "reasoning turns on. Matching method to the metal is."},
            {"text": "It is poor reasoning — the method fits the metal's "
                     "position and cost, not which one sounds more "
                     "advanced", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c9-03-h26",
        "band": "harder",
        "text": "A furnace fully reduces a batch of zinc oxide using a "
                "measured amount of carbon. A worker then adds MORE carbon "
                "to the same finished batch, without adding any more ore. "
                "What effect does the extra carbon have on the mass of "
                "zinc already produced?",
        "options": [
            {"text": "None — there is no oxide left for the extra carbon "
                     "to react with", "correct": True},
            {"text": "It increases the mass of zinc a little, since more "
                     "carbon gives more reducing power", "correct": False,
             "why": "Reducing power matters while oxide remains to "
                    "reduce. None remains once the batch is finished."},
            {"text": "It decreases the mass of zinc, because excess "
                     "carbon reacts with the zinc metal itself",
             "correct": False,
             "why": "Carbon does not react with zinc metal. It reacts "
                    "with zinc oxide, which is already gone."},
            {"text": "It converts some of the zinc back into zinc oxide",
             "correct": False,
             "why": "Adding carbon cannot push the reaction backwards. "
                    "Nothing here re-joins the zinc to oxygen."},
        ],
        "figure": None,
    },
    {
        "id": "c9-03-h27",
        "band": "harder",
        "text": "Suppose a furnace route costs about £300 per tonne of "
                "zinc, and electrolysis costs about twenty times as much "
                "per tonne. How much extra would it cost to produce 10 "
                "tonnes of zinc by electrolysis instead of by furnace?",
        "options": [
            {"text": "£3,000", "correct": False,
             "why": "That is simply the furnace cost for 10 tonnes, not "
                    "the extra cost of choosing electrolysis instead."},
            {"text": "£6,000", "correct": False,
             "why": "That treats electrolysis as twice the furnace cost "
                    "rather than twenty times it."},
            {"text": "£60,000, the full electrolysis cost for the whole "
                     "10 tonnes", "correct": False,
             "why": "That is the full electrolysis cost, before the "
                    "furnace cost is subtracted back out to find the "
                    "EXTRA."},
            {"text": "£57,000", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c9-03-h28",
        "band": "harder",
        "text": "A metal sits below carbon but ABOVE zinc in the series. "
                "Would you expect it to be freed more or less easily by "
                "carbon than zinc is, and why?",
        "options": [
            {"text": "More easily, since sitting closer to carbon on the "
                     "line means less distance for the reaction to cover",
             "correct": False,
             "why": "This is not a matter of physical distance on a line. "
                    "Nearness to carbon means a tighter grip on oxygen, "
                    "not an easier reaction."},
            {"text": "Equally easily, since both sit below carbon and "
                     "both can be freed by it", "correct": False,
             "why": "Both being below carbon means both CAN be freed. It "
                    "does not mean they are freed with equal ease."},
            {"text": "Less easily, though carbon can still do it — "
                     "sitting closer to carbon means holding its oxygen "
                     "more tightly than zinc does", "correct": True},
            {"text": "It cannot be freed by carbon, since it sits closer "
                     "to the metals that need electrolysis",
             "correct": False,
             "why": "Sitting below carbon, however close, still means "
                    "carbon can take its oxygen."},
        ],
        "figure": None,
    },
    {
        "id": "c9-03-h29",
        "band": "harder",
        "text": "A newly discovered metal's oxide reacts with carbon within "
                "seconds, even at a low furnace temperature — faster and "
                "more easily than any known metal oxide. Where would you "
                "predict it sits, relative to silver?",
        "options": [
            {"text": "Above silver, since reacting easily shows it holds "
                     "its oxygen firmly", "correct": False,
             "why": "Holding oxygen firmly is what makes a reaction "
                    "difficult. Reacting easily points the other way."},
            {"text": "Level with carbon, since carbon is the fastest "
                     "thing reacting with an oxide", "correct": False,
             "why": "Carbon is not an oxide reacting here. It is a metal "
                    "oxide reacting with carbon that is being placed."},
            {"text": "Its position cannot be estimated from how easily it "
                     "reacts with carbon", "correct": False,
             "why": "How easily an oxide gives up its oxygen is exactly "
                    "what this lesson uses to place a metal near the "
                    "bottom of the series."},
            {"text": "Very close to the bottom of the series, at least as "
                     "unreactive as silver", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c9-03-h30",
        "band": "harder",
        "text": "A history book claims humans could not have used iron "
                "until electricity was discovered, reasoning that “metals "
                "need electricity to be extracted”. What is wrong with "
                "this claim?",
        "options": [
            {"text": "The claim is correct, and iron tools found before "
                     "electricity must have come from meteorites instead",
             "correct": False,
             "why": "Meteoric iron is real and rare. The iron worked "
                    "through most of history came from ore, using "
                    "carbon."},
            {"text": "The claim is correct for iron specifically, though "
                     "not for the other metals below carbon",
             "correct": False,
             "why": "The claim is wrong for iron precisely because iron "
                    "sits below carbon, and the same reasoning applies to "
                    "every metal below carbon."},
            {"text": "The claim is wrong, though the objection given is "
                     "that early people generated static electricity by "
                     "accident", "correct": False,
             "why": "Nothing about the blast furnace route relies on "
                    "electricity, generated by accident or otherwise."},
            {"text": "The claim is wrong — iron sits below carbon and has "
                     "been smelted with carbon for thousands of years",
             "correct": True},
        ],
        "figure": None,
    },
]
