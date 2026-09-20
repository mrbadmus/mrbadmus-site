"""Biology · Bioenergetics — the MRB-338 expansion of `uses-of-glucose`.

One leaf only: AQA 8461 §4.4.1.3. The original twelve rows in
`bioenergetics.py` take the potato tuber as a starch store, nitrate ions
supplying nitrogen for amino acids, the waxy cuticle as a lipid, the
identify-the-odd-one-out on nitrate ions, why a plant still needs to
respire, why starch is converted back to glucose before use, starch
falling in the dark, oil against starch in seeds, the ATP link between
respiration and active mineral uptake, cellulose against starch, a
nitrate fertiliser raising yield, and a 40 g glucose split into 25 g
used and 15 g stored.

This file takes what they leave: the named cell processes glucose-derived
ATP actually powers — active transport, cell division, protein synthesis,
guard-cell movement — cellulose as the most abundant organic molecule on
Earth and the sole reason a plant stands upright, lipids doing double duty
in membranes as well as seeds, the two-ingredient build of a protein
(glucose's carbon skeleton plus nitrate's nitrogen) worked from both
directions, and a run of glucose-allocation arithmetic in the same style
as the original 40 g row but never repeating its numbers.

Register follows the lesson: glucose is the plant's one starting point,
and every use here is something built FROM it or powered BY it, never a
use that competes with respiration for a different fuel.
"""

TOPIC = "bioenergetics"
SUBJECT = "biology"

QUESTIONS = [
    # ══ easier · e05–e12 ═══════════════════════════════════════
    {
        "id": "ks4-uses-of-glucose-e05",
        "subtopic_slug": "uses-of-glucose",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the main use of the glucose a plant makes in photosynthesis.",
        "options": [
            "Aerobic respiration, to release energy as ATP",
            "Storage as starch, before anything happens",
            "Building cellulose for the cell walls",
            "Making lipids for the leaf's waxy cuticle",
        ],
        "correct_index": 0,
        "why": "Most of a plant's glucose is respired, releasing the energy that powers "
               "everything else the plant does.",
    },
    {
        "id": "ks4-uses-of-glucose-e06",
        "subtopic_slug": "uses-of-glucose",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the process, powered by ATP from respiration, that moves mineral ions "
               "into root cells against a concentration gradient.",
        "options": [
            "Diffusion",
            "Active transport",
            "Osmosis",
            "Transpiration",
        ],
        "correct_index": 1,
        "why": "Active transport is the only one of the four that moves particles against a "
               "gradient, and doing so needs ATP.",
    },
    {
        "id": "ks4-uses-of-glucose-e07",
        "subtopic_slug": "uses-of-glucose",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State which cell process, powered by ATP, opens and closes a leaf's stomata.",
        "options": [
            "Photosynthesis in the stomata themselves",
            "Diffusion of glucose out of the leaf",
            "The movement of the guard cells",
            "The breakdown of chlorophyll",
        ],
        "correct_index": 2,
        "why": "Guard cells change shape to open or close a stoma, and this movement needs "
               "energy from respired glucose.",
    },
    {
        "id": "ks4-uses-of-glucose-e08",
        "subtopic_slug": "uses-of-glucose",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State one reason a dividing root tip cell needs a constant supply of "
               "glucose.",
        "options": [
            "To dissolve the cell wall before it divides",
            "To absorb water directly from the surrounding air",
            "To stop the cell respiring until division is complete",
            "To provide the energy needed for cell division",
        ],
        "correct_index": 3,
        "why": "Building new cells takes energy, which respired glucose supplies as ATP.",
    },
    {
        "id": "ks4-uses-of-glucose-e09",
        "subtopic_slug": "uses-of-glucose",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State which molecule, made from glucose, is described as the most abundant "
               "organic molecule on Earth.",
        "options": [
            "Cellulose",
            "Starch",
            "Glycogen",
            "Chlorophyll",
        ],
        "correct_index": 0,
        "why": "Cellulose, built from glucose into plant cell walls, is the most abundant "
               "organic molecule on Earth.",
    },
    {
        "id": "ks4-uses-of-glucose-e10",
        "subtopic_slug": "uses-of-glucose",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State where, besides in seeds, glucose-derived lipids are used in a plant "
               "cell.",
        "options": [
            "In the nucleus",
            "In cell membranes",
            "In the vacuole",
            "In the mitochondria",
        ],
        "correct_index": 1,
        "why": "Lipids made from glucose form the phospholipids of a cell's membranes, as "
               "well as being stored in seeds.",
    },
    {
        "id": "ks4-uses-of-glucose-e11",
        "subtopic_slug": "uses-of-glucose",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name two plant organs, besides the potato tuber, in which starch is stored.",
        "options": [
            "Xylem vessels and phloem tubes",
            "Stomata and guard cells",
            "Roots and seeds",
            "Petals and stamens",
        ],
        "correct_index": 2,
        "why": "Swollen roots such as carrots and parsnips, and seeds storing energy for "
               "germination, both hold starch.",
    },
    {
        "id": "ks4-uses-of-glucose-e12",
        "subtopic_slug": "uses-of-glucose",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Identify which of these processes does NOT use glucose as an energy source.",
        "options": [
            "Active transport of mineral ions",
            "Aerobic respiration",
            "Cell division",
            "Photosynthesis",
        ],
        "correct_index": 3,
        "why": "Photosynthesis makes glucose in the first place; it does not use glucose as "
               "fuel the way the other three processes do.",
    },

    # ══ standard · s05–s26 ═══════════════════════════════════════
    {
        "id": "ks4-uses-of-glucose-s05",
        "subtopic_slug": "uses-of-glucose",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why active transport, unlike diffusion, needs energy from respired "
               "glucose.",
        "options": [
            "Active transport moves particles against a concentration gradient, which "
            "diffusion never does",
            "Active transport happens just in root hair cells, unlike diffusion",
            "Active transport moves water, while diffusion moves dissolved ions instead",
            "Active transport happens just in the dark, unlike diffusion",
        ],
        "correct_index": 0,
        "why": "Moving particles from a low to a high concentration goes against the natural "
               "direction of movement, so energy from ATP is required.",
    },
    {
        "id": "ks4-uses-of-glucose-s06",
        "subtopic_slug": "uses-of-glucose",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare the role of glucose used to build cellulose with the role of glucose "
               "used to build the lipids of a seed.",
        "options": [
            "Cellulose stores energy for germination; seed lipids strengthen the seed "
            "coat",
            "Cellulose strengthens the cell wall; seed lipids are an energy store for "
            "germination",
            "Both are broken down immediately to release energy for growth",
            "Both are built once the seed has already begun to germinate",
        ],
        "correct_index": 1,
        "why": "Cellulose gives the cell wall its rigidity, while the lipids in a seed are a "
               "concentrated energy reserve for the seedling.",
    },
    {
        "id": "ks4-uses-of-glucose-s07",
        "subtopic_slug": "uses-of-glucose",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why a plant growing in nitrate-poor soil can still photosynthesise "
               "normally, yet grows poorly overall.",
        "options": [
            "Nitrate is needed for photosynthesis, but not for making starch",
            "Nitrate is needed to absorb carbon dioxide through the stomata",
            "Photosynthesis needs no nitrate, but protein synthesis for growth does",
            "Nitrate raises the rate of respiration, which limits photosynthesis",
        ],
        "correct_index": 2,
        "why": "Photosynthesis needs only carbon dioxide, water and light, but building new "
               "proteins for growth needs nitrate as well.",
    },
    {
        "id": "ks4-uses-of-glucose-s08",
        "subtopic_slug": "uses-of-glucose",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A gardener adds a fertiliser rich in phosphate, but with no nitrate, to "
               "nitrogen-starved soil. Explain why this would not help the plant make more "
               "protein.",
        "options": [
            "Phosphate stops nitrate being absorbed by the roots properly",
            "Phosphate is toxic to a plant's protein-making machinery",
            "Phosphate converts any existing protein back into glucose",
            "Phosphate cannot supply the nitrogen an amino group needs",
        ],
        "correct_index": 3,
        "why": "Amino acids need nitrogen for their amino group, and only nitrate — not "
               "phosphate — supplies that nitrogen.",
    },
    {
        "id": "ks4-uses-of-glucose-s09",
        "subtopic_slug": "uses-of-glucose",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why plant membranes, as well as seeds, are built using lipids made "
               "from glucose.",
        "options": [
            "Membranes need lipids for their structure, just as a seed needs lipids for "
            "energy storage",
            "A membrane is simply a very thin layer of starch, made the same way as a "
            "seed's store",
            "Membranes and seeds both use the same lipid molecules for the same purpose",
            "Membranes are built from lipids just in seeds, and nowhere else in the plant",
        ],
        "correct_index": 0,
        "why": "Lipids serve two separate purposes: structural phospholipids in every "
               "membrane, and an energy store specifically in seeds.",
    },
    {
        "id": "ks4-uses-of-glucose-s10",
        "subtopic_slug": "uses-of-glucose",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why glucose is described as the starting point for almost everything "
               "else a plant makes.",
        "options": [
            "Every mineral ion a plant absorbs is first converted into glucose",
            "Starch, cellulose, lipids and the carbon skeleton of amino acids are all "
            "built from it",
            "Glucose is the one molecule a plant is able to store for any length of time, "
            "whatever else the plant happens to be doing at the time",
            "Water and carbon dioxide are both made from glucose inside the leaf",
        ],
        "correct_index": 1,
        "why": "Photosynthesis's one product, glucose, supplies the material that starch, "
               "cellulose, lipids and amino acids are all built from.",
    },
    {
        "id": "ks4-uses-of-glucose-s11",
        "subtopic_slug": "uses-of-glucose",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A plant makes 55 g of glucose in a day and converts 31 g of it into starch, "
               "with no other product made. Determine the mass respired.",
        "options": [
            "86 g",
            "31 g",
            "24 g",
            "55 g",
        ],
        "correct_index": 2,
        "why": "55 g made minus 31 g stored as starch leaves 24 g available to be respired.",
    },
    {
        "id": "ks4-uses-of-glucose-s12",
        "subtopic_slug": "uses-of-glucose",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A pea seed stores its energy mostly as starch, while a sunflower seed stores "
               "its mostly as oil. Suggest an advantage of the sunflower's strategy for a "
               "seed that must be carried by an animal.",
        "options": [
            "Oil dissolves easily in water, so it spreads through the soil once eaten",
            "Oil is bright orange, which attracts animals to eat and disperse the seed",
            "Oil prevents the seed from ever germinating once it is swallowed",
            "Oil packs more energy into a smaller, lighter seed than starch would",
        ],
        "correct_index": 3,
        "why": "Lipids store more energy per gram than starch, so an oil-rich seed can be "
               "smaller and lighter for the same energy content.",
    },
    {
        "id": "ks4-uses-of-glucose-s13",
        "subtopic_slug": "uses-of-glucose",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a plant makes no protein at all once its nitrate supply is "
               "completely cut off, however much glucose it still has available.",
        "options": [
            "Amino acids need nitrogen from nitrate, which glucose cannot supply on its "
            "own",
            "Without nitrate, a plant is unable to photosynthesise or make any glucose",
            "Nitrate is what triggers respiration to begin releasing ATP in the first "
            "place",
            "Without nitrate, existing protein is converted straight back into starch",
        ],
        "correct_index": 0,
        "why": "Glucose supplies only the carbon skeleton of an amino acid; without nitrate "
               "there is no source of the nitrogen needed to complete it.",
    },
    {
        "id": "ks4-uses-of-glucose-s14",
        "subtopic_slug": "uses-of-glucose",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A plant's roots take in nitrate ions by active transport. Explain why this "
               "process itself depends indirectly on glucose.",
        "options": [
            "Nitrate ions are chemically identical to glucose once absorbed",
            "Active transport uses ATP, and ATP comes from respiring glucose",
            "Active transport happens just inside a chloroplast, near the glucose supply",
            "Glucose is converted directly into nitrate before it enters the root",
        ],
        "correct_index": 1,
        "why": "Active transport is powered by ATP, and that ATP is released when the root "
               "cells respire glucose.",
    },
    {
        "id": "ks4-uses-of-glucose-s15",
        "subtopic_slug": "uses-of-glucose",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare a plant's glucose demands when it is well-fertilised with nitrate "
               "against when it is grown in poor soil.",
        "options": [
            "A well-fertilised plant needs less glucose, since nitrate itself supplies "
            "energy",
            "Glucose demand is identical either way, since nitrate has no link to glucose "
            "use",
            "A well-fertilised plant uses more glucose making amino acids and protein",
            "A plant in poor soil uses more glucose, since it has to make more nitrate "
            "itself",
        ],
        "correct_index": 2,
        "why": "Plenty of nitrate lets a plant put more of its glucose towards building "
               "amino acids and protein for growth.",
    },
    {
        "id": "ks4-uses-of-glucose-s16",
        "subtopic_slug": "uses-of-glucose",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a dividing cell in a growing shoot tip respires more glucose "
               "than a mature, non-dividing leaf cell of similar size.",
        "options": [
            "A mature leaf cell has stopped respiring altogether once it is fully grown, "
            "since its cells no longer need to build anything new",
            "A dividing cell makes its own glucose, so it needs very little respiration",
            "A mature leaf cell converts all its glucose straight into starch instead",
            "Building new cell structures during division takes more energy than "
            "maintaining an existing one",
        ],
        "correct_index": 3,
        "why": "Making new cell walls, membranes and organelles during division demands far "
               "more ATP than simply maintaining a cell that has already grown.",
    },
    {
        "id": "ks4-uses-of-glucose-s17",
        "subtopic_slug": "uses-of-glucose",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why farmers sometimes plough cellulose-rich crop residue back into "
               "the soil rather than removing it.",
        "options": [
            "The residue breaks down slowly, returning organic matter and nutrients to "
            "the soil",
            "Cellulose in soil is absorbed directly by root hairs as ready-made glucose",
            "Ploughing residue in raises the soil's nitrate content immediately",
            "Cellulose residue stops the next crop's roots respiring properly",
        ],
        "correct_index": 0,
        "why": "Decomposing plant residue slowly releases nutrients and organic matter back "
               "into the soil for the next crop.",
    },
    {
        "id": "ks4-uses-of-glucose-s18",
        "subtopic_slug": "uses-of-glucose",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A plant makes 68 g of glucose in a week and converts 42 g of it into starch, "
               "with no other product made. Determine how much glucose remains for "
               "respiration and other uses.",
        "options": [
            "110 g",
            "26 g",
            "42 g",
            "68 g",
        ],
        "correct_index": 1,
        "why": "68 g made minus 42 g stored as starch leaves 26 g for respiration and every "
               "other use.",
    },
    {
        "id": "ks4-uses-of-glucose-s19",
        "subtopic_slug": "uses-of-glucose",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why starch or oil stored in a seed must be converted back into "
               "glucose before the seedling can use it.",
        "options": [
            "Starch and oil are both toxic to a growing seedling's cells",
            "A seedling has no enzymes able to break down starch or oil properly",
            "Only glucose can be respired to release usable energy as ATP",
            "Starch and oil evaporate away as soon as germination begins",
        ],
        "correct_index": 2,
        "why": "Respiration runs on glucose, so stored starch or oil has to be broken back "
               "down into glucose before its energy can be released.",
    },
    {
        "id": "ks4-uses-of-glucose-s20",
        "subtopic_slug": "uses-of-glucose",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare the uses of glucose in an actively growing shoot tip with its uses "
               "in a mature potato tuber.",
        "options": [
            "The shoot tip stores most of its glucose as starch; the tuber respires most "
            "of it for growth",
            "Both use their glucose in exactly the same proportions, regardless of their "
            "function",
            "Neither tissue uses any glucose, since both rely on stored starch instead",
            "The shoot tip respires most of its glucose for growth; the tuber stores most "
            "of it as starch",
        ],
        "correct_index": 3,
        "why": "A growing shoot tip has a high energy demand for cell division, while a "
               "tuber's role is mainly to store glucose as starch.",
    },
    {
        "id": "ks4-uses-of-glucose-s21",
        "subtopic_slug": "uses-of-glucose",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why adding nitrate fertiliser to soil has no direct effect on how "
               "much cellulose a plant makes.",
        "options": [
            "Cellulose is built from glucose alone, and nitrate supplies nitrogen, not "
            "carbon",
            "Cellulose is not made from glucose, so nitrate does not affect it either way",
            "Nitrate fertiliser stops photosynthesis, which is what makes cellulose",
            "Cellulose is broken down by nitrate as soon as it is added to soil",
        ],
        "correct_index": 0,
        "why": "Cellulose is a polymer of glucose alone, so a nitrogen source like nitrate "
               "has no direct part in making it.",
    },
    {
        "id": "ks4-uses-of-glucose-s22",
        "subtopic_slug": "uses-of-glucose",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why a plant devotes more of its glucose to making lipids while "
               "producing seeds than while growing its leaves.",
        "options": [
            "Leaves are made almost entirely of lipids, so they need very little glucose",
            "Seeds need a dense, portable energy store, unlike a growing leaf",
            "A leaf converts every gram of its glucose into cellulose instead of lipids",
            "Seeds barely respire, so most of their glucose must become lipid",
        ],
        "correct_index": 1,
        "why": "A seed benefits from a compact, energy-dense store to support the seedling, "
               "which lipids provide far better than a growing leaf needs.",
    },
    {
        "id": "ks4-uses-of-glucose-s23",
        "subtopic_slug": "uses-of-glucose",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a plant's active transport of nitrate ions would slow on a very "
               "cold night.",
        "options": [
            "Nitrate ions freeze in cold soil and cannot be absorbed",
            "Active transport works faster in the cold, since enzymes need less energy "
            "then, which is the opposite of what actually happens in cold conditions",
            "Cold temperatures slow the enzyme-controlled reactions of respiration, "
            "reducing the ATP supply",
            "Cold nights stop a plant's roots taking in water of any kind",
        ],
        "correct_index": 2,
        "why": "Colder temperatures slow respiration's enzyme-controlled reactions, cutting "
               "the ATP supply that active transport depends on.",
    },
    {
        "id": "ks4-uses-of-glucose-s24",
        "subtopic_slug": "uses-of-glucose",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A plant makes 86 g of glucose and uses 57 g of it directly in respiration, "
               "storing the rest as starch. Determine the mass stored as starch.",
        "options": [
            "57 g",
            "143 g",
            "86 g",
            "29 g",
        ],
        "correct_index": 3,
        "why": "86 g made minus 57 g respired leaves 29 g to be stored as starch.",
    },
    {
        "id": "ks4-uses-of-glucose-s25",
        "subtopic_slug": "uses-of-glucose",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why blocking a plant's active transport of mineral ions would slow "
               "its growth, even though photosynthesis continued normally.",
        "options": [
            "Nutrients such as nitrate could no longer enter the roots for protein "
            "synthesis",
            "Photosynthesis itself would stop within a few hours without active transport",
            "Blocking active transport stops respiration in every cell too",
            "The plant would immediately lose all the starch it had already stored",
        ],
        "correct_index": 0,
        "why": "Without active transport, minerals such as nitrate could not be absorbed "
               "against the gradient, starving the plant of nitrogen for growth.",
    },
    {
        "id": "ks4-uses-of-glucose-s26",
        "subtopic_slug": "uses-of-glucose",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Determine the mass of glucose made if a plant respires 37 g and stores a "
               "further 19 g as starch, with no other product made.",
        "options": [
            "18 g",
            "56 g",
            "19 g",
            "37 g",
        ],
        "correct_index": 1,
        "why": "37 g respired plus 19 g stored as starch adds up to 56 g of glucose made in "
               "total.",
    },

    # ══ harder · h05–h26 ═══════════════════════════════════════
    {
        "id": "ks4-uses-of-glucose-h05",
        "subtopic_slug": "uses-of-glucose",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Two identical plants are grown under the same bright light and CO2, but one "
               "is given plentiful nitrate and the other none at all. Predict which makes "
               "more protein, and explain.",
        "options": [
            "Both make the same protein, since glucose alone decides the outcome",
            "The plant given no nitrate, since it is forced to make its own nitrogen "
            "instead",
            "The plant with plentiful nitrate, since amino acids need nitrogen as well as "
            "glucose",
            "Neither plant can make any protein without light of a different colour "
            "entirely",
        ],
        "correct_index": 2,
        "why": "Protein synthesis needs both the carbon skeleton from glucose and the "
               "nitrogen from nitrate, so the plentifully fertilised plant makes far more "
               "protein.",
    },
    {
        "id": "ks4-uses-of-glucose-h06",
        "subtopic_slug": "uses-of-glucose",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate the claim that a plant's protein content depends only on how much "
               "glucose it makes.",
        "options": [
            "It is correct; glucose alone contains all the atoms a protein needs",
            "It is correct, provided the plant is grown in complete darkness",
            "It is wrong; protein is made entirely from nitrate, with no glucose "
            "involved, ignoring the carbon skeleton glucose supplies to every amino acid",
            "It is wrong; protein also needs nitrate for its nitrogen, however much "
            "glucose is made",
        ],
        "correct_index": 3,
        "why": "Glucose supplies only the carbon skeleton of an amino acid; nitrate must "
               "supply the nitrogen before a protein can be built.",
    },
    {
        "id": "ks4-uses-of-glucose-h07",
        "subtopic_slug": "uses-of-glucose",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A plant makes 132 g of glucose in a day: 44 g is respired, 33 g becomes "
               "starch, and 21 g becomes cellulose. Determine the mass left over for other "
               "uses.",
        "options": [
            "34 g",
            "98 g",
            "88 g",
            "44 g",
        ],
        "correct_index": 0,
        "why": "44 + 33 + 21 = 98 g accounted for, leaving 132 - 98 = 34 g for other uses "
               "such as protein and lipid synthesis.",
    },
    {
        "id": "ks4-uses-of-glucose-h08",
        "subtopic_slug": "uses-of-glucose",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare the fate of a molecule of glucose converted into starch with the "
               "fate of a molecule of glucose respired immediately.",
        "options": [
            "Both release their energy as ATP at exactly the same moment",
            "The starch molecule is held in reserve; the respired one has already "
            "released its energy as ATP",
            "The starch molecule is lost from the plant permanently; the respired one is "
            "stored, so its stored energy can never be recovered by the plant again",
            "Neither molecule can ever be used again once its fate is decided",
        ],
        "correct_index": 1,
        "why": "Converting glucose to starch delays its use, while respiring it releases the "
               "energy stored in it straight away.",
    },
    {
        "id": "ks4-uses-of-glucose-h09",
        "subtopic_slug": "uses-of-glucose",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why removing all nitrate from a plant's soil affects its protein "
               "content long before it affects its starch content.",
        "options": [
            "Starch is made from nitrate rather than glucose, so it is unaffected when "
            "nitrate runs out",
            "Protein is not affected by nitrate, just by the supply of glucose",
            "Starch needs only the glucose the plant already makes; protein needs a fresh "
            "nitrate supply too",
            "Starch and protein are both built entirely from nitrate, with glucose "
            "playing no part",
        ],
        "correct_index": 2,
        "why": "Starch synthesis draws on glucose alone, which photosynthesis keeps "
               "supplying, but protein synthesis also needs an ongoing nitrate supply.",
    },
    {
        "id": "ks4-uses-of-glucose-h10",
        "subtopic_slug": "uses-of-glucose",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A gardener notices that nitrate fertiliser increases leaf growth far more "
               "than it increases root starch storage. Suggest why.",
        "options": [
            "Nitrate fertiliser converts stored starch directly into leaf tissue, "
            "skipping the usual step of respiring it for energy along the way",
            "Extra nitrate reduces the amount of starch a root can hold too",
            "Nitrate fertiliser has an identical effect on every part of the plant",
            "Extra nitrate lets more protein be built for new leaf growth, but does not "
            "add extra glucose for starch",
        ],
        "correct_index": 3,
        "why": "Nitrate raises how much protein a plant can build for new growth, but it "
               "does not increase the glucose supply that determines how much starch is "
               "stored.",
    },
    {
        "id": "ks4-uses-of-glucose-h11",
        "subtopic_slug": "uses-of-glucose",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Determine the percentage of a plant's daily glucose production that is "
               "respired directly, if it makes 180 g of glucose and respires 63 g of it.",
        "options": [
            "35%",
            "63%",
            "18%",
            "65%",
        ],
        "correct_index": 0,
        "why": "63 out of 180 g is 63 / 180 x 100 = 35% of the day's glucose production.",
    },
    {
        "id": "ks4-uses-of-glucose-h12",
        "subtopic_slug": "uses-of-glucose",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Predict how a plant's use of glucose would change if its rate of "
               "photosynthesis suddenly doubled, but its nitrate supply stayed exactly the "
               "same, and explain.",
        "options": [
            "It would make twice as much protein, since glucose is the main thing protein "
            "synthesis needs, regardless of whether enough nitrogen is available to build "
            "it with",
            "It would store more glucose as starch and lipids, since protein production "
            "is capped by the fixed nitrate supply",
            "The plant would stop making starch altogether, putting everything into "
            "protein instead",
            "Nothing would change, since doubling photosynthesis has no effect on how "
            "glucose is used",
        ],
        "correct_index": 1,
        "why": "With protein production limited by the fixed nitrate supply, the extra "
               "glucose has to go into starch, cellulose or lipid instead.",
    },
    {
        "id": "ks4-uses-of-glucose-h13",
        "subtopic_slug": "uses-of-glucose",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a starch grain inside a chloroplast does not draw water into the "
               "cell by osmosis, while the same mass of glucose would.",
        "options": [
            "Starch dissolves in water just as easily as glucose does, so it draws in the "
            "same amount of water by osmosis",
            "Osmosis moves water out of a cell, not into one, regardless of what is "
            "stored inside it",
            "Starch is insoluble, so it has no effect on the cell's water potential, "
            "unlike dissolved glucose",
            "A chloroplast has no membrane for water to cross by osmosis in the first "
            "place",
        ],
        "correct_index": 2,
        "why": "Because starch is insoluble it cannot lower the water potential inside the "
               "cell the way dissolved glucose would, so it draws in no extra water.",
    },
    {
        "id": "ks4-uses-of-glucose-h14",
        "subtopic_slug": "uses-of-glucose",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A crop is bred to store more of its seed glucose as oil rather than starch. "
               "Suggest one advantage and one disadvantage of this change for a farmer.",
        "options": [
            "The seeds germinate faster in every soil type, with no disadvantage worth "
            "noting, a claim that ignores the real cost of processing oil after harvest",
            "The seeds become completely inedible, but store for decades without decay",
            "The seeds lose all of their stored energy, but weigh noticeably less as a "
            "result",
            "The seeds pack more energy per gram, but oil is more costly to extract and "
            "process than starch",
        ],
        "correct_index": 3,
        "why": "Oil's higher energy density is an advantage for storage, but extracting and "
               "processing oil is typically more demanding than working with starch.",
    },
    {
        "id": "ks4-uses-of-glucose-h15",
        "subtopic_slug": "uses-of-glucose",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate the claim that cellulose is 'wasted' glucose, since a plant cannot "
               "get energy back from its own cell walls.",
        "options": [
            "It is wrong; cellulose's structural support is essential, even though its "
            "glucose is not recovered as energy",
            "It is correct; a plant gains nothing worthwhile from having cellulose in its "
            "cell walls, when in reality its structural role makes it far from worthless",
            "It is correct, because cellulose is toxic to the very plant that makes it",
            "It is wrong; cellulose is broken back down into glucose overnight",
        ],
        "correct_index": 0,
        "why": "Cellulose gives a plant the structural support it could not survive without, "
               "which is a real benefit even though the glucose in it is not recovered as "
               "energy.",
    },
    {
        "id": "ks4-uses-of-glucose-h16",
        "subtopic_slug": "uses-of-glucose",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A plant makes 175 g of glucose and ends the day with 48 g stored as starch, "
               "having used the rest in respiration and growth. Determine how much glucose "
               "was used in respiration and growth combined.",
        "options": [
            "48 g",
            "127 g",
            "223 g",
            "175 g",
        ],
        "correct_index": 1,
        "why": "175 g made minus 48 g stored leaves 127 g used for respiration and growth "
               "combined.",
    },
    {
        "id": "ks4-uses-of-glucose-h17",
        "subtopic_slug": "uses-of-glucose",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a plant deprived of nitrate for several weeks gradually shows "
               "yellowing leaves and stunted growth, rather than dying immediately with no "
               "protein at all.",
        "options": [
            "The plant instantly switches to making all of its protein from glucose "
            "alone, which would in fact require making entirely new protein from scratch",
            "Yellowing and stunted growth have nothing to do with the nitrate supply",
            "Nitrogen already stored in existing proteins can be reused as the plant "
            "slowly runs short",
            "The plant makes new nitrate itself once its external supply is exhausted",
        ],
        "correct_index": 2,
        "why": "A plant can redistribute nitrogen from existing tissues for a time, so the "
               "effects of nitrate loss build up gradually rather than striking all at once.",
    },
    {
        "id": "ks4-uses-of-glucose-h18",
        "subtopic_slug": "uses-of-glucose",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare the immediate usefulness to a cell of a molecule of starch with the "
               "immediate usefulness of a molecule of glucose.",
        "options": [
            "Starch can be respired straight away; glucose must first be converted into "
            "starch, exactly as if no conversion step were needed at all",
            "Both can be respired immediately, with no real difference between them",
            "Neither molecule can ever be respired by a plant cell",
            "Glucose can be respired straight away; starch must first be broken back down "
            "into glucose",
        ],
        "correct_index": 3,
        "why": "Respiration uses glucose directly, so stored starch has an extra conversion "
               "step before its energy becomes available.",
    },
    {
        "id": "ks4-uses-of-glucose-h19",
        "subtopic_slug": "uses-of-glucose",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a plant treated with a poison that specifically blocks active "
               "transport would still be able to photosynthesise, yet fail to grow well.",
        "options": [
            "Photosynthesis needs no active transport, but taking up enough nitrate for "
            "growth does",
            "The poison would stop light reaching the chloroplasts directly, halting "
            "photosynthesis too",
            "Active transport supplies the carbon dioxide photosynthesis needs, so "
            "blocking it would stop both",
            "The poison converts all of the plant's glucose into starch immediately",
        ],
        "correct_index": 0,
        "why": "Photosynthesis runs on diffusion of CO2 and light absorption, neither of "
               "which needs active transport, but nitrate uptake for growth does.",
    },
    {
        "id": "ks4-uses-of-glucose-h20",
        "subtopic_slug": "uses-of-glucose",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Determine the mass of glucose used to make cellulose in a day, if a plant "
               "makes 108 g of glucose, respires 46 g, stores 17 g as starch, and puts the "
               "entire remainder into cellulose.",
        "options": [
            "17 g",
            "45 g",
            "46 g",
            "63 g",
        ],
        "correct_index": 1,
        "why": "46 + 17 = 63 g accounted for, leaving 108 - 63 = 45 g for cellulose.",
    },
    {
        "id": "ks4-uses-of-glucose-h21",
        "subtopic_slug": "uses-of-glucose",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate the claim that a plant growing in bright light with plenty of CO2, "
               "but with no nitrate at all, will still grow just as tall as a "
               "well-fertilised plant.",
        "options": [
            "It is correct; height depends on the rate of photosynthesis, not on nitrate "
            "supply",
            "It is correct, provided the plant is also given extra carbon dioxide to "
            "compensate",
            "It is wrong; without nitrate the plant cannot build enough new protein to "
            "support the same growth",
            "It is wrong; without nitrate a plant cannot photosynthesise properly, so it "
            "would not grow",
        ],
        "correct_index": 2,
        "why": "Growth depends on building new protein as well as making glucose, so a "
               "nitrate shortage limits height even with bright light and plentiful CO2.",
    },
    {
        "id": "ks4-uses-of-glucose-h22",
        "subtopic_slug": "uses-of-glucose",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why oil is favoured over starch as a storage molecule in seeds that "
               "must be light enough to be carried by the wind.",
        "options": [
            "Oil is heavier than starch for the same stored energy, slowing the fall",
            "Starch cannot be stored in a seed, regardless of the seed's method of "
            "dispersal",
            "Oil evaporates slowly during flight, which is what carries the seed further "
            "on the wind",
            "Oil stores more energy for a given mass, so less of it is needed for the "
            "same energy reserve",
        ],
        "correct_index": 3,
        "why": "A lighter seed travels further on the wind, and packing the same energy "
               "reserve into oil rather than starch keeps the seed's mass down.",
    },
    {
        "id": "ks4-uses-of-glucose-h23",
        "subtopic_slug": "uses-of-glucose",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A plant is treated with a poison that specifically blocks active transport. "
               "Predict the effect on its uptake of nitrate ions, and explain.",
        "options": [
            "Nitrate uptake would fall sharply, since it depends on active transport "
            "against a concentration gradient",
            "Nitrate uptake would rise, since the poison forces more diffusion of nitrate "
            "into the roots",
            "Nitrate uptake would be unaffected, since nitrate enters roots by diffusion "
            "alone",
            "Nitrate uptake would stop if the poison also blocked the plant's "
            "photosynthesis",
        ],
        "correct_index": 0,
        "why": "Nitrate is normally absorbed against its concentration gradient by active "
               "transport, so blocking that process cuts uptake sharply.",
    },
    {
        "id": "ks4-uses-of-glucose-h24",
        "subtopic_slug": "uses-of-glucose",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare how a plant's glucose is allocated during a week of rapid leaf "
               "growth with how it is allocated during a week of seed production.",
        "options": [
            "Both weeks allocate glucose identically, since growth looks the same in a "
            "plant either way",
            "Leaf growth favours protein and cellulose; seed production shifts more "
            "glucose into lipid and starch storage",
            "Leaf growth stores almost everything as starch; seed production respires "
            "almost everything instead",
            "Seed production makes little use of glucose, relying mostly on nitrate "
            "instead",
        ],
        "correct_index": 1,
        "why": "Growing leaves need protein for new cells and cellulose for new walls, while "
               "a seed's priority shifts towards building a dense, storable energy reserve.",
    },
    {
        "id": "ks4-uses-of-glucose-h25",
        "subtopic_slug": "uses-of-glucose",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Determine the mass of glucose converted into starch, if a plant makes 225 g "
               "of glucose, respires 99 g, and puts 41 g into cellulose and protein "
               "together, storing everything else as starch.",
        "options": [
            "140 g",
            "99 g",
            "85 g",
            "126 g",
        ],
        "correct_index": 2,
        "why": "99 + 41 = 140 g accounted for, leaving 225 - 140 = 85 g stored as starch.",
    },
    {
        "id": "ks4-uses-of-glucose-h26",
        "subtopic_slug": "uses-of-glucose",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student argues that because starch and cellulose are both polymers of "
               "glucose, a plant could survive on cellulose as an energy store just as it "
               "does on starch. Evaluate this argument.",
        "options": [
            "It is correct; cellulose and starch are broken down by exactly the same "
            "enzymes at exactly the same rate",
            "It is correct, since any polymer of glucose can be respired directly without "
            "being broken down first",
            "It is wrong; cellulose contains far less glucose than starch does",
            "It is wrong; cellulose's structure resists the breakdown that would release "
            "its glucose again",
        ],
        "correct_index": 3,
        "why": "Cellulose's tightly bonded structure is what gives cell walls their "
               "strength, and that same structure makes it very hard to break back down into "
               "usable glucose.",
    },
]
