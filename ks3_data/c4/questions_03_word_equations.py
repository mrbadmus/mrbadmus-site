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
]
