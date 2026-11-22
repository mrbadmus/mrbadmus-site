# -*- coding: utf-8 -*-
"""Tests for carbonates, halides and sulfates, in the lean shape. Spec table:
ks4-carbonates-halides-sulfates.md (AQA 8462 4.8.3.3 to 4.8.3.5, chemistry only, with Required
practical 7; no 8464 section). Routes TF and TH only.

LEGACY (batch 2, Ks4Ladder). The ladder (r1..r4) and the practice set stay from the Design page.
The practice set reads the route's `quiz` list (K.bank): quiz-carbonates-halides-sulfates.json, five
per route, both old stems kept. Rung 1 used to be practice question 2 (K.find on "barium chloride
is added to an acidified solution"), so a pupil met it twice; it is now its own question through
K.item (bromide, cream), as relative-formula-mass did on 16 Nov 2026. Its position, and so its id,
is kept.

The ionic equations are HT only (8462 4.1.1.1), so that card is TH only (`isTH`). The carbonate
card places the page's own apparatus drawing, `legacy-fig:rigFig` (a standard bordered div, once
in the template). Batch 2's logic is written with literal Unicode, so the edits are plain strings.
The page's own eyebrow, "AQA Chemistry (8462) 4.8.3.3–4.8.3.5 · Required practical", is right on
both routes and is not rebuilt."""

LOGIC_EDITS = [
    # Rung 1: it was practice Q2 (K.find), word for word. Now its own question on the same
    # spec point (a precipitate colour names the halide), through the same K.item path.
    ("r1: Object.assign(K.find(slug, R.route, 'barium chloride is added to an acidified "
     "solution') || { options: [] }, { command: 'Identify', marks: 1, why: 'After acidifying, a "
     "white precipitate with barium chloride can only be barium sulfate.' }),",
     "r1: Object.assign(K.item({ q: 'Dilute nitric acid and then silver nitrate solution are "
     "added to a solution. A cream precipitate forms. Which ion is present?', opts: [['Bromide, "
     "Br⁻', true], ['Chloride, Cl⁻', false], ['Iodide, I⁻', false], ['Sulfate, SO₄²⁻', false]], "
     "wrong_explanations: { '1': 'Chloride gives a white precipitate.', '2': 'Iodide gives a "
     "yellow precipitate.', '3': 'Sulfate is tested with barium chloride, not silver nitrate.' } "
     "}), { command: 'Identify', marks: 1, why: 'Silver bromide is cream. Silver chloride is "
     "white and silver iodide is yellow.' }),"),
    # Rung 3 chain: links 1 and 2 could go in either order. Link 2 now follows from link 1.
    ("'Dilute hydrochloric acid reacts with any carbonate ions first, removing them as carbon "
     "dioxide.'",
     "'So dilute hydrochloric acid goes in first. It reacts with these carbonate ions and "
     "removes them as carbon dioxide.'"),
]

# ⊕ 22 Nov 2026 (Chemical analysis pupil walk): at 390 px Rung 2's four-column results table
# was wider than the card, so the deciding column started off-screen. Drawn again with two-line
# cells (same D.svg / D.T / D.line helpers, same data, same 19/21 type) so it fits a phone, and
# "ppt" is written out as "precipitate".
LOGIC_EDITS += [
    ("figureSvg: D.table(['Solution', 'Acid + limewater', 'HNO₃ then AgNO₃', 'HCl then BaCl₂'], [['P', 'milky', 'fizzes, no ppt', 'fizzes, no ppt'], ['Q', 'stays clear', 'cream ppt', 'no ppt'], ['R', 'stays clear', 'no ppt', 'white ppt']],\n            { widths: [130, 220, 220, 210], alt: 'Table. P: acid and limewater goes milky; with nitric acid and silver nitrate, and with hydrochloric acid and barium chloride, it fizzes but gives no precipitate. Q: limewater stays clear; cream precipitate with silver nitrate; no precipitate with barium chloride. R: limewater stays clear; no precipitate with silver nitrate; white precipitate with barium chloride. ppt means precipitate.' }),",
     'figureSvg: (function (head, rows, cw, alt) {\n            var rh = 80, x0 = 20, y0 = 20, W = cw.reduce(function (a, b) { return a + b; }, 0) + 40, H = rh * (rows.length + 1) + 40, x = x0;\n            var body = \'<rect x="20" y="20" width="\' + (W - 40) + \'" height="\' + (H - 40) + \'" fill="#FFFDF8" stroke="\' + D.C.stroke + \'" stroke-width="2.5"/>\';\n            var cell = function (cx, cy, t, size, o) { var ls = String(t).split(\'\\n\'); return ls.map(function (s, j) { return D.T(cx, cy + (j - (ls.length - 1) / 2) * (size + 4), s, size, o); }).join(\'\'); };\n            cw.forEach(function (w, i) {\n              if (i) body += D.line(x, y0, x, H - 20, 2, D.C.stroke);\n              body += cell(x + w / 2, y0 + rh / 2 + 7, head[i], 19, { fill: D.C.label });\n              rows.forEach(function (r, k) { body += cell(x + w / 2, y0 + rh * (k + 1) + rh / 2 + 7, r[i], 21, { fill: D.C.stroke, weight: i === 0 ? \'bold\' : \'normal\' }); });\n              x += w;\n            });\n            for (var k = 0; k <= rows.length; k++) body += D.line(x0, y0 + rh * (k + 1), W - 20, y0 + rh * (k + 1), k === 0 ? 3 : 1.5, D.C.stroke);\n            return D.svg(W, H, body, alt);\n          })([\'Solution\', \'Acid +\\nlimewater\', \'HNO₃ then\\nAgNO₃\', \'HCl then\\nBaCl₂\'], [[\'P\', \'milky\', \'fizzes, no\\nprecipitate\', \'fizzes, no\\nprecipitate\'], [\'Q\', \'stays clear\', \'cream\\nprecipitate\', \'no\\nprecipitate\'], [\'R\', \'stays clear\', \'no\\nprecipitate\', \'white\\nprecipitate\']], [96, 130, 130, 130], \'Table. P: acid and limewater goes milky; with nitric acid and silver nitrate, and with hydrochloric acid and barium chloride, it fizzes but gives no precipitate. Q: limewater stays clear; cream precipitate with silver nitrate; no precipitate with barium chloride. R: limewater stays clear; no precipitate with silver nitrate; white precipitate with barium chloride.\'),'),
    ("figureAlt: 'Results table for solutions P, Q and R; ppt means precipitate',",
     "figureAlt: 'Results table for solutions P, Q and R',"),
]

LESSON = {
    "slug": "carbonates-halides-sulfates",
    "start": {
        "setup": "A student adds dilute hydrochloric acid, then silver nitrate solution, to "
                 "five different salts. Every tube gives a white precipitate.",
        "question": "If you had to guess, did the chloride in every tube come from the salts, or "
                    "from something she added?",
        "options": [
            ("From the salts",
             "From something she added. Hydrochloric acid contains chloride ions, so every tube "
             "made white silver chloride, whatever the salt was."),
            ("From something she added",
             "From something she added. Hydrochloric acid contains chloride ions, so every tube "
             "made white silver chloride, whatever the salt was."),
        ],
        "answer": 1,
    },
    "words": ["anion", "precipitate", "acidify"],
    "knowledge": [
        {"kind": "card", "title": "Tests for negative ions",
         "body": ["These tests identify negative ions (anions) in a solution: carbonate ions, "
                  "halide ions and sulfate ions.",
                  "Halide ions are chloride, bromide and iodide ions."]},
        {"kind": "reveal", "title": "The three tests",
         "cols": ["Add", "Positive result"],
         "rows": [
             ("Carbonate", "Dilute acid, and bubble the gas through limewater",
              "Fizzing, and the gas turns limewater milky"),
             ("Halide", "Dilute nitric acid, then silver nitrate solution",
              "A precipitate: white, cream or yellow"),
             ("Sulfate", "Dilute hydrochloric acid, then barium chloride solution",
              "A white precipitate"),
         ]},
        {"kind": "card", "title": "Carbonates",
         "body": ["Carbonates react with dilute acids to form carbon dioxide gas. Carbon dioxide "
                  "can be identified with limewater: it turns the limewater milky (cloudy).",
                  {"slot": "legacy-fig:rigFig"},
                  "Na₂CO₃ + 2HCl → 2NaCl + H₂O + CO₂",
                  "Any carbonate and acid give a salt, water and carbon dioxide."]},
        {"kind": "card", "title": "Halides",
         "body": ["Halide ions in solution produce precipitates with silver nitrate solution in the "
                  "presence of dilute nitric acid."]},
        {"kind": "reveal", "title": "The silver halide precipitates",
         "cols": ["Colour of precipitate"],
         "rows": [
             ("Chloride ions", "White: silver chloride"),
             ("Bromide ions", "Cream: silver bromide"),
             ("Iodide ions", "Yellow: silver iodide"),
         ]},
        {"kind": "card", "title": "Sulfates",
         "body": ["Sulfate ions in solution produce a white precipitate with barium chloride "
                  "solution in the presence of dilute hydrochloric acid.",
                  "The white precipitate is barium sulfate."]},
        {"kind": "card", "title": "Why the acid goes in first",
         "body": ["Carbonate ions would also give a precipitate with silver nitrate or with barium "
                  "chloride. The acid reacts with any carbonate ions first and removes them as "
                  "carbon dioxide.",
                  "The acid must not add the ion you are testing for:",
                  {"points": [
                      "Halide test: use nitric acid. Hydrochloric acid would add chloride ions.",
                      "Sulfate test: use hydrochloric acid. Sulfuric acid would add sulfate ions.",
                  ]}]},
        {"kind": "card", "title": "Naming a compound",
         "body": ["A compound has a positive ion and a negative ion. A flame test or sodium "
                  "hydroxide solution identifies the metal ion. These tests identify the negative "
                  "ion.",
                  "A solid gives a green precipitate with sodium hydroxide solution. With dilute "
                  "hydrochloric acid and barium chloride solution it gives a white precipitate. It "
                  "is iron(II) sulfate."]},
        {"kind": "card", "title": "Required practical 7",
         "body": ["Use chemical tests to identify the ions in unknown single ionic compounds. This "
                  "is the negative-ion part.",
                  {"points": [
                      "1. Dissolve a small amount of each solid in distilled water.",
                      "2. Carbonate: add dilute hydrochloric acid in a tube fitted with a delivery "
                      "tube, and bubble any gas through limewater.",
                      "3. Halide: add a few drops of dilute nitric acid, then a few drops of "
                      "silver nitrate solution. Record the colour of any precipitate.",
                      "4. Sulfate: add a few drops of dilute hydrochloric acid, then a few drops "
                      "of barium chloride solution. Look for a white precipitate.",
                      "5. Use a fresh sample for every test, and a clean dropper for every "
                      "reagent.",
                  ]},
                  "Barium chloride is toxic if swallowed. Silver nitrate stains skin. Wear eye "
                  "protection and wash your hands afterwards."]},
        {"kind": "card", "title": "Ionic equations", "routes": ["TH"],
         "body": ["Ions that are dissolved before the reaction, and still dissolved and unchanged "
                  "after it, are spectator ions. Leave them out to get the ionic equation.",
                  {"points": [
                      "Ag⁺(aq) + Cl⁻(aq) → AgCl(s)",
                      "Ba²⁺(aq) + SO₄²⁻(aq) → BaSO₄(s)",
                      "CO₃²⁻(aq) + 2H⁺(aq) → H₂O(l) + CO₂(g)",
                  ]}]},
        {"kind": "card", "title": "Easy mistakes",
         "body": [{"mistakes": [
             ("Add hydrochloric acid before the silver nitrate.",
              "Use dilute nitric acid. Hydrochloric acid adds chloride ions, so every sample gives "
              "a white precipitate."),
             ("Bromide gives a yellow precipitate.",
              "Chloride gives white, bromide cream and iodide yellow."),
             ("It fizzed with acid, so it is a carbonate.",
              "Other things fizz with acid too. The gas must turn limewater milky."),
             ("Barium chloride tests for chloride ions.",
              "Barium chloride tests for sulfate ions: a white precipitate of barium sulfate."),
         ]}]},
    ],
    "key_fact": "Carbonates react with dilute acids to form carbon dioxide, which turns limewater "
                "milky. Halide ions give a precipitate with silver nitrate solution and dilute "
                "nitric acid: chloride white, bromide cream, iodide yellow. Sulfate ions give a "
                "white precipitate with barium chloride solution and dilute hydrochloric acid.",
    "deeper": [
        {"kind": "card", "title": "Links to other lessons",
         "body": ["Flame tests and Metal hydroxides identify the metal ion in the compound.",
                  "Testing for gases has the limewater test for carbon dioxide."]},
        {"kind": "card", "title": "Command words",
         "body": [{"points": [
             "<strong>Describe</strong> a test: name every reagent in order, the acid included, "
             "then the result.",
             "<strong>Explain</strong> a step: say what would go wrong without it.",
             "<strong>Plan</strong>: tests in a logical order that tell every sample apart, with "
             "each result.",
         ]}]},
    ],
    "try": None,
    "legacy": {"batch": "batch-2", "logic_edits": LOGIC_EDITS},
}
