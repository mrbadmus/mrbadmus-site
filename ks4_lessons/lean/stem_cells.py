# -*- coding: utf-8 -*-
"""Stem cells, in the lean shape. Spec table: ks4-stem-cells.md (AQA 8464 4.1.2.3 / 8461 4.1.2.3, word
for word the same; no HT-only or Biology-only lines). "Knowledge and understanding of stem cell
techniques are not required."

LEGACY (batch 6). The ladder and the practice set stay from the Design page. The practice set is the
page's own hard-coded `bankSrc` (same five items on every route), so its fixes are logic_edits. One
practice stem is replaced (the leukaemia item: not in the spec), so that ks4q: id retires and a new
one is added; the other four stems are kept. Rung prompts keep their positions, so rung ids survive.
This batch's logic is plain ASCII with \\uXXXX escapes; the edits below are written that way
(generated from the post-ruling logic, so each `old` occurs exactly once).
"""

LOGIC_EDITS = \
[
    # Practice Q1 REPLACED (new stem, new id; the old id retires): leukaemia and bone marrow transplants are not in 4.1.2.3, and the credited option was visibly the longest (+50).
    ("{ q: 'How are stem cells used to treat leukaemia?', opts: [['A bone marrow transplant: cancerous blood cells destroyed, then donor stem cells replace them and produce healthy blood cells', true], ['Embryonic stem cells are injected into the blood to replace cancer cells', false], ['Stem cells are used to make antibodies that kill cancer cells directly', false], ['Stem cells repair the damaged DNA in leukaemia cells, reversing the cancer', false]],\n        wrong_explanations: { 1: 'Embryonic stem cells are not used for leukaemia treatment \\u2014 adult bone marrow stem cells are used. They are donated or sometimes the patient\\u2019s own (after treatment).', 2: 'Antibodies that target cancer cells are a different therapy (monoclonal antibodies) \\u2014 not how stem cells work in leukaemia treatment.', 3: 'Stem cells don\\u2019t repair cancer cell DNA \\u2014 the cancer cells are destroyed by chemotherapy/radiotherapy first, then NEW healthy cells are produced from transplanted stem cells.' } },",
     "{ q: 'What can stem cells from adult bone marrow form?', opts: [['Many types of cell, including blood cells', true], ['Any type of human cell, and plant cells too', false], ['Only nerve cells, muscle cells and skin cells', false], ['No other cells, as they are fully specialised', false]],\n        wrong_explanations: { 1: 'Bone marrow stem cells make human cells only, and not every type.', 2: 'They form many types of cell, including blood cells.', 3: 'Stem cells are undifferentiated, not specialised.' } },"),
    # Practice Q2 (ethics), stem kept: credited the longest (+55), dash.
    ("opts: [['Obtaining them requires destroying an embryo \\u2014 which some consider to be destroying a potential human life', true], ['They cause cancer in patients who receive them', false], ['They are ineffective at treating disease', false], ['They are too expensive to collect and store', false]],",
     "opts: [['An embryo is destroyed to obtain them', true], ['They always cause cancer in patients', false], ['They cannot be used to treat any disease', false], ['They are too expensive to collect', false]],"),
    ("wrong_explanations: { 1: 'Cancer risk is a technical concern \\u2014 the main ETHICAL controversy is about the moral status of the embryo that is destroyed.', 2: 'Embryonic stem cells could treat many conditions because they can become most cell types \\u2014 the objection is ethical, not about whether they work.', 3: 'Cost and practicality are challenges \\u2014 but the defining controversy is ethical: is it acceptable to destroy a potential human life for medical research?' } },",
     "wrong_explanations: { 1: 'They do not always cause cancer, and an ethical objection is about right and wrong.', 2: 'They may help treat conditions such as diabetes and paralysis.', 3: 'Cost is a practical problem, not an ethical one.' } },"),
    # Rung 2 (i): credited option visibly the longest (+23); 'a limited range' is not the spec's wording (4.1.2.3: bone marrow stem cells 'can form many types of cells including blood cells').
    ("why: 'Embryonic: most types of human cell. Bone marrow: a limited range, including blood cells.', options: [\n            { text: 'Embryonic form most types; bone marrow a limited range', correct: true }, { text: 'Both form exactly the same range', correct: false,",
     "why: 'Embryonic: most types of human cell. Bone marrow: many types, including blood cells, but fewer.', options: [\n            { text: 'Embryonic stem cells form more types than bone marrow ones', correct: true }, { text: 'Both kinds form exactly the same range of cells', correct: false,"),
    ("{ text: 'Bone marrow forms more types than embryonic', correct: false, reply: 'It is the other way round.' }, { text: 'Embryonic form only blood cells', correct: false,",
     "{ text: 'Bone marrow stem cells form more types than embryonic ones', correct: false, reply: 'It is the other way round.' }, { text: 'Embryonic stem cells form only blood cells', correct: false,"),
    # Rung 2 (ii): credited option visibly the longest (+27).
    ("{ text: 'Inject embryonic stem cells into it', correct: false, reply: 'Human embryonic stem cells make human cells.' },\n            { text: 'Give it a bone marrow transplant', correct: false, reply: 'Plants have no bone marrow.' }, { text: 'Remove its meristems', correct: false,",
     "{ text: 'Inject human embryonic stem cells into the orchid', correct: false, reply: 'Human embryonic stem cells make human cells.' },\n            { text: 'Give the orchid a bone marrow transplant', correct: false, reply: 'Plants have no bone marrow.' }, { text: 'Remove all of its meristems so it stops growing', correct: false,"),
    # Examiner, 26 Nov 2026: practice Q3 reply 2 used "a limited range"; the spec says "many types".
    ("2: 'Bone marrow stem cells form a limited range of human cells, including blood cells.'",
     "2: 'Bone marrow stem cells form many types of human cell, including blood cells, but not plant cells.'"),
    # Examiner, 26 Nov 2026: practice Q4, the credited option was the longest; one distractor lengthened.
    ("['The stem cells have no genes', false]", "['The stem cells have no genes in them at all', false]"),
]

LESSON = {
    "slug": "stem-cells",
    "start": {
        "setup": "A short cutting from a houseplant, stood in water, grows roots and becomes a whole new plant.",
        "question": "If you had to guess, could a piece of your arm grow into a whole new you?",
        "options": [
            ("Yes",
             "No. Most of our cells have already differentiated. Plants keep cells that can become "
             "any type of plant cell."),
            ("No",
             "No. Most of our cells have already differentiated. Plants keep cells that can become "
             "any type of plant cell."),
        ],
        "answer": 1,
    },
    "words": ["stem cell", "undifferentiated", "meristem", "therapeutic cloning"],
    "knowledge": [
        {"kind": "card", "title": "What a stem cell is",
         "body": ["A stem cell is an undifferentiated cell of an organism. It can give rise to many "
                  "more cells of the same type, and certain other cells can arise from it by "
                  "differentiation."]},
        {"kind": "reveal", "title": "Three sources of stem cells",
         "cols": ["Found in", "Can become"],
         "rows": [
             ("Embryonic stem cells", "Human embryos",
              "Most different types of human cell, once cloned and made to differentiate"),
             ("Adult stem cells", "Bone marrow",
              "Many types of cell, including blood cells, but fewer types than embryonic stem cells"),
             ("Meristem cells", "Plants, at the tips of roots and shoots",
              "Any type of plant cell, throughout the life of the plant"),
         ]},
        {"kind": "card", "title": "What stem cells do",
         "body": [{"points": [
             "In an embryo, stem cells divide and differentiate to form the different types of "
             "cell in the body.",
             "In adult animals, stem cells repair and replace cells, such as blood cells.",
             "In plants, meristems make new cells for growth throughout the plant's life.",
         ]}]},
        {"kind": "card", "title": "Treating disease",
         "body": ["Treatment with stem cells may be able to help conditions such as diabetes and "
                  "paralysis.",
                  "In therapeutic cloning, an embryo is produced with the same genes as the patient. "
                  "Stem cells from the embryo are not rejected by the patient's body, so they may be "
                  "used for medical treatment."]},
        {"kind": "reveal", "title": "Weighing up stem cell treatment",
         "cols": ["What to say"],
         "rows": [
             ("Benefits", "They may help conditions such as diabetes and paralysis. Cells from "
                          "therapeutic cloning are not rejected."),
             ("Practical risk", "Transfer of viral infection."),
             ("Objections", "Some people have ethical or religious objections, for example because "
                            "an embryo is destroyed."),
         ]},
        {"kind": "card", "title": "Cloning plants",
         "body": ["Stem cells from meristems can be used to produce clones of plants quickly and "
                  "economically.",
                  {"points": [
                      "Rare species can be cloned to protect them from extinction.",
                      "Crop plants with special features, such as disease resistance, can be cloned "
                      "to produce large numbers of identical plants for farmers.",
                  ]}]},
        {"kind": "card", "title": "Easy mistakes",
         "body": [{"mistakes": [
             ("Therapeutic cloning makes a baby copy of the patient.",
              "It makes an embryo only as a source of stem cells. No baby is produced."),
             ("Adult bone marrow stem cells can become any type of cell.",
              "They form many types, including blood cells, but fewer than embryonic stem cells."),
             ("Stem cells are already specialised.",
              "Stem cells are undifferentiated. They have not specialised yet."),
         ]}]},
    ],
    "key_fact": "A stem cell is an undifferentiated cell that can make more cells of the same type "
                "and can differentiate into other types. Embryonic stem cells can become most types "
                "of human cell, adult bone marrow stem cells form many types including blood cells, "
                "and meristem cells can become any type of plant cell throughout the plant's life.",
    "deeper": [
        {"kind": "card", "title": "Bone marrow transplants",
         "body": ["A bone marrow transplant gives a patient new stem cells that make blood cells, for "
                  "example to treat leukaemia, a cancer of the blood."]},
        {"kind": "card", "title": "What you do not need",
         "body": ["AQA does not ask how stem cells are grown or cloned in a laboratory."]},
        {"kind": "card", "title": "Command words",
         "body": [{"points": [
             "<strong>Describe</strong> where stem cells come from and what they can become.",
             "<strong>Compare</strong> embryonic and adult stem cells by the range of cells they "
             "form.",
             "<strong>Evaluate</strong>: the benefits, the risks and the objections, then your own "
             "judgement.",
         ]}]},
    ],
    "try": None,
    "legacy": {"batch": "batch-6", "logic_edits": LOGIC_EDITS},
}
