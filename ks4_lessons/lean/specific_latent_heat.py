# -*- coding: utf-8 -*-
"""Changes of state and specific latent heat, in the lean shape. Spec table:
ks4-specific-latent-heat.md (AQA 8464 6.3.2.3 / 8463 4.3.2.3, word for word the same). No HT-only
or physics-only line, no required practical. Every route gets the same teaching cards.

LEGACY (batch 3, Ks4Ladder). The ladder (r1..r4), the worked examples and Your turn questions
(cfExamples / cfQuestions, placed by the `cfifa` slot) and the practice set stay from the Design
page. Its eyebrow is route-aware already (8464 6.3.2.3 / 8463 4.3.2.3). The practice set reads the
route's `quiz` list (K.bank): five per route, both old stems kept word for word.

E = m L is on the Physics equation sheet (8463 Appendix, sheet equation 9: "thermal energy for a
change of state = mass × specific latent heat"); the content section words it "energy for a change
of state", which the card uses.

LOGIC_EDITS:
  1, 2. loggerFig (the cooling curve of Y) drew only as the (removed) data-logger bench ran
     (`tEnd = s.logP * 12`): drawn always, complete to 12 minutes, with its complete alt text.
  3. Rung 3 asked "Explain why sweating cools the body", the same question as practice question 2
     ("Why does sweating cool the body?"), so a pupil met it twice. It is now a chain on ice
     cooling a drink: the same spec line (latent heat; energy changes the internal energy, not the
     temperature), one right order. Same rung position, so its id (#r3) is kept. Link 2 starts
     "As it melts, ..." so it can only follow link 1 (examiner review, 24 Nov 2026)."""

LOGIC_EDITS = [
    ("const tEnd = s.logDone ? 12 : s.logP * 12;", "const tEnd = 12;"),
    ("alt: s.logDone ? 'Cooling curve for Y.", "alt: tEnd === 12 ? 'Cooling curve for Y."),
    ("r3: { command: 'Explain', marks: 3, prompt: 'Explain why sweating cools the body. Put the "
     "links in order.',\n          links: ['Sweat on the skin evaporates, changing state from "
     "liquid to gas.', 'Changing state needs energy: the latent heat of vaporisation.', 'That "
     "energy is transferred from the skin, so the skin’s temperature falls.'],\n          "
     "herrings: [{ text: 'Sweat is colder than the skin, so it cools it by conduction.', why: "
     "'Sweat comes out at body temperature. The cooling comes from evaporation.' }, { text: "
     "'Evaporating sweat releases energy into the skin.', why: 'Evaporating takes energy in. "
     "Condensing is the change that releases it.' }] },",
     "r3: { command: 'Explain', marks: 3, prompt: 'Ice at 0 °C is put into a drink at 20 °C. "
     "Explain why the drink cools as the ice melts. Put the links in order.',\n          links: "
     "['The ice melts: it changes state from solid to liquid at 0 °C.', 'As it melts, the ice "
     "needs energy, the latent heat of fusion, and this energy is transferred from the drink to "
     "the ice.', 'So "
     "the internal energy of the drink decreases, and its temperature falls.'],\n          "
     "herrings: [{ text: 'The ice gives its cold to the drink.', why: 'Energy moves from the "
     "warmer drink to the ice. There is no cold to pass on.' }, { text: 'Melting ice releases "
     "energy into the drink.', why: 'Melting takes energy in. Freezing is the change that "
     "releases it.' }] },"),
]

# ⊕ 24 Nov 2026 (pupil walk at 390 px): curve() drew 640 wide with 20 to 24-unit labels, so on a phone
# Rung 2's graph of Z squeezed its tick numbers to about 7 px, its A label sat on the line, and the
# card's cooling curve of Y faded at the right (D and "12"). It is drawn again 460 wide with labels of
# 22 units or more (tick numbers 24: 24 x 278 / 460 = 14.5 px in a 278 px box), numbers every 2
# minutes plus 3 (so 3 and 10 can be read), and each letter placed off the line. The card's curve of Y
# drops Design's vial (the green "Y" tube: with no caption it read as a meaningless bar) and uses its
# width. (Re-walk, 24 Nov 2026: tick numbers raised from 19 to 24 units, ticks thinned, vial off.)
LOGIC_EDITS += [
    (('  curve(pts, o) {\n'
     '    const D = window.KS4D; const C = D.C;\n'
     '    const W = o.w || 640, H = 380, L = 92, Rt = o.right || 600, Tp = 28, B = 310;\n'
     '    const X = (x) => L + (Rt - L) * (x / 12), Y = (T) => B - (B - Tp) * (T / 100);\n'
     "    let b = '';\n"
     "    for (let T = 0; T <= 100; T += 10) b += D.line(L, Y(T), Rt, Y(T), 1, '#C9C3B2') + D.line(L - 7, Y(T), L, Y(T), 2) + (T % 20 === 0 ? D.T(L - 11, Y(T) + 8, String(T), 24, { weight: 'normal', fill: C.stroke, anchor: 'end' }) : '');\n"
     "    for (let m = 0; m <= 12; m++) b += D.line(X(m), Tp, X(m), B, 1, '#C9C3B2') + (m % 2 === 0 ? D.T(X(m), B + 30, String(m), 24, { weight: 'normal', fill: C.stroke }) : '');\n"
     '    b += D.line(L, Tp, L, B, 2.5) + D.line(L, B, Rt, B, 2.5);\n'
     '    b += D.T((L + Rt) / 2, H - 12, \'Time / minutes\', 24) + \'<text x="22" y="\' + ((Tp + B) / 2) + \'" transform="rotate(-90 22 \' + ((Tp + B) / 2) + \')" font-family="\' + D.F + \'" font-size="24" font-weight="bold" fill="\' + C.label + \'" text-anchor="middle">Temperature / °C</text>\';\n'
     '    const tEnd = o.tEnd === undefined ? 12 : o.tEnd;\n'
     "    let d = '', last = null;\n"
     '    for (let i = 0; i < pts.length - 1; i++) {\n'
     '      const a = pts[i], c = pts[i + 1];\n'
     '      if (a[0] >= tEnd) break;\n'
     '      const e = Math.min(c[0], tEnd), f = (e - a[0]) / (c[0] - a[0]);\n'
     '      last = [e, a[1] + (c[1] - a[1]) * f];\n'
     "      d += (d ? ' L' : 'M') + X(a[0]).toFixed(1) + ' ' + Y(a[1]).toFixed(1) + ' L' + X(last[0]).toFixed(1) + ' ' + Y(last[1]).toFixed(1);\n"
     '    }\n'
     '    if (d) b += \'<path d="\' + d + \'" fill="none" stroke="\' + C.arrow + \'" stroke-width="4" stroke-linejoin="round" stroke-linecap="round"/>\';\n'
     '    if (o.dot && last && tEnd < 12) b += D.circ(X(last[0]), Y(last[1]), 8, C.gold, C.stroke, 2.5);\n'
     "    if (o.letters && tEnd >= 12) ['A', 'B', 'C', 'D'].forEach((lt, i) => { b += D.circ(X(pts[i][0]), Y(pts[i][1]), 5, C.stroke) + D.T(X(pts[i][0]) + (i === 0 ? 16 : i === 3 ? -14 : 0), Y(pts[i][1]) - 12, lt, 24, { fill: C.stroke }); });\n"
     '    if (o.vial) {\n'
     '      const frozen = tEnd <= 3 ? 0 : tEnd >= 10 ? 1 : (tEnd - 3) / 7;\n'
     '      const vx = 610, top = 96, bot = 286, h = bot - top;\n'
     '      b += \'<rect x="\' + vx + \'" y="\' + top + \'" width="18" height="\' + h + \'" fill="#FFFDF8" stroke="none"/>\';\n'
     '      b += \'<rect x="\' + vx + \'" y="\' + (bot - h * frozen).toFixed(1) + \'" width="18" height="\' + (h * frozen).toFixed(1) + \'" fill="\' + C.nm + \'"/>\';\n'
     '      if (frozen < 0.97) b += \'<rect x="\' + vx + \'" y="\' + (top + 6) + \'" width="18" height="\' + Math.max(0, h * (1 - frozen) - 6).toFixed(1) + \'" fill="\' + C.blue + \'" fill-opacity="0.45"/>\';\n'
     '      b += \'<rect x="\' + vx + \'" y="\' + top + \'" width="18" height="\' + h + \'" rx="9" fill="none" stroke="\' + C.stroke + \'" stroke-width="2.5"/>\' + D.T(vx + 9, top - 12, \'Y\', 20, { fill: C.stroke });\n'
     '    }\n'
     '    return D.svg(W, H, b, o.alt);\n'
     '  }'),
     ('  curve(pts, o) {\n'
     '    const D = window.KS4D; const C = D.C;\n'
     '    const W = o.w || 460, H = 350, L = 84, Rt = o.right || 444, Tp = 26, B = 280;\n'
     '    const X = (x) => L + (Rt - L) * (x / 12), Y = (T) => B - (B - Tp) * (T / 100);\n'
     "    let b = '';\n"
     "    for (let T = 0; T <= 100; T += 10) b += D.line(L, Y(T), Rt, Y(T), 1, '#C9C3B2') + D.line(L - 6, Y(T), L, Y(T), 2) + (T % 20 === 0 ? D.T(L - 9, Y(T) + 8, String(T), 24, { weight: 'normal', fill: C.stroke, anchor: 'end' }) : '');\n"
     '    /* every 2 minutes, plus 3: the flat sections of Y and Z run from 3 to 10 minutes */\n'
     "    for (let m = 0; m <= 12; m++) b += D.line(X(m), Tp, X(m), B, 1, '#C9C3B2') + (m % 2 === 0 || m === 3 ? D.T(X(m), B + 28, String(m), 24, { weight: 'normal', fill: C.stroke }) : '');\n"
     '    b += D.line(L, Tp, L, B, 2.5) + D.line(L, B, Rt, B, 2.5);\n'
     '    b += D.T((L + Rt) / 2, H - 8, \'Time / minutes\', 22) + \'<text x="20" y="\' + ((Tp + B) / 2) + \'" transform="rotate(-90 20 \' + ((Tp + B) / 2) + \')" font-family="\' + D.F + \'" font-size="22" font-weight="bold" fill="\' + C.label + \'" text-anchor="middle">Temperature / °C</text>\';\n'
     '    const tEnd = o.tEnd === undefined ? 12 : o.tEnd;\n'
     "    let d = '', last = null;\n"
     '    for (let i = 0; i < pts.length - 1; i++) {\n'
     '      const a = pts[i], c = pts[i + 1];\n'
     '      if (a[0] >= tEnd) break;\n'
     '      const e = Math.min(c[0], tEnd), f = (e - a[0]) / (c[0] - a[0]);\n'
     '      last = [e, a[1] + (c[1] - a[1]) * f];\n'
     "      d += (d ? ' L' : 'M') + X(a[0]).toFixed(1) + ' ' + Y(a[1]).toFixed(1) + ' L' + X(last[0]).toFixed(1) + ' ' + Y(last[1]).toFixed(1);\n"
     '    }\n'
     '    if (d) b += \'<path d="\' + d + \'" fill="none" stroke="\' + C.arrow + \'" stroke-width="4" stroke-linejoin="round" stroke-linecap="round"/>\';\n'
     '    if (o.dot && last && tEnd < 12) b += D.circ(X(last[0]), Y(last[1]), 7, C.gold, C.stroke, 2.5);\n'
     '    /* each letter sits off the line: a rising curve (Z) and a falling one (Y) take opposite sides */\n'
     '    const up = pts[1][1] > pts[0][1];\n'
     '    const OFF = up ? [[18, 30], [0, -14], [0, 32], [-18, -12]] : [[18, -12], [0, 32], [0, -14], [-18, 30]];\n'
     "    if (o.letters && tEnd >= 12) ['A', 'B', 'C', 'D'].forEach((lt, i) => { b += D.circ(X(pts[i][0]), Y(pts[i][1]), 5, C.stroke) + D.T(X(pts[i][0]) + OFF[i][0], Y(pts[i][1]) + OFF[i][1], lt, 24, { fill: C.stroke }); });\n"
     '    if (o.vial) {\n'
     '      const frozen = tEnd <= 3 ? 0 : tEnd >= 10 ? 1 : (tEnd - 3) / 7;\n'
     '      const vx = Rt + 16, top = 84, bot = 262, h = bot - top;\n'
     '      b += \'<rect x="\' + vx + \'" y="\' + top + \'" width="18" height="\' + h + \'" fill="#FFFDF8" stroke="none"/>\';\n'
     '      b += \'<rect x="\' + vx + \'" y="\' + (bot - h * frozen).toFixed(1) + \'" width="18" height="\' + (h * frozen).toFixed(1) + \'" fill="\' + C.nm + \'"/>\';\n'
     '      if (frozen < 0.97) b += \'<rect x="\' + vx + \'" y="\' + (top + 6) + \'" width="18" height="\' + Math.max(0, h * (1 - frozen) - 6).toFixed(1) + \'" fill="\' + C.blue + \'" fill-opacity="0.45"/>\';\n'
     '      b += \'<rect x="\' + vx + \'" y="\' + top + \'" width="18" height="\' + h + \'" rx="9" fill="none" stroke="\' + C.stroke + \'" stroke-width="2.5"/>\' + D.T(vx + 9, top - 12, \'Y\', 20, { fill: C.stroke });\n'
     '    }\n'
     '    return D.svg(W, H, b, o.alt);\n'
     '  }\n'
     '')),
    ("vial: true, right: 570,", ""),
]

# ⊕ 24 Nov 2026 (pupil walk at 390 px): numbers, number-and-unit pairs and short equations in the
# page's worked examples and Your turn questions broke across lines ("27 / 000 J", "100 / °C",
# "E = m / L"). No-break spaces (U+00A0) inside them, in the worked-example text only: no rung,
# option or answer key is touched. Written by the same rule as the cards (docs table, M3).
LOGIC_EDITS += [
    ("head: 'Steam condenses on a cold window and releases 45.2 kJ. Calculate the mass of steam that condensed. (Lv = 2.26 MJ/kg)'",
     "head: 'Steam condenses on a cold window and releases 45.2\xa0kJ. Calculate the mass of steam that condensed. (Lv = 2.26\xa0MJ/kg)'"),
    ("line: '45.2 kJ × 1000 = 45 200 J; 2.26 MJ/kg × 1 000 000 = 2 260 000 J/kg'",
     "line: '45.2\xa0kJ × 1000 = 45\xa0200\xa0J; 2.26\xa0MJ/kg × 1\xa0000\xa0000 = 2\xa0260\xa0000\xa0J/kg'"),
    ("line: 'E = m × L'",
     "line: 'E\xa0=\xa0m\xa0×\xa0L'"),
    ("line: '45 200 = m × 2 260 000'",
     "line: '45\xa0200 = m × 2\xa0260\xa0000'"),
    ("line: 'm = 45 200 ÷ 2 260 000 = 0.020'",
     "line: 'm = 45\xa0200 ÷ 2\xa0260\xa0000 = 0.020'"),
    ("line: 'm = 0.020 kg (20 g)'",
     "line: 'm = 0.020\xa0kg (20\xa0g)'"),
    ("note: 'Converting only L gives 45.2 ÷ 2 260 000 = 0.00002 kg (0.02 g): a thousand times too small.'",
     "note: 'Converting only L gives 45.2 ÷ 2\xa0260\xa0000 = 0.00002\xa0kg (0.02\xa0g): a thousand times too small.'"),
    ("head: 'Calculate the energy needed to melt 250 g of ice at 0 °C. (Lf = 334 000 J/kg)'",
     "head: 'Calculate the energy needed to melt 250\xa0g of ice at 0\xa0°C. (Lf = 334\xa0000\xa0J/kg)'"),
    ("line: '250 g ÷ 1000 = 0.25 kg'",
     "line: '250\xa0g ÷ 1000 = 0.25\xa0kg'"),
    ("line: 'm = 0.25 kg, L = 334 000 J/kg'",
     "line: 'm = 0.25\xa0kg, L = 334\xa0000\xa0J/kg'"),
    ("line: 'E = 0.25 × 334 000'",
     "line: 'E = 0.25 × 334\xa0000'"),
    ("line: 'E = 83 500 J (83.5 kJ)'",
     "line: 'E = 83\xa0500\xa0J (83.5\xa0kJ)'"),
    ("note: 'Left in grams, 250 × 334 000 = 83 500 000 J: a thousand times too big.'",
     "note: 'Left in grams, 250 × 334\xa0000 = 83\xa0500\xa0000\xa0J: a thousand times too big.'"),
    ("head: 'It takes 316 000 J to melt 0.80 kg of a metal at its melting point. Calculate the metal’s specific latent heat of fusion.'",
     "head: 'It takes 316\xa0000\xa0J to melt 0.80\xa0kg of a metal at its melting point. Calculate the metal’s specific latent heat of fusion.'"),
    ("close: 'Check: 0.80 × 395 000 = 316 000 J.'",
     "close: 'Check: 0.80 × 395\xa0000 = 316\xa0000\xa0J.'"),
    ("line: '316 000 = 0.80 × L'",
     "line: '316\xa0000 = 0.80 × L'"),
    ("line: 'L = 316 000 ÷ 0.80 = 395 000'",
     "line: 'L = 316\xa0000 ÷ 0.80 = 395\xa0000'"),
    ("line: 'L = 395 000 J/kg'",
     "line: 'L = 395\xa0000\xa0J/kg'"),
    ("head: '200 g of water at 20 °C is heated until it has all turned to steam at 100 °C. Calculate the total energy needed. (c = 4200 J/kg °C, Lv = 2 260 000 J/kg)'",
     "head: '200\xa0g of water at 20\xa0°C is heated until it has all turned to steam at 100\xa0°C. Calculate the total energy needed. (c = 4200\xa0J/kg\xa0°C, Lv = 2\xa0260\xa0000\xa0J/kg)'"),
    ("line: '200 g ÷ 1000 = 0.20 kg'",
     "line: '200\xa0g ÷ 1000 = 0.20\xa0kg'"),
    ("line: 'Heating: ΔE = m c Δθ. Boiling: E = m L.'",
     "line: 'Heating: ΔE\xa0=\xa0m\xa0c\xa0Δθ. Boiling: E\xa0=\xa0m\xa0L.'"),
    ("line: 'ΔE = 0.20 × 4200 × 80; E = 0.20 × 2 260 000'",
     "line: 'ΔE = 0.20 × 4200 × 80; E = 0.20 × 2\xa0260\xa0000'"),
    ("line: '67 200 + 452 000 = 519 200'",
     "line: '67\xa0200 + 452\xa0000 = 519\xa0200'"),
    ("line: 'Total energy = 519 200 J'",
     "line: 'Total energy = 519\xa0200\xa0J'"),
    ("head: 'Calculate the energy needed to boil away 1.5 kg of water at 100 °C. (Lv = 2 260 000 J/kg)'",
     "head: 'Calculate the energy needed to boil away 1.5\xa0kg of water at 100\xa0°C. (Lv = 2\xa0260\xa0000\xa0J/kg)'"),
    ("close: 'No Δθ anywhere: the temperature stays at 100 °C the whole time.'",
     "close: 'No Δθ anywhere: the temperature stays at 100\xa0°C the whole time.'"),
    ("line: 'm = 1.5 kg, L = 2 260 000 J/kg'",
     "line: 'm = 1.5\xa0kg, L = 2\xa0260\xa0000\xa0J/kg'"),
    ("line: 'E = 1.5 × 2 260 000'",
     "line: 'E = 1.5 × 2\xa0260\xa0000'"),
    ("line: 'E = 3 390 000 J'",
     "line: 'E = 3\xa0390\xa0000\xa0J'"),
    ("head: '400 g of water at 0 °C freezes. Calculate the energy it releases. (Lf = 334 000 J/kg)'",
     "head: '400\xa0g of water at 0\xa0°C freezes. Calculate the energy it releases. (Lf = 334\xa0000\xa0J/kg)'"),
    ("line: '400 g ÷ 1000 = 0.40 kg'",
     "line: '400\xa0g ÷ 1000 = 0.40\xa0kg'"),
    ("line: 'm = 0.40 kg, L = 334 000 J/kg'",
     "line: 'm = 0.40\xa0kg, L = 334\xa0000\xa0J/kg'"),
    ("line: 'E = 0.40 × 334 000'",
     "line: 'E = 0.40 × 334\xa0000'"),
    ("line: 'E = 133 600 J'",
     "line: 'E = 133\xa0600\xa0J'"),
]

# ⊕ 24 Nov 2026 (re-walk at 390 px): rung STEMS only get no-break spaces inside numbers and
# number-unit pairs ("(c = 385 J/kg °C)", "a drink at 20 °C" split across lines). Rung ids are by
# position, so the ids hold; no option text or answer key is touched.
LOGIC_EDITS += [
    ("prompt: 'Name the energy needed to change 1 kg of a liquid into a gas with no change in temperature.'",
     "prompt: 'Name the energy needed to change 1\xa0kg of a liquid into a gas with no change in temperature.'"),
    ("prompt: 'Solid Z is heated by a 50 W heater, and all of the energy goes into Z. The graph shows its temperature. Z’s specific latent heat of fusion is 84 000 J/kg. Calculate the mass of Z. Work it on paper, then choose the conversion and give the answer and unit.'",
     "prompt: 'Solid Z is heated by a 50\xa0W heater, and all of the energy goes into Z. The graph shows its temperature. Z’s specific latent heat of fusion is 84\xa0000\xa0J/kg. Calculate the mass of Z. Work it on paper, then choose the conversion and give the answer and unit.'"),
    ("prompt: 'A 2.5 g piece of crushed ice at 0 °C melts in a drink. Calculate the energy it takes in. (Lf = 334 000 J/kg) Work it on paper, then choose the conversion and give the answer and unit.'",
     "prompt: 'A 2.5\xa0g piece of crushed ice at 0\xa0°C melts in a drink. Calculate the energy it takes in. (Lf = 334\xa0000\xa0J/kg) Work it on paper, then choose the conversion and give the answer and unit.'"),
    ("prompt: 'Ice at 0 °C is put into a drink at 20 °C. Explain why the drink cools as the ice melts. Put the links in order.'",
     "prompt: 'Ice at 0\xa0°C is put into a drink at 20\xa0°C. Explain why the drink cools as the ice melts. Put the links in order.'"),
]

LESSON = {
    "slug": "specific-latent-heat",
    "start": {
        "setup": "A splash of boiling water and a puff of steam are both at 100\u00a0°C. The steam "
                 "gives a much worse burn.",
        "question": "If you had to guess, is that because the steam spreads over more skin, or "
                    "because it gives the skin more energy?",
        "options": [
            ("It spreads over more skin",
             "It gives the skin more energy. The steam condenses into water on your skin, and "
             "condensing releases a lot of energy with no change in temperature."),
            ("It gives the skin more energy",
             "It gives the skin more energy. The steam condenses into water on your skin, and "
             "condensing releases a lot of energy with no change in temperature."),
        ],
        "answer": 1,
    },
    "words": ["latent heat", "specific latent heat", "fusion", "vaporisation"],
    "knowledge": [
        {"kind": "card", "title": "Latent heat",
         "body": ["The energy needed for a substance to change state is called latent heat.",
                  "When a change of state occurs, the energy supplied changes the energy stored "
                  "(internal energy) but not the temperature."]},
        {"kind": "card", "title": "Specific latent heat",
         "body": ["The specific latent heat of a substance is the amount of energy required to "
                  "change the state of one kilogram of the substance with no change in "
                  "temperature.",
                  {"points": [
                      "Specific latent heat of fusion: change of state from solid to liquid.",
                      "Specific latent heat of vaporisation: change of state from liquid to "
                      "vapour.",
                      "Freezing and condensing transfer the same amount of energy back out.",
                  ]}]},
        {"kind": "card", "title": "The equation",
         "body": ["E\u00a0=\u00a0m\u00a0L",
                  {"points": ["energy, E, in joules (J)",
                              "mass, m, in kilograms (kg)",
                              "specific latent heat, L, in joules per kilogram (J/kg)"]},
                  "This equation is on the Physics equation sheet. You need to be able to use it "
                  "and rearrange it.",
                  {"slot": "triangle:EQ_SLH"}]},
        {"kind": "card", "title": "Worked examples",
         "body": [{"slot": "cfifa"}]},
        {"kind": "card", "title": "Heating and cooling graphs",
         "body": [{"slot": "legacy-fig:loggerFig"},
                  "Liquid Y cools in a cold room. On a graph of temperature against time:",
                  {"points": [
                      "A sloping section: the temperature changes and the state does not. Use "
                      "ΔE\u00a0=\u00a0m\u00a0c\u00a0Δθ.",
                      "A flat section: the state changes and the temperature does not. Use "
                      "E\u00a0=\u00a0m\u00a0L.",
                      "B to C is Y freezing at 50\u00a0°C.",
                  ]}]},
        {"kind": "card", "title": "Energy from a flat section",
         "body": ["The 60\u00a0g of Y transfers energy to the room at a steady 30\u00a0J every second "
                  "(30\u00a0W).",
                  {"points": [
                      "The flat section lasts from 3 to 10\u00a0minutes: 7\u00a0minutes, which is 420\u00a0s.",
                      "Energy transferred: E\u00a0=\u00a0P\u00a0t = 30 × 420 = 12\u00a0600\u00a0J.",
                      "Specific latent heat of fusion: L\u00a0=\u00a0E\u00a0÷\u00a0m = 12\u00a0600 ÷ 0.060 = 210\u00a0000\u00a0J/kg.",
                  ]}]},
        {"kind": "card", "title": "Measuring the specific latent heat of fusion of water",
         "body": [{"points": [
             "Put an immersion heater in a funnel of crushed ice, with a beaker underneath.",
             "Switch the heater on. Start timing once water drips steadily from the heated "
             "funnel.",
             "After a set time, measure the energy supplied with a joulemeter, and the mass of "
             "water that has melted.",
             "Set up a second funnel of ice with no heater, for the same time. Take away the mass "
             "of water it melts: that ice was melted by the warm room, not the heater.",
             "Then L\u00a0=\u00a0E\u00a0÷\u00a0m.",
         ]}]},
        {"kind": "reveal", "title": "Specific heat capacity (c) or specific latent heat (L)",
         "cols": ["c", "L"],
         "rows": [
             ("What changes", "Temperature", "State"),
             ("Equation", "ΔE\u00a0=\u00a0m\u00a0c\u00a0Δθ", "E\u00a0=\u00a0m\u00a0L"),
             ("Unit", "J/kg\u00a0°C", "J/kg"),
             ("On a heating graph", "A sloping section", "A flat section"),
         ]},
        {"kind": "card", "title": "Easy mistakes",
         "body": [{"mistakes": [
             ("The temperature stays the same, so no energy is transferred.",
              "Energy is transferred. It changes the internal energy, but not the temperature."),
             ("Use ΔE\u00a0=\u00a0m\u00a0c\u00a0Δθ for a change of state.",
              "During a change of state Δθ = 0. Use E\u00a0=\u00a0m\u00a0L."),
             ("The latent heat of fusion is for boiling.",
              "Fusion is melting, solid to liquid. Vaporisation is liquid to vapour."),
         ]}]},
    ],
    "key_fact": "The specific latent heat of a substance is the energy needed to change the state "
                "of 1\u00a0kg of it with no change in temperature. Energy for a change of state = mass "
                "× specific latent heat. During a change of state, the energy supplied changes the "
                "internal energy but not the temperature.",
    "deeper": [
        {"kind": "card", "title": "Water's values",
         "body": ["For water, the specific latent heat of fusion is 334\u00a0000\u00a0J/kg and the specific "
                  "latent heat of vaporisation is 2\u00a0260\u00a0000\u00a0J/kg. Boiling 1\u00a0kg of water takes "
                  "almost seven times the energy of melting 1\u00a0kg of ice."]},
        {"kind": "card", "title": "More than one stage",
         "body": ["Ice at −10\u00a0°C heated to water at 20\u00a0°C goes through three stages: the ice warms "
                  "(ΔE\u00a0=\u00a0m\u00a0c\u00a0Δθ), the ice melts (E\u00a0=\u00a0m\u00a0L), the water warms (ΔE\u00a0=\u00a0m\u00a0c\u00a0Δθ). Work out "
                  "each one, then add them."]},
        {"kind": "card", "title": "Why sweating cools you",
         "body": ["Sweat evaporates from the skin. Evaporating needs energy, the latent heat of "
                  "vaporisation, and this energy is transferred from the skin, so the skin "
                  "cools."]},
        {"kind": "card", "title": "Command words",
         "body": [{"points": [
             "<strong>Determine</strong>: get it from the graph, for example a time from where a "
             "flat section starts and ends.",
             "<strong>Calculate</strong>: write every line. With two stages, use one equation for "
             "each, then add.",
             "<strong>Compare</strong>: say how both are alike and how they differ, naming both "
             "each time.",
         ]}]},
    ],
    "try": None,
    "legacy": {"batch": "batch-3", "logic_edits": LOGIC_EDITS},
    "equations": {
        "EQ_SLH": {"name": "Specific latent heat",
                   "written": "energy for a change of state = mass × specific latent heat",
                   "source": "none",
                   "top": {"s": "E", "name": "energy", "unit": "J"},
                   "bottom": [{"s": "m", "name": "mass", "unit": "kg"},
                              {"s": "L", "name": "specific latent heat", "unit": "J/kg"}]},
    },
}
