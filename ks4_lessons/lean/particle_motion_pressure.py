# -*- coding: utf-8 -*-
"""Particle motion in gases, in the lean shape. Spec table: ks4-particle-motion-pressure.md
(AQA 8464 6.3.3.1 on CF CH; 8463 4.3.3.1 and 4.3.3.2 (physics only) on TF TH, and 4.3.3.3
(physics only, HT only) on TH). The Design page already taught 4.3.3.2 and 4.3.3.3 on the Triple
routes (its piston bench, pV worked examples and the bicycle-pump Rung 4), so they stay in this
lesson, as route-gated cards: no new lesson is needed.

LEGACY (batch 3, Ks4Ladder). The ladder (r1..r4, which differs by route), the pV worked examples
and Your turn questions (cfExamples / cfQuestions, placed by the `cfifa` slot in a Triple-only card;
cfExamples is empty on Combined) and the practice set stay from the Design page. Its eyebrow is
route-aware already: "AQA Combined Science (8464) 6.3.3.1", "AQA Physics (8463) 4.3.3.1–4.3.3.2"
on TF and "4.3.3.1–4.3.3.3" on TH. The practice set reads the route's `quiz` list (K.bank): five
per route, both old stems kept word for word; the fifth question is a pV calculation on TF TH only.

pV = constant is on the Physics equation sheet (8463 Appendix, sheet equation 12). It is physics
only, so it is never on a Combined page.

PRE_EDITS (lean_ks4 `pre_edits`, made before the rail edits): the page keeps two rails, RAIL_BASE
and RAIL_TRIPLE, picks one per route, and ticks a per-route done[]. The lean page has one rail for
every route (Start here, Key knowledge, Practice), so RAIL_TRIPLE goes, RAIL_BASE becomes RAIL, the
two per-route picks read RAIL, and done[] becomes one plain array for the rail edit to replace."""

PRE_EDITS = [
    ("const RAIL_TRIPLE = [\n"
     "  { id: 's-hook', label: 'An empty can', short: 'HOOK' },\n"
     "  { id: 's-bench', label: 'The gas bench', short: 'BENCH' },\n"
     "  { id: 's-mark', label: 'Mark it', short: 'MARK' },\n"
     "  { id: 's-piston', label: 'The piston bench', short: 'PISTON' },\n"
     "  { id: 's-calc', label: 'Calculate pV', short: 'CFIFA' },\n"
     "  { id: 's-ladder', label: 'Exam ladder', short: 'LADDER' }\n"
     "];", ""),
    ("const RAIL_BASE = [", "const RAIL = ["),
    ("this.rail = window.KS4.route(this).isTriple ? RAIL_TRIPLE : RAIL_BASE;", "this.rail = RAIL;"),
    ("    const RAIL = tri ? RAIL_TRIPLE : RAIL_BASE;\n", ""),
    ("const done = tri ? [s.hook !== null, benchAll, s.mark, pistonAll, s.calc >= 2, s.ladder] "
     ": [s.hook !== null, benchAll, s.mark, s.ladder];",
     "const done = [s.hook !== null, s.ladder];"),
]

# LOGIC_EDITS (examiner review, 24 Nov 2026): the TH worked example "Find a volume" reduced the
# pressure to 120 kPa, so its Fine-tune line read "V₂ = 120 ÷ 120", the same number twice, which
# hides what is being divided by what. The new pressure is 100 kPa: V₂ = 120 ÷ 100 = 1.2 m³.
# That made it the twin of TH Your turn question 1 (2400 kPa × 0.050 m³ into 100 kPa, also
# 120 ÷ 100 = 1.2 m³), so the worked example would have given the answer away: the Your-turn
# cylinder now holds 0.030 m³, so 72 ÷ 100 = 0.72 m³. Its edits come first, while its lines are
# still the only ones that read "120 ÷ 100" and "1.2 m³".
LOGIC_EDITS = [
    ("A gas cylinder holds 0.050 m³ of gas at 2400 kPa.", "A gas cylinder holds 0.030 m³ of gas at 2400 kPa."),
    ("Check: 100 × 1.2 = 120 = 2400 × 0.050.", "Check: 100 × 0.72 = 72 = 2400 × 0.030."),
    ("line: '2400 × 0.050 = 100 × V₂'", "line: '2400 × 0.030 = 100 × V₂'"),
    ("line: 'V₂ = 120 ÷ 100 = 1.2' }", "line: 'V₂ = 72 ÷ 100 = 0.72' }"),
    ("line: 'V₂ = 1.2 m³' }", "line: 'V₂ = 0.72 m³' }"),
    ("The pressure is reduced to 120 kPa. Calculate the new volume.",
     "The pressure is reduced to 100 kPa. Calculate the new volume."),
    ("'150 × 0.80 = 120 × V₂'", "'150 × 0.80 = 100 × V₂'"),
    ("'V₂ = 120 ÷ 120 = 1.0'", "'V₂ = 120 ÷ 100 = 1.2'"),
    ("'V₂ = 1.0 m³'", "'V₂ = 1.2 m³'"),
]

# ⊕ 24 Nov 2026 (pupil walk at 390 px): Rung 2's pressure tables (CF and CH) were 540 wide with
# 19-unit headings, so a phone drew them 312 px wide and clipped the right border. Narrower columns
# (11 x 390 / 19 = 226 px). The CH table's 50 °C reading becomes 108 kPa: from 95 kPa at 10 °C
# (283 K), p is proportional to T in kelvin, so 323 K gives 108.4 kPa. The keyed 126 kPa at 100 °C
# (the rule gives 125.2) is still the only option near the trend (109, 113, 126, 218 kPa); its
# feedback now says so. CF option "It doubles each time the °C doubles" is reworded; still wrong.
LOGIC_EDITS += [
    ("widths: [260, 240]", "widths: [190, 160]"),
    ("['50', '109']", "['50', '108']"),
    ("at 50, 109", "at 50, 108"),
    ("'It doubles each time the °C doubles'", "'It doubles when the temperature in °C doubles'"),
    ("so it reaches about 126 kPa at 100 °C.'", "so it reaches about 125 kPa at 100 °C: 126 kPa is the closest option.'"),
    ("'100 °C is 50 °C above the last reading: 109 + 50 ÷ 3 ≈ 126 kPa.'",
     "'100 °C is 50 °C above the last reading: 108 + 50 ÷ 3 ≈ 125 kPa, so 126 kPa.'"),
]

# ⊕ 24 Nov 2026 (pupil walk at 390 px): numbers, number-and-unit pairs and short equations in the
# page's worked examples and Your turn questions broke across lines ("27 / 000 J", "100 / °C",
# "E = m / L"). No-break spaces (U+00A0) inside them, in the worked-example text only: no rung,
# option or answer key is touched. Written by the same rule as the cards (docs table, M3).
LOGIC_EDITS += [
    ("head: 'A fixed mass of gas at constant temperature has a volume of 0.80 m³ at 150 kPa. The pressure is reduced to 100 kPa. Calculate the new volume.'",
     "head: 'A fixed mass of gas at constant temperature has a volume of 0.80\xa0m³ at 150\xa0kPa. The pressure is reduced to 100\xa0kPa. Calculate the new volume.'"),
    ("line: 'p₁V₁ = p₂V₂'",
     "line: 'p₁V₁\xa0=\xa0p₂V₂'"),
    ("line: 'V₂ = 1.2 m³'",
     "line: 'V₂ = 1.2\xa0m³'"),
    ("head: 'A gas at 100 kPa occupies 2 m³. What pressure when compressed to 0.5 m³ at constant temperature?'",
     "head: 'A gas at 100\xa0kPa occupies 2\xa0m³. What pressure when compressed to 0.5\xa0m³ at constant temperature?'"),
    ("line: 'p₂ = 400 kPa'",
     "line: 'p₂ = 400\xa0kPa'"),
    ("head: 'A sealed syringe holds 60 cm³ of air at 1.0 × 10⁵ Pa. The plunger is pushed in slowly, at constant temperature, until the pressure is 240 kPa. Calculate the new volume in m³.'",
     "head: 'A sealed syringe holds 60\xa0cm³ of air at 1.0 × 10⁵ Pa. The plunger is pushed in slowly, at constant temperature, until the pressure is 240\xa0kPa. Calculate the new volume in m³.'"),
    ("line: '1.0 × 10⁵ Pa = 100 kPa'",
     "line: '1.0 × 10⁵ Pa = 100\xa0kPa'"),
    ("line: 'V₂ = 6000 ÷ 240 = 25 cm³'",
     "line: 'V₂ = 6000 ÷ 240 = 25\xa0cm³'"),
    ("line: 'V₂ = 25 cm³ = 2.5 × 10⁻⁵ m³'",
     "line: 'V₂ = 25\xa0cm³ = 2.5 × 10⁻⁵ m³'"),
    ("note: '1 cm³ = 1 × 10⁻⁶ m³.'",
     "note: '1\xa0cm³ = 1 × 10⁻⁶ m³.'"),
    ("head: 'An air bubble has a volume of 4.0 cm³ at a pressure of 250 kPa. It rises to where the pressure is 100 000 Pa. Its temperature stays the same. Calculate its new volume.'",
     "head: 'An air bubble has a volume of 4.0\xa0cm³ at a pressure of 250\xa0kPa. It rises to where the pressure is 100\xa0000\xa0Pa. Its temperature stays the same. Calculate its new volume.'"),
    ("line: '100 000 Pa ÷ 1000 = 100 kPa'",
     "line: '100\xa0000\xa0Pa ÷ 1000 = 100\xa0kPa'"),
    ("line: 'V₂ = 10 cm³'",
     "line: 'V₂ = 10\xa0cm³'"),
    ("note: 'Left unconverted, 1000 ÷ 100 000 gives 0.01 cm³: the bubble would shrink as the pressure falls.'",
     "note: 'Left unconverted, 1000 ÷ 100\xa0000 gives 0.01\xa0cm³: the bubble would shrink as the pressure falls.'"),
    ("head: 'A gas cylinder holds 0.030 m³ of gas at 2400 kPa. The gas is let out slowly into a balloon at 100 kPa, at constant temperature. Calculate the volume the gas would occupy at 100 kPa.'",
     "head: 'A gas cylinder holds 0.030\xa0m³ of gas at 2400\xa0kPa. The gas is let out slowly into a balloon at 100\xa0kPa, at constant temperature. Calculate the volume the gas would occupy at 100\xa0kPa.'"),
    ("line: 'V₂ = 0.72 m³'",
     "line: 'V₂ = 0.72\xa0m³'"),
    ("head: 'A syringe holds 45 cm³ of air at 100 kPa. The plunger is pushed in slowly, at constant temperature, until the pressure is 1.5 × 10⁵ Pa. Calculate the new volume.'",
     "head: 'A syringe holds 45\xa0cm³ of air at 100\xa0kPa. The plunger is pushed in slowly, at constant temperature, until the pressure is 1.5 × 10⁵ Pa. Calculate the new volume.'"),
    ("close: 'Mixing 100 (kPa) with 150 000 (Pa) gives 0.03 cm³: a thousand times too small.'",
     "close: 'Mixing 100 (kPa) with 150\xa0000 (Pa) gives 0.03\xa0cm³: a thousand times too small.'"),
    ("line: '1.5 × 10⁵ Pa = 150 kPa'",
     "line: '1.5 × 10⁵ Pa = 150\xa0kPa'"),
    ("line: 'V₂ = 30 cm³'",
     "line: 'V₂ = 30\xa0cm³'"),
    ("head: 'A fixed mass of gas at constant temperature has a volume of 0.40 m³ at 120 kPa. Its volume is increased to 0.60 m³. Calculate the new pressure.'",
     "head: 'A fixed mass of gas at constant temperature has a volume of 0.40\xa0m³ at 120\xa0kPa. Its volume is increased to 0.60\xa0m³. Calculate the new pressure.'"),
    ("close: 'Bigger volume, lower pressure: 80 kPa is less than 120 kPa.'",
     "close: 'Bigger volume, lower pressure: 80\xa0kPa is less than 120\xa0kPa.'"),
    ("line: 'p₂ = 80 kPa'",
     "line: 'p₂ = 80\xa0kPa'"),
    ("head: 'A weather balloon holds 3.0 m³ of gas at 100 kPa. It rises until the pressure outside, and so the pressure of its gas, is 75 000 Pa. Assume the temperature stays the same. Calculate its new volume.'",
     "head: 'A weather balloon holds 3.0\xa0m³ of gas at 100\xa0kPa. It rises until the pressure outside, and so the pressure of its gas, is 75\xa0000\xa0Pa. Assume the temperature stays the same. Calculate its new volume.'"),
    ("close: 'Left unconverted, 300 ÷ 75 000 gives 0.004 m³: the balloon would shrink as the pressure falls.'",
     "close: 'Left unconverted, 300 ÷ 75\xa0000 gives 0.004\xa0m³: the balloon would shrink as the pressure falls.'"),
    ("line: '75 000 Pa ÷ 1000 = 75 kPa'",
     "line: '75\xa0000\xa0Pa ÷ 1000 = 75\xa0kPa'"),
    ("line: 'V₂ = 4.0 m³'",
     "line: 'V₂ = 4.0\xa0m³'"),
]

# ⊕ 24 Nov 2026 (re-walk at 390 px): rung STEMS only get no-break spaces inside numbers and
# number-unit pairs ("(c = 385 J/kg °C)", "a drink at 20 °C" split across lines). Rung ids are by
# position, so the ids hold; no option text or answer key is touched.
LOGIC_EDITS += [
    ("prompt: 'A balloon holds 0.0090 m³ of air at 100 kPa. It is squeezed slowly, at constant temperature, until its volume is 2500 cm³. Calculate the new pressure in kPa. Work it on paper, then choose the conversion and give the answer and unit.'",
     "prompt: 'A balloon holds 0.0090\xa0m³ of air at 100\xa0kPa. It is squeezed slowly, at constant temperature, until its volume is 2500\xa0cm³. Calculate the new pressure in kPa. Work it on paper, then choose the conversion and give the answer and unit.'"),
    ("prompt: 'A fixed mass of gas at constant temperature has a volume of 0.060 m³ at a pressure of 100 kPa. It is compressed to 0.024 m³. Calculate the new pressure. Work it on paper, then choose the conversion and give the answer and unit.'",
     "prompt: 'A fixed mass of gas at constant temperature has a volume of 0.060\xa0m³ at a pressure of 100\xa0kPa. It is compressed to 0.024\xa0m³. Calculate the new pressure. Work it on paper, then choose the conversion and give the answer and unit.'"),
]

# ⊕ 24 Nov 2026 (blind key pass). Q087: TF/TH Rung 3's second link did not depend on the first, so
# either could come first; it now picks up "that same speed" from link 1, so only one order works.
# Q081: CH Rung 2's keyed option becomes 125 kPa (95 kPa at 283 K gives 125.2 kPa at 373 K); its
# feedback and model line follow. No distractor is 125 kPa.
LOGIC_EDITS += [
    ("'In the bigger volume, the molecules travel further between hits on the walls.'",
     "'At that same speed, in the bigger volume, the molecules travel further between hits on the "
     "walls.'"),
    ("options: ['109 kPa', '113 kPa', '126 kPa', '218 kPa']",
     "options: ['109 kPa', '113 kPa', '125 kPa', '218 kPa']"),
    ("so it reaches about 125 kPa at 100 °C: 126 kPa is the closest option.'",
     "so it reaches about 125 kPa at 100 °C.'"),
    ("108 + 50 ÷ 3 ≈ 125 kPa, so 126 kPa.'", "108 + 50 ÷ 3 ≈ 125 kPa.'"),
]

LESSON = {
    "slug": "particle-motion-pressure",
    "start": {
        "setup": "Every aerosol can says “Do not burn, even after use”. An empty can is still "
                 "sealed, and still full of gas.",
        "question": "If you had to guess, why does a heated can burst?",
        "options": [
            ("The gas inside catches fire",
             "The hot gas pushes harder. Its molecules move faster and hit the walls more often "
             "and harder, until the metal splits. A can of air, which cannot burn, bursts too."),
            ("The hot gas pushes harder on the walls",
             "The hot gas pushes harder. Its molecules move faster and hit the walls more often "
             "and harder, until the metal splits. A can of air, which cannot burn, bursts too."),
        ],
        "answer": 1,
    },
    "words": ["random motion", "pressure", "kinetic energy"],
    "knowledge": [
        {"kind": "card", "title": "How gas molecules move",
         "body": ["The molecules of a gas are in constant random motion.",
                  {"points": [
                      "They move in all directions, at a range of speeds.",
                      "Each one travels in a straight line until it hits another molecule or a "
                      "wall of the container.",
                  ]}]},
        {"kind": "card", "title": "Where gas pressure comes from",
         "body": [{"slot": "fig:gas-pressure"},
                  "Each molecule that hits a wall of the container exerts a force on it.",
                  "Huge numbers of collisions every second add up to a steady force on the walls. "
                  "This is the pressure of the gas.",
                  "Only collisions with the walls push on the walls."]},
        {"kind": "card", "title": "Temperature and the molecules",
         "body": ["The temperature of the gas is related to the average kinetic energy of the "
                  "molecules.",
                  "In a hotter gas the molecules have more kinetic energy on average, so they "
                  "move faster."]},
        {"kind": "card", "title": "Heating a gas at constant volume",
         "body": ["Changing the temperature of a gas, held at constant volume, changes the "
                  "pressure exerted by the gas.",
                  {"points": [
                      "The temperature rises, so the average kinetic energy of the molecules "
                      "increases.",
                      "The molecules move faster, so they hit the walls more often and with more "
                      "force.",
                      "So the pressure increases.",
                  ]},
                  "Cooling the gas does the opposite: the pressure decreases."]},
        {"kind": "card", "title": "Pressure in gases", "routes": ["TF", "TH"],
         "body": ["A gas can be compressed or expanded by pressure changes. The pressure produces "
                  "a net force at right angles to the wall of the gas container (or any surface).",
                  "Increase the volume of a gas at constant temperature:",
                  {"points": [
                      "The temperature is the same, so the molecules keep the same average speed.",
                      "In the bigger volume they travel further between hits on the walls.",
                      "So each part of the wall is hit less often, and the pressure decreases.",
                  ]}]},
        {"kind": "card", "title": "Pressure and volume", "routes": ["TF", "TH"],
         "body": ["For a fixed mass of gas held at a constant temperature:",
                  "pressure × volume = constant",
                  "p\u00a0V\u00a0=\u00a0constant",
                  {"points": ["pressure, p, in pascals (Pa)",
                              "volume, V, in metres cubed (m³)"]},
                  "This equation is on the Physics equation sheet.",
                  "To compare before and after, write it as p₁\u00a0V₁\u00a0=\u00a0p₂\u00a0V₂. Halve the volume and "
                  "the pressure doubles.",
                  "The two pressures must be in the same unit, and so must the two volumes: "
                  "1\u00a0kPa = 1000\u00a0Pa, and 1\u00a0m³ = 1\u00a0000\u00a0000\u00a0cm³."]},
        {"kind": "card", "title": "Worked examples", "routes": ["TF", "TH"],
         "body": [{"slot": "cfifa"}]},
        {"kind": "card", "title": "Doing work on a gas", "routes": ["TH"],
         "body": ["Work is the transfer of energy by a force.",
                  "Doing work on a gas increases the internal energy of the gas and can cause an "
                  "increase in the temperature of the gas.",
                  {"points": [
                      "Block the outlet of a bicycle pump and push the piston in quickly.",
                      "The force on the piston does work on the air: energy is transferred to it.",
                      "The internal energy of the air increases, so its temperature rises.",
                      "Its molecules move faster, so the pressure rises by more than the smaller "
                      "volume alone would cause.",
                  ]}]},
        {"kind": "card", "title": "Easy mistakes",
         "body": [{"mistakes": [
             ("Heating a gas makes its molecules bigger.",
              "The molecules stay the same size. They move faster."),
             ("The molecules hit each other more, so the pressure rises.",
              "Only hits on the walls push on the walls. The pressure rises because the molecules "
              "hit the walls more often and harder."),
             ("Gas molecules vibrate about fixed positions.",
              "That describes a solid. Gas molecules move freely in all directions."),
         ]}]},
    ],
    "key_fact": "Gas pressure is caused by the molecules colliding with the walls of their "
                "container. Heating a gas at constant volume increases the average kinetic energy "
                "of its molecules, so they hit the walls more often and with more force, and the "
                "pressure increases.",
    "deeper": [
        {"kind": "card", "title": "Links to other lessons",
         "body": [{"points": [
             "Internal energy: the energy stored by the particles of a system.",
             "Changes of state: what happens when a gas cools enough to condense.",
         ]}]},
        {"kind": "card", "title": "Command words",
         "body": [{"points": [
             "<strong>Describe</strong>: say what the molecules do: random directions, constant "
             "motion, a range of speeds.",
             "<strong>Explain</strong>: link every step: temperature, kinetic energy, speed, hits "
             "on the walls, pressure.",
             "<strong>Predict</strong>: say what will happen, using a pattern in the data or the "
             "particle model.",
         ]}]},
    ],
    "try": None,
    "legacy": {"batch": "batch-3", "pre_edits": PRE_EDITS, "logic_edits": LOGIC_EDITS},
}
