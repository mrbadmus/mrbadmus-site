# -*- coding: utf-8 -*-
"""Metal hydroxides, in the lean shape. Spec table: ks4-metal-hydroxides.md (AQA 8462 4.8.3.2,
chemistry only; no 8464 section). Routes TF and TH only.

LEGACY (batch 2, Ks4Ladder). The ladder (r1..r4) and the practice set stay from the Design page.
The practice set reads the route's `quiz` list (K.bank): quiz-metal-hydroxides.json, five per route,
both old stems kept. Rung 1 used to be practice question 1 (K.find on "gives a brown precipitate
with NaOH"), so a pupil met it twice; it is now its own question through K.item (iron(II), green),
as relative-formula-mass did on 16 Nov 2026. Its position, and so its id, is kept.

4.8.3.2 has no HT-only line: the balanced equations are on both routes. The ionic equations are HT
only (8462 4.1.1.1), so that card is TH only (`isTH`, bound by `Object.assign({}, R, `). Batch 2's
logic is written with literal Unicode, so the edits are plain strings. The page's own eyebrow,
"AQA Chemistry (8462) 4.8.3.2 · Classify", is right on both routes and is not rebuilt."""

LOGIC_EDITS = [
    # Rung 1: it was practice Q1 (K.find), word for word. Now its own question on the same
    # spec line (a coloured precipitate names the ion), through the same K.item path.
    ("r1: Object.assign(K.find(slug, R.route, 'gives a brown precipitate with NaOH') || "
     "{ options: [] }, { command: 'Identify', marks: 1, why: 'Iron(III) hydroxide is brown. "
     "Iron(II) gives green.' }),",
     "r1: Object.assign(K.item({ q: 'A few drops of sodium hydroxide solution are added to a "
     "solution. A green precipitate forms. Which metal ion is present?', opts: [['Iron(II), Fe²⁺', "
     "true], ['Iron(III), Fe³⁺', false], ['Copper(II), Cu²⁺', false], ['Magnesium, Mg²⁺', false]], "
     "wrong_explanations: { '1': 'Iron(III) gives a brown precipitate.', '2': 'Copper(II) gives a "
     "blue precipitate.', '3': 'Magnesium gives a white precipitate.' } }), { command: 'Identify', "
     "marks: 1, why: 'Iron(II) hydroxide is green. Iron(III) hydroxide is brown.' }),"),
]

# ⊕ 22 Nov 2026 (Chemical analysis pupil walk): at 390 px Rung 2's four-column results table
# was wider than the card, so the deciding column started off-screen. Drawn again with two-line
# cells (same D.svg / D.T / D.line helpers, same data, same 19/21 type) so it fits a phone, and
# "ppt" is written out as "precipitate".
LOGIC_EDITS += [
    ("figureSvg: D.table(['Solution', 'Few drops of NaOH', 'Excess NaOH', 'Flame test'], [['P', 'white precipitate', 'dissolves', 'not done'], ['Q', 'green precipitate', 'stays', 'not done'], ['R', 'white precipitate', 'stays', 'orange-red']],\n            { widths: [130, 250, 170, 170], alt: 'Table. P: white precipitate that dissolves in excess. Q: green precipitate that stays. R: white precipitate that stays, and an orange-red flame.' }),",
     'figureSvg: (function (head, rows, cw, alt) {\n            var rh = 80, x0 = 20, y0 = 20, W = cw.reduce(function (a, b) { return a + b; }, 0) + 40, H = rh * (rows.length + 1) + 40, x = x0;\n            var body = \'<rect x="20" y="20" width="\' + (W - 40) + \'" height="\' + (H - 40) + \'" fill="#FFFDF8" stroke="\' + D.C.stroke + \'" stroke-width="2.5"/>\';\n            var cell = function (cx, cy, t, size, o) { var ls = String(t).split(\'\\n\'); return ls.map(function (s, j) { return D.T(cx, cy + (j - (ls.length - 1) / 2) * (size + 4), s, size, o); }).join(\'\'); };\n            cw.forEach(function (w, i) {\n              if (i) body += D.line(x, y0, x, H - 20, 2, D.C.stroke);\n              body += cell(x + w / 2, y0 + rh / 2 + 7, head[i], 19, { fill: D.C.label });\n              rows.forEach(function (r, k) { body += cell(x + w / 2, y0 + rh * (k + 1) + rh / 2 + 7, r[i], 21, { fill: D.C.stroke, weight: i === 0 ? \'bold\' : \'normal\' }); });\n              x += w;\n            });\n            for (var k = 0; k <= rows.length; k++) body += D.line(x0, y0 + rh * (k + 1), W - 20, y0 + rh * (k + 1), k === 0 ? 3 : 1.5, D.C.stroke);\n            return D.svg(W, H, body, alt);\n          })([\'Solution\', \'A few drops\\nof NaOH\', \'Excess\\nNaOH\', \'Flame\\ntest\'], [[\'P\', \'white\\nprecipitate\', \'dissolves\', \'not done\'], [\'Q\', \'green\\nprecipitate\', \'stays\', \'not done\'], [\'R\', \'white\\nprecipitate\', \'stays\', \'orange-red\']], [96, 140, 120, 120], \'Table. P: white precipitate that dissolves in excess. Q: green precipitate that stays. R: white precipitate that stays, and an orange-red flame.\'),'),
]

LESSON = {
    "slug": "metal-hydroxides",
    "start": {
        "setup": "Copper(II) sulfate solution is clear and blue. A few drops of colourless sodium "
                 "hydroxide solution are added, and a blue solid appears.",
        "question": "If you had to guess, is the blue solid a new substance, or copper sulfate "
                    "coming back out of the solution?",
        "options": [
            ("A new substance",
             "A new substance. It is copper(II) hydroxide. It is insoluble, so it forms a solid "
             "in the solution: a precipitate."),
            ("Copper sulfate coming back out",
             "A new substance. It is copper(II) hydroxide. It is insoluble, so it forms a solid "
             "in the solution: a precipitate."),
        ],
        "answer": 0,
    },
    "words": ["precipitate", "sodium hydroxide solution", "in excess"],
    "knowledge": [
        {"kind": "card", "title": "Testing with sodium hydroxide",
         "body": ["Sodium hydroxide solution can be used to identify some metal ions (cations).",
                  "Add a few drops of sodium hydroxide solution to a solution of the compound. The "
                  "hydroxide ions join the metal ions to make a metal hydroxide. These metal "
                  "hydroxides are insoluble, so they form a precipitate.",
                  "Record the colour of the precipitate, not the colour of the solution."]},
        {"kind": "reveal", "title": "Precipitates with sodium hydroxide solution",
         "cols": ["Precipitate", "In excess"],
         "rows": [
             ("Aluminium ions", "White", "The precipitate dissolves"),
             ("Calcium ions", "White", "The precipitate stays"),
             ("Magnesium ions", "White", "The precipitate stays"),
             ("Copper(II) ions", "Blue", "The precipitate stays"),
             ("Iron(II) ions", "Green", "The precipitate stays"),
             ("Iron(III) ions", "Brown", "The precipitate stays"),
         ]},
        {"kind": "card", "title": "A few drops first, then excess",
         "body": ["Solutions of aluminium, calcium and magnesium ions form white precipitates when "
                  "sodium hydroxide solution is added, but only the aluminium hydroxide precipitate "
                  "dissolves in excess sodium hydroxide solution.",
                  "So add the sodium hydroxide a few drops at a time, then keep adding until it is "
                  "in excess. Added all at once, the aluminium precipitate may dissolve before it "
                  "is seen."]},
        {"kind": "card", "title": "Calcium or magnesium",
         "body": ["Calcium and magnesium both give a white precipitate that stays in excess. Sodium "
                  "hydroxide cannot tell them apart.",
                  "A flame test can: calcium compounds give an orange-red flame."]},
        {"kind": "card", "title": "Iron(II) or iron(III)",
         "body": ["The number in brackets is the charge on the iron ion.",
                  {"points": [
                      "Iron(II), Fe²⁺, gives a green precipitate.",
                      "Iron(III), Fe³⁺, gives a brown precipitate.",
                  ]}]},
        {"kind": "card", "title": "Writing the equation",
         "body": ["metal salt + sodium hydroxide → metal hydroxide + sodium salt",
                  "The metal hydroxide has one hydroxide ion, OH⁻, for each positive charge "
                  "on the metal ion. Then balance the sodium.",
                  {"points": [
                      "CuSO₄(aq) + 2NaOH(aq) → Cu(OH)₂(s) + Na₂SO₄(aq)",
                      "FeCl₃(aq) + 3NaOH(aq) → Fe(OH)₃(s) + 3NaCl(aq)",
                  ]},
                  "The (s) shows the precipitate."]},
        {"kind": "reveal", "title": "The formula of each hydroxide",
         "cols": ["Hydroxide"],
         "rows": [
             ("Mg²⁺", "Mg(OH)₂"),
             ("Ca²⁺", "Ca(OH)₂"),
             ("Al³⁺", "Al(OH)₃"),
             ("Cu²⁺", "Cu(OH)₂"),
             ("Fe²⁺", "Fe(OH)₂"),
             ("Fe³⁺", "Fe(OH)₃"),
         ]},
        {"kind": "card", "title": "Ionic equations", "routes": ["TH"],
         "body": ["The ionic equation shows only the ions that make the precipitate:",
                  {"points": [
                      "M²⁺(aq) + 2OH⁻(aq) → M(OH)₂(s)",
                      "M³⁺(aq) + 3OH⁻(aq) → M(OH)₃(s)",
                  ]},
                  "Cu²⁺(aq) + 2OH⁻(aq) → Cu(OH)₂(s)",
                  "The sodium ions and the other ion of the salt stay dissolved and unchanged. "
                  "They are spectator ions, so they are left out."]},
        {"kind": "card", "title": "Required practical 7",
         "body": ["Use chemical tests to identify the ions in unknown single ionic compounds. This "
                  "is the sodium hydroxide part.",
                  {"points": [
                      "1. Put about 1\u00a0cm³ of the solution in a clean test tube.",
                      "2. Add dilute sodium hydroxide solution a few drops at a time. Record the "
                      "colour of any precipitate.",
                      "3. Keep adding sodium hydroxide, shaking, until it is in excess. Record "
                      "whether a white precipitate dissolves.",
                  ]},
                  "Sodium hydroxide solution is harmful to eyes: wear eye protection."]},
        {"kind": "card", "title": "Easy mistakes",
         "body": [{"mistakes": [
             ("Iron(II) gives a brown precipitate.",
              "Iron(II) gives a green precipitate. Iron(III) gives a brown one."),
             ("Calcium hydroxide dissolves in excess sodium hydroxide.",
              "Only aluminium hydroxide dissolves in excess."),
             ("Copper(II) sulfate is blue, so the result is blue.",
              "Report the colour of the precipitate. The solution was blue before anything was "
              "added."),
             ("Add all the sodium hydroxide at once.",
              "Add a few drops first, then go on to excess, so the aluminium precipitate is seen."),
         ]}]},
    ],
    "key_fact": "Sodium hydroxide solution gives white precipitates with aluminium, calcium and "
                "magnesium ions, but only aluminium hydroxide dissolves in excess sodium hydroxide. "
                "Copper(II) ions give a blue precipitate, iron(II) a green precipitate and "
                "iron(III) a brown precipitate.",
    "deeper": [
        {"kind": "card", "title": "Iron(II) hydroxide on standing",
         "body": ["Left to stand, green iron(II) hydroxide slowly turns brown at its surface, as it "
                  "reacts with oxygen from the air. Record the colour it has when it first forms: "
                  "green."]},
        {"kind": "card", "title": "Links to other lessons",
         "body": ["Flame tests tell calcium from magnesium.",
                  "Tests for carbonates, halides and sulfates identify the other ion in the "
                  "compound."]},
        {"kind": "card", "title": "Command words",
         "body": [{"points": [
             "<strong>Identify</strong>: name the ion from the results given.",
             "<strong>Complete</strong> an equation: the missing formula and the balancing "
             "numbers.",
             "<strong>Plan</strong>: tests in order that tell every sample apart, with the result "
             "each one gives.",
         ]}]},
    ],
    "try": None,
    "legacy": {"batch": "batch-2", "logic_edits": LOGIC_EDITS},
}
