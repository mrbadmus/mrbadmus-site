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

    # ── easier · MRB-335 top-up ─────────────────────────────────────────
    {
        "id": "c10-04-e05",
        "band": "easier",
        "text": "What is a RESERVE, as this lesson uses the word?",
        "options": [
            {"text": "A store of material kept back for emergencies",
             "correct": False,
             "why": "That is the everyday sense. Here it is about what is "
                    "economically extractable"},
            {"text": "The part of a resource that has already been used",
             "correct": False,
             "why": "A reserve is what is still available under today's "
                    "conditions"},
            {"text": "The total amount of a resource that is in the ground "
                     "anywhere on Earth, measured by surveying and then "
                     "published as a figure for how much is left",
             "correct": False,
             "why": "That is the whole stock. A reserve is the part worth "
                    "digging today, which is why the figure moves"},
            {"text": "The part of a resource that can be extracted at a "
                     "profit with the technology we have now",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c10-04-e06",
        "band": "easier",
        "text": "Recycled aluminium takes about a twentieth of the energy of "
                "new metal from ore. Where does that saving come from?",
        "options": [
            {"text": "The oxygen has already been prised off once, so that "
                     "step does not have to be paid for again",
             "correct": True},
            {"text": "Recycled metal does not have to be melted, so the "
                     "furnace stage of making it is skipped altogether and "
                     "with it most of the energy that stage would use",
             "correct": False,
             "why": "Recycled aluminium IS melted. The twentieth that is "
                    "still spent is mostly the melting"},
            {"text": "Less transport is needed",
             "correct": False,
             "why": "Transport is a small part of the total. The electricity "
                    "for extraction is the large one"},
            {"text": "Recycled aluminium is a different metal",
             "correct": False,
             "why": "It is the same metal, atom for atom. That is why it can "
                    "be used again"},
        ],
        "figure": None,
    },
    {
        "id": "c10-04-e07",
        "band": "easier",
        "text": "Why does recycling slow extraction rather than ending it?",
        "options": [
            {"text": "Because not everybody puts their waste in the right "
                     "bin, so a proportion of what could be recycled is "
                     "thrown away with the ordinary rubbish instead",
             "correct": False,
             "why": "Collection matters and even perfect collection leaks. "
                    "The losses are in the process"},
            {"text": "Because every loop loses some material",
             "correct": True},
            {"text": "Because recycled material is always worse than new",
             "correct": False,
             "why": "Aluminium comes back as good as new. Some materials "
                    "degrade and not all"},
            {"text": "Because recycling uses more energy than extraction",
             "correct": False,
             "why": "It uses far less for most materials. The problem is that "
                    "material is lost each pass"},
        ],
        "figure": None,
    },
    {
        "id": "c10-04-e08",
        "band": "easier",
        "text": "Which of these is NOT a finite resource?",
        "options": [
            {"text": "Copper ore",
             "correct": False,
             "why": "It formed over millions of years and is not being "
                    "replaced. Finite"},
            {"text": "Crude oil",
             "correct": False,
             "why": "Made from buried remains over millions of years, and "
                    "extracted in centuries"},
            {"text": "Sunlight",
             "correct": True},
            {"text": "Phosphate rock, which is spread on fields as fertiliser "
                     "and is replaced by the weathering of the rocks "
                     "underneath them at about the rate it is used",
             "correct": False,
             "why": "Weathering releases phosphorus far too slowly to matter. "
                    "Phosphate rock is one of the sharpest finite problems "
                    "there is"},
        ],
        "figure": None,
    },

    # ── standard · MRB-335 top-up ───────────────────────────────────────
    {
        "id": "c10-04-s05",
        "band": "standard",
        "text": "Why is a crisp packet close to unrecyclable, when both the "
                "materials in it can be recycled on their own?",
        "options": [
            {"text": "The packet is contaminated with food",
             "correct": False,
             "why": "Washing deals with that. The lamination is what defeats "
                    "the process"},
            {"text": "Nobody collects them",
             "correct": False,
             "why": "The bench collected nine in ten and almost nothing came "
                    "back. Collection was not the problem"},
            {"text": "The aluminium layer is only a few microns thick, so "
                     "there is too little of it in any one packet to be worth "
                     "the trouble of recovering it at all",
             "correct": False,
             "why": "Thin layers are recovered in bulk elsewhere. The "
                    "obstacle is that the two are bonded together"},
            {"text": "No process separates the plastic film from the "
                     "aluminium layer economically",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c10-04-s06",
        "band": "standard",
        "text": "The lesson calls the crisp packet a real trade-off rather "
                "than a mistake. Why?",
        "options": [
            {"text": "Because the property that makes it useful — keeping "
                     "food fresh with very little material — is the same one "
                     "that makes it hard to recover",
             "correct": True},
            {"text": "Because nobody knew when it was designed that "
                     "laminated materials would be difficult to recycle, and "
                     "by the time anybody realised it was too late to change "
                     "the design",
             "correct": False,
             "why": "The difficulty follows from the design working. It is "
                    "not an oversight that could simply have been avoided"},
            {"text": "Because the packet is cheap",
             "correct": False,
             "why": "Cost is not the trade-off being described. Performance "
                    "against recoverability is"},
            {"text": "Because crisps would go stale otherwise",
             "correct": False,
             "why": "That is one half of the trade-off. The other half is "
                    "what it costs at the end of the packet's life"},
        ],
        "figure": None,
    },
    {
        "id": "c10-04-s07",
        "band": "standard",
        "text": "A recycled bottle becomes a fleece. Which word describes "
                "that, and why does it matter?",
        "options": [
            {"text": "Recycling, and it matters because it shows that "
                     "plastic can go round indefinitely as long as somebody "
                     "is willing to find a use for what comes back each time",
             "correct": False,
             "why": "It goes round ONCE and then stops. That is what makes it "
                    "downcycling rather than a loop"},
            {"text": "Downcycling, and it matters because the fleece cannot "
                     "become a bottle or another fleece",
             "correct": True},
            {"text": "Reusing, and it matters because nothing was melted",
             "correct": False,
             "why": "The bottle was melted and reprocessed. Reusing would "
                    "mean refilling it"},
            {"text": "Downcycling, and it does not matter much",
             "correct": False,
             "why": "It matters a great deal — the loop ends there, and new "
                     "plastic is still needed for the next bottle"},
        ],
        "figure": None,
    },
    {
        "id": "c10-04-s08",
        "band": "standard",
        "text": "Why do published figures for how many years of a metal are "
                "left keep changing?",
        "options": [
            {"text": "Because the estimates were wrong to begin with",
             "correct": False,
             "why": "They were right for the conditions of their day. The "
                    "conditions changed"},
            {"text": "Because new deposits are found all the time, and each "
                     "one adds to the total amount of the metal that is known "
                     "to exist in the crust",
             "correct": False,
             "why": "New finds happen and are not the main reason. The line "
                    "between worthless rock and ore keeps moving"},
            {"text": "Because a reserve depends on price and technology, so "
                     "rock that was worthless can become worth digging",
             "correct": True},
            {"text": "Because more of the metal forms underground each year",
             "correct": False,
             "why": "Ore takes millions of years to form. Nothing is being "
                    "topped up"},
        ],
        "figure": None,
    },

    # ── harder · MRB-335 top-up ─────────────────────────────────────────
    {
        "id": "c10-04-h05",
        "band": "harder",
        "text": "The lesson says a limit shows up as rising ENERGY COST long "
                "before anything physically runs out. Why?",
        "options": [
            {"text": "Because mining companies raise prices as stocks fall",
             "correct": False,
             "why": "Prices do rise, and the underlying cause is the physical "
                    "one: poorer ore takes more energy"},
            {"text": "Because energy itself is running out",
             "correct": False,
             "why": "The point is about the ore rather than about the energy "
                    "supply"},
            {"text": "Because the price of energy rises as a resource becomes "
                     "scarcer, so the cost of extraction goes up even when "
                     "the ore itself is no harder to dig than before",
             "correct": False,
             "why": "The ore genuinely does get harder. It is the "
                    "concentration that falls, not just the price"},
            {"text": "Because the cheap concentrated ore is used first, and "
                     "everything after it takes more energy to extract",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c10-04-h06",
        "band": "harder",
        "text": "Two materials are collected at the same rate and one "
                "recycles far better. What must differ?",
        "options": [
            {"text": "How much of what is collected survives the process "
                     "fit to be used again",
             "correct": True},
            {"text": "How carefully the two of them are sorted before they "
                     "reach the plant, since a stream with less contamination "
                     "in it always comes back in better condition",
             "correct": False,
             "why": "Collection was held equal, and sorting is part of "
                    "collection. The difference is in what the process can "
                    "recover"},
            {"text": "How much each is worth per tonne",
             "correct": False,
             "why": "Value decides whether anyone bothers. It does not decide "
                    "how much survives"},
            {"text": "How heavy each one is",
             "correct": False,
             "why": "Mass was compared equally on the bench and the gap was "
                    "still enormous"},
        ],
        "figure": None,
    },
    {
        "id": "c10-04-h07",
        "band": "harder",
        "text": "A phone holds about thirty elements in layers a few atoms "
                "thick. What would designers have to change for it to recycle "
                "well?",
        "options": [
            {"text": "Use more of each element, so that there is enough of "
                     "every one of them in a single phone to be worth "
                     "recovering when it reaches the end of its life",
             "correct": False,
             "why": "That would make a heavier phone using more material. The "
                    "problem is that they cannot be separated"},
            {"text": "Design for disassembly — fewer materials, and parts "
                     "that come apart",
             "correct": True},
            {"text": "Collect more phones",
             "correct": False,
             "why": "Collection is the easy half. What defeats it is the "
                    "bonding"},
            {"text": "Make phones last longer",
             "correct": False,
             "why": "A genuinely good idea, and it reduces demand rather than "
                    "making a phone recyclable"},
        ],
        "figure": None,
    },
    {
        "id": "c10-04-h08",
        "band": "harder",
        "text": "Suppose a material could be recycled perfectly, with no "
                "losses at all. Would extraction stop?",
        "options": [
            {"text": "Yes, provided everybody recycled everything",
             "correct": False,
             "why": "Perfect recycling is what the question already assumes. "
                    "Growth in what is in use is the remaining gap"},
            {"text": "Yes — with no losses the same material would go round "
                     "for ever, so nothing new would ever have to be taken "
                     "out of the ground again",
             "correct": False,
             "why": "It would go round for ever and there would still be more "
                    "of it in use each year than the year before"},
            {"text": "No — recycling only returns what is thrown away, and "
                     "anything still in use is not available to return",
             "correct": True},
            {"text": "No, because perfect recycling is impossible",
             "correct": False,
             "why": "That refuses the question rather than answering it. The "
                    "interesting point holds even if it were possible"},
        ],
        "figure": None,
    },

    # ── easier · MRB-338 night-3 top-up ──────────────────────────────────
    {
        "id": "c10-04-e09",
        "band": "easier",
        "text": "When recycling is described using a 'recovery' figure, what "
                "does that figure measure?",
        "options": [
            {"text": "The fraction of the material collected that comes "
                     "back usable at the same grade",
             "correct": True},
            {"text": "The total mass of the material collected from bins "
                     "each year",
             "correct": False,
             "why": "That is about collection, not about what happens once "
                    "the material reaches the plant."},
            {"text": "How much cheaper the recycled material is compared "
                     "with new material",
             "correct": False,
             "why": "Price is not what is being measured. It is what "
                    "fraction survives the process."},
            {"text": "How many times a material can be melted before it is "
                     "thrown away",
             "correct": False,
             "why": "That is closer to a lifetime count than to the "
                    "recovery figure itself, which is the fraction per "
                    "pass."},
        ],
        "figure": None,
    },
    {
        "id": "c10-04-e10",
        "band": "easier",
        "text": "Bauxite is the ore aluminium is extracted from. What is it "
                "mainly smelted into?",
        "options": [
            {"text": "Steel, since bauxite is rich in iron as well as "
                     "aluminium",
             "correct": False,
             "why": "Bauxite is the aluminium ore. Iron comes from iron "
                    "ore, a different rock entirely."},
            {"text": "Aluminium metal, used in cans, window frames and "
                     "aircraft",
             "correct": True},
            {"text": "Cement, because bauxite is a type of limestone used "
                     "in construction",
             "correct": False,
             "why": "Bauxite is not limestone. It is the rock aluminium is "
                    "extracted from."},
            {"text": "Glass, because bauxite contains the silica glass is "
                     "made from",
             "correct": False,
             "why": "Glass is made from sand, not from bauxite. Bauxite is "
                    "the source of aluminium."},
        ],
        "figure": None,
    },
    {
        "id": "c10-04-e11",
        "band": "easier",
        "text": "Bauxite's limit is best described as an ENERGY limit "
                "rather than a limit on the amount in the ground. Why?",
        "options": [
            {"text": "There is very little bauxite left to mine",
             "correct": False,
             "why": "There is plenty in the ground for now. The limit is "
                    "not about running low on rock."},
            {"text": "Aluminium is so light that moving the bauxite from "
                     "the mine to the smelter uses most of the energy",
             "correct": False,
             "why": "Transport is a small part of the total. Almost all "
                    "of the energy goes into separating the metal from "
                    "the ore."},
            {"text": "Extracting aluminium from it is one of the most "
                     "energy-hungry industrial processes there is",
             "correct": True},
            {"text": "Bauxite only forms in a small number of countries",
             "correct": False,
             "why": "That describes phosphate rock's problem. Bauxite's "
                    "stated limit is energy."},
        ],
        "figure": None,
    },
    {
        "id": "c10-04-e12",
        "band": "easier",
        "text": "Iron ore is described as the most abundant of the useful "
                "ores. What is it mainly used to make?",
        "options": [
            {"text": "Aluminium",
             "correct": False,
             "why": "Aluminium comes from bauxite. Iron ore makes a "
                    "different metal."},
            {"text": "Fertiliser",
             "correct": False,
             "why": "Fertiliser comes from phosphate rock. Iron ore is a "
                    "metal ore."},
            {"text": "Plastic, made from polymers refined out of crude oil",
             "correct": False,
             "why": "Plastic is made from crude oil. Iron ore contains no "
                    "carbon compounds usable that way."},
            {"text": "Steel, used in buildings, cars, ships, tools and "
                     "tins",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c10-04-e13",
        "band": "easier",
        "text": "Which kind of limit best describes iron ore's resource "
                "problem?",
        "options": [
            {"text": "Grade — high-grade deposits are used first, so what "
                     "remains needs more digging and energy per tonne",
             "correct": True},
            {"text": "No substitute — nothing else can do the job iron "
                     "does",
             "correct": False,
             "why": "That describes phosphate rock. Iron has substitutes "
                    "for many of its uses."},
            {"text": "Leaves the planet — once used, it escapes into space",
             "correct": False,
             "why": "That is helium's limit. Iron stays on Earth however "
                    "it is used."},
            {"text": "Burnt out of the loop — once it has been burned, its carbon "
                     "can never again be recovered and turned back into "
                     "oil",
             "correct": False,
             "why": "That is crude oil's limit as a fuel. Iron is not "
                    "burned or destroyed by use."},
        ],
        "figure": None,
    },
    {
        "id": "c10-04-e14",
        "band": "easier",
        "text": "Besides being burned as fuel, what is crude oil mainly "
                "used for?",
        "options": [
            {"text": "Making the steel used in tools and vehicles",
             "correct": False,
             "why": "Steel comes from iron ore. Crude oil is not used to "
                    "make metal."},
            {"text": "The feedstock for plastics, dyes, solvents and "
                     "synthetic fibres",
             "correct": True},
            {"text": "Fertiliser for growing crops",
             "correct": False,
             "why": "Fertiliser comes from phosphate rock. Crude oil has "
                    "no role in it."},
            {"text": "Cooling powerful magnets in scientific equipment",
             "correct": False,
             "why": "That is helium's job. Crude oil cannot stay liquid at "
                    "the temperatures that needs."},
        ],
        "figure": None,
    },
    {
        "id": "c10-04-e15",
        "band": "easier",
        "text": "Which kind of limit best describes crude oil, once it has "
                "been burned as fuel?",
        "options": [
            {"text": "Grade — the remaining oil is always of a lower "
                     "quality",
             "correct": False,
             "why": "That describes iron ore. Oil's limit as a fuel is "
                    "about where the carbon ends up."},
            {"text": "No substitute — other fuels genuinely exist that could "
                     "replace crude oil for many purposes and needs",
             "correct": False,
             "why": "Other fuels exist. The stated limit for burnt oil is "
                    "that the carbon leaves the loop."},
            {"text": "Burnt out of the loop — the carbon is released into "
                     "the air and cannot be recovered as oil again",
             "correct": True},
            {"text": "Leaves the planet — the carbon dioxide released does "
                     "eventually settle back into rocks and oceans given "
                     "enough time to pass",
             "correct": False,
             "why": "The carbon stays in Earth's air and oceans. Leaving "
                    "the planet describes helium, not carbon."},
        ],
        "figure": None,
    },
    {
        "id": "c10-04-e16",
        "band": "easier",
        "text": "What is phosphate rock mainly used for?",
        "options": [
            {"text": "Making steel noticeably stronger and much more durable",
             "correct": False,
             "why": "Steel-strengthening additives come from other "
                    "sources. Phosphate rock's use is elsewhere."},
            {"text": "Cooling equipment",
             "correct": False,
             "why": "That is helium's use. Phosphate rock is not used for "
                    "cooling anything."},
            {"text": "Making plastic used in packaging and construction",
             "correct": False,
             "why": "Plastic is made from crude oil. Phosphate rock has a "
                    "different, single major use."},
            {"text": "Fertiliser, since crops cannot be grown without "
                     "phosphorus",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c10-04-e17",
        "band": "easier",
        "text": "Why is phosphate rock's limit best described as 'no "
                "substitute', rather than a grade or energy limit?",
        "options": [
            {"text": "Because phosphorus is one of the few elements crops "
                     "cannot be grown without, and nothing else can do "
                     "its job",
             "correct": True},
            {"text": "Because there is very little phosphate rock anywhere "
                     "in the world",
             "correct": False,
             "why": "Scarcity is not the stated reason. The reason given "
                    "is that nothing else can replace it."},
            {"text": "Because phosphate rock needs more energy to mine and "
                     "process than any other resource taken out of the "
                     "ground anywhere",
             "correct": False,
             "why": "Energy is bauxite's stated limit, not phosphate's. "
                    "Phosphate's is having no substitute."},
            {"text": "Because phosphate rock cannot be turned into fertiliser "
                     "without expensive machinery that most farming "
                     "regions cannot afford",
             "correct": False,
             "why": "Cost of processing is not the reason given. It is "
                    "that crops need phosphorus and nothing replaces it."},
        ],
        "figure": None,
    },
    {
        "id": "c10-04-e18",
        "band": "easier",
        "text": "Besides cooling the magnets in MRI scanners, what is "
                "helium used for?",
        "options": [
            {"text": "Making fertiliser",
             "correct": False,
             "why": "Fertiliser needs phosphorus, not helium. Helium has "
                    "no role in it."},
            {"text": "Welding and leak detection",
             "correct": True},
            {"text": "Smelting aluminium from bauxite",
             "correct": False,
             "why": "Smelting aluminium uses huge amounts of electricity, "
                    "not helium."},
            {"text": "Strengthening steel",
             "correct": False,
             "why": "Steel strength comes from its own alloying elements, "
                    "not from helium."},
        ],
        "figure": None,
    },
    {
        "id": "c10-04-e19",
        "band": "easier",
        "text": "Which kind of limit uniquely describes helium, unlike any "
                "metal ore?",
        "options": [
            {"text": "Grade — a description that would fit iron ore's situation "
                     "far better, where digging simply gets harder over "
                     "time",
             "correct": False,
             "why": "That describes iron ore. Helium's stated limit is "
                    "different."},
            {"text": "No substitute — nothing else is used to cool the magnets in "
                     "hospital scanning equipment either",
             "correct": False,
             "why": "That is close to true of its USE, but the stated "
                    "LIMIT for helium is about where it goes once "
                    "released."},
            {"text": "Leaves the planet — once released into the air, it "
                     "rises away into space for good",
             "correct": True},
            {"text": "Burnt out of the loop — helium does not react with anything "
                     "at all, so nothing chemically destroys it when it "
                     "is used",
             "correct": False,
             "why": "Helium reacts with nothing. It is not destroyed; it "
                    "simply leaves the atmosphere."},
        ],
        "figure": None,
    },
    {
        "id": "c10-04-e20",
        "band": "easier",
        "text": "Recycled crisp-packet film needs about 90 MJ/kg to "
                "process, and brand-new film needs about 90 MJ/kg too. "
                "What does that show?",
        "options": [
            {"text": "That recycling film is impossible, whatever the "
                     "collection rate",
             "correct": False,
             "why": "Impossible is too strong — the figure is about "
                    "energy cost, not about whether a process exists."},
            {"text": "That crisp packets should never have been invented",
             "correct": False,
             "why": "The packet is treated as an engineering trade-off, "
                    "not as a mistake to regret."},
            {"text": "That collecting crisp packets more carefully would "
                     "fix the energy problem",
             "correct": False,
             "why": "Collection changes how much comes back, not how much "
                    "energy each kilogram costs to process."},
            {"text": "That even if the film could be recycled, doing so "
                     "would save no energy at all",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c10-04-e21",
        "band": "easier",
        "text": "About what fraction of collected glass bottles comes back "
                "usable at full grade?",
        "options": [
            {"text": "About 90%",
             "correct": True},
            {"text": "About 50%",
             "correct": False,
             "why": "That is PET's recovery figure. Glass comes back at a "
                    "much higher fraction."},
            {"text": "About 2%",
             "correct": False,
             "why": "That is crisp-packet film's figure — the worst of "
                    "the five. Glass recovers far better."},
            {"text": "About 21%",
             "correct": False,
             "why": "That number belongs to oxygen's share of the air, a "
                    "different lesson's fact entirely."},
        ],
        "figure": None,
    },
    {
        "id": "c10-04-e22",
        "band": "easier",
        "text": "About what fraction of collected steel cans comes back "
                "usable at the same grade?",
        "options": [
            {"text": "About 50%",
             "correct": False,
             "why": "That is PET's figure. Steel recovers at a much "
                    "higher rate than that."},
            {"text": "About 92%",
             "correct": True},
            {"text": "About 2%",
             "correct": False,
             "why": "That is crisp-packet film's figure. Steel is one of "
                    "the better recyclers of the five."},
            {"text": "About 78%",
             "correct": False,
             "why": "That number is nitrogen's share of the air. Steel's "
                    "recovery figure is higher than that."},
        ],
        "figure": None,
    },
    {
        "id": "c10-04-e23",
        "band": "easier",
        "text": "About half of collected PET bottles come back usable. What "
                "happens to the OTHER half?",
        "options": [
            {"text": "It is exported abroad in large shipments and reprocessed "
                     "there into fresh bottles for local sale the "
                     "following year",
             "correct": False,
             "why": "It has already been through the process once. There "
                    "is no second attempt on the same material."},
            {"text": "It is instead reprocessed into insulation material for buildings rather than being burned for electricity generation",
             "correct": False,
             "why": "It does not become fuel. It comes back too degraded "
                    "to be a bottle."},
            {"text": "It comes back too degraded to be made into a "
                     "bottle, so it is only fit for something less "
                     "demanding",
             "correct": True},
            {"text": "It is exported to another country for processing",
             "correct": False,
             "why": "Location is not the issue. The material itself is "
                    "degraded by the melting process."},
        ],
        "figure": None,
    },
    {
        "id": "c10-04-e24",
        "band": "easier",
        "text": "Which of the five materials combines a high recovery "
                "figure with a large energy saving when it is recycled?",
        "options": [
            {"text": "PET, since half of what is collected comes back "
                     "usable",
             "correct": False,
             "why": "Its energy saving when recycled is large, and its "
                    "recovery figure of 50% is one of the weaker ones."},
            {"text": "Glass, since it can be remelted without limit and "
                     "never comes back degraded",
             "correct": False,
             "why": "Its recovery is high, and the melting itself costs "
                    "almost as much energy either way — the saving is "
                    "only about 27%."},
            {"text": "Aluminium, since almost all of it comes back usable "
                     "and the energy saved is enormous",
             "correct": True},
            {"text": "Crisp-packet film, since it is collected at a very "
                     "high rate",
             "correct": False,
             "why": "Collection rate is not recovery. Film's recovery is "
                    "only 2%, and recycling it saves no energy at all."},
        ],
        "figure": None,
    },
    {
        "id": "c10-04-e25",
        "band": "easier",
        "text": "Phosphorus can, in principle, be recovered from sewage "
                "and manure, and this is starting to happen. What does "
                "'starting to happen' signal here?",
        "options": [
            {"text": "That the recovery is under way but is not yet the "
                     "normal way phosphorus is supplied",
             "correct": True},
            {"text": "That it is a purely theoretical idea nobody has "
                     "ever tried",
             "correct": False,
             "why": "Starting to happen is stronger than a theory nobody "
                    "has tried."},
            {"text": "That it is already how most of the world's "
                     "phosphorus is supplied",
             "correct": False,
             "why": "It is described as starting to happen, not as the "
                    "established main source yet."},
            {"text": "That scientists disagree among themselves about whether "
                     "recovering phosphorus from sewage is possible at "
                     "all",
             "correct": False,
             "why": "There is no disagreement recorded here about "
                    "whether it is possible — only about how much is "
                    "done."},
        ],
        "figure": None,
    },
    {
        "id": "c10-04-e26",
        "band": "easier",
        "text": "Plastics made from crude oil CAN be recycled. What limits "
                "how many times?",
        "options": [
            {"text": "Nothing — plastic from oil can be recycled "
                     "indefinitely, exactly like a metal",
             "correct": False,
             "why": "Only a few passes are possible before the polymer is "
                    "too degraded — unlike a metal."},
            {"text": "The polymer becomes too degraded after only a few "
                     "times through the process",
             "correct": True},
            {"text": "A law only permits plastic to be recycled once",
             "correct": False,
             "why": "No such rule is described. The limit given is a "
                    "property of the material, not of regulation."},
            {"text": "Crude-oil plastics cannot be recycled at all, even "
                     "once",
             "correct": False,
             "why": "They can be recycled, just not many times before "
                    "degrading too far."},
        ],
        "figure": None,
    },
    {
        "id": "c10-04-e27",
        "band": "easier",
        "text": "How does a good MRI installation stop its helium from "
                "being lost for good?",
        "options": [
            {"text": "By using less helium overall",
             "correct": False,
             "why": "Using less helps the budget, and it is not the fix "
                    "described. Capturing it is."},
            {"text": "By recycling the helium after it has escaped into "
                     "the room",
             "correct": False,
             "why": "Once helium is in open air it is gone. The fix has "
                    "to happen before it escapes."},
            {"text": "By capturing the helium before it can escape into "
                     "the air",
             "correct": True},
            {"text": "By replacing helium with a cheaper gas that does "
                     "the same job",
             "correct": False,
             "why": "Nothing else stays liquid at the temperature the "
                    "magnets need. Substitution is not the fix described."},
        ],
        "figure": None,
    },
    {
        "id": "c10-04-e28",
        "band": "easier",
        "text": "Why is a large share of new steel already made from "
                "scrap, rather than from fresh iron ore?",
        "options": [
            {"text": "Because scrap steel is cheaper to buy than iron ore",
             "correct": False,
             "why": "Price may follow from it, and the reason given is "
                    "physical: steel sorts itself out easily."},
            {"text": "Because there is very little iron ore left to mine",
             "correct": False,
             "why": "Iron ore is described as abundant. Scarcity is not "
                    "the reason scrap is used so much."},
            {"text": "Because steel gradually loses its strength if it is not "
                     "recycled on a sufficiently regular basis",
             "correct": False,
             "why": "Nothing says unused steel weakens. The reason given "
                    "is how easily it is collected."},
            {"text": "Because steel is magnetic, so it sorts itself out "
                     "of mixed waste easily",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c10-04-e29",
        "band": "easier",
        "text": "Recycled aluminium comes back 'as good as new'. What does "
                "that mean about its quality, compared with brand-new "
                "aluminium from ore?",
        "options": [
            {"text": "It is the same metal, with no loss of quality, so "
                     "it can do exactly the same jobs again",
             "correct": True},
            {"text": "It is slightly weaker than freshly made metal, so it can "
                     "only be used again for noticeably less demanding "
                     "jobs than before",
             "correct": False,
             "why": "That describes downcycling, which is PET's problem. "
                    "Aluminium does not degrade this way."},
            {"text": "It is a different, cheaper grade of aluminium sold "
                     "separately from the metal freshly extracted from "
                     "ore",
             "correct": False,
             "why": "It is the identical metal, atom for atom, not a "
                    "separate cheaper grade."},
            {"text": "It is only usable one further time before it must finally be "
                     "thrown away for good, unlike glass or steel",
             "correct": False,
             "why": "Aluminium can be melted and recast again and again "
                    "without losing quality."},
        ],
        "figure": None,
    },
    {
        "id": "c10-04-e30",
        "band": "easier",
        "text": "How does the lesson define 'recycling'?",
        "options": [
            {"text": "Reducing how much of a material is bought in the "
                     "first place",
             "correct": False,
             "why": "That is reduce, a separate idea that comes before "
                    "recycling in the lesson's order."},
            {"text": "Collecting a used material and processing it so it "
                     "can be made into something again",
             "correct": True},
            {"text": "Using an item for as long as possible before "
                     "replacing it",
             "correct": False,
             "why": "That is reuse. Recycling is about processing a "
                    "material again, not about keeping using the same "
                    "item."},
            {"text": "Digging a fresh supply of ore or oil out of the "
                     "ground",
             "correct": False,
             "why": "That is extraction, the opposite of recycling — "
                    "recycling avoids fresh extraction."},
        ],
        "figure": None,
    },

    # ── standard · MRB-338 night-3 top-up ────────────────────────────────
    {
        "id": "c10-04-s09",
        "band": "standard",
        "text": "A tonne of steel cans is collected and 92% of it comes "
                "back usable at the same grade. How many kilograms still "
                "have to come from fresh iron ore to replace what did "
                "not?",
        "options": [
            {"text": "80 kg",
             "correct": True},
            {"text": "92 kg",
             "correct": False,
             "why": "That is how many kilograms DID come back, not the "
                    "shortfall from a tonne."},
            {"text": "920 kg",
             "correct": False,
             "why": "That is how much came back usable. The shortfall is "
                    "the rest of the tonne, not that amount."},
            {"text": "8 kg",
             "correct": False,
             "why": "That treats 92% as if it were 9.2%, rather than "
                    "finding the 8% that failed to come back."},
        ],
        "figure": None,
    },
    {
        "id": "c10-04-s10",
        "band": "standard",
        "text": "A tonne of PET is collected at a rate where only half of "
                "what is put out is collected, and 50% of what is "
                "collected comes back usable. What fraction of the "
                "original tonne returns as usable PET after this one "
                "pass?",
        "options": [
            {"text": "A half",
             "correct": False,
             "why": "That is the collection rate alone. Recovery then "
                    "halves it again."},
            {"text": "A quarter",
             "correct": True},
            {"text": "All of it",
             "correct": False,
             "why": "Two separate 50% losses cannot add up to the whole "
                    "tonne returning."},
            {"text": "None of it",
             "correct": False,
             "why": "Some material genuinely returns — half of half is a "
                    "quarter, not nothing."},
        ],
        "figure": None,
    },
    {
        "id": "c10-04-s11",
        "band": "standard",
        "text": "Aluminium is collected at only one in four, the lowest "
                "rate above zero, but its recovery is still 95%. Roughly "
                "what fraction of the ORIGINAL tonne comes back usable "
                "after one pass?",
        "options": [
            {"text": "Almost all of it",
             "correct": False,
             "why": "The low collection rate limits this heavily, "
                    "whatever the recovery figure is."},
            {"text": "About a half",
             "correct": False,
             "why": "One in four collected is a quarter to start with, "
                    "before recovery is even applied."},
            {"text": "Nearly a quarter",
             "correct": True},
            {"text": "Almost none of it",
             "correct": False,
             "why": "A quarter collected at 95% recovery is close to a "
                    "quarter returning, not close to nothing."},
        ],
        "figure": None,
    },
    {
        "id": "c10-04-s12",
        "band": "standard",
        "text": "Glass and crisp-packet film both fail to save much "
                "energy when recycled, glass at 27% and film at 0%. What "
                "is different about WHY each one fails?",
        "options": [
            {"text": "Both fail for the same reason: neither material "
                     "can be collected in large enough quantities",
             "correct": False,
             "why": "Collection is not the stated reason for either. Both "
                    "failures are about what happens once the material is "
                    "collected."},
            {"text": "Glass fails because it always degrades quite badly on "
                     "melting every single time; film fails because "
                     "its two layers cannot ever be separated at "
                     "all",
             "correct": False,
             "why": "Degrading is PET's problem, not glass's. Glass comes "
                    "back at full grade — the melting itself is the "
                    "energy cost."},
            {"text": "Glass fails because there is not enough sand left "
                     "in the ground to keep making it; film fails because "
                     "sorting it costs more than the material is worth",
             "correct": False,
             "why": "Neither reason is given. Both failures are about "
                    "energy and separation, not scarcity or sorting cost."},
            {"text": "Glass still has to be fully melted either way, so "
                     "the saving is small; film's separation problem "
                     "means it barely comes back at all",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c10-04-s13",
        "band": "standard",
        "text": "Steel is magnetic and sorts itself out of mixed waste "
                "easily, yet a build-up of other metals over repeated "
                "recycling limits what the recovered steel can be used "
                "for. What does that show about recycling steel?",
        "options": [
            {"text": "Easy collection and a lasting change in quality are "
                     "two separate things, and steel has one without the "
                     "other",
             "correct": True},
            {"text": "Steel cannot really be recycled at all, despite what the "
                     "collection and recovery figures given here clearly "
                     "show",
             "correct": False,
             "why": "Steel does recycle well and at high volume. The "
                    "build-up limits some future uses; it does not stop "
                    "recycling."},
            {"text": "The magnetic sorting removes the other metals as "
                     "well as the steel",
             "correct": False,
             "why": "Magnetism sorts steel FROM other waste. It does "
                    "nothing to remove metals already mixed within the "
                    "steel itself."},
            {"text": "Recycled steel becomes completely unusable after a "
                     "few passes",
             "correct": False,
             "why": "It remains usable — for a narrower range of jobs, "
                    "not for none at all."},
        ],
        "figure": None,
    },
    {
        "id": "c10-04-s14",
        "band": "standard",
        "text": "Crude oil turned into a plastic bag keeps its carbon out "
                "of the air for years before landfill. The same crude oil "
                "burned as fuel releases its carbon within moments. What "
                "does the comparison show about the two uses?",
        "options": [
            {"text": "Burning it and making plastic from it release exactly the "
                     "same amount of carbon dioxide into the air "
                     "immediately, without exception",
             "correct": False,
             "why": "The plastic route delays release for a long time. "
                    "Burning releases it straight away."},
            {"text": "Turning it into a durable product delays the "
                     "carbon reaching the air, while burning releases it "
                     "at once",
             "correct": True},
            {"text": "Making plastic from crude oil produces no carbon dioxide "
                     "of any kind at all, ever, under any "
                     "circumstances whatsoever",
             "correct": False,
             "why": "The bag's carbon still eventually reaches the air "
                    "once it is destroyed. It is delayed, not avoided "
                    "forever."},
            {"text": "Neither use has any effect on how much carbon is "
                     "in the air",
             "correct": False,
             "why": "Burning has an immediate effect, and even a delayed "
                    "release from a bag eventually matters."},
        ],
        "figure": None,
    },
    {
        "id": "c10-04-s15",
        "band": "standard",
        "text": "Recovering phosphorus from sewage is described as only "
                "starting to happen. Why might that matter more for "
                "phosphorus than an equivalent scheme would for a widely "
                "available metal?",
        "options": [
            {"text": "Because sewage plants are, in general, far cheaper to build "
                     "and run than any equivalent metal recycling plant "
                     "would be",
             "correct": False,
             "why": "Cost of the plant is not the reason given. The "
                    "reason concerns the resource having no substitute."},
            {"text": "Because phosphorus dissolves in water more easily "
                     "than metals do",
             "correct": False,
             "why": "Solubility is not the stated reason. The reason "
                    "concerns substitutes and where deposits are found."},
            {"text": "Because phosphorus has no substitute and its "
                     "remaining deposits are concentrated in a handful "
                     "of countries",
             "correct": True},
            {"text": "Because phosphorus is more valuable per tonne than "
                     "any metal",
             "correct": False,
             "why": "Value is not the reason given for why recovery "
                    "matters more here."},
        ],
        "figure": None,
    },
    {
        "id": "c10-04-s16",
        "band": "standard",
        "text": "An MRI installation recaptures helium before it can "
                "escape into the room. Why does capturing it BEFORE "
                "release matter more for helium than it would for a "
                "metal such as copper?",
        "options": [
            {"text": "Because helium is, in general, a great deal more expensive to "
                     "buy than copper or most other common industrial "
                     "metals",
             "correct": False,
             "why": "Cost is not the reason. The reason concerns what "
                    "happens once each substance is released."},
            {"text": "Because copper reacts readily with the air around it over "
                     "time, while helium famously reacts with nothing "
                     "at all",
             "correct": False,
             "why": "Helium is the unreactive one here. Reactivity is not "
                    "what makes the timing matter."},
            {"text": "Because helium is heavier than the other gases in "
                     "the room",
             "correct": False,
             "why": "Helium is much LIGHTER than air, which is why it "
                    "rises. Weight is not the point being made."},
            {"text": "Because once helium reaches open air it leaves the "
                     "atmosphere for good, while copper stays on Earth "
                     "however it is used",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c10-04-s17",
        "band": "standard",
        "text": "Crisp-packet film has both a very low recovery figure "
                "(2%) and no energy saving when recycled (90 MJ/kg either "
                "way). If a perfect separation method were invented "
                "tomorrow, which of the two problems would that solve?",
        "options": [
            {"text": "Only the recovery problem — separating the layers "
                     "still would not make recycling any cheaper in "
                     "energy",
             "correct": True},
            {"text": "Both problems would be solved at once, since separation is "
                     "the only thing standing in the way of recycling "
                     "this material properly",
             "correct": False,
             "why": "Recycled film costs the same energy as new film, "
                    "which separation alone would not change."},
            {"text": "Only the energy problem would be solved, since separation "
                     "has nothing whatsoever to do with how much "
                     "material is recovered",
             "correct": False,
             "why": "Separation is exactly what the 2% recovery figure is "
                    "limited by. It would raise recovery, not fix energy."},
            {"text": "Neither problem — the film would remain exactly as "
                     "bad as it is now",
             "correct": False,
             "why": "Recovery genuinely depends on separating the layers, "
                    "so a working separation method would raise it."},
        ],
        "figure": None,
    },
    {
        "id": "c10-04-s18",
        "band": "standard",
        "text": "Materials are ranked by how many lifetimes they give per "
                "kilogram of ore in the order aluminium, steel, glass, "
                "PET, crisp-packet film. What single figure, on its own, "
                "decides this order?",
        "options": [
            {"text": "The energy needed to make each material new",
             "correct": False,
             "why": "Energy figures do not follow this order — PET needs "
                    "more energy new than steel does. Recovery does."},
            {"text": "The recovery (yield) fraction of each material",
             "correct": True},
            {"text": "How heavy each material is",
             "correct": False,
             "why": "Mass is held equal for every material in this "
                    "comparison. Weight does not decide this ranking."},
            {"text": "How much each material is worth per tonne",
             "correct": False,
             "why": "Value is not tracked here at all. The ranking "
                    "follows how much survives the process."},
        ],
        "figure": None,
    },
    {
        "id": "c10-04-s19",
        "band": "standard",
        "text": "A tonne of glass is collected at nine in ten and 90% of "
                "what is collected comes back usable. What mass returns "
                "usable after this one pass?",
        "options": [
            {"text": "900 kg",
             "correct": False,
             "why": "That only applies the collection rate. Recovery then "
                    "reduces it further."},
            {"text": "1000 kg",
             "correct": False,
             "why": "Some material is genuinely lost at both the "
                    "collection and the recovery step, so the full tonne "
                    "cannot return."},
            {"text": "810 kg",
             "correct": True},
            {"text": "90 kg",
             "correct": False,
             "why": "That treats 90% as if only a tenth were being kept, "
                    "rather than nine tenths at each of two steps."},
        ],
        "figure": None,
    },
    {
        "id": "c10-04-s20",
        "band": "standard",
        "text": "For a material that recycles badly, one explanation is "
                "that not enough is collected, and another is that what "
                "comes back is too degraded to reuse. What is different "
                "about the material's problem in each case?",
        "options": [
            {"text": "The first explanation means the material cannot survive the "
                     "melting process at all; the second means simply "
                     "that not enough of it is ever gathered",
             "correct": False,
             "why": "That is the two explanations swapped round: the "
                    "first is about gathering, the second about "
                    "surviving."},
            {"text": "Both explanations put together describe exactly the same "
                     "single underlying problem with how the material "
                     "behaves",
             "correct": False,
             "why": "They describe two different problems: how much is "
                    "gathered, against how much survives once gathered."},
            {"text": "The first explanation means the material is somehow toxic "
                     "to handle; the second means it is simply too "
                     "heavy to transport economically",
             "correct": False,
             "why": "Neither explanation is about toxicity or weight. "
                    "Both concern collection versus survival of the "
                    "process."},
            {"text": "The first means the material would recycle well if "
                     "more were gathered; the second means it fails even "
                     "when gathered",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c10-04-s21",
        "band": "standard",
        "text": "If NONE of a material is ever collected, what happens "
                "over repeated use, whatever the material's own recovery "
                "figure is?",
        "options": [
            {"text": "Nothing comes back at all; every kilogram used is "
                     "used once and gone",
             "correct": True},
            {"text": "The material still returns at its usual recovery "
                     "rate",
             "correct": False,
             "why": "With nothing collected, recovery gets no chance to "
                    "act on anything."},
            {"text": "The result depends entirely on the recovery figure, "
                     "ignoring collection",
             "correct": False,
             "why": "With zero collected, the recovery figure makes no "
                    "difference — there is nothing for it to act on."},
            {"text": "Exactly half of it returns, whatever the material",
             "correct": False,
             "why": "Zero collection returns nothing at all, not half, "
                    "for any material."},
        ],
        "figure": None,
    },
    {
        "id": "c10-04-s22",
        "band": "standard",
        "text": "Helium released into a room and crude oil burned as fuel "
                "are both described as gone from the loop for good. What "
                "is different about WHERE each one ends up?",
        "options": [
            {"text": "Helium stays safely within Earth's air and oceans for good, "
                     "while the oil's carbon is the one that actually "
                     "leaves the planet entirely",
             "correct": False,
             "why": "That is the two swapped round. Helium is the one "
                    "that leaves the planet; carbon stays in Earth's air "
                    "and oceans."},
            {"text": "Helium leaves the atmosphere for space; the oil's "
                     "carbon stays within Earth's air, oceans and rocks",
             "correct": True},
            {"text": "Both substances end up in exactly the same place deep "
                     "underground, far beneath the Earth's crust and "
                     "mantle",
             "correct": False,
             "why": "Helium rises away from the planet. Carbon from "
                    "burning stays much closer to the surface."},
            {"text": "Neither substance actually leaves anywhere at all; both of "
                     "them simply and quietly change their chemical "
                     "form over time",
             "correct": False,
             "why": "Helium genuinely departs the atmosphere. The "
                    "comparison is about where each substance goes."},
        ],
        "figure": None,
    },
    {
        "id": "c10-04-s23",
        "band": "standard",
        "text": "Phosphate deposits worth digging are concentrated in a "
                "handful of countries, while iron ore is found much more "
                "widely. How does that make phosphate's resource problem "
                "different from iron's?",
        "options": [
            {"text": "Phosphate is, on the whole, considerably cheaper to mine per "
                     "tonne than most metal ores are, so the problem "
                     "matters comparatively less",
             "correct": False,
             "why": "Cost of mining is not the stated difference. The "
                    "difference concerns substitutes and concentration."},
            {"text": "Iron cannot really be substituted for its uses either, so in "
                     "that sense the two resource problems are actually "
                     "identical in every way",
             "correct": False,
             "why": "Iron has substitutes for many uses; phosphorus, for "
                    "crops, does not. That is the stated difference."},
            {"text": "Phosphate supply is more vulnerable, since it "
                     "relies on fewer sources and nothing else can do "
                     "phosphorus's job",
             "correct": True},
            {"text": "Phosphate is recycled at a much higher rate than "
                     "iron is",
             "correct": False,
             "why": "The opposite is closer to true — phosphate recovery "
                    "is only starting, while iron is recycled at scale."},
        ],
        "figure": None,
    },
    {
        "id": "c10-04-s24",
        "band": "standard",
        "text": "A material has a recovery of 0.5 and is collected at a "
                "rate of 0.5. What fraction of the ORIGINAL material is "
                "lost after just one pass through the loop?",
        "options": [
            {"text": "None of it",
             "correct": False,
             "why": "Two separate 50% steps cannot leave nothing lost — "
                    "a good deal is lost at each stage."},
            {"text": "A quarter",
             "correct": False,
             "why": "A quarter is what RETURNS (0.5 × 0.5), not what is "
                    "lost. The lost fraction is the rest."},
            {"text": "A half",
             "correct": False,
             "why": "That is only the collection step's loss. The "
                    "recovery step then loses more of what was collected."},
            {"text": "Three quarters",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c10-04-s25",
        "band": "standard",
        "text": "Even if the plastic and aluminium layers of a crisp "
                "packet could be separated perfectly, the recycled film "
                "would still need 90 MJ/kg — the same as brand-new film. "
                "What would that reveal, once separation is no longer "
                "the problem?",
        "options": [
            {"text": "That recycling the separated materials would cost "
                     "just as much energy as making them fresh, unlike "
                     "aluminium",
             "correct": True},
            {"text": "That the packet would then recycle exactly like "
                     "aluminium does",
             "correct": False,
             "why": "Recycled aluminium takes only about a twentieth of the "
                    "energy of new metal. Film would still save none at "
                    "all."},
            {"text": "That the packet was never really made of two "
                     "different materials, so there was nothing needing to "
                     "be separated from anything else in the first place",
             "correct": False,
             "why": "It genuinely is plastic laminated to metal. The "
                    "energy figures are a separate issue from composition."},
            {"text": "That the energy figures given must be a mistake",
             "correct": False,
             "why": "The figures are the given data. What they reveal is "
                    "a genuine limit distinct from the separation problem."},
        ],
        "figure": None,
    },
    {
        "id": "c10-04-s26",
        "band": "standard",
        "text": "Steel recycles well through magnetic sorting; crude oil "
                "used as fuel does not recycle at all. What does "
                "comparing the two show about how 'one-way' a use of a "
                "resource is?",
        "options": [
            {"text": "Both uses are equally one-way, since both "
                     "eventually run out",
             "correct": False,
             "why": "Running out eventually is true of any finite "
                    "resource. The comparison is about how much comes "
                    "back from each use."},
            {"text": "Some uses of a resource allow a large share to "
                     "come back round the loop, while others end the "
                     "loop completely",
             "correct": True},
            {"text": "Steel is more one-way than burnt oil, since steel "
                     "is a solid",
             "correct": False,
             "why": "That is the wrong way round — steel recycles at "
                    "high volume, while burnt oil's carbon does not "
                    "return as fuel at all."},
            {"text": "Neither use is really one-way, since both "
                     "materials still exist somewhere afterwards",
             "correct": False,
             "why": "Existing somewhere afterwards is not the same as "
                    "being available to use again as the same resource."},
        ],
        "figure": None,
    },
    {
        "id": "c10-04-s27",
        "band": "standard",
        "text": "A plastic bag made from crude oil is recycled twice and "
                "then landfilled because it is too degraded to process "
                "again. Does that make it a closed loop like aluminium?",
        "options": [
            {"text": "Yes — being recycled at all means the loop never "
                     "really ends",
             "correct": False,
             "why": "The loop DOES end once it reaches landfill. "
                    "Aluminium's loop keeps running; this one stops."},
            {"text": "Yes — two whole passes through the recycling process "
                     "counts as a genuinely closed loop, whatever "
                     "happens to it afterwards",
             "correct": False,
             "why": "A closed loop keeps running indefinitely. Stopping "
                    "after two passes is downcycling, not a closed loop."},
            {"text": "No — it is downcycling that ends after a couple of "
                     "passes, unlike aluminium's loop which keeps "
                     "running",
             "correct": True},
            {"text": "No — because plastic cannot be recycled even once",
             "correct": False,
             "why": "It genuinely was recycled twice here. The problem is "
                    "that the loop then ends, not that recycling never "
                    "happened."},
        ],
        "figure": None,
    },
    {
        "id": "c10-04-s28",
        "band": "standard",
        "text": "Aluminium collected at nine in ten gives about seven "
                "lifetimes per kilogram of ore. If collection instead "
                "drops to one in four, roughly how many lifetimes does "
                "it give?",
        "options": [
            {"text": "About seven, since recovery decides it and that "
                     "has not changed",
             "correct": False,
             "why": "Collection rate matters too, and it has dropped "
                    "sharply, bringing the figure down a great deal."},
            {"text": "About five",
             "correct": False,
             "why": "That overstates how much a lower collection rate "
                    "can still deliver once collection drops this far."},
            {"text": "Nothing at all — a low collection rate means no "
                     "material comes back",
             "correct": False,
             "why": "Some material still comes back at one in four "
                    "collected. It is a smaller figure, not zero."},
            {"text": "About one and a third",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c10-04-s29",
        "band": "standard",
        "text": "A council doubles how many aluminium cans it collects, "
                "going from one in four to a half. Does the RECOVERY "
                "figure for aluminium change as a result?",
        "options": [
            {"text": "Yes — recovery rises quite sharply because handling more "
                     "material at once always leads to better "
                     "sorting overall",
             "correct": False,
             "why": "Recovery is a fixed property of how well the melted "
                    "metal survives, not something that shifts with the "
                    "amount gathered."},
            {"text": "No — recovery stays at 95% either way; only the "
                     "amount actually going round the loop changes",
             "correct": True},
            {"text": "Yes — recovery falls noticeably because a much bigger "
                     "batch is always harder to process safely",
             "correct": False,
             "why": "Recovery does not depend on batch size here. It is "
                    "per kilogram, whatever the amount."},
            {"text": "No — but the overall multiplier stays exactly the "
                     "same too",
             "correct": False,
             "why": "The multiplier DOES change, because it depends on "
                    "the collection rate as well as on recovery."},
        ],
        "figure": None,
    },
    {
        "id": "c10-04-s30",
        "band": "standard",
        "text": "Glass is collected at only one in four and recovers at "
                "90%. What fraction of the original mass returns usable "
                "after this one pass?",
        "options": [
            {"text": "90%",
             "correct": False,
             "why": "That is the recovery figure alone. The lower "
                    "collection rate reduces it further."},
            {"text": "A half",
             "correct": False,
             "why": "That would be the result at a collection rate of a "
                    "half, not at one in four."},
            {"text": "22.5%",
             "correct": True},
            {"text": "2%",
             "correct": False,
             "why": "That is crisp-packet film's recovery figure, a "
                    "different material entirely."},
        ],
        "figure": None,
    },

    # ── harder · MRB-338 night-3 top-up ──────────────────────────────────
    {
        "id": "c10-04-h09",
        "band": "harder",
        "text": "PET is collected at nine in ten and recovers 50%; glass "
                "is collected at only half and recovers 90%. Multiplying "
                "each material's collection rate by its recovery gives "
                "0.45 in both cases. What does that near-match show about "
                "what actually drives the loop's performance?",
        "options": [
            {"text": "Collection rate and recovery combine "
                     "multiplicatively, so a poorly-recycling material "
                     "collected very well can equal a well-recycling "
                     "material collected only half as often",
             "correct": True},
            {"text": "It shows recovery is the only figure that matters, "
                     "and collection makes no real difference",
             "correct": False,
             "why": "If collection made no difference, halving it for "
                    "glass would not have changed the product exactly as "
                    "much as recovery does."},
            {"text": "It shows collection rate is the only figure that "
                     "genuinely matters here, and recovery makes "
                     "absolutely no real difference to the outcome "
                     "at all, whatever the material happens to be",
             "correct": False,
             "why": "If recovery made no difference, PET's lower "
                    "recovery would not have been balanced out by its "
                    "higher collection rate."},
            {"text": "It shows an error has been made, since two "
                     "different materials cannot give the same result",
             "correct": False,
             "why": "Two different materials CAN give the same product "
                    "of rate and recovery. It is a genuine and "
                    "informative coincidence, not an error."},
        ],
        "figure": None,
    },
    {
        "id": "c10-04-h10",
        "band": "harder",
        "text": "Aluminium's recovery is 0.95. Using multiplier = 1 ÷ "
                "(1 − rate × recovery), roughly what multiplier results "
                "if its collection rate is only half rather than nine in "
                "ten?",
        "options": [
            {"text": "About 6.9, since aluminium's own recovery barely "
                     "changes with collection",
             "correct": False,
             "why": "The multiplier depends on rate as well as recovery, "
                    "and halving the rate brings it down a great deal."},
            {"text": "About 1.9",
             "correct": True},
            {"text": "About 3.5",
             "correct": False,
             "why": "Halving the collection rate brings the multiplier "
                    "down further than this — to under two, not three "
                    "and a half."},
            {"text": "Exactly 1, since any drop in collection removes "
                     "the benefit of recycling entirely",
             "correct": False,
             "why": "A multiplier of exactly 1 only happens with ZERO "
                    "collection. Half collection still gives a real "
                    "benefit."},
        ],
        "figure": None,
    },
    {
        "id": "c10-04-h11",
        "band": "harder",
        "text": "Steel collected at nine in ten gives a multiplier of "
                "about 5.8. Roughly what does the same formula give if "
                "collection falls to one in four?",
        "options": [
            {"text": "About 5.8, unchanged, since steel's recovery "
                     "figure alone decides the multiplier",
             "correct": False,
             "why": "The formula uses rate as well as recovery. A large "
                    "drop in rate brings the multiplier down sharply."},
            {"text": "About 3.0",
             "correct": False,
             "why": "That overstates what a drop to one in four "
                    "collection leaves. The true figure is closer to 1.3."},
            {"text": "About 1.3",
             "correct": True},
            {"text": "Zero, since one in four is too low a rate for any "
                     "material to recycle at all",
             "correct": False,
             "why": "Some material still gets through even at a low "
                    "collection rate — the multiplier is small, not "
                    "zero."},
        ],
        "figure": None,
    },
    {
        "id": "c10-04-h12",
        "band": "harder",
        "text": "Crisp-packet film is collected at nine in ten — the same "
                "rate that gets aluminium to about seven lifetimes — yet "
                "film's multiplier barely rises above 1. Why does the "
                "high collection rate fail to help film the way it helps "
                "aluminium?",
        "options": [
            {"text": "Because film is heavier than aluminium, so the "
                     "same rate collects less of it by mass",
             "correct": False,
             "why": "Mass is held equal for every material in this "
                    "comparison. Weight is not why film's multiplier "
                    "stays low."},
            {"text": "Because the collection rate for film is secretly "
                     "much lower than nine in ten",
             "correct": False,
             "why": "The same nine-in-ten rate applies to both. The "
                    "difference lies elsewhere, in the recovery figure."},
            {"text": "Because film is worth less per tonne than "
                     "aluminium, so recyclers do not try as hard",
             "correct": False,
             "why": "Value plays no part in the formula. The multiplier "
                    "depends only on rate and recovery."},
            {"text": "Because film's recovery is only 2%, so multiplying "
                     "even a high rate by a near-zero recovery still "
                     "gives almost nothing",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c10-04-h13",
        "band": "harder",
        "text": "Using multiplier = 1 ÷ (1 − rate × recovery), a material "
                "has a recovery of 0.80. What is the minimum collection "
                "rate needed for its multiplier to reach at least 2.5?",
        "options": [
            {"text": "0.75, or three in four",
             "correct": True},
            {"text": "0.60, or three in five",
             "correct": False,
             "why": "At that rate the multiplier only reaches about 1.9, "
                    "short of 2.5."},
            {"text": "0.50, or half",
             "correct": False,
             "why": "At that rate the multiplier only reaches about 1.7, "
                    "well short of 2.5."},
            {"text": "1.0, or all of it",
             "correct": False,
             "why": "Full collection is not needed — three in four "
                    "collected already reaches 2.5 at this recovery."},
        ],
        "figure": None,
    },
    {
        "id": "c10-04-h14",
        "band": "harder",
        "text": "Recycled aluminium takes only about a twentieth of the "
                "energy of new metal from ore, yet bauxite extraction is "
                "called one of the most energy-hungry industrial "
                "processes there is. How can both statements be true "
                "together?",
        "options": [
            {"text": "They cannot — one of the two figures must be "
                     "wrong",
             "correct": False,
             "why": "Both are consistent: the twentieth compares recycled "
                    "with new, while the description of bauxite "
                    "extraction is about the absolute scale of the "
                    "process."},
            {"text": "The twentieth is a comparison with new metal; making "
                     "new aluminium is so energy-intensive that even a "
                     "twentieth of that figure is a substantial amount "
                     "of energy",
             "correct": True},
            {"text": "Bauxite extraction is said to have stopped being "
                     "energy-hungry entirely once large-scale "
                     "aluminium recycling became common practice "
                     "everywhere across the industrialised world",
             "correct": False,
             "why": "Nothing says extraction became less energy-hungry. "
                    "The saving is about choosing recycling over "
                    "extraction, not about extraction changing."},
            {"text": "The twentieth refers to money saved, not energy "
                     "saved",
             "correct": False,
             "why": "The figure is an energy comparison in MJ per "
                    "kilogram, not a cost figure."},
        ],
        "figure": None,
    },
    {
        "id": "c10-04-h15",
        "band": "harder",
        "text": "Steel recycles very well and iron ore is described as "
                "abundant, yet iron ore's supply is still called "
                "genuinely limited in energy terms. Why doesn't "
                "abundance in the ground remove the limit?",
        "options": [
            {"text": "Because abundant ores of any kind are, in every single "
                     "case, always the very hardest and most costly "
                     "of all to reach and extract",
             "correct": False,
             "why": "That reverses the actual point: the easiest, "
                    "highest-grade ore is used FIRST."},
            {"text": "Because scrap steel that has already been recycled once "
                     "will eventually run out no matter how much of "
                     "it is ever recycled again",
             "correct": False,
             "why": "The limit described concerns fresh ore extraction, "
                    "not the supply of scrap."},
            {"text": "Because the highest-grade ore is used first, so "
                     "what remains needs more digging and energy per "
                     "tonne of iron produced",
             "correct": True},
            {"text": "Because recycling steel actually uses more energy "
                     "than making it new",
             "correct": False,
             "why": "Recycling steel uses far less energy than making it "
                    "new. That is not where this limit comes from."},
        ],
        "figure": None,
    },
    {
        "id": "c10-04-h16",
        "band": "harder",
        "text": "A country with large phosphate deposits argues it need "
                "not bother recovering phosphorus from sewage, since it "
                "is not short of supply today. Using how a reserve is "
                "defined, what is wrong with that argument?",
        "options": [
            {"text": "Nothing — a country holding large deposits genuinely "
                     "never needs to consider recovering phosphorus from "
                     "sewage at all",
             "correct": False,
             "why": "A large deposit today is not a promise for every "
                    "future year. The argument ignores how the usable "
                    "reserve can shrink."},
            {"text": "Today's comfortable supply says nothing about "
                     "whether the reserve stays large as the cheapest, "
                     "most concentrated deposits are used up first",
             "correct": True},
            {"text": "The argument is wrong because sewage recovery is "
                     "already the main source of phosphorus everywhere in "
                     "the world",
             "correct": False,
             "why": "Sewage recovery is described as only starting to "
                    "happen, not as the established main source anywhere "
                    "yet."},
            {"text": "The argument is wrong because phosphate rock is not "
                     "actually a finite resource at all",
             "correct": False,
             "why": "Phosphate rock is finite. The argument's flaw is "
                    "about how a comfortable supply today can still run "
                    "into trouble later, not about whether it is finite."},
        ],
        "figure": None,
    },
    {
        "id": "c10-04-h17",
        "band": "harder",
        "text": "An MRI installation captures escaping helium; a party "
                "balloon does not. Once helium DOES reach open air, "
                "regardless of how it got there, what is true of all of "
                "it?",
        "options": [
            {"text": "It will eventually rise and leave the atmosphere "
                     "for space, whatever captured it or released it "
                     "earlier",
             "correct": True},
            {"text": "It will eventually sink back down to ground level "
                     "and be absorbed into the soil, in the way a heavy gas "
                     "settles into a hollow",
             "correct": False,
             "why": "Helium is far less dense than air and rises rather "
                    "than sinking or being absorbed."},
            {"text": "It stays in the room until somebody breathes it in",
             "correct": False,
             "why": "It disperses and rises through the atmosphere; it "
                    "does not simply remain in one room."},
            {"text": "It turns into a different gas over time",
             "correct": False,
             "why": "Helium reacts with nothing and does not change into "
                    "another substance. It simply leaves."},
        ],
        "figure": None,
    },
    {
        "id": "c10-04-h18",
        "band": "harder",
        "text": "A plastic bag made from crude oil is recycled twice "
                "before landfill; the same mass of oil burned as fuel "
                "releases its carbon within moments. Which keeps the "
                "carbon out of the atmosphere for longer, and does either "
                "return it as a usable resource comparable to a reserve "
                "of oil?",
        "options": [
            {"text": "Burning keeps the carbon out of the atmosphere for "
                     "longer than anything else possibly could, and "
                     "neither route returns it as a usable resource",
             "correct": False,
             "why": "Burning releases carbon into the air almost "
                    "immediately — the opposite of keeping it out."},
            {"text": "The bag keeps it out for far longer, and neither "
                     "route turns it back into a resource comparable to "
                     "a reserve of oil",
             "correct": True},
            {"text": "The bag keeps it out for longer, and recycling it "
                     "eventually and fully restores the material to "
                     "a genuine reserve of crude oil once again",
             "correct": False,
             "why": "Recycled plastic never becomes crude oil again. "
                    "Landfill is the end of that loop."},
            {"text": "Both keep the carbon out equally long, since both "
                     "eventually reach the same end point",
             "correct": False,
             "why": "Burning releases the carbon almost at once. A "
                    "product used for years and then landfilled delays "
                    "it far longer."},
        ],
        "figure": None,
    },
    {
        "id": "c10-04-h19",
        "band": "harder",
        "text": "PET's recovery is 0.50. However high its collection rate "
                "is pushed, using multiplier = 1 ÷ (1 − rate × recovery), "
                "what is the highest multiplier PET could ever reach?",
        "options": [
            {"text": "Unlimited, since raising collection is always "
                     "enough on its own to reach any multiplier at all",
             "correct": False,
             "why": "Recovery sets a ceiling here. However high collection "
                     "goes, the multiplier cannot climb past that ceiling."},
            {"text": "About 6.9, matching the multiplier aluminium reaches "
                     "at nine in ten collected",
             "correct": False,
             "why": "That figure belongs to aluminium's own recovery of "
                    "0.95, not to PET's much lower 0.50."},
            {"text": "About 2, reached only if every single item were "
                     "collected",
             "correct": True},
            {"text": "About 1, since a recovery this low means collection "
                     "can never help at all",
             "correct": False,
             "why": "Collection does help, right up to the ceiling — it "
                    "just cannot push PET's multiplier past about 2."},
        ],
        "figure": None,
    },
    {
        "id": "c10-04-h20",
        "band": "harder",
        "text": "Even a lamination technology that separated a crisp "
                "packet's layers perfectly would still cost about "
                "90 MJ/kg to reprocess — the same as making it fresh. "
                "What would that reveal, once separation is no longer "
                "the problem?",
        "options": [
            {"text": "That the packet would then behave exactly like "
                     "aluminium",
             "correct": False,
             "why": "Recycled aluminium takes only about a twentieth of "
                    "the energy of new metal. Film, on these figures, "
                    "would still save none at all."},
            {"text": "That the separation technology must be flawed",
             "correct": False,
             "why": "The scenario assumes separation works perfectly. "
                    "The unchanged energy figure is a separate limit."},
            {"text": "That the packet was never really two different "
                     "materials in the first place, and the whole "
                     "separation problem was a misreading of how the "
                     "laminate is made",
             "correct": False,
             "why": "It genuinely is plastic bonded to metal. The energy "
                    "figures concern reprocessing cost, not composition."},
            {"text": "That recovery and energy-efficiency are two "
                     "separate properties, and film would still fail on "
                     "the second even after fixing the first",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c10-04-h21",
        "band": "harder",
        "text": "PET's energy figures show an 80% saving when recycled "
                "(85 new, 17 recycled) — a bigger percentage saving than "
                "glass's 27%. Does that make recycling PET more valuable "
                "overall than recycling glass?",
        "options": [
            {"text": "Not necessarily — PET's low recovery (50%) means "
                     "only half the collected material ever gets that "
                     "saving, while glass's 90% recovery spreads its "
                     "smaller saving over almost all of it",
             "correct": True},
            {"text": "Yes, always — the bigger percentage saving shown on "
                     "paper by itself settles the whole comparison "
                     "immediately and completely, without needing "
                     "any other figure to be checked or considered "
                     "at all, ever",
             "correct": False,
             "why": "The percentage saving alone ignores how much of the "
                    "collected material actually survives to benefit "
                    "from it."},
            {"text": "No — a material with a lower percentage saving is "
                     "always the better choice",
             "correct": False,
             "why": "That is too strong a rule. Overall value depends on "
                    "combining the saving with the recovery figure."},
            {"text": "It cannot be compared at all, since the two "
                     "materials use different units",
             "correct": False,
             "why": "Both are measured the same way, in MJ per "
                    "kilogram. A comparison is possible; it is just not "
                    "decided by the percentage alone."},
        ],
        "figure": None,
    },
    {
        "id": "c10-04-h22",
        "band": "harder",
        "text": "Unlike a metal ore, releasing helium loses it from the "
                "PLANET entirely rather than merely making it harder to "
                "extract. What follows for how a helium reserve should "
                "be managed, compared with a metal ore?",
        "options": [
            {"text": "Nothing at all follows from this difference — both kinds "
                     "of resource can simply be left exactly where "
                     "they are and extracted again later on "
                     "whenever anybody happens to need them",
             "correct": False,
             "why": "A metal ore can wait in the ground for later "
                    "extraction. Released helium cannot be gathered back "
                    "from the air later at any price."},
            {"text": "Unused metal ore can be extracted later as prices "
                     "or technology change; released helium cannot be "
                     "reclaimed from the air later at any price, so "
                     "capture must happen before release",
             "correct": True},
            {"text": "Both kinds of resource must always be captured before "
                     "release, since neither a metal ore nor a gas "
                     "like helium can ever safely be left sitting "
                     "unused underground or in the open air for any "
                     "length of time at all",
             "correct": False,
             "why": "A metal reserve is routinely left unused for later. "
                    "It is helium specifically that cannot wait once "
                    "released."},
            {"text": "Helium reserves grow back over time, unlike a "
                     "metal's",
             "correct": False,
             "why": "Helium is made underground over hundreds of "
                    "millions of years by radioactive decay — it does "
                    "not grow back on any human timescale either."},
        ],
        "figure": None,
    },
    {
        "id": "c10-04-h23",
        "band": "harder",
        "text": "A material's multiplier is 4 when collected at nine in "
                "ten (0.9). Using multiplier = 1 ÷ (1 − rate × recovery), "
                "what is that material's recovery?",
        "options": [
            {"text": "About 0.90",
             "correct": False,
             "why": "At recovery 0.90 and rate 0.9 the multiplier would "
                    "be about 5.3, higher than 4."},
            {"text": "About 0.95",
             "correct": False,
             "why": "At recovery 0.95 the multiplier would be about 6.9, "
                    "well above 4."},
            {"text": "About 0.83",
             "correct": True},
            {"text": "About 0.50",
             "correct": False,
             "why": "At recovery 0.50 the multiplier would only be about "
                    "1.8, far below 4."},
        ],
        "figure": None,
    },
    {
        "id": "c10-04-h24",
        "band": "harder",
        "text": "Using multiplier = 1 ÷ (1 − rate × recovery), what does "
                "the formula give when the collection rate is exactly "
                "zero, whatever the material's recovery figure happens "
                "to be?",
        "options": [
            {"text": "It gives a different answer each time, since recovery "
                     "still matters",
             "correct": False,
             "why": "With nothing collected, the recovery figure has "
                    "nothing to act on, so it makes no difference to the "
                    "result."},
            {"text": "It cannot be calculated when the rate is zero",
             "correct": False,
             "why": "The formula still works at rate zero: 1 minus zero "
                    "times anything is 1, and 1 divided by 1 is 1."},
            {"text": "It gives infinity, since nothing is ever lost from "
                     "the loop",
             "correct": False,
             "why": "Zero collection is the worst case, not the best — "
                    "it gives the SMALLEST possible multiplier."},
            {"text": "It always gives exactly 1, matching a material "
                     "used once and then gone",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c10-04-h25",
        "band": "harder",
        "text": "Bauxite is often described as 'plenty in the ground for "
                "now'. Does that make its supply less of a genuine limit "
                "than a metal whose published 'years left' figure is "
                "small?",
        "options": [
            {"text": "No — bauxite's limit shows up as rising energy "
                     "cost rather than as a small years-left number, "
                     "which a plentiful-sounding supply can hide",
             "correct": True},
            {"text": "Yes — a resource described as plentiful cannot "
                     "have a genuine limit at all",
             "correct": False,
             "why": "Bauxite is still finite and carries a real limit "
                    "even while its current supply is called plentiful."},
            {"text": "Yes — published 'years left' figures are always, in "
                     "every single case, far more reliable and "
                     "trustworthy than any other kind of resource "
                     "limit could ever possibly be",
             "correct": False,
             "why": "Years-left figures move with price and technology. "
                    "They are not more reliable than an energy-based "
                    "limit."},
            {"text": "No — but only because bauxite will run out sooner "
                     "than any other resource here",
             "correct": False,
             "why": "Nothing ranks bauxite as running out soonest. The "
                    "point is about what KIND of limit it faces, not its "
                    "timing."},
        ],
        "figure": None,
    },
    {
        "id": "c10-04-h26",
        "band": "harder",
        "text": "PET's polymer chains shorten a little every time the "
                "material is melted. Why does that make PET "
                "fundamentally different from a metal such as steel, "
                "which can in principle be melted and recast repeatedly?",
        "options": [
            {"text": "Steel does not actually melt when it is recycled",
             "correct": False,
             "why": "Steel genuinely is melted to be recycled. The "
                    "difference is what melting does to each material's "
                    "structure."},
            {"text": "Melting does not change a metal's atoms, but it "
                     "physically breaks down a polymer's long molecular "
                     "chains a little each time",
             "correct": True},
            {"text": "PET is heavier than steel for its size, so it takes "
                     "in more heat during melting and breaks apart faster "
                     "than the metal does",
             "correct": False,
             "why": "Weight is not the reason. The reason is the "
                    "difference between a metal's atoms and a polymer's "
                    "chain structure."},
            {"text": "Steel is a compound and PET is an element, so only "
                     "PET can degrade",
             "correct": False,
             "why": "Steel is mostly the element iron, and PET is a "
                    "compound. This has nothing to do with why one "
                    "degrades and the other does not."},
        ],
        "figure": None,
    },
    {
        "id": "c10-04-h27",
        "band": "harder",
        "text": "Which keeps crude oil's carbon out of circulation for "
                "LONGER: turning it into a durable plastic product used "
                "for decades before landfill, or turning it into fuel "
                "burned within months?",
        "options": [
            {"text": "Fuel, since burning uses up the carbon completely "
                     "and permanently",
             "correct": False,
             "why": "Burning releases the carbon into the air almost "
                    "immediately — the opposite of keeping it out of "
                    "circulation."},
            {"text": "Neither — both release the carbon at exactly the "
                     "same rate",
             "correct": False,
             "why": "A product used for decades clearly delays release "
                    "far longer than fuel burned within months."},
            {"text": "The durable plastic product, since its carbon is "
                     "not released until it is eventually destroyed, "
                     "decades later",
             "correct": True},
            {"text": "It cannot be judged, since plastic and fuel are "
                     "chemically unrelated, and the carbon in one has "
                     "nothing to do with the carbon in the other",
             "correct": False,
             "why": "Both are made from the same crude oil and contain "
                    "the same kind of carbon. A comparison of timing is "
                    "possible."},
        ],
        "figure": None,
    },
    {
        "id": "c10-04-h28",
        "band": "harder",
        "text": "At the same nine-in-ten collection rate, aluminium "
                "reaches a multiplier of about 6.9 and steel reaches "
                "about 5.8, even though their recovery figures are close "
                "(95% and 92%). What does that gap show about how "
                "sensitive the multiplier is at high collection rates?",
        "options": [
            {"text": "That the formula becomes unreliable at high "
                     "collection rates, so any figure above about eight in "
                     "ten collected should not be trusted at all",
             "correct": False,
             "why": "The formula matches the lesson's own stated figure "
                    "for aluminium. It is doing exactly what it should."},
            {"text": "That recovery stops mattering once collection is "
                     "already high",
             "correct": False,
             "why": "The gap between 6.9 and 5.8 shows recovery still "
                    "matters a great deal at high collection — it is "
                    "highly sensitive there, not irrelevant."},
            {"text": "That steel must actually have a somewhat lower rate of "
                     "collection than aluminium does in this "
                     "particular comparison being made here",
             "correct": False,
             "why": "The rate is stated as the same nine-in-ten for "
                    "both. The gap comes from the small difference in "
                    "recovery."},
            {"text": "That a small difference in recovery produces a "
                     "much larger difference in the multiplier once "
                     "collection is already high",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c10-04-h29",
        "band": "harder",
        "text": "A council reports that its overall recycling has "
                "'improved' this year because it now collects more of "
                "every material. Using what the loop shows, what "
                "question would you need answered before agreeing the "
                "improvement is real?",
        "options": [
            {"text": "Whether the RECOVERY figures for those materials "
                     "have also stayed the same, since collecting more "
                     "of a poorly-recovering material still returns "
                     "little",
             "correct": True},
            {"text": "Whether the council spent more money on collection "
                     "lorries",
             "correct": False,
             "why": "Spending on collection is not what decides the "
                    "outcome. Collection rate together with recovery "
                    "does."},
            {"text": "Whether the materials are now collected in bigger "
                     "bins",
             "correct": False,
             "why": "Bin size is not a figure that is tracked. Collection "
                    "rate and recovery are what decide the outcome."},
            {"text": "Nothing further would ever really be needed at all — "
                     "collecting more of absolutely anything, "
                     "whatever it happens to be, always counts as a "
                     "real and genuine improvement",
             "correct": False,
             "why": "Collecting more of a material with very low "
                    "recovery, such as crisp-packet film, still returns "
                    "almost nothing."},
        ],
        "figure": None,
    },
    {
        "id": "c10-04-h30",
        "band": "harder",
        "text": "Bauxite's limit is best described as an ENERGY limit, "
                "and phosphate rock's as having NO SUBSTITUTE. A student "
                "argues a resource cannot face two different kinds of "
                "limit at the same time. Is that a fair conclusion?",
        "options": [
            {"text": "Yes — a resource can only ever have exactly one single "
                     "kind of limit attached to it, and never more "
                     "than one at the same time",
             "correct": False,
             "why": "Nothing about how these limits are described rules "
                    "out a resource facing more than one kind at once."},
            {"text": "No — naming the most notable limit for a resource "
                     "does not rule out a second kind applying to it as "
                     "well",
             "correct": True},
            {"text": "Yes — energy limits and no-substitute limits are "
                     "complete opposites of one another that could "
                     "never possibly coexist together",
             "correct": False,
             "why": "The two describe different aspects of a resource — "
                    "extraction cost, and whether anything can replace "
                    "it — not opposites of each other."},
            {"text": "No — but only because every resource actually has "
                     "all of these limits at once",
             "correct": False,
             "why": "Nothing claims every resource carries every kind of "
                    "limit at once, only that having one does not "
                    "exclude having another."},
        ],
        "figure": None,
    },
]
