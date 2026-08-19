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
]
