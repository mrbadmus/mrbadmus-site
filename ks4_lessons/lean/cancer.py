# -*- coding: utf-8 -*-
"""Cancer, in the lean shape. Spec table: ks4-cancer.md (AQA 8464 4.2.2.7 / 8461 4.2.2.7, word for
word the same; no HT-only or Biology-only lines). Carcinogens and ionising radiation are 4.2.2.6
(Health, disease and risk factors): one line and a link here.

LEGACY (batch 6). The ladder and the practice set stay from the Design page. The practice set is
the page's own hard-coded `bankSrc` (same five items on every route), so its fixes are
logic_edits. One practice-set stem is replaced ("How does UV radiation cause skin cancer?": the
mutation mechanism is beyond the spec, and a distractor was partly true), so that ks4q: id retires
and a new one is added; every other stem is kept. Rung prompts keep their positions, so rung ids
survive.

tumourFig was a four-step stepper on the Design page; the lean page has no stepper, so it is
drawn at its last step (both tumours complete, the secondary tumour formed).
"""


def _js(s):
    """This batch's logic is plain ASCII with \\uXXXX escapes: spell a target the way the file does."""
    # Every non-ASCII character as backslash-u + 4 lower-case hex, the way these logic files spell
    # them (backslashreplace gave \\xNN for U+0080-U+00FF: µ ° ÷ × would never match).
    return "".join(c if ord(c) < 128 else "\\u%04x" % ord(c) for c in s)


_EDITS = [
    ("tumourFig: ready ? K.fig(this.fig(s.step), '') : null,",
     "tumourFig: ready ? K.fig(this.fig(3), '') : null,"),
    # Rung 1 Q1: credited option visibly the longest (+17).
    ("{ text: 'An infection by bacteria', correct: false, reply: 'Cancer is non-communicable.' }, { text: 'Cells dying too quickly', correct: false, reply: 'Cells divide too much, forming a tumour.' }",
     "{ text: 'An infection by bacteria passed between people', correct: false, reply: 'Cancer is non-communicable.' }, { text: 'Cells dying too quickly to be replaced', correct: false, reply: 'Cells divide too much, forming a tumour.' }"),
    # Rung 2 Q2: credited option visibly the longest (+21).
    ("{ text: 'A malignant lung tumour has spread and formed a secondary tumour', correct: true }, { text: 'A benign tumour has grown in the liver', correct: false,",
     "{ text: 'Cells from a lung tumour spread and formed a secondary tumour', correct: true }, { text: 'A benign tumour has grown inside the liver itself', correct: false,"),
    ("{ text: 'The liver has caught cancer from the lung', correct: false,",
     "{ text: 'The liver has caught cancer from the lung next to it', correct: false,"),
    # Rung 3 Q2 herring: "Benign tumours are caused by a virus" is true of some (warts), so it was
    # not definitely wrong. Replaced.
    ("{ text: 'Benign tumours are caused by a virus.', why: 'Cause doesn’t decide benign or malignant.' }",
     "{ text: 'Benign tumours are made of normal cells.', why: 'They are growths of abnormal cells.' }"),
    # Practice Q1 (benign v malignant), stem kept: credited option visibly the longest (+26);
    # "grow faster" was not definitely wrong; the chemotherapy option and replies were off spec.
    ("opts: [['Benign tumours stay in one place. Malignant tumours spread to other parts of the body (metastasis).', true], ['Benign tumours grow faster than malignant tumours.', false], ['Malignant tumours are caused by lifestyle; benign tumours are genetic.', false], ['Benign tumours require chemotherapy; malignant tumours only need surgery.', false]],",
     "opts: [['Benign tumours stay in one area. Malignant tumours spread to other parts of the body.', true], ['Benign tumours spread more slowly than malignant tumours.', false], ['Malignant tumours are caused by lifestyle; benign tumours are genetic.', false], ['Malignant tumours are always contained within a membrane.', false]],"),
    ("wrong_explanations: { 1: 'Malignant tumours typically grow FASTER and spread — benign tumours tend to grow more slowly and stay localised.', 2: 'Both types can have genetic or lifestyle causes — the distinction is about whether the tumour SPREADS, not its cause.', 3: 'This is the wrong way round — surgery is often used for localised (benign or early malignant) tumours. Chemotherapy is used for cancer that has spread.' }",
     "wrong_explanations: { 1: 'Benign tumours do not spread at all.', 2: 'Both can have genetic or lifestyle risk factors. The difference is whether the tumour spreads.', 3: 'Benign tumours are usually within a membrane. Malignant tumours invade neighbouring tissues.' }"),
    # Practice Q2 REPLACED (new stem, new id; the old id -> null): the UV mutation mechanism is
    # beyond the spec, and "reduces the immune system's ability" was partly true.
    ("{ q: 'How does UV radiation cause skin cancer?', opts: [['UV radiation damages DNA in skin cells — causing mutations in genes that control cell division', true], ['UV radiation directly kills healthy skin cells, forcing the body to replace them rapidly', false], ['UV radiation heats skin cells above their optimum temperature, causing them to mutate', false], ['UV radiation reduces the immune system’s ability to detect and destroy abnormal cells', false]],\n        wrong_explanations: { 1: 'UV radiation doesn’t kill healthy cells en masse — it damages DNA specifically. Rapid replacement due to damage is related to wound healing, not cancer.', 2: 'UV radiation doesn’t work by heat — it carries photons that directly interact with and damage DNA molecules.', 3: 'UV radiation can slightly suppress immunity, but the primary cancer-causing mechanism is direct DNA mutation in skin cells.' } },",
     "{ q: 'A tumour is contained in one area, inside a membrane. What type of tumour is it?', opts: [['Benign', true], ['Malignant', false], ['Secondary', false], ['Cancerous', false]],\n        wrong_explanations: { 1: 'Malignant tumours invade neighbouring tissues.', 2: 'A secondary tumour forms when malignant cells spread.', 3: 'A tumour contained in one area is benign, and benign tumours are not cancer.' } },"),
    # Practice Q3 (result of), stem kept: credited option visibly the longest (+23).
    ("['Catching a pathogen from another person', false], ['Cells stopping dividing altogether', false], ['Too few cells in a tissue', false]],",
     "['Catching a pathogen from another person who has cancer', false], ['Cells stopping dividing altogether, so a tissue shrinks', false], ['Too few cells being made to repair a tissue', false]],"),
    # Practice Q5 (genetic risk factor), stem kept: credited option visibly the longest (+22).
    ("opts: [['Inheriting a faulty gene from a parent', true], ['Smoking', false], ['Using sunbeds', false], ['Drinking alcohol', false]],",
     "opts: [['Inheriting a faulty gene', true], ['Smoking cigarettes every day', false], ['Using sunbeds often', false], ['Drinking a lot of alcohol', false]],"),
]

# Examiner pass (EXAMINER.md) and blind pass, 18 Nov 2026. Each old string is the logic AFTER the
# edits above, and occurs exactly once (validate.py checks).
_EDITS += [
    ("{ text: 'Cells from a lung tumour spread and formed a secondary tumour', correct: true }",
     "{ text: 'Lung tumour cells spread, forming a secondary tumour', correct: true }"),
    ("[['Benign tumours stay in one area. Malignant tumours spread to other parts of the body.', true],",
     "[['Benign tumours stay in one area; malignant tumours spread.', true],"),
    ("D.T(750, 300, 'secondary tumour', 13, { fill: C.red })",
     "D.T(792, 300, 'secondary tumour', 13, { fill: C.red, anchor: 'end' })"),
]

LESSON = {
    "slug": "cancer",
    "start": {
        "question": "If you had to guess, can every tumour spread to other parts of the body?",
        "options": [
            ("Yes, every tumour can",
             "Only some. Malignant tumours spread to other parts of the body. Benign tumours stay "
             "in one area."),
            ("No, only some can",
             "Only some. Malignant tumours spread to other parts of the body. Benign tumours stay "
             "in one area."),
        ],
        "answer": 1,
    },
    "words": ["tumour", "benign", "malignant", "secondary tumour"],
    "knowledge": [
        {"kind": "card", "title": "What cancer is",
         "body": ["Cancer is the result of changes in cells that lead to uncontrolled growth and "
                  "division.",
                  "A mass of cells formed this way is a tumour."]},
        {"kind": "card", "title": "Benign and malignant tumours",
         "body": [{"slot": "legacy-fig:tumourFig"},
                  {"points": [
                      "Benign tumours are growths of abnormal cells which are contained in one "
                      "area, usually within a membrane. They do not invade other parts of the "
                      "body.",
                      "Malignant tumour cells are cancers. They invade neighbouring tissues and "
                      "spread to different parts of the body in the blood, where they form "
                      "secondary tumours.",
                  ]},
                  "A benign tumour is not cancer, but it can still cause problems if it presses "
                  "on an organ."]},
        {"kind": "reveal", "title": "Comparing the two",
         "cols": ["Benign", "Malignant"],
         "rows": [
             ("Where it grows", "Contained in one area, usually within a membrane",
              "Invades neighbouring tissues"),
             ("Spreading", "Does not spread", "Spreads in the blood, forming secondary tumours"),
             ("Cancer", "Not cancer", "Cancer"),
         ]},
        {"kind": "card", "title": "Risk factors for cancer",
         "body": ["Scientists have identified lifestyle risk factors for various types of cancer. "
                  "There are also genetic risk factors for some cancers.",
                  {"points": [
                      "Lifestyle: smoking and lung cancer; ultraviolet from the sun or sunbeds and "
                      "skin cancer; drinking a lot of alcohol and liver cancer.",
                      "Genetic: inheriting certain faulty genes increases the risk of some "
                      "cancers, such as some breast cancers.",
                  ]},
                  "Carcinogens are substances that can cause cancer. They, and ionising "
                  "radiation, are in the lesson Health, disease and risk factors."]},
        {"kind": "card", "title": "Easy mistakes",
         "body": [{"mistakes": [
             ("All tumours are cancer.", "Only malignant tumours are cancer."),
             ("Benign tumours spread slowly.", "Benign tumours do not spread at all."),
             ("You can catch cancer from another person.",
              "Cancer is non-communicable. It cannot be caught."),
         ]}]},
    ],
    "key_fact": "Cancer is the result of changes in cells that lead to uncontrolled growth and "
                "division. Benign tumours are contained in one area and do not invade other parts "
                "of the body; malignant tumour cells are cancers, which invade neighbouring tissues "
                "and spread in the blood to form secondary tumours.",
    "deeper": [
        {"kind": "card", "title": "Metastasis",
         "body": ["Doctors call the spread of cancer cells to form secondary tumours metastasis."]},
        {"kind": "card", "title": "Command words",
         "body": [{"points": [
             "<strong>Compare</strong> tumours: say how they are alike, then give the "
             "differences, using \"benign tumours … whereas malignant tumours …\".",
             "<strong>Describe</strong> how cancer spreads: invades tissues, spreads in the "
             "blood, forms secondary tumours.",
             "<strong>Identify</strong> a tumour from information: say whether it stays in one "
             "area or spreads.",
         ]}]},
    ],
    "try": None,
    "legacy": {"batch": "batch-6", "logic_edits": [(_js(a), _js(b)) for a, b in _EDITS]},
}
