# -*- coding: utf-8 -*-
"""The digestive system, in the lean shape. Spec table: ks4-digestive-system.md (AQA 8464 4.2.2.1 /
8461 4.2.2.1, word for word the same; food tests are 8464 RP 3 / 8461 RP 4). Enzyme action,
temperature, pH and the amylase practical are on Enzymes (the same spec point).

LEGACY (batch 6). The ladder and the practice set stay from the Design page. The practice set is
the page's own hard-coded `bankSrc` (same five items on every route), so its fixes are
logic_edits. No practice-set stem is edited, so every ks4q: id survives; rung prompts keep their
positions, so rung ids survive.

The lipid test is the live Design page's ethanol emulsion test, restored word for word after the
examiner pass (the practical's own line is 'carbohydrates, lipids and proteins'); which lipid
reagent to teach is Mide's call (UNSURE.md). The rung option naming it stays.
"""


def _js(s):
    """This batch's logic is plain ASCII with \\uXXXX escapes: spell a target the way the file does."""
    # Every non-ASCII character as backslash-u + 4 lower-case hex, the way these logic files spell
    # them (backslashreplace gave \\xNN for U+0080-U+00FF: µ ° ÷ × would never match).
    return "".join(c if ord(c) < 128 else "\\u%04x" % ord(c) for c in s)


_EDITS = [
    # Rung 1 Q1: the credited option was visibly the longest (+13).
    ("{ text: 'Amino acids', correct: false, reply: 'From protein.' }, { text: 'Glycerol and fatty acids', correct: true }, { text: 'Sugars', correct: false, reply: 'From starch.' }",
     "{ text: 'Simple sugars and amino acids', correct: false, reply: 'Sugars come from carbohydrates and amino acids from proteins.' }, { text: 'Glycerol and fatty acids', correct: true }, { text: 'Glucose and glycerol', correct: false, reply: 'Glucose comes from carbohydrates, not lipids.' }"),
    # Practice Q1 (bile), stem kept: credited option visibly the longest (+37), dash tail,
    # shouting capitals in the replies.
    ("opts: [['Emulsifies fats — breaks large droplets into smaller ones to increase surface area for lipase', true], ['Chemically digests fats into fatty acids and glycerol', false], ['Kills bacteria in the small intestine using its acidity', false], ['Digests proteins into amino acids in the small intestine', false]],",
     "opts: [['It emulsifies fat into small droplets', true], ['It digests fats into fatty acids and glycerol', false], ['It kills bacteria because it is acidic', false], ['It digests proteins into amino acids', false]],"),
    ("wrong_explanations: { 1: 'Chemical digestion of fats = LIPASE. Bile only emulsifies — a physical process.', 2: 'Bile is ALKALINE, not acidic. HCl in the stomach kills bacteria. Bile actually neutralises the stomach acid.', 3: 'Protein digestion = PROTEASES (pepsin in the stomach, pancreatic proteases in the small intestine). Bile is not a protease.' }",
     "wrong_explanations: { 1: 'Lipase digests fat. Bile only breaks fat into small droplets.', 2: 'Bile is alkaline. It neutralises hydrochloric acid from the stomach.', 3: 'Proteases digest proteins. Bile is not an enzyme.' }"),
    # Practice Q2 (villi), stem kept: credited option visibly the longest (+28).
    ("opts: [['To provide a large surface area for absorbing digested nutrients into the blood', true], ['To produce digestive enzymes for breaking down food', false], ['To neutralise the acid from the stomach', false], ['To store bile before it is released onto food', false]],",
     "opts: [['To give a large surface area for absorbing digested food', true], ['To produce digestive enzymes for breaking down food', false], ['To neutralise the acid from the stomach', false], ['To store bile before it is released onto food', false]],"),
    ("wrong_explanations: { 1: 'Villi are there to give a big surface area for absorbing digested food; the enzymes come from the pancreas and the small intestine wall.', 2: 'Bile neutralises stomach acid — villi are surface-area adaptations for absorption.', 3: 'Bile is stored in the GALL BLADDER, not in villi.' }",
     "wrong_explanations: { 1: 'Villi are for absorbing digested food. They give a large surface area.', 2: 'Bile neutralises stomach acid. Villi give a large surface area for absorption.', 3: 'Bile is stored in the gall bladder.' }"),
    # Practice Q3 (proteins first digested), stem kept: credited option visibly the longest (+24),
    # dash tails, and pepsin (not in the spec; the spec says proteases).
    ("opts: [['The stomach — by the enzyme pepsin in the presence of HCl', true], ['The mouth — by salivary amylase', false], ['The large intestine — by bacteria', false], ['The liver — by bile salts', false]],",
     "opts: [['In the stomach', true], ['In the mouth', false], ['In the large intestine', false], ['In the liver', false]],"),
    ("wrong_explanations: { 1: 'Salivary amylase in the mouth digests STARCH, not proteins. Amylase has no effect on protein.', 2: 'Bacteria in the large intestine help break down some fibre but are not the main site of protein digestion.', 3: 'The liver produces bile which emulsifies FATS — bile has no protein-digesting function.' }",
     "wrong_explanations: { 1: 'Amylase in the mouth digests starch, not protein.', 2: 'Proteins are digested in the stomach and small intestine, before food reaches the large intestine.', 3: 'The liver makes bile, which is not an enzyme.' }"),
    # Practice Q4 (large intestine), stem kept: dash tails; a reply named lacteals (beyond GCSE).
    ("opts: [['Water — from the remaining undigested material', true], ['Glucose — the final stage of carbohydrate absorption', false], ['Amino acids — the final stage of protein absorption', false], ['Fatty acids — the final stage of fat absorption', false]],",
     "opts: [['Water', true], ['Glucose', false], ['Amino acids', false], ['Fatty acids', false]],"),
    ("wrong_explanations: { 1: 'Glucose is absorbed in the SMALL INTESTINE — by the time food reaches the large intestine, glucose has already been absorbed.', 2: 'Amino acids are absorbed in the SMALL INTESTINE — through the villi walls into the blood.', 3: 'Fatty acids and glycerol are absorbed in the SMALL INTESTINE into the lacteals (lymph vessels in villi).' }",
     "wrong_explanations: { 1: 'Glucose is absorbed into the blood in the small intestine.', 2: 'Amino acids are absorbed into the blood in the small intestine.', 3: 'Fatty acids are absorbed in the small intestine.' }"),
    # Practice Q5 (salivary glands), stem kept: dash tails, maltose and pepsin (not in the spec).
    # Distractors that are not enzymes at all, so each is definitely wrong.
    ("opts: [['Amylase — breaks down starch into maltose', true], ['Pepsin — breaks down proteins', false], ['Lipase — breaks down fats', false], ['Bile — emulsifies fats', false]],",
     "opts: [['Amylase', true], ['Bile', false], ['Hydrochloric acid', false], ['Fatty acids', false]],"),
    ("wrong_explanations: { 1: 'Pepsin is produced by glandular tissue in the STOMACH WALL — not the salivary glands.', 2: 'Lipase is produced by the PANCREAS — not the salivary glands.', 3: 'Bile is not an enzyme — it is produced by the LIVER and stored in the gall bladder.' }",
     "wrong_explanations: { 1: 'Bile is not an enzyme. It is made in the liver.', 2: 'Hydrochloric acid is not an enzyme. The stomach produces it.', 3: 'Fatty acids are a product of lipid digestion, not an enzyme.' }"),
]

_FOOD_TESTS = [
    "Grind the food with a little distilled water to make a solution. Use a fresh sample for "
    "each test, and wear eye protection.",
    {"points": [
        "<strong>Starch</strong>: add iodine solution. Orange-brown turns blue-black if starch is "
        "present.",
        "<strong>Sugars</strong>: add Benedict's solution and heat in a hot water bath for a few "
        "minutes. Blue turns green, yellow, orange or brick-red if a sugar is present. The more sugar, the "
        "further along that list the colour goes.",
        "<strong>Protein</strong>: add Biuret reagent. Blue turns purple if protein is present.",
        "<strong>Lipids</strong>: shake the food with ethanol, then pour into water. A cloudy white "
        "emulsion forms if lipid is present. Ethanol is flammable, so keep it away from any flame.",
    ]},
]

# Examiner pass (EXAMINER.md) and blind pass, 18 Nov 2026. Each old string is the logic AFTER the
# edits above, and occurs exactly once (validate.py checks).
_EDITS += [
    ("D.T(330, 300, 'small intestine (coiled)', 13,",
     "D.T(330, 300, 'small intestine', 13,"),
]

LESSON = {
    "slug": "digestive-system",
    "start": {
        "setup": "Bread contains starch. Starch molecules are too big to pass into the blood.",
        "question": "If you had to guess, what must happen to the starch first?",
        "options": [
            ("It is broken into smaller molecules",
             "Enzymes break starch into sugars. Sugars are small and soluble, so they can be "
             "absorbed into the bloodstream."),
            ("It is absorbed whole in the stomach",
             "Enzymes break starch into sugars. Sugars are small and soluble, so they can be "
             "absorbed into the bloodstream."),
        ],
        "answer": 0,
    },
    "words": ["carbohydrase", "protease", "lipase", "bile"],
    "knowledge": [
        {"kind": "card", "title": "The digestive system",
         "body": ["The digestive system is an organ system in which several organs work together "
                  "to digest and absorb food.",
                  {"slot": "legacy-fig:gutFig"},
                  "Digestive enzymes convert food into small soluble molecules that can be "
                  "absorbed into the bloodstream. They are absorbed in the small intestine."]},
        {"kind": "reveal", "title": "Three kinds of enzyme",
         "cols": ["Breaks down", "Into"],
         "rows": [
             ("Carbohydrases, such as amylase", "Carbohydrates, such as starch", "Simple sugars"),
             ("Proteases", "Proteins", "Amino acids"),
             ("Lipases", "Lipids (fats)", "Glycerol and fatty acids"),
         ]},
        {"kind": "card", "title": "Where the enzymes are made",
         "body": [{"points": [
             "Amylase: the salivary glands, the pancreas and the small intestine.",
             "Proteases: the stomach, the pancreas and the small intestine.",
             "Lipases: the pancreas and the small intestine.",
         ]},
             "The stomach also makes hydrochloric acid."]},
        {"kind": "card", "title": "Word equations",
         "body": [{"points": [
             "starch → simple sugars (amylase)",
             "protein → amino acids (protease)",
             "lipid → glycerol + fatty acids (lipase)",
         ]},
             "The products of digestion are used to build new carbohydrates, lipids and "
             "proteins. Some glucose is used in respiration."]},
        {"kind": "card", "title": "Bile",
         "body": ["Bile is made in the liver and stored in the gall bladder. It is not an enzyme.",
                  {"points": [
                      "Bile is alkaline, to neutralise hydrochloric acid from the stomach.",
                      "Bile emulsifies fat to form small droplets, which increases the surface "
                      "area.",
                  ]},
                  "The alkaline conditions and large surface area increase the rate of fat "
                  "breakdown by lipase."]},
        {"kind": "card", "title": "Required practical 3: food tests", "routes": ["CF", "CH"],
         "body": _FOOD_TESTS},
        {"kind": "card", "title": "Required practical 4: food tests", "routes": ["TF", "TH"],
         "body": _FOOD_TESTS},
        {"kind": "card", "title": "Easy mistakes",
         "body": [{"mistakes": [
             ("Bile is an enzyme that digests fat.",
              "Bile emulsifies fat into small droplets. Lipase digests the fat."),
             ("Proteases break proteins into sugars.",
              "Proteases break proteins into amino acids."),
             ("Benedict's turns brick-red as soon as it is added.",
              "Benedict's must be heated in a hot water bath before the colour changes."),
         ]}]},
    ],
    "key_fact": "Digestive enzymes convert food into small soluble molecules that can be absorbed "
                "into the bloodstream: carbohydrases break carbohydrates into simple sugars, "
                "proteases break proteins into amino acids, and lipases break lipids into glycerol "
                "and fatty acids. Bile neutralises stomach acid and emulsifies fat, which increases "
                "the rate of fat breakdown by lipase.",
    "deeper": [
        {"kind": "card", "title": "Villi",
         "body": ["The small intestine is lined with villi. They give a large surface area, so "
                  "digested food is absorbed into the blood quickly."]},
        {"kind": "card", "title": "How enzymes work",
         "body": ["Why each enzyme only breaks down one kind of molecule, and how temperature and "
                  "pH change the rate, are on Enzymes."]},
        {"kind": "card", "title": "Command words",
         "body": [{"points": [
             "<strong>Name</strong> the products: write the molecules, such as \"glycerol and "
             "fatty acids\".",
             "<strong>Describe</strong> a food test: the reagent, any heating, and the colour "
             "before and after.",
             "<strong>Explain</strong> how bile helps: emulsifies, larger surface area, faster "
             "breakdown by lipase.",
         ]}]},
    ],
    "try": None,
    "legacy": {"batch": "batch-6", "logic_edits": [(_js(a), _js(b)) for a, b in _EDITS]},
}
