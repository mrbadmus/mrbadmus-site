"""Biology · Organisation — the MRB-338 expansion of nine BASE subtopics.

Covers `principles-of-organisation`, `heart-blood-vessels`, `blood`,
`coronary-heart-disease`, `health-disease`, `cancer`, `plant-tissues`,
`transpiration` and `translocation`. (`digestive-system` and `enzymes` were
already at target and are expanded in their own z338 files.)

Every row here is BASE — a Foundation Combined class sits all of it — so
nothing reaches into the Higher extension or Triple-only material. The
original twelve rows per subtopic in `organisation.py` are read here as the
floor, not the ceiling: this file goes wider across each subtopic's own
material — named structures, the tissue-versus-organ test applied to new
examples, risk-factor reasoning, comparison and evaluation — rather than
asking any existing fact a second time in new words. No `quiz` entry or
`fifas` worked example from `all_subtopics_biology.py` is reproduced.
"""

TOPIC = "organisation"
SUBJECT = "biology"

QUESTIONS = [
    # ══════════════════════════════════════════════════════════════════
    # principles-of-organisation · e05-e12, s05-s26, h05-h26
    # ══════════════════════════════════════════════════════════════════
    {
        "id": "ks4-principles-of-organisation-e05",
        "subtopic_slug": "principles-of-organisation",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what a cell is.",
        "options": [
            "The smallest unit of a living organism able to carry out the processes of life",
            "A group of similar cells all working together to carry out one single function",
            "A structure built from several different types of tissue",
            "A complete individual made up of many organ systems",
        ],
        "correct_index": 0,
        "why": "A cell is the basic building block of life; tissues, organs "
               "and organisms are all built upwards from cells.",
    },
    {
        "id": "ks4-principles-of-organisation-e06",
        "subtopic_slug": "principles-of-organisation",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Identify the type of tissue that contracts and relaxes to "
                "produce movement.",
        "options": [
            "Epithelial tissue",
            "Muscle tissue",
            "Glandular tissue",
            "Nervous tissue",
        ],
        "correct_index": 1,
        "why": "Muscle tissue is made of cells specialised to contract, "
               "which is what produces movement in the body.",
    },
    {
        "id": "ks4-principles-of-organisation-e07",
        "subtopic_slug": "principles-of-organisation",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Identify the type of tissue that forms a thin lining over "
                "a body surface, such as the gut or the airways.",
        "options": [
            "Muscle tissue",
            "Nervous tissue",
            "Epithelial tissue",
            "Mesophyll tissue",
        ],
        "correct_index": 2,
        "why": "Epithelial tissue is made of thin cells that line surfaces "
               "inside and outside the body.",
    },
    {
        "id": "ks4-principles-of-organisation-e08",
        "subtopic_slug": "principles-of-organisation",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Identify the type of tissue made of cells that carry "
                "electrical impulses around the body.",
        "options": [
            "Glandular tissue",
            "Epithelial tissue",
            "Xylem tissue",
            "Nervous tissue",
        ],
        "correct_index": 3,
        "why": "Nervous tissue is made of neurones, which are specialised "
               "to carry electrical impulses.",
    },
    {
        "id": "ks4-principles-of-organisation-e09",
        "subtopic_slug": "principles-of-organisation",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Identify the plant tissue whose cells are packed with "
                "chloroplasts for photosynthesis.",
        "options": [
            "Mesophyll tissue",
            "Xylem tissue",
            "Phloem tissue",
            "Epidermal tissue",
        ],
        "correct_index": 0,
        "why": "Mesophyll cells are packed with chloroplasts, which is what "
               "makes them the main photosynthesising tissue.",
    },
    {
        "id": "ks4-principles-of-organisation-e10",
        "subtopic_slug": "principles-of-organisation",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the organ system made up of the heart, blood vessels "
                "and blood, working together.",
        "options": [
            "The respiratory system",
            "The circulatory system",
            "The nervous system",
            "The digestive system",
        ],
        "correct_index": 1,
        "why": "The heart, blood vessels and blood are the organs of the "
               "circulatory system, which transports substances round the "
               "body.",
    },
    {
        "id": "ks4-principles-of-organisation-e11",
        "subtopic_slug": "principles-of-organisation",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the main function of the respiratory system.",
        "options": [
            "Breaking down food into small, soluble molecules",
            "Detecting stimuli and coordinating a response",
            "Exchanging oxygen and carbon dioxide with the air",
            "Transporting oxygen and nutrients to every cell",
        ],
        "correct_index": 2,
        "why": "The lungs, trachea, bronchi and diaphragm work together to "
               "exchange gases with the air — the job of the respiratory "
               "system.",
    },
    {
        "id": "ks4-principles-of-organisation-e12",
        "subtopic_slug": "principles-of-organisation",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what is meant by an organism.",
        "options": [
            "A group of several organs working together for one major function in the body",
            "A group of similar cells that all carry out the same job",
            "A structure made from two or more different tissue types",
            "A complete living individual, with all its organ systems working together",
        ],
        "correct_index": 3,
        "why": "An organism is the whole living individual — the level "
               "built from every organ system working together.",
    },
    {
        "id": "ks4-principles-of-organisation-s05",
        "subtopic_slug": "principles-of-organisation",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "The pancreas contains glandular tissue that produces "
                "enzymes, together with connective tissue and blood "
                "vessels. Determine its level of organisation.",
        "options": [
            "An organ, because it combines several different tissue types in one structure",
            "A tissue, because every single cell in the pancreas produces the same enzyme",
            "An organ system, because the pancreas works with the small intestine",
            "An organism, because the pancreas carries out an essential process",
        ],
        "correct_index": 0,
        "why": "Several different tissues working together in one "
               "structure is the definition of an organ.",
    },
    {
        "id": "ks4-principles-of-organisation-s06",
        "subtopic_slug": "principles-of-organisation",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Blood contains red blood cells, white blood cells and "
                "platelets suspended in plasma. Explain why blood is still "
                "classified as one tissue rather than as an organ.",
        "options": [
            "Blood cannot be classified at any level of organisation at all, because it flows and never stays fixed in one particular shape",
            "Blood is a single tissue because it does not combine several different tissues, even though it holds several types of cell",
            "Blood is classified as a tissue only because plasma is the one single component of it that counts as being genuinely alive",
            "Blood is a tissue only because none of its cells contain a nucleus",
        ],
        "correct_index": 1,
        "why": "The test for an organ is several different tissues "
               "combined, not several different cell types — blood is one "
               "tissue however many kinds of cell it carries.",
    },
    {
        "id": "ks4-principles-of-organisation-s07",
        "subtopic_slug": "principles-of-organisation",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A root contains an outer epidermis, a core of vascular "
                "tissue and packing tissue between them. Determine its "
                "level of organisation.",
        "options": [
            "A tissue, because every cell in the root absorbs water in the same way",
            "An organ system, because the root works together with the stem and leaves",
            "An organ, because it combines at least two different types of tissue",
            "An organism, because the root can survive on its own if it is cut away",
        ],
        "correct_index": 2,
        "why": "The root combines epidermis, vascular tissue and packing "
               "tissue — several different tissues together make it an "
               "organ.",
    },
    {
        "id": "ks4-principles-of-organisation-s08",
        "subtopic_slug": "principles-of-organisation",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "The brain, spinal cord and nerves work together to detect "
                "stimuli and coordinate a response. Determine the level of "
                "organisation this represents.",
        "options": [
            "An organ, because the brain alone is responsible for the whole response",
            "A tissue, because nervous tissue is found in each of these three structures",
            "An organism, because coordinating a response keeps the whole body alive",
            "An organ system, because several organs are working together for one function",
        ],
        "correct_index": 3,
        "why": "Several organs — the brain, spinal cord and nerves — "
               "working together for one function is an organ system.",
    },
    {
        "id": "ks4-principles-of-organisation-s09",
        "subtopic_slug": "principles-of-organisation",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "The digestive system and the respiratory system are both "
                "organ systems, but they are built from different organs. "
                "Explain what makes them the same level of organisation.",
        "options": [
            "Both are groups of different organs working together for one major function",
            "Both happen to contain exactly the same total number of organs as one another",
            "Both are actually single organs that simply carry out two separate functions at once",
            "Both are made of only one type of tissue, repeated many times",
        ],
        "correct_index": 0,
        "why": "What makes something an organ system is several organs "
               "working together for one function — true of both, whatever "
               "organs they actually contain.",
    },
    {
        "id": "ks4-principles-of-organisation-s10",
        "subtopic_slug": "principles-of-organisation",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A single neurone is a cell. Explain the difference in level "
                "of organisation between a neurone and a nerve made of many "
                "neurones bundled with connective tissue.",
        "options": [
            "There is no real difference at all — both a neurone and a single nerve are simply thought of as cells",
            "A neurone is a cell, but a nerve combines nerve cells with another tissue, making it an organ",
            "A neurone is actually classed as a tissue, and a nerve is the whole organ system that it belongs to",
            "A nerve is simply one single larger neurone, formed by several smaller neurones joining together",
        ],
        "correct_index": 1,
        "why": "A neurone is one cell; a nerve bundles many neurones "
               "together with connective tissue, so it combines more than "
               "one tissue type.",
    },
    {
        "id": "ks4-principles-of-organisation-s11",
        "subtopic_slug": "principles-of-organisation",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A flower contains protective tissue, tissue that produces "
                "pollen and vascular tissue supplying it with water and "
                "sugar. Determine its level of organisation.",
        "options": [
            "A tissue, because every structure inside a flower carries out reproduction",
            "An organ system, because the flower works with the roots and leaves",
            "An organ, because it is built from several different tissues",
            "An organism, because the flower can produce a new individual",
        ],
        "correct_index": 2,
        "why": "Combining several different tissues in one structure — "
               "protective, reproductive and vascular — makes the flower "
               "an organ.",
    },
    {
        "id": "ks4-principles-of-organisation-s12",
        "subtopic_slug": "principles-of-organisation",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Skeletal muscle in the arm and cardiac muscle in the heart "
                "look and behave differently. Explain why both are still "
                "classified at the same level of organisation.",
        "options": [
            "They are not at the same level — cardiac muscle is an organ and skeletal muscle is a tissue",
            "They are the same level only because both muscles are found in humans",
            "They are the same level because both types contain the exact same proteins",
            "Both are groups of similar cells doing one job, which is the definition of a tissue",
        ],
        "correct_index": 3,
        "why": "Wherever it is found, muscle is a tissue because it is a "
               "group of similar cells specialised for one function — "
               "contraction.",
    },
    {
        "id": "ks4-principles-of-organisation-s13",
        "subtopic_slug": "principles-of-organisation",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Epithelial tissue lines the gut in one part of the body "
                "and the airways in another. Explain why both examples are "
                "classified at the same level of organisation.",
        "options": [
            "Both are tissues, because in each case it is one type of cell doing one job",
            "Both are organs, because lining a surface is a complete function on its own",
            "They are different levels — the gut lining is a tissue and the airway lining is an organ",
            "Both are organ systems, because lining tissue is found throughout the whole body",
        ],
        "correct_index": 0,
        "why": "Location does not change the level — epithelial tissue is "
               "one cell type doing one job wherever it lines a surface.",
    },
    {
        "id": "ks4-principles-of-organisation-s14",
        "subtopic_slug": "principles-of-organisation",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A root hair cell and a xylem cell come from the same plant "
                "and contain identical DNA. Explain why they look and "
                "function so differently.",
        "options": [
            "The root hair cell has gradually lost some of its original DNA as it specialised for its role",
            "Different genes are switched on in each cell type, giving each its own structure",
            "The two cells were produced by two separate parts of the same seed",
            "Xylem cells gain some extra DNA that root hair cells never manage to develop at all",
        ],
        "correct_index": 1,
        "why": "All the plant's cells share the same DNA; specialisation "
               "comes from which genes are switched on, not from a "
               "different genetic code.",
    },
    {
        "id": "ks4-principles-of-organisation-s15",
        "subtopic_slug": "principles-of-organisation",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A neurone and an epithelial cell from the same person "
                "contain identical DNA. Explain why a neurone can be over "
                "a metre long while the epithelial cell is small and flat.",
        "options": [
            "The neurone simply divides many more times than the epithelial cell does during early growth",
            "The epithelial cell actually has fewer chromosomes in its nucleus than the neurone does",
            "Different genes are active in each cell type, producing a different shape for each job",
            "The neurone simply absorbs extra material from nearby cells as the whole body continues to grow",
        ],
        "correct_index": 2,
        "why": "Specialised shape comes from which genes a cell switches "
               "on, not from a different amount of DNA or extra material "
               "taken from elsewhere.",
    },
    {
        "id": "ks4-principles-of-organisation-s16",
        "subtopic_slug": "principles-of-organisation",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Put these three structures in order from simplest to most "
                "complex: a xylem vessel, the stem, a mesophyll cell.",
        "options": [
            "The stem, a xylem vessel, a mesophyll cell",
            "A xylem vessel, the stem, a mesophyll cell",
            "A mesophyll cell, the stem, a xylem vessel",
            "A mesophyll cell, a xylem vessel, the stem",
        ],
        "correct_index": 3,
        "why": "A mesophyll cell is a single cell, a xylem vessel is a "
               "tissue, and the stem is an organ built from several "
               "tissues.",
    },
    {
        "id": "ks4-principles-of-organisation-s17",
        "subtopic_slug": "principles-of-organisation",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A large sheet of muscle tissue and a tiny gland both "
                "contain more than one cell. Explain which of the two is "
                "an organ, and why.",
        "options": [
            "The gland, if it combines glandular tissue with connective tissue and blood vessels",
            "The sheet of muscle, simply because it takes up much more physical space than the tiny gland does",
            "Both are organs, since both contain thousands of cells",
            "Neither is an organ, since neither structure counts as a complete and separate whole body part",
        ],
        "correct_index": 0,
        "why": "Size and cell number are not the test — an organ is "
               "defined by combining different tissue types, whichever "
               "structure is bigger.",
    },
    {
        "id": "ks4-principles-of-organisation-s18",
        "subtopic_slug": "principles-of-organisation",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why removing the blood vessels from the "
                "circulatory system would stop it working as an organ "
                "system, even if the heart and blood were untouched.",
        "options": [
            "The heart would then count as a tissue instead of an organ",
            "An organ system needs its organs working together, and one organ alone cannot carry out the whole function",
            "Blood cannot flow through the body under any circumstances at all without the continuous pumping action of the heart",
            "The blood itself would stop being classified as a tissue",
        ],
        "correct_index": 1,
        "why": "An organ system's function depends on all its organs "
               "working together — losing one breaks the system even if "
               "the others are fine.",
    },
    {
        "id": "ks4-principles-of-organisation-s19",
        "subtopic_slug": "principles-of-organisation",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "The diaphragm is built mainly from muscle, but also "
                "contains connective tissue and its own blood supply. "
                "Explain why it is classed as an organ rather than as "
                "muscle tissue alone.",
        "options": [
            "It is a tissue, because muscle is the tissue type that makes up most of it",
            "It is an organ system, because it works together with the lungs",
            "It is an organ, because it combines muscle tissue with other tissue types",
            "It is an organism, because it can contract without any signal from the brain",
        ],
        "correct_index": 2,
        "why": "Even though muscle dominates the diaphragm, the extra "
               "tissues it contains make it an organ rather than a tissue "
               "on its own.",
    },
    {
        "id": "ks4-principles-of-organisation-s20",
        "subtopic_slug": "principles-of-organisation",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "The spinal cord contains nervous tissue, connective tissue "
                "and blood vessels bundled together. Determine its level "
                "of organisation.",
        "options": [
            "A tissue, because nervous tissue is what carries out its main job",
            "An organ system, because it connects the brain to every nerve in the body",
            "An organism, because it is essential for the body to stay alive",
            "An organ, because it combines nervous tissue with other tissue types",
        ],
        "correct_index": 3,
        "why": "Combining nervous tissue with connective tissue and blood "
               "vessels in one structure makes the spinal cord an organ.",
    },
    {
        "id": "ks4-principles-of-organisation-s21",
        "subtopic_slug": "principles-of-organisation",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the minimum number of different tissue types a "
                "structure must combine before it can be classified as an "
                "organ.",
        "options": [
            "At least two",
            "Exactly one",
            "At least four",
            "There is no minimum number",
        ],
        "correct_index": 0,
        "why": "An organ is defined as combining several different "
               "tissues, so at least two different types must be present.",
    },
    {
        "id": "ks4-principles-of-organisation-s22",
        "subtopic_slug": "principles-of-organisation",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student says 'the heart is an organ system, because it "
                "contains cardiac muscle, valves and coronary blood "
                "vessels'. Explain the error.",
        "options": [
            "The heart actually contains only one single type of tissue, so it really should be called a tissue",
            "The heart is one organ, because it combines several tissues in one structure, not several organs",
            "The heart is actually correctly called an organ system, since it clearly has more than one moving part",
            "The heart is actually an entire organism, since it can keep on beating outside the body for a short time",
        ],
        "correct_index": 1,
        "why": "An organ system is built from several organs; the heart is "
               "a single organ built from several tissues.",
    },
    {
        "id": "ks4-principles-of-organisation-s23",
        "subtopic_slug": "principles-of-organisation",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare the nervous system and the circulatory system as "
                "organ systems.",
        "options": [
            "The nervous system has no organs; the circulatory system has three organs",
            "Both are single organs, just given two different names for convenience",
            "Both combine several different organs, but each system's organs serve a different function",
            "The circulatory system is only a tissue, while the nervous system is a true organ system",
        ],
        "correct_index": 2,
        "why": "Both are organ systems by definition — several organs "
               "working together — even though the organs and the "
               "function differ completely.",
    },
    {
        "id": "ks4-principles-of-organisation-s24",
        "subtopic_slug": "principles-of-organisation",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A structure is described as containing only neurones and "
                "no other tissue type. Explain why this structure is a "
                "tissue, not an organ.",
        "options": [
            "It is an organ, since neurones alone can generate an electrical impulse",
            "It cannot be classified, since nervous tissue never appears without other tissue in the body",
            "It is an organ system, since neurones connect to many different organs",
            "It is a tissue, because it is built from just one type of cell doing one job",
        ],
        "correct_index": 3,
        "why": "A structure built from only one cell type, whatever job "
               "that cell does, stays at the level of a tissue.",
    },
    {
        "id": "ks4-principles-of-organisation-s25",
        "subtopic_slug": "principles-of-organisation",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a structure with a thousand cells of one type "
                "is not automatically a higher level of organisation than "
                "a structure with ten cells of two different types.",
        "options": [
            "Level of organisation depends on how many different tissue types are combined, not on the total number of cells",
            "Level of organisation always depends on which structure has more cells overall",
            "The structure with more cells is always classified as the organ, no matter which types of cell it actually contains",
            "Neither structure can be classified until an exact cell count is known for both",
        ],
        "correct_index": 0,
        "why": "It is tissue diversity, not cell number, that decides "
               "whether something is a tissue or an organ.",
    },
    {
        "id": "ks4-principles-of-organisation-s26",
        "subtopic_slug": "principles-of-organisation",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "The salivary glands are built almost entirely from one "
                "type of secretory cell. Explain why this makes them "
                "glandular tissue rather than an organ, unlike the "
                "pancreas.",
        "options": [
            "The salivary glands are actually an organ already, built from exactly the same combination of tissues that makes up the pancreas",
            "The salivary glands contain only glandular tissue, while the pancreas also contains connective tissue and blood vessels",
            "The salivary glands are a tissue because saliva is a liquid rather than a solid product",
            "The salivary glands are a tissue because they are smaller in size than the pancreas",
        ],
        "correct_index": 1,
        "why": "The salivary glands are built from glandular tissue alone; "
               "the pancreas combines that tissue with others, which is "
               "what makes the pancreas an organ.",
    },
    {
        "id": "ks4-principles-of-organisation-h05",
        "subtopic_slug": "principles-of-organisation",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Put these four structures in order from simplest to most "
                "complex: the digestive system, a red blood cell, cardiac "
                "muscle, the stomach.",
        "options": [
            "A red blood cell, cardiac muscle, the stomach, the digestive system",
            "Cardiac muscle, a red blood cell, the stomach, the digestive system",
            "The stomach, cardiac muscle, a red blood cell, the digestive system",
            "The digestive system, the stomach, cardiac muscle, a red blood cell",
        ],
        "correct_index": 0,
        "why": "A red blood cell is a cell, cardiac muscle is a tissue, the "
               "stomach is an organ, and the digestive system is the organ "
               "system it belongs to.",
    },
    {
        "id": "ks4-principles-of-organisation-h06",
        "subtopic_slug": "principles-of-organisation",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A mutation stops xylem cells forming properly throughout "
                "a plant. Explain how this fault, starting in cells, can "
                "affect the whole organism.",
        "options": [
            "It cannot spread beyond the cell level, since xylem cells are not part of a tissue",
            "Faulty cells fail to build working xylem tissue, so the whole plant is starved of water",
            "The fault stays contained inside the root, since only roots contain xylem",
            "The organism level repairs the fault automatically, since it is the highest level",
        ],
        "correct_index": 1,
        "why": "Each level is built from the one below, so a fault in "
               "cells is carried up through the tissue and organ levels "
               "to affect the whole organism.",
    },
    {
        "id": "ks4-principles-of-organisation-h07",
        "subtopic_slug": "principles-of-organisation",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate this claim: 'A tissue that keeps growing larger "
                "will eventually become an organ.'",
        "options": [
            "True — an organ is simply any tissue that has grown large enough past a certain critical size",
            "True, but this rule only applies to animal tissues — plant tissues never become organs at all",
            "False — an organ needs different tissue types combined, not one tissue growing bigger",
            "False — a tissue can never grow larger once it has formed",
        ],
        "correct_index": 2,
        "why": "Growth changes size, not tissue diversity — a structure "
               "only becomes an organ once several different tissues are "
               "combined.",
    },
    {
        "id": "ks4-principles-of-organisation-h08",
        "subtopic_slug": "principles-of-organisation",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain the relationship between cardiac muscle tissue "
                "and the heart, in terms of levels of organisation.",
        "options": [
            "Cardiac muscle tissue and the heart are simply two different names given to the very same level of organisation",
            "The heart is a tissue that is used to build cardiac muscle",
            "Cardiac muscle tissue is an organ system that the heart belongs to",
            "Cardiac muscle tissue is one of several tissues combined to build the heart, an organ",
        ],
        "correct_index": 3,
        "why": "The heart, an organ, is built by combining cardiac muscle "
               "tissue with valve tissue and blood vessels.",
    },
    {
        "id": "ks4-principles-of-organisation-h09",
        "subtopic_slug": "principles-of-organisation",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate this claim: 'The digestive system and the "
                "circulatory system never need to work together.'",
        "options": [
            "False — digested food is absorbed into the blood, so the two systems depend on each other",
            "True — each and every organ system works completely independently of every other system in the body",
            "True — the digestive system never actually releases anything whatsoever into the bloodstream",
            "False, but only because both of these systems happen to share exactly the same set of organs",
        ],
        "correct_index": 0,
        "why": "Nutrients absorbed by the digestive system are carried "
               "onward by the circulatory system, so the two organ "
               "systems depend on one another.",
    },
    {
        "id": "ks4-principles-of-organisation-h10",
        "subtopic_slug": "principles-of-organisation",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "The epithelial tissue lining the airway is severely "
                "damaged by disease. Predict the effect on the respiratory "
                "system as a whole, and explain your reasoning.",
        "options": [
            "None at all — epithelial tissue plays absolutely no part in how the lungs or airway actually function",
            "The airway organ is impaired, which can reduce how well the whole respiratory system exchanges gases",
            "Only the tissue level is ever affected, since damage of this kind never manages to reach the organ or system level",
            "The digestive system is affected instead of the respiratory one, since airway tissue is somehow shared between the two",
        ],
        "correct_index": 1,
        "why": "Damage to a tissue impairs the organ it is part of, which "
               "in turn can impair the organ system that organ belongs to.",
    },
    {
        "id": "ks4-principles-of-organisation-h11",
        "subtopic_slug": "principles-of-organisation",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Xylem tissue and phloem tissue run side by side through a "
                "leaf as a vascular bundle. Compare their level of "
                "organisation with the level of the leaf itself.",
        "options": [
            "Xylem and phloem are actually both separate organs; the leaf is merely a tissue built from combining them",
            "Xylem and phloem are the same tissue; the leaf is an organ system",
            "Xylem and phloem are each a single tissue; the leaf is an organ combining them with others",
            "Xylem and phloem are actually whole organ systems; the leaf is simply the organism that they belong to",
        ],
        "correct_index": 2,
        "why": "Xylem and phloem stay at the tissue level even side by "
               "side; it is the leaf, combining them with mesophyll and "
               "epidermis, that reaches organ level.",
    },
    {
        "id": "ks4-principles-of-organisation-h12",
        "subtopic_slug": "principles-of-organisation",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why a person can survive with one damaged organ, "
                "such as a single damaged kidney, but cannot survive with "
                "an entire organ system failing.",
        "options": [
            "A damaged organ always repairs itself automatically over time, but a damaged organ system never manages to",
            "Damage to one organ always destroys every organ system in the body at once",
            "An organ system is smaller than an organ, so its failure affects less of the body",
            "An organ system's whole function is lost when it fails, while a single organ can sometimes be compensated for",
        ],
        "correct_index": 3,
        "why": "The body often has some redundancy at the organ level (a "
               "second kidney, for example), but if a whole organ system "
               "fails there is nothing left to carry out that function.",
    },
    {
        "id": "ks4-principles-of-organisation-h13",
        "subtopic_slug": "principles-of-organisation",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student argues that because red blood cells and "
                "neurones develop from the same fertilised egg, they must "
                "be identical in structure. Explain the flaw in this "
                "argument.",
        "options": [
            "Different genes are switched on as the cells specialise, so cells from the same origin can end up very different",
            "The argument is correct — cells from the same fertilised egg are always identical",
            "Red blood cells and neurones actually develop from two separate fertilised eggs",
            "Neurones lose their original DNA as they specialise into their final adult form",
        ],
        "correct_index": 0,
        "why": "Sharing an origin only means sharing the same DNA; "
               "specialisation depends on which genes are switched on, so "
               "structure can still differ completely.",
    },
    {
        "id": "ks4-principles-of-organisation-h14",
        "subtopic_slug": "principles-of-organisation",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare the level of organisation of a leaf with the level "
                "of organisation of the whole potato plant it grows on.",
        "options": [
            "Both are at exactly the same level of organisation, since both structures contain xylem and phloem tissue",
            "The leaf is an organ; the whole plant is an organism built from many organs and organ systems",
            "The leaf is actually an organ system in its own right; the whole plant is simply a single large organ",
            "The leaf is an organism in its own right, separate from the rest of the plant",
        ],
        "correct_index": 1,
        "why": "A leaf combines several tissues to reach organ level, but "
               "the whole plant — roots, stem, leaves and flowers "
               "together — is the organism.",
    },
    {
        "id": "ks4-principles-of-organisation-h15",
        "subtopic_slug": "principles-of-organisation",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare a root hair cell with the whole root it is part "
                "of, in terms of level of organisation and function.",
        "options": [
            "Both of them are already organs, since both are directly involved in absorbing water from the surrounding soil",
            "The root hair cell is actually a tissue all on its own; the root itself is a whole separate organ system",
            "The root hair cell is a single specialised cell; the root is an organ built from several tissues",
            "The root hair cell and the root are really just the same single structure, viewed at two different sizes",
        ],
        "correct_index": 2,
        "why": "A root hair cell is one specialised cell that increases "
               "surface area for absorption; the root itself combines "
               "that cell's tissue with vascular and packing tissue to "
               "reach organ level.",
    },
    {
        "id": "ks4-principles-of-organisation-h16",
        "subtopic_slug": "principles-of-organisation",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate this claim: 'An organ system always contains "
                "exactly one organ.'",
        "options": [
            "True — an organ system is just another name for a single large organ",
            "True, except for the circulatory system, which is the only system with more than one organ",
            "False, but only because the digestive system is a special exception",
            "False — an organ system is defined as several organs working together, always more than one",
        ],
        "correct_index": 3,
        "why": "By definition an organ system combines several organs — "
               "the respiratory system alone needs the lungs, trachea and "
               "diaphragm.",
    },
    {
        "id": "ks4-principles-of-organisation-h17",
        "subtopic_slug": "principles-of-organisation",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A mutation stops every cell in a developing embryo from "
                "specialising, so all the cells stay generic. Predict what "
                "this would do to the levels of organisation that could "
                "form.",
        "options": [
            "No tissues could form, because a tissue needs similar specialised cells sharing one function",
            "Tissues would still form normally, since specialisation only affects organs",
            "Only the organ system level would fail to form, leaving tissues and organs intact",
            "The organism would still develop normally, since specialisation is not required for survival",
        ],
        "correct_index": 0,
        "why": "A tissue is defined as similar cells specialised for one "
               "function; without specialisation there is nothing to "
               "group into a tissue, so no higher level could form "
               "either.",
    },
    {
        "id": "ks4-principles-of-organisation-h18",
        "subtopic_slug": "principles-of-organisation",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "The nervous system and the respiratory system carry out "
                "completely different functions. Explain what they still "
                "have in common structurally.",
        "options": [
            "Both of them are really just single organs rather than true, fully-formed organ systems at all",
            "Both are built by combining several different organs to serve one overall function",
            "Both of them happen to contain exactly the same three organs, simply used for two different purposes",
            "Neither system is actually built from tissues, unlike every single other organ system in the body",
        ],
        "correct_index": 1,
        "why": "Whatever their function, every organ system shares the "
               "same structure — several organs working together — which "
               "is what puts them at the same level.",
    },
    {
        "id": "ks4-principles-of-organisation-h19",
        "subtopic_slug": "principles-of-organisation",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student says 'a single muscle cell can be called muscle "
                "tissue'. Evaluate this statement.",
        "options": [
            "True — a single specialised cell already counts in full as the tissue that it happens to belong to",
            "True, but this is only the case for muscle cells specifically, unlike every other type of cell",
            "False — a tissue is a group of similar cells, so one cell alone stays at the cell level",
            "False — a single muscle cell already counts as being a complete organ, not merely a tissue at all",
        ],
        "correct_index": 2,
        "why": "A tissue is defined as a group of similar cells; a lone "
               "cell, however specialised, has not yet reached tissue "
               "level.",
    },
    {
        "id": "ks4-principles-of-organisation-h20",
        "subtopic_slug": "principles-of-organisation",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "The pancreas releases digestive enzymes into the gut and "
                "also releases a hormone directly into the blood. Suggest "
                "how a single organ can be involved in two very different "
                "jobs like this.",
        "options": [
            "It cannot really be one organ — it must actually be two separate organs sharing a name",
            "The hormone is released by mistake, as a side effect of producing digestive enzymes",
            "One of the two jobs must be carried out by a different organ altogether",
            "An organ can contain more than one type of tissue, each contributing a different function",
        ],
        "correct_index": 3,
        "why": "An organ's different tissues can each contribute a "
               "different job, so one organ is free to take part in more "
               "than one process in the body.",
    },
    {
        "id": "ks4-principles-of-organisation-h21",
        "subtopic_slug": "principles-of-organisation",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare the effect on the body of losing a single skin "
                "cell with the effect of losing an entire kidney.",
        "options": [
            "Losing one cell barely registers, since it is quickly replaced; losing a whole organ removes a major function outright",
            "Both have an identical effect on the body overall, since both events simply remove a small amount of living tissue from an organism",
            "Losing a single cell is more serious, because cells cannot be replaced once lost",
            "Losing a whole organ has no effect, since the body has an organ system to compensate",
        ],
        "correct_index": 0,
        "why": "The higher the level lost, the greater the disruption — "
               "one cell among billions is nothing like losing an entire "
               "organ's function.",
    },
    {
        "id": "ks4-principles-of-organisation-h22",
        "subtopic_slug": "principles-of-organisation",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student claims that because the organism is the highest "
                "level of organisation, its survival does not really "
                "depend on what happens at the tissue or organ level. "
                "Evaluate this claim.",
        "options": [
            "True — the organism level is entirely independent of anything that happens below it in the hierarchy",
            "False — the organism can only function correctly if its tissues and organs are all working properly",
            "True, but this only applies to plants, since animals depend on their organs while plants never do",
            "False, but only because organisms are actually the simplest level, not the highest",
        ],
        "correct_index": 1,
        "why": "Every level depends on the ones below it functioning "
               "correctly; being 'highest' does not make the organism "
               "independent of its tissues and organs.",
    },
    {
        "id": "ks4-principles-of-organisation-h23",
        "subtopic_slug": "principles-of-organisation",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why a flower, even though it exists only to carry "
                "out reproduction, is classified as an organ rather than "
                "as a single tissue.",
        "options": [
            "It is not really an organ at all — reproduction is always carried out purely at the level of the whole organism",
            "A flower is simply one tissue, because every single cell inside it is involved somehow in making a new plant",
            "A flower combines several different tissues — protective, reproductive and vascular — for one function",
            "A flower is actually an organ system, because it works together closely with the rest of the whole plant",
        ],
        "correct_index": 2,
        "why": "Having one overall function does not limit a structure to "
               "tissue level — the flower reaches organ level because it "
               "combines several different tissues to achieve that "
               "function.",
    },
    {
        "id": "ks4-principles-of-organisation-h24",
        "subtopic_slug": "principles-of-organisation",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Disease destroys the epithelial tissue lining a person's "
                "small intestine. Predict which levels of organisation are "
                "affected, and explain the chain of effects.",
        "options": [
            "Only the cell level is affected, since tissue damage never reaches the organ level",
            "Only the organism level is ever affected by disease, since tissues and organs are always completely unaffected by it",
            "The tissue is destroyed, but this has no further effect on any higher level",
            "The tissue is destroyed, which impairs the intestine as an organ, which can impair the whole digestive system",
        ],
        "correct_index": 3,
        "why": "Damage does not stay contained at one level — a destroyed "
               "tissue impairs the organ it belongs to, and that can "
               "impair the organ system built from it.",
    },
    {
        "id": "ks4-principles-of-organisation-h25",
        "subtopic_slug": "principles-of-organisation",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Two students disagree about whether it makes sense to "
                "compare 'the human circulatory system' directly with "
                "'a single red blood cell'. Evaluate why such a direct "
                "comparison is misleading.",
        "options": [
            "They sit at completely different levels of organisation, so comparing them directly tells you very little",
            "The comparison is actually perfectly fair to make, since both are simply part of the very same organ system",
            "The comparison is misleading only because red blood cells happen to have no nucleus of their own at all",
            "The comparison is misleading only because the circulatory system happens to be found solely in animals, never in plants",
        ],
        "correct_index": 0,
        "why": "An organ system and a single cell are different levels "
               "entirely — comparing them directly ignores everything in "
               "between.",
    },
    {
        "id": "ks4-principles-of-organisation-h26",
        "subtopic_slug": "principles-of-organisation",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why biologists study living things at several "
                "different levels — cell, tissue, organ, organ system, "
                "organism — rather than studying only the whole organism.",
        "options": [
            "Studying only the organism level would give exactly the same information as studying every lower level individually",
            "Each level reveals a mechanism the levels above it cannot show on their own, such as how one damaged cell type explains a disease",
            "The lower levels are only useful for classifying plants, never animals",
            "There is no benefit — the levels exist purely so that biology has more to name and test",
        ],
        "correct_index": 1,
        "why": "A problem often begins at a lower level — a single faulty "
               "cell type, say — and studying that level explains effects "
               "that only show up higher up.",
    },

    # ══════════════════════════════════════════════════════════════════
    # heart-blood-vessels · e05-e12, s05-s26, h05-h26
    # ══════════════════════════════════════════════════════════════════
    {
        "id": "ks4-heart-blood-vessels-e05",
        "subtopic_slug": "heart-blood-vessels",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Identify where the atrioventricular (AV) valves are found "
                "in the heart.",
        "options": [
            "Between the atria and the ventricles",
            "Between the aorta and the pulmonary artery",
            "Between the vena cava and the right atrium",
            "Between the pulmonary vein and the left atrium",
        ],
        "correct_index": 0,
        "why": "The atrioventricular valves sit between each atrium and the "
               "ventricle below it, stopping blood flowing back up.",
    },
    {
        "id": "ks4-heart-blood-vessels-e06",
        "subtopic_slug": "heart-blood-vessels",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Identify where the semilunar valves are found.",
        "options": [
            "Between the left atrium and the right atrium of the heart",
            "In the aorta and the pulmonary artery",
            "Between the vena cava and the pulmonary vein of the heart",
            "Inside the wall of the left ventricle only, not the right",
        ],
        "correct_index": 1,
        "why": "The semilunar valves sit in the aorta and pulmonary artery, "
               "where blood leaves the heart, stopping it flowing back in.",
    },
    {
        "id": "ks4-heart-blood-vessels-e07",
        "subtopic_slug": "heart-blood-vessels",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what causes the 'lub-dub' sound of a heartbeat.",
        "options": [
            "Blood rushing through the aorta at high pressure",
            "Cardiac muscle contracting in the atria and ventricles",
            "The heart valves snapping shut to stop backflow",
            "Air moving in and out of the lungs nearby",
        ],
        "correct_index": 2,
        "why": "Each 'lub' and 'dub' is a set of valves snapping shut as "
               "pressure reverses between chambers.",
    },
    {
        "id": "ks4-heart-blood-vessels-e08",
        "subtopic_slug": "heart-blood-vessels",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the vessel that delivers blood into the left atrium.",
        "options": [
            "The vena cava",
            "The left ventricle",
            "The aorta",
            "The pulmonary vein",
        ],
        "correct_index": 3,
        "why": "The pulmonary vein returns oxygenated blood from the lungs "
               "into the left atrium.",
    },
    {
        "id": "ks4-heart-blood-vessels-e09",
        "subtopic_slug": "heart-blood-vessels",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the vessel that delivers blood into the right atrium.",
        "options": [
            "The vena cava",
            "The pulmonary vein",
            "The right ventricle",
            "The pulmonary artery",
        ],
        "correct_index": 0,
        "why": "The vena cava returns deoxygenated blood from the body into "
               "the right atrium.",
    },
    {
        "id": "ks4-heart-blood-vessels-e10",
        "subtopic_slug": "heart-blood-vessels",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State which blood vessel the coronary arteries branch from.",
        "options": [
            "The pulmonary artery",
            "The aorta",
            "The vena cava",
            "The left ventricle",
        ],
        "correct_index": 1,
        "why": "The coronary arteries branch off the aorta, just after it "
               "leaves the left ventricle.",
    },
    {
        "id": "ks4-heart-blood-vessels-e11",
        "subtopic_slug": "heart-blood-vessels",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the thickness of a capillary wall.",
        "options": [
            "Ten cells thick",
            "Three cells thick",
            "One cell thick",
            "Five cells thick",
        ],
        "correct_index": 2,
        "why": "A capillary wall is a single cell thick, giving the "
               "shortest possible diffusion distance for exchange.",
    },
    {
        "id": "ks4-heart-blood-vessels-e12",
        "subtopic_slug": "heart-blood-vessels",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare the width of the lumen (central channel) in a vein "
                "with that in an artery.",
        "options": [
            "A vein's lumen is much narrower than an artery's",
            "A vein's lumen and an artery's lumen are always identical",
            "A vein has no lumen at all, unlike an artery",
            "A vein's lumen is wider than an artery's",
        ],
        "correct_index": 3,
        "why": "A vein's wider lumen offers less resistance to the slower, "
               "lower-pressure flow it carries.",
    },
    {
        "id": "ks4-heart-blood-vessels-s05",
        "subtopic_slug": "heart-blood-vessels",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why the heart makes a sound each time it beats.",
        "options": [
            "The valves snap shut when pressure reverses, and this creates the sound",
            "The cardiac muscle contracts so forcefully that it vibrates audibly",
            "Blood collides with the walls of the aorta as it is pumped out",
            "Air trapped inside the heart chambers is squeezed out with each beat",
        ],
        "correct_index": 0,
        "why": "The heart sounds come from valves snapping shut, not from "
               "muscle, blood or air movement directly.",
    },
    {
        "id": "ks4-heart-blood-vessels-s06",
        "subtopic_slug": "heart-blood-vessels",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Describe the difference between an atrioventricular valve "
                "and a semilunar valve.",
        "options": [
            "There is no real difference at all; both terms simply describe the exact same single heart structure",
            "An atrioventricular valve lies between atrium and ventricle; a semilunar valve lies where blood exits",
            "An atrioventricular valve is found only in the right side of the heart, never in the left",
            "A semilunar valve only ever closes while the whole heart is resting in between each beat",
        ],
        "correct_index": 1,
        "why": "The two valve types are named by location — atrioventricular "
               "valves sit between chambers, semilunar valves sit where "
               "blood leaves the heart.",
    },
    {
        "id": "ks4-heart-blood-vessels-s07",
        "subtopic_slug": "heart-blood-vessels",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why capillaries form a dense network throughout "
                "body tissues.",
        "options": [
            "So that no single capillary has to carry very much blood at once",
            "So that the walls can be made much thicker without slowing exchange",
            "So that the total surface area for exchange with cells is as large as possible",
            "So that blood pressure can still be kept as high as possible everywhere near every single cell",
        ],
        "correct_index": 2,
        "why": "A dense network of capillaries maximises the surface area "
               "available for substances to diffuse across.",
    },
    {
        "id": "ks4-heart-blood-vessels-s08",
        "subtopic_slug": "heart-blood-vessels",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why capillaries do not need valves, unlike veins.",
        "options": [
            "Blood does not flow through a capillary at all; it only ever diffuses across the wall",
            "Capillaries lie so close to the heart that each heartbeat pushes the blood through twice",
            "A capillary carries blood in both directions at once, so a valve would have nothing to stop",
            "Pressure stays high enough through the capillary bed to keep flow moving one way",
        ],
        "correct_index": 3,
        "why": "Enough pressure survives from the heart's contraction to "
               "keep blood moving one way through the capillary bed, so no "
               "valve is needed.",
    },
    {
        "id": "ks4-heart-blood-vessels-s09",
        "subtopic_slug": "heart-blood-vessels",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain how a narrow lumen helps an artery do its job.",
        "options": [
            "It helps maintain the high pressure needed to push blood around the body",
            "It lets red blood cells travel through in large clumps rather than single file",
            "It allows the artery wall to be thinner than a vein's wall",
            "It slows blood down enough for gas exchange to take place inside it",
        ],
        "correct_index": 0,
        "why": "A narrow lumen keeps resistance and pressure high, matching "
               "an artery's job of delivering blood under force.",
    },
    {
        "id": "ks4-heart-blood-vessels-s10",
        "subtopic_slug": "heart-blood-vessels",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain how a wide lumen helps a vein do its job.",
        "options": [
            "It lets the vein carry blood at a very high pressure without ever bursting or rupturing",
            "It reduces resistance to flow, helping blood move despite the low pressure",
            "It gives room for a thick, muscular wall to develop around it",
            "It allows the vein to act as a site of gas exchange with tissues",
        ],
        "correct_index": 1,
        "why": "A wide lumen cuts resistance, which matters because a vein "
               "has so little pressure left to push blood along with.",
    },
    {
        "id": "ks4-heart-blood-vessels-s11",
        "subtopic_slug": "heart-blood-vessels",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why the pulmonary vein is unusual among veins.",
        "options": [
            "It is the only vein in the body that contains any valves at all",
            "It is the only vein with a wall as thick and muscular as an artery's",
            "It carries oxygenated blood, even though it is classified as a vein",
            "It carries blood towards the lungs rather than away from the heart",
        ],
        "correct_index": 2,
        "why": "Vessel names depend on direction, not oxygen content, so the "
               "pulmonary vein carries oxygenated blood despite being a "
               "vein.",
    },
    {
        "id": "ks4-heart-blood-vessels-s12",
        "subtopic_slug": "heart-blood-vessels",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Describe the route blood takes from the right atrium to the "
                "lungs.",
        "options": [
            "Right atrium, left ventricle, aorta, lungs",
            "Right atrium, right ventricle, pulmonary vein, lungs",
            "Right atrium, left atrium, pulmonary artery, lungs",
            "Right atrium, right ventricle, pulmonary artery, lungs",
        ],
        "correct_index": 3,
        "why": "From the right atrium blood drops into the right ventricle "
               "and leaves by the pulmonary artery towards the lungs.",
    },
    {
        "id": "ks4-heart-blood-vessels-s13",
        "subtopic_slug": "heart-blood-vessels",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "State which valves close first during a heartbeat, causing "
                "the first ('lub') sound.",
        "options": [
            "The atrioventricular valves",
            "The semilunar valves",
            "The valves in the vena cava",
            "The valves in the pulmonary vein",
        ],
        "correct_index": 0,
        "why": "The atrioventricular valves close first, as the ventricles "
               "begin to contract and pressure inside them rises.",
    },
    {
        "id": "ks4-heart-blood-vessels-s14",
        "subtopic_slug": "heart-blood-vessels",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare the wall thickness of an artery, a vein and a "
                "capillary.",
        "options": [
            "All three of these vessels actually have exactly the same wall thickness throughout the whole body",
            "An artery has the thickest wall, a vein a thinner wall, and a capillary the thinnest of all",
            "A vein actually has the thickest wall of the three, since it must resist collapsing under low pressure",
            "A capillary actually has a thicker wall than an artery does, to withstand constant exchange",
        ],
        "correct_index": 1,
        "why": "Wall thickness tracks pressure: thickest in the artery, "
               "thinner in the vein, thinnest of all in the capillary.",
    },
    {
        "id": "ks4-heart-blood-vessels-s15",
        "subtopic_slug": "heart-blood-vessels",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why gas exchange happens at capillaries but not at "
                "arteries or veins.",
        "options": [
            "Arteries and veins carry the wrong type of blood for gas exchange to occur",
            "Arteries and veins are found too far from the lungs for exchange to happen",
            "Only capillary walls are thin enough and close enough to cells for diffusion",
            "Arteries and veins move blood too quickly for any diffusion to take place",
        ],
        "correct_index": 2,
        "why": "Gas exchange needs a short diffusion distance, which only "
               "the one-cell-thick capillary wall provides.",
    },
    {
        "id": "ks4-heart-blood-vessels-s16",
        "subtopic_slug": "heart-blood-vessels",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare the pulmonary circuit with the systemic circuit.",
        "options": [
            "Both of these circuits actually carry oxygenated blood only, never any deoxygenated blood",
            "The pulmonary circuit is actually the longer of the two circuits, reaching every organ",
            "Both of these circuits pass through the right side of the heart twice during each beat",
            "The pulmonary circuit runs to the lungs; the systemic circuit runs to the rest of the body",
        ],
        "correct_index": 3,
        "why": "The pulmonary circuit connects the heart to the lungs; the "
               "systemic circuit connects it to every other organ.",
    },
    {
        "id": "ks4-heart-blood-vessels-s17",
        "subtopic_slug": "heart-blood-vessels",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "The valve between the right atrium and the right ventricle "
                "fails to close fully. Predict the effect.",
        "options": [
            "Blood leaks back into the right atrium, so less reaches the lungs each beat",
            "Blood leaks forward into the pulmonary artery much faster than it normally would",
            "Blood is completely unable to enter the right atrium from the vena cava at all",
            "Blood is somehow redirected into the left side of the heart instead of the right",
        ],
        "correct_index": 0,
        "why": "A leaking valve lets blood slip backwards on each beat, "
               "reducing how much moves forward towards the lungs.",
    },
    {
        "id": "ks4-heart-blood-vessels-s18",
        "subtopic_slug": "heart-blood-vessels",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "The vena cava becomes partly narrowed by a blood clot. "
                "Predict the effect on the heart.",
        "options": [
            "The left ventricle almost immediately stops pumping any blood at all to the body",
            "Less blood returns to the right atrium, so less is available to pump onward",
            "The aorta then narrows to match it exactly, keeping blood pressure constant",
            "More blood is simply diverted through the coronary arteries instead of onward",
        ],
        "correct_index": 1,
        "why": "A narrowed vena cava restricts how much blood returns to "
               "the right atrium, so less is available to send onward.",
    },
    {
        "id": "ks4-heart-blood-vessels-s19",
        "subtopic_slug": "heart-blood-vessels",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why the coronary arteries branch from the aorta "
                "rather than from the vena cava.",
        "options": [
            "The vena cava actually carries far too little oxygen to supply the heart muscle properly",
            "The aorta happens to sit physically closer to the heart muscle than the vena cava does",
            "The aorta carries oxygenated blood, which the heart muscle needs to respire",
            "The vena cava simply has no branches of any kind at all along its entire length",
        ],
        "correct_index": 2,
        "why": "Only the aorta carries the oxygenated blood the heart "
               "muscle needs to respire; the vena cava carries deoxygenated "
               "blood.",
    },
    {
        "id": "ks4-heart-blood-vessels-s20",
        "subtopic_slug": "heart-blood-vessels",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why fish, which have only a single circulatory "
                "system, generally have a lower maximum activity level than "
                "mammals.",
        "options": [
            "A fish heart has four chambers, so blood is slowed by passing through two extra chambers",
            "Fish take up oxygen through the skin rather than the blood, so the circulation carries none",
            "A fish has no capillaries in its muscles, so oxygen has to diffuse the whole way from the gills",
            "Blood pressure has already dropped by the time it reaches a fish's body, unlike in mammals",
        ],
        "correct_index": 3,
        "why": "With only one circuit, a fish's blood loses pressure "
               "crossing the gills before it ever reaches the body, unlike "
               "a mammal's double circulation.",
    },
    {
        "id": "ks4-heart-blood-vessels-s21",
        "subtopic_slug": "heart-blood-vessels",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain the general purpose that every valve in the heart "
                "and veins serves.",
        "options": [
            "Preventing blood from flowing backwards in the wrong direction",
            "Speeding blood up as it passes from one chamber to the next",
            "Removing carbon dioxide from the blood as it passes through",
            "Adding oxygen to the blood as it flows past each valve",
        ],
        "correct_index": 0,
        "why": "Every valve in the circulatory system exists to stop blood "
               "flowing backwards.",
    },
    {
        "id": "ks4-heart-blood-vessels-s22",
        "subtopic_slug": "heart-blood-vessels",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why red blood cells must squeeze through capillaries "
                "in single file.",
        "options": [
            "Capillaries actually contain tiny valves that only ever let one cell pass through at a time",
            "Capillaries are so narrow that only one red blood cell fits across at once",
            "Red blood cells clump together tightly as they approach a capillary",
            "Capillary walls actively pull red blood cells through one at a time",
        ],
        "correct_index": 1,
        "why": "A capillary is so narrow that red blood cells can only pass "
               "through it one at a time.",
    },
    {
        "id": "ks4-heart-blood-vessels-s23",
        "subtopic_slug": "heart-blood-vessels",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why the left atrium has a much thinner wall than "
                "the left ventricle.",
        "options": [
            "The left atrium only has to push blood a short distance into the ventricle below it",
            "The left atrium actually carries deoxygenated blood, which needs far less force to move",
            "The left atrium contracts noticeably far less often overall than the left ventricle does",
            "The left atrium is not actually made from cardiac muscle at all, unlike the left ventricle",
        ],
        "correct_index": 0,
        "why": "The atrium only pushes blood a short distance into the "
               "ventricle below, so it needs far less force than the "
               "ventricle that pumps it onward.",
    },
    {
        "id": "ks4-heart-blood-vessels-s24",
        "subtopic_slug": "heart-blood-vessels",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why blood flows more slowly through the capillaries "
                "than through the aorta, even though a huge volume must "
                "pass through both.",
        "options": [
            "Capillaries actively resist the flow of blood to protect the delicate tissue around them",
            "The heart pumps far less forcefully by the time blood reaches the capillary bed",
            "Red blood cells lose most of their oxygen before reaching the capillaries, slowing them",
            "The huge combined cross-sectional area of all the capillaries together slows the flow",
        ],
        "correct_index": 3,
        "why": "Even though each capillary is tiny, together they add up "
               "to a far larger total cross-section than the aorta, which "
               "slows the flow through them.",
    },
    {
        "id": "ks4-heart-blood-vessels-s25",
        "subtopic_slug": "heart-blood-vessels",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why oxygen diffuses out of the blood specifically at "
                "the capillaries, not earlier in an artery.",
        "options": [
            "Only capillary walls are thin enough, and close enough to cells, to allow diffusion to happen",
            "Arteries actually actively pump oxygen back into their own thick walls before releasing blood",
            "Blood travelling in an artery has not yet even been oxygenated by the lungs at that point",
            "The pressure inside an artery is actually far too low for any diffusion to take place there",
        ],
        "correct_index": 0,
        "why": "Diffusion needs a thin wall close to the cells that need "
               "the oxygen — a condition only the capillary wall meets.",
    },
    {
        "id": "ks4-heart-blood-vessels-s26",
        "subtopic_slug": "heart-blood-vessels",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why many veins run close to the surface of the "
                "skin, while the main arteries run deep inside the body.",
        "options": [
            "Veins need cooling from outside air to keep the blood inside them at a safe temperature",
            "Running deep protects the high-pressure arteries from damage if the body's surface is injured",
            "Veins are actually much lighter in construction than arteries, so they sit closer to the surface",
            "Arteries actually need to be in direct contact with the air to pick up enough oxygen",
        ],
        "correct_index": 1,
        "why": "Running deep shields the high-pressure arteries, which "
               "would bleed dangerously if cut, from everyday injury.",
    },
    {
        "id": "ks4-heart-blood-vessels-h05",
        "subtopic_slug": "heart-blood-vessels",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why blood flow feels like a pulse in an artery near "
                "the wrist, but not in a vein.",
        "options": [
            "By the time blood reaches a vein, the surge from each heartbeat has been smoothed out",
            "Veins actually contain almost no blood at all in the brief gaps between each heartbeat",
            "Arteries are located closer to the surface of the skin at every point in the body",
            "The heart actually only ever pumps blood into arteries, never directly into any vein",
        ],
        "correct_index": 0,
        "why": "The elastic walls of arteries and the distance travelled "
               "smooth out the heartbeat's surge, so the pulse has "
               "disappeared by the time blood reaches a vein.",
    },
    {
        "id": "ks4-heart-blood-vessels-h06",
        "subtopic_slug": "heart-blood-vessels",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate this claim: 'Every vessel leaving the heart is an "
                "artery, and every vessel entering it is a vein.'",
        "options": [
            "True — this is exactly how arteries and veins are defined, regardless of the blood's oxygen content",
            "False — the pulmonary artery actually carries blood directly into the heart, not out of it at all",
            "False — arteries only ever carry oxygenated blood, no matter which direction they happen to run",
            "True, but only because absolutely every vessel in the body carries oxygenated blood anyway",
        ],
        "correct_index": 0,
        "why": "Artery and vein are defined purely by direction relative to "
               "the heart, which is exactly why the pulmonary vessels break "
               "the oxygen 'rule of thumb' without breaking the actual "
               "definition.",
    },
    {
        "id": "ks4-heart-blood-vessels-h07",
        "subtopic_slug": "heart-blood-vessels",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student claims 'you can tell what a blood vessel carries "
                "just from its name — artery or vein'. Evaluate this claim "
                "using the pulmonary vessels.",
        "options": [
            "True — the pulmonary artery and pulmonary vein always match the general oxygen-based rule exactly as expected",
            "True, but only because the pulmonary vessels happen to be named completely differently from every other vessel in the body",
            "False — the pulmonary artery carries deoxygenated blood and the pulmonary vein oxygenated blood, against the general pattern",
            "False — the words 'artery' and 'vein' have no fixed and reliable meaning anywhere in the whole body",
        ],
        "correct_index": 2,
        "why": "The pulmonary vessels are the exception that breaks the "
               "'artery equals oxygenated' shortcut, showing that direction, "
               "not oxygen, is what actually defines the two names.",
    },
    {
        "id": "ks4-heart-blood-vessels-h08",
        "subtopic_slug": "heart-blood-vessels",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "The semilunar valve in the aorta fails to close fully after "
                "each heartbeat. Predict the effect.",
        "options": [
            "Blood is then completely unable to leave the left ventricle at all during the next contraction",
            "The right ventricle then begins pumping in place of the left ventricle entirely",
            "Blood backs up into the right atrium instead of flowing into the left ventricle",
            "Blood leaks back into the left ventricle, so less reaches the body with each beat",
        ],
        "correct_index": 3,
        "why": "A leaking aortic valve lets some blood slip back into the "
               "left ventricle instead of staying in the aorta, reducing "
               "how much reaches the body.",
    },
    {
        "id": "ks4-heart-blood-vessels-h09",
        "subtopic_slug": "heart-blood-vessels",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest what would happen to blood pressure delivered to the "
                "brain if the pulmonary and systemic circuits ran in a "
                "single loop, one after the other, as in a fish.",
        "options": [
            "Blood pressure reaching the brain would be much lower, since it would already have dropped crossing the lungs",
            "Blood pressure reaching the brain would end up being exactly the same as it currently is",
            "Blood pressure reaching the brain would rise instead, since the blood would only have to pass through the heart once",
            "Blood pressure reaching the brain would become completely impossible to measure at all in that case",
        ],
        "correct_index": 0,
        "why": "Pressure falls as blood crosses the narrow capillaries of "
               "the lungs, so a single loop would deliver much lower "
               "pressure onward to the brain than a double circulation "
               "does.",
    },
    {
        "id": "ks4-heart-blood-vessels-h10",
        "subtopic_slug": "heart-blood-vessels",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate this claim: 'Every artery has a thicker wall than "
                "every vein.'",
        "options": [
            "True, and this holds without any exceptions anywhere at all in the whole circulatory system",
            "False — larger veins closer to the heart can have thicker walls than the smallest arterioles",
            "True, but this is only the case in vessels that lie above the level of the heart",
            "False, but only because capillaries are technically classed as being veins",
        ],
        "correct_index": 1,
        "why": "Vessel size varies hugely — a large vein near the heart can "
               "outrank a tiny arteriole in wall thickness, so the blanket "
               "claim fails.",
    },
    {
        "id": "ks4-heart-blood-vessels-h11",
        "subtopic_slug": "heart-blood-vessels",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare how arteries and capillaries are each structurally "
                "suited to the pressure of blood passing through them.",
        "options": [
            "Arteries actually have thin walls to survive low pressure; capillaries have thick walls to survive high pressure",
            "Arteries and capillaries share an identical wall structure, since the pressure barely changes at all between one and the other",
            "Arteries have thick, elastic walls to survive high pressure; capillary walls are thin because pressure has fallen by then",
            "Arteries actually have valves to survive high pressure; capillaries instead have muscle to survive low pressure",
        ],
        "correct_index": 2,
        "why": "Each vessel's wall matches the pressure it experiences: "
               "thick and elastic where pressure is highest, thin once "
               "pressure has fallen enough for exchange to matter more.",
    },
    {
        "id": "ks4-heart-blood-vessels-h12",
        "subtopic_slug": "heart-blood-vessels",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest what would happen to gas exchange if capillary walls "
                "were as thick as artery walls.",
        "options": [
            "Gas exchange would actually speed up, since a thicker wall would carry more oxygen at once",
            "Gas exchange would be unaffected, since wall thickness makes no difference to diffusion",
            "Capillaries would then need to grow valves, which would slow the whole blood flow down",
            "Gas exchange would slow down drastically, since diffusion distance would increase",
        ],
        "correct_index": 3,
        "why": "Diffusion rate falls as distance increases, so a thicker "
               "capillary wall would slow gas exchange drastically.",
    },
    {
        "id": "ks4-heart-blood-vessels-h13",
        "subtopic_slug": "heart-blood-vessels",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student says the right side of the heart is 'weaker' than "
                "the left side. Evaluate this claim.",
        "options": [
            "Not weaker — it simply needs less force, since it only pumps blood as far as the nearby lungs",
            "Correct — the right side of the heart can often fail many years before the left side of it ever does",
            "Not weaker — both sides of the heart pump with exactly the same force at every beat",
            "Correct — the right side is built from a different, less powerful type of muscle",
        ],
        "correct_index": 0,
        "why": "The right ventricle only needs to send blood as far as the "
               "nearby lungs, so a thinner wall is fit for its purpose, not "
               "a sign of weakness.",
    },
    {
        "id": "ks4-heart-blood-vessels-h14",
        "subtopic_slug": "heart-blood-vessels",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Predict the effect on blood pressure if the aorta had a wide "
                "lumen like a vein's.",
        "options": [
            "Blood pressure delivered to the body would rise even further than normal",
            "Blood pressure delivered to the body would fall, since resistance to flow would drop",
            "Blood pressure would stay exactly the same, since the heart compensates automatically",
            "Blood would stop flowing altogether, since arteries cannot function with a wide lumen",
        ],
        "correct_index": 1,
        "why": "A wider lumen lowers resistance, and lower resistance means "
               "the pressure delivered onward would fall.",
    },
    {
        "id": "ks4-heart-blood-vessels-h15",
        "subtopic_slug": "heart-blood-vessels",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare the likely severity of a leaking valve on the left "
                "side of the heart with one on the right.",
        "options": [
            "Both are actually equally severe, since both sides of the heart pump exactly the same volume of blood",
            "The right-side leak is actually more severe, since the right ventricle is the noticeably thicker chamber",
            "The left-side leak tends to be more severe, since the left side pumps at much higher pressure",
            "Neither leak actually has any real effect on the body, since valves only ever affect heart sounds",
        ],
        "correct_index": 2,
        "why": "Higher pressure on the left side means a leak there loses "
               "more blood backwards per beat than an equivalent leak on "
               "the lower-pressure right side.",
    },
    {
        "id": "ks4-heart-blood-vessels-h16",
        "subtopic_slug": "heart-blood-vessels",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A patient has a coronary bypass graft fitted around a "
                "blocked section of artery. Explain how blood now reaches "
                "the heart muscle beyond the blockage.",
        "options": [
            "It is somehow filtered through the lungs first, which removes the blockage's effect entirely",
            "It flows backwards through the whole blocked section, arriving from the far side instead",
            "The blockage simply dissolves naturally on its own once the graft has been put in place",
            "It flows through the grafted vessel, rejoining the original artery beyond the blocked section",
        ],
        "correct_index": 3,
        "why": "A bypass graft creates an entirely new route, carrying "
               "blood around the blockage and rejoining the artery further "
               "along.",
    },
    {
        "id": "ks4-heart-blood-vessels-h17",
        "subtopic_slug": "heart-blood-vessels",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate this claim: 'Because capillaries have no valves, "
                "blood inside them can flow in either direction.'",
        "options": [
            "False — the pressure gradient across the whole circuit still keeps blood moving in one direction there too",
            "True — without any valves present, nothing at all controls which way the blood ends up moving",
            "True, but this only applies inside those capillaries found specifically in the lower half of the body",
            "False, but only because capillaries are technically too narrow for blood to ever reverse",
        ],
        "correct_index": 0,
        "why": "Direction is maintained by the pressure gradient running "
               "all the way from the heart through to the veins, not by "
               "valves at every single point.",
    },
    {
        "id": "ks4-heart-blood-vessels-h18",
        "subtopic_slug": "heart-blood-vessels",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A patient's pulmonary vein becomes completely blocked. "
                "Predict the effect.",
        "options": [
            "The right side of the heart would stop beating within a matter of seconds",
            "Oxygenated blood cannot reach the left atrium, so the whole body is starved of oxygen",
            "Blood would be rerouted completely automatically through the aorta instead of the vein",
            "The lungs would stop receiving any blood at all from the right ventricle from then on",
        ],
        "correct_index": 1,
        "why": "With the pulmonary vein blocked, oxygenated blood cannot "
               "reach the left atrium at all, so the left side has nothing "
               "oxygenated to send to the body.",
    },
    {
        "id": "ks4-heart-blood-vessels-h19",
        "subtopic_slug": "heart-blood-vessels",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "With age, the elastic fibres in artery walls become "
                "stiffer. Predict the effect on blood flow.",
        "options": [
            "Blood flow becomes perfectly smooth, since a stiff wall cannot possibly stretch unevenly",
            "Blood pressure surges become larger with each heartbeat, since the wall no longer absorbs them as well",
            "Blood flow reverses direction far more easily, since the stiffened wall no longer resists it",
            "Blood pressure actually falls steadily over time, since a stiffer wall offers less resistance overall",
        ],
        "correct_index": 1,
        "why": "A stiffer wall cannot stretch and recoil as well, so more "
               "of each heartbeat's surge reaches further down the "
               "arteries instead of being smoothed out.",
    },
    {
        "id": "ks4-heart-blood-vessels-h20",
        "subtopic_slug": "heart-blood-vessels",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest the effect on returning blood if every valve in the "
                "leg veins stopped working, while the heart valves stayed "
                "normal.",
        "options": [
            "Blood would pool in the legs, especially when standing, since gravity would pull it backwards",
            "Blood would actually flow faster back to the heart, since nothing at all would resist it",
            "Blood would somehow be rerouted through the arteries of the leg instead of the veins",
            "The heart would compensate for this completely, so no effect would be noticeable",
        ],
        "correct_index": 0,
        "why": "Without valves to stop backflow, gravity would pull blood "
               "back down the leg veins, letting it pool rather than "
               "return to the heart.",
    },
    {
        "id": "ks4-heart-blood-vessels-h21",
        "subtopic_slug": "heart-blood-vessels",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Both semilunar valves — in the aorta and in the pulmonary "
                "artery — fail at the same time. Predict the combined "
                "effect.",
        "options": [
            "Both sides of the heart become less efficient, as blood leaks back into both ventricles after each beat",
            "Only the left side of the heart would actually be affected, since the aorta carries far more blood",
            "The heart would compensate for this fully by simply beating twice as fast as normal",
            "Blood would somehow be rerouted entirely through the coronary arteries instead of onward",
        ],
        "correct_index": 0,
        "why": "Each semilunar valve failing lets blood leak back into its "
               "own ventricle, so both sides lose efficiency together.",
    },
    {
        "id": "ks4-heart-blood-vessels-h22",
        "subtopic_slug": "heart-blood-vessels",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare cardiac muscle with skeletal muscle in terms of "
                "fatigue.",
        "options": [
            "Cardiac muscle fatigues faster than skeletal muscle, since it never gets to rest between contractions",
            "Skeletal muscle fatigues faster than cardiac muscle can, since it works continuously for a lifetime",
            "Cardiac muscle can contract and relax rhythmically without tiring; skeletal muscle fatigues with sustained use",
            "Neither type of muscle ever fatigues at all, since both of them are supplied directly by the coronary arteries",
        ],
        "correct_index": 2,
        "why": "Cardiac muscle is specialised to contract rhythmically "
               "without tiring, unlike skeletal muscle, which fatigues "
               "with sustained use.",
    },
    {
        "id": "ks4-heart-blood-vessels-h23",
        "subtopic_slug": "heart-blood-vessels",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate this claim: 'A faster resting heart rate always "
                "means a stronger, fitter heart.'",
        "options": [
            "True — a faster heart rate always means that more blood is delivered to the body overall",
            "False — a fitter heart can often pump the same amount of blood with fewer, stronger beats",
            "True, but only because a faster heart rate always means larger heart chambers",
            "False, but only because heart rate has nothing at all to do with overall fitness",
        ],
        "correct_index": 1,
        "why": "A fitter heart typically pumps more blood per beat, so it "
               "can deliver the same total amount with a slower, not "
               "faster, resting rate.",
    },
    {
        "id": "ks4-heart-blood-vessels-h24",
        "subtopic_slug": "heart-blood-vessels",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A hole exists in the muscular wall between the left and "
                "right ventricles. Predict the effect on the blood leaving "
                "the aorta.",
        "options": [
            "It becomes a mixture of oxygenated and deoxygenated blood, carrying less oxygen than normal",
            "It becomes more oxygenated than normal, since blood passes through the heart twice",
            "It stops flowing altogether, since the hole removes all pressure from the left ventricle",
            "It is completely unaffected, since the hole only affects the atria above",
        ],
        "correct_index": 0,
        "why": "A hole between the ventricles lets oxygenated and "
               "deoxygenated blood mix, so blood leaving the aorta carries "
               "less oxygen than it should.",
    },
    {
        "id": "ks4-heart-blood-vessels-h25",
        "subtopic_slug": "heart-blood-vessels",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why heart muscle cannot simply absorb oxygen from "
                "the blood passing through its own chambers.",
        "options": [
            "The heart wall is far too thick for oxygen to diffuse in from the blood inside the chambers",
            "Blood inside the chambers is always deoxygenated, so there would be no oxygen to absorb",
            "The heart wall is completely impermeable, so no substance could ever cross it in either direction",
            "Heart muscle does not actually require any oxygen at all in order to keep contracting",
        ],
        "correct_index": 0,
        "why": "The heart wall is far too thick for diffusion alone to "
               "supply it, which is exactly why it needs its own coronary "
               "blood supply.",
    },
    {
        "id": "ks4-heart-blood-vessels-h26",
        "subtopic_slug": "heart-blood-vessels",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Rank these vessels from highest to lowest typical blood "
                "pressure: a capillary, the vena cava, the aorta, the "
                "pulmonary artery.",
        "options": [
            "The aorta, the pulmonary artery, a capillary, the vena cava",
            "The vena cava, a capillary, the pulmonary artery, the aorta",
            "The pulmonary artery, the aorta, the vena cava, a capillary",
            "A capillary, the aorta, the pulmonary artery, the vena cava",
        ],
        "correct_index": 0,
        "why": "Pressure falls the further blood travels from the left "
               "ventricle: highest in the aorta, still raised in the "
               "pulmonary artery, low in the capillaries, and lowest of "
               "all by the time it reaches the vena cava.",
    },

    # ══════════════════════════════════════════════════════════════════
    # blood · e05-e12, s05-s26, h05-h26
    # ══════════════════════════════════════════════════════════════════
    {
        "id": "ks4-blood-e05",
        "subtopic_slug": "blood",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State where red blood cells, white blood cells and "
                "platelets are all made.",
        "options": [
            "In the bone marrow",
            "In the spleen",
            "In the liver",
            "In the kidneys",
        ],
        "correct_index": 0,
        "why": "All three blood components are made in the bone marrow.",
    },
    {
        "id": "ks4-blood-e06",
        "subtopic_slug": "blood",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State roughly how long a red blood cell survives before "
                "being broken down.",
        "options": [
            "About 12 hours",
            "About 120 days",
            "About 12 days",
            "About 12 years",
        ],
        "correct_index": 1,
        "why": "A red blood cell survives for roughly 120 days before being "
               "broken down.",
    },
    {
        "id": "ks4-blood-e07",
        "subtopic_slug": "blood",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the organ where worn-out red blood cells are broken "
                "down.",
        "options": [
            "The bone marrow",
            "The kidney",
            "The spleen",
            "The pancreas",
        ],
        "correct_index": 2,
        "why": "Worn-out red blood cells are broken down in the spleen.",
    },
    {
        "id": "ks4-blood-e08",
        "subtopic_slug": "blood",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State which blood component still has a nucleus, unlike a "
                "red blood cell.",
        "options": [
            "A platelet",
            "Plasma",
            "Haemoglobin molecules",
            "A white blood cell",
        ],
        "correct_index": 3,
        "why": "White blood cells keep their nucleus, unlike red blood "
               "cells and platelets.",
    },
    {
        "id": "ks4-blood-e09",
        "subtopic_slug": "blood",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what an antigen is.",
        "options": [
            "A molecule on a pathogen's surface that the immune system recognises as foreign",
            "A protein made by a lymphocyte in order to help destroy a pathogen",
            "A tiny fragment of a blood cell that is mainly involved in the clotting process",
            "The liquid part of blood that simply carries dissolved substances around",
        ],
        "correct_index": 0,
        "why": "An antigen is a molecule on a pathogen's surface that marks "
               "it as foreign to the immune system.",
    },
    {
        "id": "ks4-blood-e10",
        "subtopic_slug": "blood",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State roughly what percentage of blood volume is made up "
                "of plasma.",
        "options": [
            "About 15%",
            "About 55%",
            "About 35%",
            "About 75%",
        ],
        "correct_index": 1,
        "why": "Plasma makes up roughly 55% of the total volume of blood.",
    },
    {
        "id": "ks4-blood-e11",
        "subtopic_slug": "blood",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State one thing, other than dissolved food and waste, "
                "that plasma transports around the body.",
        "options": [
            "Starch",
            "Cellulose",
            "Heat",
            "Melanin",
        ],
        "correct_index": 2,
        "why": "Plasma distributes heat from active muscles to cooler parts "
               "of the body.",
    },
    {
        "id": "ks4-blood-e12",
        "subtopic_slug": "blood",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State roughly how many haemoglobin molecules one red blood "
                "cell contains.",
        "options": [
            "About 270",
            "About 27,000",
            "About 27 billion",
            "About 270 million",
        ],
        "correct_index": 3,
        "why": "A single red blood cell contains roughly 270 million "
               "haemoglobin molecules.",
    },
    {
        "id": "ks4-blood-s05",
        "subtopic_slug": "blood",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why red blood cells cannot replace themselves by "
                "dividing.",
        "options": [
            "They have no nucleus, and a nucleus is needed to control cell division",
            "They are already far too specialised in shape to ever be able to divide again",
            "They are broken down by the spleen before they ever get the chance to divide",
            "They actually lack the energy that would be needed to carry out cell division",
        ],
        "correct_index": 0,
        "why": "Cell division is controlled from the nucleus, so a cell "
               "with no nucleus cannot divide.",
    },
    {
        "id": "ks4-blood-s06",
        "subtopic_slug": "blood",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why the body must constantly make new red blood "
                "cells.",
        "options": [
            "Red blood cells are used up completely during every respiration reaction",
            "Each one only survives for around 120 days before being broken down",
            "Red blood cells are destroyed instantly by any bacteria they meet",
            "Red blood cells dissolve away gradually as haemoglobin leaks out of them",
        ],
        "correct_index": 1,
        "why": "With each red blood cell lasting only around 120 days, new "
               "ones must constantly be made to replace those broken down.",
    },
    {
        "id": "ks4-blood-s07",
        "subtopic_slug": "blood",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A patient's bone marrow is destroyed by radiation. Explain "
                "the immediate risk to their blood.",
        "options": [
            "No new red blood cells, white blood cells or platelets can be produced",
            "All of their existing platelets instantly turn into white blood cells",
            "Their plasma would immediately stop being able to carry oxygen around the whole body",
            "Their red blood cells lose their biconcave shape within hours",
        ],
        "correct_index": 0,
        "why": "Bone marrow makes all three types of blood cell, so "
               "destroying it stops new red blood cells, white blood cells "
               "and platelets being produced.",
    },
    {
        "id": "ks4-blood-s08",
        "subtopic_slug": "blood",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Distinguish between an antigen and an antibody.",
        "options": [
            "An antigen is actually made by the whole body itself; an antibody is actually made only by a pathogen",
            "An antigen sits on a pathogen's surface; an antibody is made by a lymphocyte to bind it",
            "They are simply two different names for exactly the very same molecule",
            "An antigen actually destroys pathogens directly; an antibody only marks them for removal",
        ],
        "correct_index": 1,
        "why": "An antigen is the foreign marker on a pathogen; an antibody "
               "is the protein a lymphocyte makes to bind that marker.",
    },
    {
        "id": "ks4-blood-s09",
        "subtopic_slug": "blood",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why phagocytes, rather than lymphocytes, are usually "
                "the first cells to respond to an infection.",
        "options": [
            "Lymphocytes are only made after a person has already recovered from an infection",
            "Phagocytes travel through the blood much faster than lymphocytes are able to",
            "Phagocytes can attack any pathogen without needing to recognise a specific antigen first",
            "Lymphocytes are destroyed completely by the first pathogen that they ever encounter",
        ],
        "correct_index": 2,
        "why": "Phagocytes act non-specifically, so they can respond to any "
               "pathogen at once, while a lymphocyte first needs to "
               "recognise the specific antigen.",
    },
    {
        "id": "ks4-blood-s10",
        "subtopic_slug": "blood",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a white blood cell, unlike a red blood cell, "
                "keeps its nucleus.",
        "options": [
            "White blood cells do not need extra space for haemoglobin",
            "It needs the nucleus to produce antibodies or to control phagocytosis",
            "White blood cells are too large to lose their nucleus during development",
            "The nucleus is essentially what gives a white blood cell its distinctive round shape",
        ],
        "correct_index": 1,
        "why": "A white blood cell needs its nucleus to direct antibody "
               "production or to control phagocytosis.",
    },
    {
        "id": "ks4-blood-s11",
        "subtopic_slug": "blood",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain how a hormone made in one part of the body reaches "
                "its target organ elsewhere.",
        "options": [
            "It diffuses directly through every tissue until it reaches its target organ",
            "It dissolves in the plasma, which carries it around the body in the blood",
            "It is carried inside red blood cells until it reaches its target organ",
            "It actually travels along nerve cells until it manages to reach its target organ",
        ],
        "correct_index": 1,
        "why": "Hormones dissolve in the plasma, which distributes them "
               "around the body in the bloodstream.",
    },
    {
        "id": "ks4-blood-s12",
        "subtopic_slug": "blood",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Describe how urea travels from the liver, where it is made, "
                "to the kidneys.",
        "options": [
            "It travels inside white blood cells that carry it to the kidneys",
            "It diffuses directly through the tissue connecting the liver and kidneys",
            "It dissolves in the plasma and is carried there in the blood",
            "It is carried inside platelets that pass close to the kidneys",
        ],
        "correct_index": 2,
        "why": "Urea dissolves in the plasma, which carries it from the "
               "liver to the kidneys for excretion.",
    },
    {
        "id": "ks4-blood-s13",
        "subtopic_slug": "blood",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain the purpose of a scab forming over a wound.",
        "options": [
            "Sealing the wound, preventing further blood loss and blocking pathogens from entering",
            "Providing extra oxygen directly to the healing skin cells underneath it",
            "Producing new red blood cells to replace those lost in the bleeding",
            "Dissolving the fibrin mesh completely, once the bleeding underneath has fully and finally stopped",
        ],
        "correct_index": 0,
        "why": "A scab seals the wound, stopping further blood loss and "
               "keeping pathogens from entering.",
    },
    {
        "id": "ks4-blood-s14",
        "subtopic_slug": "blood",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a red blood cell's membrane must be flexible.",
        "options": [
            "So it can go on dividing repeatedly without its own membrane ever tearing apart",
            "So it can absorb extra haemoglobin molecules as the cell ages",
            "So it can change colour noticeably depending on how much oxygen it happens to be carrying",
            "So it can bend and squeeze through capillaries narrower than its own width",
        ],
        "correct_index": 3,
        "why": "A flexible membrane lets a red blood cell deform enough to "
               "squeeze through capillaries narrower than its own width.",
    },
    {
        "id": "ks4-blood-s15",
        "subtopic_slug": "blood",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare the role of a platelet with the role of a white "
                "blood cell.",
        "options": [
            "Both of them defend the body against pathogens by engulfing them directly",
            "A platelet is involved in clotting; a white blood cell defends against pathogens",
            "A platelet actually makes the antibodies; a white blood cell forms the clot itself",
            "Both of them transport oxygen to tissues throughout the body, just using two completely different proteins",
        ],
        "correct_index": 1,
        "why": "A platelet's role is clotting, while a white blood cell's "
               "role is defending the body against pathogens.",
    },
    {
        "id": "ks4-blood-s16",
        "subtopic_slug": "blood",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a diet very low in iron can reduce how much "
                "oxygen the blood carries.",
        "options": [
            "Iron is needed just to keep a red blood cell in its correct biconcave shape",
            "Iron binds directly to the oxygen molecules itself, instead of the haemoglobin doing so",
            "Iron is a component of haemoglobin, so too little iron means less haemoglobin can be made",
            "Iron is what red blood cells actually use as their main source of energy",
        ],
        "correct_index": 2,
        "why": "Haemoglobin contains iron, so a diet lacking iron limits how "
               "much haemoglobin can be made, cutting oxygen-carrying "
               "capacity.",
    },
    {
        "id": "ks4-blood-s17",
        "subtopic_slug": "blood",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why the second immune response to a pathogen is "
                "usually faster than the first.",
        "options": [
            "The pathogen itself becomes noticeably weaker each time it infects the same person",
            "Phagocytes multiply permanently in number after just the first infection occurs",
            "Antibodies from the very first infection remain in the blood forever completely unchanged",
            "Memory lymphocytes from the first infection are already present and can respond immediately",
        ],
        "correct_index": 3,
        "why": "Memory lymphocytes survive after the first infection, so "
               "the antibody response next time is much faster.",
    },
    {
        "id": "ks4-blood-s18",
        "subtopic_slug": "blood",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why haemoglobin releases oxygen in body tissues but "
                "binds it in the lungs.",
        "options": [
            "Oxygen concentration is high in the lungs and low in respiring tissues",
            "Haemoglobin is destroyed by tissues and remade fresh inside the lungs",
            "Body tissues are too cold for haemoglobin to hold onto oxygen",
            "The lungs contain a special enzyme that forces oxygen onto haemoglobin",
        ],
        "correct_index": 0,
        "why": "Haemoglobin binds oxygen where it is plentiful, in the "
               "lungs, and releases it where it is scarce, in respiring "
               "tissues.",
    },
    {
        "id": "ks4-blood-s19",
        "subtopic_slug": "blood",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain the specific role platelets play at the very start "
                "of the clotting process.",
        "options": [
            "They engulf and destroy any bacteria that have already entered through the wound",
            "They produce the antibodies needed to fight any infection entering the wound",
            "They divide rapidly in order to physically plug the whole gap in the vessel wall",
            "They clump together at the site of the wound, triggering the reactions that follow",
        ],
        "correct_index": 3,
        "why": "Platelets clump together first at the wound, triggering the "
               "chemical reactions that go on to form the fibrin clot.",
    },
    {
        "id": "ks4-blood-s20",
        "subtopic_slug": "blood",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A sample of blood is left to settle. Explain what makes up "
                "the pale yellow liquid layer that separates out.",
        "options": [
            "Haemoglobin, which is released from red blood cells as they settle",
            "Plasma, since it is the liquid part of blood that carries dissolved substances",
            "White blood cells, which float to the top as they are less dense",
            "Platelets, since they clump together and rise above the other blood components as it settles",
        ],
        "correct_index": 1,
        "why": "The pale yellow liquid that separates from settled blood is "
               "plasma.",
    },
    {
        "id": "ks4-blood-s21",
        "subtopic_slug": "blood",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A virus mutates so that the shape of its antigen changes. "
                "Predict the effect on a person who has already had this "
                "virus before.",
        "options": [
            "The person becomes completely immune to every possible future virus as a result",
            "Existing antibodies may no longer bind the new antigen shape, so protection is reduced",
            "Their memory lymphocytes would then automatically update themselves to recognise the new antigen shape instantly",
            "The change makes no difference, since all antibodies bind every antigen shape",
        ],
        "correct_index": 1,
        "why": "Antibodies are shape-specific, so a changed antigen shape "
               "may no longer be recognised, reducing the protection "
               "memory cells provide.",
    },
    {
        "id": "ks4-blood-s22",
        "subtopic_slug": "blood",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why white blood cells are not efficient oxygen "
                "carriers, unlike red blood cells.",
        "options": [
            "White blood cells are far too large to enter the smallest capillaries at all",
            "White blood cells actively destroy any haemoglobin that happens to enter them",
            "White blood cells already carry their own completely separate supply of oxygen",
            "Their nucleus and organelles take up space that would otherwise hold haemoglobin",
        ],
        "correct_index": 3,
        "why": "The nucleus and organelles a white blood cell keeps take up "
               "space that a red blood cell instead fills with "
               "haemoglobin.",
    },
    {
        "id": "ks4-blood-s23",
        "subtopic_slug": "blood",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a low platelet count, but a normal white blood "
                "cell count, mainly causes bleeding problems rather than "
                "infections.",
        "options": [
            "White blood cells take over the job of clotting when platelets are low",
            "Platelets and white blood cells both do exactly the same job within the body",
            "A low platelet count always means the white blood cell count is low too",
            "Platelets are involved in clotting, not in defending the body against pathogens",
        ],
        "correct_index": 3,
        "why": "Platelets are specifically for clotting, so a shortage of "
               "them causes bleeding problems while leaving normal white "
               "blood cell defences intact.",
    },
    {
        "id": "ks4-blood-s24",
        "subtopic_slug": "blood",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A blood sample has a volume of 400 cm3. Calculate the "
                "approximate volume of plasma it contains.",
        "options": [
            "120 cm3",
            "180 cm3",
            "220 cm3",
            "280 cm3",
        ],
        "correct_index": 2,
        "why": "Plasma is roughly 55% of blood volume: 55% of 400 cm3 = "
               "220 cm3.",
    },
    {
        "id": "ks4-blood-s25",
        "subtopic_slug": "blood",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A person's bone marrow works normally, but their spleen "
                "has been removed. Predict the effect on the production of "
                "new red blood cells.",
        "options": [
            "Production is unaffected, since new red blood cells are made in the bone marrow",
            "Production stops completely, since the spleen is where new red blood cells are made",
            "Production doubles, since the marrow must replace cells the spleen used to supply",
            "Production moves to the kidneys, which take over the marrow's role once the spleen is gone",
        ],
        "correct_index": 0,
        "why": "New red blood cells are made in the bone marrow, not the "
               "spleen, so production itself is unaffected by the spleen "
               "being removed."
    },
    {
        "id": "ks4-blood-s26",
        "subtopic_slug": "blood",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare a red blood cell with a platelet, in terms of what "
                "each one actually is.",
        "options": [
            "Both of them are actually complete cells, each one containing a fully formed nucleus",
            "A red blood cell is a cell fragment; a platelet is a whole cell without a nucleus",
            "A red blood cell is a whole cell without a nucleus; a platelet is a fragment of a cell",
            "Neither of them is a true cell at all — both are simply fragments of tissue",
        ],
        "correct_index": 2,
        "why": "A red blood cell is a whole cell that has lost its nucleus; "
               "a platelet is only a fragment of a cell.",
    },
    {
        "id": "ks4-blood-h05",
        "subtopic_slug": "blood",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare a red blood cell with a phagocyte in terms of "
                "whether each can divide to replace itself.",
        "options": [
            "A phagocyte, unlike a red blood cell, keeps its nucleus and so can still divide",
            "Neither cell type can ever divide again once it has fully and completely matured",
            "A red blood cell can divide freely, since it has more space without a nucleus",
            "Both cell types divide at exactly the same rate throughout their lifetime",
        ],
        "correct_index": 0,
        "why": "Keeping a nucleus is what lets a phagocyte still divide, "
               "unlike a red blood cell, which has lost its nucleus.",
    },
    {
        "id": "ks4-blood-h06",
        "subtopic_slug": "blood",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate this claim: 'A raised white blood cell count "
                "always means a person has an infection.'",
        "options": [
            "True, since white blood cells are never raised for any other reason at all",
            "False — a raised count usually suggests infection, but is not absolute certainty",
            "True, but only because infections are the only thing white blood cells respond to",
            "False, since white blood cells always stay at a fixed number throughout life",
        ],
        "correct_index": 1,
        "why": "A raised white blood cell count is strong evidence of "
               "infection, but is a signal, not proof — other things can "
               "raise it too.",
    },
    {
        "id": "ks4-blood-h07",
        "subtopic_slug": "blood",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why the first antibody response to a brand-new "
                "pathogen can take several days to build up.",
        "options": [
            "Phagocytes must be destroyed first before any lymphocyte can begin to respond",
            "Antibodies dissolve almost as fast as they are made during a first infection",
            "The one matching lymphocyte must first be found and then multiply into large numbers",
            "The pathogen must multiply for several days before the immune system notices it",
        ],
        "correct_index": 2,
        "why": "Only one lymphocyte type matches a given antigen, so it "
               "takes time for that one type to be found and multiply into "
               "large enough numbers.",
    },
    {
        "id": "ks4-blood-h08",
        "subtopic_slug": "blood",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A mutation stops a person's lymphocytes from ever forming "
                "memory cells after an infection. Predict the effect.",
        "options": [
            "Every infection would now be fought off before symptoms could ever develop",
            "The person would become permanently immune to all pathogens instead",
            "Phagocytes would take over the antibody-making role that the lymphocytes usually have",
            "Each infection with the same pathogen would be fought off as slowly as the first time",
        ],
        "correct_index": 3,
        "why": "Without memory cells there is no faster second response, so "
               "every repeat infection would be fought off as slowly as "
               "the first.",
    },
    {
        "id": "ks4-blood-h09",
        "subtopic_slug": "blood",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A patient has an unusually low platelet count. Predict the "
                "effect on a minor cut.",
        "options": [
            "Bleeding continues for much longer, since a clot forms slowly or not at all",
            "The cut heals faster, since fewer platelets means less blockage at the wound",
            "White blood cells clot the wound instead, at exactly the same speed",
            "The wound becomes far more likely to develop into a large tumour",
        ],
        "correct_index": 0,
        "why": "With too few platelets, a stable clot forms slowly or not "
               "at all, so bleeding continues for longer than normal.",
    },
    {
        "id": "ks4-blood-h10",
        "subtopic_slug": "blood",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate this claim: 'Plasma is mostly water, so it cannot "
                "be carrying anything biologically important.'",
        "options": [
            "True — water cannot dissolve or carry biologically important substances at all",
            "False — plasma dissolves and carries glucose, urea, hormones, antibodies and heat",
            "True, but only because dissolved substances never actually reach their target organs",
            "False, but only because plasma is not actually made mostly of water at all",
        ],
        "correct_index": 1,
        "why": "Water is an excellent solvent, and plasma uses this to "
               "carry glucose, urea, hormones, antibodies and heat around "
               "the body.",
    },
    {
        "id": "ks4-blood-h11",
        "subtopic_slug": "blood",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare the effect of losing a volume of blood with the "
                "effect of carbon monoxide binding to a similar proportion "
                "of the haemoglobin that remains.",
        "options": [
            "Losing blood is always more dangerous, since carbon monoxide never actually reduces oxygen delivery",
            "Carbon monoxide has no effect on oxygen delivery, since it binds to plasma rather than haemoglobin",
            "Both reduce the oxygen delivered to tissues by a similar amount, just through different mechanisms",
            "Neither has any real effect on oxygen delivery, since the body compensates instantly",
        ],
        "correct_index": 2,
        "why": "Losing blood removes haemoglobin along with it, while "
               "carbon monoxide leaves the haemoglobin in place but unable "
               "to carry oxygen — both cut oxygen delivery by a similar "
               "amount.",
    },
    {
        "id": "ks4-blood-h12",
        "subtopic_slug": "blood",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why an antibody made against one pathogen almost "
                "never binds to an unrelated pathogen's antigen by "
                "accident.",
        "options": [
            "Antibodies are destroyed before they get the chance to meet an unrelated pathogen",
            "Unrelated pathogens never actually carry any antigens on their surface at all",
            "All antibodies happen to have completely identical shapes to one another",
            "An antibody's shape is so specific that it only fits one particular antigen shape",
        ],
        "correct_index": 3,
        "why": "An antibody's shape is specific to one antigen, which is "
               "why it very rarely binds an unrelated pathogen's antigen "
               "by accident.",
    },
    {
        "id": "ks4-blood-h13",
        "subtopic_slug": "blood",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A person loses a small amount of blood every day over "
                "several months. Predict the long-term effect if bone "
                "marrow cannot keep up.",
        "options": [
            "Red blood cell numbers fall gradually, reducing how much oxygen the blood can carry",
            "White blood cell numbers rise sharply to compensate for the lost red blood cells",
            "Plasma volume falls to zero, since it is the first component to be lost",
            "Platelet numbers double automatically to seal the source of the bleeding",
        ],
        "correct_index": 0,
        "why": "If replacement cannot keep pace with the daily loss, red "
               "blood cell numbers gradually fall, cutting how much "
               "oxygen the blood can carry.",
    },
    {
        "id": "ks4-blood-h14",
        "subtopic_slug": "blood",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate this claim: 'Since platelets have no nucleus, they "
                "cannot do anything active in the body.'",
        "options": [
            "True — a nucleus is required for absolutely any activity a cell fragment carries out",
            "False — platelets actively clump together and trigger clotting despite having no nucleus",
            "True, but only because platelets are technically not part of the blood at all",
            "False, but only because platelets actually do still contain a full nucleus",
        ],
        "correct_index": 1,
        "why": "Platelets have no nucleus but are still active — they clump "
               "together at a wound and trigger the reactions that form a "
               "clot.",
    },
    {
        "id": "ks4-blood-h15",
        "subtopic_slug": "blood",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare how long memory lymphocytes last in the body with "
                "how long the antibodies from one infection last.",
        "options": [
            "Both last for exactly the same length of time, often only a few weeks",
            "Antibodies last for years, while memory lymphocytes disappear within days",
            "Memory lymphocytes can last for years, while the antibody level itself falls much sooner",
            "Neither one lasts beyond the infection itself; both disappear within hours of recovery",
        ],
        "correct_index": 2,
        "why": "Memory lymphocytes can persist for years, ready to respond "
               "quickly, even once the antibody level from the original "
               "infection has fallen.",
    },
    {
        "id": "ks4-blood-h16",
        "subtopic_slug": "blood",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A mutation stops phagocytes from being able to engulf "
                "pathogens, though lymphocytes work normally. Predict the "
                "effect.",
        "options": [
            "Infections would still be fought off exactly as quickly and just as easily as they always were before",
            "Lymphocytes would then take over the job of engulfing pathogens directly instead",
            "The body would become completely and permanently immune to every pathogen instead",
            "Early, non-specific defence would be lost, though antibodies could still eventually clear infections",
        ],
        "correct_index": 3,
        "why": "Losing phagocytes removes the fast, non-specific first "
               "defence, but the slower, specific antibody response from "
               "lymphocytes could still clear an infection eventually.",
    },
    {
        "id": "ks4-blood-h17",
        "subtopic_slug": "blood",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate this claim: 'Because urea is found dissolved in "
                "plasma, the blood itself must produce urea.'",
        "options": [
            "False — the liver produces urea, and plasma merely carries it onward to the kidneys",
            "True — any substance dissolved in plasma must have been produced by the blood itself",
            "True, but only because red blood cells specifically manufacture the urea",
            "False, but only because urea is not actually found in plasma at all",
        ],
        "correct_index": 0,
        "why": "Plasma only transports urea; it is the liver that actually "
               "produces it, carrying it onward to the kidneys.",
    },
    {
        "id": "ks4-blood-h18",
        "subtopic_slug": "blood",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A condition destroys all of a person's white blood cells, "
                "while red blood cells and platelets stay normal. Predict "
                "the main risk.",
        "options": [
            "Oxygen delivery to tissues fails almost immediately in this case",
            "The person becomes extremely vulnerable to infections, with no phagocytes or lymphocytes left",
            "Wounds no longer clot, leading to dangerous and uncontrolled bleeding",
            "Blood pressure drops sharply, since white blood cells maintain vessel pressure",
        ],
        "correct_index": 1,
        "why": "White blood cells are the body's pathogen defence, so "
               "losing all of them leaves a person extremely vulnerable to "
               "infection, even with normal red blood cells and platelets.",
    },
    {
        "id": "ks4-blood-h19",
        "subtopic_slug": "blood",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare the immediate consequence of losing a large volume "
                "of plasma with losing the same volume of red blood cells.",
        "options": [
            "Both produce identical symptoms, since plasma and red blood cells serve exactly the same function",
            "Losing red blood cells is never noticeable, since plasma carries all essential substances",
            "Losing plasma affects blood volume and pressure; losing red blood cells affects oxygen delivery",
            "Losing plasma has no effect at all, since it is only 55% water by volume",
        ],
        "correct_index": 2,
        "why": "Each component has a different job, so losing plasma "
               "mainly disrupts blood volume and pressure, while losing "
               "red blood cells mainly disrupts oxygen delivery.",
    },
    {
        "id": "ks4-blood-h20",
        "subtopic_slug": "blood",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why the immune system sometimes produces antibodies "
                "against a harmless substance, causing unnecessary "
                "symptoms.",
        "options": [
            "Phagocytes would mistakenly digest the harmless substance instead of any actual real pathogen that might be present nearby",
            "Memory lymphocytes from some past infection wrongly reactivate for absolutely no reason",
            "Plasma proteins bind to the harmless substance and trigger clotting by complete mistake",
            "A lymphocyte's antibody happens to match the shape of the harmless substance closely enough to trigger a response",
        ],
        "correct_index": 3,
        "why": "If an antibody's shape happens to match part of a harmless "
               "substance closely enough, it can trigger a full immune "
               "response even though there is no real pathogen present.",
    },
    {
        "id": "ks4-blood-h21",
        "subtopic_slug": "blood",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate this claim: 'Because a red blood cell has no "
                "nucleus, it can go on working for as long as the person "
                "lives.'",
        "options": [
            "False — with no nucleus it cannot make new proteins to repair itself, so it wears out and is replaced",
            "True — a cell with no nucleus has nothing left in it that is able to wear out or be damaged",
            "True, since the bone marrow repairs each red blood cell in turn as it passes back through",
            "False, because a red blood cell grows itself a replacement nucleus once its haemoglobin starts to fail",
        ],
        "correct_index": 0,
        "why": "Without a nucleus a red blood cell cannot make new proteins "
               "to repair itself, so it wears out and has to be broken down "
               "and replaced."
    },
    {
        "id": "ks4-blood-h22",
        "subtopic_slug": "blood",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare what a red blood cell transports with what plasma "
                "transports.",
        "options": [
            "Both transport exactly the same substances, just using different methods",
            "A red blood cell mainly transports oxygen; plasma transports many dissolved substances instead",
            "A red blood cell actually transports urea instead; plasma transports oxygen using dissolved haemoglobin molecules",
            "Neither actually transports anything; both simply exist to fill space in the blood",
        ],
        "correct_index": 1,
        "why": "A red blood cell's job is carrying oxygen, while plasma "
               "carries a wide range of other dissolved substances.",
    },
    {
        "id": "ks4-blood-h23",
        "subtopic_slug": "blood",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest how plasma helps the body respond when muscles "
                "generate extra heat during exercise.",
        "options": [
            "Plasma cools the muscles directly by evaporating from their surface",
            "Plasma stops carrying heat during exercise, to protect the muscles from overheating",
            "Plasma carries the extra heat away from the muscles to other parts of the body",
            "Plasma converts the extra heat directly into extra glucose for the muscles to use",
        ],
        "correct_index": 2,
        "why": "Plasma distributes heat produced by active muscles to other "
               "parts of the body, helping regulate body temperature.",
    },
    {
        "id": "ks4-blood-h24",
        "subtopic_slug": "blood",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Severe dehydration reduces the water content of a person's "
                "plasma. Predict the effect on blood flow.",
        "options": [
            "Blood becomes thinner overall and flows much faster through even the narrowest capillaries",
            "Red blood cells multiply rapidly to replace the lost plasma volume",
            "White blood cells become unable to recognise any antigens at all",
            "Blood becomes thicker and more concentrated, making it harder to pump around the body",
        ],
        "correct_index": 3,
        "why": "Losing water from plasma concentrates the blood, making it "
               "thicker and harder for the heart to pump around the body.",
    },
    {
        "id": "ks4-blood-h25",
        "subtopic_slug": "blood",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate this claim: 'Phagocytes are less useful than "
                "lymphocytes, since they cannot target one specific "
                "pathogen.'",
        "options": [
            "Not necessarily — being non-specific lets phagocytes respond immediately to any pathogen at all",
            "True — a non-specific defence can never actually remove a real pathogen",
            "True, but only because phagocytes are technically a type of lymphocyte",
            "Not necessarily, but this is only because phagocytes secretly do target one single specific pathogen",
        ],
        "correct_index": 0,
        "why": "Being non-specific is a strength, not a weakness, since it "
               "lets a phagocyte respond immediately to whatever pathogen "
               "it meets, without waiting to recognise it first.",
    },
    {
        "id": "ks4-blood-h26",
        "subtopic_slug": "blood",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A rare condition means a person's blood can never form "
                "fibrin. Predict the effect of even a small cut.",
        "options": [
            "Platelets alone are able to seal the wound completely, so nothing else changes",
            "Bleeding continues for a dangerously long time, since no stable clot can ever form",
            "White blood cells replace the missing fibrin and seal the wound instead",
            "The wound heals faster, since fibrin normally only slows the healing process down",
        ],
        "correct_index": 1,
        "why": "Fibrin is what forms the mesh that traps cells into a "
               "stable clot, so without it a cut would bleed for a "
               "dangerously long time.",
    },

    # ══════════════════════════════════════════════════════════════════
    # coronary-heart-disease · e05-e12, s05-s26, h05-h26
    # ══════════════════════════════════════════════════════════════════
    {
        "id": "ks4-coronary-heart-disease-e05",
        "subtopic_slug": "coronary-heart-disease",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what angioplasty involves.",
        "options": [
            "Passing a thin tube through a blood vessel to reach the narrowed artery",
            "Injecting cholesterol-lowering drugs directly into the heart muscle",
            "Grafting a vein from the leg around the blocked artery",
            "Transplanting a healthy donor heart into the chest",
        ],
        "correct_index": 0,
        "why": "Angioplasty passes a thin tube through a blood vessel to "
               "reach the narrowed section, where a stent is then fitted.",
    },
    {
        "id": "ks4-coronary-heart-disease-e06",
        "subtopic_slug": "coronary-heart-disease",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State a known side effect of taking statins.",
        "options": [
            "Permanent hair loss",
            "Muscle pain",
            "Loss of taste",
            "Blurred vision",
        ],
        "correct_index": 1,
        "why": "Muscle pain is a recognised side effect statins can cause "
               "in some patients.",
    },
    {
        "id": "ks4-coronary-heart-disease-e07",
        "subtopic_slug": "coronary-heart-disease",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State where the healthy blood vessel used in bypass "
                "surgery usually comes from.",
        "options": [
            "The lung",
            "The brain",
            "The leg",
            "The kidney",
        ],
        "correct_index": 2,
        "why": "A vein taken from the leg is commonly used as the graft in "
               "bypass surgery.",
    },
    {
        "id": "ks4-coronary-heart-disease-e08",
        "subtopic_slug": "coronary-heart-disease",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State how the risk of coronary heart disease generally "
                "changes with age.",
        "options": [
            "It falls steadily throughout life",
            "It stays exactly the same at every age",
            "It rises sharply in childhood, then falls",
            "It rises as a person gets older",
        ],
        "correct_index": 3,
        "why": "Age is a risk factor for coronary heart disease: risk "
               "rises as a person gets older.",
    },
    {
        "id": "ks4-coronary-heart-disease-e09",
        "subtopic_slug": "coronary-heart-disease",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State how the risk of coronary heart disease compares "
                "between men and women at a younger age.",
        "options": [
            "It is generally higher in men",
            "It is generally higher in women",
            "It is exactly identical for both",
            "It only affects men, never women",
        ],
        "correct_index": 0,
        "why": "Men tend to develop coronary heart disease at younger ages "
               "than women, though risk equalises later in life.",
    },
    {
        "id": "ks4-coronary-heart-disease-e10",
        "subtopic_slug": "coronary-heart-disease",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State how high blood pressure raises the risk of coronary "
                "heart disease.",
        "options": [
            "It cools the blood, slowing the heart down",
            "It damages the artery walls, making plaques more likely",
            "It dissolves the fatty plaques that form",
            "It increases the number of red blood cells produced",
        ],
        "correct_index": 1,
        "why": "High blood pressure damages artery walls, making them more "
               "susceptible to plaque formation.",
    },
    {
        "id": "ks4-coronary-heart-disease-e11",
        "subtopic_slug": "coronary-heart-disease",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State which substance in the blood statins mainly reduce.",
        "options": [
            "Glucose",
            "Urea",
            "LDL cholesterol",
            "Haemoglobin",
        ],
        "correct_index": 2,
        "why": "Statins work by reducing the level of LDL cholesterol in "
               "the blood.",
    },
    {
        "id": "ks4-coronary-heart-disease-e12",
        "subtopic_slug": "coronary-heart-disease",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State one risk factor for coronary heart disease that "
                "cannot be changed.",
        "options": [
            "Smoking",
            "Diet",
            "Exercise level",
            "Genetics",
        ],
        "correct_index": 3,
        "why": "Genetics is a non-modifiable risk factor, unlike lifestyle "
               "choices such as smoking, diet and exercise.",
    },
    {
        "id": "ks4-coronary-heart-disease-s05",
        "subtopic_slug": "coronary-heart-disease",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Classify smoking and family history as risk factors for "
                "coronary heart disease.",
        "options": [
            "Smoking is a modifiable risk factor; family history is not",
            "Both are modifiable risk factors that a person can control",
            "Family history is modifiable; smoking is not",
            "Neither one is actually a risk factor for coronary heart disease",
        ],
        "correct_index": 0,
        "why": "Smoking is a lifestyle choice that can be changed; family "
               "history is inherited and cannot be.",
    },
    {
        "id": "ks4-coronary-heart-disease-s06",
        "subtopic_slug": "coronary-heart-disease",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why obesity raises the risk of coronary heart "
                "disease.",
        "options": [
            "It blocks the coronary arteries directly with fat cells carried from the diet",
            "It raises blood pressure and cholesterol, both of which damage arteries",
            "It slows the heart rate to a dangerously low level",
            "It stops statins from working in the bloodstream",
        ],
        "correct_index": 1,
        "why": "Obesity is linked to higher blood pressure and cholesterol, "
               "both of which raise coronary heart disease risk.",
    },
    {
        "id": "ks4-coronary-heart-disease-s07",
        "subtopic_slug": "coronary-heart-disease",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain how a diet high in saturated fat increases the "
                "risk of coronary heart disease.",
        "options": [
            "It lowers blood pressure to an unsafe level, so the heart has to beat harder",
            "It reduces the number of red blood cells made",
            "It raises blood cholesterol, which builds up as plaques in artery walls",
            "It directly damages the heart valves",
        ],
        "correct_index": 2,
        "why": "A high-fat diet raises blood cholesterol, which can build "
               "up as plaques in the artery walls.",
    },
    {
        "id": "ks4-coronary-heart-disease-s08",
        "subtopic_slug": "coronary-heart-disease",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain how a lack of exercise increases the risk of "
                "coronary heart disease.",
        "options": [
            "It stops the heart producing red blood cells",
            "It thickens the artery walls through simple disuse of the muscle",
            "It lowers cholesterol levels far too much",
            "It contributes to obesity and higher cholesterol over time",
        ],
        "correct_index": 3,
        "why": "Physical inactivity contributes to obesity and raised "
               "cholesterol, both of which raise coronary heart disease "
               "risk.",
    },
    {
        "id": "ks4-coronary-heart-disease-s09",
        "subtopic_slug": "coronary-heart-disease",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Distinguish angioplasty (used to fit a stent) from bypass "
                "surgery.",
        "options": [
            "Angioplasty reaches the artery through a tube; bypass surgery is open surgery using a grafted vessel",
            "Both procedures use exactly the same surgical method",
            "Angioplasty is open surgery on the chest; bypass surgery threads a thin tube along to the artery",
            "Neither procedure actually reaches the coronary arteries",
        ],
        "correct_index": 0,
        "why": "Angioplasty threads a tube through a vessel to fit a stent, "
               "while bypass surgery is open surgery using a grafted "
               "vessel.",
    },
    {
        "id": "ks4-coronary-heart-disease-s10",
        "subtopic_slug": "coronary-heart-disease",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a smoker who also eats a high-fat diet has a "
                "higher risk than either factor alone would suggest.",
        "options": [
            "The two risk factors cancel each other out completely",
            "Risk factors add together, so combined exposure raises risk further",
            "Only the more recent of a person's risk factors counts towards their overall risk",
            "Diet has no effect at all once a person already smokes",
        ],
        "correct_index": 1,
        "why": "Risk factors add together, so a person exposed to two of "
               "them carries a higher combined risk than either alone.",
    },
    {
        "id": "ks4-coronary-heart-disease-s11",
        "subtopic_slug": "coronary-heart-disease",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare how quickly statins and stents each act on "
                "coronary heart disease.",
        "options": [
            "Both act within seconds of being taken or fitted",
            "Statins act immediately on blood flow; a stent takes years to have any effect at all",
            "A stent restores blood flow immediately; statins act slowly over the long term",
            "Neither has any effect on blood flow at any point",
        ],
        "correct_index": 2,
        "why": "A stent restores flow the moment it is fitted, while "
               "statins work slowly over months and years to slow plaque "
               "build-up.",
    },
    {
        "id": "ks4-coronary-heart-disease-s12",
        "subtopic_slug": "coronary-heart-disease",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a heart transplant is considered only as a "
                "last resort.",
        "options": [
            "It is the cheapest treatment, so it is used first instead",
            "It removes the need for any further medication afterwards",
            "It can be carried out immediately, since no donor or waiting period is involved",
            "It is major surgery with real risks, and requires a suitable donor heart",
        ],
        "correct_index": 3,
        "why": "A transplant carries major surgical risk and depends on a "
               "suitable donor becoming available, so it is only used once "
               "other treatments cannot help.",
    },
    {
        "id": "ks4-coronary-heart-disease-s13",
        "subtopic_slug": "coronary-heart-disease",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A patient with a strong family history of coronary heart "
                "disease still has a raised risk even after adopting a very "
                "healthy lifestyle. Suggest why.",
        "options": [
            "Their family history of the disease cannot be changed by lifestyle",
            "Lifestyle changes always remove every risk factor completely",
            "Statins are not effective for patients with a healthy lifestyle",
            "A healthy lifestyle actually raises the risk in some patients",
        ],
        "correct_index": 0,
        "why": "Family history is a non-modifiable risk factor, so no "
               "lifestyle change can remove the risk it adds.",
    },
    {
        "id": "ks4-coronary-heart-disease-s14",
        "subtopic_slug": "coronary-heart-disease",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why coronary heart disease often develops over "
                "many years before symptoms appear.",
        "options": [
            "Statins prevent symptoms until treatment eventually stops",
            "Plaques build up gradually, only reducing blood flow noticeably once they are large",
            "The coronary arteries regrow completely every few years",
            "Symptoms only appear once a person turns seventy, whatever their arteries are like",
        ],
        "correct_index": 1,
        "why": "Plaques accumulate gradually over years, so blood flow "
               "only becomes noticeably restricted once narrowing is "
               "significant.",
    },
    {
        "id": "ks4-coronary-heart-disease-s15",
        "subtopic_slug": "coronary-heart-disease",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why statins specifically target LDL cholesterol "
                "rather than cholesterol in general.",
        "options": [
            "All types of cholesterol are identical, so targeting any type works",
            "LDL cholesterol has no connection to coronary heart disease at all",
            "LDL cholesterol is the type most linked to plaque formation in arteries",
            "Statins cannot distinguish between different types of cholesterol",
        ],
        "correct_index": 2,
        "why": "LDL cholesterol is the type most closely linked to plaque "
               "formation, which is why statins specifically target it.",
    },
    {
        "id": "ks4-coronary-heart-disease-s16",
        "subtopic_slug": "coronary-heart-disease",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why the difference in coronary heart disease risk "
                "between men and women becomes smaller after menopause.",
        "options": [
            "Men's risk falls sharply once they reach the age at which women reach menopause",
            "Statins become more effective in women after menopause",
            "Genetics changes completely once a woman reaches menopause",
            "A hormone that had been protective in women becomes less available after menopause",
        ],
        "correct_index": 3,
        "why": "A hormone that offers some protection before menopause "
               "becomes less available afterwards, narrowing the "
               "difference in risk between men and women.",
    },
    {
        "id": "ks4-coronary-heart-disease-s17",
        "subtopic_slug": "coronary-heart-disease",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a partially narrowed coronary artery can cause "
                "chest pain during exercise but not at rest.",
        "options": [
            "Exercise raises the heart's oxygen demand beyond what the narrowed artery can supply",
            "Exercise always closes the coronary arteries completely",
            "Rest increases the heart's demand for oxygen far more than any exercise ever does",
            "Chest pain during exercise is unrelated to the coronary arteries",
        ],
        "correct_index": 0,
        "why": "Exercise raises the heart's demand for oxygen, and a "
               "narrowed artery may not supply enough to meet that raised "
               "demand.",
    },
    {
        "id": "ks4-coronary-heart-disease-s18",
        "subtopic_slug": "coronary-heart-disease",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a patient who has already had one stent fitted "
                "may need another one fitted in a different artery later.",
        "options": [
            "The first stent eventually stops working and has to be replaced elsewhere",
            "Atherosclerosis can continue narrowing other arteries elsewhere in the heart",
            "Stents can only ever be fitted once in a person's lifetime",
            "A second stent is always fitted purely as a precaution",
        ],
        "correct_index": 1,
        "why": "A stent only treats one narrowed section; atherosclerosis "
               "can continue narrowing other arteries elsewhere.",
    },
    {
        "id": "ks4-coronary-heart-disease-s19",
        "subtopic_slug": "coronary-heart-disease",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why quitting smoking lowers a person's risk of "
                "coronary heart disease even years after they have already "
                "smoked for a long time.",
        "options": [
            "Quitting reverses all of the damage already done to the arteries instantly",
            "Quitting stops further damage, even though existing plaques remain",
            "Quitting only helps if a person has never smoked at all",
            "Quitting has no effect on coronary heart disease risk",
        ],
        "correct_index": 1,
        "why": "Quitting stops the ongoing damage smoking causes, even "
               "though plaques that have already formed generally remain.",
    },
    {
        "id": "ks4-coronary-heart-disease-s20",
        "subtopic_slug": "coronary-heart-disease",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why a vein from the leg, rather than an artery, is "
                "often used for a coronary bypass graft.",
        "options": [
            "Leg veins carry no blood at all, so one can be removed with no effect whatever",
            "Leg veins are far too narrow to be used in this way",
            "Arteries cannot be grafted anywhere else in the body",
            "A leg vein can be removed without seriously affecting blood flow to the leg",
        ],
        "correct_index": 3,
        "why": "A leg vein can be spared without seriously disrupting blood "
               "flow in the leg, which is not true of most arteries.",
    },
    {
        "id": "ks4-coronary-heart-disease-s21",
        "subtopic_slug": "coronary-heart-disease",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Rank statins, a stent, and bypass surgery from least to "
                "most invasive.",
        "options": [
            "Statins, a stent, bypass surgery",
            "A stent, statins, bypass surgery",
            "Bypass surgery, a stent, statins",
            "A stent, bypass surgery, statins",
        ],
        "correct_index": 0,
        "why": "Statins are a daily tablet, a stent is fitted by a "
               "minimally invasive procedure, and bypass surgery is major "
               "open surgery — increasing invasiveness in that order.",
    },
    {
        "id": "ks4-coronary-heart-disease-s22",
        "subtopic_slug": "coronary-heart-disease",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest the effect of a patient stopping their statin "
                "medication without any other lifestyle change.",
        "options": [
            "Cholesterol has no chance of rising again, since the damage is already done",
            "Cholesterol may begin rising again, since the drug is no longer lowering it",
            "The existing plaques disappear completely once the drug is stopped",
            "Blood pressure drops permanently, regardless of the statin being stopped",
        ],
        "correct_index": 1,
        "why": "Without the statin's effect, cholesterol may begin rising "
               "again, since nothing else about the patient's situation "
               "has changed.",
    },
    {
        "id": "ks4-coronary-heart-disease-s23",
        "subtopic_slug": "coronary-heart-disease",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why narrowing specifically in the coronary arteries "
                "is so dangerous, compared with narrowing elsewhere in the "
                "body.",
        "options": [
            "The coronary arteries carry blood to the brain, not the heart",
            "Narrowing anywhere in the body is equally dangerous",
            "The coronary arteries supply the heart muscle itself, which cannot stop working",
            "The coronary arteries are the only vessels in the body at no risk of narrowing",
        ],
        "correct_index": 2,
        "why": "The coronary arteries supply the heart muscle itself, "
               "which must keep working continuously, making any "
               "narrowing there especially dangerous.",
    },
    {
        "id": "ks4-coronary-heart-disease-s24",
        "subtopic_slug": "coronary-heart-disease",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare a patient with one risk factor for coronary heart "
                "disease to a patient with four risk factors.",
        "options": [
            "Both patients have exactly the same overall risk",
            "The patient with one risk factor has the higher overall risk",
            "Risk factors do not add together at all, so having four is no worse than one",
            "The patient with four risk factors has a considerably higher overall risk",
        ],
        "correct_index": 3,
        "why": "Risk factors add together, so a patient with four of them "
               "carries a considerably higher overall risk than one with "
               "only a single risk factor.",
    },
    {
        "id": "ks4-coronary-heart-disease-s25",
        "subtopic_slug": "coronary-heart-disease",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why doctors still prescribe statins to many "
                "patients despite the risk of muscle pain as a side "
                "effect.",
        "options": [
            "The reduction in heart attack risk generally outweighs the side effect for most patients",
            "Muscle pain is actually a sign that the statin is not working",
            "Statins are prescribed only to those patients who already suffer from muscle pain in the legs",
            "The side effect only ever affects patients who do not need the drug",
        ],
        "correct_index": 0,
        "why": "For most patients, the reduction in heart attack risk from "
               "taking a statin outweighs the risk of the side effect.",
    },
    {
        "id": "ks4-coronary-heart-disease-s26",
        "subtopic_slug": "coronary-heart-disease",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare genetics and age as risk factors for coronary "
                "heart disease.",
        "options": [
            "Both can be changed through diet and exercise alone",
            "Both are risk factors that cannot be modified, though age affects everyone equally over time",
            "Genetics is modifiable; age is not",
            "Neither genetics nor age is linked to coronary heart disease in any real way that has been measured",
        ],
        "correct_index": 1,
        "why": "Genetics and age are both non-modifiable risk factors, "
               "though age is one that every person experiences over "
               "time.",
    },
    {
        "id": "ks4-coronary-heart-disease-h05",
        "subtopic_slug": "coronary-heart-disease",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate this claim: 'Because statins prevent further "
                "plaque build-up, patients never need a stent once they "
                "start taking statins.'",
        "options": [
            "False — statins cannot restore flow through an artery already severely narrowed",
            "True — statins dissolve any plaque that has already formed",
            "True, since a stent only works in a patient who has never taken any statins",
            "False, but only because statins are never actually effective at all",
        ],
        "correct_index": 0,
        "why": "Statins slow further build-up but cannot restore flow "
               "through an artery already badly narrowed, which is exactly "
               "what a stent is for.",
    },
    {
        "id": "ks4-coronary-heart-disease-h06",
        "subtopic_slug": "coronary-heart-disease",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A heavy smoker with early-stage atherosclerosis quits "
                "smoking completely. Predict the long-term effect on their "
                "coronary arteries.",
        "options": [
            "The existing plaques instantly disappear once smoking stops",
            "Further damage slows, though the plaques already formed generally remain",
            "The arteries return to a completely healthy state within a few days",
            "Quitting smoking has no effect once atherosclerosis has begun",
        ],
        "correct_index": 1,
        "why": "Quitting removes the ongoing cause of further damage, but "
               "the plaques that have already formed generally remain in "
               "place.",
    },
    {
        "id": "ks4-coronary-heart-disease-h07",
        "subtopic_slug": "coronary-heart-disease",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate this claim: 'Since age and sex cannot be changed, "
                "doctors should ignore them when assessing a patient's "
                "risk.'",
        "options": [
            "True — only the modifiable risk factors are of any use at all in assessing a patient's overall risk",
            "True, since unmodifiable risk factors never actually affect real risk",
            "False — unmodifiable risk factors still add to overall risk and inform how it is managed",
            "False, but only because age and sex are technically modifiable after all",
        ],
        "correct_index": 2,
        "why": "Even a risk factor that cannot be changed still adds to a "
               "patient's overall risk, and knowing it helps a doctor "
               "decide how closely to monitor and treat them.",
    },
    {
        "id": "ks4-coronary-heart-disease-h08",
        "subtopic_slug": "coronary-heart-disease",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A patient who already has a stent fitted then develops "
                "high blood pressure. Predict the effect on their risk.",
        "options": [
            "Risk falls, since the stent already protects that artery completely",
            "Risk stays exactly the same, since blood pressure has no link at all to coronary heart disease",
            "The stent is removed automatically once blood pressure rises",
            "Risk rises further, since high blood pressure can damage other arteries the stent does not cover",
        ],
        "correct_index": 3,
        "why": "A stent only treats one artery; high blood pressure can go "
               "on damaging other arteries the stent does not cover, "
               "raising overall risk further.",
    },
    {
        "id": "ks4-coronary-heart-disease-h09",
        "subtopic_slug": "coronary-heart-disease",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest one reason a doctor might recommend bypass surgery "
                "rather than a stent for a patient with several severely "
                "narrowed arteries.",
        "options": [
            "A single bypass operation can address several narrowed arteries at once, unlike one stent",
            "Bypass surgery is always a smaller, much less invasive procedure than fitting a stent",
            "Stents can only ever be used on patients under the age of thirty",
            "Bypass surgery removes the need for the patient to have a heart at all",
        ],
        "correct_index": 0,
        "why": "A single bypass operation can reroute blood around several "
               "narrowed arteries at once, where fitting several stents "
               "might otherwise be needed.",
    },
    {
        "id": "ks4-coronary-heart-disease-h10",
        "subtopic_slug": "coronary-heart-disease",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate this claim: 'Coronary heart disease only ever "
                "affects elderly people.'",
        "options": [
            "True — no case of coronary heart disease has ever been recorded in a younger patient at all",
            "False — age raises risk, but younger patients with other risk factors can still develop it",
            "True, since arteries cannot narrow before a person turns sixty-five",
            "False, but only because age is not actually a risk factor at all",
        ],
        "correct_index": 1,
        "why": "Age raises risk, but it is one factor among several — a "
               "younger person with other risk factors can still develop "
               "coronary heart disease.",
    },
    {
        "id": "ks4-coronary-heart-disease-h11",
        "subtopic_slug": "coronary-heart-disease",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A patient quits smoking and starts taking statins at the "
                "same time. Compare the likely combined effect on their "
                "risk with quitting smoking alone.",
        "options": [
            "The combined effect is identical to quitting smoking on its own",
            "Starting statins actually cancels out the benefit of quitting smoking",
            "The combined effect reduces risk further than either change alone would",
            "Only the more recently made change has any effect on overall risk",
        ],
        "correct_index": 2,
        "why": "Since risk factors add together, removing more than one at "
               "once reduces overall risk further than removing just one.",
    },
    {
        "id": "ks4-coronary-heart-disease-h12",
        "subtopic_slug": "coronary-heart-disease",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why a doctor still recommends lifestyle changes to "
                "a patient even after they have had a stent successfully "
                "fitted.",
        "options": [
            "Lifestyle changes are only of any use before a patient has been given any treatment at all",
            "A stent removes every risk factor the patient previously had",
            "Lifestyle advice is given purely out of habit, with no real benefit",
            "The underlying atherosclerosis can still continue in other arteries the stent does not treat",
        ],
        "correct_index": 3,
        "why": "A stent fixes one narrowed section mechanically, but the "
               "atherosclerosis that caused it can still continue "
               "elsewhere unless lifestyle risk factors are addressed.",
    },
    {
        "id": "ks4-coronary-heart-disease-h13",
        "subtopic_slug": "coronary-heart-disease",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate this claim: 'Bypass surgery repairs the original "
                "blocked coronary artery.'",
        "options": [
            "False — the graft creates an entirely new route; the original blocked artery is left as it is",
            "True — the surgery removes the blockage from inside the original artery",
            "True, but only because the graft is threaded inside the original blocked artery itself to reopen it",
            "False, but only because bypass surgery does not actually treat the heart",
        ],
        "correct_index": 0,
        "why": "Bypass surgery creates an entirely new route around the "
               "blocked section; the original artery itself is not "
               "repaired.",
    },
    {
        "id": "ks4-coronary-heart-disease-h14",
        "subtopic_slug": "coronary-heart-disease",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A patient has untreated high cholesterol and high blood "
                "pressure for many years. Predict the state of their "
                "coronary arteries by the time symptoms appear.",
        "options": [
            "Their arteries will show no more narrowing than those of a person with neither of the two factors",
            "Their arteries are likely to be significantly more narrowed than with just one of these factors",
            "The two risk factors will have cancelled each other out completely",
            "Only the cholesterol will have had any real effect on their arteries",
        ],
        "correct_index": 1,
        "why": "Two risk factors acting together over many years are "
               "likely to cause significantly more narrowing than either "
               "one alone.",
    },
    {
        "id": "ks4-coronary-heart-disease-h15",
        "subtopic_slug": "coronary-heart-disease",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Two patients have the same diet and exercise habits. One "
                "has a family history of coronary heart disease and one "
                "does not. Compare their overall risk.",
        "options": [
            "Both patients have exactly the same risk, since lifestyle is the only factor that ever matters",
            "The patient with no family history actually has the higher risk",
            "The patient with a family history has a higher overall risk, from that added non-lifestyle factor",
            "Neither patient has any measurable risk without a poor lifestyle present too",
        ],
        "correct_index": 2,
        "why": "Family history adds an extra, non-lifestyle risk factor, "
               "so the patient with it carries a higher overall risk even "
               "with identical lifestyles.",
    },
    {
        "id": "ks4-coronary-heart-disease-h16",
        "subtopic_slug": "coronary-heart-disease",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate this claim: 'A heart transplant is the only real "
                "treatment for coronary heart disease.'",
        "options": [
            "True — statins, stents and bypass surgery are not real treatments at all",
            "True, since every case of coronary heart disease eventually needs a transplant",
            "False, but only because a heart transplant is never used for this particular disease at all",
            "False — statins, stents and bypass surgery are all used before a transplant is ever considered",
        ],
        "correct_index": 3,
        "why": "Statins, stents and bypass surgery are the standard "
               "treatments; a transplant is only considered as a last "
               "resort.",
    },
    {
        "id": "ks4-coronary-heart-disease-h17",
        "subtopic_slug": "coronary-heart-disease",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A patient survives a heart attack and then removes every "
                "lifestyle risk factor they had. Predict the effect on "
                "their future risk.",
        "options": [
            "Future risk falls, though it remains higher than someone who never had a heart attack",
            "Future risk falls to exactly zero, matching someone who never smoked",
            "Future risk stays exactly the same as before the lifestyle changes",
            "Future risk actually rises, since removing risk factors puts strain on the heart",
        ],
        "correct_index": 0,
        "why": "Removing lifestyle risk factors lowers future risk, but "
               "existing damage from the heart attack means risk stays "
               "higher than for someone without that history.",
    },
    {
        "id": "ks4-coronary-heart-disease-h18",
        "subtopic_slug": "coronary-heart-disease",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a patient is often prescribed statins even "
                "after successfully having a stent fitted.",
        "options": [
            "The stent alone removes every future risk of any further narrowing anywhere in the coronary arteries",
            "The stent treats one narrowed section; statins address the ongoing cause elsewhere in the arteries",
            "Statins are given only to reverse the effect of the stent",
            "Statins are required to keep the stent physically in place",
        ],
        "correct_index": 1,
        "why": "The stent mechanically fixes one narrowing, while statins "
               "act on the underlying cholesterol that would otherwise "
               "keep narrowing arteries elsewhere.",
    },
    {
        "id": "ks4-coronary-heart-disease-h19",
        "subtopic_slug": "coronary-heart-disease",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate this claim: 'A family history of coronary heart "
                "disease guarantees a person will develop it too.'",
        "options": [
            "True — inherited risk factors always lead to the same disease appearing",
            "True, but only if the person also happens to be male",
            "False — family history raises the probability, but never makes the disease certain",
            "False, but only because a family history is not a real risk factor for this disease at all",
        ],
        "correct_index": 2,
        "why": "A risk factor changes the probability of disease; it never "
               "makes it certain, however strong the family history.",
    },
    {
        "id": "ks4-coronary-heart-disease-h20",
        "subtopic_slug": "coronary-heart-disease",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why public health campaigns about coronary heart "
                "disease usually focus on lifestyle factors rather than "
                "genetic ones.",
        "options": [
            "Lifestyle factors are the only risk factors doctors currently know about",
            "Genetic risk factors are actually far more common than lifestyle ones",
            "Genetic risk factors have already been eliminated entirely by modern medicine",
            "Lifestyle factors, unlike genetic ones, can actually be changed by the people affected",
        ],
        "correct_index": 3,
        "why": "Campaigns focus on lifestyle factors because, unlike "
               "genetic ones, people can actually act on them to reduce "
               "their own risk.",
    },
    {
        "id": "ks4-coronary-heart-disease-h21",
        "subtopic_slug": "coronary-heart-disease",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare the likely coronary artery condition of two "
                "patients with identical starting risk: one takes statins "
                "from an early age, one takes no treatment at all.",
        "options": [
            "The treated patient's arteries will generally narrow more slowly over time",
            "Both patients will have identical arteries, since statins have no real effect",
            "The untreated patient's arteries will actually narrow more slowly",
            "Neither patient's arteries will change at all over the years without symptoms",
        ],
        "correct_index": 0,
        "why": "By slowing cholesterol build-up, statins taken from an "
               "early age generally slow how quickly the treated patient's "
               "arteries narrow.",
    },
    {
        "id": "ks4-coronary-heart-disease-h22",
        "subtopic_slug": "coronary-heart-disease",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A coronary bypass graft becomes blocked itself, several "
                "years after the operation. Predict the effect on the "
                "heart muscle it was supplying.",
        "options": [
            "The heart muscle is completely unaffected, since the original artery has already healed",
            "The heart muscle it supplies is again at risk of being starved of oxygen",
            "The blockage automatically transfers to a healthy artery instead",
            "The heart compensates by growing an entirely new coronary artery",
        ],
        "correct_index": 1,
        "why": "If the graft itself becomes blocked, the heart muscle it "
               "supplies is again at risk of being starved of oxygen, just "
               "as before the operation.",
    },
    {
        "id": "ks4-coronary-heart-disease-h23",
        "subtopic_slug": "coronary-heart-disease",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why treating a patient's high blood pressure also "
                "lowers their risk of coronary heart disease.",
        "options": [
            "Blood pressure medication directly dissolves any existing plaques",
            "Lower blood pressure has no real connection at all to how quickly any plaques form",
            "Lower blood pressure reduces the damage to artery walls that allows plaques to form",
            "Blood pressure medication works only by lowering cholesterol instead",
        ],
        "correct_index": 2,
        "why": "Lower blood pressure means less damage to artery walls, "
               "which reduces the conditions that allow plaques to form "
               "there.",
    },
    {
        "id": "ks4-coronary-heart-disease-h24",
        "subtopic_slug": "coronary-heart-disease",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate this claim: 'Since coronary heart disease develops "
                "slowly, there is no benefit to reducing risk factors "
                "before any symptoms appear.'",
        "options": [
            "True — treating risk factors only ever helps once symptoms have already started",
            "True, since plaques cannot form at all before symptoms are noticed",
            "False, but only because the symptoms always appear at the very earliest stage of the disease",
            "False — reducing risk factors early can slow or prevent the plaque build-up that causes symptoms",
        ],
        "correct_index": 3,
        "why": "Acting on risk factors before symptoms appear can slow or "
               "prevent the plaque build-up that would otherwise go on to "
               "cause symptoms.",
    },
    {
        "id": "ks4-coronary-heart-disease-h25",
        "subtopic_slug": "coronary-heart-disease",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest how a hypothetical new drug that could fully "
                "reverse existing plaques would change coronary heart "
                "disease treatment, compared with statins.",
        "options": [
            "It would work in exactly the same way as a statin, since a statin already fully reverses every plaque that has formed",
            "It would remove the need to treat narrowed arteries surgically, unlike current statins, which only slow further build-up",
            "It would have no advantage over a statin at all",
            "It would need to be combined with a stent to have any effect",
        ],
        "correct_index": 1,
        "why": "Current statins only slow future build-up rather than "
               "reversing existing plaques, so a drug that could reverse "
               "them would remove the need for surgical treatment "
               "altogether.",
    },
    {
        "id": "ks4-coronary-heart-disease-h26",
        "subtopic_slug": "coronary-heart-disease",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A treatment involves passing a thin tube through a blood "
                "vessel to reach a narrowed coronary artery, then "
                "expanding a small mesh tube to hold it open. Identify "
                "this treatment and compare it with bypass surgery.",
        "options": [
            "This is bypass surgery; unlike a stent, it uses a whole vessel grafted from the patient's own leg instead",
            "This is a stent, fitted by angioplasty; unlike bypass surgery, it works from inside the original artery",
            "This is a heart transplant; unlike a stent, it replaces the whole heart",
            "This is a description of taking statins, which lower blood cholesterol",
        ],
        "correct_index": 1,
        "why": "This describes angioplasty fitting a stent, which works "
               "from inside the original artery, unlike bypass surgery, "
               "which builds an entirely new route around it.",
    },

    # ══════════════════════════════════════════════════════════════════
    # health-disease · e05-e12, s05-s26, h05-h26
    # ══════════════════════════════════════════════════════════════════
    {
        "id": "ks4-health-disease-e05",
        "subtopic_slug": "health-disease",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State one thing all pathogens have in common.",
        "options": [
            "They can all cause a communicable disease",
            "They are all forms of bacteria",
            "They can never be destroyed by the immune system",
            "They all live permanently inside the human body",
        ],
        "correct_index": 0,
        "why": "Whatever type of pathogen it is, causing a communicable "
               "disease is what defines it as a pathogen.",
    },
    {
        "id": "ks4-health-disease-e06",
        "subtopic_slug": "health-disease",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Classify type 2 diabetes as communicable or "
                "non-communicable.",
        "options": [
            "Communicable, spread by contact",
            "Non-communicable",
            "Communicable, spread by an insect",
            "Communicable, caused by a fungus",
        ],
        "correct_index": 1,
        "why": "Type 2 diabetes is not caused by a pathogen and cannot be "
               "passed on, so it is a non-communicable disease.",
    },
    {
        "id": "ks4-health-disease-e07",
        "subtopic_slug": "health-disease",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name a type of pathogen that is neither a bacterium nor a "
                "virus.",
        "options": [
            "An antibody",
            "A platelet",
            "A fungus",
            "A hormone",
        ],
        "correct_index": 2,
        "why": "Fungi and protists are pathogens too, alongside bacteria "
               "and viruses.",
    },
    {
        "id": "ks4-health-disease-e08",
        "subtopic_slug": "health-disease",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State how having diabetes affects a person's risk of "
                "cardiovascular disease.",
        "options": [
            "It lowers the risk",
            "It has no effect on the risk",
            "It removes the risk completely",
            "It raises the risk",
        ],
        "correct_index": 3,
        "why": "Diabetes is known to raise a person's risk of "
               "cardiovascular disease.",
    },
    {
        "id": "ks4-health-disease-e09",
        "subtopic_slug": "health-disease",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the organ most directly damaged by excessive "
                "long-term alcohol consumption.",
        "options": [
            "The liver",
            "The kidney",
            "The lungs",
            "The pancreas",
        ],
        "correct_index": 0,
        "why": "Excessive alcohol is strongly linked to liver disease and "
               "liver cancer.",
    },
    {
        "id": "ks4-health-disease-e10",
        "subtopic_slug": "health-disease",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the dietary factor linked to an increased risk of "
                "bowel cancer.",
        "options": [
            "A high intake of vitamin C",
            "A low intake of fibre",
            "A high intake of water",
            "A low intake of salt",
        ],
        "correct_index": 1,
        "why": "A low-fibre diet is linked to an increased risk of bowel "
               "cancer.",
    },
    {
        "id": "ks4-health-disease-e11",
        "subtopic_slug": "health-disease",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the BMI value generally used to define obesity.",
        "options": [
            "Above 18",
            "Above 25",
            "Above 30",
            "Above 40",
        ],
        "correct_index": 2,
        "why": "A BMI above 30 is generally used to define obesity.",
    },
    {
        "id": "ks4-health-disease-e12",
        "subtopic_slug": "health-disease",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Classify UV radiation as a type of risk factor.",
        "options": [
            "A lifestyle risk factor",
            "A genetic risk factor",
            "A risk factor for communicable disease only",
            "An environmental risk factor",
        ],
        "correct_index": 3,
        "why": "UV radiation is an environmental risk factor, alongside "
               "things like air pollution and asbestos.",
    },
    {
        "id": "ks4-health-disease-s05",
        "subtopic_slug": "health-disease",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Classify athlete's foot, an infection caused by a fungus.",
        "options": [
            "Communicable, since it is caused by a pathogen",
            "Non-communicable, since it only affects the feet",
            "Non-communicable, since fungi are not classed as pathogens",
            "Communicable, but only because it is painful",
        ],
        "correct_index": 0,
        "why": "Athlete's foot is caused by a fungal pathogen, so it is a "
               "communicable disease.",
    },
    {
        "id": "ks4-health-disease-s06",
        "subtopic_slug": "health-disease",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Classify arthritis, a condition that causes joint pain and "
                "stiffness.",
        "options": [
            "Communicable, spread through joint contact",
            "Non-communicable, since it is not caused by a pathogen",
            "Communicable, caused by a bacterium",
            "Non-communicable, but only in people under thirty",
        ],
        "correct_index": 1,
        "why": "Arthritis is not caused by a pathogen and cannot be passed "
               "on, so it is non-communicable.",
    },
    {
        "id": "ks4-health-disease-s07",
        "subtopic_slug": "health-disease",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A person has recovered fully from a physical injury but is "
                "still in poor mental wellbeing. Apply the WHO definition of "
                "health to this case.",
        "options": [
            "Yes, since the physical injury itself has completely healed",
            "Yes, since mental wellbeing is not part of the WHO definition",
            "No, since health includes mental wellbeing, not just physical recovery",
            "No, but only because a physical injury always leads to long-term illness",
        ],
        "correct_index": 2,
        "why": "The WHO definition covers mental as well as physical "
               "wellbeing, so poor mental wellbeing means this person is not "
               "healthy by that definition even once the injury has healed.",
    },
    {
        "id": "ks4-health-disease-s08",
        "subtopic_slug": "health-disease",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a person can develop lung cancer without ever "
                "having been exposed to any known risk factor.",
        "options": [
            "This is impossible, since a known risk factor must always be present for any cancer",
            "Risk factors always guarantee that the disease will develop",
            "Every case of lung cancer has an identical, known cause",
            "A risk factor raises probability; disease can still occur without it being present",
        ],
        "correct_index": 3,
        "why": "A risk factor only changes the probability of disease, so "
               "disease can still occur in someone without that risk "
               "factor.",
    },
    {
        "id": "ks4-health-disease-s09",
        "subtopic_slug": "health-disease",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why alcohol is linked to a higher rate of "
                "accidents, as well as to disease.",
        "options": [
            "It impairs judgement and coordination, increasing the chance of accidents happening",
            "It only affects the liver, so it cannot influence accident rates at all",
            "It strengthens muscle coordination so much that people take risks they otherwise would not",
            "It has no effect on the brain or behaviour of any kind",
        ],
        "correct_index": 0,
        "why": "Alcohol impairs judgement and coordination, which raises "
               "the chance of accidents as well as long-term disease risk.",
    },
    {
        "id": "ks4-health-disease-s10",
        "subtopic_slug": "health-disease",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain how a diet high in sugar increases the risk of "
                "type 2 diabetes.",
        "options": [
            "Sugar directly destroys the pancreas within a few days",
            "Excess sugar contributes to obesity, which raises the risk of type 2 diabetes",
            "Sugar lowers blood pressure, and low blood pressure is what causes type 2 diabetes",
            "Sugar has no link at all to type 2 diabetes or obesity",
        ],
        "correct_index": 1,
        "why": "A high-sugar diet contributes to obesity, and obesity is a "
               "strong risk factor for type 2 diabetes.",
    },
    {
        "id": "ks4-health-disease-s11",
        "subtopic_slug": "health-disease",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare how a communicable disease and a non-communicable "
                "disease are each best prevented.",
        "options": [
            "Both are prevented in exactly the same way, through vaccination alone",
            "Neither type of disease can be meaningfully prevented at all",
            "A communicable disease is limited by reducing contact with pathogens; a non-communicable one by lifestyle change",
            "A non-communicable disease is prevented by avoiding all contact with the pathogen that spreads it",
        ],
        "correct_index": 2,
        "why": "Communicable disease spreads through contact with a "
               "pathogen, so limiting that contact helps prevent it; "
               "non-communicable disease is instead reduced through "
               "lifestyle change.",
    },
    {
        "id": "ks4-health-disease-s12",
        "subtopic_slug": "health-disease",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A patient smokes, works outdoors in strong sunlight, and "
                "has a family history of skin cancer. Explain how these "
                "three risk factors relate to one another.",
        "options": [
            "Only the strongest of the three risk factors actually counts towards overall risk",
            "The three risk factors cancel each other out, leaving no overall change in risk",
            "Genetic risk factors override both lifestyle and environmental ones completely",
            "They come from three different categories, but all add together to raise overall risk",
        ],
        "correct_index": 3,
        "why": "Lifestyle, environmental and genetic risk factors are "
               "different categories, but they add together rather than "
               "cancelling out or overriding one another.",
    },
    {
        "id": "ks4-health-disease-s13",
        "subtopic_slug": "health-disease",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain what would be needed to show that smoking causes "
                "lung cancer, rather than the two merely being correlated.",
        "options": [
            "Evidence of a biological mechanism linking smoking to the DNA damage that causes cancer",
            "A single study showing that smokers and non-smokers have different lung cancer rates",
            "A survey asking smokers whether they personally believe smoking is dangerous",
            "Proof that every single smoker eventually develops lung cancer",
        ],
        "correct_index": 0,
        "why": "Showing causation needs more than one correlation study — a "
               "known biological mechanism is strong evidence that the "
               "link is causal.",
    },
    {
        "id": "ks4-health-disease-s14",
        "subtopic_slug": "health-disease",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A patient asks whether smoking IS lung cancer. Explain the "
                "distinction.",
        "options": [
            "They are the same thing, described using two different words",
            "Smoking is a risk factor that raises the probability of lung cancer developing; it is not the disease itself",
            "Smoking is a disease in its own right, and is entirely unrelated to whether a person later develops lung cancer",
            "Lung cancer is a risk factor that can lead to smoking",
        ],
        "correct_index": 1,
        "why": "Smoking is a risk factor — something that raises the "
               "probability of disease — and is not the disease itself.",
    },
    {
        "id": "ks4-health-disease-s15",
        "subtopic_slug": "health-disease",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a doctor treating a patient for obesity is also "
                "likely to check their blood pressure and cholesterol.",
        "options": [
            "Obesity has no real connection to blood pressure or cholesterol levels",
            "Checking blood pressure always cures obesity directly",
            "Obesity is linked to raised blood pressure and cholesterol, both of which carry their own risks",
            "Blood pressure and cholesterol only matter in a patient who is not obese to begin with",
        ],
        "correct_index": 2,
        "why": "Obesity is linked to raised blood pressure and cholesterol, "
               "so a doctor checks both when assessing a patient's overall "
               "risk.",
    },
    {
        "id": "ks4-health-disease-s16",
        "subtopic_slug": "health-disease",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a patient with poorly controlled diabetes is "
                "more likely to develop infections in a wound.",
        "options": [
            "Diabetes has no effect on the body's ability to fight infection",
            "Diabetes makes every wound completely painless, so any infection in it goes unnoticed",
            "Diabetes instantly cures any infection that starts in a wound",
            "Diabetes can impair the body's normal defences, making infection more likely",
        ],
        "correct_index": 3,
        "why": "Poorly controlled diabetes can impair the body's normal "
               "defences, making wound infections more likely.",
    },
    {
        "id": "ks4-health-disease-s17",
        "subtopic_slug": "health-disease",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain how malaria, caused by a protist, is spread between "
                "people.",
        "options": [
            "Indirectly, via a mosquito that carries the protist between hosts",
            "Directly, through the air when an infected person coughs",
            "Directly, through shared food and water only",
            "It is not communicable, since a protist is not a true pathogen",
        ],
        "correct_index": 0,
        "why": "Malaria spreads indirectly, carried between people by a "
               "mosquito that transmits the protist.",
    },
    {
        "id": "ks4-health-disease-s18",
        "subtopic_slug": "health-disease",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A study finds that towns with more gyms have lower rates "
                "of heart disease. Suggest another explanation besides "
                "gyms directly preventing heart disease.",
        "options": [
            "There is no other possible explanation available at all",
            "Towns with more gyms may simply have wealthier, more health-conscious residents overall",
            "Low rates of heart disease are what cause more gyms to open in a town in the first place",
            "Gyms directly inject medication into the local water supply",
        ],
        "correct_index": 1,
        "why": "A third factor, such as wealth or general health-"
               "consciousness, could explain both more gyms and lower "
               "heart disease rates, without gyms causing the effect "
               "directly.",
    },
    {
        "id": "ks4-health-disease-s19",
        "subtopic_slug": "health-disease",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why heavy alcohol use is linked to a higher rate of "
                "mental health problems.",
        "options": [
            "Alcohol has no known effect on the brain or on behaviour",
            "Mental health problems are what cause a person to start drinking, never the reverse",
            "Alcohol can affect brain chemistry and disrupt sleep, both of which affect mental health",
            "Alcohol only affects physical organs, never anything related to the brain",
        ],
        "correct_index": 2,
        "why": "Alcohol affects brain chemistry and sleep, both of which "
               "can, in turn, affect mental health.",
    },
    {
        "id": "ks4-health-disease-s20",
        "subtopic_slug": "health-disease",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Classify exposure to asbestos in the workplace as a type "
                "of risk factor.",
        "options": [
            "A lifestyle risk factor, since it is a personal choice",
            "A genetic risk factor, since it is inherited",
            "Not a risk factor at all, since asbestos is not linked to any disease",
            "An environmental risk factor",
        ],
        "correct_index": 3,
        "why": "Asbestos exposure is an environmental risk factor, linked "
               "to lung disease including mesothelioma.",
    },
    {
        "id": "ks4-health-disease-s21",
        "subtopic_slug": "health-disease",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Two office workers have identical lifestyles. One later "
                "works for years around asbestos. Compare their risk of "
                "lung disease.",
        "options": [
            "The asbestos-exposed worker has a higher risk, from that added environmental factor",
            "Both workers have exactly the same risk, since the two of them have identical lifestyles",
            "The other worker has the higher risk, since asbestos actually lowers risk",
            "Neither worker has any risk at all without a family history present too",
        ],
        "correct_index": 0,
        "why": "Asbestos exposure adds an environmental risk factor on top "
               "of identical lifestyles, giving the exposed worker a "
               "higher overall risk.",
    },
    {
        "id": "ks4-health-disease-s22",
        "subtopic_slug": "health-disease",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why stopping heavy drinking lowers a person's risk "
                "of further liver damage, even after years of alcohol use.",
        "options": [
            "It reverses all existing liver damage within a few days",
            "It removes the ongoing cause of damage, even though past damage may remain",
            "It has no effect once damage has already started",
            "It only helps a person who has never drunk any alcohol at all before then",
        ],
        "correct_index": 1,
        "why": "Stopping drinking removes the ongoing cause of further "
               "damage, even though damage already done may remain.",
    },
    {
        "id": "ks4-health-disease-s23",
        "subtopic_slug": "health-disease",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare how a typical communicable disease and a typical "
                "non-communicable disease tend to progress over time.",
        "options": [
            "Both types of disease always last for the rest of a person's life once they have been caught, whatever treatment is given",
            "Neither type of disease changes in severity over time",
            "A communicable disease often clears once the pathogen is cleared; a non-communicable one often persists or develops gradually",
            "A non-communicable disease always clears within a few days",
        ],
        "correct_index": 2,
        "why": "A communicable disease often clears with the pathogen; a "
               "non-communicable one more often develops gradually and "
               "persists.",
    },
    {
        "id": "ks4-health-disease-s24",
        "subtopic_slug": "health-disease",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "An employee has no physical illness but feels completely "
                "isolated and undervalued at work. Explain whether they "
                "meet the WHO definition of health.",
        "options": [
            "Yes, since they have no diagnosed physical illness at all",
            "Yes, since social wellbeing is not part of the WHO definition",
            "No, but only because isolation always causes physical illness eventually",
            "No, since health requires social as well as physical and mental wellbeing",
        ],
        "correct_index": 3,
        "why": "The WHO definition requires social as well as physical and "
               "mental wellbeing, so isolation at work makes this "
               "employee unhealthy by that definition.",
    },
    {
        "id": "ks4-health-disease-s25",
        "subtopic_slug": "health-disease",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A doctor treats smoking and stress as risk factors for "
                "heart disease very differently in her advice. Suggest "
                "why.",
        "options": [
            "The strength of evidence linking each factor to heart disease differs considerably",
            "Stress is actually a communicable condition, unlike smoking",
            "Smoking has never actually been linked to heart disease",
            "All risk factors must always be treated as being of exactly equal importance in advice",
        ],
        "correct_index": 0,
        "why": "Different risk factors are supported by different "
               "strengths of evidence, which affects how strongly a "
               "doctor advises against them.",
    },
    {
        "id": "ks4-health-disease-s26",
        "subtopic_slug": "health-disease",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a doctor asks about family history when "
                "assessing a patient's risk of heart disease, but not "
                "usually when diagnosing a cold.",
        "options": [
            "A cold is far more dangerous than heart disease, so a family history is of no use in diagnosing it",
            "Genetics contributes to non-communicable disease risk; a cold is caused directly by a pathogen instead",
            "Family history is only ever relevant to communicable diseases",
            "Doctors never actually ask about family history for any condition",
        ],
        "correct_index": 1,
        "why": "Genetics contributes to non-communicable disease risk, "
               "while a cold is caused directly by a pathogen, making "
               "family history far less relevant to it.",
    },
    {
        "id": "ks4-health-disease-h05",
        "subtopic_slug": "health-disease",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest what kind of evidence convinced scientists that "
                "smoking causes lung cancer, rather than the two merely "
                "being linked by chance.",
        "options": [
            "Many large studies, a dose-response relationship, and a known biological mechanism, together",
            "A single anonymous survey of ten smokers",
            "The observation that some non-smokers have also gone on to develop lung cancer themselves",
            "An opinion poll asking doctors which they personally believed",
        ],
        "correct_index": 0,
        "why": "Causation is established through a convergence of "
               "evidence — many studies, a dose-response pattern and a "
               "known mechanism — not any single piece of evidence alone.",
    },
    {
        "id": "ks4-health-disease-h06",
        "subtopic_slug": "health-disease",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A study finds that children with bigger feet tend to read "
                "better. Evaluate what this shows.",
        "options": [
            "Bigger feet directly cause better reading ability",
            "Both are linked to age — older children have both bigger feet and better reading skills",
            "Better reading ability directly causes feet to grow larger",
            "This proves that foot size has no relationship at all with any other variable measured",
        ],
        "correct_index": 1,
        "why": "A third factor, age, explains both variables at once, "
               "which is why the correlation does not mean one causes the "
               "other.",
    },
    {
        "id": "ks4-health-disease-h07",
        "subtopic_slug": "health-disease",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate this claim: 'Since non-communicable diseases are "
                "not caused by pathogens, nothing can be done to prevent "
                "them.'",
        "options": [
            "True — nothing at all can reduce the risk of a non-communicable disease",
            "True, since only a communicable disease can ever respond to any kind of prevention measure at all",
            "False — lifestyle and environmental risk factors for non-communicable disease can often be reduced",
            "False, but only because non-communicable diseases do not actually exist",
        ],
        "correct_index": 2,
        "why": "Non-communicable disease risk can often be reduced by "
               "changing lifestyle and environmental risk factors, even "
               "without a pathogen involved.",
    },
    {
        "id": "ks4-health-disease-h08",
        "subtopic_slug": "health-disease",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A country's population is ageing rapidly. Predict the "
                "likely effect on rates of non-communicable disease.",
        "options": [
            "Non-communicable disease rates would be expected to fall sharply",
            "There would be no change at all, since a person's age is unrelated to any non-communicable disease",
            "Only communicable disease rates would be affected by an ageing population",
            "Non-communicable disease rates would be expected to rise, since age is a risk factor for many of them",
        ],
        "correct_index": 3,
        "why": "Age is a risk factor for many non-communicable diseases, so "
               "an ageing population would be expected to see rates rise.",
    },
    {
        "id": "ks4-health-disease-h09",
        "subtopic_slug": "health-disease",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate this claim: 'All risk factors for disease have "
                "exactly the same strength of scientific evidence behind "
                "them.'",
        "options": [
            "False — some risk factors, like smoking, have strong causal evidence; others show only correlation so far",
            "True — every risk factor identified has identical, fully proven causation",
            "True, since correlation and causation always mean exactly the same thing in any scientific work at all",
            "False, but only because risk factors are never actually studied scientifically",
        ],
        "correct_index": 0,
        "why": "Risk factors vary hugely in how strongly they are "
               "evidenced — some, like smoking, have strong causal "
               "evidence, while others are supported only by correlation "
               "so far.",
    },
    {
        "id": "ks4-health-disease-h10",
        "subtopic_slug": "health-disease",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest what would happen to a population's rate of "
                "non-communicable disease if every lifestyle risk factor "
                "were removed, but genetic and environmental factors "
                "remained.",
        "options": [
            "Non-communicable disease would disappear completely from the population",
            "Rates would fall, but would not reach zero, since other risk factor categories would remain",
            "Rates would rise, since lifestyle factors actually protect against disease",
            "Rates would stay exactly the same, since lifestyle factors have no real effect on them",
        ],
        "correct_index": 1,
        "why": "Removing one category of risk factor would lower rates, "
               "but genetic and environmental risk factors would still "
               "contribute, so disease would not disappear entirely.",
    },
    {
        "id": "ks4-health-disease-h11",
        "subtopic_slug": "health-disease",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain the chain of risk that links obesity to an "
                "increased risk of cardiovascular disease.",
        "options": [
            "Obesity directly damages the heart valves within weeks",
            "Obesity has no connection to cardiovascular disease whatsoever",
            "Obesity raises the risk of diabetes, and diabetes itself raises cardiovascular risk further",
            "Cardiovascular disease is what always causes obesity, and never the other way round at all",
        ],
        "correct_index": 2,
        "why": "Obesity raises the risk of diabetes, and diabetes in turn "
               "raises cardiovascular risk, forming a chain of increased "
               "risk.",
    },
    {
        "id": "ks4-health-disease-h12",
        "subtopic_slug": "health-disease",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate this claim: 'Following a completely healthy "
                "lifestyle guarantees a person will never develop a "
                "non-communicable disease.'",
        "options": [
            "True — lifestyle is the only risk factor that matters for any disease",
            "True, since genetic and environmental risk factors do not really exist",
            "False, but only because a completely healthy lifestyle raises a person's disease risk instead",
            "False — genetic and environmental risk factors can still contribute, even with a perfect lifestyle",
        ],
        "correct_index": 3,
        "why": "Genetic and environmental risk factors act independently "
               "of lifestyle, so even a perfect lifestyle cannot guarantee "
               "protection from every non-communicable disease.",
    },
    {
        "id": "ks4-health-disease-h13",
        "subtopic_slug": "health-disease",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why controlling an outbreak of a communicable "
                "disease usually requires different public health action "
                "than reducing rates of a non-communicable disease.",
        "options": [
            "A communicable disease needs contact and hygiene measures; a non-communicable one needs lifestyle and environmental change",
            "Both are controlled using exactly the same vaccination programme",
            "Neither type of disease responds to any public health action at all, so exactly the same approach is taken to both of them",
            "Non-communicable disease is controlled entirely through quarantine",
        ],
        "correct_index": 0,
        "why": "Because the two disease types have different causes, "
               "controlling them calls for different action — contact and "
               "hygiene measures for one, lifestyle and environmental "
               "change for the other.",
    },
    {
        "id": "ks4-health-disease-h14",
        "subtopic_slug": "health-disease",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A country bans smoking in all public places. Predict the "
                "likely long-term effect on national rates of lung cancer "
                "and coronary heart disease.",
        "options": [
            "No effect, since public smoking bans do not reduce overall smoking exposure",
            "A gradual fall, as overall exposure to smoke and smoking itself likely decreases over time",
            "An immediate and complete disappearance of both diseases within a year",
            "A rise in both diseases, since smokers who are banned switch to still more harmful habits",
        ],
        "correct_index": 1,
        "why": "Reduced exposure to smoking over time would be expected to "
               "gradually lower rates of diseases linked to it, though not "
               "instantly.",
    },
    {
        "id": "ks4-health-disease-h15",
        "subtopic_slug": "health-disease",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate this claim: 'If a person's heart disease risk is "
                "partly genetic, lifestyle changes are pointless for "
                "them.'",
        "options": [
            "True — a genetic risk factor cancels out any benefit lifestyle change could offer",
            "True, since genetic risk factors always outweigh lifestyle ones completely",
            "False — lifestyle change can still reduce the modifiable part of their overall risk",
            "False, but only because genetics is not really a risk factor for heart disease",
        ],
        "correct_index": 2,
        "why": "Risk factors add together rather than cancelling out, so "
               "lifestyle change can still reduce the modifiable part of "
               "overall risk even alongside a genetic factor.",
    },
    {
        "id": "ks4-health-disease-h16",
        "subtopic_slug": "health-disease",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A survey finds that people who smoke, drink heavily and "
                "rarely exercise have far higher rates of several "
                "diseases. Evaluate whether this alone proves each factor "
                "causes disease.",
        "options": [
            "Yes, a single survey showing a strong link is always sufficient proof of causation",
            "Yes, but only because surveys are always more reliable than laboratory experiments",
            "No, because a survey of this size can never detect a link between any two things",
            "No — correlation alone cannot prove causation without further supporting evidence",
        ],
        "correct_index": 3,
        "why": "A correlation from one survey, on its own, cannot prove "
               "causation — further supporting evidence is needed before "
               "that conclusion can be drawn.",
    },
    {
        "id": "ks4-health-disease-h17",
        "subtopic_slug": "health-disease",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare what 'curing' typically means for a communicable "
                "disease with what it typically means for a chronic "
                "non-communicable disease.",
        "options": [
            "A communicable disease can often be cleared entirely once the pathogen is removed; many non-communicable diseases are instead managed long-term",
            "Both types of disease are always cured permanently using antibiotics",
            "Neither type of disease can ever be treated in any way",
            "A non-communicable disease is always cured far faster than a communicable one",
        ],
        "correct_index": 0,
        "why": "A communicable disease can often be fully cleared once the "
               "pathogen is gone, while many chronic non-communicable "
               "diseases are instead managed rather than cured outright.",
    },
    {
        "id": "ks4-health-disease-h18",
        "subtopic_slug": "health-disease",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate this claim: 'Environmental risk factors, such as "
                "air pollution, only matter for people who work outdoors.'",
        "options": [
            "True — an indoor environment carries no environmental risk factor of any kind at all",
            "False — air pollution and other environmental exposures can affect anyone living in an affected area",
            "True, since air pollution cannot travel into any building",
            "False, but only because environmental risk factors do not actually exist",
        ],
        "correct_index": 1,
        "why": "Air pollution and similar environmental exposures affect "
               "anyone living in an affected area, not only those who "
               "work outdoors.",
    },
    {
        "id": "ks4-health-disease-h19",
        "subtopic_slug": "health-disease",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare how influenza and malaria are each spread between "
                "people.",
        "options": [
            "Both spread in exactly the same way, through insect bites",
            "Influenza spreads through the bites of insects; malaria spreads through droplets carried in the air",
            "Influenza spreads through airborne droplets; malaria spreads via a mosquito carrying the protist",
            "Neither disease is actually communicable",
        ],
        "correct_index": 2,
        "why": "Influenza spreads directly through airborne droplets, "
               "while malaria spreads indirectly via a mosquito carrying "
               "the protist.",
    },
    {
        "id": "ks4-health-disease-h20",
        "subtopic_slug": "health-disease",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why a national fall in smoking rates tends to "
                "reduce rates of several different diseases at once, not "
                "just one.",
        "options": [
            "Smoking is linked to only one single disease, so a fall of this kind would not actually happen at all",
            "Smoking cures every other risk factor a person has, once they stop",
            "Diseases only ever fall in rate for reasons unrelated to smoking",
            "Smoking is a shared risk factor for several diseases, including lung cancer, CHD and other cancers",
        ],
        "correct_index": 3,
        "why": "Because smoking is a shared risk factor across several "
               "diseases, reducing it lowers the rate of each of them at "
               "once.",
    },
    {
        "id": "ks4-health-disease-h21",
        "subtopic_slug": "health-disease",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate this claim: 'Doctors should ignore a risk factor "
                "identified only through correlation until causation is "
                "fully proven.'",
        "options": [
            "Not necessarily — acting on a strong correlation can still reduce risk while further evidence is gathered",
            "True — no health advice should ever be based on correlation alone",
            "True, since correlation studies are always completely unreliable",
            "Not necessarily, but only because a strong correlation always amounts to causation in the end anyway",
        ],
        "correct_index": 0,
        "why": "Acting on a strong correlation can reduce risk in the "
               "meantime, even while further evidence towards proving "
               "causation is still being gathered.",
    },
    {
        "id": "ks4-health-disease-h22",
        "subtopic_slug": "health-disease",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest whether a genetic risk factor could ever make a "
                "person more likely to catch a communicable disease.",
        "options": [
            "No — genetic risk factors only ever apply to non-communicable disease",
            "Yes — genetics can affect how well a person's immune system responds to a pathogen",
            "No, since communicable disease depends only on pathogen exposure",
            "Yes, but only because communicable diseases are not caused by pathogens",
        ],
        "correct_index": 1,
        "why": "Genetics can affect how well a person's immune system "
               "responds to a pathogen, so it can act as a risk factor for "
               "communicable disease too.",
    },
    {
        "id": "ks4-health-disease-h23",
        "subtopic_slug": "health-disease",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate this claim: 'Since obesity raises the risk of so "
                "many diseases, obesity itself should just be classed as "
                "one of those diseases.'",
        "options": [
            "True — a risk factor and a disease are always exactly the same thing",
            "True, but only because obesity has no separate definition of its own",
            "Debatable — obesity is generally treated as a risk factor, distinct from the diseases it raises the risk of",
            "False, but only because obesity is not linked to any single one of those diseases in the first place at all",
        ],
        "correct_index": 2,
        "why": "Obesity is generally treated as a risk factor in its own "
               "right, kept distinct from the diseases whose probability "
               "it raises.",
    },
    {
        "id": "ks4-health-disease-h24",
        "subtopic_slug": "health-disease",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "An area introduces strict air pollution controls. Predict "
                "the effect on the lung disease risk of a resident who "
                "also smokes heavily.",
        "options": [
            "Their risk falls to zero, since air pollution was their only risk factor",
            "Their risk becomes identical to that of a non-smoker in a polluted area",
            "Their risk rises, since cleaner air increases the harm that smoking does to the lungs",
            "Their risk falls somewhat, but smoking remains a separate, significant risk factor",
        ],
        "correct_index": 3,
        "why": "Removing one risk factor lowers overall risk somewhat, but "
               "the remaining risk factor, smoking, still contributes "
               "significantly on its own.",
    },
    {
        "id": "ks4-health-disease-h25",
        "subtopic_slug": "health-disease",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why wealthier countries tend to see a shift "
                "towards more non-communicable disease and less "
                "communicable disease, rather than simply more disease "
                "overall.",
        "options": [
            "Improved sanitation and medicine reduce communicable disease, while lifestyle factors raise non-communicable disease",
            "Wealthier countries have stopped experiencing any disease of either type",
            "Communicable disease becomes far more common as a country's sanitation and its own medicine both improve over time",
            "Non-communicable disease is entirely unrelated to any change in lifestyle",
        ],
        "correct_index": 0,
        "why": "Better sanitation and medicine cut communicable disease, "
               "while lifestyle factors common in wealthier countries "
               "raise non-communicable disease, producing a shift rather "
               "than simply more disease.",
    },
    {
        "id": "ks4-health-disease-h26",
        "subtopic_slug": "health-disease",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why improving hygiene has a bigger effect on rates "
                "of communicable disease than on rates of non-communicable "
                "disease.",
        "options": [
            "Hygiene has an identical effect on both types of disease",
            "Hygiene reduces exposure to pathogens, which communicable but not non-communicable disease depends on",
            "Hygiene raises the rate of non-communicable disease rather than lowering it in any way at all",
            "Non-communicable disease is entirely caused by poor hygiene",
        ],
        "correct_index": 1,
        "why": "Hygiene works by reducing exposure to pathogens, which "
               "matters for communicable disease but has little bearing "
               "on non-communicable disease.",
    },

    # ══════════════════════════════════════════════════════════════════
    # cancer · e05-e12, s05-s26, h05-h26
    # ══════════════════════════════════════════════════════════════════
    {
        "id": "ks4-cancer-e05",
        "subtopic_slug": "cancer",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name a type of gene in which an inherited mutation is "
                "linked to a higher risk of breast and ovarian cancer.",
        "options": [
            "A BRCA gene",
            "A haemoglobin gene",
            "An insulin gene",
            "A collagen gene",
        ],
        "correct_index": 0,
        "why": "Inherited mutations in a BRCA gene are linked to a higher "
               "risk of breast and ovarian cancer.",
    },
    {
        "id": "ks4-cancer-e06",
        "subtopic_slug": "cancer",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the type of pathogen linked to most cases of liver "
                "cancer.",
        "options": [
            "A protist",
            "A virus",
            "A fungus",
            "A bacterium",
        ],
        "correct_index": 1,
        "why": "Hepatitis B and C, both viruses, are linked to most cases "
               "of liver cancer.",
    },
    {
        "id": "ks4-cancer-e07",
        "subtopic_slug": "cancer",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Classify ionising radiation, such as X-rays, as a risk "
                "factor for cancer.",
        "options": [
            "A lifestyle risk factor",
            "A genetic risk factor",
            "An environmental risk factor",
            "Not a risk factor at all",
        ],
        "correct_index": 2,
        "why": "Ionising radiation is an environmental risk factor for "
               "cancer, alongside things like UV radiation and asbestos.",
    },
    {
        "id": "ks4-cancer-e08",
        "subtopic_slug": "cancer",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the type of cancer linked to long-term exposure to "
                "asbestos fibres.",
        "options": [
            "Skin cancer",
            "Bowel cancer",
            "Cervical cancer (a viral cancer)",
            "Mesothelioma (a lung cancer)",
        ],
        "correct_index": 3,
        "why": "Long-term exposure to asbestos fibres is linked to "
               "mesothelioma, a cancer affecting the lining of the lungs.",
    },
    {
        "id": "ks4-cancer-e09",
        "subtopic_slug": "cancer",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what typically encloses a benign tumour.",
        "options": [
            "A capsule",
            "A layer of bone",
            "A ring of muscle",
            "Nothing; it has no boundary at all",
        ],
        "correct_index": 0,
        "why": "A benign tumour typically stays enclosed within a capsule "
               "rather than invading surrounding tissue.",
    },
    {
        "id": "ks4-cancer-e10",
        "subtopic_slug": "cancer",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name, in addition to the blood, the other body system "
                "malignant cells can travel through to spread.",
        "options": [
            "The digestive system",
            "The lymph system",
            "The nervous system",
            "The skeletal system",
        ],
        "correct_index": 1,
        "why": "Malignant cells can travel through the blood or the lymph "
               "system to form secondary tumours elsewhere.",
    },
    {
        "id": "ks4-cancer-e11",
        "subtopic_slug": "cancer",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State a side effect radiotherapy can cause in the area "
                "being treated.",
        "options": [
            "Permanent loss of taste",
            "Immediate hair regrowth",
            "Hair loss in that area",
            "Improved night vision",
        ],
        "correct_index": 2,
        "why": "Radiotherapy can damage healthy cells near the tumour, "
               "which can cause hair loss in the treated area.",
    },
    {
        "id": "ks4-cancer-e12",
        "subtopic_slug": "cancer",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State whether every tumour is automatically cancer.",
        "options": [
            "Yes, all tumours are cancer",
            "Yes, but only tumours found in the lungs",
            "No, a tumour only becomes cancer once it is surgically removed",
            "No, only a malignant tumour is cancer",
        ],
        "correct_index": 3,
        "why": "A tumour is any abnormal mass of cells; only a malignant "
               "tumour is classed as cancer.",
    },
    {
        "id": "ks4-cancer-s05",
        "subtopic_slug": "cancer",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a family history of a particular cancer is "
                "considered a risk factor for that cancer.",
        "options": [
            "Inherited gene mutations can be passed down, raising risk in later generations",
            "Family history has no genetic basis and is purely coincidental",
            "Cancer is always caught directly by close contact with an affected family member",
            "A family history guarantees that cancer will definitely develop",
        ],
        "correct_index": 0,
        "why": "Gene mutations that raise cancer risk can be inherited, "
               "which is why family history is a genetic risk factor.",
    },
    {
        "id": "ks4-cancer-s06",
        "subtopic_slug": "cancer",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain how long-term hepatitis B or C infection can lead "
                "to liver cancer.",
        "options": [
            "The virus itself is a cancer cell that grows inside the liver",
            "Long-term infection can damage liver cells over years, raising the risk of cancer developing",
            "Hepatitis stops every cell in the liver from ever dividing again, so no tumour can form there",
            "Hepatitis only affects the lungs, never the liver",
        ],
        "correct_index": 1,
        "why": "Long-term hepatitis infection damages liver cells over "
               "years, which raises the risk of liver cancer developing.",
    },
    {
        "id": "ks4-cancer-s07",
        "subtopic_slug": "cancer",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain how asbestos fibres breathed in years earlier can "
                "lead to cancer developing later.",
        "options": [
            "The fibres dissolve completely and have no lasting effect on the lungs",
            "The fibres are coughed out within a day, leaving no trace behind",
            "The fibres lodge in lung tissue and damage cells there over a long period",
            "The fibres are absorbed directly into the bloodstream and destroyed instantly",
        ],
        "correct_index": 2,
        "why": "Asbestos fibres lodge in lung tissue and damage cells "
               "there over a long period, which is why mesothelioma can "
               "appear decades after exposure.",
    },
    {
        "id": "ks4-cancer-s08",
        "subtopic_slug": "cancer",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare how far radiotherapy and chemotherapy each reach "
                "in the body.",
        "options": [
            "Both reach every cancer cell in the body equally well",
            "Radiotherapy reaches the whole body; chemotherapy only reaches the treated area",
            "Neither treatment can reach cancer cells anywhere in the body",
            "Radiotherapy targets a specific area; chemotherapy travels throughout the whole body",
        ],
        "correct_index": 3,
        "why": "Radiotherapy is aimed at one specific area, while "
               "chemotherapy travels in the blood, reaching cells "
               "throughout the whole body.",
    },
    {
        "id": "ks4-cancer-s09",
        "subtopic_slug": "cancer",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A person has a family history of a cancer, works with "
                "asbestos, and smokes. Classify these three risk factors.",
        "options": [
            "Genetic, environmental and lifestyle, respectively",
            "All three are lifestyle risk factors",
            "All three are genetic risk factors",
            "None of these three is actually a risk factor for cancer",
        ],
        "correct_index": 0,
        "why": "Family history is genetic, asbestos exposure at work is "
               "environmental, and smoking is a lifestyle choice.",
    },
    {
        "id": "ks4-cancer-s10",
        "subtopic_slug": "cancer",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why chemotherapy commonly causes nausea as a side "
                "effect.",
        "options": [
            "It has no effect on any cells outside the tumour itself",
            "It also affects the rapidly dividing cells lining the gut",
            "It lowers body temperature, which directly causes nausea",
            "It only affects the cells of the immune system",
        ],
        "correct_index": 1,
        "why": "Chemotherapy targets rapidly dividing cells wherever they "
               "are, including the cells lining the gut, which can cause "
               "nausea.",
    },
    {
        "id": "ks4-cancer-s11",
        "subtopic_slug": "cancer",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain what surgery and radiotherapy have in common as "
                "cancer treatments.",
        "options": [
            "Both travel through the bloodstream to reach cancer cells wherever they are in the body",
            "Neither treatment has any effect on a tumour of any kind",
            "Both mainly treat a tumour in one specific location, rather than the whole body",
            "Both always cause complete loss of hair across the whole body",
        ],
        "correct_index": 2,
        "why": "Both surgery and radiotherapy mainly treat a tumour where "
               "it is, rather than reaching cancer cells throughout the "
               "whole body.",
    },
    {
        "id": "ks4-cancer-s12",
        "subtopic_slug": "cancer",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why cells from a benign tumour do not form "
                "secondary tumours elsewhere in the body.",
        "options": [
            "Benign cells actively travel to other organs but always die on arrival",
            "Benign tumours contain no cells capable of dividing at all",
            "Benign tumours always shrink before they can spread anywhere",
            "Benign cells stay enclosed and do not break away to travel elsewhere",
        ],
        "correct_index": 3,
        "why": "Benign tumour cells stay enclosed within the tumour and do "
               "not break away to travel and form secondary tumours.",
    },
    {
        "id": "ks4-cancer-s13",
        "subtopic_slug": "cancer",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a patient might be given both surgery and "
                "chemotherapy for the same cancer.",
        "options": [
            "Surgery removes the main tumour; chemotherapy targets any cells that may have already spread",
            "Surgery and chemotherapy always cancel out each other's effects when they are used together",
            "Chemotherapy is only ever given to patients who refuse surgery",
            "Surgery is only used once chemotherapy has completely failed",
        ],
        "correct_index": 0,
        "why": "Surgery removes the main tumour, while chemotherapy can "
               "reach cells that may have already spread beyond it.",
    },
    {
        "id": "ks4-cancer-s14",
        "subtopic_slug": "cancer",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why ionising radiation is described both as a "
                "treatment for cancer and as a risk factor for it.",
        "options": [
            "Radiation is not really a risk factor for cancer at all; the idea is a common misunderstanding among patients",
            "At a controlled dose it can destroy cancer cells; at an uncontrolled dose it can damage DNA and cause cancer",
            "It always causes cancer, whatever dose is used",
            "It only ever destroys cancer cells and can never damage DNA",
        ],
        "correct_index": 1,
        "why": "A controlled, targeted dose can destroy cancer cells, while "
               "uncontrolled exposure can damage DNA in a way that causes "
               "cancer.",
    },
    {
        "id": "ks4-cancer-s15",
        "subtopic_slug": "cancer",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A woman is found to carry a BRCA1 gene mutation. Explain "
                "what this means for her going forward.",
        "options": [
            "She will definitely go on to develop breast cancer within the next year or so",
            "She has no greater risk of breast cancer than anyone else",
            "Her risk of developing breast or ovarian cancer is raised, though not made certain",
            "She is already immune to breast cancer as a result",
        ],
        "correct_index": 2,
        "why": "A BRCA1 mutation raises the probability of breast or "
               "ovarian cancer developing, without making it certain.",
    },
    {
        "id": "ks4-cancer-s16",
        "subtopic_slug": "cancer",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A scan shows a tumour enclosed within a distinct capsule, "
                "with no sign of it in surrounding tissue. Suggest whether "
                "it is more likely benign or malignant.",
        "options": [
            "Malignant, since capsules only form around aggressive tumours",
            "Malignant, since all tumours found on a scan are cancerous",
            "There is not enough information here to draw any conclusion of any kind at all",
            "Benign, since staying enclosed rather than invading is typical of a benign tumour",
        ],
        "correct_index": 3,
        "why": "Staying enclosed in a capsule, rather than invading "
               "surrounding tissue, is typical of a benign tumour.",
    },
    {
        "id": "ks4-cancer-s17",
        "subtopic_slug": "cancer",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A patient has surgery to remove a tumour, but is then also "
                "given chemotherapy. Suggest why.",
        "options": [
            "To destroy any cancer cells that may have already spread beyond the tumour before it was removed",
            "To regrow the tumour that was removed by mistake",
            "To reverse the effects of the surgery entirely",
            "Chemotherapy is never given to a patient once surgery has already taken place on them at all",
        ],
        "correct_index": 0,
        "why": "Chemotherapy given after surgery can destroy cancer cells "
               "that may have already spread beyond the tumour that was "
               "removed.",
    },
    {
        "id": "ks4-cancer-s18",
        "subtopic_slug": "cancer",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Distinguish asbestos exposure from smoking as risk factors "
                "for cancer.",
        "options": [
            "Both are exactly the same type of risk factor",
            "Asbestos exposure is environmental; smoking is a lifestyle choice",
            "Asbestos exposure is a lifestyle choice; smoking is environmental",
            "Neither one is actually linked to any type of cancer",
        ],
        "correct_index": 1,
        "why": "Asbestos exposure is an environmental risk factor, while "
               "smoking is a lifestyle risk factor.",
    },
    {
        "id": "ks4-cancer-s19",
        "subtopic_slug": "cancer",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain how long-term heavy alcohol use raises the risk of "
                "mouth and throat cancer, not only liver disease.",
        "options": [
            "Alcohol has no contact with the mouth or throat as it is swallowed",
            "Alcohol only ever affects organs it does not pass through directly",
            "Alcohol and the substances it breaks down into can damage cells in the mouth and throat as it passes through",
            "Alcohol strengthens the cells lining the mouth and the throat against any later damage",
        ],
        "correct_index": 2,
        "why": "Alcohol and its breakdown products come into direct contact "
               "with cells in the mouth and throat as it is swallowed, "
               "which can damage them.",
    },
    {
        "id": "ks4-cancer-s20",
        "subtopic_slug": "cancer",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A health report lists obesity as a risk factor for bowel, "
                "breast and uterine cancer. State what that listing means.",
        "options": [
            "Obesity directly causes tumours to form within days in any organ",
            "Obesity has no real connection to any of these three cancers",
            "Only bowel cancer, and not the other two, is actually linked to obesity",
            "Obesity is associated with a raised risk of each of these different cancers",
        ],
        "correct_index": 3,
        "why": "Obesity is associated with a raised risk of bowel, breast "
               "and uterine cancer, among others.",
    },
    {
        "id": "ks4-cancer-s21",
        "subtopic_slug": "cancer",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why a surgeon might decide not to remove a tumour, "
                "even though it is still localised.",
        "options": [
            "Its location may make it too risky to safely reach with surgery",
            "Localised tumours can never be reached by any surgeon",
            "Surgery is only ever used for tumours that have already spread everywhere",
            "A localised tumour never requires any treatment of any kind",
        ],
        "correct_index": 0,
        "why": "A tumour's location can make it too risky to remove "
               "safely, even while it is still localised.",
    },
    {
        "id": "ks4-cancer-s22",
        "subtopic_slug": "cancer",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare HPV and hepatitis B as risk factors for cancer.",
        "options": [
            "Both of these viruses are risk factors for exactly the same one single type of cancer",
            "HPV is linked mainly to cervical cancer; hepatitis B is linked mainly to liver cancer",
            "Neither virus is actually linked to any form of cancer",
            "HPV is a bacterium; hepatitis B is a fungus",
        ],
        "correct_index": 1,
        "why": "HPV is linked mainly to cervical cancer, while hepatitis B "
               "is linked mainly to liver cancer.",
    },
    {
        "id": "ks4-cancer-s23",
        "subtopic_slug": "cancer",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare the treatment options generally available for a "
                "cancer caught early, while still localised, with one "
                "caught after it has already spread.",
        "options": [
            "Exactly the same treatments are available at every stage",
            "A cancer caught early is always completely untreatable",
            "A cancer caught early can often be treated with surgery alone; one that has spread needs treatment reaching the whole body",
            "A cancer that has already spread through the body can only ever be treated with surgery to remove the original tumour",
        ],
        "correct_index": 2,
        "why": "A localised cancer caught early can often be treated with "
               "surgery alone, while one that has spread generally needs "
               "treatment that reaches the whole body.",
    },
    {
        "id": "ks4-cancer-s24",
        "subtopic_slug": "cancer",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why the drop in white blood cells caused by "
                "chemotherapy is usually temporary rather than permanent.",
        "options": [
            "White blood cells are not actually affected by chemotherapy at all",
            "Chemotherapy permanently destroys the bone marrow in every patient",
            "The white blood cells that were destroyed are rebuilt from the platelets left circulating",
            "The bone marrow's ability to make new white blood cells recovers between courses of treatment",
        ],
        "correct_index": 3,
        "why": "The bone marrow's ability to make new white blood cells "
               "generally recovers in the gaps between courses of "
               "chemotherapy.",
    },
    {
        "id": "ks4-cancer-s25",
        "subtopic_slug": "cancer",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a benign tumour pressing on a nerve might still "
                "need treatment, even though it is not cancerous.",
        "options": [
            "It can still cause harm by physically compressing the nerve as it grows",
            "Every benign tumour eventually turns malignant if it is left alone",
            "A benign tumour pressing on a nerve is not possible",
            "Only malignant tumours are ever capable of causing any harm",
        ],
        "correct_index": 0,
        "why": "A benign tumour can still cause harm by physically "
               "compressing a nerve or other structure as it grows.",
    },
    {
        "id": "ks4-cancer-s26",
        "subtopic_slug": "cancer",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why the word 'cancer' specifically refers to a "
                "malignant tumour, and not to a benign one.",
        "options": [
            "Benign tumours are simply the name that doctors use for exactly the same thing",
            "Only a malignant tumour can invade tissue and spread, which is what defines cancer",
            "Cancer refers to any lump found anywhere in the body",
            "A benign tumour always grows faster than a malignant one",
        ],
        "correct_index": 1,
        "why": "Cancer is defined by the ability to invade tissue and "
               "spread, which only a malignant tumour can do.",
    },
    {
        "id": "ks4-cancer-h05",
        "subtopic_slug": "cancer",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate this claim: 'Since radiotherapy uses radiation, "
                "and radiation causes cancer, radiotherapy must always "
                "cause cancer rather than treat it.'",
        "options": [
            "False — a controlled, targeted dose can destroy cancer cells before it causes enough damage to cause new cancer",
            "True — any use of radiation on the body always causes cancer instead",
            "True, but only because radiotherapy is never actually radiation at all",
            "False, but only because radiotherapy uses a completely different form of energy from the radiation that causes cancer",
        ],
        "correct_index": 0,
        "why": "A controlled, targeted dose of radiation can destroy "
               "cancer cells while limiting the damage that would be "
               "needed to cause new cancer.",
    },
    {
        "id": "ks4-cancer-h06",
        "subtopic_slug": "cancer",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Patients treated with radiotherapy sometimes have a "
                "slightly raised risk of developing a second, different "
                "cancer years later. Evaluate whether this contradicts "
                "radiotherapy being an effective cancer treatment.",
        "options": [
            "It fully contradicts it — an effective treatment can never carry any risk at all",
            "It does not contradict it — the benefit of treating the existing cancer can still outweigh a small added future risk",
            "It contradicts it, since no treatment is ever allowed to have any side effect",
            "It does not contradict it, but only because radiotherapy is itself incapable of ever causing a cancer in a patient",
        ],
        "correct_index": 1,
        "why": "A treatment can still be effective and worthwhile even with "
               "a small added risk, if the benefit of treating the "
               "existing cancer outweighs it.",
    },
    {
        "id": "ks4-cancer-h07",
        "subtopic_slug": "cancer",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A woman carries a BRCA1 mutation and also smokes. Predict "
                "how her overall cancer risk compares with a woman who has "
                "the mutation but does not smoke.",
        "options": [
            "Her risk is lower, since smoking cancels out the genetic risk she carries",
            "Her risk is identical, since only the genetic factor actually matters",
            "Her risk is higher, since the genetic and lifestyle risk factors add together",
            "Neither woman has any real risk without a viral infection present too",
        ],
        "correct_index": 2,
        "why": "Risk factors from different categories add together, so "
               "having both a genetic and a lifestyle risk factor gives a "
               "higher overall risk than either alone.",
    },
    {
        "id": "ks4-cancer-h08",
        "subtopic_slug": "cancer",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest what would happen to a person's cancer risk if a "
                "treatment could permanently prevent any further mutation "
                "in their cell-cycle regulatory genes.",
        "options": [
            "Their risk would rise sharply, since the regulatory genes themselves are what normally cause a cancer",
            "There would be no change at all to their cancer risk",
            "Every existing tumour would be instantly destroyed by the treatment",
            "Their risk of NEW cancers starting would fall, since new mutations could no longer accumulate there",
        ],
        "correct_index": 3,
        "why": "Since cancer begins with mutations in cell-cycle "
               "regulatory genes, preventing any further mutation there "
               "would lower the risk of new cancers starting.",
    },
    {
        "id": "ks4-cancer-h09",
        "subtopic_slug": "cancer",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate this claim: 'Since chemotherapy targets rapidly "
                "dividing cells, it must be completely selective for "
                "cancer cells and cause no side effects elsewhere.'",
        "options": [
            "False — healthy cells that also divide rapidly, such as hair follicles and gut lining, are affected too",
            "True — cancer cells are the only rapidly dividing cells anywhere in the body",
            "True, but only because hair and gut cells never actually divide",
            "False, but only because chemotherapy does not target rapidly dividing cells in the first place at all",
        ],
        "correct_index": 0,
        "why": "Chemotherapy cannot distinguish cancer cells from other "
               "rapidly dividing healthy cells, such as those in hair "
               "follicles and the gut lining, so those are affected too.",
    },
    {
        "id": "ks4-cancer-h10",
        "subtopic_slug": "cancer",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare the typical side effects of radiotherapy with "
                "those of chemotherapy, in terms of where they occur.",
        "options": [
            "Both cause identical side effects across the entire body",
            "Radiotherapy's side effects are mostly local to the treated area; chemotherapy's affect rapidly dividing cells throughout the body",
            "Radiotherapy's side effects affect rapidly dividing cells throughout the whole body; chemotherapy's affect only the area that was treated",
            "Neither treatment causes any side effects of any kind",
        ],
        "correct_index": 1,
        "why": "Radiotherapy's side effects are mostly local to the area "
               "treated, while chemotherapy's side effects arise from "
               "affecting rapidly dividing cells throughout the whole "
               "body.",
    },
    {
        "id": "ks4-cancer-h11",
        "subtopic_slug": "cancer",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A cancer has already spread to several organs. Compare how "
                "well surgery and radiotherapy alone could each treat it.",
        "options": [
            "Both could fully cure the cancer by treating each one of the affected organs at the same time",
            "Surgery could cure it fully; radiotherapy would have no effect at all",
            "Neither could reach every affected site; both are best suited to a single, localised tumour",
            "Radiotherapy could cure it fully; surgery would have no effect at all",
        ],
        "correct_index": 2,
        "why": "Both surgery and radiotherapy are best suited to treating a "
               "single, localised tumour, so neither alone can reach every "
               "site once a cancer has spread widely.",
    },
    {
        "id": "ks4-cancer-h12",
        "subtopic_slug": "cancer",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A woman learns through genetic testing that she carries a "
                "BRCA1 mutation, before any tumour has formed. Suggest how "
                "this knowledge could change her future care.",
        "options": [
            "It has no possible use, since a mutation cannot be detected at all before a tumour appears",
            "It guarantees she will never develop cancer, regardless of any future monitoring",
            "It means surgery must be performed on her immediately, regardless of any tumour",
            "It can lead to closer monitoring, so that any tumour that does form might be caught earlier",
        ],
        "correct_index": 3,
        "why": "Knowing about a raised genetic risk can lead to closer "
               "monitoring, giving a better chance of catching any future "
               "tumour early.",
    },
    {
        "id": "ks4-cancer-h13",
        "subtopic_slug": "cancer",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate this claim: 'A tumour is either completely benign "
                "or completely malignant, and doctors can always tell "
                "which just by its size.'",
        "options": [
            "False — size alone does not decide whether a tumour is benign or malignant",
            "True — a larger tumour is always malignant and a smaller one always benign",
            "True, since malignant tumours are always found to be smaller than benign ones",
            "False, but only because tumours are never actually classified in this way",
        ],
        "correct_index": 0,
        "why": "Whether a tumour is benign or malignant depends on whether "
               "it invades and spreads, not on its size.",
    },
    {
        "id": "ks4-cancer-h14",
        "subtopic_slug": "cancer",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Two patients have tumours of exactly the same size. One is "
                "treated with surgery alone; the other needs chemotherapy "
                "as well. Suggest what is most likely different between "
                "the two cases.",
        "options": [
            "The patient having chemotherapy as well most likely has a tumour that has already spread",
            "Tumour size is the only thing that ever decides which treatment is used",
            "The patient having surgery alone must have the more dangerous of the two tumours here",
            "There is no possible reason for the two patients to be treated differently",
        ],
        "correct_index": 0,
        "why": "Since size alone does not decide treatment, the patient "
               "given chemotherapy as well most likely has a tumour that "
               "has already spread beyond its original site.",
    },
    {
        "id": "ks4-cancer-h15",
        "subtopic_slug": "cancer",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare a BRCA gene mutation with an HPV infection, as two "
                "different types of cancer risk factor.",
        "options": [
            "Both are identical types of risk factor, acquired in exactly the same way",
            "An HPV infection is inherited at birth; a BRCA mutation is caught through contact with another person",
            "A BRCA mutation is usually inherited at birth; an HPV infection is instead caught later in life",
            "Neither of these is actually linked to any real risk of cancer",
        ],
        "correct_index": 2,
        "why": "A BRCA mutation is a genetic risk factor usually present "
               "from birth, while HPV is a viral risk factor caught "
               "through infection later in life.",
    },
    {
        "id": "ks4-cancer-h16",
        "subtopic_slug": "cancer",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate this claim: 'Since a benign tumour cannot spread "
                "to other organs, it can never be fatal.'",
        "options": [
            "True — no benign tumour has ever caused serious harm to a patient",
            "True, since only a malignant tumour is ever capable of causing a patient any harm at all",
            "False, but only because every benign tumour eventually turns malignant",
            "False — a benign tumour growing in a critical location, such as the brain, can still be dangerous",
        ],
        "correct_index": 3,
        "why": "A benign tumour growing in a critical location, such as "
               "the brain, can still be dangerous by pressing on vital "
               "structures, even though it does not spread.",
    },
    {
        "id": "ks4-cancer-h17",
        "subtopic_slug": "cancer",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why doctors usually try to remove or destroy a "
                "cancer while it is still small and localised, rather "
                "than waiting.",
        "options": [
            "A larger, more advanced cancer is generally harder to treat and more likely to have already spread",
            "Cancer only ever appears in a patient once it has already spread right through the whole body",
            "Waiting has no effect at all on how easy a cancer is to treat",
            "A small, localised cancer is always more dangerous than a larger one",
        ],
        "correct_index": 0,
        "why": "The longer a cancer is left, the more likely it is to grow "
               "and spread, making it generally harder to treat.",
    },
    {
        "id": "ks4-cancer-h18",
        "subtopic_slug": "cancer",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A patient stops a course of chemotherapy partway through, "
                "once their symptoms begin to improve. Predict the risk of "
                "doing this.",
        "options": [
            "There is no risk at all, since the cancer is already fully treated by that point",
            "Cancer cells that have not yet been destroyed may survive and continue dividing",
            "The remaining chemotherapy drug will destroy the cancer completely on its own",
            "Stopping early always improves the final outcome of the treatment",
        ],
        "correct_index": 1,
        "why": "Symptoms improving does not mean every cancer cell has "
               "been destroyed, so stopping early risks leaving cells "
               "that can survive and continue dividing.",
    },
    {
        "id": "ks4-cancer-h19",
        "subtopic_slug": "cancer",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare how smoking and heavy alcohol use each raise cancer "
                "risk, in terms of the route by which harmful substances "
                "reach the affected cells.",
        "options": [
            "Both reach the affected cells in exactly the same way, through the skin",
            "Smoking's carcinogens are inhaled directly into the lungs; alcohol's harmful substances are absorbed as it is swallowed and processed",
            "Neither substance ever makes direct contact with the cells it affects",
            "Smoking's carcinogens are swallowed and reach the liver that way; alcohol's harmful substances are inhaled straight into the lungs",
        ],
        "correct_index": 1,
        "why": "Smoking's carcinogens are inhaled directly into the lungs, "
               "while alcohol's harmful substances make contact with "
               "cells as it is swallowed and processed by the body.",
    },
    {
        "id": "ks4-cancer-h20",
        "subtopic_slug": "cancer",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why a skin cancer is often diagnosed at an earlier "
                "stage than a cancer growing deep inside an internal "
                "organ.",
        "options": [
            "Skin cancers are always more dangerous than internal ones, so doctors check for them far more urgently",
            "Internal cancers never produce a tumour large enough to be noticed",
            "Skin cancer cells divide much faster than the cells of any internal cancer",
            "A change on the skin's surface can often be seen or felt, unlike a tumour hidden deep inside the body",
        ],
        "correct_index": 3,
        "why": "A visible or noticeable change on the skin is often spotted "
               "sooner than a tumour hidden deep inside the body.",
    },
    {
        "id": "ks4-cancer-h21",
        "subtopic_slug": "cancer",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate this claim: 'A person with none of the known "
                "lifestyle, environmental, genetic or viral risk factors "
                "for a cancer cannot develop it.'",
        "options": [
            "False — cancer can still arise from a mutation with no identifiable risk factor behind it",
            "True — a cancer can only ever develop in a person when a known risk factor is present",
            "True, since mutations never occur without an external cause behind them",
            "False, but only because every cancer is actually caused by a virus",
        ],
        "correct_index": 0,
        "why": "Cancer begins with mutations that can occur without any "
               "identifiable risk factor being present, so having none of "
               "the known risk factors does not rule it out.",
    },
    {
        "id": "ks4-cancer-h22",
        "subtopic_slug": "cancer",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Predict the effect on a population's overall cancer rate "
                "of completely eliminating smoking, while every other "
                "risk factor remains unchanged.",
        "options": [
            "Cancer rates would fall, since several cancers are linked to smoking, though rates would not reach zero",
            "Cancer rates would fall to exactly zero across every type of cancer",
            "Cancer rates would rise, since smoking actually protects against most cancers",
            "Cancer rates would stay exactly the same, since smoking has no link at all to any single type of cancer",
        ],
        "correct_index": 0,
        "why": "Removing smoking would lower rates of the several cancers "
               "linked to it, but other risk factors would remain, so "
               "cancer would not disappear entirely.",
    },
    {
        "id": "ks4-cancer-h23",
        "subtopic_slug": "cancer",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare how a viral risk factor for cancer, such as HPV, "
                "and a genetic risk factor, such as a BRCA mutation, can "
                "each be managed.",
        "options": [
            "Both can be completely prevented in exactly the same way",
            "Neither type of risk factor can be managed or reduced in any way",
            "Exposure to a viral risk factor can potentially be avoided; a genetic risk factor can only be monitored, not avoided",
            "A genetic risk factor can be avoided entirely by changing lifestyle; exposure to a viral one can never be avoided",
        ],
        "correct_index": 2,
        "why": "Exposure to a virus can potentially be avoided, while an "
               "inherited genetic mutation is already present and can "
               "only be monitored for, not avoided.",
    },
    {
        "id": "ks4-cancer-h24",
        "subtopic_slug": "cancer",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate this claim: 'Since obesity is a risk factor for "
                "several cancers, every person who is obese will develop "
                "cancer.'",
        "options": [
            "True — a risk factor always guarantees the disease it is linked to",
            "True, but only for bowel cancer specifically, not the others",
            "False, but only because obesity is not linked to any one type of cancer in the first place",
            "False — a risk factor raises probability, but never makes a disease certain for any individual",
        ],
        "correct_index": 3,
        "why": "A risk factor raises the probability of disease; it never "
               "makes it certain for any individual, however strong the "
               "link.",
    },
    {
        "id": "ks4-cancer-h25",
        "subtopic_slug": "cancer",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain the difference between using genetic testing to "
                "monitor cancer risk and using surgery or chemotherapy to "
                "treat cancer.",
        "options": [
            "Genetic testing helps detect risk or disease early; surgery and chemotherapy treat cancer once it exists",
            "Both achieve exactly the same outcome, just using different equipment",
            "Genetic testing treats existing tumours directly, without any need for surgery",
            "Surgery and chemotherapy are used only on those patients who carry no genetic risk factors at all here",
        ],
        "correct_index": 0,
        "why": "Genetic testing helps detect risk or catch disease early, "
               "while surgery and chemotherapy are treatments used once "
               "cancer already exists.",
    },
    {
        "id": "ks4-cancer-h26",
        "subtopic_slug": "cancer",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A researcher lists four different types of risk factor for "
                "cancer. Identify which one of these examples is a "
                "lifestyle risk factor, as opposed to environmental, "
                "genetic or viral.",
        "options": [
            "Long-term exposure to asbestos fibres at work",
            "Smoking cigarettes over many years",
            "Inheriting a mutated BRCA1 gene",
            "Long-term infection with the hepatitis B virus",
        ],
        "correct_index": 1,
        "why": "Smoking is a lifestyle choice, unlike asbestos exposure "
               "(environmental), a BRCA1 mutation (genetic) or hepatitis B "
               "infection (viral).",
    },

    # ══════════════════════════════════════════════════════════════════
    # plant-tissues · e05-e12, s05-s26, h05-h26
    # ══════════════════════════════════════════════════════════════════
    {
        "id": "ks4-plant-tissues-e05",
        "subtopic_slug": "plant-tissues",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the main functions of the stem in a plant.",
        "options": [
            "Support and transporting substances between roots and leaves",
            "Producing pollen for reproduction",
            "Absorbing water directly from the soil",
            "Carrying out most of the plant's photosynthesis in its outer cells",
        ],
        "correct_index": 0,
        "why": "The stem supports the plant and transports substances "
               "between the roots and the leaves.",
    },
    {
        "id": "ks4-plant-tissues-e06",
        "subtopic_slug": "plant-tissues",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the main function of a flower.",
        "options": [
            "Support and transport",
            "Reproduction",
            "Water absorption",
            "Gas exchange",
        ],
        "correct_index": 1,
        "why": "The flower is the plant organ involved in reproduction.",
    },
    {
        "id": "ks4-plant-tissues-e07",
        "subtopic_slug": "plant-tissues",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State where palisade mesophyll cells are found in a leaf.",
        "options": [
            "In the lower epidermis",
            "In the shaded layer just below the spongy mesophyll",
            "In the upper part of the leaf, nearest the light",
            "Inside the xylem vessels",
        ],
        "correct_index": 2,
        "why": "Palisade mesophyll cells are found in the upper part of "
               "the leaf, where they receive the most light.",
    },
    {
        "id": "ks4-plant-tissues-e08",
        "subtopic_slug": "plant-tissues",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the function of the air spaces between spongy "
                "mesophyll cells.",
        "options": [
            "Storing starch produced by photosynthesis",
            "Strengthening the leaf against wind and insect damage",
            "Absorbing light for photosynthesis",
            "Allowing gases to diffuse easily to and from cells",
        ],
        "correct_index": 3,
        "why": "The air spaces in spongy mesophyll allow carbon dioxide and "
               "oxygen to diffuse easily to and from the photosynthesising "
               "cells.",
    },
    {
        "id": "ks4-plant-tissues-e09",
        "subtopic_slug": "plant-tissues",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the main function of the waxy cuticle on a leaf's "
                "surface.",
        "options": [
            "Reducing water loss from the leaf",
            "Absorbing carbon dioxide directly",
            "Producing the leaf's green colour",
            "Transporting sugars out of the leaf",
        ],
        "correct_index": 0,
        "why": "The waxy cuticle is a waterproof layer that reduces water "
               "loss by evaporation from the leaf surface.",
    },
    {
        "id": "ks4-plant-tissues-e10",
        "subtopic_slug": "plant-tissues",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State how xylem cells are arranged to form a continuous "
                "tube.",
        "options": [
            "They are wrapped in a spiral around the phloem",
            "They are stacked end to end with no end walls between them",
            "They are scattered at random through the whole stem tissue",
            "They are joined only at sieve plates",
        ],
        "correct_index": 1,
        "why": "Xylem cells are stacked end to end with no end walls "
               "between them, forming one continuous open tube.",
    },
    {
        "id": "ks4-plant-tissues-e11",
        "subtopic_slug": "plant-tissues",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State how many guard cells surround a single stoma.",
        "options": [
            "One",
            "Three",
            "Two",
            "Four",
        ],
        "correct_index": 2,
        "why": "A pair of two guard cells surrounds each stoma.",
    },
    {
        "id": "ks4-plant-tissues-e12",
        "subtopic_slug": "plant-tissues",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what a vascular bundle in a leaf contains.",
        "options": [
            "Only xylem tissue",
            "Only phloem tissue",
            "Guard cells and stomata only",
            "Both xylem and phloem tissue",
        ],
        "correct_index": 3,
        "why": "A vascular bundle contains both xylem and phloem, running "
               "together through the leaf.",
    },
    {
        "id": "ks4-plant-tissues-s05",
        "subtopic_slug": "plant-tissues",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain how root hair cells are adapted to absorb water "
                "efficiently.",
        "options": [
            "They have a long extension that increases their surface area",
            "They contain chloroplasts to photosynthesise underground",
            "They are covered in a thick, waxy, waterproof layer",
            "They have no cell membrane, allowing water to pass freely",
        ],
        "correct_index": 0,
        "why": "A root hair cell's long extension increases its surface "
               "area, helping it absorb water efficiently.",
    },
    {
        "id": "ks4-plant-tissues-s06",
        "subtopic_slug": "plant-tissues",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain how the epidermis of a leaf protects the tissues "
                "beneath it.",
        "options": [
            "It converts sunlight directly into a chemical barrier",
            "It forms a protective outer layer against damage, pests and water loss",
            "It absorbs all incoming light before it reaches the mesophyll",
            "It actively attacks and digests any pathogen landing on the leaf surface",
        ],
        "correct_index": 1,
        "why": "The epidermis forms a protective outer layer, guarding the "
               "tissues beneath against damage, pests and water loss.",
    },
    {
        "id": "ks4-plant-tissues-s07",
        "subtopic_slug": "plant-tissues",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare the number of chloroplasts typically found in "
                "palisade mesophyll cells with the number in spongy "
                "mesophyll cells.",
        "options": [
            "Both layers contain exactly the same number of chloroplasts",
            "Spongy mesophyll cells contain far more chloroplasts, since they sit deeper in the leaf",
            "Palisade mesophyll cells contain more chloroplasts, since they receive the most light",
            "Neither layer contains any chloroplasts at all",
        ],
        "correct_index": 2,
        "why": "Palisade mesophyll cells, receiving the most light, are "
               "packed with more chloroplasts than spongy mesophyll cells.",
    },
    {
        "id": "ks4-plant-tissues-s08",
        "subtopic_slug": "plant-tissues",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare the cell walls of xylem vessels with the cell "
                "walls of phloem sieve tubes.",
        "options": [
            "Both are strengthened with exactly the same amount of lignin",
            "Phloem walls are lignified; xylem walls are not",
            "Neither xylem nor phloem cell walls contain any lignin",
            "Xylem walls are strengthened with lignin; phloem walls are not",
        ],
        "correct_index": 3,
        "why": "Xylem walls are strengthened with lignin, which phloem "
               "walls lack, since phloem cells stay alive.",
    },
    {
        "id": "ks4-plant-tissues-s09",
        "subtopic_slug": "plant-tissues",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a mature phloem sieve tube cell relies on its "
                "companion cell for energy.",
        "options": [
            "The sieve tube cell loses most of its own organelles, including its nucleus, to make room for flow",
            "The sieve tube cell is completely dead, like a xylem vessel",
            "The sieve tube cell keeps so many organelles of its own that no room is left for any respiration",
            "The companion cell physically replaces the sieve tube cell's cell wall",
        ],
        "correct_index": 0,
        "why": "A mature sieve tube cell loses most of its own organelles "
               "to make room for the flow of sap, so it relies on its "
               "companion cell for energy.",
    },
    {
        "id": "ks4-plant-tissues-s10",
        "subtopic_slug": "plant-tissues",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why the leaf is described as carrying out several "
                "different jobs at once.",
        "options": [
            "It carries out only photosynthesis, and nothing else",
            "It combines photosynthesis, gas exchange and water loss within one organ",
            "It only transports substances, and never carries out photosynthesis itself",
            "Each job is carried out by a completely separate leaf",
        ],
        "correct_index": 1,
        "why": "The leaf combines photosynthesis, gas exchange and water "
               "loss within one organ, all carried out by its different "
               "tissues.",
    },
    {
        "id": "ks4-plant-tissues-s11",
        "subtopic_slug": "plant-tissues",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A leaf's waxy cuticle is scraped away by an insect. Predict "
                "the effect on the leaf.",
        "options": [
            "The leaf photosynthesises faster, since more light can reach the mesophyll",
            "The leaf's colour changes permanently to yellow",
            "The leaf loses water more quickly than normal through its damaged surface",
            "The leaf stops producing oxygen altogether",
        ],
        "correct_index": 2,
        "why": "Without its waxy cuticle, the leaf's surface loses its "
               "waterproof protection, so water evaporates from it more "
               "quickly.",
    },
    {
        "id": "ks4-plant-tissues-s12",
        "subtopic_slug": "plant-tissues",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest the disadvantage there would be if xylem vessels "
                "stayed alive, rather than dying as they mature.",
        "options": [
            "Living contents would take up space and could obstruct the flow of water",
            "A living xylem vessel would conduct water far more quickly than a dead one",
            "Living cells would make the xylem far stronger than lignin alone can",
            "There would be no disadvantage of any kind to xylem staying alive",
        ],
        "correct_index": 0,
        "why": "Living contents would take up space inside the vessel and "
               "could obstruct the free flow of water, which dying "
               "removes.",
    },
    {
        "id": "ks4-plant-tissues-s13",
        "subtopic_slug": "plant-tissues",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why guard cells are unevenly thickened, with a "
                "thicker inner wall facing the stoma.",
        "options": [
            "This uneven thickening makes the pair bow apart into a pore shape when turgid",
            "The uneven thickening has no effect on the shape the stoma takes when turgid",
            "It prevents the guard cells from ever opening under any conditions",
            "It makes the guard cells identical in shape to epidermal cells",
        ],
        "correct_index": 0,
        "why": "The uneven wall thickness makes the guard cell pair bow "
               "apart into a pore shape as they take up water and become "
               "turgid.",
    },
    {
        "id": "ks4-plant-tissues-s14",
        "subtopic_slug": "plant-tissues",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest the effect on photosynthesis if a leaf's spongy "
                "mesophyll had no air spaces between its cells.",
        "options": [
            "Photosynthesis would speed up, since the cells would be packed more tightly",
            "Carbon dioxide would reach the photosynthesising cells more slowly",
            "The leaf would immediately stop losing any water through transpiration",
            "The palisade layer would take over the spongy layer's job instantly",
        ],
        "correct_index": 1,
        "why": "Without air spaces to allow easy diffusion, carbon dioxide "
               "would reach the photosynthesising cells more slowly.",
    },
    {
        "id": "ks4-plant-tissues-s15",
        "subtopic_slug": "plant-tissues",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest a structural reason why phloem can carry substances "
                "in either direction while xylem carries water in one "
                "direction only.",
        "options": [
            "Xylem vessels are living, allowing flow in only one fixed direction",
            "Phloem sieve tubes are dead, hollow tubes, so the sap inside them runs either way with nothing at all to control it",
            "Living sieve tube cells can actively load and unload sucrose at either end, unlike the passively-drawn water in xylem",
            "Xylem and phloem are actually the exact same tissue, just given two names",
        ],
        "correct_index": 2,
        "why": "Because phloem cells are alive, they can actively load and "
               "unload sucrose at either end, letting flow go either way, "
               "unlike xylem's passively-drawn water.",
    },
    {
        "id": "ks4-plant-tissues-s16",
        "subtopic_slug": "plant-tissues",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare the upper epidermis of a leaf with the lower "
                "epidermis, in terms of function.",
        "options": [
            "Both layers are completely identical in structure and function",
            "The lower epidermis lets light through from below; the upper epidermis carries the stomata",
            "Neither layer has any specific function beyond covering the leaf",
            "The upper epidermis lets light through; the lower epidermis carries most of the stomata",
        ],
        "correct_index": 3,
        "why": "The upper epidermis is thin and transparent to let light "
               "through, while the lower epidermis carries most of the "
               "stomata.",
    },
    {
        "id": "ks4-plant-tissues-s17",
        "subtopic_slug": "plant-tissues",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a single xylem vessel cannot, by itself, move "
                "water all the way from root to leaf in a tall tree.",
        "options": [
            "Xylem vessels are joined end to end into one long continuous column, so it is the whole tissue, not one vessel, that moves the water",
            "A single xylem vessel grows longer as the tree grows, so one vessel on its own always reaches from the roots to the topmost leaf",
            "Water is instead moved entirely by a single very long root hair cell",
            "No plant taller than a few centimetres can move water in xylem at all",
        ],
        "correct_index": 0,
        "why": "Xylem vessels are joined end to end into one continuous "
               "column, so the whole tissue, not any single vessel, moves "
               "water the full height of the plant.",
    },
    {
        "id": "ks4-plant-tissues-s18",
        "subtopic_slug": "plant-tissues",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the relationship between a companion cell and a "
                "sieve tube cell.",
        "options": [
            "There is no direct relationship between the two cell types",
            "Each sieve tube cell has at least one companion cell lying directly beside it",
            "A single companion cell in the root supplies energy to the entire plant's phloem",
            "Companion cells replace sieve tube cells once they mature",
        ],
        "correct_index": 1,
        "why": "Each sieve tube cell has at least one companion cell "
               "lying directly beside it, supplying the energy it needs.",
    },
    {
        "id": "ks4-plant-tissues-s19",
        "subtopic_slug": "plant-tissues",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A mutation stops a plant's guard cells from ever changing "
                "shape. Suggest one problem this could cause.",
        "options": [
            "The plant would photosynthesise faster at all times, since a stoma fixed in shape is held permanently wide open",
            "The leaf would produce extra chlorophyll to compensate",
            "Stomata could get stuck open, losing water uncontrollably, or stuck shut, starving photosynthesis of carbon dioxide",
            "This mutation would have no effect on the plant at all",
        ],
        "correct_index": 2,
        "why": "Without guard cells able to change shape, stomata could get "
               "stuck open, losing water uncontrollably, or stuck shut, "
               "starving photosynthesis of carbon dioxide.",
    },
    {
        "id": "ks4-plant-tissues-s20",
        "subtopic_slug": "plant-tissues",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why cutting straight through the central vein of a "
                "leaf disrupts the leaf's water supply.",
        "options": [
            "The central vein contains no xylem, only phloem",
            "Cutting the vein has no effect, since every cell in the leaf draws its own water straight from the air",
            "The central vein only carries sugars, never water",
            "The vein contains the xylem supplying water to that part of the leaf, which the cut interrupts",
        ],
        "correct_index": 3,
        "why": "The central vein contains the xylem supplying water to "
               "that part of the leaf, so cutting it interrupts the "
               "supply.",
    },
    {
        "id": "ks4-plant-tissues-s21",
        "subtopic_slug": "plant-tissues",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Distinguish the role of the epidermis from the role of the "
                "waxy cuticle it produces.",
        "options": [
            "The epidermis is the layer of cells; the cuticle is the waterproof coating those cells secrete",
            "The epidermis and the cuticle are two names for the same single layer",
            "The cuticle is the layer of living cells; the epidermis is the waxy coating that those cells secrete",
            "Neither structure has any real function in the leaf",
        ],
        "correct_index": 0,
        "why": "The epidermis is the layer of living cells; the cuticle is "
               "the waterproof coating those cells secrete on top of "
               "themselves.",
    },
    {
        "id": "ks4-plant-tissues-s22",
        "subtopic_slug": "plant-tissues",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "An insect eats away the palisade mesophyll of a leaf but "
                "leaves the spongy mesophyll intact. Predict the effect on "
                "photosynthesis in that leaf.",
        "options": [
            "Photosynthesis is unaffected, since spongy mesophyll holds just as many chloroplasts",
            "Photosynthesis falls significantly, since most chloroplasts were in the palisade layer",
            "Photosynthesis increases, since removing cells lets in more light",
            "Photosynthesis stops entirely across the whole plant immediately",
        ],
        "correct_index": 1,
        "why": "Since most chloroplasts sit in the palisade layer, losing "
               "it causes photosynthesis in that leaf to fall "
               "significantly.",
    },
    {
        "id": "ks4-plant-tissues-s23",
        "subtopic_slug": "plant-tissues",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain the function of a sieve plate in phloem.",
        "options": [
            "It blocks sugar solution from passing between sieve tube cells, so each one works alone",
            "It filters out water so that only pure sugar can pass through",
            "It is a perforated wall that lets sugar solution flow from one sieve tube cell to the next",
            "It converts sugars into starch as they pass through it",
        ],
        "correct_index": 2,
        "why": "A sieve plate is a perforated end wall that lets sugar "
               "solution flow from one sieve tube cell into the next.",
    },
    {
        "id": "ks4-plant-tissues-s24",
        "subtopic_slug": "plant-tissues",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A leaf variety has unusually few vascular bundles running "
                "through it. Suggest the likely effect on that leaf.",
        "options": [
            "The leaf would photosynthesise faster, since fewer bundles leave more room for mesophyll",
            "The leaf would need no water supply at all",
            "The leaf would produce far more oxygen than a typical leaf",
            "Parts of the leaf farther from a vascular bundle may receive water and sugar less efficiently",
        ],
        "correct_index": 3,
        "why": "With fewer vascular bundles, cells farther from one may "
               "receive water and sugar less efficiently than in a leaf "
               "with a denser network.",
    },
    {
        "id": "ks4-plant-tissues-s25",
        "subtopic_slug": "plant-tissues",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest an advantage of xylem and phloem running together "
                "as one vascular bundle, rather than separately through "
                "the leaf.",
        "options": [
            "Water, minerals and sugars can all be exchanged with nearby cells along a single route",
            "Running together blocks both tissues, so neither can transport anything along the bundle",
            "It prevents the leaf from ever losing water through transpiration",
            "It means xylem and phloem become one single, identical tissue",
        ],
        "correct_index": 0,
        "why": "Running together lets water, minerals and sugars all be "
               "exchanged with nearby cells along a single shared route.",
    },
    {
        "id": "ks4-plant-tissues-s26",
        "subtopic_slug": "plant-tissues",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest what would happen to xylem vessels if their walls "
                "contained no lignin.",
        "options": [
            "They would conduct water far more efficiently than before",
            "They would be more likely to collapse under the pressure of water being pulled through them",
            "They would take up sugars instead of water, since it is lignin that selects what may enter",
            "They would develop a nucleus and become living cells",
        ],
        "correct_index": 1,
        "why": "Without lignin to strengthen their walls, xylem vessels "
               "would be more likely to collapse under the pressure of "
               "water being pulled through them.",
    },
    {
        "id": "ks4-plant-tissues-h05",
        "subtopic_slug": "plant-tissues",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate this claim: 'Since xylem cells are dead, xylem "
                "cannot really be classed as a tissue.'",
        "options": [
            "False — a tissue is defined by similar cells sharing one function, not by whether those cells are alive",
            "True — only living cells can ever form a tissue",
            "True, but only because xylem should be classed as an organ, since it combines several different tissues",
            "False, but only because xylem cells are not actually dead",
        ],
        "correct_index": 0,
        "why": "A tissue is defined by similar cells sharing one function, "
               "not by whether the cells are alive, so xylem still counts "
               "as a tissue despite being dead.",
    },
    {
        "id": "ks4-plant-tissues-h06",
        "subtopic_slug": "plant-tissues",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why phloem transport requires a constant supply of "
                "ATP from companion cells, while xylem transport does not "
                "need any energy input at all.",
        "options": [
            "Xylem transport is driven by evaporation pulling water up passively; phloem transport requires sucrose to be actively loaded",
            "Xylem cells generate their own ATP internally, unlike phloem cells",
            "Phloem transport happens only at night, when the leaf has no other demand at all for the ATP that its own cells are making",
            "Neither tissue actually requires or uses any energy at any point",
        ],
        "correct_index": 0,
        "why": "Xylem transport is driven passively by evaporation pulling "
               "water upward, while phloem transport needs sucrose to be "
               "actively loaded, which requires energy.",
    },
    {
        "id": "ks4-plant-tissues-h07",
        "subtopic_slug": "plant-tissues",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A mutation stops a plant producing lignin anywhere in its "
                "body. Predict the effect on the plant as a whole.",
        "options": [
            "The plant would grow taller and stronger than normal",
            "Only the leaves would be affected; the stem and roots would be unaffected",
            "The plant would struggle to stand upright and its xylem vessels could collapse",
            "The plant would be completely unaffected, since lignin has no structural role",
        ],
        "correct_index": 2,
        "why": "Without lignin, the plant would lose much of its structural "
               "support and its xylem vessels could collapse under the "
               "pressure of water being drawn through them.",
    },
    {
        "id": "ks4-plant-tissues-h08",
        "subtopic_slug": "plant-tissues",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare the likely rate of water loss through the surface "
                "of a very young, newly unfurled leaf with a fully mature "
                "leaf of the same species, assuming the young leaf has "
                "not yet built up a full waxy cuticle.",
        "options": [
            "Both leaves lose water at the same rate, since water escapes only through the stomata",
            "The mature leaf loses water faster, since its cuticle is thicker",
            "Neither leaf loses any water at all through its surface",
            "The young leaf likely loses water faster, since its thinner cuticle offers less protection",
        ],
        "correct_index": 3,
        "why": "A thinner cuticle offers less protection against "
               "evaporation, so the younger leaf likely loses water "
               "faster than the mature one.",
    },
    {
        "id": "ks4-plant-tissues-h09",
        "subtopic_slug": "plant-tissues",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate this claim: 'Since companion cells only support "
                "the phloem sieve tubes, they are not really essential to "
                "the plant.'",
        "options": [
            "False — without a companion cell's energy, sieve tube loading could fail, disrupting translocation",
            "True — sieve tubes can load sucrose perfectly well without any companion cell",
            "True, since companion cells are not connected to sieve tubes in any way",
            "False, but only because a companion cell takes over from the sieve tube and carries the sap itself",
        ],
        "correct_index": 0,
        "why": "Without the energy a companion cell supplies, sucrose "
               "loading into the sieve tube could fail, disrupting "
               "translocation, so companion cells are essential.",
    },
    {
        "id": "ks4-plant-tissues-h10",
        "subtopic_slug": "plant-tissues",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why guard cells, unlike the ordinary epidermal "
                "cells around them, are able to change shape to open and "
                "close a pore.",
        "options": [
            "Ordinary epidermal cells are actually more flexible than guard cells",
            "Guard cells have an uneven cell wall thickness that makes them bow apart as they take up water",
            "Guard cells contain no cell wall at all, unlike epidermal cells",
            "Ordinary epidermal cells also bow apart in just the same way, so every cell forms its own pore",
        ],
        "correct_index": 1,
        "why": "The uneven wall thickness of guard cells makes them bow "
               "apart as they take up water, which ordinary epidermal "
               "cells do not do.",
    },
    {
        "id": "ks4-plant-tissues-h11",
        "subtopic_slug": "plant-tissues",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare the efficiency of gas exchange in a leaf with both "
                "palisade and spongy mesophyll to one built from palisade "
                "mesophyll alone, with no spongy layer.",
        "options": [
            "Both leaves would exchange gases equally well, since only palisade cells matter",
            "The palisade-only leaf would exchange gases more efficiently, since its tightly packed cells all sit closer to the air outside the leaf",
            "The leaf with both layers would exchange gases more efficiently, since the spongy layer's air spaces let gases diffuse further into the leaf",
            "Neither leaf could exchange any gases at all without a phloem layer present",
        ],
        "correct_index": 2,
        "why": "The spongy layer's air spaces let gases diffuse further "
               "into the leaf, so a leaf with both layers exchanges gases "
               "more efficiently than one with palisade cells alone.",
    },
    {
        "id": "ks4-plant-tissues-h12",
        "subtopic_slug": "plant-tissues",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest the effect on phloem transport if a plant's "
                "companion cells were destroyed, while the sieve tube "
                "cells themselves remained physically intact.",
        "options": [
            "Transport would continue entirely unaffected, since a sieve tube cell makes all of the ATP it needs itself",
            "Transport would speed up, since companion cells normally slow the process down",
            "The sieve tubes would immediately become photosynthetic instead",
            "Sucrose loading would likely fail without the energy companion cells normally supply, disrupting translocation",
        ],
        "correct_index": 3,
        "why": "Without the energy companion cells normally supply, "
               "sucrose loading would likely fail, disrupting "
               "translocation even with the sieve tubes intact.",
    },
    {
        "id": "ks4-plant-tissues-h13",
        "subtopic_slug": "plant-tissues",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate this claim: 'A leaf could photosynthesise just as "
                "well without any epidermis at all.'",
        "options": [
            "False — without the epidermis and its cuticle, the leaf would likely dry out and be damaged before photosynthesis could continue normally",
            "True — the epidermis plays no part in keeping a leaf able to photosynthesise",
            "True, since photosynthesis happens only in the epidermis itself",
            "False, but only because the epidermis is the layer that makes all the leaf's chlorophyll, so losing it stops photosynthesis outright",
        ],
        "correct_index": 0,
        "why": "Without the epidermis and its protective cuticle, a leaf "
               "would likely dry out and be damaged, disrupting normal "
               "photosynthesis rather than leaving it unaffected.",
    },
    {
        "id": "ks4-plant-tissues-h14",
        "subtopic_slug": "plant-tissues",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare how a leaf adapted for a shaded environment might "
                "differ in its palisade mesophyll from one adapted for "
                "full sun, in terms of chloroplast need.",
        "options": [
            "A shaded leaf would need far fewer chloroplasts, since there is much less light for each one of them to be capturing",
            "A shaded leaf might pack its palisade cells with more chloroplasts, to capture as much of the limited light as possible",
            "Chloroplast number in palisade cells never varies between different environments",
            "A sun leaf would need no palisade mesophyll at all",
        ],
        "correct_index": 1,
        "why": "A shaded leaf may pack its palisade cells with more "
               "chloroplasts, helping it capture as much of the limited "
               "available light as possible.",
    },
    {
        "id": "ks4-plant-tissues-h15",
        "subtopic_slug": "plant-tissues",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why both xylem and phloem are found together in "
                "the same vascular bundle in a leaf, rather than the leaf "
                "growing two entirely separate transport systems.",
        "options": [
            "Combining them lets nutrients and water be exchanged efficiently with the same surrounding cells along one route",
            "Two separate systems would be far more efficient, since neither one of them would slow the other down at all",
            "Running them together stops the leaf from losing any water at all",
            "It is purely coincidental and offers no advantage to the plant",
        ],
        "correct_index": 0,
        "why": "Combining xylem and phloem in one bundle lets water and "
               "nutrients be exchanged efficiently with the same "
               "surrounding cells along a single shared route.",
    },
    {
        "id": "ks4-plant-tissues-h16",
        "subtopic_slug": "plant-tissues",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate this claim: 'Since a xylem vessel is hollow, it "
                "must be weaker than a solid living stem cell.'",
        "options": [
            "True — a hollow tube can never be as strong as a solid living cell",
            "True, since lignin thins the xylem wall rather than strengthening it, leaving it fragile",
            "False, but only because xylem vessels are not actually hollow",
            "False — the lignified walls of a xylem vessel can be very strong, despite being hollow",
        ],
        "correct_index": 3,
        "why": "The lignified walls of a xylem vessel can be very strong "
               "despite being hollow, so hollowness alone does not make "
               "it weaker.",
    },
    {
        "id": "ks4-plant-tissues-h17",
        "subtopic_slug": "plant-tissues",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "An early frost damages only the palisade mesophyll of a "
                "plant's leaves, leaving the rest of the leaf structure "
                "intact. Predict the main effect.",
        "options": [
            "Photosynthesis falls sharply, since most chloroplasts were lost with the palisade layer",
            "Water loss through the stomata stops completely as a result",
            "The xylem stops transporting water to those leaves, since palisade cells drive the pull",
            "The leaf's epidermis takes over photosynthesis instead",
        ],
        "correct_index": 0,
        "why": "Since most chloroplasts sit in the palisade layer, "
               "damaging it causes photosynthesis to fall sharply.",
    },
    {
        "id": "ks4-plant-tissues-h18",
        "subtopic_slug": "plant-tissues",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why xylem vessels lose their living contents as "
                "they mature, while phloem sieve tubes remain living, "
                "despite both being transport tissues.",
        "options": [
            "Both tissues do lose their living contents as they mature, so the only real difference between the two of them is one of name alone",
            "Water can move through xylem simply by being pulled; sucrose must be actively loaded and unloaded in phloem, which needs living cells",
            "Phloem sieve tubes lose their contents too, immediately after forming",
            "Xylem vessels stay alive for the whole life of the plant, unlike phloem",
        ],
        "correct_index": 1,
        "why": "Water moves through xylem simply by being pulled, needing "
               "no living cells, while sucrose must be actively loaded "
               "and unloaded in phloem, which needs living cells.",
    },
    {
        "id": "ks4-plant-tissues-h19",
        "subtopic_slug": "plant-tissues",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why damage to the xylem in a plant's stem can "
                "affect leaves far above the point of damage, even though "
                "the damage itself is localised.",
        "options": [
            "Damage to the stem has no effect above it, since every leaf stores all of the water that it will need",
            "The roots automatically reroute water through the phloem instead",
            "Xylem vessels form one continuous column, so a break interrupts the water supply to everything above it",
            "Only the single leaf directly above the damage is ever affected",
        ],
        "correct_index": 2,
        "why": "Because xylem vessels form one continuous column, a break "
               "at any point interrupts the water supply to everything "
               "above it.",
    },
    {
        "id": "ks4-plant-tissues-h20",
        "subtopic_slug": "plant-tissues",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate this claim: 'All the stomata on a single leaf "
                "must open and close in perfect unison, since every pair "
                "of guard cells is built identically.'",
        "options": [
            "True — guard cells built to an identical structure always respond together, whatever the conditions around each one",
            "True, since a leaf only ever contains a single pair of guard cells",
            "False, but only because guard cells are not actually identical to one another",
            "False — nearby conditions can vary across a leaf, so identical guard cells can still respond at slightly different times",
        ],
        "correct_index": 3,
        "why": "Even with identical guard cell structure, local conditions "
               "can vary across a leaf, so stomata can still respond at "
               "slightly different times.",
    },
    {
        "id": "ks4-plant-tissues-h21",
        "subtopic_slug": "plant-tissues",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why a leaf's vascular bundles form early, while "
                "the leaf is still very small, rather than developing "
                "only once the leaf is fully grown.",
        "options": [
            "Every part of the growing leaf needs a water and sugar supply throughout its development, not only once it is mature",
            "Vascular bundles are not actually needed until a leaf stops growing",
            "A fully grown leaf survives for weeks with no supply at all, so its bundles can safely form right at the very end",
            "Leaves grow instantly, so there is no early stage requiring a bundle",
        ],
        "correct_index": 0,
        "why": "A growing leaf needs a water and sugar supply throughout "
               "its development, not only once mature, which is why "
               "vascular bundles form early.",
    },
    {
        "id": "ks4-plant-tissues-h22",
        "subtopic_slug": "plant-tissues",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest a disadvantage a very thick waxy cuticle could have "
                "for a leaf, alongside its advantage of reducing water "
                "loss.",
        "options": [
            "A thick cuticle has no possible disadvantage of any kind",
            "A very thick cuticle could also make it harder for light and gases to reach the cells beneath it",
            "A thick cuticle would prevent the leaf losing any structural strength",
            "A thick cuticle stops the roots absorbing water, since uptake is driven from the leaf surface",
        ],
        "correct_index": 1,
        "why": "A very thick cuticle, while reducing water loss, could "
               "also make it harder for light and gases to reach the "
               "cells beneath it.",
    },
    {
        "id": "ks4-plant-tissues-h23",
        "subtopic_slug": "plant-tissues",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why translocation in phloem is generally slower "
                "than the movement of water in xylem.",
        "options": [
            "Phloem sap actually moves faster than water in xylem, not slower",
            "Sucrose is a much lighter molecule than water is, so phloem sap should in fact be moving the faster of the two by quite some way",
            "Xylem transport is a fast, physical pulling process; sucrose must be actively loaded and unloaded at each end, which takes more time",
            "Phloem tubes are wider than xylem vessels, which always slows any flow down",
        ],
        "correct_index": 2,
        "why": "Xylem transport is a fast, passive pulling process, while "
               "phloem transport requires sucrose to be actively loaded "
               "and unloaded, which takes more time.",
    },
    {
        "id": "ks4-plant-tissues-h24",
        "subtopic_slug": "plant-tissues",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate this claim: 'A plant with severely damaged roots "
                "can still get all the water it needs through its leaves "
                "alone.'",
        "options": [
            "True — leaves absorb more than enough water straight from the humid air around them to supply the whole of the plant",
            "True, since xylem can draw water from the atmosphere just as easily as from soil",
            "False, but only because leaves never lose any water in the first place",
            "False — roots are the main site of water uptake, and root damage generally limits the water available to the whole plant",
        ],
        "correct_index": 3,
        "why": "Roots are the main site of water uptake, so severe root "
               "damage generally limits the water available to the whole "
               "plant, whatever the leaves can do.",
    },
    {
        "id": "ks4-plant-tissues-h25",
        "subtopic_slug": "plant-tissues",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A fungal infection destroys the phloem in a section of a "
                "plant's stem, while leaving the xylem in that section "
                "undamaged. Predict the effect on the parts of the plant "
                "below the infection.",
        "options": [
            "Those parts would be starved of the sugars normally delivered from the leaves, even though water would still arrive",
            "Those parts would be immediately starved of water, since phloem carries water",
            "Those parts would be unaffected, since the sugar they need reaches them by diffusing through the xylem instead",
            "Those parts would begin producing their own phloem instantly to compensate",
        ],
        "correct_index": 0,
        "why": "With the phloem destroyed but the xylem intact, parts "
               "below would still receive water but would be starved of "
               "the sugars normally delivered from the leaves.",
    },
    {
        "id": "ks4-plant-tissues-h26",
        "subtopic_slug": "plant-tissues",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare the effect of destroying a section of xylem in a "
                "stem with the effect of destroying a section of phloem "
                "in the same location.",
        "options": [
            "Both would have an identical effect, since the two tissues carry out the same job",
            "Destroying the xylem would cut off water to parts above it; destroying the phloem would cut off sugar to parts below it",
            "Destroying the xylem would cut off the sugar to the parts above it; destroying the phloem would cut off water below",
            "Neither type of damage would have any effect on the rest of the plant",
        ],
        "correct_index": 1,
        "why": "Destroying the xylem cuts off the water supply to parts "
               "above the damage, while destroying the phloem cuts off "
               "the sugar supply to parts below it.",
    },

    # ══════════════════════════════════════════════════════════════════
    # transpiration · e05-e12, s05-s26, h05-h26
    # ══════════════════════════════════════════════════════════════════
    {
        "id": "ks4-transpiration-e05",
        "subtopic_slug": "transpiration",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State how transpiration helps cool a plant down.",
        "options": [
            "Evaporating water from the leaf surface removes heat",
            "It increases the rate of respiration in every cell",
            "It reflects sunlight away from the leaf surface",
            "It converts heat directly into extra sugar",
        ],
        "correct_index": 0,
        "why": "Evaporation of water from the leaf surface removes heat, "
               "cooling the plant, much like sweating cools an animal.",
    },
    {
        "id": "ks4-transpiration-e06",
        "subtopic_slug": "transpiration",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the direction an air bubble moves in a potometer as "
                "a shoot takes up water.",
        "options": [
            "Away from the shoot",
            "Towards the shoot",
            "It stays in a fixed position at all times",
            "It moves in a random direction each time",
        ],
        "correct_index": 1,
        "why": "As the shoot takes up water, the air bubble moves towards "
               "it along the capillary tube.",
    },
    {
        "id": "ks4-transpiration-e07",
        "subtopic_slug": "transpiration",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the effect of bright light on the width of the "
                "stomata's opening.",
        "options": [
            "It closes the stomata completely",
            "It has no effect on the stomata at all",
            "It causes the stomata to open wider",
            "It causes the guard cells to burst",
        ],
        "correct_index": 2,
        "why": "Bright light causes guard cells to open the stomata "
               "wider, letting in more carbon dioxide but also losing more "
               "water vapour.",
    },
    {
        "id": "ks4-transpiration-e08",
        "subtopic_slug": "transpiration",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the effect of high humidity (moist air) on the rate "
                "of transpiration.",
        "options": [
            "It speeds transpiration up considerably",
            "It has no effect on the rate of transpiration at all",
            "It causes stomata to open much wider than normal",
            "It slows transpiration down",
        ],
        "correct_index": 3,
        "why": "High humidity reduces the concentration gradient for water "
               "vapour, slowing transpiration down.",
    },
    {
        "id": "ks4-transpiration-e09",
        "subtopic_slug": "transpiration",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State a typical unit used to measure the rate of water "
                "uptake in a potometer.",
        "options": [
            "mm per minute",
            "degrees per second",
            "newtons per metre",
            "joules per kilogram",
        ],
        "correct_index": 0,
        "why": "The rate of water uptake in a potometer is typically "
               "measured in millimetres per minute.",
    },
    {
        "id": "ks4-transpiration-e10",
        "subtopic_slug": "transpiration",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the general effect of a shoot having more leaves on "
                "its rate of water uptake.",
        "options": [
            "It has no effect on the rate of water uptake",
            "The rate of water uptake generally increases",
            "The rate of water uptake always falls to zero",
            "Water uptake stops completely once more than one leaf is present",
        ],
        "correct_index": 1,
        "why": "More leaves generally means more stomata and a greater "
               "surface area for water loss, so uptake generally "
               "increases.",
    },
    {
        "id": "ks4-transpiration-e11",
        "subtopic_slug": "transpiration",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the effect on water uptake of removing every leaf "
                "from a shoot in a potometer.",
        "options": [
            "Water uptake rises sharply",
            "Water uptake stays exactly the same",
            "Water uptake falls close to zero",
            "Water uptake becomes impossible to affect in any way",
        ],
        "correct_index": 2,
        "why": "With no leaves and so no stomata, there is almost nothing "
               "to drive transpiration, so water uptake falls close to "
               "zero.",
    },
    {
        "id": "ks4-transpiration-e12",
        "subtopic_slug": "transpiration",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State why a potometer experiment uses a leafy shoot rather "
                "than a bare stick with no leaves.",
        "options": [
            "A bare stick would take up water faster than a leafy shoot",
            "A bare stick already has a fixed transpiration rate",
            "Leaves have no connection at all to the rate at which a shoot takes up water",
            "The leaves and their stomata are what drives transpiration and water uptake",
        ],
        "correct_index": 3,
        "why": "It is the leaves and their stomata that drive "
               "transpiration, so a leafless stick would show little or "
               "no water uptake.",
    },
    {
        "id": "ks4-transpiration-s05",
        "subtopic_slug": "transpiration",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A potometer records a rate of water uptake of 5 mm per "
                "minute. Calculate the equivalent rate in mm per hour.",
        "options": [
            "300 mm/hour",
            "60 mm/hour",
            "5 mm/hour",
            "3000 mm/hour",
        ],
        "correct_index": 0,
        "why": "There are 60 minutes in an hour, so 5 mm/min × 60 = "
               "300 mm/hour.",
    },
    {
        "id": "ks4-transpiration-s06",
        "subtopic_slug": "transpiration",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "In a potometer, the rate of water uptake is measured as "
                "6 mm/min. Calculate how far the bubble would travel in "
                "9 minutes at that steady rate.",
        "options": [
            "15 mm",
            "54 mm",
            "1.5 mm",
            "63 mm",
        ],
        "correct_index": 1,
        "why": "Distance is rate multiplied by time: 6 mm/min × 9 min = "
               "54 mm.",
    },
    {
        "id": "ks4-transpiration-s07",
        "subtopic_slug": "transpiration",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a plant kept under a bright lamp transpires "
                "faster than the same plant kept in dim light.",
        "options": [
            "Bright light heats the water inside the xylem vessels directly, pushing it upward",
            "Bright light makes the leaf's cuticle dissolve temporarily",
            "Bright light causes the stomata to open wider, letting more water vapour escape",
            "Bright light has no real effect on the rate of transpiration",
        ],
        "correct_index": 2,
        "why": "Bright light causes the stomata to open wider, which lets "
               "more water vapour escape and raises the transpiration "
               "rate.",
    },
    {
        "id": "ks4-transpiration-s08",
        "subtopic_slug": "transpiration",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a plant transpires more slowly in a humid "
                "greenhouse than in dry outdoor air.",
        "options": [
            "Humid air makes the stomata close permanently",
            "Humid air increases the concentration gradient that drives water loss from the leaf",
            "Humid air has no effect on the rate of transpiration",
            "Humid air reduces the concentration gradient between the leaf and the surrounding air",
        ],
        "correct_index": 3,
        "why": "Humid air narrows the concentration gradient for water "
               "vapour between the leaf and the surrounding air, slowing "
               "transpiration.",
    },
    {
        "id": "ks4-transpiration-s09",
        "subtopic_slug": "transpiration",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare the transpiration rate of a plant in hot, humid "
                "air with the same plant in hot, dry air.",
        "options": [
            "The plant in hot, dry air transpires faster, since the concentration gradient is steeper",
            "The plant in hot, humid air transpires faster, since heat and humidity add together",
            "Both plants transpire at exactly the same rate, since temperature is identical",
            "Neither plant transpires at all once the air becomes humid",
        ],
        "correct_index": 0,
        "why": "Dry air gives a steeper concentration gradient for water "
               "vapour than humid air, so the plant in dry air transpires "
               "faster despite the identical temperature.",
    },
    {
        "id": "ks4-transpiration-s10",
        "subtopic_slug": "transpiration",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A shoot's total leaf surface area is roughly doubled by "
                "leaving more leaves attached. Predict the effect on its "
                "rate of water uptake.",
        "options": [
            "The rate of water uptake would be expected to fall by roughly half, since each leaf gets less water",
            "The rate of water uptake would be expected to increase, though not necessarily by exactly double",
            "The rate of water uptake would stay completely unaffected",
            "The rate of water uptake would fall to zero immediately",
        ],
        "correct_index": 1,
        "why": "More leaf surface area means more stomata overall, so "
               "uptake would be expected to increase, though not "
               "necessarily in exact proportion.",
    },
    {
        "id": "ks4-transpiration-s11",
        "subtopic_slug": "transpiration",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a plant's rate of transpiration is generally "
                "higher at midday than early in the morning.",
        "options": [
            "Midday is generally both cooler and darker than the early morning, so the rate falls back",
            "Stomata close completely by midday to protect the plant",
            "Midday generally brings higher temperature and brighter light, both of which raise the rate",
            "Transpiration is not affected by the time of day at all",
        ],
        "correct_index": 2,
        "why": "Higher temperature and brighter light at midday both raise "
               "the rate of transpiration compared with early morning.",
    },
    {
        "id": "ks4-transpiration-s12",
        "subtopic_slug": "transpiration",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a plant standing in indirect, cloudy daylight "
                "still transpires, even though light intensity is much "
                "lower than in direct sun.",
        "options": [
            "Transpiration only ever occurs in complete darkness",
            "Cloudy daylight always closes every stoma completely",
            "Cloud cover has no possible effect on the rate of transpiration at any point in the day",
            "Stomata remain at least partly open in daylight, even when it is not direct sunlight",
        ],
        "correct_index": 3,
        "why": "Stomata remain at least partly open in daylight generally, "
               "not only in direct sunlight, so some transpiration "
               "continues.",
    },
    {
        "id": "ks4-transpiration-s13",
        "subtopic_slug": "transpiration",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A bubble moves 24 mm in 2 minutes at 15°C, and 36 mm in "
                "2 minutes at 25°C. Calculate how many times faster the "
                "rate is at 25°C.",
        "options": [
            "2 times faster",
            "0.5 times faster",
            "4 times faster",
            "1.5 times faster",
        ],
        "correct_index": 3,
        "why": "12 mm/min at 15°C and 18 mm/min at 25°C, and "
               "18 ÷ 12 = 1.5.",
    },
    {
        "id": "ks4-transpiration-s14",
        "subtopic_slug": "transpiration",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a hot, windy day produces a much faster "
                "transpiration rate than a hot, still day.",
        "options": [
            "Wind has no effect once temperature is already high",
            "Wind removes the humid air building up around the stomata, keeping the concentration gradient steep even as heat also raises the rate",
            "Wind cools the leaf so much that transpiration nearly stops",
            "Wind forces the stomata to close completely on a hot day",
        ],
        "correct_index": 1,
        "why": "Wind clears the humid air around the stomata, keeping the "
               "gradient steep, while heat also raises the rate — the two "
               "effects combine.",
    },
    {
        "id": "ks4-transpiration-s15",
        "subtopic_slug": "transpiration",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why warming the capillary tube of a potometer "
                "directly, rather than the plant itself, could give a "
                "misleading reading.",
        "options": [
            "It would have no effect on the bubble's movement at all",
            "It would make the plant transpire less, not more",
            "The air inside the tube could expand, pushing the bubble without any real change in water uptake",
            "Warming the tube would immediately stop the bubble moving along the scale altogether",
        ],
        "correct_index": 2,
        "why": "Warming the tube could make the trapped air inside expand, "
               "pushing the bubble without any real change in the "
               "shoot's actual water uptake.",
    },
    {
        "id": "ks4-transpiration-s16",
        "subtopic_slug": "transpiration",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A rapidly growing shoot uses an unusually large amount of "
                "the water it takes up for growth, rather than losing it "
                "as vapour. Explain the effect on how accurately the "
                "potometer reflects its true transpiration rate.",
        "options": [
            "The potometer would still measure the transpiration itself exactly",
            "The potometer would overestimate transpiration, since growth speeds up water loss",
            "The potometer reading would have no relationship to water uptake at all",
            "The potometer would overestimate transpiration, since some of the water taken up is used for growth rather than transpired",
        ],
        "correct_index": 3,
        "why": "Since a potometer measures total water uptake, water used "
               "for growth rather than transpired makes the reading "
               "overestimate the true transpiration rate.",
    },
    {
        "id": "ks4-transpiration-s17",
        "subtopic_slug": "transpiration",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A shoot has had its leaves' waxy cuticle artificially "
                "removed before being placed in a potometer. Predict the "
                "effect on the potometer reading.",
        "options": [
            "The reading would show a much faster rate of water uptake than normal",
            "The reading would show no water uptake at all",
            "The reading would be completely unaffected by this change",
            "The reading would show the water moving backwards along the tube instead",
        ],
        "correct_index": 0,
        "why": "Without its waterproof cuticle, the leaf surface loses "
               "water far more freely, so the potometer reading would "
               "show a much faster rate.",
    },
    {
        "id": "ks4-transpiration-s18",
        "subtopic_slug": "transpiration",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Two identical shoots are placed in potometers, one in dry "
                "air and one in humid air, for the same length of time. "
                "Compare the distance each bubble is likely to travel.",
        "options": [
            "The bubble in humid air travels further, since a higher humidity always speeds transpiration up in any plant",
            "The bubble in dry air travels further, since the steeper gradient drives faster water loss and uptake",
            "Both bubbles travel exactly the same distance, regardless of humidity",
            "Neither bubble moves at all once humidity changes",
        ],
        "correct_index": 1,
        "why": "Dry air gives a steeper concentration gradient, driving "
               "faster water loss and so faster uptake, so its bubble "
               "travels further.",
    },
    {
        "id": "ks4-transpiration-s19",
        "subtopic_slug": "transpiration",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain what ultimately provides the pulling force that "
                "draws water up through the xylem during transpiration.",
        "options": [
            "The pumping action of the root hair cells",
            "Pressure created by the leaves photosynthesising",
            "Evaporation of water from the leaf cells into the air spaces and out through the stomata",
            "A pumping structure at the base of the stem that pushes the water up towards the leaves",
        ],
        "correct_index": 2,
        "why": "Evaporation of water from the leaf cells creates the "
               "pulling force that draws more water up through the xylem "
               "to replace it.",
    },
    {
        "id": "ks4-transpiration-s20",
        "subtopic_slug": "transpiration",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Half of the leaves on a shoot have their stomata sealed "
                "with petroleum jelly; the other half are left untreated. "
                "Predict the effect on the potometer reading compared "
                "with an identical, fully untreated shoot.",
        "options": [
            "The reading would be identical to that of the untreated shoot, since only some of the leaves were sealed",
            "The reading would show a faster rate than the untreated shoot",
            "The reading would show water flowing in the opposite direction",
            "The reading would show a reduced rate, somewhere between a fully sealed and a fully untreated shoot",
        ],
        "correct_index": 3,
        "why": "With only half the leaves able to transpire normally, the "
               "reading would fall somewhere between a fully sealed and a "
               "fully untreated shoot.",
    },
    {
        "id": "ks4-transpiration-s21",
        "subtopic_slug": "transpiration",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Two identical shoots, from the same plant and under the "
                "same conditions, are placed in potometers — one with "
                "twice as many leaves as the other. Compare their bubble "
                "movement over the same time.",
        "options": [
            "The shoot with more leaves generally shows greater bubble movement, from its larger total stomatal surface",
            "The shoot with fewer leaves always shows greater bubble movement",
            "Both shoots show exactly identical bubble movement, whatever number of leaves each one of them carries",
            "Neither shoot shows any bubble movement without direct sunlight present",
        ],
        "correct_index": 0,
        "why": "More leaves means a larger total stomatal surface, so the "
               "shoot with more leaves generally shows greater bubble "
               "movement.",
    },
    {
        "id": "ks4-transpiration-s22",
        "subtopic_slug": "transpiration",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "In a potometer, the rate of water uptake is measured as "
                "30 mm/min. Calculate how long the bubble would take to "
                "travel 45 mm at that steady rate.",
        "options": [
            "15 minutes",
            "1.5 minutes",
            "0.67 minutes",
            "75 minutes",
        ],
        "correct_index": 1,
        "why": "Time is distance divided by rate: 45 mm ÷ 30 mm/min = "
               "1.5 minutes.",
    },
    {
        "id": "ks4-transpiration-s23",
        "subtopic_slug": "transpiration",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why the same potted plant, left in the same spot "
                "in a garden, can show a very different transpiration "
                "rate from one day to the next.",
        "options": [
            "Transpiration rate never actually changes for a plant left in the same spot",
            "Only the age of the plant can ever change its transpiration rate",
            "Day-to-day changes in temperature, light, humidity and wind all affect the rate",
            "The plant's genes rewrite themselves daily to fix the rate",
        ],
        "correct_index": 2,
        "why": "Temperature, light, humidity and wind all vary from day to "
               "day and each affects transpiration rate.",
    },
    {
        "id": "ks4-transpiration-s24",
        "subtopic_slug": "transpiration",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "One leaf out of many on a shoot is covered to block light, "
                "while the rest remain in full light. Predict the effect "
                "on the shoot's overall potometer reading.",
        "options": [
            "The reading falls right to zero, since even one shaded leaf stops the whole shoot transpiring",
            "The reading rises sharply, since shading one leaf speeds up the others",
            "The reading is completely unaffected, since only leaves absorb water, not stems",
            "The reading falls only slightly, since most of the shoot's leaves are still transpiring normally",
        ],
        "correct_index": 3,
        "why": "With only one leaf out of many affected, the overall "
               "reading falls only slightly, since most leaves are still "
               "transpiring normally.",
    },
    {
        "id": "ks4-transpiration-s25",
        "subtopic_slug": "transpiration",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A shoot is already wilting slightly before being placed in "
                "a potometer. Predict the effect on its initial reading, "
                "compared with a fully turgid shoot under identical "
                "conditions.",
        "options": [
            "The wilting shoot's stomata are likely already partly closed, giving a lower initial reading",
            "The wilting shoot will always show a faster reading than a fully turgid one does under the same conditions",
            "Wilting has no effect on stomata or on the potometer reading",
            "The potometer cannot be used at all on a wilting shoot",
        ],
        "correct_index": 0,
        "why": "A wilting shoot's stomata are likely already partly "
               "closed to conserve water, which would give a lower "
               "initial reading than a fully turgid shoot.",
    },
    {
        "id": "ks4-transpiration-s26",
        "subtopic_slug": "transpiration",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why the air bubble in a potometer is reset to the "
                "start of the scale before starting a new timed reading.",
        "options": [
            "Resetting it changes the leaf's rate of transpiration",
            "Resetting it means the full length of the scale is available for the next timed measurement",
            "Resetting the bubble has no real purpose during the experiment",
            "Resetting the bubble permanently increases the total leaf area that the shoot itself carries",
        ],
        "correct_index": 1,
        "why": "Resetting the bubble to the start means the full length "
               "of the scale is available to measure the next timed "
               "reading.",
    },
    {
        "id": "ks4-transpiration-h05",
        "subtopic_slug": "transpiration",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "In a potometer, the rate of water uptake rises from "
                "20 mm/min in still air to 35 mm/min once a fan is "
                "switched on. Calculate the percentage increase in the "
                "rate.",
        "options": [
            "75%",
            "15%",
            "175%",
            "57%",
        ],
        "correct_index": 0,
        "why": "Percentage increase = (increase ÷ original) × 100 = "
               "(15 ÷ 20) × 100 = 75%.",
    },
    {
        "id": "ks4-transpiration-h06",
        "subtopic_slug": "transpiration",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate this claim: 'Since high humidity slows "
                "transpiration, a plant kept at 100% humidity will never "
                "transpire at all.'",
        "options": [
            "True — 100% humidity always reduces the concentration gradient to exactly zero, everywhere around every leaf, so nothing at all can evaporate",
            "Debatable — if the air right at the leaf surface is fully saturated the gradient may approach zero, but this is an extreme, rarely achieved case",
            "False, since humidity actually has no effect on the concentration gradient",
            "True, but only because leaves stop producing water vapour at high humidity",
        ],
        "correct_index": 1,
        "why": "A gradient approaching zero at full saturation is an "
               "extreme, rarely fully achieved case, so a flat 'never at "
               "all' claim is too strong.",
    },
    {
        "id": "ks4-transpiration-h07",
        "subtopic_slug": "transpiration",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Two readings are taken from the same shoot under identical "
                "temperature and humidity: one in bright light, one with "
                "added wind but dimmer light. Suggest which reading is "
                "likely to show the faster rate, and why.",
        "options": [
            "The bright-light reading, since light intensity alone always outweighs wind as a factor",
            "Neither reading would differ, since temperature and humidity are unchanged",
            "It depends on which effect is stronger under those specific conditions — both light and wind can raise the rate independently",
            "The windy, dim reading, since wind always has a far bigger effect on the rate than light does",
        ],
        "correct_index": 2,
        "why": "Both light and wind can raise the rate independently, so "
               "which reading is faster depends on how strong each "
               "specific effect is, not a fixed rule.",
    },
    {
        "id": "ks4-transpiration-h08",
        "subtopic_slug": "transpiration",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A gardener assumes that a fast bubble movement in a "
                "potometer always means a healthy, thriving plant. "
                "Evaluate this assumption.",
        "options": [
            "True — a faster rate always indicates a healthier plant in every case",
            "True, since only a completely healthy plant is capable of transpiring at all",
            "False, since a wilting or stressed plant always transpires a good deal more than a fully healthy one ever does",
            "Not necessarily — a fast rate could also result from hot, dry or windy conditions, regardless of the plant's health",
        ],
        "correct_index": 3,
        "why": "A fast rate can simply reflect hot, dry or windy "
               "conditions rather than the plant's health, so it is not a "
               "reliable indicator on its own.",
    },
    {
        "id": "ks4-transpiration-h09",
        "subtopic_slug": "transpiration",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate this claim: 'Since both wind and low humidity "
                "increase transpiration by steepening the concentration "
                "gradient, using both together must always exactly "
                "double the rate compared with either alone.'",
        "options": [
            "Not necessarily — the two effects both act on the same gradient, so their combined effect need not simply add up to double",
            "True — every combination of two rate-increasing factors always doubles the rate exactly, whatever the two factors happen to be",
            "False, since wind and humidity can never act on a plant at the same time",
            "True, but only because wind and humidity are actually the same factor",
        ],
        "correct_index": 0,
        "why": "Since wind and low humidity both act on the same "
               "underlying gradient, their combined effect need not add "
               "up to a simple, exact doubling.",
    },
    {
        "id": "ks4-transpiration-h10",
        "subtopic_slug": "transpiration",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A potometer has a small air leak at one of its joints. "
                "Predict the effect this would have on the recorded rate "
                "of water uptake, compared with a correctly sealed "
                "potometer.",
        "options": [
            "The reading would be identical to a correctly sealed potometer's, since an air leak of this kind never affects the reading a potometer gives at all",
            "The reading would likely be inaccurate, since air entering at the leak could affect the bubble's movement independently of the shoot's real uptake",
            "The reading would always be higher than the true rate, without exception",
            "The leak would have no effect unless the whole potometer were submerged in water",
        ],
        "correct_index": 1,
        "why": "Air entering at a leak could move the bubble independently "
               "of the shoot's real water uptake, making the reading "
               "unreliable.",
    },
    {
        "id": "ks4-transpiration-h11",
        "subtopic_slug": "transpiration",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "One shoot has a larger total leaf area than a second shoot, "
                "but a lower density of stomata per unit area. Suggest how "
                "their overall rates of water uptake might compare.",
        "options": [
            "The larger shoot will always transpire faster than the smaller one, whatever the density of stomata on each of their leaves happens to be in each case",
            "The smaller shoot will always transpire faster, regardless of its leaf area",
            "The outcome depends on both factors together — a larger area with fewer stomata per unit area could match, exceed, or fall behind a smaller, denser one",
            "Stomatal density has no bearing on the total rate of transpiration",
        ],
        "correct_index": 2,
        "why": "Both leaf area and stomatal density affect the total "
               "number of stomata, so the outcome depends on how the two "
               "factors combine, not on either alone.",
    },
    {
        "id": "ks4-transpiration-h12",
        "subtopic_slug": "transpiration",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A shoot's temperature is raised enough to double its "
                "transpiration rate, and at the same time its leaf area "
                "is also doubled by leaving extra leaves attached. "
                "Predict the combined effect on its overall rate of water "
                "loss, compared with the original shoot.",
        "options": [
            "The rate would stay exactly the same as the original shoot",
            "The rate would only double, since only one single factor at a time can ever act on a shoot in a potometer",
            "The rate would actually fall, since two changes at once always cancel out",
            "The rate would increase substantially more than from either change alone, since both push the rate up together",
        ],
        "correct_index": 3,
        "why": "Since both changes independently push the rate up, "
               "applying them together increases the rate substantially "
               "more than either change alone would.",
    },
    {
        "id": "ks4-transpiration-h13",
        "subtopic_slug": "transpiration",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate this claim: 'Since a potometer measures water "
                "uptake rather than transpiration itself, its readings "
                "are worthless as an indicator of transpiration.'",
        "options": [
            "False — uptake closely tracks transpiration in most cases, even though a little of the water taken up is used elsewhere",
            "True — uptake and transpiration have no relationship to one another at all",
            "True, since a potometer cannot detect any change in water movement",
            "False, but only because water uptake and transpiration are in fact exactly identical to one another at all times",
        ],
        "correct_index": 0,
        "why": "Uptake closely tracks transpiration in most cases, even "
               "though a little of the water is used elsewhere, so the "
               "readings are still a useful indicator.",
    },
    {
        "id": "ks4-transpiration-h14",
        "subtopic_slug": "transpiration",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Predict how a continuous potometer reading, taken on the "
                "same shoot from midday until midnight, would be expected "
                "to change over that period.",
        "options": [
            "The rate would be expected to rise steadily throughout the period, with no fall at any point",
            "The rate would be expected to fall as light and temperature drop towards evening and night",
            "The rate would stay completely constant throughout, regardless of the time of day",
            "The rate would rise sharply the moment it becomes dark",
        ],
        "correct_index": 1,
        "why": "As light and temperature fall towards evening and night, "
               "the transpiration rate would be expected to fall too.",
    },
    {
        "id": "ks4-transpiration-h15",
        "subtopic_slug": "transpiration",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain two separate reasons why the volume of water a "
                "potometer records as 'taken up' can be slightly more "
                "than the volume actually lost through transpiration.",
        "options": [
            "All of the water taken up by the shoot is always transpired away, so there is no possible difference at all between the two figures recorded",
            "The difference only ever occurs because the potometer itself leaks water",
            "Some of the water taken up is used directly in photosynthesis, and some supports growth or keeps cells turgid, rather than being transpired",
            "The difference occurs only because temperature affects the accuracy of the scale",
        ],
        "correct_index": 2,
        "why": "Some of the water taken up is used directly in "
               "photosynthesis, and some supports growth or keeps cells "
               "turgid, rather than all of it being transpired.",
    },
    {
        "id": "ks4-transpiration-h16",
        "subtopic_slug": "transpiration",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate this claim: 'Increasing wind speed always "
                "increases the rate of transpiration, without any "
                "limit.'",
        "options": [
            "Transpiration rate rises in direct, unlimited proportion to the speed of the wind",
            "Wind is the only one of the four factors that is capable of affecting the transpiration rate at all",
            "Wind lowers the rate, because it cools the leaf faster than it clears the humid air",
            "Once wind has already removed the humid air around a stoma, more wind may add little further benefit",
        ],
        "correct_index": 3,
        "why": "Once wind has already cleared the humid air around a "
               "stoma, further wind may add little additional benefit, so "
               "the effect is not unlimited.",
    },
    {
        "id": "ks4-transpiration-h17",
        "subtopic_slug": "transpiration",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A shoot's potometer reading is taken in a cool, humid "
                "room, then the whole setup is moved partway through to a "
                "hot, dry, windy spot. Predict what happens to the "
                "bubble's speed after the move.",
        "options": [
            "The bubble speeds up, since temperature, humidity and wind have all changed in ways that raise the rate",
            "The bubble slows down, since moving a plant at all always reduces the rate at which it can transpire",
            "The bubble stops completely, since moving the apparatus breaks the water column",
            "The bubble's speed is completely unaffected by any change in these conditions",
        ],
        "correct_index": 0,
        "why": "Higher temperature, lower humidity and added wind all "
               "raise the transpiration rate, so the bubble would be "
               "expected to speed up after the move.",
    },
    {
        "id": "ks4-transpiration-h18",
        "subtopic_slug": "transpiration",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate this claim: 'A bare stick with no leaves would "
                "work just as well as a leafy shoot in a potometer for "
                "measuring transpiration.'",
        "options": [
            "True — the type of shoot used makes no difference at all to the measurement that is being taken here",
            "False — with no leaves, there are no stomata, so there would be little or no transpiration to measure",
            "True, since transpiration mainly happens through the bark of a stem",
            "False, but only because a bare stick cannot physically fit into a potometer",
        ],
        "correct_index": 1,
        "why": "Without leaves there are no stomata, so there would be "
               "little or no transpiration for a potometer to measure.",
    },
    {
        "id": "ks4-transpiration-h19",
        "subtopic_slug": "transpiration",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A potometer reading rises through the morning and then "
                "levels off around midday, staying steady into the "
                "afternoon even as the sun stays out. Suggest an "
                "explanation for the reading levelling off rather than "
                "continuing to rise.",
        "options": [
            "The plant has run out of water completely by midday",
            "The stomata physically disappear from the leaf altogether once each one of them has been open for some hours",
            "Conditions such as temperature and light may have stopped increasing further once they reached their midday peak",
            "Potometers are only able to record a rising reading, never a steady one",
        ],
        "correct_index": 2,
        "why": "If temperature and light stop rising once they reach "
               "their midday peak, the transpiration rate they drive "
               "would also level off rather than keep rising.",
    },
    {
        "id": "ks4-transpiration-h20",
        "subtopic_slug": "transpiration",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A single potometer trial, using one shoot, shows "
                "transpiration rate doubling when wind is added. Evaluate "
                "whether this one result proves the effect for the whole "
                "plant species.",
        "options": [
            "Yes — a single trial on one shoot is always sufficient to prove a rule holding good for an entire plant species",
            "Yes, but only because potometer results are never affected by any other variable",
            "No, since a single shoot can never show any real change in rate at all",
            "Not conclusively — repeating the trial with other shoots would be needed to be confident the pattern holds generally",
        ],
        "correct_index": 3,
        "why": "One trial on one shoot cannot rule out other explanations, "
               "so repeating it with other shoots would be needed before "
               "generalising confidently.",
    },
    {
        "id": "ks4-transpiration-h21",
        "subtopic_slug": "transpiration",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Two different plant species, one with a thick waxy "
                "cuticle and one with a thin cuticle, are tested side by "
                "side in identical potometer conditions. Predict which is "
                "likely to show the faster reading.",
        "options": [
            "The thin-cuticle species, since less waterproofing means faster water loss and uptake",
            "The thick-cuticle species, since a thicker cuticle always speeds up transpiration",
            "Both species would show identical readings, regardless of cuticle thickness",
            "Neither species would show any reading at all under identical conditions",
        ],
        "correct_index": 0,
        "why": "A thinner cuticle offers less protection against water "
               "loss, so the thin-cuticle species would be expected to "
               "show the faster reading.",
    },
    {
        "id": "ks4-transpiration-h22",
        "subtopic_slug": "transpiration",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A potometer reading is being taken as the temperature "
                "suddenly drops sharply partway through the experiment. "
                "Predict the effect on the bubble's speed from that point "
                "onward.",
        "options": [
            "The bubble speeds up further, since a falling temperature always raises the rate of transpiration in a plant",
            "The bubble is likely to slow down, since a lower temperature generally reduces the rate of transpiration",
            "The bubble stops moving in either direction from that point on",
            "Temperature has no real effect on the bubble's speed at any point",
        ],
        "correct_index": 1,
        "why": "A lower temperature generally reduces the transpiration "
               "rate, so the bubble would be expected to slow down.",
    },
    {
        "id": "ks4-transpiration-h23",
        "subtopic_slug": "transpiration",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a potometer experiment, where only one factor "
                "is changed at a time, gives more useful evidence about "
                "transpiration than simply observing a plant outdoors.",
        "options": [
            "Outdoor observation always gives more accurate evidence than any laboratory experiment",
            "A potometer removes water uptake from the measurement entirely, unlike outdoor observation",
            "Changing only one factor at a time lets any change in rate be linked confidently to that one factor, rather than several changing together outdoors",
            "There is no real difference at all between the two approaches in terms of the quality of the evidence that each one of the two of them provides here",
        ],
        "correct_index": 2,
        "why": "Changing only one factor at a time lets a change in rate "
               "be linked confidently to that one factor, unlike outdoors, "
               "where several factors change together.",
    },
    {
        "id": "ks4-transpiration-h24",
        "subtopic_slug": "transpiration",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate this claim: 'Since transpiration carries dissolved "
                "minerals up to the leaves along with the water, an "
                "increased transpiration rate can never be a problem for "
                "the plant.'",
        "options": [
            "True — a faster transpiration rate always benefits the plant in every possible respect",
            "True, since minerals only ever travel through the phloem, never through the xylem",
            "False, but only because transpiration and mineral transport are two completely unconnected processes in a plant",
            "Not necessarily — a very fast rate can also risk excessive water loss and wilting, even while delivering minerals",
        ],
        "correct_index": 3,
        "why": "A very fast transpiration rate can also risk excessive "
               "water loss and wilting, so it is not automatically a "
               "benefit in every respect.",
    },
    {
        "id": "ks4-transpiration-h25",
        "subtopic_slug": "transpiration",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest one aspect of a plant's water loss that a standard "
                "whole-shoot potometer reading cannot reveal.",
        "options": [
            "Which individual leaf, or which surface of a leaf, is losing water fastest",
            "The overall direction the bubble moves along the tube",
            "Whether the bubble is moving at all during the reading",
            "The total distance the bubble has travelled since the reading first began",
        ],
        "correct_index": 0,
        "why": "A whole-shoot reading gives a single combined rate, so it "
               "cannot reveal which individual leaf or leaf surface is "
               "losing water fastest.",
    },
    {
        "id": "ks4-transpiration-h26",
        "subtopic_slug": "transpiration",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student runs one potometer trial with added wind and one "
                "with raised temperature, finds the wind trial gives a "
                "bigger increase, and concludes that wind always affects "
                "transpiration more strongly than temperature does. "
                "Evaluate this conclusion.",
        "options": [
            "Correct — a single comparison of this kind is always enough to generalise the relative strength of any two factors in any plant at all here",
            "Too strong a conclusion — the relative sizes of the two effects could depend on exactly how much the wind or temperature was actually changed",
            "Incorrect — wind is proven to have no effect on transpiration whatsoever",
            "Correct, but only because temperature never has any effect on transpiration at all",
        ],
        "correct_index": 1,
        "why": "The relative sizes of the two effects could depend on "
               "exactly how much each factor was changed, so one "
               "comparison cannot support such a general conclusion.",
    },

    # ══════════════════════════════════════════════════════════════════
    # translocation · e05-e12, s05-s26, h05-h26
    # ══════════════════════════════════════════════════════════════════
    {
        "id": "ks4-translocation-e05",
        "subtopic_slug": "translocation",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Define translocation.",
        "options": [
            "The movement of dissolved sugars through the phloem, from source to sink",
            "The movement of water through the xylem, from roots to leaves",
            "The movement of oxygen out of a leaf through the stomata",
            "The movement of a plant's roots deeper down into the soil as the season goes on",
        ],
        "correct_index": 0,
        "why": "Translocation is the movement of dissolved sugars through "
               "the phloem, from a source to a sink.",
    },
    {
        "id": "ks4-translocation-e06",
        "subtopic_slug": "translocation",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the term for sucrose being moved into the phloem at "
                "the source.",
        "options": [
            "Unloading",
            "Loading",
            "Translocation reversal",
            "Respiration",
        ],
        "correct_index": 1,
        "why": "Loading is the term for sucrose being actively moved into "
               "the phloem at the source.",
    },
    {
        "id": "ks4-translocation-e07",
        "subtopic_slug": "translocation",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the term for sucrose being moved out of the phloem "
                "at the sink.",
        "options": [
            "Loading",
            "Photosynthesis",
            "Unloading",
            "Transpiration",
        ],
        "correct_index": 2,
        "why": "Unloading is the term for sucrose leaving the phloem at "
               "the sink.",
    },
    {
        "id": "ks4-translocation-e08",
        "subtopic_slug": "translocation",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State whether a developing seed acts as a source or a "
                "sink for sugar.",
        "options": [
            "A source, since seeds produce their own sugar",
            "Neither; seeds play no part in translocation",
            "A source, but only once the seed has germinated and started to grow",
            "A sink, since sugar is delivered there for the seed to use and store",
        ],
        "correct_index": 3,
        "why": "A developing seed is a sink, receiving sugar delivered "
               "from the source to use and store.",
    },
    {
        "id": "ks4-translocation-e09",
        "subtopic_slug": "translocation",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State whether a fully grown green leaf in summer acts as a "
                "source or a sink for sugar.",
        "options": [
            "A source, since it makes more sugar by photosynthesis than it uses itself",
            "A sink, since sugar is delivered to it from the roots below all summer",
            "Neither; a leaf has no connection to translocation at any point",
            "A sink, but only while the plant is carrying no fruit at all",
        ],
        "correct_index": 0,
        "why": "A fully grown green leaf in summer makes more sugar than it "
               "needs, so it loads the surplus into the phloem and acts as a "
               "source.",
    },
    {
        "id": "ks4-translocation-e10",
        "subtopic_slug": "translocation",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what happens to sucrose at a sink if it is not "
                "needed immediately.",
        "options": [
            "It is transported back to the source unchanged",
            "It can be converted to starch and stored",
            "It is broken down into water and released as vapour",
            "It is converted directly into cellulose for structural support",
        ],
        "correct_index": 1,
        "why": "Sucrose not needed immediately at a sink can be converted "
               "to starch and stored.",
    },
    {
        "id": "ks4-translocation-e11",
        "subtopic_slug": "translocation",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State whether a plant can have more than one sink at the "
                "same time.",
        "options": [
            "No, a plant only ever has exactly one sink",
            "No, sinks and sources are always the same structure",
            "Yes, a plant can have several sinks at once, such as roots, fruit and growing tips",
            "Yes, but only once the plant has stopped growing entirely and needs no more sugar",
        ],
        "correct_index": 2,
        "why": "A plant can have several sinks at once, such as roots, "
               "fruit and growing tips, all receiving sugar together.",
    },
    {
        "id": "ks4-translocation-e12",
        "subtopic_slug": "translocation",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what is dissolved in the sap that moves through the "
                "phloem during translocation.",
        "options": [
            "Water only, with nothing dissolved in it",
            "Mineral ions only",
            "Oxygen gas",
            "Sugars, mainly sucrose, dissolved in water",
        ],
        "correct_index": 3,
        "why": "Phloem sap is mainly sugars, especially sucrose, dissolved "
               "in water.",
    },
    {
        "id": "ks4-translocation-s05",
        "subtopic_slug": "translocation",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "In summer a potato plant's tuber stores starch; in "
                "spring, before new leaves have grown, that same tuber "
                "supplies sugar to the growing shoot. Explain what this "
                "shows about the tuber's role.",
        "options": [
            "The tuber can act as either a sink or a source, depending on the time of year",
            "The tuber acts as a source in every season of the year, without any exception",
            "The tuber is always a sink, in every season without exception",
            "The tuber has no real connection to translocation at all",
        ],
        "correct_index": 0,
        "why": "The tuber's role changes with the season — a sink while "
               "storing starch, a source when releasing it in spring.",
    },
    {
        "id": "ks4-translocation-s06",
        "subtopic_slug": "translocation",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A fruit tree is producing a large crop of fruit at the "
                "same time as new shoots are trying to grow. Suggest why "
                "the new shoots might grow more slowly than usual.",
        "options": [
            "New shoots always grow fastest when fruit is also developing",
            "The fruit acts as a strong sink, competing with the growing shoots for the available sugar",
            "Fruit only ever forms once all of the shoot growth on the plant has completely finished",
            "Fruit and shoots use two completely separate types of sugar",
        ],
        "correct_index": 1,
        "why": "The fruit acts as a strong sink, competing with the "
               "growing shoots for the sugar available.",
    },
    {
        "id": "ks4-translocation-s07",
        "subtopic_slug": "translocation",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A gardener removes just one leaf from a plant with many "
                "leaves. Compare the likely effect on translocation with "
                "removing every leaf from the same plant.",
        "options": [
            "Removing one leaf stops translocation completely, in exactly the same way that removing every single one of the plant's leaves would do",
            "Removing every leaf has no more effect than removing just one",
            "Removing one leaf has little overall effect, since other leaves keep acting as a source; removing all of them removes the source entirely",
            "Removing leaves, in any amount, has no effect on translocation at all",
        ],
        "correct_index": 2,
        "why": "With many leaves acting as sources, losing just one has "
               "little overall effect; removing every leaf removes the "
               "source entirely.",
    },
    {
        "id": "ks4-translocation-s08",
        "subtopic_slug": "translocation",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A leaf partway up a plant's stem loads sugar into the "
                "phloem. Explain why some of that sugar can travel upward "
                "to a growing tip while some travels downward to the "
                "roots, at the same time.",
        "options": [
            "Sugar can only ever travel in one single direction from any one leaf",
            "The leaf switches between loading sugar upward and loading it downward every few minutes, so each sink is served in turn",
            "The roots and the growing tip are actually the same single sink",
            "Different sinks lie in different directions from that leaf, and phloem can carry sugar towards each of them independently",
        ],
        "correct_index": 3,
        "why": "Since the growing tip and the roots are different sinks "
               "lying in different directions, phloem can carry sugar "
               "towards each independently at the same time.",
    },
    {
        "id": "ks4-translocation-s09",
        "subtopic_slug": "translocation",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare what is happening in the phloem tissue at a "
                "source with what is happening in the phloem tissue at a "
                "sink.",
        "options": [
            "Sucrose is actively loaded in at a source; it is unloaded and used or stored at a sink",
            "Sucrose is unloaded at a source; it is loaded in at a sink",
            "Exactly the same loading process happens at both a source and at a sink in phloem",
            "No sucrose is present in the phloem at a source at any point",
        ],
        "correct_index": 0,
        "why": "Sucrose is actively loaded into the phloem at a source, "
               "then unloaded to be used or stored at a sink.",
    },
    {
        "id": "ks4-translocation-s10",
        "subtopic_slug": "translocation",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a plant's growing tip depends on translocation "
                "to receive sugar.",
        "options": [
            "The growing tip photosynthesises more than enough of its own sugar to meet its needs",
            "The growing tip's cells are dividing rapidly and need a supply of sugar for that process",
            "The growing tip does not actually require any sugar to develop",
            "The growing tip only ever needs water, never sugar",
        ],
        "correct_index": 1,
        "why": "The growing tip's rapidly dividing cells need a steady "
               "supply of sugar, which translocation delivers.",
    },
    {
        "id": "ks4-translocation-s11",
        "subtopic_slug": "translocation",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "All the flowers are removed from a plant before they can "
                "develop into fruit. Suggest the likely effect on sugar "
                "delivery to the plant's roots and growing tips.",
        "options": [
            "Sugar delivery to roots and growing tips would be expected to fall",
            "Sugar delivery would stop completely everywhere in the plant",
            "With one sink removed, more of the available sugar may be delivered to the remaining sinks instead",
            "Removing flowers has no effect on how sugar is distributed in the plant",
        ],
        "correct_index": 2,
        "why": "With one sink removed, more of the available sugar may be "
               "delivered to the remaining sinks instead.",
    },
    {
        "id": "ks4-translocation-s12",
        "subtopic_slug": "translocation",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare the solution carried in phloem during "
                "translocation with the solution carried in xylem.",
        "options": [
            "Both carry exactly the same dissolved substances",
            "Xylem carries dissolved sugars; phloem carries water and dissolved minerals",
            "Neither xylem nor phloem carries any dissolved substance of any kind",
            "Phloem carries dissolved sugars; xylem carries water and dissolved mineral ions",
        ],
        "correct_index": 3,
        "why": "Phloem sap carries dissolved sugars, while xylem sap "
               "carries water and dissolved mineral ions.",
    },
    {
        "id": "ks4-translocation-s13",
        "subtopic_slug": "translocation",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A chemical specifically stops companion cells at the "
                "source from loading any sucrose into the phloem. Predict "
                "the effect on sinks elsewhere in the plant.",
        "options": [
            "Sinks elsewhere would be starved of sugar, since none could be loaded into the phloem to reach them",
            "Sinks would receive even more sugar than usual as a result",
            "Sinks elsewhere would begin producing all of their own sugar by photosynthesis instead of receiving any",
            "This chemical would have no effect on sinks anywhere in the plant",
        ],
        "correct_index": 0,
        "why": "Without sucrose being loaded at the source, no sugar can "
               "reach sinks elsewhere in the plant, starving them.",
    },
    {
        "id": "ks4-translocation-s14",
        "subtopic_slug": "translocation",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain whether translocation itself requires light to "
                "take place.",
        "options": [
            "Yes, translocation only ever happens during the day in bright light",
            "No — translocation can continue in the dark, as long as sugar made earlier is still available to move",
            "Yes, since light is what actively loads sucrose into the phloem",
            "No, because translocation and photosynthesis are in fact one and the same process within a plant",
        ],
        "correct_index": 1,
        "why": "Translocation can continue in the dark, moving sugar made "
               "earlier, since it is a separate process from "
               "photosynthesis itself.",
    },
    {
        "id": "ks4-translocation-s15",
        "subtopic_slug": "translocation",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A source leaf sits close to one growing tip and far from "
                "a second growing tip. Suggest which tip is more likely "
                "to receive sugar more readily when overall sugar supply "
                "is limited.",
        "options": [
            "The nearer tip, other things being equal, since sugar has a shorter distance to travel to reach it",
            "The farther tip, since a greater distance always increases how much sugar any one sink receives",
            "Both tips always receive exactly identical amounts, regardless of distance",
            "Neither tip can ever receive any sugar from that leaf",
        ],
        "correct_index": 0,
        "why": "Other things being equal, a nearer sink has a shorter "
               "distance for sugar to travel, so it is more likely to "
               "receive sugar more readily under limited supply.",
    },
    {
        "id": "ks4-translocation-s16",
        "subtopic_slug": "translocation",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A cell is respiring using sugar delivered by the phloem, "
                "without storing any of it. Determine whether this cell "
                "counts as a sink.",
        "options": [
            "No, because storing the sugar away is the only thing that defines a sink at all here",
            "No, since only leaves can ever act as a sink",
            "It cannot be determined without knowing the cell's exact location",
            "Yes — a sink is any place sugar is used OR stored, and using it in respiration counts",
        ],
        "correct_index": 3,
        "why": "A sink is defined as anywhere sugar is used or stored, so "
               "using it for respiration counts, even without any "
               "storage.",
    },
    {
        "id": "ks4-translocation-s17",
        "subtopic_slug": "translocation",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A sudden cold spell stops photosynthesis in a plant's "
                "leaves for several days. Predict the effect on sinks "
                "that rely only on the current day's sugar supply, rather "
                "than on stored reserves.",
        "options": [
            "Those sinks would receive little or no sugar until photosynthesis resumes",
            "Those sinks would receive more sugar than usual during the cold spell",
            "Cold weather has no effect on translocation or on any sink",
            "Those sinks would begin making their own sugar by respiration instead",
        ],
        "correct_index": 0,
        "why": "With photosynthesis stopped and no reserves to draw on, "
               "those sinks would receive little or no sugar until it "
               "resumes.",
    },
    {
        "id": "ks4-translocation-s18",
        "subtopic_slug": "translocation",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the general definition of a 'source' in "
                "translocation, beyond just 'the leaves'.",
        "options": [
            "Any part of a plant that only ever stores sugar and never releases it",
            "Any part of a plant where sugar is made or released into the phloem",
            "Any part of a plant that carries out photosynthesis, and nothing else",
            "Only the very tip of a growing root can ever act as a source",
        ],
        "correct_index": 1,
        "why": "A source is any part of a plant where sugar is made or "
               "released into the phloem, whether that is a leaf or a "
               "storage organ.",
    },
    {
        "id": "ks4-translocation-s19",
        "subtopic_slug": "translocation",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A seed stores sugar as it develops on the parent plant, "
                "then releases that stored sugar to fuel the growth of a "
                "new seedling once it germinates. Explain what this shows "
                "about the seed's role over time.",
        "options": [
            "The seed acts only as a sink throughout its entire existence",
            "The seed acts only as a source throughout its entire existence",
            "The seed's role changes from sink, while developing, to source, once it germinates",
            "The seed plays no role in translocation at any point in the whole of its life",
        ],
        "correct_index": 2,
        "why": "The seed is a sink while developing and storing sugar, then "
               "becomes a source once it germinates and releases that "
               "sugar.",
    },
    {
        "id": "ks4-translocation-s20",
        "subtopic_slug": "translocation",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student assumes that, because phloem can carry sugar in "
                "either direction, sugar moves randomly and "
                "unpredictably around a plant. Explain why this is not "
                "the case.",
        "options": [
            "Sugar movement is genuinely completely random, with no predictable pattern at all",
            "Sugar only ever moves in a single, permanently fixed direction throughout the plant's life",
            "Phloem itself decides the direction randomly, independent of where sugar is made or needed",
            "Direction is set by the position of sources and sinks relative to one another, not by chance",
        ],
        "correct_index": 3,
        "why": "Direction is determined by where sources and sinks are "
               "relative to one another, not by chance, even though "
               "phloem itself has no fixed direction.",
    },
    {
        "id": "ks4-translocation-s21",
        "subtopic_slug": "translocation",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest what is likely to happen to sugar made by a "
                "plant's leaves if, temporarily, none of its usual sinks "
                "need any additional sugar.",
        "options": [
            "The sugar is likely to be stored somewhere, such as converted to starch, rather than translocated away for immediate use",
            "The sugar is instantly destroyed by the plant if no sink needs it",
            "The leaves immediately stop photosynthesising altogether whenever no sink is available to take the sugar they would make",
            "The sugar leaks out of the plant into the surrounding soil",
        ],
        "correct_index": 0,
        "why": "With no sink needing it immediately, sugar is likely to be "
               "stored, for example as starch, rather than lost.",
    },
    {
        "id": "ks4-translocation-s22",
        "subtopic_slug": "translocation",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A plant is grown in permanently low light, producing far "
                "less sugar than normal. Suggest the likely effect on how "
                "well multiple sinks, such as growing tips and developing "
                "fruit, can all be supplied at once.",
        "options": [
            "Every sink would still be supplied fully and equally, however little sugar the leaves are actually able to make",
            "With less sugar overall available, competition between sinks for the limited supply would be expected to increase",
            "Low light has no effect on translocation, only on photosynthesis",
            "The plant would immediately stop forming any sinks at all",
        ],
        "correct_index": 1,
        "why": "With less sugar overall available, competition between "
               "sinks for the limited supply would be expected to "
               "increase.",
    },
    {
        "id": "ks4-translocation-s23",
        "subtopic_slug": "translocation",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "State which step of translocation is described as actively "
                "using energy supplied by companion cells.",
        "options": [
            "Both loading and unloading equally",
            "Neither step uses energy of any kind",
            "Loading sucrose into the phloem at the source",
            "Only the movement of the phloem sap itself along the tube",
        ],
        "correct_index": 2,
        "why": "Loading sucrose into the phloem at the source is the step "
               "described as actively using energy from companion cells.",
    },
    {
        "id": "ks4-translocation-s24",
        "subtopic_slug": "translocation",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare a heavily fruiting plant with an otherwise "
                "identical plant that has produced no fruit that year, in "
                "terms of where their leaves' sugar output is likely to "
                "end up.",
        "options": [
            "Both plants send all of their sugar to exactly the same places within the plant, whether or not either one is carrying any fruit at the time",
            "The fruiting plant stores far more of its sugar than the non-fruiting plant does",
            "Neither plant's sugar goes to any sink at all without fruit present",
            "The fruiting plant sends much of its sugar to the fruit itself; the non-fruiting plant instead sends more towards growth and storage elsewhere",
        ],
        "correct_index": 3,
        "why": "The fruiting plant's fruit acts as a strong sink for its "
               "sugar, while the non-fruiting plant sends more of its "
               "sugar towards growth and storage instead.",
    },
    {
        "id": "ks4-translocation-s25",
        "subtopic_slug": "translocation",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the two general things sucrose can be used for once "
                "it is unloaded at a sink.",
        "options": [
            "Respiration for energy, or storage as starch",
            "Photosynthesis, or being reloaded straight back into the xylem",
            "Producing chlorophyll, or being expelled as a waste gas",
            "Making new DNA exclusively, with no other possible use",
        ],
        "correct_index": 0,
        "why": "Sucrose unloaded at a sink is either used in respiration "
               "for energy or converted to starch and stored.",
    },
    {
        "id": "ks4-translocation-s26",
        "subtopic_slug": "translocation",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A mutation stops a plant converting sucrose into starch "
                "for storage in any of its sinks. Predict the effect on "
                "that plant's growth early in spring, before its leaves "
                "have fully developed.",
        "options": [
            "Growth would be completely unaffected, since it is only the autumn growth that relies at all on the plant's own stored starch",
            "Early spring growth would likely suffer, since there would be no stored reserves to draw on before new leaves can photosynthesise",
            "The plant would grow more strongly in spring than a normal plant would",
            "This mutation would only ever affect the plant's flowers, nothing else",
        ],
        "correct_index": 1,
        "why": "With no stored starch reserves, early spring growth would "
               "likely suffer before new leaves can photosynthesise "
               "enough sugar of their own.",
    },
    {
        "id": "ks4-translocation-h05",
        "subtopic_slug": "translocation",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate this claim: 'A single plant structure can never "
                "act as both a source and a sink, even at different "
                "times.'",
        "options": [
            "False — the same structure, such as a storage organ, can switch roles at different times of year",
            "True — a structure that is permanently fixed as a source can never afterwards become a sink",
            "True, since sources and sinks are two completely separate types of plant",
            "False, but only because sources and sinks are actually the same thing",
        ],
        "correct_index": 0,
        "why": "A storage organ such as a tuber can switch roles at "
               "different times of year, acting as a sink then later as "
               "a source.",
    },
    {
        "id": "ks4-translocation-h06",
        "subtopic_slug": "translocation",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare a potato tuber and a germinating seed, in terms "
                "of how each one's role in translocation changes over "
                "time.",
        "options": [
            "Neither one ever changes role; both stay a sink permanently",
            "Both switch from being a sink, while sugar is stored, to being a source, when that sugar is later released",
            "The tuber is always a source and the seed is always a sink, with neither one of them ever switching role",
            "Both switch from source to sink, and never switch back to source again",
        ],
        "correct_index": 1,
        "why": "Both a tuber and a seed act as a sink while storing sugar, "
               "then switch to being a source when that sugar is later "
               "released.",
    },
    {
        "id": "ks4-translocation-h07",
        "subtopic_slug": "translocation",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A plant has one small developing fruit and an extensive "
                "root system, both acting as sinks at the same time. "
                "Suggest how the total sugar delivered to each might "
                "compare, and why this is hard to predict from size "
                "alone.",
        "options": [
            "The fruit will always receive more in total, since fruit is always the strongest possible sink",
            "The roots will always receive more in total, since they are physically larger overall",
            "It depends on the relative strength of demand from each sink, not simply on their physical size",
            "Both will always receive an exactly identical total amount of sugar",
        ],
        "correct_index": 2,
        "why": "How much sugar each sink receives depends on the relative "
               "strength of its demand, not simply on its physical size.",
    },
    {
        "id": "ks4-translocation-h08",
        "subtopic_slug": "translocation",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate this claim: 'Since leaves make sugar "
                "continuously, translocation must always be delivering "
                "more sugar to sinks than the plant actually needs.'",
        "options": [
            "True — sugar production and sink demand can never match one another at any point in the whole of a plant's lifetime here",
            "True, since sinks can never store any excess sugar that arrives",
            "False, but only because leaves never actually make sugar continuously",
            "Not necessarily — sinks can store surplus sugar as starch, and demand can rise and fall to roughly match supply over time",
        ],
        "correct_index": 3,
        "why": "Surplus sugar can be stored as starch, and sink demand "
               "varies over time, so supply and demand can roughly match "
               "rather than always producing an excess.",
    },
    {
        "id": "ks4-translocation-h09",
        "subtopic_slug": "translocation",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A plant is kept in complete darkness for several days. "
                "Compare the likely effect on translocation with the "
                "likely effect on transpiration over that time.",
        "options": [
            "Translocation would be expected to slow as sugar reserves run low; transpiration could continue if stomata remain even partly open",
            "Both processes would stop instantly and completely, the moment darkness began",
            "Translocation would speed up in the dark, while transpiration would stop completely the very moment that the light was taken away",
            "Neither process is affected by light at all, in any way",
        ],
        "correct_index": 0,
        "why": "As sugar reserves run low in the dark, translocation would "
               "be expected to slow, while transpiration could continue "
               "if stomata remain even partly open.",
    },
    {
        "id": "ks4-translocation-h10",
        "subtopic_slug": "translocation",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate this claim: 'Since translocation can move sugar "
                "downward to the roots, gravity must be the force "
                "responsible for that downward movement.'",
        "options": [
            "True — gravity is the sole force driving all of translocation, which is why sugar reaches the roots of a plant at all and never runs the other way up it",
            "False — translocation depends on active loading and unloading at each end, which can move sugar in any direction relative to gravity, not on gravity itself",
            "True, but only because sugar is much denser than the surrounding phloem sap",
            "False, but only because sugar never actually moves downward in a real plant",
        ],
        "correct_index": 1,
        "why": "Translocation depends on active loading and unloading, "
               "which can move sugar in any direction relative to "
               "gravity, so gravity is not the driving force.",
    },
    {
        "id": "ks4-translocation-h11",
        "subtopic_slug": "translocation",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Two mutant plants exist: one whose companion cells can "
                "load sucrose but whose sinks cannot unload it, and one "
                "whose companion cells cannot load sucrose at all. "
                "Compare the likely outcome for each plant.",
        "options": [
            "Both mutants would translocate their sugar completely normally, since only one of the two steps is affected in each of the two cases here",
            "Neither mutant would show any difference in growth, health or survival at all",
            "The first mutant would likely build up sugar trapped in the phloem with none reaching sinks; the second would have no sugar to move at all",
            "The first mutant would translocate too much sugar; the second would translocate exactly double the normal amount",
        ],
        "correct_index": 2,
        "why": "Without unloading, sugar would build up trapped in the "
               "phloem of the first mutant; without loading, the second "
               "mutant would have no sugar to move at all.",
    },
    {
        "id": "ks4-translocation-h12",
        "subtopic_slug": "translocation",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A fruit tree is bred to produce an unusually large number "
                "of fruit in a single year. Suggest the likely effect on "
                "the growth of its roots and shoots that same year.",
        "options": [
            "Root and shoot growth would be expected to increase substantially, since more fruit always means more sugar overall",
            "Root and shoot growth would be completely unaffected by how much fruit is produced",
            "The tree would simply produce even more sugar to cover every sink's needs at once",
            "Root and shoot growth may be reduced, since the unusually large fruit sink competes strongly for the available sugar",
        ],
        "correct_index": 3,
        "why": "The unusually large fruit sink competes strongly for the "
               "available sugar, so root and shoot growth may be reduced "
               "as a result.",
    },
    {
        "id": "ks4-translocation-h13",
        "subtopic_slug": "translocation",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate this claim: 'Since sugary sap flows out on its "
                "own when an aphid punctures the phloem, showing the sap "
                "is under pressure, that pressure alone must push sugar "
                "in every direction inside the plant at once.'",
        "options": [
            "Not quite — pressure explains why sap moves along the phloem, but the overall direction still depends on where sucrose is loaded and unloaded",
            "True — pressure alone decides the exact direction that the sugar travels, whatever the positions of the sources and the sinks in the plant",
            "False, since the aphid experiment actually shows phloem carries no pressure at all",
            "True, but only because every sink in a plant is at exactly the same pressure",
        ],
        "correct_index": 0,
        "why": "Pressure explains how sap can flow along the phloem, but "
               "the overall direction still depends on where sucrose is "
               "loaded and unloaded.",
    },
    {
        "id": "ks4-translocation-h14",
        "subtopic_slug": "translocation",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A plant experiences a severe drought, and its cells "
                "generally lose turgor. Suggest the likely effect on "
                "translocation, given that phloem sap is a water-based "
                "solution.",
        "options": [
            "Translocation would be expected to speed up considerably during a severe drought",
            "Translocation could be impaired, since moving a water-based sap depends on the plant's cells having enough water",
            "Drought has no possible effect on translocation, only on transpiration",
            "Translocation would switch entirely to moving water instead of sugar",
        ],
        "correct_index": 1,
        "why": "Since phloem sap is a water-based solution, a severe "
               "drought that leaves cells short of water could impair "
               "translocation too.",
    },
    {
        "id": "ks4-translocation-h15",
        "subtopic_slug": "translocation",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare a plant whose roots are damaged and unable to act "
                "as a sink with an otherwise identical plant whose "
                "growing tip is damaged instead. Suggest how sugar "
                "distribution might differ between them.",
        "options": [
            "Both plants would distribute their sugar in exactly the same way as each other",
            "Neither plant could transport any sugar anywhere once one sink was damaged",
            "With one sink no longer able to receive sugar, more may be directed towards the plant's remaining sinks in each case",
            "Sugar production in the leaves would stop entirely in both plants",
        ],
        "correct_index": 2,
        "why": "With one sink no longer able to receive sugar, more may be "
               "directed towards each plant's remaining sinks instead.",
    },
    {
        "id": "ks4-translocation-h16",
        "subtopic_slug": "translocation",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate this claim: 'A plant could survive indefinitely "
                "on stored starch alone, using its sinks without ever "
                "needing an active source again.'",
        "options": [
            "True — stored starch alone can support unlimited growth forever",
            "True, since sinks can generate their own sugar once they run out of reserves",
            "False, but only because stored starch can never be converted back into a usable sugar again",
            "False — stored reserves are eventually used up, so an active source is needed again before long",
        ],
        "correct_index": 3,
        "why": "Stored reserves are finite and are eventually used up, so "
               "an active source is needed again before long.",
    },
    {
        "id": "ks4-translocation-h17",
        "subtopic_slug": "translocation",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A new, very strong sink develops close to an existing, "
                "weaker sink that a source leaf has been supplying. "
                "Predict the likely effect on how much sugar the weaker "
                "sink continues to receive.",
        "options": [
            "The weaker sink is likely to receive less sugar, as the stronger nearby sink draws more of the available supply",
            "The weaker sink is guaranteed to receive exactly the same amount as before",
            "The weaker sink will always receive more sugar than it did before once a nearby competing sink appears beside it",
            "New sinks have no effect whatsoever on sugar delivered to existing sinks",
        ],
        "correct_index": 0,
        "why": "A stronger nearby sink draws more of the available "
               "supply, so the weaker sink is likely to receive less than "
               "before.",
    },
    {
        "id": "ks4-translocation-h18",
        "subtopic_slug": "translocation",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate this claim: 'Since translocation happens in "
                "phloem and transpiration happens in xylem, damaging one "
                "tissue could never have any knock-on effect on the "
                "other process.'",
        "options": [
            "True — the two tissues and the two processes are completely isolated from one another in every respect, at every point in the plant",
            "Not entirely — severe damage to one transport tissue can weaken the whole plant, indirectly affecting processes relying on the other",
            "False, but only because xylem and phloem are actually the exact same tissue",
            "True, since phloem and xylem are never found anywhere near each other in a plant",
        ],
        "correct_index": 1,
        "why": "Severe damage to one transport tissue can weaken the "
               "whole plant, which can indirectly affect processes "
               "relying on the other tissue too.",
    },
    {
        "id": "ks4-translocation-h19",
        "subtopic_slug": "translocation",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why sugar reaching a fruit at the very tip of a "
                "long branch might take noticeably longer than water "
                "reaching a nearby leaf through the xylem, even over a "
                "similar distance.",
        "options": [
            "Water and sugar always move at exactly the same speed as one another, whichever tissue they travel in and whatever the distance",
            "Sugar cannot travel through phloem at all if the sink is far from the source",
            "Xylem transport is a fast, passively-pulled flow; phloem transport depends on active loading and unloading, which can take more time",
            "Fruit sinks are never supplied by translocation, only by their own photosynthesis",
        ],
        "correct_index": 2,
        "why": "Xylem transport is a fast, passively-pulled flow, while "
               "phloem transport depends on active loading and unloading, "
               "which can take more time over a similar distance.",
    },
    {
        "id": "ks4-translocation-h20",
        "subtopic_slug": "translocation",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate this claim: 'A heavily shaded leaf, making very "
                "little sugar of its own, cannot act as a source at "
                "all.'",
        "options": [
            "True — a leaf can only be a source if it is in full, direct sunlight",
            "True, since any leaf not in full sun automatically becomes a sink instead",
            "False, but only because a heavily shaded leaf in fact makes far more sugar than a fully sunlit one does",
            "Not entirely — it may still export what little sugar it does make, just at a lower rate than a well-lit leaf",
        ],
        "correct_index": 3,
        "why": "Even a heavily shaded leaf can still export what little "
               "sugar it makes, just at a lower rate than a well-lit "
               "leaf, rather than ceasing to be a source altogether.",
    },
    {
        "id": "ks4-translocation-h21",
        "subtopic_slug": "translocation",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "An insect pest destroys most of a fruit tree's leaves "
                "while its fruit is still developing. Predict the effect "
                "on the fruit.",
        "options": [
            "Fruit development is likely to be impaired, since there is little source left to supply it with sugar",
            "Fruit development would be completely unaffected, since fruit makes its own sugar",
            "Fruit development would actually improve, since the sugar can no longer reach the leaves to be competed for",
            "The tree would immediately grow entirely new fruit-independent leaves within hours",
        ],
        "correct_index": 0,
        "why": "With most of its source leaves destroyed, there is little "
               "left to supply the developing fruit with sugar, so its "
               "development is likely to be impaired.",
    },
    {
        "id": "ks4-translocation-h22",
        "subtopic_slug": "translocation",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate this claim: 'Once sugar has arrived at a sink, "
                "that structure can never later become a source, using "
                "the sugar it received to supply somewhere else.'",
        "options": [
            "True — a structure that has once been a sink can never afterwards supply its sugar anywhere else",
            "False — a sink such as a storage organ can later release its stored sugar and act as a source itself",
            "True, but only because sinks are physically incapable of storing sugar in the first place",
            "False, but only because sinks and sources are actually the same structure at all times",
        ],
        "correct_index": 1,
        "why": "A sink such as a storage organ can later release its "
               "stored sugar and act as a source itself, as a tuber does "
               "in spring.",
    },
    {
        "id": "ks4-translocation-h23",
        "subtopic_slug": "translocation",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A gardener grafts a fruiting branch from one apple "
                "variety onto the rootstock of a different variety. "
                "Suggest whether translocation can still deliver sugar "
                "from the branch's leaves down to the rootstock's roots.",
        "options": [
            "No — translocation only ever works between tissues taken from one single genetically identical individual plant, never across a graft",
            "No, since grafted tissues can never form a functioning vascular connection",
            "Yes — as long as a working phloem connection forms, sugar can be translocated regardless of the two varieties' genetic difference",
            "Yes, but only because the graft converts the rootstock into a second source",
        ],
        "correct_index": 2,
        "why": "As long as a working phloem connection forms across the "
               "graft, sugar can be translocated regardless of any "
               "genetic difference between the two varieties.",
    },
    {
        "id": "ks4-translocation-h24",
        "subtopic_slug": "translocation",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate this claim: 'A mutation that forces every one of "
                "a plant's sinks to receive exactly equal sugar at all "
                "times, regardless of need, would have no real "
                "disadvantage.'",
        "options": [
            "True — every sink needing exactly the same amount of sugar at every moment is the normal and efficient state for any plant anyway",
            "True, since sinks never actually have different sugar requirements from one another",
            "False, but only because equal sharing would always exactly match what every plant needs regardless of conditions",
            "False — different sinks have different needs at different times, so equal sharing could starve one sink while wasting sugar on another",
        ],
        "correct_index": 3,
        "why": "Different sinks have different needs at different times, "
               "so forcing equal sharing could starve one sink while "
               "wasting sugar on another.",
    },
    {
        "id": "ks4-translocation-h25",
        "subtopic_slug": "translocation",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A plant photosynthesises strongly in bright sunlight "
                "during a season when none of its usual sinks — growth, "
                "fruit or flowers — are actively developing. Suggest "
                "what is most likely to happen to the sugar it produces.",
        "options": [
            "Most of the surplus sugar is likely to be stored, for example as starch, rather than lost",
            "The sugar is immediately released into the air as a waste gas",
            "The leaves stop photosynthesising the very moment that no sink is actively developing",
            "The surplus sugar has nowhere at all to go and simply disappears",
        ],
        "correct_index": 0,
        "why": "With no actively developing sink to use it, the surplus "
               "sugar is most likely to be stored, for example as starch, "
               "rather than lost.",
    },
    {
        "id": "ks4-translocation-h26",
        "subtopic_slug": "translocation",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare the eventual fate of sugar delivered to a storage "
                "tuber, to a developing seed, and to a ripening fruit, as "
                "three different sinks.",
        "options": [
            "All three of these sinks use the sugar delivered to them in exactly the same way as one another, with no real difference at all between the three",
            "The tuber and seed can later release their stored sugar to support new growth; a ripening fruit's sugar is generally not recovered by the parent plant",
            "None of these three structures can ever store any of the sugar they receive",
            "Only the fruit can ever release its sugar again; the tuber and seed never do",
        ],
        "correct_index": 1,
        "why": "A tuber and a seed can later release their stored sugar to "
               "support new growth, while a ripening fruit's sugar is "
               "generally not recovered by the parent plant once the "
               "fruit is dispersed or eaten.",
    },
]
