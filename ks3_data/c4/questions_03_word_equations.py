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
]
