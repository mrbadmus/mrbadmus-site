"""Biology · Cell biology — the MRB-338 expansion of `stem-cells`.

One leaf only: AQA 8461 §4.1.2.3. The original twelve rows in
`cell_biology.py` take the meaning of undifferentiated, tissue culture from
meristem, the two defining properties, the embryonic stem cell of a five-day
embryo, the multipotency limit on bone marrow, an autologous graft not being
rejected, five thousand identical orchids, the 'swap in a whole organ'
misconception, the tumour risk, the fourteen-day limit, insulin-producing
cells against daily injections, and the leftover-IVF-embryo argument.

This file takes what they leave: where a plant's stem cells actually are and
for how long, what marrow stem cells make and the transplant that uses them,
therapeutic cloning and the antigen reason its cells are accepted, viral
transfer, the AQA-named treatment targets, the plant applications — rare
species and identical disease-resistant crops, quickly and cheaply — and the
whole misconception set: cure-everything headlines, embryonic and adult cells
treated as interchangeable, stem cells imagined only in seeds, a stem cell
mistaken for a specialised one, and therapeutic cloning confused with
reproductive cloning.

The weight follows the CONTENT. `easier` stays at eight because recall here is
a short list of sources, names and one risk, and a ninth way of asking it is
the same question in new words. The demand lives in explaining a mechanism
from a named case and, above all, in evaluating an argument — this leaf
carries a genuine ethical debate, and the examinable skill is identifying what
an argument does and does not settle, never which side a pupil takes. So
`standard` and `harder` carry twenty-two each. Where a row cites an objection
it states it as the position of the people who hold it.

Numbers here are the ones the biology supplies: a donor-register expectation,
a micropropagation yield, and a one-off treatment cost set against a lifetime
of annual care.
"""

TOPIC = "cell-biology"
SUBJECT = "biology"

QUESTIONS = [
    # ══ easier · e05–e12 ═════════════════════════════════════════════════
    # Where plant stem cells are and how long they last, what marrow stem
    # cells make, the disease the transplant treats, the viral risk,
    # therapeutic cloning's product, the two named treatment targets, and
    # what rejection means.
    {
        "id": "ks4-stem-cells-e05",
        "subtopic_slug": "stem-cells",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the regions of a plant in which stem cells are found.",
        "options": [
            "Meristems, found at the tips of the roots and shoots",
            "The waxy cuticle on the upper surface of each leaf",
            "The xylem vessels that run the length of the stem",
            "Only inside the seed, before the plant starts to grow",
        ],
        "correct_index": 0,
        "why": "A plant's stem cells are its meristem cells, and meristem "
               "tissue sits at the growing tips of roots and shoots.",
    },
    {
        "id": "ks4-stem-cells-e06",
        "subtopic_slug": "stem-cells",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State which cells are produced by the stem cells in bone "
                "marrow.",
        "options": [
            "Nerve cells, because marrow lies close to the spinal cord",
            "Blood cells",
            "Muscle cells, because marrow sits inside a bone that muscles pull on",
            "Any of the two hundred or more cell types in the human body",
        ],
        "correct_index": 1,
        "why": "Bone marrow stem cells are adult stem cells, and they form "
               "the different types of blood cell.",
    },
    {
        "id": "ks4-stem-cells-e07",
        "subtopic_slug": "stem-cells",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the disease of the blood that is treated using a bone "
                "marrow transplant.",
        "options": [
            "Type 1 diabetes, in which the pancreas stops releasing insulin",
            "Cystic fibrosis, in which thick mucus collects in the lungs",
            "Leukaemia, which is a cancer of the white blood cells",
            "Paralysis following an injury to the spinal cord",
        ],
        "correct_index": 2,
        "why": "Leukaemia is a cancer of the blood cells, and transplanted "
               "marrow stem cells restore healthy blood cell production.",
    },
    {
        "id": "ks4-stem-cells-e08",
        "subtopic_slug": "stem-cells",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State one risk to a patient of being treated with stem cells "
                "that have been grown in a laboratory.",
        "options": [
            "The stem cells lose their nucleus while they are being grown",
            "The stem cells stop the patient's own cells respiring",
            "The stem cells turn the patient's specialised cells back into stem cells",
            "A virus may be passed from the culture to the patient",
        ],
        "correct_index": 3,
        "why": "Transfer of a viral infection is a recognised risk, because "
               "cells grown in culture may themselves be infected.",
    },
    {
        "id": "ks4-stem-cells-e09",
        "subtopic_slug": "stem-cells",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what is produced in therapeutic cloning.",
        "options": [
            "A fully formed organ that is ready to be transplanted",
            "A baby that is genetically identical to the patient",
            "A sample of the patient's DNA, copied many million times over",
            "An early embryo that carries the same genes as the patient",
        ],
        "correct_index": 3,
        "why": "Therapeutic cloning produces an embryo carrying the "
               "patient's own genes, from which stem cells are then taken.",
    },
    {
        "id": "ks4-stem-cells-e10",
        "subtopic_slug": "stem-cells",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name two conditions that doctors hope to treat using stem "
                "cells.",
        "options": [
            "Measles and mumps",
            "Broken bones and bruises",
            "Diabetes and paralysis",
            "Hay fever and asthma",
        ],
        "correct_index": 2,
        "why": "Stem cells could replace the insulin-producing cells lost in "
               "diabetes and the nerve cells lost in paralysis.",
    },
    {
        "id": "ks4-stem-cells-e11",
        "subtopic_slug": "stem-cells",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what is meant by rejection when a patient is given "
                "cells from a donor.",
        "options": [
            "The donated cells refuse to divide once they have been placed inside the patient",
            "The patient's immune system recognises the donated cells as foreign and attacks them",
            "The donated cells attack the patient's own red blood cells and break them down",
            "The donated cells differentiate into the wrong specialised type for the tissue",
        ],
        "correct_index": 1,
        "why": "Rejection is the immune system treating the donated cells as "
               "foreign, because their antigens differ from the patient's.",
    },
    {
        "id": "ks4-stem-cells-e12",
        "subtopic_slug": "stem-cells",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State for how long a plant keeps cells that are able to "
                "differentiate.",
        "options": [
            "Throughout the plant's whole life",
            "Only while the seed is germinating",
            "Only during the plant's first year of growth",
            "Only while the plant is in flower",
        ],
        "correct_index": 0,
        "why": "Meristem cells stay undifferentiated for the whole of a "
               "plant's life, which is why new roots and leaves can always "
               "be made.",
    },

    # ══ standard · s05–s26 ═══════════════════════════════════════════════
    # The named cases explained — therapeutic cloning, the marrow transplant,
    # tissue culture, cord blood, burns, the pancreas, the spinal cord — and
    # the misconception set met head on, one row each.
    {
        "id": "ks4-stem-cells-s05",
        "subtopic_slug": "stem-cells",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why stem cells produced by therapeutic cloning are "
                "not attacked by the patient's immune system.",
        "options": [
            "They are taken before the embryo has developed any antigens",
            "They are treated with a drug that hides them from white blood cells",
            "They carry the patient's genes, so their antigens are the patient's own",
            "They divide too quickly for the white blood cells to reach them",
        ],
        "correct_index": 2,
        "why": "The embryo is made using the patient's own nucleus, so its "
               "cells carry the patient's antigens and are not seen as "
               "foreign.",
    },
    {
        "id": "ks4-stem-cells-s06",
        "subtopic_slug": "stem-cells",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a patient's own bone marrow is destroyed before "
                "donor marrow is transplanted to treat leukaemia.",
        "options": [
            "The patient's own cancerous stem cells would otherwise keep making abnormal blood cells",
            "The old marrow would take up the space the donor cells need in order to respire",
            "The old marrow would differentiate into the donor's cell types and confuse the diagnosis",
            "Destroying it softens the bone enough for the donor cells to be injected into it",
        ],
        "correct_index": 0,
        "why": "The disease lies in the patient's own blood-forming stem "
               "cells, so they are destroyed and healthy donor stem cells "
               "take over.",
    },
    {
        "id": "ks4-stem-cells-s07",
        "subtopic_slug": "stem-cells",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A grower wants two hundred strawberry plants that all crop "
                "at the same time. Explain why meristem tissue is used "
                "rather than seed.",
        "options": [
            "Seed cannot be collected from a strawberry plant at all",
            "Seed takes in water, and so grows more slowly than a tissue culture does",
            "Seed carries only half the genes, so the plants grown from it would be smaller",
            "Seed comes from sexual reproduction, so the plants would vary",
        ],
        "correct_index": 3,
        "why": "Tissue culture from meristem gives clones with identical "
               "genes, while seed is the product of sexual reproduction and "
               "varies.",
    },
    {
        "id": "ks4-stem-cells-s08",
        "subtopic_slug": "stem-cells",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest how cloning from meristem tissue helps to protect a "
                "rare plant species from extinction.",
        "options": [
            "It alters the plant's genes so that it can survive in new habitats",
            "Large numbers of identical new plants can be produced from very little tissue",
            "It lets the species reproduce sexually without needing a partner",
            "It makes every new plant resistant to all the diseases of its habitat",
        ],
        "correct_index": 1,
        "why": "A small piece of meristem yields many identical plants, so a "
               "species reduced to a few individuals can be built back up.",
    },
    {
        "id": "ks4-stem-cells-s09",
        "subtopic_slug": "stem-cells",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A patient given stem cells from a donor is prescribed drugs "
                "that suppress the immune system. Explain the benefit and "
                "one drawback.",
        "options": [
            "The donor cells are not rejected, but the patient catches infections more easily",
            "The donor cells divide faster, but the drugs are extremely expensive to make",
            "The donor cells stop differentiating, but the course lasts only a single week",
            "The donor cells lose their antigens, but the patient's platelets are destroyed too",
        ],
        "correct_index": 0,
        "why": "Suppressing the immune response stops it attacking the "
               "foreign antigens on the donor cells, but a weakened immune "
               "system fights infection less well.",
    },
    {
        "id": "ks4-stem-cells-s10",
        "subtopic_slug": "stem-cells",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain how a virus could reach a patient during a stem "
                "cell treatment.",
        "options": [
            "A virus is produced by any stem cell that is made to differentiate",
            "A virus forms inside the patient whenever a foreign antigen enters the blood",
            "A virus infecting the cultured cells is carried into the patient with them",
            "A virus is added to the culture deliberately, to make the stem cells divide",
        ],
        "correct_index": 2,
        "why": "Cells grown in culture can be carrying a viral infection, "
               "and transplanting the cells transplants the virus with them.",
    },
    {
        "id": "ks4-stem-cells-s11",
        "subtopic_slug": "stem-cells",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student writes that embryonic and adult stem cells can be "
                "used in place of one another. Explain why this is wrong.",
        "options": [
            "Embryonic stem cells are rejected by every patient, while adult ones never are",
            "An embryonic stem cell can form cell types that an adult stem cell simply cannot",
            "Adult stem cells occur only in bone marrow, while embryonic ones occur everywhere",
            "Adult stem cells divide by meiosis, while embryonic stem cells divide by mitosis",
        ],
        "correct_index": 1,
        "why": "The two differ in the range of cells they can become, so one "
               "cannot simply stand in for the other.",
    },
    {
        "id": "ks4-stem-cells-s12",
        "subtopic_slug": "stem-cells",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student states that a plant's stem cells are found only in "
                "its seeds. Explain the error.",
        "options": [
            "A seed holds no living cells at all until it has been watered",
            "A seed holds only specialised cells, because its embryo plant is complete",
            "Stem cells are found only in the flowers, where the new seeds are made",
            "Meristems at the root and shoot tips hold stem cells for life",
        ],
        "correct_index": 3,
        "why": "Meristem tissue at the growing tips keeps its stem cells "
               "permanently, which is how a mature plant still makes new "
               "roots and leaves.",
    },
    {
        "id": "ks4-stem-cells-s13",
        "subtopic_slug": "stem-cells",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student says a stem cell must be specialised, because "
                "dividing is its own special job. Explain why this is wrong.",
        "options": [
            "It has not yet developed a structure suited to one particular job, so it is undifferentiated",
            "It is specialised, but only for the short while that passes between one "
            "division and the next",
            "It is specialised for dividing, which is exactly why it is called a stem cell",
            "It has no nucleus, so it cannot be specialised for anything at all",
        ],
        "correct_index": 0,
        "why": "A stem cell is undifferentiated: it has not taken on the "
               "structure that suits a cell to one particular function.",
    },
    {
        "id": "ks4-stem-cells-s14",
        "subtopic_slug": "stem-cells",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Describe how therapeutic cloning differs from reproductive "
                "cloning.",
        "options": [
            "Therapeutic cloning uses an egg cell, and reproductive cloning uses a sperm cell",
            "Therapeutic cloning copies only the DNA, while reproductive cloning moves a whole nucleus",
            "Therapeutic cloning produces cells for treatment, not a new individual",
            "Therapeutic cloning is carried out in plants, and reproductive cloning in animals",
        ],
        "correct_index": 2,
        "why": "Both begin with an embryo carrying the patient's genes, but "
               "in therapeutic cloning that embryo supplies stem cells and "
               "is never allowed to develop into an individual.",
    },
    {
        "id": "ks4-stem-cells-s15",
        "subtopic_slug": "stem-cells",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why some people object to research that uses human "
                "embryonic stem cells.",
        "options": [
            "They have found that embryonic stem cells cannot be made to differentiate",
            "They have found that embryonic stem cells are rejected by every patient",
            "They have shown that adult stem cells work better for every known condition",
            "They hold that an embryo is a potential human life",
        ],
        "correct_index": 3,
        "why": "The objection people raise is that obtaining the cells "
               "destroys the embryo, which they regard as a potential human "
               "life.",
    },
    {
        "id": "ks4-stem-cells-s16",
        "subtopic_slug": "stem-cells",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why a person who objects to embryonic stem cell "
                "research may still support research on adult stem cells.",
        "options": [
            "Adult stem cells can be taken only from people who have already died",
            "Taking adult stem cells from a living donor does not destroy an embryo",
            "Adult stem cells can become any cell type, so no embryo is ever needed",
            "Adult stem cells are the only kind that a patient's body will accept",
        ],
        "correct_index": 1,
        "why": "Adult stem cells come from a living, consenting donor's own "
               "tissue, so the objection about destroying an embryo does not "
               "arise.",
    },
    {
        "id": "ks4-stem-cells-s17",
        "subtopic_slug": "stem-cells",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain how stem cells might be used to treat a person "
                "paralysed by a spinal injury.",
        "options": [
            "They would dissolve the scar tissue so the old nerve cells could re-join",
            "They would carry the messages between the brain and the muscles themselves",
            "They would differentiate into nerve cells that restore the connection",
            "They would replace the muscle cells that have wasted since the injury",
        ],
        "correct_index": 2,
        "why": "The stem cells differentiate into new nerve cells, replacing "
               "those destroyed at the injury and restoring the pathway to "
               "the muscles.",
    },
    {
        "id": "ks4-stem-cells-s18",
        "subtopic_slug": "stem-cells",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain which cells a stem cell treatment for Type 1 "
                "diabetes would have to replace.",
        "options": [
            "The cells of the pancreas that produce insulin",
            "The red blood cells that carry glucose around the body",
            "The liver cells that convert glucose into glycogen for storage",
            "The muscle cells that take glucose out of the blood as it flows past",
        ],
        "correct_index": 0,
        "why": "In Type 1 diabetes the insulin-producing cells of the "
               "pancreas have been destroyed, so those are the cells that "
               "would have to be replaced.",
    },
    {
        "id": "ks4-stem-cells-s19",
        "subtopic_slug": "stem-cells",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why some parents pay to have blood from their "
                "baby's umbilical cord stored.",
        "options": [
            "It holds ready-made blood cells that could be transfused back at any age",
            "It holds stem cells that would match the child if treatment were ever needed",
            "It holds embryonic stem cells, which can become any cell type in the body",
            "It holds antibodies that would protect the child against infection for life",
        ],
        "correct_index": 1,
        "why": "Cord blood is rich in blood-forming stem cells carrying the "
               "child's own antigens, so they would not be rejected if they "
               "were used later.",
    },
    {
        "id": "ks4-stem-cells-s20",
        "subtopic_slug": "stem-cells",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain one practical difficulty in using a patient's own "
                "adult stem cells for a treatment.",
        "options": [
            "They are rejected far more strongly than any donor's cells would be",
            "They can be collected only from a patient who is under ten years old",
            "They lose their genes each time they are made to divide in the laboratory",
            "They are present in small numbers and are hard to grow in culture",
        ],
        "correct_index": 3,
        "why": "Adult stem cells are scarce in a tissue and difficult to "
               "grow in large numbers, so obtaining enough of them is a real "
               "obstacle.",
    },
    {
        "id": "ks4-stem-cells-s21",
        "subtopic_slug": "stem-cells",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why growing crop plants from meristem tissue is "
                "described as economical.",
        "options": [
            "Many identical plants are produced quickly from a very small piece of tissue",
            "The plants produced need no watering, so the whole cost of irrigation is saved",
            "Every plant produced makes its own seed, which the grower can then sell on",
            "The plants produced are all different, so the grower can sell a wider range",
        ],
        "correct_index": 0,
        "why": "A little tissue yields a great many plants in a short time "
               "and a small space, so the cost of each plant is low.",
    },
    {
        "id": "ks4-stem-cells-s22",
        "subtopic_slug": "stem-cells",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A newspaper headline claims that stem cells can cure any "
                "disease. Suggest why a scientist would treat this with "
                "caution.",
        "options": [
            "Stem cells have so far been used successfully only in plants",
            "Stem cells can be given only to a patient under one year old",
            "Most possible uses are still being researched, not proven",
            "Stem cells are known to cause the very disease they are meant to treat",
        ],
        "correct_index": 2,
        "why": "Bone marrow transplants are established, but most other "
               "stem cell treatments are still at the research stage, so a "
               "claim to cure any disease goes well beyond the evidence.",
    },
    {
        "id": "ks4-stem-cells-s23",
        "subtopic_slug": "stem-cells",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "In therapeutic cloning a nucleus from the patient is put "
                "into an egg cell whose own nucleus has been removed. "
                "Explain why the embryo then has the patient's genes.",
        "options": [
            "The egg cell copies the patient's genes from the fluid around it",
            "The egg's cytoplasm supplies the genes once the patient's cell is added",
            "The patient's nucleus makes the egg's own genes change to match it",
            "The genetic material of a cell is held in its nucleus",
        ],
        "correct_index": 3,
        "why": "A cell's genes are in its nucleus, so replacing the egg's "
               "nucleus with the patient's replaces the genetic information "
               "entirely.",
    },
    {
        "id": "ks4-stem-cells-s24",
        "subtopic_slug": "stem-cells",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why skin grown from a burns patient's own stem "
                "cells may be better than a graft taken from elsewhere on "
                "their body.",
        "options": [
            "Skin grown from stem cells carries no antigens, so it can never be rejected",
            "No healthy skin has to be removed from another part of the patient",
            "Skin grown from stem cells regrows by itself if it is ever damaged again",
            "Skin taken from elsewhere on the body is always rejected by the immune system",
        ],
        "correct_index": 1,
        "why": "Growing the skin from the patient's own stem cells avoids "
               "wounding a second area of the body, while still giving a "
               "genetic match.",
    },
    {
        "id": "ks4-stem-cells-s25",
        "subtopic_slug": "stem-cells",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why every plant grown from the meristem of one "
                "disease-resistant parent also resists that disease.",
        "options": [
            "The plants take the resistance in from the culture medium as they grow",
            "Half of the plants grown will be resistant and half of them will not",
            "They are clones of that parent plant, so they carry exactly the same genes as it does",
            "The plants become resistant by meeting the disease while they are very young",
        ],
        "correct_index": 2,
        "why": "Tissue culture is a form of asexual reproduction, so every "
               "plant carries the parent's genes and therefore the same "
               "resistance.",
    },
    {
        "id": "ks4-stem-cells-s26",
        "subtopic_slug": "stem-cells",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest one economic argument that is made for funding stem "
                "cell research.",
        "options": [
            "A single treatment could cost less than caring for a patient for years",
            "The money spent on research is returned in full if the treatment fails",
            "Stem cell treatments would need no doctors, so staffing costs would fall",
            "Stem cells can be collected free of charge from any patient who agrees",
        ],
        "correct_index": 0,
        "why": "The economic case put forward is that a treatment which "
               "repairs a condition once may cost less overall than a "
               "lifetime of managing it.",
    },

    # ══ harder · h05–h26 ═════════════════════════════════════════════════
    # Unfamiliar cases, two-case comparison, three calculations, and the
    # evaluation work this leaf exists for — what an argument settles and
    # what it leaves standing, never which side is right.
    {
        "id": "ks4-stem-cells-h05",
        "subtopic_slug": "stem-cells",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A patient has a blood disorder caused by a faulty allele. "
                "Explain why treating them with stem cells from their own "
                "bone marrow is unlikely to work.",
        "options": [
            "Bone marrow stem cells form white blood cells only, and not red ones",
            "The patient's own stem cells carry the same faulty allele as all their other cells",
            "The patient's own stem cells would be rejected by their immune system",
            "Bone marrow stem cells stop dividing once a person reaches adulthood",
        ],
        "correct_index": 1,
        "why": "Every cell of the patient, marrow stem cells included, "
               "carries the faulty allele, so the blood cells they made "
               "would be faulty too.",
    },
    {
        "id": "ks4-stem-cells-h06",
        "subtopic_slug": "stem-cells",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate the claim that therapeutic cloning removes every "
                "ethical objection to using embryonic stem cells.",
        "options": [
            "The claim holds, because the embryo produced is the patient's own tissue rather than a separate life",
            "The claim fails, because therapeutic cloning produces no usable stem cells at all",
            "The claim holds, because no embryo of any kind is involved in therapeutic cloning",
            "It answers the rejection problem, but an embryo is still created and then destroyed",
        ],
        "correct_index": 3,
        "why": "Therapeutic cloning solves the immune-rejection problem, but "
               "people who object to destroying an embryo hold the same "
               "objection to it.",
    },
    {
        "id": "ks4-stem-cells-h07",
        "subtopic_slug": "stem-cells",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate the argument that adult stem cells make research "
                "on embryonic stem cells unnecessary.",
        "options": [
            "It is weak, because adult stem cells form a narrower range of cell types",
            "It is sound, because an adult stem cell can form any of the body's cell types",
            "It is weak, because adult stem cells are always rejected by the patient",
            "It is sound, because adult stem cells are the only ones that will grow in culture",
        ],
        "correct_index": 0,
        "why": "Adult stem cells cannot form every cell type, so they cannot "
               "yet replace embryonic cells for conditions needing tissues "
               "outside their range.",
    },
    {
        "id": "ks4-stem-cells-h08",
        "subtopic_slug": "stem-cells",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Patient A is treated with stem cells grown from their own "
                "tissue and patient B with cells from an unrelated donor. "
                "Predict which is more likely to reject them, and explain.",
        "options": [
            "Patient A, because cells taken from their own body divide too quickly once returned",
            "Neither, because a stem cell is undifferentiated and so carries no antigens at all",
            "Patient B, because the donor's cells carry different antigens",
            "Patient B, because donated cells are always given in far larger numbers",
        ],
        "correct_index": 2,
        "why": "Rejection follows from foreign antigens, and only the "
               "donor's cells carry antigens different from the recipient's.",
    },
    {
        "id": "ks4-stem-cells-h09",
        "subtopic_slug": "stem-cells",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Stem cells restored movement in paralysed mice. Evaluate "
                "the conclusion that the same treatment will work in people.",
        "options": [
            "It is sound, because mice and humans have identical nervous systems",
            "It is not yet supported; a result in one species must be tested in humans",
            "It is sound, because stem cells behave in the same way in every organism",
            "It is wrong, because a treatment that works in an animal never works in a person",
        ],
        "correct_index": 1,
        "why": "An animal result is evidence that the approach may work, but "
               "human trials are needed before the conclusion can be drawn.",
    },
    {
        "id": "ks4-stem-cells-h10",
        "subtopic_slug": "stem-cells",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A private clinic sells a stem cell treatment that has never "
                "been through a clinical trial. Suggest what a patient "
                "should weigh up before agreeing to it.",
        "options": [
            "Only the cost, because a treatment on sale to the public must already be safe",
            "Only how near the clinic is, because every stem cell treatment works the same way",
            "Only the clinic's own reports of success, because it treats such patients daily",
            "That the benefit is unproven, while the risks of infection and tumours are real",
        ],
        "correct_index": 3,
        "why": "Without trial evidence there is no reliable measure of "
               "benefit, while the known risks of stem cell treatment still "
               "apply.",
    },
    {
        "id": "ks4-stem-cells-h11",
        "subtopic_slug": "stem-cells",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare the range of cell types a plant meristem cell can "
                "produce with the range produced by an adult stem cell in "
                "human bone marrow.",
        "options": [
            "Both can produce any cell type found anywhere in their own organism",
            "Both are limited to the cell types of the tissue in which they sit",
            "The meristem cell can form any plant cell; the marrow cell forms blood cells",
            "The marrow cell can form any human cell; the meristem cell forms only root cells",
        ],
        "correct_index": 2,
        "why": "Plant meristem cells stay able to form any plant cell, while "
               "a human bone marrow stem cell is restricted to the blood "
               "cells of its own tissue.",
    },
    {
        "id": "ks4-stem-cells-h12",
        "subtopic_slug": "stem-cells",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A rare orchid is saved from extinction by cloning the one "
                "surviving plant. Suggest why the new population is still "
                "vulnerable to a new disease.",
        "options": [
            "They all have the same genes, so none is likely to resist the new disease",
            "A cloned plant has a weaker cell wall than a plant that was grown from seed",
            "A cloned plant cannot produce any new meristem tissue of its own",
            "A cloned plant carries no genes for resistance to any disease whatsoever",
        ],
        "correct_index": 0,
        "why": "Cloning produces no genetic variation, so a disease that "
               "affects one plant affects every one of them.",
    },
    {
        "id": "ks4-stem-cells-h13",
        "subtopic_slug": "stem-cells",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain, in terms of antigens, why cells from an embryo made "
                "by therapeutic cloning are accepted, while cells from a "
                "leftover IVF embryo may not be.",
        "options": [
            "The cloned embryo's cells have no antigens, while the IVF embryo's cells do",
            "The cloned embryo's cells make antibodies that shut down the immune response",
            "The IVF embryo's cells are older, so their antigens have already broken down",
            "The cloned embryo's cells carry the patient's own antigens, while the IVF embryo's do not",
        ],
        "correct_index": 3,
        "why": "The cloned embryo is made from the patient's nucleus, so its "
               "antigens match, whereas an IVF embryo has two unrelated "
               "parents and different antigens.",
    },
    {
        "id": "ks4-stem-cells-h14",
        "subtopic_slug": "stem-cells",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate the view that stem cell research should be judged "
                "only by the number of lives it could save.",
        "options": [
            "It is a complete test, because saving lives is the only purpose medicine has",
            "It ignores the objections that people raise about the way the cells are obtained",
            "It is a complete test, because nobody is harmed at any stage of the research",
            "It is useless, because the number of lives saved could never be estimated",
        ],
        "correct_index": 1,
        "why": "Counting the benefit is one side of an evaluation; a full "
               "judgement also weighs the objections raised about the source "
               "of the cells.",
    },
    {
        "id": "ks4-stem-cells-h15",
        "subtopic_slug": "stem-cells",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A hospital chooses a bone marrow transplant rather than an "
                "embryonic stem cell treatment for a patient with "
                "leukaemia. Suggest two reasons for that choice.",
        "options": [
            "Embryonic stem cells cannot divide, so they would produce no new blood at all",
            "Embryonic stem cells are much cheaper, but they take many years to prepare",
            "It is an established treatment, and the cells needed are blood cells",
            "Bone marrow stem cells can form any cell type, and embryonic stem cells cannot",
        ],
        "correct_index": 2,
        "why": "Marrow transplants are a proven, routine treatment, and the "
               "cells the patient needs are exactly the ones a marrow stem "
               "cell makes.",
    },
    {
        "id": "ks4-stem-cells-h16",
        "subtopic_slug": "stem-cells",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A donor register holds 600 000 people, and about 1 in "
                "20 000 of them is a tissue match for one particular "
                "patient. Calculate the number of matching donors expected.",
        "options": [
            "30 donors",
            "3 donors",
            "300 donors",
            "0.03 donors",
        ],
        "correct_index": 0,
        "why": "600 000 divided by 20 000 gives 30, so about thirty people "
               "on the register would be expected to match.",
    },
    {
        "id": "ks4-stem-cells-h17",
        "subtopic_slug": "stem-cells",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A laboratory divides one piece of meristem tissue into 24 "
                "explants, and each explant grows into 15 plantlets. "
                "Calculate the number of plants produced.",
        "options": [
            "39 plants",
            "360 plants",
            "24 plants",
            "1.6 plants",
        ],
        "correct_index": 1,
        "why": "24 explants multiplied by 15 plantlets each gives 360 "
               "plants, every one of them a clone of the parent.",
    },
    {
        "id": "ks4-stem-cells-h18",
        "subtopic_slug": "stem-cells",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A patient with an otherwise untreatable condition is "
                "offered a stem cell treatment that carries a small risk of "
                "viral infection. Evaluate how that risk should be weighed.",
        "options": [
            "The risk can be ignored, because any virus passed on could be treated with antibiotics",
            "The treatment must be refused, because a risk of any size makes a treatment unethical",
            "The risk vanishes if the cells are taken from the patient's own body to begin with",
            "The risk is weighed against the benefit of treating the condition",
        ],
        "correct_index": 3,
        "why": "Evaluation means setting a small, known risk against the "
               "size of the benefit, rather than treating either one on its "
               "own as decisive.",
    },
    {
        "id": "ks4-stem-cells-h19",
        "subtopic_slug": "stem-cells",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student argues that because therapeutic cloning begins in "
                "the same way as reproductive cloning, it must end the same "
                "way. Evaluate this reasoning.",
        "options": [
            "It is wrong; the embryo supplies stem cells and is never implanted",
            "It is correct, because both of these processes always produce a living individual",
            "It is wrong, because the two processes begin in completely different ways",
            "It is correct, because an embryo cannot be stopped once it has been made",
        ],
        "correct_index": 0,
        "why": "The first steps are shared, but the therapeutic embryo is "
               "used as a source of stem cells and is not implanted, so the "
               "outcomes differ.",
    },
    {
        "id": "ks4-stem-cells-h20",
        "subtopic_slug": "stem-cells",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare the ethical debate about embryonic stem cells with "
                "the absence of such a debate about cloning plants from "
                "meristem tissue.",
        "options": [
            "There is no real difference between them; both are debated just as strongly",
            "Plant cloning is not debated, because plant cells are not truly alive",
            "The objections concern a human embryo, which plant cloning does not involve",
            "Plant cloning is not debated, because plants have no genes that could be copied",
        ],
        "correct_index": 2,
        "why": "The objection raised to embryonic stem cells is about "
               "destroying a human embryo, and no embryo is involved when a "
               "plant is cloned from meristem.",
    },
    {
        "id": "ks4-stem-cells-h21",
        "subtopic_slug": "stem-cells",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Cells grown from a patient's own tissue take eight weeks to "
                "prepare, while a stored donor line is ready at once. "
                "Suggest what this means for someone who has just had a "
                "heart attack.",
        "options": [
            "It makes no difference, because heart muscle repairs itself within eight weeks anyway",
            "Their own cells remain the better choice, because a stored line cannot be rejected",
            "The stored line should never be used, because stored cells lose their genes",
            "The donor line may have to be used, despite the risk of rejection",
        ],
        "correct_index": 3,
        "why": "Damage after a heart attack cannot wait eight weeks, so the "
               "immediately available donor cells may be chosen even though "
               "they may be rejected.",
    },
    {
        "id": "ks4-stem-cells-h22",
        "subtopic_slug": "stem-cells",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A farmer is deciding whether to raise a new crop from seed "
                "or to clone it from meristem tissue. Compare the two, "
                "giving one advantage of each.",
        "options": [
            "Cloning brings variation, while seed gives plants identical to the parent",
            "Cloning gives identical high-yielding plants quickly; seed brings variation",
            "Cloning is slower but cheaper, while seed is faster but far more expensive",
            "Cloning needs no parent plant at all, while seed needs two parent plants",
        ],
        "correct_index": 1,
        "why": "Meristem cloning produces many identical plants of a chosen "
               "quality very quickly, while seed brings the genetic "
               "variation a cloned crop lacks.",
    },
    {
        "id": "ks4-stem-cells-h23",
        "subtopic_slug": "stem-cells",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Embryonic stem cell research is permitted in some countries "
                "and banned in others. Explain how the same evidence can "
                "lead to different rules.",
        "options": [
            "One group of scientists holds evidence that the other group has never seen",
            "The evidence itself changes according to where the research is carried out",
            "The evidence shows what is possible; the rules also weigh people's beliefs",
            "The rules are set by whichever country has the larger research budget",
        ],
        "correct_index": 2,
        "why": "Science establishes what can be done, but whether it should "
               "be done is a judgement that also draws on ethical and "
               "religious views, and those differ between societies.",
    },
    {
        "id": "ks4-stem-cells-h24",
        "subtopic_slug": "stem-cells",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A patient could be treated either with stem cells or with a "
                "donated organ. Suggest one advantage of the stem cell "
                "route.",
        "options": [
            "A stem cell treatment carries no risk of any kind to the patient",
            "The cells can be grown from the patient's own tissue, so no matching donor is needed",
            "A stem cell treatment does away with the need for the patient to have surgery",
            "Stem cells work immediately, while a donated organ takes years to start working",
        ],
        "correct_index": 1,
        "why": "Growing the cells from the patient's own tissue avoids both "
               "the wait for a matching donor and the rejection a donated "
               "organ risks.",
    },
    {
        "id": "ks4-stem-cells-h25",
        "subtopic_slug": "stem-cells",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A stem cell treatment costs 250 000 pounds once. The "
                "current treatment costs 8 000 pounds every year for life. "
                "Determine after how many years the stem cell treatment "
                "becomes cheaper.",
        "options": [
            "After 3 years",
            "After 313 years",
            "After 320 years",
            "After 32 years",
        ],
        "correct_index": 3,
        "why": "250 000 divided by 8 000 is 31.25, so the running cost "
               "passes the one-off cost during the thirty-second year.",
    },
    {
        "id": "ks4-stem-cells-h26",
        "subtopic_slug": "stem-cells",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate the statement that because embryonic stem cells "
                "can become any cell type, they are always the best choice "
                "for a treatment.",
        "options": [
            "It overlooks rejection, the risk of tumours, and the objections raised",
            "It is correct, because versatility is the only property that matters here",
            "It is wrong, because an embryonic stem cell can only ever become a nerve cell",
            "It is correct, because embryonic stem cells are never rejected by a patient",
        ],
        "correct_index": 0,
        "why": "Versatility is one factor, but donor embryonic cells can be "
               "rejected, cells left undifferentiated may form tumours, and "
               "their source is contested.",
    },
]
