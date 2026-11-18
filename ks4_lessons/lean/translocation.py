# -*- coding: utf-8 -*-
"""Translocation, in the lean shape. Spec table: ks4-translocation.md (AQA 8464 4.2.3.2 / 8461
4.2.3.2, word for word the same; no HT-only or Biology-only lines). This lesson owns translocation
and the xylem-against-phloem comparison; the transpiration stream and root hair cells are on
Transpiration (the same spec point). "The detailed structure of phloem tissue or the mechanism of
transport is not required."

LEGACY (batch 6). The ladder and the practice set stay from the Design page. The practice set is
the page's own hard-coded `bankSrc` (same five items on every route), so its fixes are
logic_edits. No practice-set stem is edited, so every ks4q: id survives; rung prompts keep their
positions, so rung ids survive. "Sucrose" and "dead cells" leave the options: the spec says
"dissolved sugars" and "hollow tubes strengthened by lignin". tubeFig keeps its "dead" label as
the one gloss.
"""


def _js(s):
    """This batch's logic is plain ASCII with \\uXXXX escapes: spell a target the way the file does."""
    # Every non-ASCII character as backslash-u + 4 lower-case hex, the way these logic files spell
    # them (backslashreplace gave \\xNN for U+0080-U+00FF: µ ° ÷ × would never match).
    return "".join(c if ord(c) < 128 else "\\u%04x" % ord(c) for c in s)


_EDITS = [
    # Rung 1 Q2: credited option visibly the longest (+13).
    ("{ text: 'Loss of water from the leaves', correct: false, reply: 'That is transpiration.' }",
     "{ text: 'Loss of water vapour from the leaves', correct: false, reply: 'That is transpiration.' }"),
    ("{ text: 'Movement of water up the xylem', correct: false, reply: 'That is the transpiration stream.' }",
     "{ text: 'Movement of water up through the xylem', correct: false, reply: 'That is the transpiration stream.' }"),
    # Rung 2 Q1: "xylem cells are dead" is beyond the spec; the reply and the why are reworded.
    ("why: 'Hollow tubes of dead cells (no end walls), or walls strengthened by lignin.'",
     "why: 'Xylem is hollow tubes, with walls strengthened by lignin.'"),
    ("{ text: 'Many chloroplasts', correct: false, reply: 'Xylem cells are dead.' }",
     "{ text: 'Many chloroplasts', correct: false, reply: 'Chloroplasts are for photosynthesis, not for carrying water.' }"),
    # Rung 2 Q2: credited option visibly the longest (+13).
    ("{ text: 'Water can no longer reach the roots', correct: false,",
     "{ text: 'Water can no longer travel down to the roots', correct: false,"),
    ("{ text: 'The leaves can no longer make sugar', correct: false,",
     "{ text: 'The leaves above the ring can no longer make sugar', correct: false,"),
    # Rung 4 point: said in the spec's words.
    ("'Xylem is hollow tubes of dead cells strengthened by lignin; phloem is elongated living cells.'",
     "'Xylem is hollow tubes strengthened by lignin; phloem is tubes of elongated cells.'"),
    # Practice Q1 (phloem), stem kept: "sucrose" (the spec says dissolved sugars), dash tails,
    # capitals in the replies.
    ("opts: [['Sucrose (dissolved sugar) — from leaves to other parts of the plant', true], ['Water and dissolved mineral ions — from roots to leaves', false], ['Oxygen produced by photosynthesis', false], ['Carbon dioxide for use in photosynthesis', false]],",
     "opts: [['Dissolved sugars', true], ['Water and mineral ions', false], ['Oxygen from photosynthesis', false], ['Carbon dioxide for photosynthesis', false]],"),
    ("wrong_explanations: { 1: 'Water and minerals = XYLEM transport (transpiration stream). Phloem carries sugars.', 2: 'Oxygen diffuses through air spaces and out through stomata — it is not transported in phloem.', 3: 'CO₂ diffuses through stomata into the leaf — it is not transported in phloem.' }",
     "wrong_explanations: { 1: 'Xylem carries water and mineral ions.', 2: 'Oxygen leaves the leaf through the stomata. It is not carried in the phloem.', 3: 'Carbon dioxide enters through the stomata. It is not carried in the phloem.' }"),
    # Practice Q2 (direction), stem kept: credited option visibly the longest (+16), dash tails,
    # capitals.
    ("opts: [['Both upwards and downwards — from source (leaves) to any sink where sugar is needed', true], ['Upwards only — like the transpiration stream in xylem', false], ['Downwards only — gravity pulls the sugar solution down to the roots', false], ['Outwards only — from the centre of the stem to the leaf surfaces', false]],",
     "opts: [['Up and down, to wherever the sugars are needed', true], ['Upwards only, like water in the xylem', false], ['Downwards only, pulled by gravity to the roots', false], ['Outwards only, from the stem to the leaf surfaces', false]],"),
    ("wrong_explanations: { 1: 'Upwards only = TRANSPIRATION in XYLEM. Translocation in phloem moves in both directions depending on where the sink is.', 2: 'If translocation were downwards only, growing shoot tips at the top of the plant could never receive sugars — but they clearly do.', 3: 'Translocation moves along the length of the plant (up and down), not outwards from centre to leaf surface.' }",
     "wrong_explanations: { 1: 'Water in the xylem moves upwards. Phloem carries sugars up or down.', 2: 'Growing tips at the top of the plant also receive sugars.', 3: 'Translocation moves sugars along the plant, up or down.' }"),
    # Practice Q3 (sink), stem kept: credited option visibly the longest (+30), dash tails,
    # capitals.
    ("opts: [['Any part of the plant where sugars are used or stored — e.g. roots, fruits, growing tips', true], ['The leaves — where sugars are produced by photosynthesis', false], ['The phloem vessels that transport sugars through the plant', false], ['The stomata — where water and gases are exchanged', false]],",
     "opts: [['Any part of the plant where sugars are used or stored', true], ['The leaves, where sugars are made by photosynthesis', false], ['The phloem tubes that carry the sugars', false], ['The stomata, where gases are exchanged', false]],"),
    ("wrong_explanations: { 1: 'The leaves are the SOURCE — where sugars are MADE. A sink is the DESTINATION where sugars are used or stored.', 2: 'The phloem is the VESSEL — not the destination. Sinks are the organs that USE or STORE the sugars.', 3: 'Stomata are gas exchange pores — they have no role in the source-sink relationship of translocation.' }",
     "wrong_explanations: { 1: 'The leaves are where the sugars are made. A sink is where they are used or stored.', 2: 'The phloem carries the sugars to the sink.', 3: 'Stomata are pores for gas exchange.' }"),
    # Practice Q5 (difference), stem kept: credited option visibly the longest (+27), and it
    # tested "dead" and "living" (beyond the spec).
    ("opts: [['Xylem is hollow tubes of dead cells; phloem is elongated living cells', true], ['Xylem carries sugar; phloem carries water', false], ['Xylem moves both ways; phloem only upwards', false], ['Only phloem is found in the stem', false]],",
     "opts: [['Xylem carries water; phloem carries dissolved sugars', true], ['Xylem carries sugar; phloem carries water', false], ['Xylem moves both ways; phloem only upwards', false], ['Only phloem is found in the stems of plants', false]],"),
]

# Examiner pass (EXAMINER.md) and blind pass, 18 Nov 2026. Each old string is the logic AFTER the
# edits above, and occurs exactly once (validate.py checks).
_EDITS += [
    ("{ text: 'Walls strengthened by lignin', correct: true }",
     "{ text: 'Lignin in the walls', correct: true }"),
    ("[['Xylem carries water; phloem carries dissolved sugars', true],",
     "[['Xylem carries water; phloem carries sugars', true],"),
    ("if (k === 'root') b +=",
     "if (k === 'root' || k === 'all') b +="),
    ("if (k === 'fruit') b +=",
     "if (k === 'fruit' || k === 'all') b +="),
    ("if (k === 'tip') b +=",
     "if (k === 'tip' || k === 'all') b +="),
    ("SINKS.filter((x) => x.k === k)[0].label.toLowerCase() + '.'",
     "(k === 'all' ? 'growing tip, the fruit and the storage root' : SINKS.filter((x) => x.k === k)[0].label.toLowerCase()) + '.'"),
    ("plantFig: ready ? K.fig(this.plantFig(s.sink), '') : null,",
     "plantFig: ready ? K.fig(this.plantFig('all'), '') : null,"),
]

LESSON = {
    "slug": "translocation",
    "start": {
        "setup": "A potato is a swollen underground stem, full of starch.",
        "question": "If you had to guess, where was the sugar for that starch made?",
        "options": [
            ("In the leaves",
             "In the leaves, by photosynthesis. It was carried down to the potato in the phloem as "
             "dissolved sugar, then stored as starch."),
            ("In the potato itself",
             "In the leaves, by photosynthesis. It was carried down to the potato in the phloem as "
             "dissolved sugar, then stored as starch."),
        ],
        "answer": 0,
    },
    "words": ["phloem", "translocation", "xylem", "cell sap"],
    "knowledge": [
        {"kind": "card", "title": "Translocation",
         "body": [{"slot": "legacy-fig:plantFig"},
                  "Phloem tissue transports dissolved sugars from the leaves to the rest of the "
                  "plant for immediate use or storage.",
                  "The movement of food molecules through phloem tissue is called translocation.",
                  "The sugars can move up the plant, to growing tips and fruits, or down, to the "
                  "roots and storage organs. The leaves, where the sugars are made, are the "
                  "source; a place where they are used or stored is a sink."]},
        {"kind": "card", "title": "Phloem and xylem tubes",
         "body": [{"slot": "legacy-fig:tubeFig"},
                  "Phloem is made of tubes of elongated (long, thin) cells. Cell sap can move from one phloem "
                  "cell to the next through pores in the end walls.",
                  "Xylem is made of hollow tubes strengthened by lignin (a tough, woody substance).",
                  "You do not need the detailed structure of phloem, or how the sap is moved."]},
        {"kind": "reveal", "title": "Xylem and phloem compared",
         "cols": ["Xylem", "Phloem"],
         "rows": [
             ("Carries", "Water and mineral ions", "Dissolved sugars"),
             ("Direction", "From the roots to the stems and leaves",
              "From the leaves to the rest of the plant, up or down"),
             ("Structure", "Hollow tubes strengthened by lignin",
              "Tubes of elongated cells with pores in the end walls"),
             ("The movement is called", "The transpiration stream", "Trans\u00adlocation"),
         ]},
        {"kind": "card", "title": "Easy mistakes",
         "body": [{"mistakes": [
             ("Phloem carries water.", "Xylem carries water. Phloem carries dissolved sugars."),
             ("Translocation only moves sugars downwards.",
              "Sugars move up or down, to wherever they are used or stored."),
             ("Translocation is the loss of water from the leaves.",
              "That is transpiration. Translocation is the movement of dissolved sugars in the "
              "phloem."),
         ]}]},
    ],
    "key_fact": "Phloem tissue transports dissolved sugars from the leaves to the rest of the plant "
                "for immediate use or storage, and this movement is called translocation. Phloem "
                "is made of tubes of elongated cells with pores in the end walls; xylem is made of "
                "hollow tubes strengthened by lignin and carries water and mineral ions.",
    "deeper": [
        {"kind": "card", "title": "What the sugars are used for",
         "body": ["The sugars are used in respiration, or stored, for example as starch. Uses of "
                  "glucose has the details."]},
        {"kind": "card", "title": "Command words",
         "body": [{"points": [
             "<strong>State</strong> what translocation is: the movement of dissolved sugars "
             "through phloem.",
             "<strong>Compare</strong> xylem and phloem: what each carries, which way, and its "
             "structure, point by point.",
             "<strong>Suggest</strong> an effect: follow where the sugars can and cannot go.",
         ]}]},
    ],
    "try": None,
    "legacy": {"batch": "batch-6", "logic_edits": [(_js(a), _js(b)) for a, b in _EDITS]},
}
