"""C2 lesson 03 — Compounds: twelve questions (MRB-269).

The lesson's argument is that the same two elements can sit in one dish twice
over, and that only the quiet tests tell the two apart: the magnet, the acid
and — strongest of all — weighing what actually combines. These twelve probe
that argument from the angles the ladder leaves alone: which evidence settles
anything and which only looks convincing, what the disabled proportion control
is actually saying, and what happens when there is more of one element than the
fixed proportion can take.

The distractors are built from the lesson's two declared misconceptions.
ATOM-06 (a compound is a very thoroughly mixed mixture) drives the wrong
options in e02, s01, s02 and h04 — every one of them treats thorough mixing, a
uniform appearance or an adjustable recipe as evidence of joining. ATOM-07 (the
iron is still in there, so it must still be magnetic — the sulfur is just
covering it up) drives e02, e04, h01 and h03, where the elements are imagined
as intact but hidden, coated or wrapped up rather than genuinely gone. A third
strand, everywhere in the lesson and not in the register, is that a compound's
proportion might be negotiable after all — that heat sets it, or that half of
each always reacts: e03, s01 and h03 each carry a distractor that does exactly
that.
"""

UNIT = "C2"
LESSON = "compounds"
LESSON_NUMBER = 3

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "c2-03-e01",
        "band": "easier",
        "text": "Four tests were run on the dish, before heating and after. "
                "Three of them settle whether the substance is a mixture or a "
                "compound. Which one settles nothing?",
        "options": [
            {"text": "Look at it", "correct": True},
            {"text": "Hold a magnet over it", "correct": False,
             "why": "The magnet does settle it. The iron can be pulled out of "
                    "the mixture because it is still iron, and nothing moves "
                    "afterwards because there is no iron left to pull."},
            {"text": "Weigh what combines", "correct": False,
             "why": "Weighing is the quiet test and the strongest one there "
                    "is. A mixture can be any proportion at all; the compound "
                    "is always 7 g of iron to 4 g of sulfur."},
            {"text": "Add dilute acid", "correct": False,
             "why": "The acid settles it too. The mixture gives a gas that "
                    "burns with a squeaky pop; the compound gives a gas that "
                    "stinks of rotten eggs."},
        ],
        "figure": None,
    },
    {
        "id": "c2-03-e02",
        "band": "easier",
        "text": "Grey iron filings and yellow sulfur powder are stirred "
                "together for ten minutes. What has the stirring changed "
                "about the two substances?",
        "options": [
            {"text": "Stirred for long enough, they join up into a compound",
             "correct": False,
             "why": "This is the commonest idea about compounds and it is the "
                    "one to drop: a compound is not a very thoroughly mixed "
                    "mixture. Joining atoms takes a chemical reaction, and no "
                    "amount of stirring is one."},
            {"text": "The sulfur has coated each piece of iron and hidden it",
             "correct": False,
             "why": "A coating would leave iron underneath, and the magnet "
                    "would still find it — which it does. Stirring puts the "
                    "two in the same place and does nothing else."},
            {"text": "Nothing — each is still the same substance, now in the "
                     "same dish", "correct": True},
            {"text": "The iron has been made weaker and less magnetic than it "
                     "was", "correct": False,
             "why": "Hold a magnet over the stirred dish and the iron jumps "
                    "straight out of it, exactly as it did before. Mixing "
                    "changes nothing about a substance's properties."},
        ],
        "figure": None,
    },
    {
        "id": "c2-03-e03",
        "band": "easier",
        "text": "Iron and sulfur join in one fixed proportion. Which pair of "
                "masses reacts completely, with nothing left over?",
        "options": [
            {"text": "Any amounts at all, as long as they are stirred well "
                     "first", "correct": False,
             "why": "Any amounts make a mixture. Once they react, only 7 g of "
                    "iron to every 4 g of sulfur joins up, and whatever is "
                    "extra sits there unreacted."},
            {"text": "Equal masses, because one atom joins to one atom",
             "correct": False,
             "why": "One iron atom does join to one sulfur atom — but an iron "
                    "atom is heavier than a sulfur atom, so equal numbers do "
                    "not mean equal masses. It is 7 g to 4 g."},
            {"text": "4 g of iron with 7 g of sulfur", "correct": False,
             "why": "Right numbers, wrong way round. Iron takes the larger "
                    "share, because its atoms are the heavier ones: 7 g of "
                    "iron to every 4 g of sulfur."},
            {"text": "7 g of iron with 4 g of sulfur", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c2-03-e04",
        "band": "easier",
        "text": "After the dish has been heated until it glows, the magnet "
                "does nothing at all. Why not?",
        "options": [
            {"text": "The sulfur has coated every piece of iron, so the "
                     "magnet cannot reach it", "correct": False,
             "why": "A magnet works straight through a coating — that is why "
                    "one holds a note to a fridge door. Nothing is covering "
                    "the iron up; there is no iron there to cover."},
            {"text": "The heat destroyed the iron atoms in the dish",
             "correct": False,
             "why": "Not one atom has been lost. Every iron atom that went "
                    "into the dish is still in it — heating joined them to "
                    "sulfur, it did not destroy them."},
            {"text": "No iron is left — its atoms are in iron sulfide, "
                     "which is not magnetic", "correct": True},
            {"text": "The iron melted and ran to the bottom, out of the "
                     "magnet's reach", "correct": False,
             "why": "Nothing has run anywhere: the solid is the same dull "
                    "grey-black all the way through. Being magnetic is a "
                    "property of iron, and what is in the dish is not iron."},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "c2-03-s01",
        "band": "standard",
        "text": "Before heating you can set the dish to mostly iron, half and "
                "half, or mostly sulfur. After heating, that control refuses "
                "to move. What is the refusal telling you?",
        "options": [
            {"text": "Heating locks the proportion in at whatever you chose "
                     "beforehand", "correct": False,
             "why": "Your choice is not carried over. Whatever you started "
                    "with, what forms is one iron atom joined to one sulfur "
                    "atom, and any excess is left over unreacted."},
            {"text": "A compound has one fixed proportion, and it is not "
                     "adjustable", "correct": True},
            {"text": "The proportion changes depending on how hot the dish "
                     "gets", "correct": False,
             "why": "Temperature decides whether the reaction happens, not "
                    "what comes out of it. Iron sulfide is one iron atom to "
                    "one sulfur atom however hot the dish is."},
            {"text": "Half of each always reacts, whatever you started with",
             "correct": False,
             "why": "There is nothing special about half. The 7 g of iron and "
                    "4 g of sulfur that can react do react; what is left over "
                    "is whichever element you had spare."},
        ],
        "figure": None,
    },
    {
        "id": "c2-03-s02",
        "band": "standard",
        "text": "A student heats the dish, sees a solid that is the same dull "
                "grey-black all the way through, and says that proves it is a "
                "compound. What is wrong with the reasoning?",
        "options": [
            {"text": "Nothing is wrong — looking the same all through is what "
                     "makes something a compound", "correct": False,
             "why": "Looking uniform is not what makes a compound; being "
                    "chemically joined in a fixed proportion is. Appearance "
                    "is the one test here that settles nothing."},
            {"text": "They should have looked at the dish before heating as "
                     "well as after", "correct": False,
             "why": "They have the before picture already — grey specks and "
                    "yellow powder. Even with both, looking is the test that "
                    "cannot decide it."},
            {"text": "Grind a mixture finely enough and it looks uniform too, "
                     "so appearance settles nothing", "correct": True},
            {"text": "The heated solid would still look like two different "
                     "things side by side", "correct": False,
             "why": "It really does look uniform — the student described it "
                    "correctly. The trouble is that a uniform look is not "
                    "evidence of joining, however convincing it is."},
        ],
        "figure": None,
    },
    {
        "id": "c2-03-s03",
        "band": "standard",
        "text": "Dilute acid is added to the stirred mixture, and then to the "
                "heated solid. Which comparison is right?",
        "options": [
            {"text": "Neither fizzes, because acid does nothing to a solid",
             "correct": False,
             "why": "Both fizz. The useful question is which gas comes off, "
                    "and it is a different gas each time — which is exactly "
                    "what tells you the substances are different."},
            {"text": "The mixture gives a popping gas; the heated solid a "
                     "rotten-egg gas", "correct": True},
            {"text": "Both give a gas that pops, because both of them contain "
                     "iron", "correct": False,
             "why": "Both contain iron atoms, but only the mixture contains "
                    "iron. In the mixture the iron reacts as iron and gives "
                    "hydrogen; in the compound there is no iron to do that."},
            {"text": "The mixture gives the rotten-egg smell, because its "
                     "sulfur is loose", "correct": False,
             "why": "It is the other way round. Loose sulfur powder smells of "
                    "very little; the rotten-egg gas is hydrogen sulfide, and "
                    "only the compound can give it."},
        ],
        "figure": None,
    },
    {
        "id": "c2-03-s04",
        "band": "standard",
        "text": "A steelmaker makes a harder steel by adding a little more "
                "carbon to the iron. What does being able to do that tell you "
                "about steel?",
        "options": [
            {"text": "It is a compound of iron and carbon, in whichever ratio "
                     "was chosen", "correct": False,
             "why": "A compound does not have a ratio anybody chooses — that "
                    "is the whole difference. A proportion you can dial up or "
                    "down is the mark of a mixture."},
            {"text": "It is a compound, because heat was used to join the "
                     "carbon to the iron", "correct": False,
             "why": "Heat is involved, but nothing has joined in a fixed "
                    "proportion. The carbon is set by the steelmaker, and "
                    "that is what makes steel a mixture."},
            {"text": "It is an element, because it is a metal you can hammer "
                     "and bend", "correct": False,
             "why": "Steel has at least two elements in it, iron and carbon, "
                    "so it cannot be an element. Behaving like a metal says "
                    "nothing about that either way."},
            {"text": "It is a mixture — anything whose recipe can be adjusted "
                     "is a mixture", "correct": True},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "c2-03-h01",
        "band": "harder",
        "text": "Sodium is a metal that catches fire in water. Chlorine is a "
                "poisonous green gas. Joined together they make the salt you "
                "put on your chips. Which explains that best?",
        "options": [
            {"text": "The two poisons cancel each other out when they are put "
                     "together", "correct": False,
             "why": "Properties are not opposites that add up to nothing. "
                    "Salt is a new substance, and its properties are its own "
                    "rather than what is left of the other two."},
            {"text": "Salt is a compound, and its properties belong to the "
                     "substance, not to the elements in it", "correct": True},
            {"text": "The sodium and chlorine are still in there, wrapped up "
                     "so that they cannot reach you", "correct": False,
             "why": "Same idea as the iron 'still being in there'. The atoms "
                    "are all present; the elements are not. Nothing is "
                    "wrapped up — the atoms are joined into something else."},
            {"text": "There is so little of each in a grain of salt that "
                     "neither can do any harm", "correct": False,
             "why": "Amount is not the point. A grain of salt is nothing but "
                    "sodium and chlorine atoms, and it is harmless because "
                    "they are joined, not because there are few of them."},
        ],
        "figure": None,
    },
    {
        "id": "c2-03-h02",
        "band": "harder",
        "text": "Electricity can split water back into hydrogen and oxygen. A "
                "magnet cannot pull the iron back out of iron sulfide. Taken "
                "together, what do those two facts show?",
        "options": [
            {"text": "A compound can be taken apart, but only by a chemical "
                     "change, never by a magnet", "correct": True},
            {"text": "Water is a mixture of hydrogen and oxygen, while iron "
                     "sulfide is a compound", "correct": False,
             "why": "Both are compounds. Water had to be split by a chemical "
                    "change — a mixture would have come apart with a filter "
                    "or a magnet and no reaction at all."},
            {"text": "Iron sulfide cannot be broken down by anything, so it "
                     "must be an element", "correct": False,
             "why": "Anything made of two elements joined cannot itself be an "
                    "element. Iron sulfide can be broken down; a magnet is "
                    "simply the wrong kind of tool for the job."},
            {"text": "Electricity is stronger than a magnet, so it works "
                     "where the magnet fails", "correct": False,
             "why": "It is not a contest of strength. A magnet can only sort "
                    "things that are already separate, and splitting a "
                    "compound means breaking the joins between atoms."},
        ],
        "figure": None,
    },
    {
        "id": "c2-03-h03",
        "band": "harder",
        "text": "In a fume cupboard, a teacher heats 14 g of iron with 4 g of "
                "sulfur until the glow spreads. Once it has cooled, a magnet "
                "is held over the product. What happens?",
        "options": [
            {"text": "Nothing moves, because all of the iron is now part of a "
                     "compound", "correct": False,
             "why": "Only 7 g of the iron had sulfur to join to. The other "
                    "7 g never reacted with anything, and it is still iron — "
                    "so the magnet will find it."},
            {"text": "Some of the solid jumps to the magnet: 7 g of iron "
                     "reacted, and 7 g is left over", "correct": True},
            {"text": "All of the solid is pulled to the magnet, because the "
                     "dish was mostly iron", "correct": False,
             "why": "The iron sulfide that formed is not magnetic, however "
                    "much iron went into the dish. Only the 7 g that never "
                    "reacted will move."},
            {"text": "Nothing moves, because the sulfur is spread through all "
                     "of the iron", "correct": False,
             "why": "Sulfur does not spread through iron — it joins to it, "
                    "atom to atom, until it runs out. It ran out after 7 g of "
                    "iron, leaving 7 g of plain iron behind."},
        ],
        "figure": None,
    },
    {
        "id": "c2-03-h04",
        "band": "harder",
        "text": "Water taken from the Red Sea is much saltier than water "
                "taken from the Baltic Sea. What does that comparison, on its "
                "own, establish?",
        "options": [
            {"text": "Sea water is a compound whose proportion depends on how "
                     "warm the sea is", "correct": False,
             "why": "A compound has one proportion and nothing shifts it — "
                    "not heat, not where it came from. A composition that "
                    "varies is the signature of a mixture."},
            {"text": "Nothing: a compound can be any proportion too, as long "
                     "as it is thoroughly mixed", "correct": False,
             "why": "This is the idea the whole lesson exists to correct. Any "
                    "proportion means a mixture; a compound is one fixed "
                    "proportion, everywhere it is found."},
            {"text": "Red Sea water is a compound and Baltic water is a "
                     "mixture of salt and water", "correct": False,
             "why": "Both are mixtures of exactly the same kind. Being "
                    "saltier does not make anything more chemically joined — "
                    "it just means more salt in the same water."},
            {"text": "Sea water is a mixture — its composition varies, and "
                     "a compound's cannot", "correct": True},
        ],
        "figure": None,
    },

    # ── easier · MRB-335 top-up ─────────────────────────────────────────
    {
        "id": "c2-03-e05",
        "band": "easier",
        "text": "What does it mean to say two atoms are bonded?",
        "options": [
            {"text": "That they are lying next to each other in the same dish "
                     "after the two powders have been thoroughly stirred",
             "correct": False,
             "why": "Being next to each other is all that stirring achieves. "
                    "Bonded means actually joined"},
            {"text": "That they are the same kind of atom as each other",
             "correct": False,
             "why": "Bonding happens between different kinds and between the "
                    "same kind. What matters is the join, not the kind"},
            {"text": "That they are held to each other by a chemical join",
             "correct": True},
            {"text": "That they are stuck together but can be pulled apart "
                     "with a magnet",
             "correct": False,
             "why": "A magnet lifts iron out of a mixture and nothing out of "
                    "iron sulfide. A bond is not undone that way"},
        ],
        "figure": None,
    },
    {
        "id": "c2-03-e06",
        "band": "easier",
        "text": "Carbon dioxide is always one carbon atom to two oxygen "
                "atoms, whether it comes from a volcano, your lungs or a "
                "factory. What does that make it?",
        "options": [
            {"text": "A mixture, because it comes from so many different "
                     "places and each of those places makes it differently",
             "correct": False,
             "why": "Where it comes from does not matter at all. The fixed "
                    "one-to-two ratio is what settles it"},
            {"text": "An element, because it always behaves in exactly the "
                     "same way",
             "correct": False,
             "why": "It holds two kinds of atom, so it cannot be an element. "
                    "Behaving consistently is a property of compounds too"},
            {"text": "A mixture, because carbon and oxygen are both in it",
             "correct": False,
             "why": "Two elements being present is not enough — in a mixture "
                    "they are not joined. Here they are"},
            {"text": "A compound",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c2-03-e07",
        "band": "easier",
        "text": "The particle diagram of the heated dish shows every iron "
                "atom joined to one sulfur atom, all the way through. What is "
                "that a picture of?",
        "options": [
            {"text": "Iron sulfide, a compound",
             "correct": True},
            {"text": "A mixture in which the two powders have been stirred "
                     "for long enough to be evenly spread out everywhere",
             "correct": False,
             "why": "In a mixture nothing is joined to anything, however "
                    "evenly it is spread. The joins are the difference"},
            {"text": "Iron with sulfur coating the outside of each grain",
             "correct": False,
             "why": "That is the covering-it-up idea. Every atom is joined "
                    "right through the solid, not just on the surface"},
            {"text": "Two elements sitting side by side without touching",
             "correct": False,
             "why": "The diagram shows them joined, one to one. Side by side "
                    "is the picture of the dish BEFORE it was heated"},
        ],
        "figure": None,
    },
    {
        "id": "c2-03-e08",
        "band": "easier",
        "text": "Which of these can be separated again without any chemical "
                "reaction?",
        "options": [
            {"text": "Iron sulfide, which was made by heating iron and sulfur "
                     "together in a dish until the mixture glowed",
             "correct": False,
             "why": "A reaction made it, and only a reaction will undo it. A "
                    "magnet gets nothing out"},
            {"text": "A stirred mixture of iron filings and sulfur powder",
             "correct": True},
            {"text": "Carbon dioxide",
             "correct": False,
             "why": "Its carbon and oxygen are joined. Splitting them is a "
                    "chemical change"},
            {"text": "Sugar",
             "correct": False,
             "why": "A compound of carbon, hydrogen and oxygen in a fixed "
                    "ratio, however carefully it is purified"},
        ],
        "figure": None,
    },
    {
        "id": "c2-03-e09",
        "band": "easier",
        "text": "Two elements are stirred together in a dish. What has to "
                "happen before they become a compound?",
        "options": [
            {"text": "They have to be stirred for long enough that no part of "
                     "the dish is any different from any other part of it",
             "correct": False,
             "why": "However evenly a mixture is spread, nothing in it is "
                    "joined. Stirring never makes a compound"},
            {"text": "One of them has to dissolve in the other",
             "correct": False,
             "why": "Dissolving spreads one substance through another and "
                    "joins nothing. Evaporate it and both come back"},
            {"text": "Their atoms have to be joined, in a chemical reaction",
             "correct": True},
            {"text": "They have to be heated until they melt",
             "correct": False,
             "why": "Melting is a change of state. Two melted elements poured "
                    "together are still a mixture"},
        ],
        "figure": None,
    },

    # ── standard · MRB-335 top-up ───────────────────────────────────────
    {
        "id": "c2-03-s05",
        "band": "standard",
        "text": "The four tests on the dish are: look at it, use a magnet, "
                "add dilute acid, and vary the proportions. Which two both "
                "settle the question?",
        "options": [
            {"text": "Looking at it and the magnet, since the mixture is "
                     "obviously two colours and the compound is obviously "
                     "one",
             "correct": False,
             "why": "Grind a mixture finely and it looks uniform too. Looking "
                    "settles nothing here"},
            {"text": "Looking at it and adding acid",
             "correct": False,
             "why": "Acid does settle it — the two gases are different — but "
                    "looking still settles nothing"},
            {"text": "The magnet and varying the proportions",
             "correct": True},
            {"text": "The magnet and looking at it",
             "correct": False,
             "why": "The magnet settles it. Looking does not, however "
                    "carefully it is done"},
        ],
        "figure": None,
    },
    {
        "id": "c2-03-s06",
        "band": "standard",
        "text": "A student says iron sulfide is really just a mixture that "
                "has been mixed extremely thoroughly. Which single result "
                "deals with that?",
        "options": [
            {"text": "It is a uniform grey-black colour all the way through "
                     "the dish",
             "correct": False,
             "why": "A finely ground mixture looks uniform too. Colour is the "
                    "one thing that settles nothing"},
            {"text": "It had to be heated until it glowed before it would "
                     "form",
             "correct": False,
             "why": "Heat is how the reaction was started. Something can be "
                    "heated and still end up a mixture"},
            {"text": "It is a solid rather than a powder",
             "correct": False,
             "why": "Both states of the dish are solid. The texture is not "
                    "evidence about joining"},
            {"text": "Only one exact proportion of iron to sulfur will react, "
                     "and anything extra is left over",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c2-03-s07",
        "band": "standard",
        "text": "Dilute acid on the stirred mixture gives a gas that pops "
                "with a lit splint. Dilute acid on the heated solid gives a "
                "gas that smells of rotten eggs. Why the difference?",
        "options": [
            {"text": "In the mixture the acid reaches iron, which is still "
                     "iron; in the compound it reaches iron sulfide, which is "
                     "not",
             "correct": True},
            {"text": "The heated solid has been damaged by the heat, so it "
                     "gives off a different gas from the one it used to give",
             "correct": False,
             "why": "It has not been damaged — it is a new substance. The "
                    "gas is different because the starting material is"},
            {"text": "The acid becomes weaker after the first test, so the "
                     "second result cannot be compared with it",
             "correct": False,
             "why": "Fresh acid is used each time. Weak acid would give less "
                    "gas, not a different gas"},
            {"text": "Both gases are the same and only the smell differs",
             "correct": False,
             "why": "One pops and one stinks — they are hydrogen and hydrogen "
                    "sulfide, two different substances"},
        ],
        "figure": None,
    },
    {
        "id": "c2-03-s08",
        "band": "standard",
        "text": "Iron and sulfur join in the ratio 7 g to 4 g. A student "
                "heats 14 g of iron with 8 g of sulfur until the glow "
                "spreads. What do they get?",
        "options": [
            {"text": "11 g of iron sulfide, with 11 g left over unreacted",
             "correct": False,
             "why": "Both amounts have been doubled together, so both react. "
                    "Doubling a recipe does not leave half of it behind"},
            {"text": "22 g of iron sulfide, with nothing at all left over "
                     "once the dish has cooled down again completely",
             "correct": True},
            {"text": "A mixture, because the amounts were not 7 g and 4 g "
                     "exactly",
             "correct": False,
             "why": "The RATIO is what has to be right, and 14 to 8 is the "
                    "same ratio as 7 to 4"},
            {"text": "A compound with twice as much of each element inside "
                     "every particle",
             "correct": False,
             "why": "A compound's proportion is fixed. Doubling the "
                    "ingredients makes twice as much of the same compound"},
        ],
        "figure": None,
    },
    {
        "id": "c2-03-s09",
        "band": "standard",
        "text": "Air can be 21% oxygen at sea level and slightly less high on "
                "a mountain, and it is still air. What does that establish?",
        "options": [
            {"text": "That air is a compound whose formula changes with "
                     "height above sea level, which is why breathing is "
                     "harder up there",
             "correct": False,
             "why": "A compound has one formula and it never changes. Varying "
                    "proportions rule a compound out"},
            {"text": "That air is an element that has been diluted",
             "correct": False,
             "why": "Air holds nitrogen, oxygen, argon and more. An element "
                    "is one kind of atom"},
            {"text": "That air is a mixture",
             "correct": True},
            {"text": "That oxygen is not really part of the air, but "
                     "dissolved in it",
             "correct": False,
             "why": "Oxygen is one of air's components. Dissolved or not, the "
                    "varying proportion is what matters"},
        ],
        "figure": None,
    },

    # ── harder · MRB-335 top-up ─────────────────────────────────────────
    {
        "id": "c2-03-h05",
        "band": "harder",
        "text": "A 2:1 mixture of hydrogen and oxygen explodes at a spark. "
                "Water has the same two elements in the same 2:1 ratio and "
                "puts fires out. What is the only difference?",
        "options": [
            {"text": "The water has been cooled down, and cold substances "
                     "cannot burn however much energy is put into them",
             "correct": False,
             "why": "Boiling water still puts fires out, and cold hydrogen "
                    "still explodes. Temperature is not what separates "
                    "them"},
            {"text": "The water holds far more oxygen than the mixture does",
             "correct": False,
             "why": "The ratio is the same in both — two hydrogens to one "
                    "oxygen. That is what makes the pair so striking"},
            {"text": "Whether the atoms are chemically bonded to each other",
             "correct": True},
            {"text": "The mixture holds hydrogen atoms and the water holds "
                     "hydrogen particles",
             "correct": False,
             "why": "The atoms are the same atoms throughout. Only what they "
                    "are joined to has changed"},
        ],
        "figure": None,
    },
    {
        "id": "c2-03-h06",
        "band": "harder",
        "text": "A grey-black powder might be a mixture of iron and sulfur "
                "or the compound iron sulfide. You may run ONE test. Which is "
                "the strongest?",
        "options": [
            {"text": "Grind a little of it and look at it under a microscope "
                     "to see whether two different colours can be made out",
             "correct": False,
             "why": "A finely ground mixture looks uniform. Appearance is the "
                    "test that settles nothing"},
            {"text": "Weigh it, since a compound is always heavier than the "
                     "mixture it came from",
             "correct": False,
             "why": "Nothing is gained or lost in the dish. The mass is the "
                    "same either way"},
            {"text": "Heat it and see whether it glows",
             "correct": False,
             "why": "A mixture glows as it reacts; a compound has already "
                    "reacted. It works, but it destroys the sample and the "
                    "magnet does not"},
            {"text": "Hold a magnet over it and see whether anything jumps up "
                     "to it",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c2-03-h07",
        "band": "harder",
        "text": "Sugar is carbon, hydrogen and oxygen. Carbon is a black "
                "solid and the other two are gases, yet sugar is a sweet white "
                "solid. What does that show?",
        "options": [
            {"text": "That a compound's properties belong to the compound, "
                     "not to the elements in it",
             "correct": True},
            {"text": "That the carbon in sugar must be in an unusual white "
                     "form",
             "correct": False,
             "why": "There is no carbon left as carbon in it. Its atoms are "
                    "bonded into a substance of its own"},
            {"text": "That sugar must be a mixture, since three substances "
                     "are in it",
             "correct": False,
             "why": "Three ELEMENTS are in it, in a fixed ratio, chemically "
                    "joined. That is a compound"},
            {"text": "That the gases have been squashed into the solid",
             "correct": False,
             "why": "Nothing has been squashed. The atoms have been joined "
                    "into a new substance"},
        ],
        "figure": None,
    },
    {
        "id": "c2-03-h08",
        "band": "harder",
        "text": "A student says a compound is heavier than the elements that "
                "made it, because the atoms have been packed together. What is "
                "wrong?",
        "options": [
            {"text": "It is heavier, but only because heating the dish adds "
                     "energy and energy has a mass of its own that shows on a "
                     "balance",
             "correct": False,
             "why": "Nothing about heat adds weight you could measure. The "
                    "answer is simpler — the same atoms are present"},
            {"text": "Nothing is added and nothing is lost, so the mass is "
                     "the same before and after",
             "correct": True},
            {"text": "It is lighter, because joining atoms squeezes the space "
                     "out from between them",
             "correct": False,
             "why": "Empty space has no mass, so removing it cannot make "
                    "anything lighter"},
            {"text": "It is heavier, because the sulfur takes in oxygen as it "
                     "reacts",
             "correct": False,
             "why": "The dish holds iron and sulfur only. Nothing joins from "
                    "outside"},
        ],
        "figure": None,
    },
    {
        "id": "c2-03-h09",
        "band": "harder",
        "text": "Bronze is copper with tin added, and its hardness depends on "
                "how much tin the smith puts in. Which single fact settles "
                "whether bronze is a compound?",
        "options": [
            {"text": "That it is harder than either copper or tin on their "
                     "own, which is exactly the sort of new property a "
                     "compound has",
             "correct": False,
             "why": "New properties are suggestive but not decisive — a "
                    "mixture's properties change with its recipe too, which "
                    "is what happens here"},
            {"text": "That it has no entry on the periodic table",
             "correct": False,
             "why": "Compounds have no entry either, so that cannot separate "
                    "the two"},
            {"text": "That the amount of tin can be chosen",
             "correct": True},
            {"text": "That it has to be heated before it can be made",
             "correct": False,
             "why": "Heating is how it is made, and mixtures can need heat "
                    "too. The recipe is what decides it"},
        ],
        "figure": None,
    },
    {
        "id": "c2-03-e10",
        "band": "easier",
        "text": "A compound and a mixture can both contain more than one "
                "element. What is the difference between them?",
        "options": [
            {"text": "In a compound the substances are stirred for longer",
             "correct": False,
             "why": "Stirring moves powders around and joins nothing. Stir "
                    "for an hour and you still have a mixture"},
            {"text": "In a compound the substances are ground more finely",
             "correct": False,
             "why": "Grinding makes the pieces smaller, not joined. A fine "
                    "powder is still a mixture"},
            {"text": "In a compound the atoms are chemically bonded together",
             "correct": True},
            {"text": "In a compound the substances are present in much "
                     "larger amounts",
             "correct": False,
             "why": "Amount decides nothing. A pinch of salt is a compound "
                    "and a bucket of sand and salt is a mixture"},
        ],
        "figure": None,
    },
    {
        "id": "c2-03-e11",
        "band": "easier",
        "text": "Three samples of pure water are analysed and every one of "
                "them is H₂O. A fourth sample is sold as H₃O. What is wrong "
                "with that label?",
        "options": [
            {"text": "Nothing — H₃O is water with spare hydrogen dissolved in "
                     "it",
             "correct": False,
             "why": "Dissolving something in water does not change the "
                    "water's own formula. H₂O is still H₂O"},
            {"text": "A compound has one fixed ratio, so H₃O is not water",
             "correct": True},
            {"text": "Nothing — H₃O is what water becomes when it is warmed",
             "correct": False,
             "why": "Warming water changes its temperature and its state, "
                    "never the number of atoms in it"},
            {"text": "The letters are correct but written in the wrong order",
             "correct": False,
             "why": "The order is not the problem. The problem is the count: "
                    "three hydrogen atoms to one oxygen is not water"},
        ],
        "figure": None,
    },
    {
        "id": "c2-03-e12",
        "band": "easier",
        "text": "Copper is a red-brown metal that conducts electricity. "
                "Copper oxide is a black powder that conducts nothing. What "
                "does that difference show?",
        "options": [
            {"text": "A compound has properties of its own", "correct": True},
            {"text": "The copper has been coated in a black layer",
             "correct": False,
             "why": "Nothing is sitting on top of the copper. The copper "
                    "atoms are bonded to oxygen atoms right through"},
            {"text": "The copper has been destroyed by the oxygen",
             "correct": False,
             "why": "Every copper atom is still there. The substance they "
                    "belong to is what has changed"},
            {"text": "A compound's properties are an average of its "
                     "elements'",
             "correct": False,
             "why": "Nothing is averaged. Copper conducts and oxygen is a "
                    "gas, and copper oxide is neither of those things"},
        ],
        "figure": None,
    },
    {
        "id": "c2-03-e13",
        "band": "easier",
        "text": "A student wants to get the copper out of copper oxide, which "
                "is a compound. What kind of change is needed?",
        "options": [
            {"text": "A physical change, such as passing the powder "
                     "through filter paper",
             "correct": False,
             "why": "A filter parts things that were never joined. The "
                    "copper and oxygen here are bonded"},
            {"text": "A chemical change, such as heating it with carbon",
             "correct": True},
            {"text": "A physical change, such as dissolving and evaporating",
             "correct": False,
             "why": "Evaporating brings back whatever was dissolved, "
                    "unchanged. It cannot part bonded atoms"},
            {"text": "A chemical change, such as dissolving it in warm "
                     "water",
             "correct": False,
             "why": "Dissolving is a physical change, and copper oxide "
                    "barely dissolves at all. Nothing is reacted by it"},
        ],
        "figure": None,
    },
    {
        "id": "c2-03-e14",
        "band": "easier",
        "text": "Magnesium is burned in oxygen and a white solid is made. "
                "What is that compound called?",
        "options": [
            {"text": "Magnesium oxygen", "correct": False,
             "why": "The second element's name is changed, not kept whole. A "
                    "compound of two elements takes the -ide ending"},
            {"text": "Magnesium dioxide", "correct": False,
             "why": "Prefixes belong to compounds of two non-metals. A metal "
                    "compound takes the -ide ending on its own"},
            {"text": "Magnesium oxate", "correct": False,
             "why": "There is no -ate ending here. -ate would mean a third "
                    "element, oxygen, on top of two others"},
            {"text": "Magnesium oxide", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c2-03-e15",
        "band": "easier",
        "text": "The name copper sulfate ends in -ate rather than -ide. What "
                "does that ending tell you the compound contains?",
        "options": [
            {"text": "Copper and sulfur only", "correct": False,
             "why": "Copper and sulfur only would be copper sulfide. The "
                    "-ate ending marks something extra"},
            {"text": "Copper, sulfur and oxygen", "correct": True},
            {"text": "Copper and oxygen only", "correct": False,
             "why": "That would be copper oxide. The word sulfate keeps the "
                    "sulfur in the compound"},
            {"text": "Copper, sulfur and hydrogen", "correct": False,
             "why": "The -ate ending marks oxygen, not hydrogen. Hydrogen is "
                    "not named by it at all"},
        ],
        "figure": None,
    },
    {
        "id": "c2-03-e16",
        "band": "easier",
        "text": "A compound of two non-metals is named using prefixes. In the "
                "name carbon dioxide, what is the prefix di- counting?",
        "options": [
            {"text": "The oxygen atoms joined to each carbon atom",
             "correct": True},
            {"text": "The carbon atoms joined on to each oxygen atom",
             "correct": False,
             "why": "The prefix sits in front of oxide, so it counts oxygen. "
                    "There is one carbon atom, not two"},
            {"text": "The different elements the compound contains",
             "correct": False,
             "why": "The prefix counts atoms, not elements. Both carbon "
                    "monoxide and carbon dioxide hold two elements"},
            {"text": "The separate particles present in the gas",
             "correct": False,
             "why": "A number in front of the whole name would count "
                    "particles. A prefix inside the name counts atoms"},
        ],
        "figure": None,
    },
    {
        "id": "c2-03-e17",
        "band": "easier",
        "text": "A bottle in a laboratory is labelled KNO₃. Which three "
                "elements does the compound contain?",
        "options": [
            {"text": "Krypton, nitrogen and oxygen", "correct": False,
             "why": "Krypton is Kr. A single capital K on its own is "
                    "potassium"},
            {"text": "Potassium, nickel and oxygen", "correct": False,
             "why": "Nickel is Ni and needs its own small letter. N on its "
                    "own is nitrogen"},
            {"text": "Potassium, nitrogen and oxygen", "correct": True},
            {"text": "Potassium, nitrogen and osmium", "correct": False,
             "why": "Osmium is Os. The single capital O in a formula is "
                    "oxygen"},
        ],
        "figure": None,
    },
    {
        "id": "c2-03-e18",
        "band": "easier",
        "text": "Aluminium oxide has the formula Al₂O₃. How many oxygen "
                "atoms are there in one particle of it?",
        "options": [
            {"text": "Two", "correct": False,
             "why": "Two is the small number after the Al, which counts "
                    "aluminium atoms, not oxygen atoms"},
            {"text": "Three", "correct": True},
            {"text": "Five", "correct": False,
             "why": "Five is every atom in the particle added together, not "
                    "the oxygen atoms on their own"},
            {"text": "Six", "correct": False,
             "why": "Six comes from multiplying the two small numbers. They "
                    "are separate counts and are not multiplied"},
        ],
        "figure": None,
    },
    {
        "id": "c2-03-e19",
        "band": "easier",
        "text": "Calcium hydroxide is written Ca(OH)₂, with the small 2 "
                "standing outside the brackets. What does that 2 apply to?",
        "options": [
            {"text": "The hydrogen atoms on their own", "correct": False,
             "why": "A number outside brackets never picks out one symbol. "
                    "It would have to sit against the H to do that"},
            {"text": "Everything inside the brackets", "correct": True},
            {"text": "The calcium atom on its own", "correct": False,
             "why": "The calcium sits outside the brackets altogether, so "
                    "the 2 does not reach it"},
            {"text": "The oxygen atoms on their own", "correct": False,
             "why": "The oxygen is doubled, but so is the hydrogen beside "
                    "it. The brackets tie the two together"},
        ],
        "figure": None,
    },
    {
        "id": "c2-03-e20",
        "band": "easier",
        "text": "Which pair of elements is the compound water made from?",
        "options": [
            {"text": "Hydrogen and carbon", "correct": False,
             "why": "Hydrogen and carbon together make substances such as "
                    "methane, which burns. Water does not"},
            {"text": "Helium and oxygen", "correct": False,
             "why": "Helium joins with nothing at all. The H in water stands "
                    "for hydrogen"},
            {"text": "Hydrogen and nitrogen", "correct": False,
             "why": "Hydrogen and nitrogen make ammonia, a sharp-smelling "
                    "gas. Water contains oxygen instead"},
            {"text": "Hydrogen and oxygen", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c2-03-e21",
        "band": "easier",
        "text": "Carbon dioxide is breathed out by every animal. Which "
                "elements is that compound made from?",
        "options": [
            {"text": "Carbon and oxygen", "correct": True},
            {"text": "Carbon and hydrogen", "correct": False,
             "why": "The word dioxide names oxygen. Carbon and hydrogen "
                    "would make a fuel such as methane"},
            {"text": "Carbon on its own", "correct": False,
             "why": "Carbon on its own is an element, not a compound. Carbon "
                    "dioxide holds two elements"},
            {"text": "Carbon, oxygen and hydrogen", "correct": False,
             "why": "There is no hydrogen in the name and none in the gas. "
                    "Carbon and oxygen are the whole list"},
        ],
        "figure": None,
    },
    {
        "id": "c2-03-e22",
        "band": "easier",
        "text": "Methane is the main compound in the natural gas supply and "
                "its formula is CH₄. How many atoms are there altogether in "
                "one particle of methane?",
        "options": [
            {"text": "Four", "correct": False,
             "why": "Four counts the hydrogen atoms only and leaves the "
                    "carbon atom out"},
            {"text": "Five", "correct": True},
            {"text": "Two", "correct": False,
             "why": "Two is the number of different elements, not the number "
                    "of atoms"},
            {"text": "Eight", "correct": False,
             "why": "Eight doubles the hydrogen. The 4 counts the hydrogen "
                    "atoms once"},
        ],
        "figure": None,
    },
    {
        "id": "c2-03-e23",
        "band": "easier",
        "text": "Ammonia is used in cleaning products and contains nitrogen "
                "and hydrogen only. Which formula fits that description?",
        "options": [
            {"text": "NO₃", "correct": False,
             "why": "That names nitrogen and oxygen. There is no hydrogen "
                    "anywhere in it"},
            {"text": "N₂O", "correct": False,
             "why": "That names nitrogen and oxygen as well, in a different "
                    "proportion. Hydrogen is still missing"},
            {"text": "NH₃", "correct": True},
            {"text": "NaH", "correct": False,
             "why": "Na is sodium, not nitrogen. The capital-then-small "
                    "pattern makes it a different element"},
        ],
        "figure": None,
    },
    {
        "id": "c2-03-e24",
        "band": "easier",
        "text": "Chalk, limestone and marble are all the compound calcium "
                "carbonate. Which elements is that compound made from?",
        "options": [
            {"text": "Calcium, carbon and oxygen", "correct": True},
            {"text": "Calcium and carbon only", "correct": False,
             "why": "That would be calcium carbide. The -ate ending puts "
                    "oxygen in as well"},
            {"text": "Calcium, carbon and hydrogen", "correct": False,
             "why": "There is no hydrogen in calcium carbonate. The -ate "
                    "ending marks oxygen"},
            {"text": "Carbon and oxygen only", "correct": False,
             "why": "That pair on its own is carbon dioxide. The calcium is "
                    "named first and is part of the compound"},
        ],
        "figure": None,
    },
    {
        "id": "c2-03-e25",
        "band": "easier",
        "text": "Table salt is the compound sodium chloride. What is a grain "
                "of it made of?",
        "options": [
            {"text": "Sodium grains stirred through chlorine gas",
             "correct": False,
             "why": "Stirring would make a mixture, and the sodium would "
                    "still behave as sodium. Nothing in salt does"},
            {"text": "Sodium atoms bonded to carbon atoms", "correct": False,
             "why": "Chloride names chlorine, not carbon. There is no carbon "
                    "in table salt"},
            {"text": "Chlorine atoms bonded to other chlorine atoms",
             "correct": False,
             "why": "Chlorine bonded only to chlorine is the element "
                    "chlorine, a green gas, not salt"},
            {"text": "Sodium atoms bonded to chlorine atoms", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c2-03-e26",
        "band": "easier",
        "text": "Rust forms where iron is left in damp air, and rust is iron "
                "oxide. What kind of substance is iron oxide?",
        "options": [
            {"text": "A mixture of iron and oxygen", "correct": False,
             "why": "A mixture would let the iron behave as iron. In rust "
                    "the iron atoms are bonded to oxygen atoms"},
            {"text": "A compound of iron and oxygen", "correct": True},
            {"text": "An element with its own periodic table entry",
             "correct": False,
             "why": "Only iron and oxygen have entries. A compound of the "
                    "two never gets one of its own"},
            {"text": "A mixture of iron, oxygen and water", "correct": False,
             "why": "Water is needed for rusting to happen but is not part "
                    "of the compound that forms"},
        ],
        "figure": None,
    },
    {
        "id": "c2-03-e27",
        "band": "easier",
        "text": "How many different elements must a compound contain?",
        "options": [
            {"text": "At least two", "correct": True},
            {"text": "Exactly two", "correct": False,
             "why": "Two is the smallest number, not the only one. Calcium "
                    "carbonate holds three"},
            {"text": "Exactly one", "correct": False,
             "why": "One kind of atom on its own is an element. A compound "
                    "needs atoms of different elements joined"},
            {"text": "At least three", "correct": False,
             "why": "Water holds two elements and is a compound. Three is "
                    "more than the definition asks for"},
        ],
        "figure": None,
    },
    {
        "id": "c2-03-e28",
        "band": "easier",
        "text": "Sand and salt are stirred together in a beaker until the "
                "heap looks even. Is the result a compound?",
        "options": [
            {"text": "No, because the two are not chemically joined",
             "correct": True},
            {"text": "No, because a compound has to contain a metal "
                     "element",
             "correct": False,
             "why": "Plenty of compounds contain no metal at all. Water, "
                    "ammonia and carbon dioxide are three of them"},
            {"text": "Yes, because stirring joins the grains to each other",
             "correct": False,
             "why": "Stirring rearranges grains. Only a chemical reaction "
                    "joins atoms"},
            {"text": "Yes, because sand and salt mix in a fixed proportion",
             "correct": False,
             "why": "You can put in any amounts of either. A proportion you "
                    "choose is the mark of a mixture"},
        ],
        "figure": None,
    },
    {
        "id": "c2-03-e29",
        "band": "easier",
        "text": "Every sample of pure copper oxide turns out to be 80% copper "
                "by mass, wherever it came from. What does that show?",
        "options": [
            {"text": "Copper oxide is a mixture that has always been "
                     "stirred well",
             "correct": False,
             "why": "A mixture's proportion depends on who made it. It does "
                    "not come out the same every time"},
            {"text": "Copper oxide is a compound of fixed composition",
             "correct": True},
            {"text": "Copper oxide is an element that contains copper",
             "correct": False,
             "why": "An element holds one kind of atom. Copper oxide holds "
                    "copper atoms and oxygen atoms"},
            {"text": "Copper oxide samples differ, but only very slightly",
             "correct": False,
             "why": "They do not differ at all. Every sample gives the same "
                    "figure because the ratio is fixed"},
        ],
        "figure": None,
    },
    {
        "id": "c2-03-e30",
        "band": "easier",
        "text": "Iron and sulfur sit unchanged in a dish until one corner is "
                "heated until it glows. What is the heating supplying?",
        "options": [
            {"text": "The stirring needed to spread the two powders",
             "correct": False,
             "why": "The powders are already spread. Spreading them further "
                    "would not join a single atom"},
            {"text": "The extra sulfur needed to finish the reaction",
             "correct": False,
             "why": "Heat supplies energy, never matter. No sulfur is added "
                    "by a burner"},
            {"text": "The energy needed to start the reaction",
             "correct": True},
            {"text": "The oxygen needed to join the two elements",
             "correct": False,
             "why": "No oxygen goes into iron sulfide. Iron and sulfur join "
                    "to each other"},
        ],
        "figure": None,
    },
    {
        "id": "c2-03-e31",
        "band": "easier",
        "text": "A student stirs sugar into water until none of it can be "
                "seen, and says a new compound has been made. What has "
                "actually happened?",
        "options": [
            {"text": "The sugar and the water are mixed, not joined",
             "correct": True},
            {"text": "The sugar has bonded chemically on to the water",
             "correct": False,
             "why": "Nothing has bonded. Boil the water off and the same "
                    "sugar comes back, unchanged"},
            {"text": "The sugar has broken down into its elements",
             "correct": False,
             "why": "Its elements are carbon, hydrogen and oxygen, and none "
                    "of them appears. The sugar is still sugar"},
            {"text": "The sugar has reacted with the water to make a "
                     "syrup",
             "correct": False,
             "why": "A syrup is only concentrated sugar solution. No new "
                    "substance has been made"},
        ],
        "figure": None,
    },
    {
        "id": "c2-03-e32",
        "band": "easier",
        "text": "A pure compound melts at one sharp temperature. What does a "
                "mixture of two solids do as it is heated?",
        "options": [
            {"text": "It melts at one sharp temperature as well",
             "correct": False,
             "why": "A sharp melting point is the mark of a pure substance. "
                    "A mixture does not give one"},
            {"text": "It stays solid until it reacts, rather than ever "
                     "melting",
             "correct": False,
             "why": "Mixtures melt perfectly well. They simply do not do it "
                    "all at one temperature"},
            {"text": "It melts over a range of temperatures",
             "correct": True},
            {"text": "It melts at the temperature of its heavier part",
             "correct": False,
             "why": "Mass decides nothing here. Each substance in the "
                    "mixture softens the other's melting point"},
        ],
        "figure": None,
    },
    {
        "id": "c2-03-s10",
        "band": "standard",
        "text": "A grey powder holds two elements. No filter, sieve or magnet "
                "parts them, and every sample is 70% of one element by mass. "
                "Classify the powder and give the reason.",
        "options": [
            {"text": "A mixture, because two elements are "
                     "sitting side by side in it",
             "correct": False,
             "why": "Two elements in one place is true of every mixture and "
                    "every compound. It settles nothing on its own"},
            {"text": "A compound, because the composition is fixed and "
                     "nothing physical parts it",
             "correct": True},
            {"text": "A mixture, because an even grey powder is "
                     "what a good blend gives",
             "correct": False,
             "why": "Grind any mixture finely enough and it looks even. "
                    "Appearance is the one test that settles nothing"},
            {"text": "A compound, because it is grey rather than two colours",
             "correct": False,
             "why": "Colour is not evidence. The fixed composition is what "
                    "makes this one a compound"},
        ],
        "figure": None,
    },
    {
        "id": "c2-03-s11",
        "band": "standard",
        "text": "18 g of water always splits into 2 g of hydrogen and 16 g of "
                "oxygen. Calculate the masses obtained from 36 g of water.",
        "options": [
            {"text": "2 g of hydrogen and 34 g of oxygen", "correct": False,
             "why": "The hydrogen has been left at its old value and the "
                    "whole extra 18 g given to oxygen. Both must double"},
            {"text": "4 g of hydrogen and 16 g of oxygen", "correct": False,
             "why": "The hydrogen has been doubled and the oxygen has not. "
                    "The two masses have to stay in step"},
            {"text": "18 g of hydrogen and 18 g of oxygen", "correct": False,
             "why": "Water is not half hydrogen by mass. Splitting the total "
                    "evenly ignores the fixed 2 g to 16 g ratio"},
            {"text": "4 g of hydrogen and 32 g of oxygen", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c2-03-s12",
        "band": "standard",
        "text": "Chlorine is a poisonous green gas, yet sodium chloride is "
                "sprinkled on food. Explain how that is possible.",
        "options": [
            {"text": "The chlorine atoms are bonded into a new substance "
                     "with its own properties",
             "correct": True},
            {"text": "The chlorine is present in too small an "
                     "amount of the salt to do harm",
             "correct": False,
             "why": "Chlorine is well over half of salt by mass. Amount is "
                    "not what makes salt safe"},
            {"text": "The sodium cancels out the poisonous effect of the "
                     "chlorine",
             "correct": False,
             "why": "Nothing is cancelled. Sodium is violently reactive on "
                    "its own, so two hazards would not make a safe one"},
            {"text": "The chlorine escapes as a gas while the salt is being "
                     "made",
             "correct": False,
             "why": "If the chlorine had left there would be no chloride. "
                    "The chlorine atoms are all still in the salt"},
        ],
        "figure": None,
    },
    {
        "id": "c2-03-s13",
        "band": "standard",
        "text": "Filtering can separate many mixtures but it never separates "
                "a compound into its elements. Explain why not.",
        "options": [
            {"text": "The elements dissolve into one another, so they "
                     "pass straight through the paper",
             "correct": False,
             "why": "Dissolving is not what is happening. The atoms are "
                    "bonded, and a bond is not undone by a filter"},
            {"text": "The pieces of each element are too small for the paper "
                     "to catch",
             "correct": False,
             "why": "Size is not the obstacle. There are no separate pieces "
                    "of each element in a compound to catch"},
            {"text": "The elements are chemically bonded, and no filter "
                     "breaks a bond",
             "correct": True},
            {"text": "The elements in a compound are always the same size as "
                     "each other",
             "correct": False,
             "why": "Atoms of different elements are different sizes. Even "
                    "so, a filter could not part them"},
        ],
        "figure": None,
    },
    {
        "id": "c2-03-s14",
        "band": "standard",
        "text": "Zinc is heated with sulfur and the two react completely. "
                "Name the compound made, and give the reason for its ending.",
        "options": [
            {"text": "Zinc sulfate, because the compound contains sulfur",
             "correct": False,
             "why": "Sulfate would mean oxygen is in there too. Only zinc "
                    "and sulfur went into the tube"},
            {"text": "Zinc sulfur, because both element names are kept whole",
             "correct": False,
             "why": "The second name is always changed. Keeping it whole "
                    "names a mixture rather than a compound"},
            {"text": "Zinc sulfide, because sulfur is the "
                     "heavier of the two elements",
             "correct": False,
             "why": "The name is right and the reason is not. Mass has "
                    "nothing to do with which ending a compound takes"},
            {"text": "Zinc sulfide, because a compound of two elements takes "
                     "-ide",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c2-03-s15",
        "band": "standard",
        "text": "Two white powders are labelled calcium sulfide and calcium "
                "sulfate. Which one contains oxygen, and how do you know?",
        "options": [
            {"text": "Calcium sulfate, because the -ate ending shows oxygen "
                     "is present",
             "correct": True},
            {"text": "Calcium sulfide, because the -ide ending shows oxygen "
                     "is present",
             "correct": False,
             "why": "The -ide ending means the compound holds just the two "
                    "elements named. Oxygen is not one of them"},
            {"text": "Both of them, because every compound holds some oxygen "
                     "in it",
             "correct": False,
             "why": "Plenty of compounds hold none. Methane and ammonia are "
                    "two of them"},
            {"text": "Neither of them, because oxygen is a gas and both of "
                     "these are solids",
             "correct": False,
             "why": "A bonded oxygen atom is not a gas. Water is a liquid "
                    "and is nearly all oxygen by mass"},
        ],
        "figure": None,
    },
    {
        "id": "c2-03-s16",
        "band": "standard",
        "text": "Sulfur dioxide and sulfur trioxide are both made of sulfur "
                "and oxygen only. Explain what makes them different "
                "compounds.",
        "options": [
            {"text": "Each sulfur atom is joined to a different number of "
                     "oxygen atoms",
             "correct": True},
            {"text": "Each sulfur atom is joined to a different kind of "
                     "oxygen atom",
             "correct": False,
             "why": "Every oxygen atom is the same as every other. What "
                    "differs is how many of them are joined on"},
            {"text": "One of the two is a compound and the other one is a "
                     "mixture",
             "correct": False,
             "why": "Both are compounds. Each has a fixed formula and its "
                    "own properties"},
            {"text": "One of the two contains sulfur and the other one "
                     "contains oxygen",
             "correct": False,
             "why": "Both names carry both elements. Neither is made of one "
                    "element on its own"},
        ],
        "figure": None,
    },
    {
        "id": "c2-03-s17",
        "band": "standard",
        "text": "Two bottles are labelled CuSO₄ and CaSO₄. A student says "
                "they must hold the same elements because both end in SO₄. "
                "Where is the error?",
        "options": [
            {"text": "SO₄ stands for a different pair of elements in each "
                     "compound",
             "correct": False,
             "why": "S is sulfur and O is oxygen in both. The shared part is "
                    "genuinely the same"},
            {"text": "The opening symbols differ, so one holds copper and "
                     "the other calcium",
             "correct": True},
            {"text": "They hold the same elements, just in different "
                     "amounts",
             "correct": False,
             "why": "Cu and Ca are two different elements, so the lists "
                    "differ. It is not a question of amount"},
            {"text": "The symbols differ, so one holds copper and the "
                     "other carbon",
             "correct": False,
             "why": "Carbon is C on its own. Ca with a small a after it is "
                    "calcium"},
        ],
        "figure": None,
    },
    {
        "id": "c2-03-s18",
        "band": "standard",
        "text": "Ammonium chloride has the formula NH₄Cl. State how many "
                "hydrogen atoms and how many chlorine atoms are in one "
                "particle.",
        "options": [
            {"text": "One hydrogen atom and four chlorine atoms",
             "correct": False,
             "why": "The 4 sits after the H, so it counts hydrogen. The Cl "
                    "carries no number, which means one"},
            {"text": "Four hydrogen atoms and four chlorine atoms",
             "correct": False,
             "why": "A small number counts only the symbol in front of it. "
                    "It does not carry on to the next one"},
            {"text": "Five hydrogen atoms and one chlorine atom",
             "correct": False,
             "why": "Five adds the nitrogen atom to the hydrogen count. "
                    "Nitrogen is a different element"},
            {"text": "Four hydrogen atoms and one chlorine atom",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c2-03-s19",
        "band": "standard",
        "text": "Magnesium hydroxide, the active ingredient in indigestion "
                "tablets, is Mg(OH)₂. Calculate the total number of atoms in "
                "one particle.",
        "options": [
            {"text": "Three", "correct": False,
             "why": "Three reads the brackets once and ignores the 2 "
                    "outside them"},
            {"text": "Four", "correct": False,
             "why": "Four doubles what is in the brackets but drops the "
                    "magnesium atom in front of them"},
            {"text": "Five", "correct": True},
            {"text": "Six", "correct": False,
             "why": "Six doubles the magnesium as well. The 2 outside the "
                    "brackets reaches only what is inside them"},
        ],
        "figure": None,
    },
    {
        "id": "c2-03-s20",
        "band": "standard",
        "text": "A puddle dries up on a hot day and the water disappears. "
                "Explain what has happened to the compound water.",
        "options": [
            {"text": "Its particles have spread into the air, still as water",
             "correct": True},
            {"text": "It has split into hydrogen and oxygen",
             "correct": False,
             "why": "Splitting water takes a strong electric current. A warm "
                    "day supplies nothing like enough"},
            {"text": "It has joined the air to make a new compound",
             "correct": False,
             "why": "No reaction happens. The same water can be collected "
                    "again as rain, unchanged"},
            {"text": "Its particles have been destroyed by the heat",
             "correct": False,
             "why": "Heat never destroys particles. Every water particle "
                    "that left the puddle is still in the air"},
        ],
        "figure": None,
    },
    {
        "id": "c2-03-s21",
        "band": "standard",
        "text": "A candle burns in air and makes carbon dioxide. State where "
                "the carbon atoms and the oxygen atoms in that gas have come "
                "from.",
        "options": [
            {"text": "Both from the wax, which holds carbon dioxide already",
             "correct": False,
             "why": "Wax holds carbon and hydrogen, not carbon dioxide. The "
                    "gas is made during the burning"},
            {"text": "The carbon from the air and the oxygen from the wax",
             "correct": False,
             "why": "It is the other way round. Air holds very little "
                    "carbon, and wax holds a great deal"},
            {"text": "Both from the air, which holds carbon dioxide already",
             "correct": False,
             "why": "Air does hold a trace of carbon dioxide, but the candle "
                    "makes far more than was there. The carbon is the wax's"},
            {"text": "The carbon from the wax and the oxygen from the air",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c2-03-s22",
        "band": "standard",
        "text": "Methane is CH₄. A student says it must be a mixture of "
                "carbon and hydrogen, because it holds both. Explain the "
                "error.",
        "options": [
            {"text": "The two elements are present in unequal amounts here",
             "correct": False,
             "why": "Unequal amounts are normal in compounds and in "
                    "mixtures. It is not what decides between them"},
            {"text": "The atoms are bonded, so methane is a single substance",
             "correct": True},
            {"text": "Carbon is a solid, so it cannot be part of any gas",
             "correct": False,
             "why": "A bonded carbon atom takes the properties of whatever "
                    "it is part of. Carbon dioxide is a gas too"},
            {"text": "A mixture has to hold at least three substances in it",
             "correct": False,
             "why": "Two is enough for a mixture. Iron stirred with sulfur "
                    "is one"},
        ],
        "figure": None,
    },
    {
        "id": "c2-03-s23",
        "band": "standard",
        "text": "One gas jar holds ammonia. Another holds nitrogen and "
                "hydrogen simply mixed. Give the result of a lit splint in "
                "each jar.",
        "options": [
            {"text": "The ammonia jar pops and the mixed jar does not",
             "correct": False,
             "why": "It is the wrong way round. Ammonia holds no loose "
                    "hydrogen, and loose hydrogen is what pops"},
            {"text": "The mixed jar pops and the ammonia jar does not",
             "correct": True},
            {"text": "Both jars pop, because both hold hydrogen atoms",
             "correct": False,
             "why": "Holding hydrogen atoms is not the same as holding "
                    "hydrogen. In ammonia they are bonded to nitrogen"},
            {"text": "Neither jar pops, because nitrogen smothers a flame",
             "correct": False,
             "why": "Nitrogen does not stop the hydrogen in the mixture from "
                    "reaching the splint and popping"},
        ],
        "figure": None,
    },
    {
        "id": "c2-03-s24",
        "band": "standard",
        "text": "Chalk is soft and white, marble is hard and polished, and "
                "both are calcium carbonate. State what must be true of both "
                "of them.",
        "options": [
            {"text": "They hold the same elements in the same fixed ratio",
             "correct": True},
            {"text": "They hold the same three elements in a different "
                     "fixed ratio",
             "correct": False,
             "why": "Different ratios would make them different compounds "
                    "with different names"},
            {"text": "They are mixtures of calcium, carbon and oxygen",
             "correct": False,
             "why": "A mixture of those three would let each behave as "
                    "itself. Carbon is black and oxygen is a gas"},
            {"text": "They hold calcium only, with other things added "
                     "on later",
             "correct": False,
             "why": "Carbonate names carbon and oxygen as well. They are "
                    "part of the compound, not additions to it"},
        ],
        "figure": None,
    },
    {
        "id": "c2-03-s25",
        "band": "standard",
        "text": "Salt is stirred into water and the liquid goes clear. A "
                "student says the salt has broken into sodium and chlorine. "
                "Explain what is wrong.",
        "options": [
            {"text": "Dissolving splits it, but the pieces are too small to "
                     "see",
             "correct": False,
             "why": "Nothing is split. Sodium would react violently with the "
                    "water and chlorine would smell sharply"},
            {"text": "Dissolving spreads the salt out and it stays sodium "
                     "chloride",
             "correct": True},
            {"text": "Dissolving joins the salt to the water as a new "
                     "compound",
             "correct": False,
             "why": "No new compound forms. Boil the water away and the same "
                    "salt is left behind"},
            {"text": "Dissolving destroys the salt entirely, which is "
                     "why it vanishes from view",
             "correct": False,
             "why": "The salt is still there and can be tasted. Out of sight "
                    "is not destroyed"},
        ],
        "figure": None,
    },
    {
        "id": "c2-03-s26",
        "band": "standard",
        "text": "A gate turns from grey iron to red-brown crumbly rust. A "
                "student says the iron is still there, so the gate is as "
                "strong as ever. Respond.",
        "options": [
            {"text": "The iron atoms are gone, destroyed by the oxygen",
             "correct": False,
             "why": "Atoms are never destroyed in a reaction. Every iron "
                    "atom is still in the rust"},
            {"text": "The iron atoms are there, but the substance is not "
                     "iron",
             "correct": True},
            {"text": "The iron is there and strong, under a red coating",
             "correct": False,
             "why": "Rust is not a coating over intact iron. The iron itself "
                    "has been used up making it"},
            {"text": "The iron has changed into a different element",
             "correct": False,
             "why": "A chemical reaction cannot change one element into "
                    "another. It only joins atoms up differently"},
        ],
        "figure": None,
    },
    {
        "id": "c2-03-s27",
        "band": "standard",
        "text": "A chemist analyses a pure substance and finds nothing in it "
                "but carbon atoms. Can that substance be a compound?",
        "options": [
            {"text": "Yes, as long as the carbon atoms are all bonded "
                     "to one another",
             "correct": False,
             "why": "Bonding alone is not enough. The atoms bonded together "
                    "have to be atoms of different elements"},
            {"text": "Yes, because a great many atoms are joined up in it",
             "correct": False,
             "why": "Number of atoms decides nothing. A large lump of "
                    "carbon is still the element carbon"},
            {"text": "No, because a compound needs at least two elements",
             "correct": True},
            {"text": "No, because carbon atoms cannot bond to anything at "
                     "all",
             "correct": False,
             "why": "Carbon bonds readily. It is in carbon dioxide, methane "
                    "and every sugar"},
        ],
        "figure": None,
    },
    {
        "id": "c2-03-s28",
        "band": "standard",
        "text": "Tap water holds dissolved minerals and the amount varies "
                "from town to town. Distilled water holds none. State which "
                "of the two is a compound.",
        "options": [
            {"text": "The tap water, because it holds more than one "
                     "substance",
             "correct": False,
             "why": "Holding several substances in no fixed proportion is "
                    "exactly what makes it a mixture"},
            {"text": "Both of them, because both are mostly water by mass",
             "correct": False,
             "why": "Mostly one substance is not the same as one substance. "
                    "The tap water is still a mixture"},
            {"text": "Neither of them, because water splits under "
                     "electricity",
             "correct": False,
             "why": "Splitting into elements by a reaction is what compounds "
                    "do. It does not stop water being one"},
            {"text": "The distilled water, because it is nothing but H₂O",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c2-03-s29",
        "band": "standard",
        "text": "Sample A of a white powder is 40% calcium by mass and "
                "sample B is 31% calcium by mass. State what that comparison "
                "tells you.",
        "options": [
            {"text": "They cannot both be the same pure compound",
             "correct": True},
            {"text": "They are the same compound, weighed carelessly",
             "correct": False,
             "why": "A nine per cent gap is far too large for weighing "
                    "error. Something is genuinely different"},
            {"text": "They are the same compound in different amounts",
             "correct": False,
             "why": "A percentage by mass does not change with the size of "
                    "the sample. That is the point of using one"},
            {"text": "They are both elements rather than compounds",
             "correct": False,
             "why": "An element would be 100% of one thing. Both hold "
                    "calcium and something else"},
        ],
        "figure": None,
    },
    {
        "id": "c2-03-s30",
        "band": "standard",
        "text": "Once iron and sulfur begin to react, the glow spreads "
                "through the whole dish with the burner taken away. State "
                "what that shows about the reaction.",
        "options": [
            {"text": "The burner's heat is travelling along through the "
                     "dish",
             "correct": False,
             "why": "The burner has been removed, so there is no heat coming "
                    "from it. The reaction is making its own"},
            {"text": "It gives out more energy than it needs to keep going",
             "correct": True},
            {"text": "It takes energy in from the room around it as it "
                     "spreads",
             "correct": False,
             "why": "A reaction taking energy in would cool down and stop "
                    "once the burner was removed"},
            {"text": "The sulfur melts and carries the heat along with it",
             "correct": False,
             "why": "Molten sulfur would spread heat a little way and then "
                    "cool. It cannot keep a glow going across a dish"},
        ],
        "figure": None,
    },
    {
        "id": "c2-03-s31",
        "band": "standard",
        "text": "Salt is dissolved in water and the water is then evaporated "
                "away. The same mass of salt is recovered. State what that "
                "result shows.",
        "options": [
            {"text": "The salt and water had reacted, and heat undid it",
             "correct": False,
             "why": "Heating does not reverse a reaction to order. Nothing "
                    "had reacted in the first place"},
            {"text": "The salt was destroyed and then remade by the heat",
             "correct": False,
             "why": "Heat does not build salt. What was recovered had been "
                    "there the whole time"},
            {"text": "The salt and water had formed a mixture, not a "
                     "compound",
             "correct": True},
            {"text": "The salt reacted with the water and then with the air",
             "correct": False,
             "why": "Two reactions would leave a different substance behind. "
                    "The same salt comes back"},
        ],
        "figure": None,
    },
    {
        "id": "c2-03-s32",
        "band": "standard",
        "text": "Pure aspirin melts sharply at 135 °C. A sample from a "
                "cupboard melts gradually between 118 °C and 130 °C. Suggest "
                "what that says about the sample.",
        "options": [
            {"text": "It is a pure compound that was heated too quickly",
             "correct": False,
             "why": "Heating quickly blurs a melting point by a degree or "
                    "two, not by twelve"},
            {"text": "It is a mixture rather than one pure compound",
             "correct": True},
            {"text": "It is a different pure compound that melts in a range",
             "correct": False,
             "why": "Every pure compound melts at one sharp temperature. A "
                    "range is the mark of a mixture"},
            {"text": "It is an element, since elements melt across a range",
             "correct": False,
             "why": "Elements are pure substances and melt sharply too. "
                    "Iron melts at one temperature"},
        ],
        "figure": None,
    },
    {
        "id": "c2-03-h10",
        "band": "harder",
        "text": "A student proposes a rule: any substance holding two "
                "elements is a compound. Test that rule against air and "
                "against carbon dioxide.",
        "options": [
            {"text": "It holds — air is a compound of nitrogen and oxygen",
             "correct": False,
             "why": "Air's proportions vary from place to place and its "
                    "gases can be parted by cooling. It is a mixture"},
            {"text": "It fails — air holds several elements and is a mixture",
             "correct": True},
            {"text": "It fails — carbon dioxide holds two elements and is a "
                     "mixture",
             "correct": False,
             "why": "Carbon dioxide is the compound of the pair. It has one "
                    "fixed formula and puts out fires"},
            {"text": "It holds — both of them are compounds of two elements",
             "correct": False,
             "why": "Only one of the two is. Air is the case that breaks the "
                    "rule"},
        ],
        "figure": None,
    },
    {
        "id": "c2-03-h11",
        "band": "harder",
        "text": "Copper forms two compounds with oxygen: in one, 64 g of "
                "copper joins 16 g of oxygen; in the other, 128 g joins 16 g. "
                "A student says one must be a mixture. Evaluate that.",
        "options": [
            {"text": "Right — one pair of elements can only ever have "
                     "one fixed proportion",
             "correct": False,
             "why": "Two elements can form several compounds, each with its "
                    "own fixed proportion. Carbon and oxygen do"},
            {"text": "Wrong — the two are one compound, weighed out "
                     "differently",
             "correct": False,
             "why": "Doubling the copper against the same oxygen is a "
                    "different composition, so it is a different compound"},
            {"text": "Right — the second is the first with spare copper "
                     "mixed in",
             "correct": False,
             "why": "The second is a compound in its own right, with its own "
                    "colour and its own fixed proportion"},
            {"text": "Wrong — each compound has its own fixed proportion",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c2-03-h12",
        "band": "harder",
        "text": "Hydrogen sulfide stinks of rotten eggs, although neither "
                "hydrogen nor sulfur smells of anything like it. A student "
                "says the smell belongs to the compound alone. Evaluate that.",
        "options": [
            {"text": "Right — a compound's properties belong to the compound "
                     "itself",
             "correct": True},
            {"text": "Wrong — the smell comes from sulfur left over in the "
                     "gas",
             "correct": False,
             "why": "Solid sulfur has almost no smell, so leftover sulfur "
                    "could not produce this one"},
            {"text": "Wrong — a compound's smell is an average of its "
                     "elements'",
             "correct": False,
             "why": "Nothing about a compound is an average of its elements. "
                    "Its properties are new ones"},
            {"text": "Right — but only because the two elements cancel each "
                     "other out",
             "correct": False,
             "why": "Nothing is cancelled. Both elements are still in the "
                    "gas, bonded, and the smell is the compound's own"},
        ],
        "figure": None,
    },
    {
        "id": "c2-03-h13",
        "band": "harder",
        "text": "Boiling parts sea water into salt and water, but no amount "
                "of boiling parts salt into sodium and chlorine. Explain what "
                "that pair of facts establishes.",
        "options": [
            {"text": "Boiling parts a mixture, while parting a compound "
                     "needs a reaction",
             "correct": True},
            {"text": "Boiling parts both of them, but the salt "
                     "needs a far higher heat",
             "correct": False,
             "why": "Salt boils as salt at 1400 °C and still comes off as "
                    "salt. Temperature is not the obstacle"},
            {"text": "Boiling parts a compound, so sea water is the compound "
                     "here",
             "correct": False,
             "why": "It is the other way round. Sea water is the mixture, "
                    "and its saltiness varies from sea to sea"},
            {"text": "Neither is parted, since boiling only drives off the "
                     "water",
             "correct": False,
             "why": "Driving off the water is exactly how the salt is "
                    "recovered. That counts as parting the mixture"},
        ],
        "figure": None,
    },
    {
        "id": "c2-03-h14",
        "band": "harder",
        "text": "Potassium reacts with bromine to give one compound, and with "
                "oxygen to give another. Predict the names of the two "
                "compounds.",
        "options": [
            {"text": "Potassium bromate and potassium oxide", "correct": False,
             "why": "Bromate would mean oxygen is in there as well. Only "
                    "potassium and bromine reacted"},
            {"text": "Potassium bromine and potassium oxygen", "correct": False,
             "why": "The second element's name always changes when a "
                    "compound forms. Leaving it whole names a mixture"},
            {"text": "Potassium bromide and potassium oxide", "correct": True},
            {"text": "Bromine potasside and oxygen potasside", "correct": False,
             "why": "The metal is named first and keeps its name. It is the "
                    "non-metal that takes the -ide ending"},
        ],
        "figure": None,
    },
    {
        "id": "c2-03-h15",
        "band": "harder",
        "text": "A jar is labelled sodium nitrate. A student says it holds "
                "sodium and nitrogen only. Evaluate that, and say what the "
                "ending adds.",
        "options": [
            {"text": "Right — the -ate ending simply marks a metal compound",
             "correct": False,
             "why": "Metal compounds take -ide just as often. The ending "
                    "reports the elements, not the kind of element"},
            {"text": "Right — nitrate is simply another way of writing "
                     "nitrogen",
             "correct": False,
             "why": "Nitrate and nitride name different compounds. The "
                    "ending is doing real work"},
            {"text": "Wrong — the -ate ending shows oxygen is present as "
                     "well",
             "correct": True},
            {"text": "Wrong — the -ate ending shows hydrogen is present as "
                     "well",
             "correct": False,
             "why": "The -ate ending always marks oxygen. Hydrogen is never "
                    "what it reports"},
        ],
        "figure": None,
    },
    {
        "id": "c2-03-h16",
        "band": "harder",
        "text": "Nitrogen and oxygen form the compounds nitrogen monoxide "
                "and nitrogen dioxide. A sealed flask of air holds the same "
                "two elements and forms neither. Explain the difference.",
        "options": [
            {"text": "In the flask the two are unjoined; in the compounds "
                     "they are bonded",
             "correct": True},
            {"text": "In the flask the two are bonded, but in a "
                     "proportion that keeps drifting",
             "correct": False,
             "why": "A bonded proportion cannot drift. Nothing in ordinary "
                    "air is bonded together at all"},
            {"text": "In the flask the two are bonded only while the air is "
                     "cold",
             "correct": False,
             "why": "Cooling air liquefies it and the gases separate out "
                    "unchanged, which is the opposite of bonding"},
            {"text": "In the flask the two are the same gas in different "
                     "forms",
             "correct": False,
             "why": "Nitrogen and oxygen are different elements with "
                    "different atoms, in the flask as everywhere else"},
        ],
        "figure": None,
    },
    {
        "id": "c2-03-h17",
        "band": "harder",
        "text": "Two compounds are written CaCO₃ and CaC₂. A student says "
                "they cannot be the same compound, because one holds oxygen "
                "and the other does not. Evaluate that.",
        "options": [
            {"text": "Right — but the real difference is how much calcium "
                     "each holds",
             "correct": False,
             "why": "Both hold one calcium atom. It is the oxygen, and the "
                    "number of carbon atoms, that differ"},
            {"text": "Wrong — both hold calcium and carbon, which settles "
                     "the matter",
             "correct": False,
             "why": "Which elements are present is only half of a formula. "
                    "The oxygen in the first one is part of the list too"},
            {"text": "Wrong — the O₃ is a separate substance mixed in with "
                     "the rest",
             "correct": False,
             "why": "Everything inside one formula is bonded into one "
                    "compound. Nothing in it is mixed in"},
            {"text": "Right — the element lists differ, so the compounds "
                     "differ",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c2-03-h18",
        "band": "harder",
        "text": "Ammonium nitrate, a common fertiliser, has the formula "
                "NH₄NO₃. Determine how many atoms of each element are in one "
                "particle.",
        "options": [
            {"text": "One nitrogen, four hydrogen and three oxygen",
             "correct": False,
             "why": "There is an N at each end of the formula, so the two "
                    "nitrogen atoms have to be added together"},
            {"text": "Two nitrogen, four hydrogen and four oxygen",
             "correct": False,
             "why": "The 3 after the last O counts the oxygen atoms. Four "
                    "counts the 4 from the hydrogen by mistake"},
            {"text": "Two nitrogen, four hydrogen and three oxygen",
             "correct": True},
            {"text": "Two nitrogen, three hydrogen and four oxygen",
             "correct": False,
             "why": "The 4 belongs to the H and the 3 to the O. The two "
                    "numbers have been swapped over"},
        ],
        "figure": None,
    },
    {
        "id": "c2-03-h19",
        "band": "harder",
        "text": "Aluminium sulfate has the formula Al₂(SO₄)₃. Determine the "
                "total number of atoms in one particle of it.",
        "options": [
            {"text": "7", "correct": False,
             "why": "Seven reads the brackets once and ignores the 3 "
                    "standing outside them"},
            {"text": "15", "correct": False,
             "why": "Fifteen multiplies the oxygen by three but leaves the "
                    "sulfur inside the brackets un-multiplied"},
            {"text": "21", "correct": False,
             "why": "Twenty-one multiplies the aluminium by three as well. "
                    "The 3 reaches only what is inside the brackets"},
            {"text": "17", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c2-03-h20",
        "band": "harder",
        "text": "A chemist must show that a colourless liquid is a compound "
                "and not a mixture of two liquids. Which result would settle "
                "it?",
        "options": [
            {"text": "It boils at one fixed temperature and splits only "
                     "under electricity",
             "correct": True},
            {"text": "It boils across a range of temperatures "
                     "and settles into layers",
             "correct": False,
             "why": "A boiling range and layers are both marks of a mixture. "
                    "That result would settle it the other way"},
            {"text": "It is clear and colourless right through the whole "
                     "sample",
             "correct": False,
             "why": "Looking at a liquid settles nothing. Two well-mixed "
                    "liquids look just as even"},
            {"text": "It can be poured, filtered and evaporated without "
                     "changing",
             "correct": False,
             "why": "Those are all physical handling. Surviving them says "
                    "nothing about whether the atoms are bonded"},
        ],
        "figure": None,
    },
    {
        "id": "c2-03-h21",
        "band": "harder",
        "text": "A fire extinguisher is filled with carbon dioxide. A student "
                "says it should feed a fire, because it contains oxygen. "
                "Evaluate that claim.",
        "options": [
            {"text": "Right — any substance holding oxygen atoms will feed a "
                     "fire",
             "correct": False,
             "why": "Water holds oxygen atoms and puts fires out. Holding "
                    "the atoms is not the same as supplying the gas"},
            {"text": "Wrong — the oxygen atoms are bonded into the compound",
             "correct": True},
            {"text": "Right — the oxygen leaks back out of it as the gas "
                     "warms",
             "correct": False,
             "why": "Warming a compound does not release its elements. The "
                    "bonds hold at the temperature of a fire"},
            {"text": "Wrong — carbon dioxide holds no oxygen atoms at all",
             "correct": False,
             "why": "The name and the formula both say it holds two oxygen "
                    "atoms. The point is that they are bonded"},
        ],
        "figure": None,
    },
    {
        "id": "c2-03-h22",
        "band": "harder",
        "text": "Natural gas is mostly methane, CH₄, and burning it wets the "
                "inside of a cold window. A student says the water is made in "
                "the flame from the methane's hydrogen. Evaluate that.",
        "options": [
            {"text": "Wrong — the water was mixed into the gas supply "
                     "beforehand",
             "correct": False,
             "why": "Dry methane wets a cold window just as much. The water "
                    "is made in the flame, not carried into it"},
            {"text": "Right — the hydrogen joins oxygen drawn in from the "
                     "air",
             "correct": True},
            {"text": "Right — but the oxygen for it comes from the methane "
                     "itself",
             "correct": False,
             "why": "There is no oxygen in CH₄ at all. Every oxygen atom in "
                    "the water came out of the air"},
            {"text": "Wrong — the water is made from the carbon in the "
                     "methane",
             "correct": False,
             "why": "The carbon ends up in the carbon dioxide. It is the "
                    "hydrogen that ends up in the water"},
        ],
        "figure": None,
    },
    {
        "id": "c2-03-h23",
        "band": "harder",
        "text": "Ammonia dissolved in water turns damp red litmus blue, "
                "although neither nitrogen nor hydrogen does. A student says "
                "the litmus is detecting nitrogen. Evaluate that.",
        "options": [
            {"text": "Wrong — the alkaline behaviour belongs to ammonia "
                     "itself",
             "correct": True},
            {"text": "Right — nitrogen is the alkaline one of the two "
                     "elements",
             "correct": False,
             "why": "Nitrogen gas turns litmus no colour at all. On its own "
                    "it is almost entirely unreactive"},
            {"text": "Right — litmus responds to whichever element is the "
                     "heavier",
             "correct": False,
             "why": "Litmus responds to acids and alkalis. Mass has nothing "
                    "to do with what it shows"},
            {"text": "Wrong — the litmus is detecting the hydrogen in it "
                     "instead",
             "correct": False,
             "why": "Hydrogen gas does not turn litmus blue either. The "
                    "property belongs to the whole compound"},
        ],
        "figure": None,
    },
    {
        "id": "c2-03-h24",
        "band": "harder",
        "text": "A builder says chalk, marble and limestone must be three "
                "different substances, because they look and feel different. "
                "All three are calcium carbonate. Explain how both can hold.",
        "options": [
            {"text": "They are different compounds that happen to share one "
                     "name",
             "correct": False,
             "why": "A name reports a composition. Three different "
                    "compositions would need three different names"},
            {"text": "They are the same compound in three different fixed "
                     "ratios",
             "correct": False,
             "why": "One compound has one ratio. Change it and you have a "
                    "different compound"},
            {"text": "They are the same compound, differing in texture and "
                     "grain",
             "correct": True},
            {"text": "They hold calcium carbonate joined on to different "
                     "extra elements",
             "correct": False,
             "why": "Joining on another element would change the formula and "
                    "the name. All three answer to CaCO₃"},
        ],
        "figure": None,
    },
    {
        "id": "c2-03-h25",
        "band": "harder",
        "text": "Molten sodium chloride can be split by a strong electric "
                "current into sodium and chlorine, but no sieve, filter or "
                "magnet parts it. What does that pair of facts establish?",
        "options": [
            {"text": "Its elements are mixed too finely for any sieve to "
                     "reach",
             "correct": False,
             "why": "A finely mixed powder still gives its parts up to "
                    "dissolving or a magnet. This one gives up nothing"},
            {"text": "Its elements are bonded, so nothing whatever can part "
                     "them",
             "correct": False,
             "why": "Something did part them. Electricity is a chemical "
                    "change and it worked"},
            {"text": "It is a mixture, since electricity managed to part it "
                     "at all",
             "correct": False,
             "why": "Physical methods part mixtures. Needing a chemical "
                    "change is the mark of a compound"},
            {"text": "Its elements are bonded, so only a reaction parts them",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c2-03-h26",
        "band": "harder",
        "text": "Iron is grey, strong and conducts electricity. Rust is "
                "red-brown, crumbly and conducts poorly. A student says rust "
                "is iron with something added. Say what is right and what is "
                "wrong in that.",
        "options": [
            {"text": "Oxygen is added, but the product is a new substance, "
                     "not iron",
             "correct": True},
            {"text": "Oxygen is added, and the iron underneath is left "
                     "unchanged",
             "correct": False,
             "why": "The iron that rusted has gone into the rust. There is "
                    "less iron than there was, not the same amount"},
            {"text": "Nothing is added, and the iron simply wears out with "
                     "age",
             "correct": False,
             "why": "Atoms do not wear out. Rust is heavier than the iron "
                    "it came from, because oxygen joined on"},
            {"text": "Oxygen is added, and it turns the iron into a "
                     "different element altogether",
             "correct": False,
             "why": "No chemical reaction turns one element into another. "
                    "The iron atoms are still iron atoms"},
        ],
        "figure": None,
    },
    {
        "id": "c2-03-h27",
        "band": "harder",
        "text": "A black solid is 100% carbon by mass and survives heating, "
                "acid and electrolysis unchanged. Determine whether it can be "
                "a compound, and justify the answer.",
        "options": [
            {"text": "It can, because its carbon atoms are bonded to one "
                     "another",
             "correct": False,
             "why": "Bonding is necessary but not sufficient. The atoms "
                    "bonded have to come from different elements"},
            {"text": "It cannot, because a compound needs two elements at "
                     "least",
             "correct": True},
            {"text": "It cannot, because every compound breaks down under "
                     "heating",
             "correct": False,
             "why": "Many compounds survive strong heating. The reason this "
                    "one is not a compound is its single element"},
            {"text": "It can, because any substance that resists acid "
                     "must be a compound",
             "correct": False,
             "why": "Gold resists acid and is an element. Resisting acid "
                    "classifies nothing"},
        ],
        "figure": None,
    },
    {
        "id": "c2-03-h28",
        "band": "harder",
        "text": "Liquid A boils at 100 °C exactly and gives two gases when a "
                "current is passed through it. Liquid B boils between 78 °C "
                "and 100 °C and gives no gases. Classify each liquid.",
        "options": [
            {"text": "A is a mixture and B is a compound",
             "correct": False,
             "why": "It is the reverse. A sharp boiling point marks a pure "
                    "substance, and a range marks a mixture"},
            {"text": "Both are compounds, boiling at different temperatures",
             "correct": False,
             "why": "A compound boils at one temperature, not across a "
                    "range. B's range rules it out"},
            {"text": "A is a compound and B is a mixture", "correct": True},
            {"text": "Both are mixtures, since both are colourless liquids",
             "correct": False,
             "why": "Colour settles nothing at all. The boiling behaviour is "
                    "what separates these two"},
        ],
        "figure": None,
    },
    {
        "id": "c2-03-h29",
        "band": "harder",
        "text": "Four samples of a white compound give 40.0%, 40.1%, 39.9% "
                "and 40.0% calcium by mass. A fifth gives 36.2%. Suggest what "
                "is most likely about the fifth sample.",
        "options": [
            {"text": "It is the same compound with less calcium bonded into "
                     "it",
             "correct": False,
             "why": "A compound's proportion is not adjustable. Less calcium "
                    "would make it a different compound"},
            {"text": "It shows that a compound's composition can drift a "
                     "little",
             "correct": False,
             "why": "The first four agree to a tenth of a per cent, which is "
                    "exactly what no drift looks like"},
            {"text": "It is the same compound, weighed out on a warmer day",
             "correct": False,
             "why": "A percentage by mass does not depend on the weather. "
                    "Nearly four per cent is far too large for that"},
            {"text": "It is not pure, so something else is present in it",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c2-03-h30",
        "band": "harder",
        "text": "Making iron sulfide from its elements gives energy out, and "
                "getting the iron back from iron sulfide takes energy in. "
                "Explain what that pair of facts says about a compound.",
        "options": [
            {"text": "The compound stores away the heat it was made "
                     "with and returns it",
             "correct": False,
             "why": "Heat is not stored and handed back. Undoing the "
                    "reaction costs energy rather than releasing it"},
            {"text": "A compound gives energy out whichever way it is "
                     "changed",
             "correct": False,
             "why": "Then a compound would be an endless supply of energy. "
                    "Breaking it up costs what making it gave"},
            {"text": "Bonds made release energy, and breaking them costs "
                     "energy",
             "correct": True},
            {"text": "The iron takes energy in only because it is a metal",
             "correct": False,
             "why": "Non-metals cost energy to recover too. The bonds are "
                    "what decide it, not the kind of element"},
        ],
        "figure": None,
    },
    {
        "id": "c2-03-h31",
        "band": "harder",
        "text": "A student stirs sugar into hot tea until none is visible, "
                "and says no compound was made because boiling the tea away "
                "returns the sugar. Evaluate that.",
        "options": [
            {"text": "Wrong — dissolving is a chemical reaction between the "
                     "two",
             "correct": False,
             "why": "Dissolving is a physical change. No new substance "
                    "appears and none has to be reacted to undo it"},
            {"text": "Right — but only because sugar cannot bond to anything "
                     "at all",
             "correct": False,
             "why": "Sugar's own atoms are bonded, and it reacts readily "
                    "when it is burned. It simply does not bond to water"},
            {"text": "Right — getting it back unchanged shows nothing was "
                     "joined",
             "correct": True},
            {"text": "Wrong — the sugar bonded to the water and then came "
                     "apart",
             "correct": False,
             "why": "Bonding and unbonding are reactions, and neither "
                    "happens here. The sugar was never joined to anything"},
        ],
        "figure": None,
    },
    {
        "id": "c2-03-h32",
        "band": "harder",
        "text": "Two white solids are handed over: one is a pure compound "
                "and one is a mixture of two compounds. Only a melting-point "
                "apparatus is available. Describe the result that identifies "
                "the pure one.",
        "options": [
            {"text": "The pure one melts across a wide range of "
                     "temperatures",
             "correct": False,
             "why": "A range is what the mixture gives. Purity shows as a "
                    "sharp, single temperature"},
            {"text": "The pure one melts at the higher of the two "
                     "temperatures",
             "correct": False,
             "why": "A mixture usually melts lower than either substance "
                    "alone, and across a range either way"},
            {"text": "The pure one melts sharply at a single temperature",
             "correct": True},
            {"text": "The pure one does not melt at all before it breaks "
                     "down",
             "correct": False,
             "why": "Most pure solids melt cleanly. Decomposing instead of "
                    "melting is not a test of purity"},
        ],
        "figure": None,
    },
]
