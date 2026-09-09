"""Biology · Cell biology — the MRB-338 expansion of `cell-specialisation`.

One leaf only: AQA 8461 §4.1.1, differentiation and the named specialised
cells. The original twelve rows in `cell_biology.py` take gene switching, the
meristem, the acrosome, phloem's cargo, sieve plates, root hair osmosis, the
myelin sheath, animal-vs-plant differentiation, the biconcave disc, lignin,
the haploid nucleus and companion cells. This file takes what they leave: the
definition of differentiation itself, division-before-differentiation, the
muscle cell and the neurone's dendrites and synaptic terminals, the palisade
cell, xylem's dead hollow lumen and missing end walls, root hair surface area
and its thin wall and vacuole, differentiation as repair in the adult, and the
whole misconception set — lost genes, specialised-means-larger, living xylem,
photosynthesising roots, and differentiation confused with mitosis.

The weight follows the CONTENT. `easier` stays at eight because recall in this
leaf is a short list of structures and two definitions, and asking it a ninth
way is the same question in new words. The demand lives in structure→function
reasoning run in both directions — given a job, predict the feature; given a
feature count, deduce the activity — and in comparing two cells and saying
which and why, so `standard` and `harder` carry twenty-two each.

Numbers here are the ones the biology actually supplies: a surface-area ratio
from a root hair projection and a conduction-time difference along a myelinated
axon. Magnification belongs to `microscopy` and would be that leaf's question
wearing this leaf's slug.
"""

TOPIC = "cell-biology"
SUBJECT = "biology"

QUESTIONS = [
    # ══ easier · e05–e12 ═════════════════════════════════════════════════
    # The definition of differentiation, division-before-differentiation, the
    # structures the original four never name (protein fibres, dendrites,
    # flagellum), the root hair projection, xylem's dead lumen, and
    # differentiation's job in the adult.
    {
        "id": "ks4-cell-specialisation-e05",
        "subtopic_slug": "cell-specialisation",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what the term differentiation means.",
        "options": [
            "A cell developing a structure that suits it to a particular job",
            "A cell dividing to make two cells that are identical to each other",
            "A cell growing until it reaches full size",
            "A cell taking in the substances it needs",
        ],
        "correct_index": 0,
        "why": "Differentiation is the process by which a cell acquires the "
               "structure that suits it to carrying out one particular "
               "function.",
    },
    {
        "id": "ks4-cell-specialisation-e06",
        "subtopic_slug": "cell-specialisation",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the parts of a muscle cell that slide past one another "
                "to make the cell shorter.",
        "options": [
            "Ribosomes, which build the proteins the muscle needs",
            "Mitochondria, which release the energy for the movement",
            "Protein fibres",
            "Lignin fibres, which give the cell its strength when it pulls",
        ],
        "correct_index": 2,
        "why": "A muscle cell contains contractile protein fibres that slide "
               "over one another, shortening the cell.",
    },
    {
        "id": "ks4-cell-specialisation-e07",
        "subtopic_slug": "cell-specialisation",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the short branching fibres of a nerve cell that receive "
                "signals from other nerve cells.",
        "options": [
            "The axon, the single long fibre that carries a signal away",
            "The dendrites, which branch out to meet many other nerve cells",
            "The myelin sheath, the fatty coat wrapped along the fibre",
            "The synaptic terminals, the endings that pass a signal on",
        ],
        "correct_index": 1,
        "why": "Dendrites are the short branched fibres that carry incoming "
               "signals towards the cell body.",
    },
    {
        "id": "ks4-cell-specialisation-e08",
        "subtopic_slug": "cell-specialisation",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State why a root hair cell has a long, narrow projection.",
        "options": [
            "It anchors the plant firmly into the soil so it cannot be pulled up",
            "It lets the cell reach down to water lying deep below the plant",
            "It stores the water taken in",
            "It increases the surface area for absorption",
        ],
        "correct_index": 3,
        "why": "The hair-like projection greatly increases the surface area "
               "in contact with soil water, so more can be absorbed.",
    },
    {
        "id": "ks4-cell-specialisation-e09",
        "subtopic_slug": "cell-specialisation",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State whether the cells that make up xylem are living or "
                "dead once they are carrying water.",
        "options": [
            "Living, because only a living cell can pull water upwards",
            "Living, but only during the daytime when water is moving",
            "Dead, so the tube is hollow and open",
            "Dead only in the roots",
        ],
        "correct_index": 2,
        "why": "Mature xylem cells are dead, which leaves an empty lumen with "
               "nothing inside to obstruct the water.",
    },
    {
        "id": "ks4-cell-specialisation-e10",
        "subtopic_slug": "cell-specialisation",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the type of cell division that produces the many cells "
                "of an embryo from one fertilised egg.",
        "options": [
            "Mitosis, which makes genetically identical body cells",
            "Meiosis, which halves the chromosome number each time",
            "Differentiation, which is a cell splitting into two",
            "Fertilisation, which repeats at every later division",
        ],
        "correct_index": 0,
        "why": "A zygote divides repeatedly by mitosis, producing identical "
               "cells that only later differentiate.",
    },
    {
        "id": "ks4-cell-specialisation-e11",
        "subtopic_slug": "cell-specialisation",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the main reason differentiation still happens in a "
                "mature animal.",
        "options": [
            "To let the animal grow much taller than it already is",
            "To allow the animal to change its body plan as the seasons change",
            "To let old organs be swapped for completely new organ types",
            "To repair and replace cells",
        ],
        "correct_index": 3,
        "why": "In a mature animal differentiation is largely restricted to "
               "repairing damage and replacing worn-out cells.",
    },
    {
        "id": "ks4-cell-specialisation-e12",
        "subtopic_slug": "cell-specialisation",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the structure that propels a sperm cell towards the egg.",
        "options": [
            "The acrosome at the very tip of the head",
            "The flagellum, or tail",
            "The midpiece",
            "The nucleus",
        ],
        "correct_index": 1,
        "why": "The flagellum is the whip-like tail that drives the sperm "
               "forward through fluid.",
    },

    # ══ standard · s05–s26 ═══════════════════════════════════════════════
    # Structure→function applied to a familiar cell, both directions of the
    # reasoning, and the misconception set met head on.
    {
        "id": "ks4-cell-specialisation-s05",
        "subtopic_slug": "cell-specialisation",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain how a muscle cell's mitochondria and its protein "
                "fibres work together when the cell contracts.",
        "options": [
            "The mitochondria push the protein fibres past one another using their own membranes",
            "The fibres pull, and the mitochondria supply the energy",
            "The protein fibres release the energy, and the mitochondria store it as glycogen",
            "The mitochondria shorten first and the protein fibres then hold the new length",
        ],
        "correct_index": 1,
        "why": "The protein fibres do the pulling, and the mitochondria "
               "release by respiration the energy that pulling costs.",
    },
    {
        "id": "ks4-cell-specialisation-s06",
        "subtopic_slug": "cell-specialisation",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain how a red blood cell being flexible helps it to do "
                "its job.",
        "options": [
            "It can stretch to hold more haemoglobin",
            "It can bend around white blood cells so that it is not attacked by them as it passes",
            "It can fold up and pass through the capillary wall",
            "It can squeeze through capillaries narrower than itself without tearing",
        ],
        "correct_index": 3,
        "why": "A flexible cell deforms to pass along the narrowest "
               "capillaries, so oxygen reaches every tissue.",
    },
    {
        "id": "ks4-cell-specialisation-s07",
        "subtopic_slug": "cell-specialisation",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why palisade mesophyll cells are packed with "
                "chloroplasts and sit near the upper surface of a leaf.",
        "options": [
            "They absorb the most light for photosynthesis there",
            "They shade the cells below so that those cells do not overheat in strong sun",
            "They are the first cells to receive water arriving from the xylem in the stem",
            "They must touch the cuticle to stay wet",
        ],
        "correct_index": 0,
        "why": "Light is strongest at the top of the leaf, so chloroplasts "
               "stacked there absorb the most of it.",
    },
    {
        "id": "ks4-cell-specialisation-s08",
        "subtopic_slug": "cell-specialisation",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain how the absence of end walls between xylem cells "
                "suits water transport.",
        "options": [
            "It lets the cells share cytoplasm so water can be pumped along",
            "It lets water leak sideways into the tissues that surround the tube",
            "The cells stack into one continuous open pipe, so water flows from root to leaf "
            "without being interrupted",
            "It makes the tube light enough for the stem to hold upright",
        ],
        "correct_index": 2,
        "why": "With the end walls gone the cells form an unbroken column, so "
               "the water is never interrupted on its way up.",
    },
    {
        "id": "ks4-cell-specialisation-s09",
        "subtopic_slug": "cell-specialisation",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student writes that a specialised cell must be bigger than "
                "an unspecialised one. Explain what is wrong with this.",
        "options": [
            "Nothing is wrong; specialising always adds structures and so adds size",
            "It is wrong, because every specialised cell is smaller than an unspecialised one",
            "It is wrong, because unspecialised cells are the largest cells in the body",
            "It is wrong, because specialising is about the structures a cell has, not its size; "
            "a sperm cell is tiny and highly specialised",
        ],
        "correct_index": 3,
        "why": "Specialisation is judged by the structures a cell has for its "
               "job; size has nothing to do with it.",
    },
    {
        "id": "ks4-cell-specialisation-s10",
        "subtopic_slug": "cell-specialisation",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Root hair cells contain unusually many mitochondria. Explain "
                "what this shows about how mineral ions enter the cell.",
        "options": [
            "Mitochondria make the glucose that the root needs in order to grow and divide",
            "Taking in mineral ions by active transport needs energy from respiration",
            "Mitochondria draw water into the cell from the soil by osmosis, against the gradient",
            "The cell stores minerals inside them",
        ],
        "correct_index": 1,
        "why": "Mineral ions are absorbed against a concentration gradient by "
               "active transport, which is powered by respiration.",
    },
    {
        "id": "ks4-cell-specialisation-s11",
        "subtopic_slug": "cell-specialisation",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain how the great length of a nerve cell's axon suits "
                "its function.",
        "options": [
            "A long axon gives the impulse more time to build up its strength",
            "A long axon can store many impulses at once until they are needed",
            "One cell can carry the impulse the whole way, with no delay at a junction between cells",
            "A long axon lets the cell reach a blood vessel and collect the glucose it needs to "
            "respire quickly",
        ],
        "correct_index": 2,
        "why": "A single long axon carries the impulse from one end to the "
               "other without the delay of crossing a synapse.",
    },
    {
        "id": "ks4-cell-specialisation-s12",
        "subtopic_slug": "cell-specialisation",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why meristems are found at the tips of roots and "
                "shoots.",
        "options": [
            "That is where the plant grows longer",
            "That is where the plant is thickest and needs the most support from new cells",
            "That is where the plant is safest from being eaten by animals in the soil",
            "That is where sugars from the leaves collect before they are used up",
        ],
        "correct_index": 0,
        "why": "Roots and shoots extend at their tips, so the undifferentiated "
               "cells that supply the new tissue sit there.",
    },
    {
        "id": "ks4-cell-specialisation-s13",
        "subtopic_slug": "cell-specialisation",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A cell's job is to make and release large amounts of a "
                "protein hormone. Predict the sub-cellular structure it will "
                "contain in unusually large numbers.",
        "options": [
            "Ribosomes, because proteins are assembled there",
            "Chloroplasts, because the hormone is built from the products of photosynthesis",
            "Vacuoles, to hold the hormone",
            "Sieve plates",
        ],
        "correct_index": 0,
        "why": "Proteins are built at the ribosomes, so a cell exporting a "
               "protein hormone carries far more of them than usual.",
    },
    {
        "id": "ks4-cell-specialisation-s14",
        "subtopic_slug": "cell-specialisation",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A plant cell sits deep inside a stem where no light reaches. "
                "Predict which sub-cellular structure it will not develop.",
        "options": [
            "The cell wall, since there is no need for support so far inside",
            "The mitochondria, since a cell in the dark cannot respire at all",
            "The chloroplasts",
            "The permanent vacuole, since there is no water this far from the roots",
        ],
        "correct_index": 2,
        "why": "Chloroplasts are only worth making where light reaches, so a "
               "cell in permanent darkness does not develop them.",
    },
    {
        "id": "ks4-cell-specialisation-s15",
        "subtopic_slug": "cell-specialisation",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain how the large permanent vacuole of a root hair cell "
                "helps water to enter it.",
        "options": [
            "It pushes water out of the cell so that more can flow in behind it",
            "It holds a concentrated cell sap, so water moves in from the more dilute soil water "
            "by osmosis",
            "It stores the mineral ions until the plant is ready to use them",
            "It presses on the cell wall and forces the soil water inwards",
        ],
        "correct_index": 1,
        "why": "The concentrated sap keeps the inside of the cell more "
               "concentrated than the soil water, so water enters by osmosis.",
    },
    {
        "id": "ks4-cell-specialisation-s16",
        "subtopic_slug": "cell-specialisation",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why the head of a sperm cell is streamlined.",
        "options": [
            "It reduces the number of mitochondria the cell has to carry along with it",
            "It makes the sperm heavy enough to sink towards the egg in the fluid",
            "It spreads the enzymes evenly",
            "It reduces drag, so the sperm swims faster",
        ],
        "correct_index": 3,
        "why": "A streamlined head meets less resistance from the fluid, so "
               "the same effort moves the sperm faster.",
    },
    {
        "id": "ks4-cell-specialisation-s17",
        "subtopic_slug": "cell-specialisation",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why phloem cells keep their cytoplasm while xylem "
                "cells lose theirs.",
        "options": [
            "Phloem carries a heavier substance, so it needs the cytoplasm for extra strength",
            "Xylem cells are younger, and cells lose their cytoplasm as they get older",
            "Phloem is living and needs cytoplasm to move sugars along",
            "Phloem must photosynthesise",
        ],
        "correct_index": 2,
        "why": "Phloem is a living tissue and its cytoplasm is where the "
               "sugar solution is carried from cell to cell.",
    },
    {
        "id": "ks4-cell-specialisation-s18",
        "subtopic_slug": "cell-specialisation",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student says that differentiation is another name for cell "
                "division. Explain what is wrong with this.",
        "options": [
            "Division makes more cells of the same kind, while differentiation is the change that "
            "makes a cell suited to one particular job",
            "Nothing is wrong; both words describe one cell becoming two cells",
            "Differentiation happens first, and cell division then copies the specialised cell",
            "Division only happens in plants, while differentiation only happens in animals",
        ],
        "correct_index": 0,
        "why": "Division increases cell number; differentiation changes what a "
               "cell is, and the two are separate events.",
    },
    {
        "id": "ks4-cell-specialisation-s19",
        "subtopic_slug": "cell-specialisation",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student says a muscle cell has got rid of the genes for "
                "making haemoglobin. Explain what is wrong.",
        "options": [
            "It is right; the unused genes are broken down as the cell specialises",
            "It is right, because only red blood cells are given the haemoglobin gene at first",
            "It is wrong, because muscle cells make small amounts of haemoglobin all the time",
            "It is wrong; the gene is still there but switched off",
        ],
        "correct_index": 3,
        "why": "Differentiation switches genes off rather than removing them, "
               "so every body cell keeps the whole set.",
    },
    {
        "id": "ks4-cell-specialisation-s20",
        "subtopic_slug": "cell-specialisation",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A cell is found to contain very few mitochondria. Explain "
                "why it is unlikely to be a muscle cell.",
        "options": [
            "Muscle cells have no mitochondria at all, so any at all rules it out",
            "Muscle contraction demands a lot of energy, so a muscle cell has many mitochondria",
            "Muscle cells are big, so they must contain more of every organelle than other cells",
            "Muscle cells respire without oxygen, so they have no use for mitochondria",
        ],
        "correct_index": 1,
        "why": "Mitochondria number tracks energy demand, and a contracting "
               "muscle cell has one of the highest demands in the body.",
    },
    {
        "id": "ks4-cell-specialisation-s21",
        "subtopic_slug": "cell-specialisation",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why the end of a nerve cell's axon branches into "
                "many bulb-like terminals.",
        "options": [
            "They anchor the nerve cell to the muscle so the signal cannot be shaken loose",
            "They release neurotransmitter to pass the signal on",
            "They collect the glucose the nerve cell will respire during a long journey",
            "They store impulses until the next nerve cell is ready to receive them",
        ],
        "correct_index": 1,
        "why": "Each terminal forms a synapse and releases neurotransmitter, "
               "which carries the signal to the next cell.",
    },
    {
        "id": "ks4-cell-specialisation-s22",
        "subtopic_slug": "cell-specialisation",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain how the thin cell wall of a root hair cell suits "
                "absorption.",
        "options": [
            "It lets the whole cell bend so it can push between the soil particles",
            "It lets ions in with no energy",
            "It keeps the cell from bursting",
            "It gives a short distance for water and ions to cross",
        ],
        "correct_index": 3,
        "why": "A thinner wall shortens the distance substances have to "
               "travel, so they enter the cell faster.",
    },
    {
        "id": "ks4-cell-specialisation-s23",
        "subtopic_slug": "cell-specialisation",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A gardener grows a whole new plant from a cut piece of stem, "
                "but a person cannot regrow a lost finger. Explain the "
                "difference.",
        "options": [
            "Plants keep undifferentiated meristem cells all through life",
            "Human cells are too specialised to divide by mitosis even once more",
            "Plant cells divide by meiosis, which can rebuild any part of the plant",
            "A plant has no organs",
        ],
        "correct_index": 0,
        "why": "Meristem cells stay undifferentiated for the plant's whole "
               "life, so a cutting can still make every tissue it needs.",
    },
    {
        "id": "ks4-cell-specialisation-s24",
        "subtopic_slug": "cell-specialisation",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain the advantage to a multicellular organism of having "
                "specialised cells.",
        "options": [
            "It means every cell can do every job if another cell fails",
            "It means the organism needs fewer cells altogether",
            "Each type of cell is very good at one job, so the whole organism works more "
            "efficiently than if every cell did everything",
            "It means the organism can grow without ever dividing its cells again",
        ],
        "correct_index": 2,
        "why": "Dividing the work between cell types lets each do its own job "
               "well, which makes the whole organism more efficient.",
    },
    {
        "id": "ks4-cell-specialisation-s25",
        "subtopic_slug": "cell-specialisation",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a sperm cell's mitochondria are packed into the "
                "midpiece, just behind the head.",
        "options": [
            "It keeps them away from the acrosome enzymes at the front",
            "It balances the cell so the head does not tip over as it swims",
            "It leaves the head free to hold the nucleus and nothing else",
            "Energy is released right beside the tail that uses it, so none of it has to be "
            "carried the length of the cell",
        ],
        "correct_index": 3,
        "why": "Placing the mitochondria next to the tail supplies energy "
               "exactly where the swimming movement is produced.",
    },
    {
        "id": "ks4-cell-specialisation-s26",
        "subtopic_slug": "cell-specialisation",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a red blood cell cannot divide to replace itself.",
        "options": [
            "It is too flexible to hold the shape needed while it divides in two",
            "It has no nucleus, so it has no DNA to copy",
            "It has too few mitochondria to supply the energy that division would need",
            "It is dead",
        ],
        "correct_index": 1,
        "why": "Losing the nucleus loses the DNA, and no cell can divide "
               "without a copy of its genetic material to pass on.",
    },

    # ══ harder · h05–h26 ═════════════════════════════════════════════════
    # Unfamiliar contexts, comparison and evaluation, the two calculations
    # the biology genuinely supplies, and the misconception set met from the
    # wrong side.
    {
        "id": "ks4-cell-specialisation-h05",
        "subtopic_slug": "cell-specialisation",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare the number of mitochondria you would expect in a "
                "mature xylem cell with the number in a root hair cell, and "
                "explain the difference.",
        "options": [
            "Both have many, because both of them are involved in moving substances through the whole "
            "plant",
            "The xylem has more, because pulling water upwards is the more demanding job",
            "The root hair cell has many and the xylem has none, because xylem cells are dead",
            "Both have none, because plants respire only in their leaves",
        ],
        "correct_index": 2,
        "why": "A mature xylem cell has lost all its living contents, so it "
               "has no mitochondria, while the root hair cell needs plenty "
               "for active transport.",
    },
    {
        "id": "ks4-cell-specialisation-h06",
        "subtopic_slug": "cell-specialisation",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Cell A contains roughly 200 mitochondria and cell B roughly "
                "5. Deduce which is the more likely to be a heart muscle "
                "cell, and why.",
        "options": [
            "Cell A, because contracting constantly needs energy",
            "Cell B, because heart muscle works slowly and steadily rather than in bursts",
            "Cell A, because heart muscle cells are the largest cells in the human body",
            "Cell B, because the heart is supplied with so much blood that it needs few "
            "mitochondria of its own",
        ],
        "correct_index": 0,
        "why": "Mitochondria number is a measure of a cell's energy demand, "
               "and heart muscle contracts without rest for a lifetime.",
    },
    {
        "id": "ks4-cell-specialisation-h07",
        "subtopic_slug": "cell-specialisation",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate the claim that xylem cells must be alive because "
                "water keeps moving through them.",
        "options": [
            "The claim is wrong; water is pulled up by evaporation from the leaves, so the tube "
            "itself need not be alive",
            "The claim is right; a xylem cell uses energy from respiration to pump each drop of "
            "water on to the next cell above it",
            "The claim is right, because only living cells can be waterproofed with lignin",
            "The claim is wrong; xylem cells are alive only while the plant is growing",
        ],
        "correct_index": 0,
        "why": "The pull comes from evaporation at the leaves, not from the "
               "tube, so a dead hollow xylem cell moves water perfectly well.",
    },
    {
        "id": "ks4-cell-specialisation-h08",
        "subtopic_slug": "cell-specialisation",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A chemical stops mitochondria releasing energy in a root. "
                "Predict what happens to water uptake and to mineral ion "
                "uptake.",
        "options": [
            "Both stop, because every substance is taken into the root by active transport",
            "Both continue, because the root takes in soil water through its thin walls "
            "without help",
            "Water uptake continues; mineral ion uptake stops",
            "Water uptake stops, but mineral ions keep entering by diffusion down the gradient",
        ],
        "correct_index": 2,
        "why": "Osmosis is passive and carries on, but active transport of "
               "mineral ions stops the moment its energy supply is cut.",
    },
    {
        "id": "ks4-cell-specialisation-h09",
        "subtopic_slug": "cell-specialisation",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "The tip of a shoot is cut off and the plant stops getting "
                "taller, though its existing leaves grow normally. Explain "
                "this in terms of meristems.",
        "options": [
            "The cut has removed the leaves that supply the sugars for growth",
            "The shoot tip held the meristem, the only cells still able to divide and then "
            "differentiate into new stem tissue",
            "Cutting the shoot has blocked the xylem so no water can reach the top",
            "The plant has switched off every gene it uses for growing taller",
        ],
        "correct_index": 1,
        "why": "Height comes from the shoot meristem, so removing it removes "
               "the only supply of new undifferentiated cells for the stem.",
    },
    {
        "id": "ks4-cell-specialisation-h10",
        "subtopic_slug": "cell-specialisation",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why the trunk of a tree is made largely of dead "
                "xylem yet still holds the tree upright.",
        "options": [
            "The dead cells are held rigid by the living phloem wrapped around them on the outside",
            "Water pressure inside holds it up",
            "Dead cells shrink and pack tightly together, and that packing is what gives the "
            "strength",
            "Lignin in the walls stays strong after the cell dies",
        ],
        "correct_index": 3,
        "why": "Lignin is a hard thickening in the cell wall, and it goes on "
               "supporting the trunk long after the cell contents have gone.",
    },
    {
        "id": "ks4-cell-specialisation-h11",
        "subtopic_slug": "cell-specialisation",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A root hair projection raises one cell's surface area in "
                "contact with soil water from 0.02 mm2 to 0.20 mm2. Determine "
                "the factor by which the absorbing surface increases.",
        "options": [
            "0.18 times, from subtracting the smaller area from the larger",
            "100 times, because there are two decimal places in the figures",
            "10 times, since 0.20 divided by 0.02 is 10",
            "0.22 times, from adding the two areas",
        ],
        "correct_index": 2,
        "why": "A factor is a ratio, so 0.20 divided by 0.02 gives a "
               "ten-fold increase in absorbing surface.",
    },
    {
        "id": "ks4-cell-specialisation-h12",
        "subtopic_slug": "cell-specialisation",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "An impulse travels 1.0 m along a myelinated axon at 100 m/s, "
                "and along an identical unmyelinated axon at 1.0 m/s. "
                "Determine how much longer the unmyelinated axon takes.",
        "options": [
            "0.99 s longer, because the times are 1.0 s and 0.010 s",
            "99 s longer, because the times are 100 s and 1.0 s",
            "1.01 s longer, because the times are 1.0 s and 0.010 s",
            "0.010 s longer, because that is the myelinated axon's time",
        ],
        "correct_index": 0,
        "why": "The times are 1.0 s and 0.010 s, so the myelinated axon saves "
               "0.99 s over the same distance.",
    },
    {
        "id": "ks4-cell-specialisation-h13",
        "subtopic_slug": "cell-specialisation",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate the claim that a differentiated cell contains fewer "
                "genes than the fertilised egg it came from.",
        "options": [
            "The claim is right; the unused genes are broken down as the cell specialises",
            "The claim is right, because each cell keeps only the genes for the one job it does",
            "The claim is wrong; a differentiated cell has copied its genes and so holds twice "
            "as many",
            "The claim is wrong; all the genes are still there, just not all in use",
        ],
        "correct_index": 3,
        "why": "Every body cell carries the full set of genes; differentiation "
               "changes which are switched on, not how many are present.",
    },
    {
        "id": "ks4-cell-specialisation-h14",
        "subtopic_slug": "cell-specialisation",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Sucrose can be found moving both up and down a stem, but "
                "water in the xylem moves only upwards. Explain the "
                "difference.",
        "options": [
            "Xylem is much the wider tube, so gravity always wins and pulls all of its contents "
            "downwards towards the roots of the plant",
            "Phloem loads sugar wherever it is made and unloads it wherever it is needed, so "
            "flow can run either way",
            "Water is lighter than sucrose, so it can only ever be carried upwards",
            "Xylem is dead, so it cannot choose a direction",
        ],
        "correct_index": 1,
        "why": "Phloem is living and loads sugar actively at a source and "
               "unloads it at a sink, so its flow can run in either direction.",
    },
    {
        "id": "ks4-cell-specialisation-h15",
        "subtopic_slug": "cell-specialisation",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A ring of bark containing the phloem is cut away all round a "
                "tree trunk. The leaves stay green for weeks but the roots "
                "eventually die. Explain why.",
        "options": [
            "The xylem has been cut too, so no water can reach the roots from the soil below",
            "Sugars can no longer reach the roots",
            "The roots can no longer send water up to the leaves through the missing phloem",
            "The leaves keep all the sugar for themselves once the tree is damaged in any way",
        ],
        "correct_index": 1,
        "why": "The xylem is deeper in and still carries water up, but the "
               "roots depend on sugar delivered by phloem and starve without "
               "it.",
    },
    {
        "id": "ks4-cell-specialisation-h16",
        "subtopic_slug": "cell-specialisation",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest one advantage to a muscle cell of storing glycogen "
                "rather than relying only on glucose arriving in the blood.",
        "options": [
            "Glycogen can be respired without any oxygen, unlike the glucose carried in the blood",
            "Glycogen gives more energy per gram",
            "Glycogen takes up less room",
            "A store on the spot supplies glucose fast when demand suddenly rises",
        ],
        "correct_index": 3,
        "why": "A store inside the cell can be broken down immediately, so "
               "supply does not have to wait on delivery by the blood.",
    },
    {
        "id": "ks4-cell-specialisation-h17",
        "subtopic_slug": "cell-specialisation",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A cell in the lining of the small intestine takes up glucose "
                "from the gut even when the gut is more dilute than the cell. "
                "Predict two features it will have.",
        "options": [
            "Many mitochondria and a folded membrane",
            "Many chloroplasts and a thick lignified wall",
            "A large vacuole and a permanent store of glycogen",
            "No nucleus",
        ],
        "correct_index": 0,
        "why": "Absorbing against a gradient means active transport, so the "
               "cell needs plenty of mitochondria and a large folded surface.",
    },
    {
        "id": "ks4-cell-specialisation-h18",
        "subtopic_slug": "cell-specialisation",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Cell X is much larger than cell Y under the same microscope. "
                "Evaluate the conclusion that cell X must therefore be the "
                "more specialised of the two.",
        "options": [
            "The conclusion is right, because specialising always adds organelles and "
            "bulk, so of any two cells seen together the larger is always the one "
            "that has taken on a job",
            "The conclusion is right, unless cell Y happens to be a plant cell",
            "The conclusion is unsafe; specialisation is judged by the structures a cell has for "
            "its job, and a sperm cell is among the smallest and most specialised there is",
            "The conclusion is wrong, because the smaller cell is always the more "
            "specialised, so cell Y has taken on a particular job and cell X has not",
        ],
        "correct_index": 2,
        "why": "Size is not evidence either way; what marks specialisation is "
               "the structures a cell has developed for one job.",
    },
    {
        "id": "ks4-cell-specialisation-h19",
        "subtopic_slug": "cell-specialisation",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student claims a root hair cell makes its own glucose. "
                "Explain where the glucose that a root hair cell respires "
                "actually comes from.",
        "options": [
            "From the soil water, taken in alongside the mineral ions",
            "From the chloroplasts in the root, working by the light that reaches the topsoil",
            "From the mineral ions, which the cell joins together into glucose in "
            "its own cytoplasm",
            "From the leaves, where photosynthesis makes it; the phloem then carries it down to "
            "the root",
        ],
        "correct_index": 3,
        "why": "A root hair cell has no chloroplasts, so its glucose is made "
               "in the leaves and delivered to the root by the phloem.",
    },
    {
        "id": "ks4-cell-specialisation-h20",
        "subtopic_slug": "cell-specialisation",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "One cell divides to give two identical cells, and those two "
                "later become a nerve cell and a muscle cell. Name the "
                "process responsible for each stage.",
        "options": [
            "Differentiation makes the two cells, and mitosis then makes them different",
            "Mitosis makes the two cells; differentiation then makes them different",
            "Mitosis does both, because it can copy a cell and change it at the same time",
            "Meiosis makes the two cells, and mitosis then makes them different",
        ],
        "correct_index": 1,
        "why": "Mitosis produces the identical pair; differentiation is the "
               "later change that gives each one its own structure.",
    },
    {
        "id": "ks4-cell-specialisation-h21",
        "subtopic_slug": "cell-specialisation",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why the nerve cells of an adult are hardly ever "
                "replaced, while skin cells are replaced continually.",
        "options": [
            "Nerve cells never wear out, so none of them ever needs replacing",
            "Skin cells are unspecialised, so they can keep on dividing however often they "
            "happen to be lost",
            "Skin is worn away and replaced from cells that still divide; nerve cells no longer "
            "divide",
            "Nerve cells are replaced just as often, but the new ones are too small to see",
        ],
        "correct_index": 2,
        "why": "Skin keeps a supply of dividing cells for replacement, "
               "whereas a fully differentiated nerve cell has lost the ability "
               "to divide.",
    },
    {
        "id": "ks4-cell-specialisation-h22",
        "subtopic_slug": "cell-specialisation",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A cell has no nucleus, almost no mitochondria, and is filled "
                "with a protein that binds oxygen. Deduce what the cell is "
                "and what its shape will be.",
        "options": [
            "A red blood cell, shaped as a biconcave disc",
            "A sperm cell, with a streamlined head and a long tail behind it",
            "A xylem cell, forming a hollow tube with no end walls left in place",
            "A root hair cell, drawn out into a long thin projection into the soil",
        ],
        "correct_index": 0,
        "why": "No nucleus and a store of haemoglobin identify a red blood "
               "cell, which is a biconcave disc.",
    },
    {
        "id": "ks4-cell-specialisation-h23",
        "subtopic_slug": "cell-specialisation",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A palisade cell and a root hair cell in the same plant contain "
                "identical genes, yet one has chloroplasts and the other has "
                "none. Explain how.",
        "options": [
            "The two cells switch on different genes as they differentiate, according to where "
            "in the plant they end up",
            "The two cells come from different parts of the original fertilised egg cell, and so "
            "were never the same to begin with",
            "The root hair cell lost its chloroplasts when it was buried in the soil",
            "Only cells above ground contain genes for chloroplasts",
        ],
        "correct_index": 0,
        "why": "Identical meristem cells become different cells because "
               "differentiation switches on a different set of genes in each.",
    },
    {
        "id": "ks4-cell-specialisation-h24",
        "subtopic_slug": "cell-specialisation",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Xylem cells lose their end walls completely, while phloem "
                "sieve tubes keep end walls with pores in them. Suggest why "
                "phloem cannot lose its end walls as well.",
        "options": [
            "Without end walls the sugar solution would be pulled up into the xylem instead of "
            "travelling on",
            "Without end walls the phloem tube would collapse inwards, because it has no lignin "
            "in its walls to hold it open",
            "Phloem cells are alive, and the plates hold their contents in place while letting "
            "sap through",
            "Phloem must stay short",
        ],
        "correct_index": 2,
        "why": "A living cell needs its contents kept in place, so phloem "
               "keeps a perforated plate rather than an open end.",
    },
    {
        "id": "ks4-cell-specialisation-h25",
        "subtopic_slug": "cell-specialisation",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain, in terms of its protein fibres, why a muscle cell "
                "can shorten itself but cannot lengthen itself.",
        "options": [
            "The fibres slide apart again as soon as the cell has run out of stored glycogen",
            "The fibres can only pull, so another muscle must stretch this one out again",
            "The fibres are dissolved when the cell shortens and have to be rebuilt each time",
            "The fibres are held rigid by lignin, so they cannot be pushed back out again",
        ],
        "correct_index": 1,
        "why": "Contractile fibres generate a pulling force only, so a muscle "
               "is returned to length by a second muscle pulling the other way.",
    },
    {
        "id": "ks4-cell-specialisation-h26",
        "subtopic_slug": "cell-specialisation",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate the statement that a highly specialised cell is "
                "always more use to an organism than a less specialised one.",
        "options": [
            "It is always true, because a specialised cell can do several jobs at once",
            "It is never true, because a specialised cell can only ever be replaced by another "
            "cell of exactly its own kind",
            "It is always true, because specialised cells divide faster than unspecialised ones",
            "It is better at its one job, but cannot change role, so the organism still needs "
            "unspecialised cells",
        ],
        "correct_index": 3,
        "why": "Specialisation buys efficiency at the cost of flexibility, so "
               "an organism needs undifferentiated cells as well for growth "
               "and repair.",
    },
]
