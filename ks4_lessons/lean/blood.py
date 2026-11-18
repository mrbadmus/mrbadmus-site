# -*- coding: utf-8 -*-
"""Blood, in the lean shape. Spec table: ks4-blood.md (AQA 8464 4.2.2.3 / 8461 4.2.2.3, word for word
the same; no HT-only or Biology-only lines). The white blood cells' three defences are 4.3.1.6
content: one line each here.

LEGACY (batch 4). The ladder and the practice set stay from the Design page. The practice set is
the page's own hard-coded `bankSrc` (same five items on every route), so its fixes are
logic_edits. One practice-set stem is replaced ("Which substance does plasma NOT transport?":
a little oxygen does dissolve in plasma, so the item was arguable), so that ks4q: id retires and a
new one is added; every other stem is kept. Rung prompts keep their positions, so rung ids survive.
"""


def _js(s):
    """This batch's logic is plain ASCII with \\uXXXX escapes: spell a target the way the file does."""
    # Every non-ASCII character as backslash-u + 4 lower-case hex, the way these logic files spell
    # them (backslashreplace gave \\xNN for U+0080-U+00FF: µ ° ÷ × would never match).
    return "".join(c if ord(c) < 128 else "\\u%04x" % ord(c) for c in s)


_EDITS = [
    # Rung 2 Q1: credited option visibly the longest (+14).
    ("{ text: 'Phagocyte (white blood cell)', correct: true },",
     "{ text: 'Phagocyte', correct: true },"),
    # Rung 3 Q1 herring: "no nucleus so they can squeeze through capillaries" is not definitely
    # wrong (its own reply conceded it). Replaced by one that is.
    ("{ text: 'They have no nucleus so they can squeeze through capillaries.', why: 'The examined reason is more room for haemoglobin.' }",
     "{ text: 'They have a large nucleus to control the haemoglobin.', why: 'Red blood cells have no nucleus.' }"),
    # Practice Q1 (no nucleus), stem kept: credited option the longest, dash; "squeeze through
    # capillaries" and "reduce their weight" were not definitely wrong. Replaced.
    ("opts: [['To create more space for haemoglobin — allowing the cell to carry more oxygen', true], ['So they can divide and replace themselves when worn out', false], ['To reduce their weight so they flow faster through blood vessels', false], ['So they can squeeze through capillaries more easily', false]],",
     "opts: [['So there is more room for haemoglobin, to carry more oxygen', true], ['So they can divide and replace themselves when worn out', false], ['So they can make more haemoglobin for themselves', false], ['So they can engulf pathogens more easily', false]],"),
    ("wrong_explanations: { 1: 'Cells without a nucleus CANNOT divide — red blood cells are produced in bone marrow and cannot reproduce themselves.', 2: 'Weight difference between a nucleus and haemoglobin molecules is negligible — the primary reason is space for haemoglobin.', 3: 'Flexibility helps red blood cells squeeze through capillaries — but this is a result of their biconcave shape and flexibility, not the absence of a nucleus.' }",
     "wrong_explanations: { 1: 'A cell with no nucleus cannot divide.', 2: 'A cell with no nucleus cannot make new proteins, such as haemoglobin.', 3: 'Phagocytes, a type of white blood cell, engulf pathogens.' }"),
    # Practice Q2 (few lymphocytes), stem kept: credited option visibly the longest (+34), dash
    # tails, "severe anaemia" (not in the spec), capitals.
    ("opts: [['Unable to produce specific antibodies — prolonged or repeated infections that are hard to clear', true], ['Unable to carry oxygen — severe anaemia', false], ['Blood will not clot properly — excessive bleeding from wounds', false], ['Unable to digest food properly — nutrients not absorbed', false]],",
     "opts: [['It makes fewer antibodies, so infections last longer', true], ['It cannot carry enough oxygen around the body', false], ['Its blood will not clot properly after a cut', false], ['It cannot digest its food properly', false]],"),
    ("wrong_explanations: { 1: 'Oxygen carrying = RED BLOOD CELLS using haemoglobin. Lymphocytes are white blood cells.', 2: 'Blood clotting = PLATELETS forming a fibrin mesh. Lymphocytes produce antibodies, not clotting factors.', 3: 'Food digestion = digestive enzymes in the gut. Lymphocytes are part of the immune system.' }",
     "wrong_explanations: { 1: 'Red blood cells carry oxygen. Lymphocytes are white blood cells.', 2: 'Platelets help the blood to clot.', 3: 'Digestive enzymes digest food. Lymphocytes help defend the body against pathogens.' }"),
    # Practice Q3 (platelets), stem kept: credited option visibly the longest (+47), "fibrin mesh"
    # (beyond the spec), capitals in the replies.
    ("['Blood clotting — they clump at wound sites and trigger fibrin mesh formation to seal the damage', true]",
     "['Helping the blood to clot at a wound', true]"),
    ("wrong_explanations: { 1: 'Oxygen transport = RED BLOOD CELLS using haemoglobin.', 2: 'Producing antibodies = LYMPHOCYTES (a type of white blood cell).', 3: 'Engulfing bacteria = PHAGOCYTES (a type of white blood cell).' }",
     "wrong_explanations: { 1: 'Red blood cells carry oxygen.', 2: 'Lymphocytes, a type of white blood cell, produce antibodies.', 3: 'Phagocytes, a type of white blood cell, engulf bacteria.' }"),
    # Practice Q4 REPLACED (new stem, new id; the old id -> null): "Which substance does plasma
    # NOT transport? Oxygen" was arguable (some oxygen dissolves in plasma), and a reply was A level
    # (bicarbonate ions).
    ("{ q: 'Which substance does plasma NOT transport?', opts: [['Oxygen — this is carried by haemoglobin inside red blood cells', true], ['Glucose from the small intestine to body cells', false], ['Urea from the liver to the kidneys', false], ['Carbon dioxide from respiring cells to the lungs', false]],\n        wrong_explanations: { 1: 'Glucose IS carried in plasma — after absorption from the small intestine.', 2: 'Urea IS carried in plasma — from the liver to the kidneys for excretion.', 3: 'Carbon dioxide IS dissolved in plasma — most CO₂ travels as bicarbonate ions dissolved in plasma.' } },",
     "{ q: 'What is plasma?', opts: [['The liquid in which the blood cells are suspended', true], ['A type of white blood cell', false], ['The red pigment that carries oxygen', false], ['A tiny fragment of a cell that helps clotting', false]],\n        wrong_explanations: { 1: 'White blood cells are cells. Plasma is the liquid part of blood.', 2: 'Haemoglobin is the red pigment, inside red blood cells.', 3: 'That is a platelet.' } },"),
    # Practice Q5 (antitoxins), stem kept: credited option the longest (+10).
    ("['Carry oxygen to infected tissue', false]", "['Carry extra oxygen to the infected tissue', false]"),
]

# Examiner pass (EXAMINER.md) and blind pass, 18 Nov 2026. Each old string is the logic AFTER the
# edits above, and occurs exactly once (validate.py checks).
_EDITS += [
    ("links: ['They contain haemoglobin, which binds oxygen in the lungs and releases it in the tissues.', 'They have no nucleus, so there is more room for haemoglobin.', 'Their biconcave shape gives a large surface area for oxygen to diffuse in and out.'],",
     "links: ['Red blood cells have no nucleus.', 'So there is more room inside them for haemoglobin.', 'More haemoglobin binds more oxygen in the lungs, to release in the tissues.'],"),
    ("links: ['Phagocytes engulf pathogens and digest them.', 'Lymphocytes produce antibodies that target a particular pathogen.', 'Some white blood cells produce antitoxins, which neutralise toxins released by bacteria.'],",
     "links: ['A white blood cell called a phagocyte reaches a pathogen.', 'The phagocyte engulfs the pathogen.', 'It digests the pathogen, so the pathogen is destroyed.'],"),
    ("opts: [['It makes fewer antibodies, so infections last longer', true], ['It cannot carry enough oxygen around the body', false], ['Its blood will not clot properly after a cut', false], ['It cannot digest its food properly', false]],",
     "opts: [['They make fewer antibodies against pathogens', true], ['They cannot carry enough oxygen around the body', false], ['Their blood will not clot properly after a cut', false], ['They cannot digest their food properly', false]],"),
]

LESSON = {
    "slug": "blood",
    "start": {
        "setup": "Blood looks like a red liquid.",
        "question": "If you had to guess, what makes it red?",
        "options": [
            ("Red cells floating in a pale liquid",
             "Red blood cells make it red. They are suspended in plasma, which is a pale yellow "
             "liquid."),
            ("The liquid itself is red",
             "Red blood cells make it red. They are suspended in plasma, which is a pale yellow "
             "liquid."),
        ],
        "answer": 0,
    },
    "words": ["plasma", "haemoglobin", "white blood cell", "platelets"],
    "knowledge": [
        {"kind": "card", "title": "Blood is a tissue",
         "body": ["Blood is a tissue consisting of plasma, in which the red blood cells, white "
                  "blood cells and platelets are suspended."]},
        {"kind": "reveal", "title": "The four components",
         "cols": ["Function"],
         "rows": [
             ("Plasma", "Transports the blood cells and dissolved substances, such as glucose, "
                        "carbon dioxide, urea and hormones"),
             ("Red blood cells", "Carry oxygen from the lungs to the cells of the body"),
             ("White blood cells", "Defend the body against pathogens"),
             ("Platelets", "Help the blood to clot at a wound"),
         ]},
        {"kind": "card", "title": "Red blood cells",
         "body": [{"slot": "legacy-fig:rbcFig"},
                  {"points": [
                      "They contain haemoglobin, which binds to oxygen in the lungs and releases "
                      "it in the tissues.",
                      "They have no nucleus, so there is more room for haemoglobin.",
                      "Their biconcave disc shape gives a large surface area for oxygen to "
                      "diffuse in and out.",
                  ]}]},
        {"kind": "card", "title": "White blood cells",
         "body": ["White blood cells have a nucleus. They defend the body in three ways.",
                  {"points": [
                      "Some engulf pathogens and digest them. This is phagocytosis.",
                      "Some produce antibodies.",
                      "Some produce antitoxins, which neutralise toxins released by bacteria.",
                  ]},
                  "How these defences work is on Infection and response."]},
        {"kind": "card", "title": "Recognising blood cells",
         "body": ["A drawing of blood seen under a microscope.",
                  {"slot": "legacy-fig:smearFig"}]},
        {"kind": "reveal", "title": "The cells in the drawing",
         "cols": ["What it looks like", "What it is"],
         "rows": [
             ("A", "A small disc with a pale centre and no nucleus. The most common cell.",
              "Red blood cell"),
             ("B", "Larger, with a nucleus in several lobes", "Phagocyte, a white blood cell"),
             ("C", "Almost filled by one large round nucleus", "Lymphocyte, a white blood cell"),
             ("D", "Tiny fragments with no nucleus", "Platelets"),
         ]},
        {"kind": "card", "title": "Easy mistakes",
         "body": [{"mistakes": [
             ("Plasma carries the oxygen.",
              "Red blood cells carry oxygen, bound to haemoglobin."),
             ("Platelets are a type of white blood cell.",
              "Platelets are fragments of cells that help the blood to clot."),
             ("Most blood cells are white blood cells.",
              "Red blood cells are by far the most common."),
         ]}]},
    ],
    "key_fact": "Blood is a tissue consisting of plasma, in which the red blood cells, white blood "
                "cells and platelets are suspended. Red blood cells carry oxygen, white blood cells "
                "defend the body against pathogens, platelets help the blood to clot, and plasma "
                "transports the cells and dissolved substances.",
    "deeper": [
        {"kind": "card", "title": "Seeing blood cells yourself",
         "body": ["A thin smear of blood, stained and looked at under a light microscope, shows "
                  "the cells in the drawing. The stain makes the nuclei of the white blood cells "
                  "show up."]},
        {"kind": "card", "title": "Command words",
         "body": [{"points": [
             "<strong>Give</strong> a function: one component, one job.",
             "<strong>Identify</strong> a cell in a photograph: use its size and its nucleus.",
             "<strong>Explain</strong> an adaptation: the feature, then how it helps, such as "
             "\"no nucleus, so more room for haemoglobin\".",
         ]}]},
    ],
    "try": None,
    "legacy": {"batch": "batch-4", "logic_edits": [(_js(a), _js(b)) for a, b in _EDITS]},
}
