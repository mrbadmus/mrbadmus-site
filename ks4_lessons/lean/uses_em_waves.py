# -*- coding: utf-8 -*-
"""Uses and applications of electromagnetic waves, in the lean shape. LEGACY record: the Design
batch-4 page keeps its ladder (Ks4Practice) and its practice set, so their question ids survive.
Spec table: ks4-uses-em-waves.md (AQA 8464 6.6.2.4 / 8463 4.6.2.4, word for word the same).

The practice set is a hard-coded bank in the logic (`base`, and `hq` on Higher routes): every
item audited and correct, so no edit. xrayFig and satFig draw only on Higher routes (R.isHigher),
so they sit in the CH TH card. The eyebrow is the literal "AQA Physics 6.6.2.4" on every route:
lean_ks4's physics eyebrow rule makes it route-aware.

logic_edits:
  1. Rung 2 (ii): "Identify the wave usually used for each" with "(i) gamma rays (ii) X-rays"
     marked wrong. The spec gives X-rays and gamma rays BOTH for medical imaging and treatments,
     and gamma rays are also used to image bones, so the swapped option was arguable. The stem now
     asks for "a wave that can be used", and the swapped option is replaced by a definitely wrong
     one. Same rung position, same id.
  2. Rung 3 (sunbed chain): links 2 and 3 were two parallel effects, so two orders were right.
     Rewritten so each link follows from the one before.
  3. Rung 4 reject "Gamma rays: imaging broken bones" is creditworthy on this spec (X-rays and
     gamma rays: medical imaging). Replaced by a pairing that is definitely wrong."""

LESSON = {
    "slug": "uses-em-waves",
    "start": {
        "setup": "A TV remote control and a hospital X-ray machine both send out waves.",
        "question": "If you had to guess, are they the same kind of wave?",
        "options": [
            ("The same kind of wave",
             "The same kind. Both are electromagnetic waves: infrared from the remote, X-rays in "
             "the hospital."),
            ("Different kinds of wave",
             "The same kind. Both are electromagnetic waves: infrared from the remote, X-rays in "
             "the hospital."),
        ],
        "answer": 0,
    },
    "words": ["electromagnetic spectrum", "application", "fibre optics", "medical imaging"],
    "knowledge": [
        {"kind": "card", "title": "Every group has uses",
         "body": ["Electromagnetic waves have many practical applications.",
                  {"slot": "legacy-fig:spectrumFig"}]},
        {"kind": "reveal", "title": "The uses",
         "cols": ["Uses"],
         "rows": [
             ("Radio waves", "Television and radio"),
             ("Microwaves", "Satellite communications, cooking food"),
             ("Infrared", "Electrical heaters, cooking food, infrared cameras"),
             ("Visible light", "Fibre optic communications"),
             ("Ultraviolet", "Energy efficient lamps, sun tanning"),
             ("X-rays and gamma rays", "Medical imaging and treatments"),
         ]},
        {"kind": "card", "title": "Some uses carry risks",
         "body": [{"points": [
             "Sunbeds give out ultraviolet. It can make the skin age prematurely and increases "
             "the risk of skin cancer.",
             "X-rays and gamma rays are ionising radiation. They can cause the mutation of genes "
             "and cancer.",
             "A radiographer takes many X-rays each day, so they stand behind a screen to keep "
             "their own exposure low.",
         ]}]},
        {"kind": "card", "title": "Why each wave suits its job", "routes": ["CH", "TH"],
         "body": [{"points": [
             "<strong>Radio waves</strong>: an alternating current in a transmitter's aerial "
             "produces them, and they induce an alternating current in a receiver's aerial. So "
             "they can carry television and radio signals.",
             "<strong>Microwaves</strong>: they pass through the atmosphere, so they can reach "
             "satellites. Water molecules in food absorb them, which heats the food.",
             "<strong>Infrared</strong>: objects that absorb it get hotter, so it heats rooms and "
             "cooks food. Warm objects emit it, so an infrared camera can detect them.",
             "<strong>Visible light</strong>: it reflects along the inside of a thin glass fibre, "
             "so it can carry information.",
             "<strong>Ultraviolet</strong>: a coating inside an energy efficient lamp absorbs it "
             "and gives out visible light.",
             "<strong>X-rays</strong>: they pass through soft tissue but are absorbed by bone, so "
             "the bones show up on the image.",
             "<strong>Gamma rays</strong>: they are ionising, so a beam aimed at a tumour can kill "
             "the cancer cells.",
         ]},
             {"slot": "legacy-fig:satFig"},
             {"slot": "legacy-fig:xrayFig"}]},
        {"kind": "card", "title": "Easy mistakes",
         "body": [{"mistakes": [
             ("Fibre optic communications use X-rays.",
              "Fibre optic communications use visible light."),
             ("Microwave ovens use radio waves.",
              "Microwave ovens use microwaves."),
             ("An infrared camera detects visible light.",
              "It detects the infrared emitted by warm objects."),
         ]}]},
    ],
    "key_fact": "Each type of electromagnetic wave has practical uses: radio waves for television "
                "and radio; microwaves for satellite communications and cooking food; infrared for "
                "electrical heaters, cooking food and infrared cameras; visible light for fibre "
                "optic communications; ultraviolet for energy efficient lamps and sun tanning; "
                "X-rays and gamma rays for medical imaging and treatments.",
    "deeper": [
        {"kind": "card", "title": "Around the house",
         "body": [{"points": [
             "A TV remote control sends infrared signals to the television.",
             "A grill and a toaster cook food with infrared.",
             "Broadband through a fibre optic cable is carried by light.",
         ]}]},
        {"kind": "card", "title": "Command words",
         "body": [{"points": [
             "<strong>Give</strong> a use: name the wave and one application.",
             "<strong>Explain</strong> why a wave suits a job: say what the wave does, such as "
             "passing through or being absorbed, that makes it work.",
         ]}]},
    ],
    "try": None,
    "legacy": {
        "batch": "batch-4",
        "logic_edits": [
            ("Identify the wave usually used for each.", "Identify a wave that can be used for each."),
            ("{ text: '(i) gamma rays (ii) X-rays', correct: false, reply: 'Swapped. X-rays image "
             "bones; gamma rays treat tumours.' },",
             "{ text: '(i) visible light (ii) radio waves', correct: false, reply: 'Neither is used "
             "here. X-rays and gamma rays are used for medical imaging and treatments.' },"),
            ("links: ['Sunbeds give out ultraviolet, which is absorbed by the skin.', 'Ultraviolet "
             "can make the skin age prematurely.', 'It also increases the risk of skin cancer.'],",
             "links: ['Sunbeds give out ultraviolet.', 'The ultraviolet is absorbed by the skin.', "
             "'This can make the skin age prematurely, and increases the risk of skin cancer.'],"),
            ("Gamma rays: imaging broken bones.", "Ultraviolet: imaging broken bones."),
            # Examiner (EXAMINER.md) MUST/SHOULD fixes, applied after the record's own edits.
            ("['Ultraviolet can make skin age prematurely and increases the risk of skin cancer', true]",
             "['Ultraviolet increases the risk of skin cancer', true]"),
            ("['Energy efficient lamps', false]",
             "['Energy efficient lamps and sun tanning', false]"),
            ("2: 'Energy efficient lamps use ultraviolet.'",
             "2: 'Energy efficient lamps and sun tanning use ultraviolet.'"),
            ("['They are absorbed by water molecules in the food, transferring energy to its thermal store', true]",
             "['Water molecules in the food absorb them', true]"),
            ("['A coating inside the lamp absorbs the ultraviolet and gives out visible light', true]",
             "['A coating absorbs it and gives out visible light', true]"),
            ("['X-ray', 'imaging'], ['Gamma', 'treatment']",
             "['X-ray', 'imaging, treatment'], ['Gamma', 'imaging, treatment']"),
            ('and tanning; X-rays for imaging; gamma rays for treatment.',
             'and tanning; X-rays and gamma rays for medical imaging and treatments.'),
            # Blind-pass fixes (blind/RESULT.md), applied after the edits above.
            ("'Ionising radiation can cause the mutation of genes and cancer.'",
             "'So they can cause the mutation of genes and cancer.'"),
        ],
    },
}
