"""C4 lesson 03 — Word equations: twelve questions (MRB-246).

The lesson's argument is a line of grammar with chemistry inside it:
reactants on the left, products on the right, the arrow read as "makes", and
ONLY substances anywhere in it. These twelve probe the angles the mastery
ladder leaves alone — which side a named substance belongs on, what a
spectator is, what happens to a condition, and the two things a word equation
cannot do at all.

The distractors are built from the lesson's two declared misconceptions.
`REACT-06` (heat, energy or a flame written in as a reactant) drives the wrong
options in e02, s03 and h01, and h03 carries its over-corrected twin — a
student who has learnt "conditions are not substances" and applies it to the
oxygen. `REACT-05` (the arrow means equals, so the sides can swap) drives s02,
and it is behind one option in e04 and one in s04: an equation that "balances"
by having the same number of names on each side is the same belief wearing
different clothes.

A third strand runs through e01, e03, s01, h02 and h04 and is in neither
register entry, because it is not a wrong idea about equations — it is a wrong
idea about what counts as a substance. A thing you can see (bubbles, a flame),
a thing that was in the room (nitrogen, the hob), a thing in a different test
tube (limewater) and a name that covers three different compounds ("iron
oxide") are four ways of putting something in an equation that has no business
being there, and each of those five questions carries one.

Equations are written with the word "makes" rather than a typed arrow, exactly
as Design writes them in her own rung 2. The shipped font subsets contain no
U+2192, so an arrow in a question bank is a drawn mark or it is nothing.

Every question here is new prose — a question bank is the one place in these
two files where that is true, and the bar is §13's: each distractor is a WRONG
RULE in the correct answer's own shape, and each is a mistake a real student
in a real classroom makes.
"""

UNIT = "C4"
LESSON = "word-equations"
LESSON_NUMBER = 3

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "c4-03-e01",
        "band": "easier",
        "text": "A student writes: methane + oxygen makes carbon dioxide + "
                "water. Which two substances are the products?",
        "options": [
            {"text": "Carbon dioxide and water, because they are on the "
                     "right of the arrow", "correct": True},
            {"text": "Methane and oxygen, because they are on the left of "
                     "the arrow", "correct": False,
             "why": "Those two are the reactants. The left of the arrow is "
                    "what you started with; the products are what the "
                    "reaction made, and they are always on the right."},
            {"text": "Methane and carbon dioxide, because they both contain "
                     "carbon", "correct": False,
             "why": "What a substance is made of does not decide which side "
                    "it goes on. Only the arrow decides that, and methane is "
                    "on the left of it."},
            {"text": "Methane and water, because one is burned and one is "
                     "made", "correct": False,
             "why": "One of those is a reactant and one is a product, so "
                    "they cannot be listed together as products. The side of "
                    "the arrow is what groups them."},
        ],
        "figure": None,
    },
    {
        "id": "c4-03-e02",
        "band": "easier",
        "text": "A reaction is started by heating. Where does the word "
                "\"heat\" belong in the word equation?",
        "options": [
            {"text": "On the left with the reactants, because a fire cannot "
                     "start until something heats it", "correct": False,
             "why": "Heat is needed and heat is not a substance. Everything "
                    "in the line of an equation is a substance, so a "
                    "condition cannot be one of the reactants."},
            {"text": "Nowhere in the line of substances — if it is written "
                     "at all, it goes above the arrow", "correct": True},
            {"text": "On the right with the products, because burning gives "
                     "out heat you can feel", "correct": False,
             "why": "Energy really is given out, and it still is not a "
                    "substance. Neither side of a word equation is the place "
                    "for it."},
            {"text": "On whichever side is shorter, because the two sides "
                     "have to match up", "correct": False,
             "why": "The two sides of an equation are not made to match by "
                    "adding words to the short one. They already contain the "
                    "same atoms, rearranged."},
        ],
        "figure": None,
    },
    {
        "id": "c4-03-e03",
        "band": "easier",
        "text": "Magnesium is burned in air. Most of the air is nitrogen, "
                "and the nitrogen takes no part. Should nitrogen be in the "
                "word equation?",
        "options": [
            {"text": "Yes — it was in the air all around it, so it was part "
                     "of what happened", "correct": False,
             "why": "Being present is not the same as reacting. A word "
                    "equation names what reacted and what was made, and the "
                    "nitrogen did neither."},
            {"text": "Yes, on both sides, because it went in and came out "
                     "again unchanged", "correct": False,
             "why": "A substance that comes out exactly as it went in has "
                    "not taken part, so it is left out altogether rather "
                    "than written on both sides."},
            {"text": "No — only what reacts and what is made goes into a "
                     "word equation", "correct": True},
            {"text": "No — but only because there is so little of it in the "
                     "air to matter", "correct": False,
             "why": "There is more nitrogen in air than anything else. It is "
                    "left out because it took no part, not because there is "
                    "not much of it."},
        ],
        "figure": None,
    },
    {
        "id": "c4-03-e04",
        "band": "easier",
        "text": "copper carbonate makes copper oxide + carbon dioxide. How "
                "many substances were there at the start, and how many at "
                "the end?",
        "options": [
            {"text": "Two at the start and one at the end", "correct": False,
             "why": "That is this equation read backwards. One substance is "
                    "on the left of the arrow and two are on the right, so "
                    "one has broken apart into two."},
            {"text": "Three at the start, because every name in it was there "
                     "to begin with", "correct": False,
             "why": "Only the names on the left were there at the start. The "
                    "two on the right did not exist until the reaction made "
                    "them."},
            {"text": "Two on each side, because an equation always has to "
                     "balance", "correct": False,
             "why": "What balances is the ATOMS, not the number of names. "
                    "One substance can easily break apart into two."},
            {"text": "One at the start and two at the end", "correct": True},
                   ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "c4-03-s01",
        "band": "standard",
        "text": "Marble chips — calcium carbonate — are dropped into "
                "hydrochloric acid. The gas given off turns limewater in a "
                "separate tube cloudy. Which word equation describes the "
                "reaction?",
        "options": [
            {"text": "calcium carbonate + hydrochloric acid makes calcium "
                     "chloride + water + carbon dioxide", "correct": True},
            {"text": "calcium carbonate + hydrochloric acid + limewater "
                     "makes calcium chloride + water + carbon dioxide",
             "correct": False,
             "why": "The limewater was in a different tube and never met the "
                    "marble. It tested the gas afterwards, which makes it "
                    "part of a separate reaction, not this one."},
            {"text": "calcium carbonate + hydrochloric acid makes calcium "
                     "chloride + water + bubbles", "correct": False,
             "why": "Bubbles are what you saw, not a substance. The gas in "
                    "them has a name — carbon dioxide — and the equation "
                    "wants the name."},
            {"text": "calcium carbonate + acid makes calcium chloride + "
                     "water + carbon dioxide", "correct": False,
             "why": "Which acid it was decides the salt. Hydrochloric acid "
                    "gives calcium chloride; a different acid gives a "
                    "different salt, so \"acid\" is not enough."},
                   ],
        "figure": None,
    },
    {
        "id": "c4-03-s02",
        "band": "standard",
        "text": "A student writes: magnesium oxide makes magnesium + oxygen, "
                "and says it is the burning equation written backwards. Are "
                "they right?",
        "options": [
            {"text": "Yes — the arrow works like an equals sign, so the two "
                     "sides can swap", "correct": False,
             "why": "An equals sign works both ways and an arrow does not. "
                    "It records which way the reaction actually went, and "
                    "white powder does not turn back into burning metal."},
            {"text": "No — that describes a different reaction, and the "
                     "arrow says which way it went", "correct": True},
            {"text": "Yes, as long as the plus signs are kept in the same "
                     "places", "correct": False,
             "why": "Nothing about the plus signs makes a reversed equation "
                    "true. What has changed is the claim about which "
                    "substances were there first."},
            {"text": "No — the two sides would no longer have the same atoms "
                     "in them", "correct": False,
             "why": "The atoms are the same either way, which is exactly why "
                    "this looks tempting. What is wrong is the direction, "
                    "not the atoms."},
                   ],
        "figure": None,
    },
    {
        "id": "c4-03-s03",
        "band": "standard",
        "text": "Methane burns on a gas hob. Which of these belongs in the "
                "word equation?",
        "options": [
            {"text": "The flame, because you can see it and it is where the "
                     "reaction is", "correct": False,
             "why": "The flame is the reaction, seen. Nothing is made of "
                    "flame, so there is no substance there to write down."},
            {"text": "Energy, because the reaction gives out a great deal of "
                     "it", "correct": False,
             "why": "Energy is given out and energy is not a substance. It "
                    "has no place on either side of a word equation."},
            {"text": "Oxygen, because the methane reacts with the oxygen in "
                     "the air", "correct": True},
            {"text": "The hob, because the reaction could not happen without "
                     "one", "correct": False,
             "why": "The hob supplies the gas and holds the flame, and none "
                    "of it reacts. Equipment never goes into an equation."},
                   ],
        "figure": None,
    },
    {
        "id": "c4-03-s04",
        "band": "standard",
        "text": "A student writes: magnesium makes magnesium oxide. What is "
                "wrong with it?",
        "options": [
            {"text": "Nothing — the oxygen comes from the air, so it does "
                     "not need writing down", "correct": False,
             "why": "A reactant is a reactant wherever it came from. The "
                    "oxygen in the air is the easiest one in chemistry to "
                    "forget, and it is still half the reaction."},
            {"text": "The two sides should be swapped, because the powder "
                     "was there at the end", "correct": False,
             "why": "The powder is on the right already, which is where "
                    "something made by the reaction belongs. What is missing "
                    "is on the left."},
            {"text": "Magnesium oxide should be on the left as well, because "
                     "it contains the magnesium", "correct": False,
             "why": "A substance goes on the side it was on. Magnesium oxide "
                    "did not exist before the reaction, so it cannot be one "
                    "of the things you started with."},
            {"text": "The oxygen is missing, so the equation says those "
                     "atoms came from nowhere", "correct": True},
                   ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "c4-03-h01",
        "band": "harder",
        "text": "A reaction happens only when the mixture is heated "
                "strongly. How should a chemist record that on the equation?",
        "options": [
            {"text": "Above the arrow, because only substances go in the "
                     "line itself", "correct": True},
            {"text": "As an extra reactant, because the reaction cannot "
                     "happen without it", "correct": False,
             "why": "Needed and present are two different claims. Heat is "
                    "needed, and a reactant is a substance that is used up — "
                    "heat is neither a substance nor used up."},
            {"text": "As an extra product, because the heat comes back out "
                     "again afterwards", "correct": False,
             "why": "Some reactions do give out heat and some take it in, "
                    "and neither puts energy in the line of substances."},
            {"text": "In brackets at the end, so that it is not read as a "
                     "substance", "correct": False,
             "why": "Anything written in the line of an equation is read as "
                    "a substance, brackets or no brackets. There is already "
                    "a place for a condition and it is above the arrow."},
        ],
        "figure": None,
    },
    {
        "id": "c4-03-h02",
        "band": "harder",
        "text": "Carbon dioxide from the marble and acid reaction is bubbled "
                "into limewater in another tube, and the limewater turns "
                "cloudy. Should limewater be in the marble and acid equation?",
        "options": [
            {"text": "Yes — it did react with the gas, so it is part of the "
                     "same reaction", "correct": False,
             "why": "It really does react with the gas — and that is a "
                    "SECOND reaction, in a second tube, with a word equation "
                    "of its own. One equation describes one reaction."},
            {"text": "No — it never met the marble, so it took no part in "
                     "that reaction", "correct": True},
            {"text": "Yes, on the right, because the cloudiness is one of "
                     "the things produced", "correct": False,
             "why": "The cloudiness is what you saw in the other tube. The "
                    "marble and acid made calcium chloride, water and carbon "
                    "dioxide, and nothing cloudy."},
            {"text": "No — the change in the limewater is a physical one "
                     "rather than a chemical one", "correct": False,
             "why": "The limewater goes cloudy because a new insoluble "
                    "substance forms in it, which is a chemical change. It "
                    "is out of this equation because it is in a different "
                    "tube."},
                   ],
        "figure": None,
    },
    {
        "id": "c4-03-h03",
        "band": "harder",
        "text": "Why can \"methane + oxygen makes carbon dioxide + water\" "
                "not tell an engineer how much oxygen a gas hob needs?",
        "options": [
            {"text": "Oxygen is a condition rather than a reactant, so it "
                     "carries no amount", "correct": False,
             "why": "Oxygen is a substance and it is used up, which makes it "
                    "a reactant. A condition is something like heat, which "
                    "is not a substance at all."},
            {"text": "The oxygen comes out of the air, and nobody can "
                     "measure the air in a room", "correct": False,
             "why": "Air can be measured perfectly well. What is missing is "
                    "in the equation, not in the room: it gives no numbers "
                    "for anything."},
            {"text": "It names the substances and never says how many "
                     "particles of each react", "correct": True},
            {"text": "It cannot, until somebody weighs the methane and "
                     "writes the mass in", "correct": False,
             "why": "A mass written into the line would be one more thing in "
                    "there that is not a substance. What is needed is a way "
                    "to say how many particles, which is what symbols do."},
                   ],
        "figure": None,
    },
    {
        "id": "c4-03-h04",
        "band": "harder",
        "text": "Rust is often called \"iron oxide\". Why does that name "
                "make an honest word equation for rusting hard to write?",
        "options": [
            {"text": "Iron oxide is a mixture, and only compounds can go in "
                     "a word equation", "correct": False,
             "why": "Rust is a compound, not a mixture. The trouble is with "
                    "the name, which covers several different compounds at "
                    "once."},
            {"text": "Rusting is slow, and a word equation can only describe "
                     "a fast reaction", "correct": False,
             "why": "Speed makes no difference to an equation. A reaction "
                    "that takes years is written exactly the same way as one "
                    "that takes a second."},
            {"text": "Iron oxide is the name of a reactant, so it cannot "
                     "also name a product", "correct": False,
             "why": "A name goes on whichever side that substance was on in "
                    "that reaction. Nothing about a name fixes it to one "
                    "side for ever."},
            {"text": "\"Iron oxide\" names more than one compound, and rust "
                     "is a watery one", "correct": True},
                   ],
        "figure": None,
    },

    # ── easier · MRB-335 top-up ─────────────────────────────────────────
    {
        "id": "c4-03-e05",
        "band": "easier",
        "text": "In a word equation, what does the plus sign mean?",
        "options": [
            {"text": "Add up, so that the masses written on either side of it "
                     "can be totalled to give the mass of what the reaction "
                     "produces",
             "correct": False,
             "why": "It never means add. A word equation carries no masses at "
                    "all"},
            {"text": "And",
             "correct": True},
            {"text": "Makes",
             "correct": False,
             "why": "That is the arrow. The plus sign separates substances on "
                    "the same side"},
            {"text": "Or",
             "correct": False,
             "why": "Both substances take part. It is not a choice between "
                    "them"},
        ],
        "figure": None,
    },
    {
        "id": "c4-03-e06",
        "band": "easier",
        "text": "What is a condition, in the language of this lesson?",
        "options": [
            {"text": "The state a substance is in when the reaction starts, "
                     "which has to be written into the equation so that the "
                     "reader knows what was in the flask",
             "correct": False,
             "why": "States are written at GCSE, in brackets. A condition is "
                    "something else — heat, light or a catalyst"},
            {"text": "A substance that appears on the left of the arrow",
             "correct": False,
             "why": "That is a reactant, and it is exactly what a condition "
                    "is not"},
            {"text": "Something a reaction needs but is not made of — heat, "
                     "light, a catalyst",
             "correct": True},
            {"text": "The temperature the products end up at",
             "correct": False,
             "why": "A condition is supplied to the reaction rather than "
                    "produced by it"},
        ],
        "figure": None,
    },
    {
        "id": "c4-03-e07",
        "band": "easier",
        "text": "hydrogen + oxygen makes water. Which substances are the "
                "reactants?",
        "options": [
            {"text": "Water only",
             "correct": False,
             "why": "Water is on the right of the arrow, so it is the "
                    "product"},
            {"text": "Hydrogen only",
             "correct": False,
             "why": "Both substances on the left are reactants, and there are "
                    "two of them"},
            {"text": "All three, because every substance named in an equation "
                     "has taken part in the reaction it describes",
             "correct": False,
             "why": "They have all taken part, and only the ones on the LEFT "
                    "are reactants"},
            {"text": "Hydrogen and oxygen",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c4-03-e08",
        "band": "easier",
        "text": "Which of these could never appear in the line of substances "
                "in a word equation?",
        "options": [
            {"text": "Energy",
             "correct": True},
            {"text": "Oxygen",
             "correct": False,
             "why": "Oxygen is a substance and is a reactant in a great many "
                    "equations"},
            {"text": "Carbon dioxide",
             "correct": False,
             "why": "A substance, and a common product"},
            {"text": "Calcium carbonate",
             "correct": False,
             "why": "A substance, and the reactant in the marble-and-acid "
                    "equation"},
        ],
        "figure": None,
    },
    {
        "id": "c4-03-e09",
        "band": "easier",
        "text": "A student writes: zinc + copper sulfate makes zinc sulfate + "
                "copper. How should that be read out loud?",
        "options": [
            {"text": "Zinc plus copper sulfate equals zinc sulfate plus "
                     "copper, in the same way as an ordinary sum in "
                     "arithmetic would be read out",
             "correct": False,
             "why": "Plus and equals describe a sum. This is a reaction, and "
                    "the arrow only runs one way"},
            {"text": "Zinc and copper sulfate react to make zinc sulfate and "
                     "copper",
             "correct": True},
            {"text": "Zinc, added to copper sulfate, gives the same amount of "
                     "zinc sulfate and copper",
             "correct": False,
             "why": "A word equation says nothing about amounts. Reading "
                    "quantities into it is exactly the trap"},
            {"text": "Zinc sulfate and copper react to make zinc and copper "
                     "sulfate",
             "correct": False,
             "why": "That is the line read backwards, which describes a "
                    "reaction that does not happen"},
        ],
        "figure": None,
    },
    {
        "id": "c4-03-e10",
        "band": "easier",
        "text": "What is limewater used for in a word-equation question?",
        "options": [
            {"text": "As a reactant that has to be written into the equation "
                     "whenever a gas is given off, because it takes part in "
                     "collecting that gas",
             "correct": False,
             "why": "It never meets the reaction. It goes nowhere in the "
                    "equation"},
            {"text": "To speed the reaction up",
             "correct": False,
             "why": "That would be a catalyst, and limewater is not one"},
            {"text": "To test the gas and show that carbon dioxide was made",
             "correct": True},
            {"text": "To neutralise the acid at the end",
             "correct": False,
             "why": "It is alkaline, and that is not what it is used for "
                    "here. It identifies a gas"},
        ],
        "figure": None,
    },

    # ── standard · MRB-335 top-up ───────────────────────────────────────
    {
        "id": "c4-03-s05",
        "band": "standard",
        "text": "Zinc is added to hydrochloric acid and bubbles come off. "
                "Which word equation is right?",
        "options": [
            {"text": "zinc + hydrochloric acid makes zinc chloride + water",
             "correct": False,
             "why": "Water is what an acid gives with an alkali. With a metal "
                    "the second product is a gas"},
            {"text": "zinc + hydrochloric acid makes zinc chloride + "
                     "hydrogen",
             "correct": True},
            {"text": "zinc + hydrochloric acid makes zinc + hydrogen "
                     "chloride, because the acid gives up its hydrogen and "
                     "the zinc is left behind unchanged in the tube",
             "correct": False,
             "why": "The zinc does not survive unchanged — it ends up in the "
                    "salt. Hydrogen chloride IS the acid"},
            {"text": "zinc chloride makes zinc + hydrochloric acid",
             "correct": False,
             "why": "That is the reaction written backwards, which describes "
                    "something that does not happen"},
        ],
        "figure": None,
    },
    {
        "id": "c4-03-s06",
        "band": "standard",
        "text": "Hydrogen peroxide breaks down over manganese dioxide to give "
                "water and oxygen. Where does the manganese dioxide belong?",
        "options": [
            {"text": "On the left with the hydrogen peroxide, since it has to "
                     "be present for the reaction to go at any useful rate at "
                     "all",
             "correct": False,
             "why": "Being needed does not make it a reactant. It is not used "
                    "up, so it belongs above the arrow"},
            {"text": "On the right with the products",
             "correct": False,
             "why": "It is not made by the reaction. It was there before it "
                    "and is there after"},
            {"text": "Above the arrow, as a condition",
             "correct": True},
            {"text": "On both sides, because it is there at the start and at "
                     "the end",
             "correct": False,
             "why": "That is one honest way to think of it, and the "
                    "convention is to put a catalyst above the arrow"},
        ],
        "figure": None,
    },
    {
        "id": "c4-03-s07",
        "band": "standard",
        "text": "A student writes: iron + oxygen + water makes rust. What is "
                "the one thing wrong with it?",
        "options": [
            {"text": "Water should not be there, because rusting only needs "
                     "iron and oxygen and the water simply happens to be "
                     "present when it occurs",
             "correct": False,
             "why": "Water genuinely is needed for rusting. It belongs on the "
                    "left"},
            {"text": "There are three reactants, and an equation may only "
                     "have two",
             "correct": False,
             "why": "There is no limit on how many reactants an equation may "
                    "name"},
            {"text": "Oxygen should be written above the arrow",
             "correct": False,
             "why": "Oxygen is used up and ends inside the product, so it is "
                    "a reactant"},
            {"text": "Rust is not a proper substance name",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c4-03-s08",
        "band": "standard",
        "text": "sodium + water makes sodium hydroxide + hydrogen. How many "
                "reactants and how many products?",
        "options": [
            {"text": "Two reactants and two products",
             "correct": True},
            {"text": "One reactant and three products, because the sodium is "
                     "the only thing that really reacts and the water is "
                     "there as the liquid it happens in",
             "correct": False,
             "why": "The water is used up and its atoms end in the products, "
                    "so it is a reactant"},
            {"text": "Three reactants and one product",
             "correct": False,
             "why": "Count on either side of the arrow: two on the left, two "
                    "on the right"},
            {"text": "Four reactants",
             "correct": False,
             "why": "Only what is left of the arrow is a reactant. Two of "
                    "these four are products"},
        ],
        "figure": None,
    },
    {
        "id": "c4-03-s09",
        "band": "standard",
        "text": "copper carbonate makes copper oxide + carbon dioxide. What "
                "kind of reaction does that shape describe?",
        "options": [
            {"text": "Two substances joining to make one, which is what any "
                     "equation with a single product on the right of the "
                     "arrow describes",
             "correct": False,
             "why": "There is one substance on the LEFT and two on the right, "
                    "so it is the other way round"},
            {"text": "One substance breaking down into two",
             "correct": True},
            {"text": "Two substances swapping partners",
             "correct": False,
             "why": "A swap needs two reactants. Here there is only one"},
            {"text": "Nothing can be told from the shape alone",
             "correct": False,
             "why": "The shape tells you a great deal: one in, two out is a "
                    "breakdown"},
        ],
        "figure": None,
    },
    {
        "id": "c4-03-s10",
        "band": "standard",
        "text": "A student is told a reaction happens only in bright "
                "sunlight. Where does that fact go?",
        "options": [
            {"text": "On the left with the reactants, because a reaction that "
                     "cannot happen without it is plainly using it up as it "
                     "goes along",
             "correct": False,
             "why": "Being needed is not being used up as a substance. Light "
                    "is a condition"},
            {"text": "On the right with the products",
             "correct": False,
             "why": "Nothing produces sunlight here. It is supplied to the "
                    "reaction"},
            {"text": "Above the arrow",
             "correct": True},
            {"text": "It does not go anywhere, because it is not part of the "
                     "chemistry",
             "correct": False,
             "why": "It is very much part of the chemistry, and it is "
                    "recorded above the arrow rather than in the line"},
        ],
        "figure": None,
    },

    # ── harder · MRB-335 top-up ─────────────────────────────────────────
    {
        "id": "c4-03-h05",
        "band": "harder",
        "text": "A student writes: hydrogen + oxygen makes water + energy. "
                "The reaction does give out energy. What is still wrong?",
        "options": [
            {"text": "Nothing is wrong — the energy is a real product of the "
                     "reaction and leaving it out would make the equation an "
                     "incomplete description of what happens",
             "correct": False,
             "why": "Energy is real and it is not a substance. Only "
                    "substances go in the line"},
            {"text": "Energy is not a substance, so it does not belong in the "
                     "line",
             "correct": True},
            {"text": "The energy should be on the left instead",
             "correct": False,
             "why": "Neither side is the place for it. If it is recorded at "
                    "all, it goes above the arrow"},
            {"text": "Water is not the only product",
             "correct": False,
             "why": "Water is the only substance made. The fault is the extra "
                    "term"},
        ],
        "figure": None,
    },
    {
        "id": "c4-03-h06",
        "band": "harder",
        "text": "Two equations are written for the same bench: magnesium + "
                "oxygen makes magnesium oxide, and magnesium oxide makes "
                "magnesium + oxygen. Can both be right?",
        "options": [
            {"text": "Yes — they are the same equation written two ways, "
                     "because an equation works in both directions in exactly "
                     "the way an equals sign does",
             "correct": False,
             "why": "The arrow is not an equals sign. Each line describes a "
                    "different change"},
            {"text": "No — the second is impossible under any conditions",
             "correct": False,
             "why": "Metal oxides can be broken down, with enough energy. It "
                    "is simply not what the bench did"},
            {"text": "They describe two different reactions, and only the "
                     "first is the one on the bench",
             "correct": True},
            {"text": "Yes, provided the same amounts are used both times",
             "correct": False,
             "why": "Amounts are not what separates them. Direction is"},
        ],
        "figure": None,
    },
    {
        "id": "c4-03-h07",
        "band": "harder",
        "text": "Which of these word equations describes something that "
                "cannot happen, judging by the atoms alone?",
        "options": [
            {"text": "magnesium + oxygen makes magnesium oxide, which asks "
                     "one metal and one gas to produce a solid neither of "
                     "them resembles in any way at all",
             "correct": False,
             "why": "New properties are what a reaction produces. Every atom "
                    "in the product is on the left"},
            {"text": "calcium carbonate makes calcium oxide + carbon "
                     "dioxide",
             "correct": False,
             "why": "Every atom on the right is in the calcium carbonate on "
                    "the left. Nothing has come from nowhere"},
            {"text": "zinc + hydrochloric acid makes zinc chloride + "
                     "hydrogen",
             "correct": False,
             "why": "Zinc, hydrogen and chlorine are all on the left before "
                    "they appear on the right"},
            {"text": "copper + oxygen makes copper sulfate",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c4-03-h08",
        "band": "harder",
        "text": "A word equation is written for burning a candle in air, and "
                "nitrogen is left out although most of the air is nitrogen. Is "
                "that right?",
        "options": [
            {"text": "Yes — nitrogen takes no part, so it belongs nowhere in "
                     "the equation",
             "correct": True},
            {"text": "No — everything present when a reaction happens has to "
                     "be recorded, or the equation is not a full account of "
                     "what was in the flask",
             "correct": False,
             "why": "Only what reacts and what is made goes in. Being present "
                    "is not enough"},
            {"text": "No — nitrogen should be written above the arrow",
             "correct": False,
             "why": "Above the arrow is for conditions. Nitrogen is neither a "
                    "condition nor a reactant here"},
            {"text": "Yes — but only because there is so much of it",
             "correct": False,
             "why": "The amount is irrelevant. A trace of a reactant would "
                    "still belong in the line"},
        ],
        "figure": None,
    },
    {
        "id": "c4-03-h09",
        "band": "harder",
        "text": "An equation is written for a reaction whose product a "
                "student describes only as “a black solid”. What is the "
                "problem?",
        "options": [
            {"text": "That black solids are always mixtures, so no single "
                     "name would do",
             "correct": False,
             "why": "Plenty of black solids are single substances — copper "
                    "oxide for one. The trouble is the description"},
            {"text": "That an appearance is not a substance name, so the "
                     "equation does not say what was made",
             "correct": True},
            {"text": "That the colour should be written above the arrow",
             "correct": False,
             "why": "Above the arrow is for conditions. A colour is not one"},
            {"text": "Nothing, as long as the reactants are named",
             "correct": False,
             "why": "An equation has to name the products too, or it says "
                    "nothing about what the reaction made"},
        ],
        "figure": None,
    },
    {
        "id": "c4-03-h10",
        "band": "harder",
        "text": "The lesson says word equations depend on the name being "
                "agreed. Which pair of facts makes that a real problem for "
                "rusting?",
        "options": [
            {"text": "That rust is orange and iron is grey, so the two look "
                     "nothing alike",
             "correct": False,
             "why": "Colour is not the difficulty. The difficulty is that one "
                    "name covers several compounds"},
            {"text": "That rusting needs water, and water is easy to leave "
                     "out",
             "correct": False,
             "why": "A real mistake and a different one. This question is "
                    "about the name of the product"},
            {"text": "That “iron oxide” names more than one compound, and "
                     "rust is a hydrated one",
             "correct": True},
            {"text": "That rusting is slow, so the products are hard to "
                     "collect",
             "correct": False,
             "why": "Slowness makes it awkward to study and does not make the "
                    "equation dishonest"},
        ],
        "figure": None,
    },

    # ── easier · MRB-338 top-up ─────────────────────────────────────────
    {
        "id": "c4-03-e11",
        "band": "easier",
        "text": "What is written on the left of the arrow in a word "
                "equation?",
        "options": [
            {"text": "The substances the reaction made",
             "correct": False,
             "why": "Those are the products, and they go on the right"},
            {"text": "The substances you started with",
             "correct": True},
            {"text": "The conditions the reaction needed",
             "correct": False,
             "why": "Conditions go above the arrow, never in the line"},
            {"text": "The equipment the reaction was carried out in",
             "correct": False,
             "why": "Equipment goes nowhere in an equation. Only substances "
                    "appear"},
        ],
        "figure": None,
    },
    {
        "id": "c4-03-e12",
        "band": "easier",
        "text": "iron + sulfur makes iron sulfide. Which substance is the "
                "product?",
        "options": [
            {"text": "Iron",
             "correct": False,
             "why": "Iron is on the left, so it is one of the reactants"},
            {"text": "Sulfur",
             "correct": False,
             "why": "Sulfur is on the left too, and it reacted with the iron"},
            {"text": "Iron sulfide",
             "correct": True},
            {"text": "Iron and sulfur",
             "correct": False,
             "why": "Those two are what the reaction started with rather "
                    "than what it made"},
        ],
        "figure": None,
    },
    {
        "id": "c4-03-e13",
        "band": "easier",
        "text": "A student is choosing names for an equation. Which one of "
                "these names a substance?",
        "options": [
            {"text": "Stirring",
             "correct": False,
             "why": "Stirring is something you do. It is not a substance"},
            {"text": "Warmth",
             "correct": False,
             "why": "Warmth is a condition, and conditions go above the "
                    "arrow"},
            {"text": "A Bunsen burner",
             "correct": False,
             "why": "A burner is equipment, and equipment goes nowhere in an "
                    "equation"},
            {"text": "Sodium chloride",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c4-03-e14",
        "band": "easier",
        "text": "What does an arrow tell a reader that an equals sign would "
                "not?",
        "options": [
            {"text": "How much of each substance took part",
             "correct": False,
             "why": "Neither symbol says anything about amounts"},
            {"text": "How long the reaction took from start to finish",
             "correct": False,
             "why": "No part of a word equation records time"},
            {"text": "Which way the change went",
             "correct": True},
            {"text": "How hot the reaction had to be",
             "correct": False,
             "why": "Temperature is a condition, and it is written above the "
                    "arrow if it is written at all"},
        ],
        "figure": None,
    },
    {
        "id": "c4-03-e15",
        "band": "easier",
        "text": "copper + sulfur makes copper sulfide. How many "
                "reactants are there?",
        "options": [
            {"text": "One",
             "correct": False,
             "why": "There are two names on the left, and both took part"},
            {"text": "Two",
             "correct": True},
            {"text": "Three",
             "correct": False,
             "why": "Three is the number of names in the whole equation. One "
                    "of them is the product"},
            {"text": "It cannot be told from the equation",
             "correct": False,
             "why": "The equation says it plainly: everything left of the "
                    "arrow is a reactant"},
        ],
        "figure": None,
    },
    {
        "id": "c4-03-e16",
        "band": "easier",
        "text": "A reaction needs a catalyst. Where is the catalyst's name "
                "written?",
        "options": [
            {"text": "Above the arrow",
             "correct": True},
            {"text": "On the left, with the reactants",
             "correct": False,
             "why": "A reactant is used up, and a catalyst is not"},
            {"text": "On the right, with the products",
             "correct": False,
             "why": "A catalyst is not made by the reaction. It was there "
                    "beforehand"},
            {"text": "On both sides of the arrow",
             "correct": False,
             "why": "Writing it twice says it was a reactant and a product, "
                    "and it is neither"},
        ],
        "figure": None,
    },
    {
        "id": "c4-03-e17",
        "band": "easier",
        "text": "A reaction is carried out in a glass beaker. Should the "
                "beaker appear in the word equation?",
        "options": [
            {"text": "Yes, on the left, because the reaction happened inside "
                     "it",
             "correct": False,
             "why": "A reactant has to react. The beaker holds the mixture "
                    "and takes no part"},
            {"text": "Yes, above the arrow, because it was needed",
             "correct": False,
             "why": "Above the arrow is for conditions such as heat or "
                    "light, not for equipment"},
            {"text": "No, because equipment is not a substance that reacts",
             "correct": True},
            {"text": "No, because glass beakers are used in most reactions "
                     "anyway",
             "correct": False,
             "why": "How common it is decides nothing. It is left out "
                    "because it took no part"},
        ],
        "figure": None,
    },
    {
        "id": "c4-03-e18",
        "band": "easier",
        "text": "Two substances are on the same side of an equation. What is "
                "written between them?",
        "options": [
            {"text": "An arrow",
             "correct": False,
             "why": "An arrow separates the two SIDES. It does not sit "
                    "inside one of them"},
            {"text": "A plus sign",
             "correct": True},
            {"text": "An equals sign",
             "correct": False,
             "why": "No equals sign appears in a word equation anywhere"},
            {"text": "A comma",
             "correct": False,
             "why": "The convention is a plus sign, read as the word and"},
        ],
        "figure": None,
    },
    {
        "id": "c4-03-e19",
        "band": "easier",
        "text": "Magnesium is burned in air. Which substance out of the air "
                "belongs on the left of the equation?",
        "options": [
            {"text": "Oxygen",
             "correct": True},
            {"text": "Nitrogen",
             "correct": False,
             "why": "There is more nitrogen in air than anything else, and "
                    "it takes no part in this reaction"},
            {"text": "Water vapour",
             "correct": False,
             "why": "Air holds some water vapour and none of it reacts with "
                    "burning magnesium"},
            {"text": "Air",
             "correct": False,
             "why": "Air is a mixture. An equation names the substance in it "
                    "that reacted"},
        ],
        "figure": None,
    },
    {
        "id": "c4-03-e20",
        "band": "easier",
        "text": "A substance sits in the flask throughout a reaction and "
                "takes no part in it. Where does its name go?",
        "options": [
            {"text": "On the left, because it was there at the start",
             "correct": False,
             "why": "Being there at the start is not enough. A reactant has "
                    "to react"},
            {"text": "Above the arrow, as a condition",
             "correct": False,
             "why": "A condition is something the reaction needs, such as "
                    "heat or light. This is a substance that is simply "
                    "present"},
            {"text": "On both sides, because it is there before and after",
             "correct": False,
             "why": "Writing it twice claims it took part twice. It took "
                    "part not at all"},
            {"text": "Nowhere in the equation",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c4-03-e21",
        "band": "easier",
        "text": "copper + oxygen makes copper oxide. What is the oxygen in "
                "that equation?",
        "options": [
            {"text": "A product",
             "correct": False,
             "why": "It is on the left of the arrow, so it is one of the "
                    "starting substances"},
            {"text": "A condition",
             "correct": False,
             "why": "Oxygen is a substance and it is used up here, which "
                    "makes it a reactant"},
            {"text": "A catalyst",
             "correct": False,
             "why": "A catalyst is left over unchanged. This oxygen ends up "
                    "inside the copper oxide"},
            {"text": "A reactant",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c4-03-e22",
        "band": "easier",
        "text": "Every name written in the line of a word equation has to be "
                "the name of what?",
        "options": [
            {"text": "A substance",
             "correct": True},
            {"text": "An element",
             "correct": False,
             "why": "Compounds appear in equations constantly. The rule is "
                    "wider than elements"},
            {"text": "A chemical the school keeps in a bottle",
             "correct": False,
             "why": "Plenty of substances in equations are made during the "
                    "reaction and were never in a bottle"},
            {"text": "Something that can be seen happening",
             "correct": False,
             "why": "Bubbles and flames can be seen and are not substances. "
                    "Colourless gases cannot be seen and are"},
        ],
        "figure": None,
    },
    {
        "id": "c4-03-e23",
        "band": "easier",
        "text": "calcium carbonate makes calcium oxide + carbon dioxide. How "
                "many products are there?",
        "options": [
            {"text": "One",
             "correct": False,
             "why": "One is the number of reactants here. Two names sit on "
                    "the right"},
            {"text": "Two",
             "correct": True},
            {"text": "Three",
             "correct": False,
             "why": "Three is every name in the equation, and one of them is "
                    "on the left"},
            {"text": "None, because nothing new was made",
             "correct": False,
             "why": "Two substances were made that were not there before"},
        ],
        "figure": None,
    },
    {
        "id": "c4-03-e24",
        "band": "easier",
        "text": "zinc + sulfuric acid makes zinc sulfate + hydrogen. Which "
                "two substances were in the flask before the reaction?",
        "options": [
            {"text": "Zinc sulfate and hydrogen",
             "correct": False,
             "why": "Those two are on the right, so the reaction made them"},
            {"text": "Zinc and zinc sulfate",
             "correct": False,
             "why": "One of those is a reactant and one is a product, so "
                    "they cannot be paired"},
            {"text": "Zinc and sulfuric acid",
             "correct": True},
            {"text": "Sulfuric acid and the hydrogen gas",
             "correct": False,
             "why": "The hydrogen came out of the acid during the reaction "
                    "and was not there as a gas beforehand"},
        ],
        "figure": None,
    },
    {
        "id": "c4-03-e25",
        "band": "easier",
        "text": "Which of these can a word equation not tell you?",
        "options": [
            {"text": "Which substances were there first",
             "correct": False,
             "why": "It names them, and that is half of what it is for"},
            {"text": "Which substances the reaction made",
             "correct": False,
             "why": "They are on the right of the arrow, named"},
            {"text": "Which way the change went",
             "correct": False,
             "why": "The arrow says exactly that"},
            {"text": "How many particles of each substance react",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c4-03-e26",
        "band": "easier",
        "text": "potassium hydroxide + nitric acid makes potassium nitrate "
                "+ water. How many substances are named altogether?",
        "options": [
            {"text": "Two",
             "correct": False,
             "why": "Two is the count on one side. The question asks about "
                    "the whole line"},
            {"text": "Three",
             "correct": False,
             "why": "There are two names on each side of the arrow"},
            {"text": "Four",
             "correct": True},
            {"text": "Five, counting the arrow",
             "correct": False,
             "why": "The arrow is not a substance and is never counted as "
                    "one"},
        ],
        "figure": None,
    },
    {
        "id": "c4-03-e27",
        "band": "easier",
        "text": "Which of these would be written above the arrow rather than "
                "in the line?",
        "options": [
            {"text": "Oxygen",
             "correct": False,
             "why": "Oxygen is a substance and is used up, so it is a "
                    "reactant"},
            {"text": "Water",
             "correct": False,
             "why": "Water is a substance. It goes on whichever side it "
                    "belongs to"},
            {"text": "Carbon dioxide",
             "correct": False,
             "why": "A substance, and usually a product. It belongs in the "
                    "line"},
            {"text": "Heat",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c4-03-e28",
        "band": "easier",
        "text": "A reaction gives off a gas that you can see bubbling out of "
                "the liquid. What should be written in the equation?",
        "options": [
            {"text": "The word bubbles",
             "correct": False,
             "why": "Bubbles are what you saw. The equation wants what the "
                    "gas is"},
            {"text": "The name of the gas",
             "correct": True},
            {"text": "The word fizzing",
             "correct": False,
             "why": "Fizzing describes the sight and the sound rather than a "
                    "substance"},
            {"text": "Nothing, because a gas escapes from the flask",
             "correct": False,
             "why": "A gas that was made by the reaction is a product, "
                    "whether it stays or leaves"},
        ],
        "figure": None,
    },
    {
        "id": "c4-03-e29",
        "band": "easier",
        "text": "hydrogen + oxygen makes water. Was there any water in the "
                "flask before the reaction?",
        "options": [
            {"text": "Yes, hidden inside the two gases",
             "correct": False,
             "why": "Nothing is hidden. The water was assembled from the "
                    "atoms in the two gases"},
            {"text": "Yes, because water is on both sides",
             "correct": False,
             "why": "Water is on the right of the arrow only"},
            {"text": "No — it is on the right, so the reaction made it",
             "correct": True},
            {"text": "No, because water is never in an equation",
             "correct": False,
             "why": "Water appears in a great many equations, on either side"},
        ],
        "figure": None,
    },
    {
        "id": "c4-03-e30",
        "band": "easier",
        "text": "An equation has two names on the left of the arrow. What "
                "does that tell you?",
        "options": [
            {"text": "Two substances were made",
             "correct": False,
             "why": "What was made is on the right of the arrow"},
            {"text": "The reaction happened twice over",
             "correct": False,
             "why": "How many times a reaction is run is not something an "
                    "equation records"},
            {"text": "Twice as much of one substance was used",
             "correct": False,
             "why": "A word equation carries no amounts of any kind"},
            {"text": "Two substances reacted together",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c4-03-e31",
        "band": "easier",
        "text": "Which of these is a condition rather than a substance?",
        "options": [
            {"text": "Light",
             "correct": True},
            {"text": "Hydrogen",
             "correct": False,
             "why": "A gas, and a substance. It goes in the line"},
            {"text": "Limewater",
             "correct": False,
             "why": "A liquid you can pour, and a substance"},
            {"text": "Copper oxide",
             "correct": False,
             "why": "A black powder, and a substance"},
        ],
        "figure": None,
    },
    {
        "id": "c4-03-e32",
        "band": "easier",
        "text": "Some equations are written with the word makes in place of "
                "an arrow. What does that word stand for?",
        "options": [
            {"text": "The plus sign",
             "correct": False,
             "why": "The plus sign is read as and, and it separates "
                    "substances on one side"},
            {"text": "The arrow",
             "correct": True},
            {"text": "An equals sign",
             "correct": False,
             "why": "Makes runs one way, and an equals sign runs both. They "
                    "are not the same claim"},
            {"text": "The word and",
             "correct": False,
             "why": "And is the plus sign. Makes separates the two sides"},
        ],
        "figure": None,
    },

    # ── standard · MRB-338 top-up ───────────────────────────────────────
    {
        "id": "c4-03-s11",
        "band": "standard",
        "text": "Sodium hydroxide solution is neutralised by nitric acid. "
                "Sodium nitrate and water are left in the beaker. Which word "
                "equation is right?",
        "options": [
            {"text": "sodium hydroxide + nitric acid makes sodium nitrate + "
                     "water",
             "correct": True},
            {"text": "sodium hydroxide + acid makes sodium nitrate + water",
             "correct": False,
             "why": "Which acid it was decides the salt. Nitric acid gives a "
                    "nitrate, and another acid would give something else"},
            {"text": "sodium hydroxide + nitric acid makes sodium chloride + "
                     "water",
             "correct": False,
             "why": "A chloride would need chlorine, and there is none in "
                    "either reactant"},
            {"text": "sodium nitrate + water makes sodium hydroxide + nitric "
                     "acid",
             "correct": False,
             "why": "That is the line reversed, and it claims the salt "
                    "solution turned itself back into acid and alkali"},
        ],
        "figure": None,
    },
    {
        "id": "c4-03-s12",
        "band": "standard",
        "text": "Magnesium is dropped into blue copper sulfate solution. "
                "Magnesium sulfate forms and copper settles out. Which word "
                "equation is right?",
        "options": [
            {"text": "magnesium + copper sulfate makes magnesium sulfate + "
                     "blue colour",
             "correct": False,
             "why": "Colour is something you see. The substance that comes "
                    "out has a name, and it is copper"},
            {"text": "magnesium + copper sulfate makes magnesium sulfate + "
                     "copper",
             "correct": True},
            {"text": "magnesium + sulfate makes magnesium sulfate + copper",
             "correct": False,
             "why": "The reactant is copper sulfate. Dropping the copper "
                    "from its name leaves the copper on the right "
                    "unexplained"},
            {"text": "magnesium sulfate + copper makes magnesium + copper "
                     "sulfate",
             "correct": False,
             "why": "That is the reaction written backwards, and it "
                    "describes something the beaker did not do"},
        ],
        "figure": None,
    },
    {
        "id": "c4-03-s13",
        "band": "standard",
        "text": "A plant uses water and carbon dioxide to make glucose and "
                "oxygen, and the reaction happens only in light. Which word "
                "equation is right?",
        "options": [
            {"text": "carbon dioxide + water + light makes glucose + oxygen",
             "correct": False,
             "why": "Light is needed and light is not a substance. It "
                    "belongs above the arrow"},
            {"text": "carbon dioxide + water makes glucose + oxygen, with "
                     "light written above the arrow",
             "correct": True},
            {"text": "glucose + oxygen makes carbon dioxide + water, with "
                     "light above the arrow",
             "correct": False,
             "why": "That is the line the other way round, which describes a "
                    "different change altogether"},
            {"text": "carbon dioxide + water makes glucose + oxygen + light",
             "correct": False,
             "why": "The light is supplied to this reaction rather than made "
                    "by it, and either way it is not a substance"},
        ],
        "figure": None,
    },
    {
        "id": "c4-03-s14",
        "band": "standard",
        "text": "In a blast furnace, carbon monoxide reacts with iron oxide "
                "and gives iron and carbon dioxide. Which substances go on "
                "the left of the arrow?",
        "options": [
            {"text": "Carbon monoxide and iron oxide",
             "correct": True},
            {"text": "Iron oxide only, because the carbon monoxide is blown "
                     "through the furnace rather than fed into it",
             "correct": False,
             "why": "A reactant is a reactant however it arrives. The carbon "
                    "monoxide is used up, so it goes on the left"},
            {"text": "Iron and carbon dioxide",
             "correct": False,
             "why": "Those two are made by the reaction, so they belong on "
                    "the right"},
            {"text": "All four substances, because all four are involved",
             "correct": False,
             "why": "Being involved does not put a substance on the left. "
                    "The side records when it was there"},
        ],
        "figure": None,
    },
    {
        "id": "c4-03-s15",
        "band": "standard",
        "text": "An electric current is passed through water and two gases "
                "bubble off: hydrogen and oxygen. Which word equation is "
                "right?",
        "options": [
            {"text": "water + electricity makes hydrogen + oxygen",
             "correct": False,
             "why": "Electricity is a condition rather than a substance, so "
                    "it goes above the arrow if it goes anywhere"},
            {"text": "water makes bubbles + oxygen",
             "correct": False,
             "why": "Bubbles are what you saw. The gas inside them is "
                    "hydrogen and the equation wants its name"},
            {"text": "water makes hydrogen + oxygen",
             "correct": True},
            {"text": "hydrogen + oxygen makes water",
             "correct": False,
             "why": "That is the reverse reaction, which is what happens "
                    "when the two gases are lit rather than what happened "
                    "here"},
        ],
        "figure": None,
    },
    {
        "id": "c4-03-s16",
        "band": "standard",
        "text": "Coal contains sulfur. When it is burned, the sulfur reacts "
                "with oxygen and sulfur dioxide goes up the chimney. Which "
                "equation describes that part of the burning?",
        "options": [
            {"text": "sulfur + coal makes sulfur dioxide",
             "correct": False,
             "why": "The sulfur is in the coal rather than reacting with it. "
                    "What it reacts with is the oxygen"},
            {"text": "sulfur + oxygen makes sulfur dioxide",
             "correct": True},
            {"text": "sulfur + smoke makes sulfur dioxide",
             "correct": False,
             "why": "Smoke is a mixture you can see, and an equation names "
                    "the substance that reacted"},
            {"text": "sulfur dioxide makes sulfur + oxygen",
             "correct": False,
             "why": "That is the line reversed. It says the chimney gas "
                    "broke apart, which is not what happened"},
        ],
        "figure": None,
    },
    {
        "id": "c4-03-s17",
        "band": "standard",
        "text": "A student writes an equation ending in the word salt. Why "
                "is that not good enough?",
        "options": [
            {"text": "Because salt is a mixture, and mixtures cannot be "
                     "written into an equation at all",
             "correct": False,
             "why": "The salts made by reactions are compounds. The trouble "
                    "is that the word covers many of them"},
            {"text": "Because salt names a whole family of substances rather "
                     "than one",
             "correct": True},
            {"text": "Because salt is an everyday word, and equations use "
                     "chemical symbols in place of everyday words",
             "correct": False,
             "why": "Word equations use words. What they need is a word that "
                    "names one substance"},
            {"text": "Because salt is a reactant, so it cannot be written on "
                     "the right of the arrow",
             "correct": False,
             "why": "A salt is very often the product. Which side it goes on "
                    "depends on the reaction"},
        ],
        "figure": None,
    },
    {
        "id": "c4-03-s18",
        "band": "standard",
        "text": "In which of these has a substance been written on the wrong "
                "side of the arrow?",
        "options": [
            {"text": "iron + sulfur makes iron sulfide",
             "correct": False,
             "why": "The two elements are on the left and the compound they "
                    "made is on the right, which is correct"},
            {"text": "zinc + hydrochloric acid makes zinc chloride + "
                     "hydrogen",
             "correct": False,
             "why": "The metal and acid start, the salt and the gas are "
                    "made. Both sides are right"},
            {"text": "calcium carbonate makes calcium oxide + carbon dioxide",
             "correct": False,
             "why": "One substance broke down into two, and the equation "
                    "says so correctly"},
            {"text": "sodium + water + hydrogen makes sodium hydroxide",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c4-03-s19",
        "band": "standard",
        "text": "Which of these equations has something in the line that is "
                "not a substance?",
        "options": [
            {"text": "copper carbonate makes copper oxide + carbon dioxide",
             "correct": False,
             "why": "All three names are substances, and the sides are right"},
            {"text": "silver chloride + light makes silver + chlorine",
             "correct": True},
            {"text": "sodium + water makes sodium hydroxide + hydrogen",
             "correct": False,
             "why": "Four substances and nothing else in the line"},
            {"text": "carbon + oxygen makes carbon dioxide",
             "correct": False,
             "why": "Two elements and one compound, all of them substances"},
        ],
        "figure": None,
    },
    {
        "id": "c4-03-s20",
        "band": "standard",
        "text": "One student writes calcium carbonate + acid, and another "
                "writes calcium carbonate + hydrochloric acid. Which is "
                "better, and why?",
        "options": [
            {"text": "The first, because it covers every acid the reaction "
                     "would work with",
             "correct": False,
             "why": "Covering several acids is the problem. Each one gives a "
                    "different salt, so the products would change"},
            {"text": "The second, because the acid decides which salt is "
                     "made",
             "correct": True},
            {"text": "The first, because a shorter equation is easier for a "
                     "reader to follow quickly",
             "correct": False,
             "why": "Shortness is worth nothing if the equation no longer "
                    "says which substances reacted"},
            {"text": "Neither, because an acid is a condition rather than a "
                     "substance",
             "correct": False,
             "why": "An acid is a substance, and it is used up in the "
                    "reaction, which makes it a reactant"},
        ],
        "figure": None,
    },
    {
        "id": "c4-03-s21",
        "band": "standard",
        "text": "A gas given off by a reaction is tested with a lit splint "
                "and pops. Should the splint be written into the equation?",
        "options": [
            {"text": "Yes, on the left, because it started the pop",
             "correct": False,
             "why": "The splint tested the gas after the first reaction was "
                    "over. It is no part of that equation"},
            {"text": "Yes, above the arrow, because it was needed for the "
                     "test",
             "correct": False,
             "why": "Above the arrow is for conditions the reaction itself "
                    "needed, and this one needed no splint"},
            {"text": "No, because a splint is made of wood, not a chemical",
             "correct": False,
             "why": "Wood is a substance too. It is left out because it took "
                    "no part in the reaction being described"},
            {"text": "No, because a test done afterwards is not part of the "
                     "reaction",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c4-03-s22",
        "band": "standard",
        "text": "Which of these is a word equation rather than a description "
                "of what happened?",
        "options": [
            {"text": "Magnesium burned brightly in air and left a white "
                     "powder behind in the dish it was held over",
             "correct": False,
             "why": "That is a description. It never names what the "
                    "magnesium reacted with or what the powder is"},
            {"text": "Magnesium reacts with oxygen when it is heated "
                     "strongly enough to catch",
             "correct": False,
             "why": "A sentence about the reaction, and it names no product "
                    "and has no arrow"},
            {"text": "magnesium + oxygen makes magnesium oxide",
             "correct": True},
            {"text": "The white powder weighed more than the ribbon that was "
                     "burned to make it",
             "correct": False,
             "why": "A true observation about mass, and not an equation at "
                    "all"},
        ],
        "figure": None,
    },
    {
        "id": "c4-03-s23",
        "band": "standard",
        "text": "sodium + chlorine makes sodium chloride. What does the "
                "equation claim about sodium chloride?",
        "options": [
            {"text": "That it was made by the reaction and was not there "
                     "before",
             "correct": True},
            {"text": "That it is a mixture of the sodium and the chlorine",
             "correct": False,
             "why": "The arrow says a reaction happened, so the product is a "
                    "compound rather than a mixture"},
            {"text": "That it weighs the same as the sodium did",
             "correct": False,
             "why": "A word equation carries no masses. The chlorine is in "
                    "there too"},
            {"text": "That it can be turned back into sodium and chlorine by "
                     "reversing the arrow",
             "correct": False,
             "why": "An arrow records which way this reaction went. It gives "
                    "no permission to run it backwards"},
        ],
        "figure": None,
    },
    {
        "id": "c4-03-s24",
        "band": "standard",
        "text": "An equation saying water turns into hydrogen and oxygen "
                "is correct, and yet a glass of water does not fall apart on "
                "its own. What has the equation left out?",
        "options": [
            {"text": "The conditions the reaction needs, which go above the "
                     "arrow",
             "correct": True},
            {"text": "The second reactant, which is missing from the left of "
                     "the arrow",
             "correct": False,
             "why": "There is no second reactant. Water alone gives both "
                    "gases"},
            {"text": "The third product, which is missing from the right",
             "correct": False,
             "why": "Hydrogen and oxygen are all that is made. Nothing is "
                    "missing from the right"},
            {"text": "The time the reaction takes to finish",
             "correct": False,
             "why": "No word equation records time, and that is not what "
                    "makes this one look wrong"},
        ],
        "figure": None,
    },
    {
        "id": "c4-03-s25",
        "band": "standard",
        "text": "A copper strip is left in zinc sulfate solution for an hour "
                "and nothing changes. What word equation should be written?",
        "options": [
            {"text": "copper + zinc sulfate makes copper sulfate + zinc",
             "correct": False,
             "why": "That equation claims a reaction happened, and the "
                    "beaker says none did"},
            {"text": "copper + zinc sulfate makes nothing",
             "correct": False,
             "why": "Nothing is not a substance, so it cannot be written as "
                    "a product"},
            {"text": "copper + zinc sulfate makes copper + zinc sulfate",
             "correct": False,
             "why": "Both sides the same says a reaction happened and "
                    "changed nothing, which is not what an equation is for"},
            {"text": "None, because no reaction took place",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c4-03-s26",
        "band": "standard",
        "text": "A reaction makes two products, and one of them stays "
                "dissolved in the liquid instead of being seen. Should it be "
                "in the equation?",
        "options": [
            {"text": "No, because a substance that dissolves has not "
                     "properly been made yet",
             "correct": False,
             "why": "It has been made, and dissolving is simply where it "
                    "went"},
            {"text": "No, because only the products you can see are written "
                     "down",
             "correct": False,
             "why": "Seeing has nothing to do with it. Colourless gases are "
                    "written in every day"},
            {"text": "Yes, but it is written above the arrow rather than in "
                     "the line",
             "correct": False,
             "why": "Above the arrow is for conditions. A product goes on "
                    "the right"},
            {"text": "Yes, because it is a substance the reaction made",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c4-03-s27",
        "band": "standard",
        "text": "Which of these equations shows two substances swapping "
                "partners?",
        "options": [
            {"text": "copper carbonate makes copper oxide + carbon dioxide",
             "correct": False,
             "why": "One substance broke down into two. There is nothing for "
                    "it to swap with"},
            {"text": "iron + sulfur makes iron sulfide",
             "correct": False,
             "why": "Two substances joined into one, which is the opposite "
                    "shape"},
            {"text": "sodium hydroxide + hydrochloric acid makes sodium "
                     "chloride + water",
             "correct": True},
            {"text": "carbon + oxygen makes carbon dioxide",
             "correct": False,
             "why": "Another joining reaction, with one product and no swap"},
        ],
        "figure": None,
    },
    {
        "id": "c4-03-s28",
        "band": "standard",
        "text": "An equation reads: X + Y makes Z. What must be true of the "
                "atoms in Z?",
        "options": [
            {"text": "Every one of them came from X or from Y",
             "correct": True},
            {"text": "They are new atoms, made when X and Y met each other",
             "correct": False,
             "why": "A reaction makes no atoms. It rearranges the ones it is "
                    "given"},
            {"text": "Half came from X and half came from Y",
             "correct": False,
             "why": "The share can be anything. What is fixed is that the "
                    "two reactants are the only source"},
            {"text": "They are the atoms of X, with the atoms of Y left over "
                     "unchanged",
             "correct": False,
             "why": "Y is on the left, so it reacted. Its atoms are in the "
                    "product as well"},
        ],
        "figure": None,
    },
    {
        "id": "c4-03-s29",
        "band": "standard",
        "text": "Can the products of a reaction be worked out from the "
                "reactants on their own?",
        "options": [
            {"text": "Yes, because two substances can react in one way and "
                     "no other",
             "correct": False,
             "why": "The same two substances can give different products "
                    "under different conditions"},
            {"text": "Yes, because the equation is written before the "
                     "experiment",
             "correct": False,
             "why": "An equation records what a reaction did. It is not a "
                    "prediction made in advance"},
            {"text": "No, because the reactants put a limit on the products "
                     "without fixing them",
             "correct": True},
            {"text": "No, because the products depend on the conditions "
                     "rather than on the reactants used",
             "correct": False,
             "why": "They have everything to do with them: every atom in a "
                    "product came from a reactant"},
        ],
        "figure": None,
    },
    {
        "id": "c4-03-s30",
        "band": "standard",
        "text": "Ammonia is made from nitrogen and hydrogen, over iron, "
                "which is unchanged at the end. Which word equation is "
                "right?",
        "options": [
            {"text": "nitrogen + hydrogen + iron makes ammonia",
             "correct": False,
             "why": "The iron is not used up, so it is not a reactant. It "
                    "goes above the arrow"},
            {"text": "nitrogen + hydrogen makes ammonia + iron",
             "correct": False,
             "why": "The iron was there at the start and was not made by the "
                    "reaction"},
            {"text": "ammonia makes nitrogen + hydrogen, with iron written "
                     "above the arrow",
             "correct": False,
             "why": "That is the line reversed, and it describes ammonia "
                    "breaking apart instead of being made"},
            {"text": "nitrogen + hydrogen makes ammonia, with iron written "
                     "above the arrow",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c4-03-s31",
        "band": "standard",
        "text": "A student writes the products first because they were "
                "recorded first in the lab book. Does the order matter?",
        "options": [
            {"text": "No, because both sides hold the same atoms in the end "
                     "whichever way they are written down",
             "correct": False,
             "why": "The atoms do match, and the sides still make different "
                    "claims about which substances came first"},
            {"text": "No, as long as the plus signs stay where they are",
             "correct": False,
             "why": "Nothing about the plus signs decides which substances "
                    "were there at the start"},
            {"text": "Yes, because the equation would then have too many "
                     "substances on one side of the arrow",
             "correct": False,
             "why": "The count on each side is unchanged by swapping them. "
                    "What changes is what the line claims"},
            {"text": "Yes, because the side a substance is on says when it "
                     "was there",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c4-03-s32",
        "band": "standard",
        "text": "Carbon dioxide is bubbled into limewater and a white solid, "
                "calcium carbonate, forms in it. Which equation describes "
                "that test?",
        "options": [
            {"text": "carbon dioxide + limewater makes calcium carbonate + "
                     "water",
             "correct": True},
            {"text": "carbon dioxide + limewater makes cloudiness",
             "correct": False,
             "why": "Cloudiness is what you see. The substance that makes it "
                    "cloudy has a name"},
            {"text": "calcium carbonate + water makes carbon dioxide + "
                     "limewater",
             "correct": False,
             "why": "That is the test written backwards, which is not what "
                    "the tube did"},
            {"text": "limewater makes calcium carbonate + water",
             "correct": False,
             "why": "Leaving the gas out says the carbon came from nowhere. "
                    "The gas is a reactant here"},
        ],
        "figure": None,
    },

    # ── harder · MRB-338 top-up ─────────────────────────────────────────
    {
        "id": "c4-03-h11",
        "band": "harder",
        "text": "A textbook prints the line: metal + acid makes salt + "
                "hydrogen. What is that line good for, and what can it not "
                "do?",
        "options": [
            {"text": "It is a pattern for a family of reactions, and it "
                     "names no particular substances",
             "correct": True},
            {"text": "It is a word equation for one reaction, and it leaves "
                     "out the conditions that reaction needs",
             "correct": False,
             "why": "It describes no single reaction. Metal and salt each "
                    "stand for a whole family"},
            {"text": "It is a word equation that works for every metal, and "
                     "it cannot say how fast the reaction goes",
             "correct": False,
             "why": "It does not work for every metal — copper gives no "
                    "hydrogen with dilute acid — and speed is not the point"},
            {"text": "It is a pattern, and it cannot be used until the salt "
                     "has been weighed",
             "correct": False,
             "why": "No weighing turns a pattern into an equation. Naming "
                    "the actual substances does"},
        ],
        "figure": None,
    },
    {
        "id": "c4-03-h12",
        "band": "harder",
        "text": "Limewater in a second tube is kept out of the marble and "
                "acid equation. A student says the carbon dioxide should be "
                "left out for the same reason. What is wrong with that?",
        "options": [
            {"text": "Nothing is wrong: a substance that ends up in another "
                     "tube belongs in that tube's equation only",
             "correct": False,
             "why": "Where a substance goes afterwards is not the test. The "
                    "carbon dioxide was MADE by this reaction"},
            {"text": "The carbon dioxide was made by this reaction, so it is "
                     "one of its products",
             "correct": True},
            {"text": "The carbon dioxide is a condition of the reaction, so "
                     "it belongs above the arrow rather than in the line",
             "correct": False,
             "why": "It is a substance the reaction produced, which makes it "
                    "a product and never a condition"},
            {"text": "The limewater should be in the equation as well, so "
                     "the student has the wrong rule twice over",
             "correct": False,
             "why": "The limewater is correctly left out. Only the second "
                    "half of the student's reasoning fails"},
        ],
        "figure": None,
    },
    {
        "id": "c4-03-h13",
        "band": "harder",
        "text": "A student checks equations by counting the names on each "
                "side and calling an equation right when the counts match. "
                "Evaluate that method.",
        "options": [
            {"text": "It works, because a reaction cannot make more "
                     "substances than it started with",
             "correct": False,
             "why": "One substance can break into two, and two can join into "
                    "one. The counts need not match"},
            {"text": "It works for breakdown reactions and fails for the "
                     "rest, which is why it is unsafe",
             "correct": False,
             "why": "It fails for breakdowns in particular, where one name "
                    "on the left gives two on the right"},
            {"text": "It fails, because what has to match is the atoms and "
                     "not the number of names",
             "correct": True},
            {"text": "It fails, because names cannot be counted until the "
                     "amounts of each substance are known",
             "correct": False,
             "why": "Names can be counted easily. The trouble is that the "
                    "count proves nothing"},
        ],
        "figure": None,
    },
    {
        "id": "c4-03-h14",
        "band": "harder",
        "text": "Water can be split into hydrogen and oxygen with "
                "electricity, and hydrogen burns in oxygen to give water. A "
                "student says one of those two equations must be wrong. What "
                "is the answer?",
        "options": [
            {"text": "The burning one is right, because a substance cannot "
                     "be taken apart once it has been made",
             "correct": False,
             "why": "Compounds are taken apart every day. Splitting water is "
                    "a real reaction"},
            {"text": "The splitting one is right, because an arrow points "
                     "one way and the reverse line is not allowed",
             "correct": False,
             "why": "The reverse line is allowed when the reverse reaction "
                    "really happens, and here it does"},
            {"text": "Neither is right, because the two lines contradict "
                     "each other about which substances react",
             "correct": False,
             "why": "There is no contradiction. Each line records a "
                    "different change, in a different set of conditions"},
            {"text": "Both are right: they describe two different reactions, "
                     "under different conditions",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c4-03-h15",
        "band": "harder",
        "text": "Why can a word equation not tell a chemist whether a "
                "reaction will take a second or a year?",
        "options": [
            {"text": "Because the time depends on the amounts, and amounts "
                     "are written above the arrow instead",
             "correct": False,
             "why": "Nothing about amounts is written anywhere in a word "
                    "equation, above the arrow or in the line"},
            {"text": "Because it records only which substances took part, "
                     "and nothing about how the change ran",
             "correct": True},
            {"text": "Because a slow reaction is written with a different "
                     "arrow from a fast one",
             "correct": False,
             "why": "There is one arrow, and it says the same thing however "
                    "long the reaction takes"},
            {"text": "Because a reaction that takes a year is not a reaction "
                     "and cannot be written as an equation",
             "correct": False,
             "why": "Rusting takes years and is a reaction with an equation "
                    "like any other"},
        ],
        "figure": None,
    },
    {
        "id": "c4-03-h16",
        "band": "harder",
        "text": "One student writes magnesium + hydrochloric acid, another "
                "writes hydrochloric acid + magnesium. Does the order of two "
                "reactants matter?",
        "options": [
            {"text": "Yes, because the substance written first is the one "
                     "that was added to the flask first",
             "correct": False,
             "why": "An equation records no order of adding. Both names are "
                    "simply on the left"},
            {"text": "Yes, because the first name on the left has to match "
                     "the first name on the right",
             "correct": False,
             "why": "There is no such matching rule, and the products need "
                    "not line up with the reactants at all"},
            {"text": "No, because the plus sign is read as and, and both are "
                     "reactants either way",
             "correct": True},
            {"text": "No, because the order matters only when there are "
                     "three or more reactants in the line",
             "correct": False,
             "why": "The order never matters on one side, however many names "
                    "are on it"},
        ],
        "figure": None,
    },
    {
        "id": "c4-03-h17",
        "band": "harder",
        "text": "A student writes a product into an equation that nobody has "
                "found any evidence for in the flask. What is the problem "
                "with the equation?",
        "options": [
            {"text": "It claims a substance was made, and the claim has not "
                     "been tested",
             "correct": True},
            {"text": "It has too many names on the right, and an equation is "
                     "allowed two products at most",
             "correct": False,
             "why": "There is no limit on the number of products an equation "
                    "may name"},
            {"text": "It is fine, because an equation is a prediction and a "
                     "prediction need not be checked",
             "correct": False,
             "why": "An equation is a claim about what happened, and a claim "
                    "has to be supported"},
            {"text": "It is fine, so long as the extra product contains "
                     "atoms from the reactants",
             "correct": False,
             "why": "Having the right atoms available makes a product "
                    "possible, and not something that happened"},
        ],
        "figure": None,
    },
    {
        "id": "c4-03-h18",
        "band": "harder",
        "text": "Iron is heated with copper oxide. Copper and iron oxide are "
                "left in the crucible. Which word equation is right?",
        "options": [
            {"text": "iron + copper oxide makes iron copper oxide",
             "correct": False,
             "why": "There is no such substance here. The crucible holds two "
                    "products, and they have names of their own"},
            {"text": "copper + iron oxide makes iron + copper oxide",
             "correct": False,
             "why": "That is the line reversed. It says the crucible started "
                    "with the two substances it finished with"},
            {"text": "iron + copper oxide + heat makes iron oxide + copper",
             "correct": False,
             "why": "Heat is a condition rather than a substance, so it goes "
                    "above the arrow"},
            {"text": "iron + copper oxide makes iron oxide + copper",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c4-03-h19",
        "band": "harder",
        "text": "Propane burns in air to give water and carbon dioxide. "
                "Which of these students has written an honest equation?",
        "options": [
            {"text": "Ali, who writes propane makes carbon dioxide + water",
             "correct": False,
             "why": "The oxygen is missing, so the line says those atoms "
                    "came from nowhere"},
            {"text": "Beth, who writes propane + oxygen makes carbon dioxide "
                     "+ water + flame",
             "correct": False,
             "why": "The flame is the reaction being seen. Nothing is made "
                    "of flame"},
            {"text": "Cara, who writes propane + air makes carbon dioxide + "
                     "water",
             "correct": False,
             "why": "Air is a mixture, and the equation should name the "
                    "substance in it that reacted"},
            {"text": "Dev, who writes propane + oxygen makes carbon dioxide "
                     "+ water",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c4-03-h20",
        "band": "harder",
        "text": "Oxygen is a reactant in one word equation and a product in "
                "another. Can both equations be right?",
        "options": [
            {"text": "No, because a substance keeps the same place in every "
                     "equation it appears in",
             "correct": False,
             "why": "Nothing fixes a substance to one side for ever. The "
                    "side depends on the reaction"},
            {"text": "Yes, because which side a substance goes on depends on "
                     "the reaction being described",
             "correct": True},
            {"text": "No, because oxygen is used up rather than made",
             "correct": False,
             "why": "Oxygen is made by plants and by splitting water, among "
                    "other reactions"},
            {"text": "Yes, but only if the two equations are written for the "
                     "same flask on the same day",
             "correct": False,
             "why": "Two unrelated reactions can do this. Nothing ties them "
                    "to one flask"},
        ],
        "figure": None,
    },
    {
        "id": "c4-03-h21",
        "band": "harder",
        "text": "A student says the arrow means the reaction has finished. "
                "What does the arrow actually claim?",
        "options": [
            {"text": "That all of the reactants were used up before the "
                     "reaction stopped",
             "correct": False,
             "why": "One reactant is often left over, and the equation is "
                    "unchanged by that"},
            {"text": "That the reaction cannot be run in the other direction "
                     "by anybody",
             "correct": False,
             "why": "Some reactions can be reversed. The arrow records which "
                    "way this one went"},
            {"text": "That the substances on the left changed into the "
                     "substances on the right",
             "correct": True},
            {"text": "That the products are stable and will not react any "
                     "further",
             "correct": False,
             "why": "A product can react again in a second reaction, with an "
                    "equation of its own"},
        ],
        "figure": None,
    },
    {
        "id": "c4-03-h22",
        "band": "harder",
        "text": "Compare two faulty equations: one leaves out a reactant, "
                "the other leaves out the heating the reaction needed. Which "
                "fault is worse, and why?",
        "options": [
            {"text": "The missing reactant, because the equation then says "
                     "its atoms came from nowhere",
             "correct": True},
            {"text": "The missing heating, because without it a reader could "
                     "not repeat the experiment",
             "correct": False,
             "why": "A missing condition is a gap in the instructions. A "
                    "missing reactant is a false claim about the atoms"},
            {"text": "Neither, because a word equation is not meant to be "
                     "complete in the first place",
             "correct": False,
             "why": "It is meant to name every substance that took part. "
                    "That is the whole of its job"},
            {"text": "Both equally, because anything left out of an equation "
                     "makes it wrong in the same way",
             "correct": False,
             "why": "One leaves out a substance and one leaves out a "
                    "condition, and only substances belong in the line"},
        ],
        "figure": None,
    },
    {
        "id": "c4-03-h23",
        "band": "harder",
        "text": "An equation for a decomposition records nothing about the "
                "strong heating the reaction needed. Is the equation wrong?",
        "options": [
            {"text": "Yes, because an equation that leaves out the heating "
                     "describes a change that never happens",
             "correct": False,
             "why": "The change happens when it is heated. The line about "
                    "substances is true either way"},
            {"text": "Yes, because heat has to be written on the left "
                     "whenever a reaction needs it",
             "correct": False,
             "why": "Heat is not a substance, so it never goes in the line "
                    "at all"},
            {"text": "No, because conditions are not recorded on a word "
                     "equation by anybody",
             "correct": False,
             "why": "They are recorded above the arrow when they matter. "
                    "Here the writer chose not to"},
            {"text": "No, because the conditions go above the arrow and this "
                     "one says nothing untrue",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c4-03-h24",
        "band": "harder",
        "text": "Two reactions are run in water. In one, the water is a "
                "reactant; in the other it is only where the reaction "
                "happened. How would a chemist tell the two apart?",
        "options": [
            {"text": "By whether the reaction happened in a beaker or in a "
                     "sealed flask",
             "correct": False,
             "why": "The container decides nothing about which substances "
                    "reacted"},
            {"text": "By whether the water is used up and its atoms end up "
                     "in a product",
             "correct": True},
            {"text": "By whether the water was there at the start of the "
                     "reaction",
             "correct": False,
             "why": "The water is there at the start in both cases. What "
                    "differs is whether it took part"},
            {"text": "By whether the products dissolve in the water once "
                     "they have been made",
             "correct": False,
             "why": "Dissolving happens after the reaction and says nothing "
                    "about whether the water reacted"},
        ],
        "figure": None,
    },
    {
        "id": "c4-03-h25",
        "band": "harder",
        "text": "Does writing a word equation for a change prove that the "
                "change was chemical rather than physical?",
        "options": [
            {"text": "Yes, because every equation has an arrow and an arrow "
                     "means a reaction",
             "correct": False,
             "why": "The arrow is written because the writer believes a "
                    "reaction happened. It is the claim, not the evidence"},
            {"text": "Yes, because a physical change has no substances in it "
                     "to write down",
             "correct": False,
             "why": "A physical change has substances. What it does not have "
                    "is a new one"},
            {"text": "No — the evidence for a new substance is what proves "
                     "it, and the equation only records the claim",
             "correct": True},
            {"text": "No, because an equation describes a physical change "
                     "just as well as a chemical one",
             "correct": False,
             "why": "A word equation names reactants and products, which a "
                    "physical change does not have"},
        ],
        "figure": None,
    },
    {
        "id": "c4-03-h26",
        "band": "harder",
        "text": "One product of a reaction is a gas that escapes from the "
                "open flask. Does the equation record that it escaped?",
        "options": [
            {"text": "No, because an equation names only the substances and "
                     "never what became of them",
             "correct": True},
            {"text": "Yes, because a product that leaves is written above "
                     "the arrow instead of on the right",
             "correct": False,
             "why": "Above the arrow is for conditions. A product stays on "
                    "the right wherever it goes afterwards"},
            {"text": "Yes, because an equation has to say what happened to "
                     "each substance it names",
             "correct": False,
             "why": "It names substances and which side they were on, and "
                    "nothing else"},
            {"text": "No, because a gas that escapes is no longer counted as "
                     "a product of the reaction",
             "correct": False,
             "why": "It was made by the reaction, so it is a product whether "
                    "it is collected or lost"},
        ],
        "figure": None,
    },
    {
        "id": "c4-03-h27",
        "band": "harder",
        "text": "A student writes: sodium + water makes sodium hydroxide + "
                "hydrogen + heat + fizzing. How many of the four things on "
                "the right belong there?",
        "options": [
            {"text": "Four",
             "correct": False,
             "why": "Two of the four are not substances, and only substances "
                    "go in the line"},
            {"text": "Three",
             "correct": False,
             "why": "Dropping the fizzing leaves the heat, and heat is not a "
                    "substance either"},
            {"text": "Two",
             "correct": True},
            {"text": "One",
             "correct": False,
             "why": "Both are products. The hydrogen escaping and the "
                    "hydroxide dissolving are not reasons to leave one out"},
        ],
        "figure": None,
    },
    {
        "id": "c4-03-h28",
        "band": "harder",
        "text": "The same word equation is used by a school class and by a "
                "chemical works making tonnes of the product. How can one "
                "line serve both?",
        "options": [
            {"text": "Because the factory writes the same line with larger "
                     "letters to stand for larger amounts",
             "correct": False,
             "why": "Nothing about how a line is written carries an amount"},
            {"text": "Because the amounts in a word equation are taken to be "
                     "one particle of each",
             "correct": False,
             "why": "A word equation gives no number of particles at all, "
                    "not even one"},
            {"text": "Because a factory uses the same masses of everything "
                     "as a school class does",
             "correct": False,
             "why": "It plainly uses far more. The equation works because it "
                    "carries no masses"},
            {"text": "Because it names the substances and says nothing about "
                     "how much of them there is",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c4-03-h29",
        "band": "harder",
        "text": "Zinc oxide is heated with carbon. Zinc comes off as a "
                "vapour, and the gas given off turns limewater cloudy. What "
                "are the products?",
        "options": [
            {"text": "Zinc and oxygen",
             "correct": False,
             "why": "Oxygen gas would not turn limewater cloudy. The oxygen "
                    "that left is joined to the carbon"},
            {"text": "Zinc and carbon dioxide",
             "correct": True},
            {"text": "Zinc oxide and carbon dioxide",
             "correct": False,
             "why": "The zinc oxide is used up rather than recovered. What "
                    "comes off as a vapour is zinc metal"},
            {"text": "Zinc carbonate",
             "correct": False,
             "why": "No carbonate is made. The limewater test shows a gas "
                    "coming off rather than a solid forming in the "
                    "crucible"},
        ],
        "figure": None,
    },
    {
        "id": "c4-03-h30",
        "band": "harder",
        "text": "Give one thing a written description of a reaction can say "
                "that its word equation cannot.",
        "options": [
            {"text": "Which substances were made by the reaction",
             "correct": False,
             "why": "The equation names them, and a description very often "
                    "fails to"},
            {"text": "Which substances reacted with each other",
             "correct": False,
             "why": "That is the other half of what an equation is for"},
            {"text": "What the change looked like while it was happening",
             "correct": True},
            {"text": "Which way round the change went",
             "correct": False,
             "why": "The arrow says that, and it cannot avoid saying it"},
        ],
        "figure": None,
    },
    {
        "id": "c4-03-h31",
        "band": "harder",
        "text": "A reaction is run with far more acid than the metal can "
                "use, and acid is left in the beaker at the end. Does the "
                "leftover change the word equation?",
        "options": [
            {"text": "No, because the equation names what reacted rather "
                     "than how much of it there was",
             "correct": True},
            {"text": "Yes, the acid should be written on both sides, because "
                     "some of it is there at the start and at the end",
             "correct": False,
             "why": "The acid that reacted is a reactant. What is left over "
                    "is the same substance, not a product"},
            {"text": "Yes, the acid should move above the arrow, because it "
                     "was not all used up by the reaction",
             "correct": False,
             "why": "Above the arrow is for conditions. The acid reacted and "
                    "its atoms are in the products"},
            {"text": "No, because a reactant that is left over stops being a "
                     "reactant once the reaction has stopped",
             "correct": False,
             "why": "The acid that reacted is still a reactant. Leftovers do "
                    "not change what took part"},
        ],
        "figure": None,
    },
    {
        "id": "c4-03-h32",
        "band": "harder",
        "text": "Magnesium reacts with hydrochloric acid, and also with "
                "sulfuric acid. Explain why one word equation cannot cover "
                "both reactions.",
        "options": [
            {"text": "Because the two acids react at different speeds, and "
                     "an equation records the speed of the change",
             "correct": False,
             "why": "No equation records speed. The difference that matters "
                    "is in the products"},
            {"text": "Because only one of the two reactions gives off "
                     "hydrogen, so the right-hand sides differ",
             "correct": False,
             "why": "Both give hydrogen. What differs is the salt that is "
                    "left in the beaker"},
            {"text": "Because sulfuric acid is a condition rather than a "
                     "reactant, so it stays out of the line",
             "correct": False,
             "why": "Both acids are substances and both are used up, which "
                    "makes them reactants"},
            {"text": "Because the two acids give different salts, so the "
                     "products are not the same",
             "correct": True},
        ],
        "figure": None,
    },
]
