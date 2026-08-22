"""C10 lesson 04 — A planet with limits: twelve questions (MRB-281).

The lesson's argument is one shape: the crust holds a fixed stock, extraction
is one-way, and recycling returns SOME of it — how much being a property of
the material rather than of how carefully anyone sorts a bin. The page teaches
it with a bench that runs 1000 kg round a loop for five materials at four
collection rates, and a shelf of five extracted things whose limits are five
different kinds of limit.

These twelve probe the angles the mastery ladder leaves alone: what "finite"
actually claims, what an ore is, where the energy in recycling goes, why a
reserve figure moves, and what a closed loop that is not closed looks like
from outside.

The distractors are built from the lesson's declared misconceptions.

`EARTH-11` (if we recycled everything we would never run out) drives the wrong
options in e03, s03 and h03. Each treats the loop as lossless.

`EARTH-12` (how much comes back depends on how carefully people sort) drives
e03, s01 and s02, where a collection rate is offered as the explanation for a
result the bench produced with collection held equal.

`EARTH-13` ("years left" is a measured fact) drives h01, where the reserve
moves and nothing about the planet has.

⚠️ **NO QUESTION QUOTES A YIELD FIGURE TO TWO DECIMAL PLACES.** NOTES-C10 is
explicit that the ordering is the claim and the second decimal place is not,
so nothing here can be got wrong by an examiner disagreeing with 0.92. Where a
number is used it is one the lesson derives and shows on the panel — about a
twentieth of the energy, about half of the PET, nine in ten collected.

⚠️ MRB-278 · ANSWER POSITION. The correct answer's index cycles through each
band — 0,1,2,3 · 1,2,3,0 · 2,3,0,1 — so this file holds three of each.

⚠️ BAND VALUES ARE FULL WORDS — `easier`, `standard`, `harder`, never the
letters.
"""

UNIT = "C10"
LESSON = "a-planet-with-limits"
LESSON_NUMBER = 4

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "c10-04-e01",
        "band": "easier",
        "text": "What does it mean to call crude oil a finite resource?",
        "options": [
            {"text": "It formed over millions of years and is not being "
                     "replaced as fast as we use it",
             "correct": True},
            {"text": "There is only a very small amount of it left "
                     "underneath the ground today",
             "correct": False,
             "why": "Finite is about not being replaced, not about how much "
                    "happens to be left today."},
            {"text": "It can only be burnt once before the fuel becomes "
                     "completely useless to us",
             "correct": False,
             "why": "Burning it once is true of any fuel. Finite describes "
                    "the stock in the ground, not the burning."},
            {"text": "It is certain to run out completely within the next "
                     "twenty or thirty years",
             "correct": False,
             "why": "Reserve figures move, and finite makes no claim about a "
                    "date at all."},
        ],
        "figure": None,
    },
    {
        "id": "c10-04-e02",
        "band": "easier",
        "text": "What is an ore?",
        "options": [
            {"text": "A metal that has been dug straight out of the ground "
                     "in its pure form",
             "correct": False,
             "why": "Only gold and a few others are found as the metal. An "
                    "ore is rock, and the metal is locked in a compound."},
            {"text": "Rock containing enough of a metal compound to make "
                     "extracting it worthwhile",
             "correct": True},
            {"text": "Any rock at all that happens to contain a few atoms of "
                     "a useful metal",
             "correct": False,
             "why": "Almost every rock does. What makes a rock an ore is "
                    "having ENOUGH to be worth extracting."},
            {"text": "The waste rock left behind once the metal has been "
                     "taken out of it",
             "correct": False,
             "why": "That is the tailings. It is what the ore becomes after "
                    "processing, not the ore itself."},
        ],
        "figure": None,
    },
    {
        "id": "c10-04-e03",
        "band": "easier",
        "text": "Which pair of actions cuts the amount taken out of the "
                "ground by more than recycling does?",
        "options": [
            {"text": "Sorting waste more carefully and washing everything "
                     "before it goes in the bin",
             "correct": False,
             "why": "Careful sorting feeds the loop, and the loop still "
                    "leaks every pass. It does not stop material leaving "
                    "the ground."},
            {"text": "Burning waste to make electricity and burying whatever "
                     "will not burn",
             "correct": False,
             "why": "Neither returns any material. Burning removes it from "
                    "the loop entirely."},
            {"text": "Using less of the material and using the things made "
                     "from it for longer",
             "correct": True},
            {"text": "Collecting every single bottle that is used and "
                     "melting all of them down",
             "correct": False,
             "why": "Even at perfect collection every pass loses some, so "
                    "extraction slows rather than stopping."},
        ],
        "figure": None,
    },
    {
        "id": "c10-04-e04",
        "band": "easier",
        "text": "What does downcycling mean?",
        "options": [
            {"text": "Recycling a material so many times that its price on "
                     "the market falls",
             "correct": False,
             "why": "Downcycling is about the GRADE the material comes back "
                    "at, not about what it sells for."},
            {"text": "Recycling a material into exactly the same product, "
                     "over and over again",
             "correct": False,
             "why": "That is a closed loop, which is what aluminium does. "
                    "Downcycling is the opposite."},
            {"text": "Sending a material to landfill once it has been "
                     "recycled a few times over",
             "correct": False,
             "why": "Landfill is where the loop ends, not a step inside it."},
            {"text": "Recycling a material into something less demanding, "
                     "because it comes back degraded",
             "correct": True},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "c10-04-s01",
        "band": "standard",
        "text": "Recycled aluminium takes about a twentieth of the energy of "
                "new metal from ore. Recycled glass saves only about a "
                "quarter of the energy of new glass. Why is the glass saving "
                "so much smaller?",
        "options": [
            {"text": "Glass is collected far less often than aluminium cans "
                     "are collected",
             "correct": False,
             "why": "The energy figure is per kilogram of material handled. "
                    "It does not depend on how much is collected."},
            {"text": "Melting is where most of the energy goes, and recycled "
                     "glass still has to be melted",
             "correct": True},
            {"text": "Glass comes back too degraded to be made into a bottle "
                     "again",
             "correct": False,
             "why": "Glass is endlessly remeltable and comes back at full "
                    "grade. Degrading on melting is PET's problem."},
            {"text": "Glass bottles are heavier, so more energy is used "
                     "moving them around",
             "correct": False,
             "why": "Transport is a small part of it. The melting is the "
                    "energy, and it is needed either way."},
        ],
        "figure": None,
    },
    {
        "id": "c10-04-s02",
        "band": "standard",
        "text": "A school collects nine crisp packets in every ten and is "
                "surprised that almost no material comes back. What is the "
                "reason?",
        "options": [
            {"text": "Nine in ten is not a high enough collection rate to "
                     "make any real difference",
             "correct": False,
             "why": "Nine in ten is very high. Aluminium at that rate gets "
                    "about seven lifetimes out of a kilogram of ore."},
            {"text": "The packets are too light for the amount collected to "
                     "matter very much",
             "correct": False,
             "why": "The bench compared equal masses of every material, and "
                    "the gap was still enormous."},
            {"text": "The plastic and the aluminium layers cannot be "
                     "separated, so almost nothing is recovered",
             "correct": True},
            {"text": "Some of the packets must have been put into the wrong "
                     "bin along the way",
             "correct": False,
             "why": "Collection was held equal on purpose. The material is "
                    "the only thing that changed."},
        ],
        "figure": None,
    },
    {
        "id": "c10-04-s03",
        "band": "standard",
        "text": "A council doubles how many plastic bottles it collects, and "
                "the amount of new plastic being made barely falls. Why?",
        "options": [
            {"text": "The bottles are being collected but are never actually "
                     "recycled at all",
             "correct": False,
             "why": "They are recycled. About half of what is collected "
                    "comes back usable, and that is the whole point."},
            {"text": "New plastic is cheaper, so nobody wants to buy the "
                     "recycled material",
             "correct": False,
             "why": "Price affects demand, but the physical reason is that "
                    "PET degrades when it is melted."},
            {"text": "Doubling the collection rate can only ever halve the "
                     "amount of new plastic needed",
             "correct": False,
             "why": "That would be true of a loop that lost nothing. This "
                    "one leaks every pass, so the gain is far smaller."},
            {"text": "PET degrades on melting, so only about half of what is "
                     "collected can be a bottle again",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c10-04-s04",
        "band": "standard",
        "text": "Helium is collected as a by-product of natural gas and used "
                "to cool the magnets in MRI scanners. Why is helium released "
                "into a room lost for good?",
        "options": [
            {"text": "It rises through the atmosphere and escapes into "
                     "space, so it never comes back",
             "correct": True},
            {"text": "It reacts with the gases in the air and becomes a "
                     "different substance entirely",
             "correct": False,
             "why": "Helium reacts with nothing at all. It is still helium; "
                    "it is simply somewhere we cannot reach."},
            {"text": "It sinks to the ground and is absorbed into the soil "
                     "underneath the building",
             "correct": False,
             "why": "Helium is far less dense than air, so it rises rather "
                    "than sinking."},
            {"text": "It can be recovered from the air later on, but only at "
                     "a very high price",
             "correct": False,
             "why": "It does not stay in the atmosphere to be recovered. "
                    "That is what makes it different from a metal."},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "c10-04-h01",
        "band": "harder",
        "text": "A country's reported copper reserves rise by a fifth in one "
                "year, and no new deposit was found. What is the most likely "
                "explanation?",
        "options": [
            {"text": "More copper ore formed in the crust during the course "
                     "of that year",
             "correct": False,
             "why": "Ores take millions of years to concentrate. Nothing was "
                    "added to the planet in a year."},
            {"text": "The country used less copper, so more of it was left "
                     "in the ground",
             "correct": False,
             "why": "A reserve counts what can be extracted at a profit, not "
                    "what happens to be unused."},
            {"text": "The price rose or the mining improved, so rock that "
                     "was not worth digging now is",
             "correct": True},
            {"text": "The earlier figure had been measured wrongly and has "
                     "now been corrected",
             "correct": False,
             "why": "Possible once. But reserves move routinely with price "
                    "and technology — that is what the word means."},
        ],
        "figure": None,
    },
    {
        "id": "c10-04-h02",
        "band": "harder",
        "text": "Steel is recycled on an enormous scale and phosphate "
                "fertiliser is barely recycled at all — yet phosphate is the "
                "sharper resource problem of the two. Why?",
        "options": [
            {"text": "There is far less phosphate rock in the crust than "
                     "there is iron ore",
             "correct": False,
             "why": "Scarcity is part of it, but the deciding fact is that "
                    "nothing can take phosphorus's place in a crop."},
            {"text": "Phosphate rock is much harder to dig out of the ground "
                     "than iron ore is",
             "correct": False,
             "why": "How hard it is to dig is not what makes a limit sharp. "
                    "Having no substitute is."},
            {"text": "Steel can be reused for ever and phosphate cannot be "
                     "reused at all",
             "correct": False,
             "why": "Phosphorus can be recovered from sewage. The problem is "
                    "that spread thinly on a field it cannot be gathered."},
            {"text": "Nothing can replace phosphorus in a crop, and once it "
                     "is spread thinly it cannot be gathered",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c10-04-h03",
        "band": "harder",
        "text": "Half of a material is collected, and four fifths of what is "
                "collected comes back usable. Roughly how many lifetimes of "
                "service does one kilogram of new material give?",
        "options": [
            {"text": "About 1.7 — each pass returns less than the one before "
                     "and the total settles just under two",
             "correct": True},
            {"text": "About 2.5, because half of it comes back and then half "
                     "of that comes back again",
             "correct": False,
             "why": "Half is not what comes back. Only half of four fifths "
                    "does, which is two fifths of the kilogram."},
            {"text": "Exactly 2, because collecting half of it means the "
                     "material gets used twice over",
             "correct": False,
             "why": "The second pass is 0.4 of a kilogram, not a whole one — "
                    "and there are passes after it."},
            {"text": "Infinitely many, because the material simply keeps "
                     "going round the loop for ever",
             "correct": False,
             "why": "Every pass loses some, so the passes add up to a finite "
                    "number. A leaking loop is still a loop."},
        ],
        "figure": None,
    },
    {
        "id": "c10-04-h04",
        "band": "harder",
        "text": "A company advertises a fleece jacket as “made "
                "entirely from recycled bottles” and calls it proof "
                "that plastic can go round for ever. What is wrong with the "
                "claim?",
        "options": [
            {"text": "The jacket is not really made from bottles, so the "
                     "label is only marketing",
             "correct": False,
             "why": "It genuinely is made from them. What is wrong is what "
                    "happens to the fleece afterwards."},
            {"text": "The fleece cannot become a bottle or another fleece, "
                     "so the loop ends there",
             "correct": True},
            {"text": "Making the fleece uses more energy than making a "
                     "brand-new bottle would use",
             "correct": False,
             "why": "Energy is not what breaks the claim. The loop ending "
                    "after one step is."},
            {"text": "Recycling always makes a material weaker, so the "
                     "fleece will fall apart quickly",
             "correct": False,
             "why": "Aluminium comes back as good as new, and the fleece is "
                    "durable. Degrading is a property of some materials, not "
                    "of recycling."},
        ],
        "figure": None,
    },
]
