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
        "text": "Sea water from the Red Sea is saltier than sea water from "
                "the Baltic. Which word describes sea water?",
        "options": [
            {"text": "A compound, because salt and water are chemically "
                     "joined together everywhere that sea water is found",
             "correct": False,
             "why": "The salt is dissolved, not joined. Boil the water off "
                    "and the salt comes back unchanged"},
            {"text": "An element, because it is one substance with one name",
             "correct": False,
             "why": "One name is not one substance. Sea water holds water, "
                    "salt and a good deal else"},
            {"text": "A mixture",
             "correct": True},
            {"text": "A compound, because it has its own properties",
             "correct": False,
             "why": "Its properties change with how salty it is, and a "
                    "compound's cannot. That is what varying proportions "
                    "mean"},
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
]
