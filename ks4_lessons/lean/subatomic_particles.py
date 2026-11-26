# -*- coding: utf-8 -*-
"""Subatomic particles, in the lean shape. Spec table: ks4-subatomic-particles.md (AQA 8464
5.1.1.4 and 5.1.1.5 / 8462 4.1.1.4 and 4.1.1.5, word for word the same; no HT-only or
Chemistry-only lines). The Design page's eyebrow already covers both points, so size and mass of
atoms, mass number, isotopes and counting particles in atoms and ions are all taught here.

LEGACY (batch 11). The ladder (Ks4Practice rungs) and the practice set (the page's own BANK, the
same five items on every route) stay from the Design page; the practice set does not read the
subtopic `quiz` list, so its fixes are logic_edits. Every stem is kept, so every practice id is kept.

logic_edits (practice set only; the rungs were checked and are unchanged):
  1. Q1 (Mg²⁺ electrons): the credited option was the longest and carried its working with a dash.
     Options are now bare numbers; replies plain. Key unchanged (10).
  2. Q2 (why an atom is neutral): the credited option was the longest (93 characters against
     55 to 64); replies in capitals. Options rewritten to similar lengths; same idea credited.
  3. Q5 (size of an atom): the credited option was the longest (73 against 31 to 40). Rewritten.

The Higher half-equation section of the Design page belongs to the HT-only line of 5.1.1.1
(atoms-elements-compounds); it is kept here as a Higher-only Dive deeper card, and the header chip
"Higher layer · half equations" is removed by a template_edit.
"""

LOGIC_EDITS = [
    ('V("A magnesium atom (Mg, atomic number 12) forms a Mg²⁺ ion. How many electrons does the ion have?", [["10 — magnesium loses 2 electrons from its original 12", true], ["14 — magnesium gains 2 electrons to form a +2 ion", false], ["12 — the number of electrons stays the same", false], ["2 — only the outermost electrons remain", false]], { "1": "Gaining electrons gives a NEGATIVE charge. Mg²⁺ is POSITIVE, so electrons were LOST.", "2": "Mg²⁺ is formed by losing 2 electrons. Original: 12 electrons. After loss: 12 − 2 = 10 electrons.", "3": "Only the 2 outermost electrons are lost — but the ion still has all 10 remaining electrons, not just 2." }),',
     'Q("A magnesium atom (Mg, atomic number 12) forms a Mg²⁺ ion. How many electrons does the ion have?", \'10\', [[\'14\', \'A positive ion has lost electrons, not gained them: 12 − 2 = 10.\'], [\'12\', \'That is the atom. The 2+ charge means two electrons were lost.\'], [\'2\', \'Only the two outer electrons are lost. The ion keeps the other 10.\']]),'),
    ('V("Why does an atom have no overall electrical charge?", [["The number of protons (+1 each) equals the number of electrons (−1 each) — the charges cancel", true], ["Protons and neutrons have equal and opposite charges that cancel", false], ["Electrons are on the outside and shield the positive nucleus", false], ["The atom vibrates too fast for any charge to accumulate", false]], { "1": "Neutrons have ZERO charge — they cannot cancel proton charges. Charge neutrality comes from protons balancing electrons.", "2": "Shielding describes how inner electrons reduce the attractive force on outer electrons — it does not explain why atoms are electrically neutral.", "3": "Vibration does not affect electrical charge — the neutrality is a consequence of proton and electron numbers being equal." }),',
     'Q("Why does an atom have no overall electrical charge?", \'It has equal numbers of protons and electrons\', [[\'Its protons and neutrons have opposite charges\', \'Neutrons have no charge, so they cannot cancel anything.\'], [\'Its electrons shield the positive nucleus\', \'Shielding does not change the total charge. Each +1 proton is balanced by a −1 electron.\'], [\'Its neutrons cancel the charge of the electrons\', \'Neutrons have no charge. The electrons balance the protons.\']]),'),
    ("Q('Which statement about the size of an atom is correct?', 'The radius of the nucleus is less than 1/10 000 of the radius of the atom', [['The nucleus takes up about half the atom', 'The atom is mostly empty space.'], ['The nucleus has a radius of about 0.1 nm', '0.1 nm is the atom’s radius; the nucleus is about 1 × 10⁻¹⁴ m.'], ['Electrons hold most of the mass', 'Almost all the mass is in the nucleus.']])",
     "Q('Which statement about the size of an atom is correct?', 'The nucleus radius is under 1/10 000 of the atom’s', [['The nucleus takes up about half the volume of the atom', 'The atom is mostly empty space. The nucleus is tiny.'], ['The nucleus radius is about 0.1 nm (1 × 10⁻¹⁰ m)', '0.1 nm is the radius of the whole atom. The nucleus is about 1 × 10⁻¹⁴ m.'], ['Most of the mass of an atom is in its electrons', 'Almost all the mass is in the nucleus.']])"),
    # Examiner fix round (26 Nov), S3: the Rung 4 model line.
    ("'Electrons = 8 \u2212 (\u22122) = 10.'", "'Electrons = 8 + 2 = 10.'"),
]

# The header chip "Higher layer · half equations" announced the Design page's Higher section. On the
# lean page half equations are a Higher-only Dive deeper card, so the chip goes.
TEMPLATE_EDITS = [
    ('\n          <sc-if value="{{ isHigher }}"><span style="font-family: var(--ks3-font-mono); '
     'font-size: 13px; font-weight: 500; letter-spacing: .06em; text-transform: uppercase; '
     'padding: 4px 11px; border-radius: 99px; background: var(--ks3-ink); color: var(--ks3-ground);">'
     'Higher layer \u00b7 half equations</span></sc-if>', ""),
]

LESSON = {
    "slug": "subatomic-particles",
    "start": {
        "setup": None,
        "question": "If you had to guess, where is almost all the mass of an atom?",
        "options": [
            ("In the nucleus",
             "In the nucleus. Protons and neutrons each have a relative mass of 1. Electrons have a "
             "very small mass."),
            ("Spread evenly through the atom",
             "Almost all the mass is in the nucleus. Most of the atom is empty space, with the "
             "electrons in it."),
        ],
        "answer": 0,
    },
    "words": ["atomic number", "mass number", "isotope", "ion"],
    "knowledge": [
        {"kind": "card", "title": "Protons, neutrons and electrons",
         "body": [{"slot": "fig:atom-particles"},
                  "Protons and neutrons are in the nucleus at the centre of the atom. Electrons move "
                  "around the nucleus in shells."]},
        {"kind": "reveal", "title": "The three particles",
         "cols": ["Relative charge", "Relative mass"],
         "rows": [
             ("Proton", "+1", "1"),
             ("Neutron", "0", "1"),
             ("Electron", "−1", "Very small"),
         ]},
        {"kind": "card", "title": "Why an atom has no charge",
         "body": ["In an atom, the number of electrons is equal to the number of protons in the "
                  "nucleus. Each +1 is balanced by a −1, so atoms have no overall electrical "
                  "charge.",
                  "The number of protons in an atom of an element is its atomic number. All atoms "
                  "of a particular element have the same number of protons. Atoms of different "
                  "elements have different numbers of protons."]},
        {"kind": "card", "title": "Mass number",
         "body": [{"slot": "fig:nuclear-symbol"},
                  "The sum of the protons and neutrons in an atom is its mass number.",
                  {"points": [
                      "protons = atomic number",
                      "neutrons = mass number − atomic number",
                      "electrons in an atom = protons",
                  ]}]},
        {"kind": "card", "title": "Isotopes",
         "body": [{"slot": "fig:isotopes-hydrogen"},
                  "Atoms of the same element can have different numbers of neutrons. These atoms "
                  "are called isotopes of that element.",
                  "Isotopes have the same atomic number but different mass numbers."]},
        {"kind": "card", "title": "Counting particles in an ion",
         "body": ["An ion forms when an atom loses or gains electrons. The number of protons does "
                  "not change.",
                  {"points": [
                      "A positive ion has lost electrons. <sup>27</sup><sub>13</sub>Al<sup>3+</sup> "
                      "has 13 protons, 27 − 13 = 14 neutrons and 13 − 3 = 10 electrons.",
                      "A negative ion has gained electrons. <sup>35</sup><sub>17</sub>Cl<sup>−</sup> "
                      "has 17 protons, 35 − 17 = 18 neutrons and 17 + 1 = 18 electrons.",
                  ]}]},
        {"kind": "card", "title": "Size and mass of atoms",
         "body": [{"slot": "fig:atom-scale"},
                  "Atoms are very small, with a radius of about 0.1 nm (1 × 10⁻¹⁰ m).",
                  "The radius of a nucleus is less than 1/10 000 of that of the atom (about "
                  "1 × 10⁻¹⁴ m). Almost all of the mass of an atom is in the "
                  "nucleus.",
                  "If an atom were 100 m across, like a football pitch, its nucleus would be less "
                  "than 1 cm across, smaller than a pea."]},
        {"kind": "card", "title": "Easy mistakes",
         "body": [{"mistakes": [
             ("Mg²⁺ has 12 electrons, because magnesium is element 12.",
              "It has lost two electrons, so it has 12 − 2 = 10."),
             ("The mass number is the number of neutrons.",
              "The mass number is protons + neutrons."),
             ("Neutrons cancel the charge of the protons.",
              "Neutrons have no charge. Equal numbers of electrons balance the protons."),
             ("An atom becomes an ion by gaining or losing protons.",
              "Only electrons are lost or gained. The protons never change."),
         ]}]},
    ],
    "key_fact": "Protons (+1) and neutrons (0) are in the nucleus and each has a relative mass of 1. "
                "Electrons (−1) have a very small mass. The atomic number is the number of "
                "protons, and the mass number is protons + neutrons. In an atom the numbers of "
                "protons and electrons are equal, so the atom has no overall charge.",
    "deeper": [
        {"kind": "card", "title": "How small is very small",
         "body": ["An electron's mass is about 1/2000 of a proton's. That is why the mass of an atom "
                  "is almost all in its nucleus."]},
        {"kind": "card", "title": "Higher: half equations",
         "routes": ["CH", "TH"],
         "body": ["A half equation shows the electrons lost or gained. The charges must balance on "
                  "both sides.",
                  {"points": [
                      "Na → Na⁺ + e⁻",
                      "Mg → Mg²⁺ + 2e⁻",
                      "Cl₂ + 2e⁻ → 2Cl⁻",
                  ]}]},
        {"kind": "card", "title": "Command words",
         "body": [{"points": [
             "<strong>Calculate</strong>: protons, neutrons and electrons from the atomic number, "
             "mass number and charge.",
             "<strong>Explain</strong>: why an atom is neutral, or why an ion has its charge.",
             "<strong>State</strong>: the relative charge and mass of each particle.",
         ]}]},
    ],
    "try": None,
    "legacy": {"batch": "batch-11", "logic_edits": LOGIC_EDITS, "template_edits": TEMPLATE_EDITS},
}
