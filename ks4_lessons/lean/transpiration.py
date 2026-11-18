# -*- coding: utf-8 -*-
"""Transpiration, in the lean shape. Spec table: ks4-transpiration.md (AQA 8464 4.2.3.2 / 8461
4.2.3.2, word for word the same; no HT-only or Biology-only lines). This lesson owns the root
hair cells, the plant organ system for transport, the transpiration stream, stomata and guard
cells, and the four factors. Translocation and the xylem-against-phloem comparison are on
Translocation (the same spec point).

LEGACY (batch 6). The ladder and the practice set stay from the Design page. The practice set is
the page's own hard-coded `bankSrc` (same five items on every route), so its fixes are
logic_edits. No practice-set stem is edited, so every ks4q: id survives; rung prompts keep their
positions, so rung ids survive.

New in the lean record (spec gaps on the Design page): the root hair cell card (4.2.3.2: water by
osmosis, mineral ions by active transport), the organ-system sentence, and one worked
graph-reading item (MS 2c, 4a, 4c) with fig:transpiration-temperature-graph.
"""


def _js(s):
    """This batch's logic is plain ASCII with \\uXXXX escapes: spell a target the way the file does."""
    # Every non-ASCII character as backslash-u + 4 lower-case hex, the way these logic files spell
    # them (backslashreplace gave \\xNN for U+0080-U+00FF: µ ° ÷ × would never match).
    return "".join(c if ord(c) < 128 else "\\u%04x" % ord(c) for c in s)


_EDITS = [
    # Practice Q1 (what is transpiration), stem kept: capitals in the replies; one reply said
    # photosynthesis produces no water and gave the Higher symbol equation.
    ("wrong_explanations: { 1: 'Transport of dissolved sugars = TRANSLOCATION (in phloem). Transpiration is specifically water evaporation from leaves.', 2: 'Water absorption by roots = OSMOSIS through root hair cells. Transpiration is what happens at the LEAVES end.', 3: 'Photosynthesis produces OXYGEN, not water — water is a REACTANT of photosynthesis (6CO₂ + 6H₂O → C₆H₁₂O₆ + 6O₂).' }",
     "wrong_explanations: { 1: 'That is translocation, in the phloem.', 2: 'Root hair cells take in water by osmosis. Transpiration happens at the leaves.', 3: 'Photosynthesis uses water. Transpiration is water evaporating from the leaves.' }"),
    # Practice Q2 (humid to dry and windy), stem kept: dash tails; "the plant closes its
    # stomata" was not definitely wrong (its own reply conceded it). Options rebuilt.
    ("opts: [['Transpiration increases significantly — lower humidity and wind both increase the rate', true], ['Transpiration decreases — the plant closes its stomata to conserve water', false], ['Transpiration stays the same — the two factors cancel each other out', false], ['Transpiration increases due to humidity but decreases due to wind — net effect is zero', false]],",
     "opts: [['It increases: dry air and wind both speed it up', true], ['It decreases: dry air and wind both slow it down', false], ['It stays the same: dry air and wind cancel out', false], ['It stops, because wind closes all the stomata', false]],"),
    ("wrong_explanations: { 1: 'The plant may eventually close stomata if it loses too much water — but the immediate effect of moving to dry, windy conditions is faster transpiration. Stomata closing is a response to stress, not an immediate automatic reaction.', 2: 'The two factors don’t cancel out — both low humidity AND wind INCREASE transpiration rate. They act in the same direction.', 3: 'Both low humidity and wind INCREASE transpiration — humidity and wind both affect the concentration gradient for water vapour in the same way (they both maintain a steep gradient).' }",
     "wrong_explanations: { 1: 'Dry air and wind both increase the rate of transpiration.', 2: 'Both factors increase the rate, so they do not cancel out.', 3: 'Wind blows water vapour away from the leaf, which speeds transpiration up.' }"),
    # Practice Q3 (brighter light), stem kept: dash; "increases the temperature of the leaf" and
    # "photosynthesis produces more water" were not definitely wrong. Replaced.
    ("opts: [['Brighter light causes stomata to open wider — allowing more water vapour to escape', true], ['Brighter light increases the temperature of the leaf, causing faster evaporation', false], ['Brighter light increases the rate of photosynthesis, which produces more water', false], ['Brighter light makes chlorophyll absorb water directly from the air', false]],",
     "opts: [['Its stomata open wider, so more water vapour escapes', true], ['Light makes the xylem pump water up faster', false], ['Light closes the stomata, so water is trapped', false], ['Light makes chlorophyll absorb water from the air', false]],"),
    ("wrong_explanations: { 1: 'Brighter light does warm leaves slightly — but the PRIMARY mechanism is guard cells responding to light by opening stomata wider.', 2: 'Photosynthesis uses water as a REACTANT — it consumes water, not produces it. Oxygen is the gas product.', 3: 'Chlorophyll absorbs LIGHT energy — it does not absorb water from the air.' }",
     "wrong_explanations: { 1: 'Nothing pumps water up the xylem. It is drawn up as water evaporates from the leaves.', 2: 'Stomata open in the light. They close in the dark.', 3: 'Chlorophyll absorbs light, not water.' }"),
]

LESSON = {
    "slug": "transpiration",
    "start": {
        "setup": "A clear plastic bag is tied round a leafy shoot in the sun. Droplets of water "
                 "soon appear inside it.",
        "question": "If you had to guess, where does the water come from?",
        "options": [
            ("Out of the leaves",
             "From the leaves. Water evaporates from the leaves and escapes through the stomata as "
             "water vapour. This is transpiration."),
            ("The air already in the bag",
             "From the leaves. Water evaporates from the leaves and escapes through the stomata as "
             "water vapour. This is transpiration."),
        ],
        "answer": 0,
    },
    "words": ["transpiration", "stomata", "guard cells", "potometer"],
    "knowledge": [
        {"kind": "card", "title": "Into the root",
         "body": ["The roots, stem and leaves form a plant organ system for transport of "
                  "substances around the plant.",
                  "Root hair cells are adapted for the efficient uptake of water by osmosis, and "
                  "mineral ions by active transport.",
                  {"points": [
                      "Each root hair is a long, thin extension of the cell, which gives a large "
                      "surface area.",
                      "The soil usually has a lower concentration of mineral ions than the root "
                      "hair cell, so they are taken in against the concentration gradient by "
                      "active transport.",
                      "Active transport needs energy from respiration, so root hair cells have "
                      "many mitochondria.",
                  ]}]},
        {"kind": "card", "title": "The transpiration stream",
         "body": ["Xylem tissue transports water and mineral ions from the roots to the stems and "
                  "leaves. It is made of hollow tubes strengthened by lignin (a tough, woody substance), "
                  "adapted for the "
                  "transport of water in the transpiration stream.",
                  {"points": [
                      "Water evaporates from the leaves and diffuses out through the stomata as "
                      "water vapour. This is transpiration.",
                      "More water is drawn up the xylem to replace it.",
                      "More water enters the root hair cells from the soil.",
                  ]},
                  "The movement of water from the roots, through the xylem and out of the leaves "
                  "is called the transpiration stream."]},
        {"kind": "card", "title": "Stomata and guard cells",
         "body": [{"slot": "legacy-fig:stomaFig"},
                  "The role of stomata and guard cells is to control gas exchange and water loss.",
                  {"points": [
                      "When the guard cells open the stoma, carbon dioxide gets in for "
                      "photosynthesis and water vapour gets out.",
                      "When they close it, less water is lost.",
                      "Stomata usually open in the light and close in the dark.",
                  ]},
                  "Most stomata are on the lower surface of the leaf."]},
        {"kind": "reveal", "title": "What changes the rate of transpiration",
         "cols": ["Effect on the rate", "Why"],
         "rows": [
             ("Higher temperature", "Faster",
              "Water evaporates and diffuses faster"),
             ("Higher humidity (more water vapour in the air)", "Slower",
              "There is less difference in water vapour between inside and outside the leaf"),
             ("More air movement", "Faster",
              "Wind blows water vapour away from the leaf, so it diffuses out faster"),
             ("Higher light intensity", "Faster",
              "The stomata open wider, so more water vapour escapes"),
         ]},
        {"kind": "card", "title": "Measuring the rate: the potometer",
         "body": [{"slot": "legacy-fig:potFig"},
                  "A potometer measures the rate of water uptake by a leafy shoot. Almost all the "
                  "water taken up is lost by transpiration, so it gives an estimate of the rate "
                  "of transpiration.",
                  "rate of water uptake = distance the bubble moves ÷ time",
                  {"slot": "cfifa"}]},
        {"kind": "card", "title": "Reading results",
         "body": ["Made-up results: how far the bubble moved in 5 minutes at three temperatures.",
                  {"points": [
                      "10 °C: 15 mm",
                      "20 °C: 30 mm",
                      "30 °C: 45 mm",
                  ]},
                  "Rate at 20 °C = 30 ÷ 5 = 6 mm/min. The rates at 10 °C and 30 °C are 3 mm/min "
                  "and 9 mm/min.",
                  {"slot": "fig:transpiration-temperature-graph"},
                  "As the temperature increases, the rate of water uptake increases."]},
        {"kind": "card", "title": "Easy mistakes",
         "body": [{"mistakes": [
             ("Water is pumped up the xylem.",
              "Water is drawn up the xylem as water evaporates from the leaves."),
             ("A potometer measures the water lost by the leaves.",
              "It measures water uptake. Almost all of that water is then lost by transpiration."),
             ("Humid air speeds up transpiration.",
              "Humid air slows it down, because there is less difference in water vapour between "
              "inside and outside the leaf."),
         ]}]},
    ],
    "key_fact": "Transpiration is the loss of water vapour from the leaves through the stomata. It "
                "draws water up the xylem from the roots in the transpiration stream, and it is "
                "faster when it is warmer, drier, windier or brighter. Root hair cells take up "
                "water by osmosis and mineral ions by active transport.",
    "deeper": [
        {"kind": "card", "title": "Why the stomata matter",
         "body": ["A plant needs its stomata open to take in carbon dioxide for photosynthesis, "
                  "but open stomata also let water vapour out. Guard cells balance the two."]},
        {"kind": "card", "title": "Command words",
         "body": [{"points": [
             "<strong>Explain</strong> the effect of a factor: say whether the rate rises or "
             "falls, then why.",
             "<strong>Calculate</strong> a rate: put the time in the unit asked for, then "
             "distance ÷ time.",
             "<strong>Describe</strong> a potometer method: change one factor, keep the others "
             "the same, time the bubble, repeat.",
         ]}]},
    ],
    "try": None,
    "legacy": {"batch": "batch-6", "logic_edits": [(_js(a), _js(b)) for a, b in _EDITS]},
}
