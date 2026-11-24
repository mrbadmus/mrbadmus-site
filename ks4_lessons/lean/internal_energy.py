# -*- coding: utf-8 -*-
"""Internal energy, in the lean shape. Spec table: ks4-internal-energy.md (AQA 8464 6.3.2.1 /
8463 4.3.2.1, word for word the same). No HT-only or physics-only line. Every route gets the same
lesson.

LEGACY (batch 2, Ks4Ladder). The ladder (r1..r4) and the practice set stay from the Design page.
The practice set reads the route's `quiz` list (K.bank): five per route, both old stems kept word
for word. The cooling curve (`coolFig`) is drawn by the legacy logic with no state, so the card
places it through a legacy-fig slot.

LOGIC_EDITS:
  1. The Combined eyebrow read "AQA Physics (8464) 6.3.2.1": 8464 is AQA Combined Science, so it
     is written as the other lean physics pages write it.
  2. Rung 1 was practice question 1 (K.find on "Its temperature stays constant for several
     minutes"), so a pupil met it twice. It is now its own question, the definition of internal
     energy, through K.item, as metal-hydroxides did on 22 Nov 2026. Its position, and so its id
     (ks4:internal-energy:<route>#r1), is kept; its options and answer key are new.
  3. Rung 3 (stearic acid freezing): its first two links could be put in either order. Link 2
     now reads "While it freezes, ...", so it follows from link 1 (examiner review, 24 Nov 2026)."""

LOGIC_EDITS = [
    ("'AQA Physics (8464) 6.3.2.1 · Model'", "'AQA Combined Science (8464) 6.3.2.1 · Model'"),
    ("r1: Object.assign(K.find(slug, R.route, 'Its temperature stays constant for several "
     "minutes') || { options: [] }, { command: 'Identify', marks: 1, why: 'At constant power, a "
     "flat section means a change of state: the energy raises the particles’ potential energy, not "
     "their kinetic energy.' }),",
     "r1: Object.assign(K.item({ q: 'Define the internal energy of a system.', opts: [['The total "
     "kinetic energy and potential energy of all the particles in the system', true], ['The "
     "average kinetic energy of the particles that make up the system', false], ['The energy "
     "needed to raise the temperature of 1 kg of the system by 1 °C', false], ['The total kinetic "
     "energy of all the particles, not counting their potential energy', false]], "
     "wrong_explanations: { '1': 'The average kinetic energy is linked to the temperature. "
     "Internal energy is a total, of kinetic and potential energy.', '2': 'That is specific heat "
     "capacity.', '3': 'Internal energy includes the potential energy of the particles too.' } }), "
     "{ command: 'Define', marks: 1, why: 'Internal energy is the total kinetic energy and "
     "potential energy of all the particles (atoms and molecules) that make up a system.' }),"),
    # 3. Rung 3 (stearic acid): links 1 and 2 could be swapped. Link 2 now starts from the
    # freezing that link 1 names, so the chain has one right order.
    ("'Energy is still being transferred to the surroundings, so its internal energy decreases.'",
     "'While it freezes, energy is still transferred to the surroundings, so its internal energy "
     "decreases.'"),
]

# ⊕ 24 Nov 2026 (pupil walk at 390 px): the heating and cooling curves were drawn 640 wide with
# 20-unit labels, so the phone text floor (11px x viewBox / smallest font, ks4-lesson.css) made them
# about 352 px wide: in the ~278 px rung box Rung 2's E and F were off screen while part 3 asks about
# D to E, and the cooling curve lost its tail after E. curve() is drawn again 440 wide with 18-unit
# labels (11 x 440 / 18 = 269 px), so the whole graph fits; the data, letters and alt text are
# unchanged. Rung 2's A label moves below the line (it sat on the rising line at the new scale).
LOGIC_EDITS += [
    (('  curve(pts, o) {\n'
     '    const D = window.KS4D; const C = D.C;\n'
     '    const W = 640, H = 360, L = 90, Rt = 612, Tp = 30, B = 300;\n'
     '    const X = (x) => L + (Rt - L) * (x / o.tmax), Y = (T) => B - (B - Tp) * ((T - o.Tmin) / (o.Tmax - o.Tmin));\n'
     '    let b = D.line(L, Tp, L, B, 2.5) + D.line(L, B, Rt, B, 2.5);\n'
     "    for (let T = o.Tmin; T <= o.Tmax; T += o.step) b += D.line(L - 8, Y(T), L, Y(T), 2) + D.T(L - 14, Y(T) + 6, (T < 0 ? '−' : '') + Math.abs(T), 20, { weight: 'normal', fill: C.stroke, anchor: 'end' }) + D.line(L, Y(T), Rt, Y(T), 1, '#C9C3B2');\n"
     '    b += D.T((L + Rt) / 2, H - 22, \'Time\', 22) + \'<text x="24" y="\' + ((Tp + B) / 2) + \'" transform="rotate(-90 24 \' + ((Tp + B) / 2) + \')" font-family="\' + D.F + \'" font-size="22" font-weight="bold" fill="\' + C.label + \'" text-anchor="middle">Temperature / °C</text>\';\n'
     "    let d = '';\n"
     '    const tEnd = o.tEnd === undefined ? o.tmax : o.tEnd;\n'
     '    for (let i = 0; i < pts.length - 1; i++) {\n'
     '      const a = pts[i], c = pts[i + 1];\n'
     '      if (a[0] >= tEnd) break;\n'
     '      const e = Math.min(c[0], tEnd), f = (e - a[0]) / (c[0] - a[0]);\n'
     "      d += (d ? ' L' : 'M') + X(a[0]).toFixed(1) + ' ' + Y(a[1]).toFixed(1) + ' L' + X(e).toFixed(1) + ' ' + Y(a[1] + (c[1] - a[1]) * f).toFixed(1);\n"
     '    }\n'
     '    if (d) b += \'<path d="\' + d + \'" fill="none" stroke="\' + C.arrow + \'" stroke-width="4" stroke-linejoin="round" stroke-linecap="round"/>\';\n'
     '    (o.letters || []).forEach((lt, i) => { if (lt && lt.t && pts[i] && pts[i][0] <= tEnd) b += D.circ(X(pts[i][0]), Y(pts[i][1]), 6, C.stroke) + D.T(X(pts[i][0]) + (lt.dx || 0), Y(pts[i][1]) + (lt.dy || -14), lt.t, 22, { fill: C.stroke }); });\n'
     '    (o.notes || []).forEach((n) => { if (n.at <= tEnd) b += D.T(X(n.x), Y(n.T) - 14, n.t, 21, { fill: C.arrow }); });\n'
     '    return D.svg(W, H, b, o.alt);\n'
     '  }'),
     ('  curve(pts, o) {\n'
     '    const D = window.KS4D; const C = D.C;\n'
     '    const W = 440, H = 330, L = 68, Rt = 420, Tp = 24, B = 270;\n'
     '    const X = (x) => L + (Rt - L) * (x / o.tmax), Y = (T) => B - (B - Tp) * ((T - o.Tmin) / (o.Tmax - o.Tmin));\n'
     '    let b = D.line(L, Tp, L, B, 2.5) + D.line(L, B, Rt, B, 2.5);\n'
     "    for (let T = o.Tmin; T <= o.Tmax; T += o.step) b += D.line(L - 7, Y(T), L, Y(T), 2) + D.T(L - 11, Y(T) + 6, (T < 0 ? '−' : '') + Math.abs(T), 18, { weight: 'normal', fill: C.stroke, anchor: 'end' }) + D.line(L, Y(T), Rt, Y(T), 1, '#C9C3B2');\n"
     '    b += D.T((L + Rt) / 2, H - 18, \'Time\', 18) + \'<text x="16" y="\' + ((Tp + B) / 2) + \'" transform="rotate(-90 16 \' + ((Tp + B) / 2) + \')" font-family="\' + D.F + \'" font-size="18" font-weight="bold" fill="\' + C.label + \'" text-anchor="middle">Temperature / °C</text>\';\n'
     "    let d = '';\n"
     '    const tEnd = o.tEnd === undefined ? o.tmax : o.tEnd;\n'
     '    for (let i = 0; i < pts.length - 1; i++) {\n'
     '      const a = pts[i], c = pts[i + 1];\n'
     '      if (a[0] >= tEnd) break;\n'
     '      const e = Math.min(c[0], tEnd), f = (e - a[0]) / (c[0] - a[0]);\n'
     "      d += (d ? ' L' : 'M') + X(a[0]).toFixed(1) + ' ' + Y(a[1]).toFixed(1) + ' L' + X(e).toFixed(1) + ' ' + Y(a[1] + (c[1] - a[1]) * f).toFixed(1);\n"
     '    }\n'
     '    if (d) b += \'<path d="\' + d + \'" fill="none" stroke="\' + C.arrow + \'" stroke-width="4" stroke-linejoin="round" stroke-linecap="round"/>\';\n'
     '    (o.letters || []).forEach((lt, i) => { if (lt && lt.t && pts[i] && pts[i][0] <= tEnd) b += D.circ(X(pts[i][0]), Y(pts[i][1]), 5, C.stroke) + D.T(X(pts[i][0]) + (lt.dx || 0), Y(pts[i][1]) + (lt.dy || -12), lt.t, 20, { fill: C.stroke }); });\n'
     '    (o.notes || []).forEach((n) => { if (n.at <= tEnd) b += D.T(X(n.x), Y(n.T) - 12, n.t, 18, { fill: C.arrow }); });\n'
     '    return D.svg(W, H, b, o.alt);\n'
     '  }\n'
     '')),
    ("letters: [{ t: 'A', dx: 18, dy: -4 }", "letters: [{ t: 'A', dx: 16, dy: 22 }"),
]

LESSON = {
    "slug": "internal-energy",
    "start": {
        "setup": "A pan of water is boiling. A thermometer in the water reads 100\u00a0°C. You turn the "
                 "heat up to full.",
        "question": "If you had to guess, does the thermometer reading go up, or stay at 100\u00a0°C?",
        "options": [
            ("It goes up",
             "It stays at 100\u00a0°C. The extra energy makes the water boil away faster. It goes "
             "into the particles' potential energy, and the temperature does not rise."),
            ("It stays at 100 °C",
             "It stays at 100\u00a0°C. The extra energy makes the water boil away faster. It goes "
             "into the particles' potential energy, and the temperature does not rise."),
        ],
        "answer": 1,
    },
    "words": ["internal energy", "kinetic energy", "potential energy", "change of state"],
    "knowledge": [
        {"kind": "card", "title": "Energy stored by particles",
         "body": ["Energy is stored inside a system by the particles (atoms and molecules) that "
                  "make up the system. This is called internal energy.",
                  {"points": [
                      "The particles move, so they have kinetic energy.",
                      "There are forces between the particles, so they also have potential "
                      "energy. It depends on how far apart they are.",
                  ]},
                  "Internal energy is the total kinetic energy and potential energy of all the "
                  "particles (atoms and molecules) that make up a system."]},
        {"kind": "card", "title": "What heating does",
         "body": ["Heating changes the energy stored within the system by increasing the energy "
                  "of the particles that make up the system. This either raises the temperature "
                  "of the system or produces a change of state.",
                  {"points": [
                      "The temperature rises: the particles move faster, so their kinetic energy "
                      "increases.",
                      "The state changes: the energy goes into the particles' potential energy. "
                      "The temperature stays the same until the change of state is complete.",
                  ]}]},
        {"kind": "reveal", "title": "Heating ice until it boils",
         "cols": ["Temperature", "Energy that increases"],
         "rows": [
             ("Ice warms from −10\u00a0°C to 0\u00a0°C", "Rises", "Kinetic"),
             ("Ice melts at 0\u00a0°C", "Stays at 0\u00a0°C", "Potential"),
             ("Water warms from 0\u00a0°C to 100\u00a0°C", "Rises", "Kinetic"),
             ("Water boils at 100\u00a0°C", "Stays at 100\u00a0°C", "Potential"),
         ]},
        {"kind": "card", "title": "Reading a cooling curve",
         "body": [{"slot": "legacy-fig:coolFig"},
                  "Energy leaves the substance all the time, so its internal energy falls along "
                  "the whole curve.",
                  {"points": [
                      "A sloping section: the temperature falls. The particles' kinetic energy "
                      "decreases.",
                      "A flat section: the substance changes state. The particles' potential "
                      "energy decreases, and the temperature stays the same.",
                      "B to C is the gas condensing at 90\u00a0°C. D to E is the liquid freezing at "
                      "40\u00a0°C.",
                  ]}]},
        {"kind": "card", "title": "Temperature and internal energy",
         "body": ["The temperature depends on the average kinetic energy of the particles. "
                  "Internal energy is the total energy of every particle, kinetic and potential.",
                  {"points": [
                      "A bath of warm water has more internal energy than a cup of hot tea. It "
                      "has far more particles.",
                      "1\u00a0kg of water at 0\u00a0°C has more internal energy than 1\u00a0kg of ice at 0\u00a0°C. "
                      "Melting raised the particles' potential energy.",
                  ]}]},
        {"kind": "card", "title": "Easy mistakes",
         "body": [{"mistakes": [
             ("Internal energy is the kinetic energy of the particles.",
              "It is the total kinetic energy and potential energy of all the particles."),
             ("Heating always makes the temperature rise.",
              "During a change of state the internal energy rises, but the temperature stays the "
              "same."),
             ("The hotter object always has more internal energy.",
              "Internal energy also depends on how many particles there are. A big, cool object "
              "can have more."),
         ]}]},
    ],
    "key_fact": "Internal energy is the total kinetic energy and potential energy of all the "
                "particles in a system. Heating increases the energy of the particles: it either "
                "raises the temperature or produces a change of state.",
    "deeper": [
        {"kind": "card", "title": "The two equations",
         "body": [{"points": [
             "Raising the temperature: ΔE\u00a0=\u00a0m\u00a0c\u00a0Δθ, in the lesson on specific heat capacity.",
             "Changing the state: E\u00a0=\u00a0m\u00a0L, in the lesson on specific latent heat.",
         ]}]},
        {"kind": "card", "title": "Command words",
         "body": [{"points": [
             "<strong>Determine</strong>: read it from the graph. A flat section gives a melting "
             "or boiling point.",
             "<strong>Describe</strong>: say what happens at each stage, in order, using the "
             "particles.",
             "<strong>Explain</strong>: link each step: energy in or out, which energy of the "
             "particles changes, what the temperature does.",
         ]}]},
    ],
    "try": None,
    "legacy": {"batch": "batch-2", "logic_edits": LOGIC_EDITS},
}
