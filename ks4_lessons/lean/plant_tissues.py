# -*- coding: utf-8 -*-
"""Plant tissues, in the lean shape. Spec table: ks4-plant-tissues.md (AQA 8464 4.2.3.1 / 8461
4.2.3.1, word for word the same; no HT-only or Biology-only lines). Xylem and phloem are placed
in the leaf here, one line each; the transpiration stream is on Transpiration and the
xylem-against-phloem comparison is on Translocation (both 4.2.3.2).

LEGACY (batch 5). The ladder and the practice set stay from the Design page. The practice set is
the page's own hard-coded `bankSrc` (same five items on every route), so its fixes are
logic_edits. One practice-set stem is replaced ("Why are xylem cells dead?": not in the spec,
which says only "hollow tubes strengthened by lignin"), so that ks4q: id retires and a new one is
added; every other stem is kept. Rung prompts keep their positions, so rung ids survive.

The Design leaf figure (leafFig) labels only the one layer the bench had selected, so the lean
card asks for a fully labelled leaf section: fig:leaf-cross-section. plantFig's two meristem
labels ran past the right edge of the drawing; they are moved inside it.
"""


def _js(s):
    """This batch's logic is plain ASCII with \\uXXXX escapes: spell a target the way the file does."""
    # Every non-ASCII character as backslash-u + 4 lower-case hex, the way these logic files spell
    # them (backslashreplace gave \\xNN for U+0080-U+00FF: µ ° ÷ × would never match).
    return "".join(c if ord(c) < 128 else "\\u%04x" % ord(c) for c in s)


_EDITS = [
    # plantFig: both labels started near the right edge and ran past it (420 wide).
    ("b += D.T(232, 52, 'meristem at the shoot tip', 15, { anchor: 'start' });",
     "b += D.T(210, 32, 'meristem at the shoot tip', 15, { anchor: 'middle' });"),
    ("b += D.T(280, 340, 'meristem at root tips', 15, { anchor: 'start' });",
     "b += D.T(210, 354, 'meristem at the root tips', 15, { anchor: 'middle' });"),
    # Rung 1 Q2: credited option visibly the longest (+17).
    ("{ text: 'In the leaf veins', correct: false, reply: 'Veins hold xylem and phloem.' },",
     "{ text: 'In the veins of the leaves, with the xylem', correct: false, reply: 'Veins hold xylem and phloem.' },"),
    ("{ text: 'In the upper epidermis', correct: false, reply: 'The epidermis covers the leaf.' }] }",
     "{ text: 'In the upper epidermis of each leaf', correct: false, reply: 'The epidermis covers the leaf.' }] }"),
    # Rung 2 Q1: credited option visibly the longest (+16).
    ("{ text: 'So water can escape', correct: false,", "{ text: 'So water vapour can escape from the leaf', correct: false,"),
    ("{ text: 'So carbon dioxide can enter', correct: false,", "{ text: 'So carbon dioxide can enter the cells below', correct: false,"),
    # Rung 2 Q2: credited option visibly the longest (+28).
    ("{ text: 'It slows, because the stomata are blocked and less carbon dioxide enters', correct: true },",
     "{ text: 'It slows, as less carbon dioxide can enter', correct: true },"),
    # Rung 3 Q2: the chain tested "xylem cells are dead" (not in the spec; the spec says hollow
    # tubes strengthened by lignin), and two of its links could go in either order. Now one
    # causal chain. Same position, same id.
    ("links: ['Xylem cells are dead, with no contents.', 'They form hollow tubes, so water flows through without obstruction.', 'Lignin strengthens the walls, so the tubes don’t collapse.'],\n            herrings: [{ text: 'Xylem cells are living, so they can pump water.', why: 'Xylem is dead; phloem is the living tissue.' },",
     "links: ['The walls of the xylem tubes are strengthened by lignin.', 'So the hollow tubes do not collapse.', 'So water can keep flowing up from the roots to the leaves.'],\n            herrings: [{ text: 'Xylem cells pump the water up to the leaves.', why: 'Xylem is made of hollow tubes. Nothing in it pumps the water.' },"),
    # Practice Q1 (xylem), stem kept: dash tail; capitals in the replies.
    ("opts: [['Water and dissolved mineral ions — upwards from roots to leaves', true],",
     "opts: [['Water and mineral ions, from the roots to the leaves', true],"),
    ("wrong_explanations: { 1: 'Dissolved sugars = PHLOEM (translocation). Xylem carries water and minerals only.', 2: 'Oxygen diffuses through air spaces in the spongy mesophyll and out through stomata — it doesn’t travel in xylem.', 3: 'CO₂ diffuses through stomata into air spaces — it doesn’t travel in xylem.' }",
     "wrong_explanations: { 1: 'Phloem carries dissolved sugars.', 2: 'Oxygen leaves the leaf through the stomata. It does not travel in the xylem.', 3: 'Carbon dioxide enters through the stomata. It does not travel in the xylem.' }"),
    # Practice Q2 REPLACED (new stem, new id; the old id -> null): why xylem cells are dead is not
    # in the spec.
    ("{ q: 'Why are xylem cells dead?', opts: [['Dead cells have no contents — forming a completely hollow tube for water to flow through without obstruction', true], ['Xylem cells die because the lignin in their walls is toxic', false], ['Dead cells are lighter, helping water move upwards against gravity', false], ['Xylem cells die when the plant is no longer growing', false]],\n        wrong_explanations: { 1: 'Lignin is not toxic — it strengthens the walls. The cells die as part of their normal development, leaving behind a hollow lignified tube.', 2: 'Dead cell content doesn’t significantly change the weight of xylem — water moves upward due to the transpiration pull, not because of weight.', 3: 'Xylem cells die as they mature during normal development, regardless of whether the plant is actively growing — this is a programmed developmental process.' } },",
     "{ q: 'What strengthens the walls of the xylem tubes?', opts: [['Lignin', true], ['Chlorophyll', false], ['Starch', false], ['Mineral ions', false]],\n        wrong_explanations: { 1: 'Chlorophyll absorbs light, inside chloroplasts.', 2: 'Starch is a store of glucose.', 3: 'Mineral ions are carried in the xylem. They are not part of its walls.' } },"),
    # Practice Q3 (stomata), stem kept: credited option visibly the longest (+51), dash;
    # capitals in the replies.
    ("['Allow CO₂ in for photosynthesis and O₂ out — also allow water vapour to escape during transpiration', true]",
     "['Let carbon dioxide in, and oxygen and water vapour out', true]"),
    ("wrong_explanations: { 1: 'Stomata are pores for gas EXCHANGE, not water absorption: water enters the plant through the roots.', 2: 'The waxy cuticle is produced by the EPIDERMIS cells — it is a secreted layer, not produced by stomata.', 3: 'Glucose storage as starch happens in chloroplasts and other cells — stomata are pores for gas exchange.' }",
     "wrong_explanations: { 1: 'Water enters the plant through the roots.', 2: 'The epidermis makes the waxy cuticle.', 3: 'Stomata are pores for gases. They do not store anything.' }"),
    # Practice Q5 (palisade), stem kept: credited option visibly the longest (+14).
    ("['They need to be close to the stomata', false], ['They make the waxy cuticle', false],",
     "['They need to be close to the stomata to get carbon dioxide', false], ['They make the waxy cuticle on the upper surface', false],"),
]

LESSON = {
    "slug": "plant-tissues",
    "start": {
        "question": "If you had to guess, where in a leaf does most photosynthesis happen?",
        "options": [
            ("Near the top surface",
             "Near the top. The palisade mesophyll is just under the upper surface, where it gets "
             "the most light."),
            ("Near the bottom surface",
             "Near the top. The palisade mesophyll is just under the upper surface, where it gets "
             "the most light."),
        ],
        "answer": 0,
    },
    "words": ["epidermis", "palisade mesophyll", "spongy mesophyll", "meristem"],
    "knowledge": [
        {"kind": "card", "title": "The leaf is a plant organ",
         "body": ["The leaf is a plant organ. Its tissues work together for photosynthesis.",
                  {"slot": "fig:leaf-cross-section"},
                  "Plant tissues include epidermal tissues, palisade mesophyll, spongy mesophyll, "
                  "xylem and phloem, and meristem tissue."]},
        {"kind": "reveal", "title": "How each leaf tissue suits its job",
         "cols": ["Structure", "Function"],
         "rows": [
             ("Upper epidermis", "Thin, transparent cells, covered by a waxy cuticle",
              "Lets light through; the waxy cuticle reduces water loss"),
             ("Palisade mesophyll", "Tall cells near the upper surface, packed with chloroplasts",
              "Absorbs light for photosynthesis"),
             ("Spongy mesophyll", "Loosely packed cells with air spaces between them",
              "Lets gases diffuse to and from the cells"),
             ("Lower epidermis", "Has many stomata", "Lets carbon dioxide in, and oxygen and "
                                                     "water vapour out"),
             ("Guard cells", "A pair of cells around each stoma", "Open and close the stoma"),
             ("Xylem", "Hollow tubes strengthened by lignin",
              "Brings water and mineral ions into the leaf"),
             ("Phloem", "Tubes of elongated cells",
              "Carries dissolved sugars from the leaf to the rest of the plant"),
         ]},
        {"kind": "card", "title": "Meristem",
         "body": [{"slot": "legacy-fig:plantFig"},
                  "Meristem tissue is found at the growing tips of shoots and roots.",
                  "Its cells divide to make new cells, so the plant can grow. They can become any "
                  "type of plant cell, throughout the life of the plant."]},
        {"kind": "card", "title": "Easy mistakes",
         "body": [{"mistakes": [
             ("Stomata take in water.",
              "Stomata let gases in and out. Water enters through the roots."),
             ("Xylem carries sugar.",
              "Xylem carries water and mineral ions. Phloem carries dissolved sugars."),
             ("Most photosynthesis happens in the spongy mesophyll.",
              "Most happens in the palisade mesophyll, which gets the most light."),
         ]}]},
    ],
    "key_fact": "The leaf is a plant organ whose tissues suit their functions: the transparent "
                "epidermis lets light through, the palisade mesophyll is packed with chloroplasts "
                "for photosynthesis, the spongy mesophyll has air spaces for gas exchange, guard "
                "cells open and close the stomata, and xylem and phloem transport substances. "
                "Meristem tissue at the growing tips of shoots and roots makes new cells.",
    "deeper": [
        {"kind": "card", "title": "More about xylem and phloem",
         "body": ["How water moves up the xylem is on Transpiration. How the two tissues compare "
                  "is on Translocation."]},
        {"kind": "card", "title": "Command words",
         "body": [{"points": [
             "<strong>Describe</strong> a tissue: say what its cells are like and where it is.",
             "<strong>Explain</strong> an adaptation: the feature, then how it helps, such as "
             "\"air spaces, so carbon dioxide can diffuse to the cells\".",
             "<strong>Suggest</strong> an effect: use what each tissue does, such as stomata "
             "letting carbon dioxide in.",
         ]}]},
    ],
    "try": None,
    "legacy": {"batch": "batch-5", "logic_edits": [(_js(a), _js(b)) for a, b in _EDITS]},
}
