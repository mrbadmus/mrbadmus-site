# Development of the Periodic Table  (Chemistry, AQA 5.1.2.2)

**Appears on routes:** Combined Foundation, Combined Higher, Triple Foundation, Triple Higher
**Route copies that differ from Triple Higher:** none (the route tags are to be set from the AQA spec's own HT / separate-science labels, not from these copies)

## Examiner's route tags (AQA spec, 2 Oct 2026)

| point | layer | spec ref |
|---|---|---|
| Ordering by atomic weight before subatomic particles; early tables incomplete, elements misplaced | base | 8464 5.1.2.2 / 8462 4.1.2.2 |
| Newlands' octaves and why rejected | base (context) | 5.1.2.2 |
| Mendeleev: gaps, changed order; predicted elements found (Ga, Sc, Ge) | base | 5.1.2.2 |
| Testing a prediction supports a scientific idea | base | WS 1.1, 1.6 |
| Moseley / atomic number; noble gases added later | base (context) | 5.1.2.1 |
| Isotopes explain why atomic-weight order was not always correct | base — **not in this file** (see below) | 5.1.2.2; 5.1.1.5–5.1.1.6 |
| quiz q1 | base — wx3 WRONG; do not use as written | 5.1.2.2 |
| quiz q2 | base | 5.1.2.2 |

True page routes: CF CH TF TH, all base. Site currently ships the same four routes.

## Spec core missing from the frozen data (written from the spec, examiner)

8464 5.1.2.2 / 8462 4.1.2.2: "Knowledge of isotopes made it possible to explain why the order based on atomic weights was not always correct."

Supporting, 8464 5.1.1.5 / 8462 4.1.1.5: "Atoms of the same element can have different numbers of neutrons; these atoms are called isotopes of that element." 8464 5.1.1.6 / 8462 4.1.1.6: "The relative atomic mass of an element is an average value that takes account of the abundance of the isotopes of the element."

This is SOURCE MATERIAL: checked science to draw from. Quiz questions (with their wrong-answer explanations), the examiner tip, worked examples (FIFA), equations and required-practical data are kept VERBATIM. The theory text may be re-cut. The matching activity is to be REPLACED (it prints its own answers). It is not a page structure to copy.

## summary

Describe how the periodic table developed, including Newlands and Mendeleev's contributions.

## theory
```json
[
  {
    "content": "Before atomic numbers were understood, scientists tried to classify elements based on RELATIVE ATOMIC MASS.\n\nJOHN NEWLANDS — Law of Octaves (1864):\nArranged elements by increasing Ar.\nNoticed that every 8th element had similar properties — called it the 'Law of Octaves' (like musical notes).\nLimitations:\nOnly worked for the first 16 elements.\nForced elements into groups even when properties didn't match.\nLeft no gaps for undiscovered elements.\nThe scientific community did not accept his work.\n\nDMITRI MENDELEEV — first successful periodic table (1869):\nAlso arranged elements by increasing Ar.\nKey improvements over Newlands:\nLeft GAPS for undiscovered elements — predicted their properties.\nRearranged some elements to make groups match better (putting chemical properties above strict Ar order).\nPredicted EKA-SILICON (now known as germanium) — when it was discovered in 1886, its properties closely matched Mendeleev's prediction.\nThis predictive power convinced the scientific community to accept the table.",
    "heading": "Early Attempts at Classification"
  },
  {
    "content": "The modern periodic table was only possible after the discovery of subatomic particles.\n\nHENRY MOSELEY (1913):\nUsed X-ray experiments to determine ATOMIC NUMBERS of elements.\nRealised elements should be arranged by ATOMIC NUMBER (protons), not atomic mass.\nThis resolved several inconsistencies in Mendeleev's table where some elements seemed in the wrong order when arranged by Ar.\n\nKey improvement: arranging by atomic number places elements in the correct groups without exception — it is the atomic number (protons = electrons) that determines chemical properties, not mass.\n\nDISCOVERY OF NOBLE GASES:\nArgon (1894) and other noble gases were discovered AFTER Mendeleev's table — but they fit perfectly as a new Group 0.\nThis was further evidence for the validity of the periodic table structure.",
    "heading": "The Modern Periodic Table"
  },
  {
    "content": "Mendeleev's table was eventually accepted by the scientific community for three main reasons:\n\n1. PREDICTIVE POWER: He predicted properties of undiscovered elements (eka-aluminium = gallium, eka-silicon = germanium, eka-boron = scandium). When discovered, they matched his predictions closely.\n\n2. GAPS: Leaving gaps was a bold scientific decision — it showed the table was a genuine model of underlying patterns, not just a classification of known elements.\n\n3. EXPLAINING PATTERNS: The table explained why elements in the same group reacted similarly — it made chemistry more systematic and predictable.\n\nScience accepts models when they successfully PREDICT new observations — Mendeleev's table did exactly this.",
    "heading": "Why Mendeleev's Table was Accepted"
  }
]
```

## common_mistake

Mendeleev arranged elements by RELATIVE ATOMIC MASS — the MODERN table is arranged by ATOMIC NUMBER. Mendeleev's arrangement had a few inconsistencies because Ar and atomic number don't always match perfectly (e.g. argon and potassium). The modern arrangement by atomic number resolves all these problems.

## key_note

Newlands: octaves — every 8th element similar — rejected (didn't work for all elements, no gaps). Mendeleev: arranged by Ar, left gaps, predicted missing elements — accepted when predictions proved correct. Modern table: arranged by atomic number (Moseley, 1913).

## matching
```json
{
  "instruction": "Match each scientist to their contribution to the periodic table.",
  "pairs": [
    [
      "Newlands",
      "Law of Octaves — every 8th element similar — not accepted by scientists at the time"
    ],
    [
      "Mendeleev",
      "Left gaps for undiscovered elements, predicted their properties — table accepted when predictions proved correct"
    ],
    [
      "Moseley",
      "Arranged elements by atomic number (protons) — resolved inconsistencies in Mendeleev's Ar-based table"
    ]
  ],
  "title": "Match the Scientist to their Contribution"
}
```

## quiz
```json
[
  {
    "opts": [
      [
        "It only worked for the first 16 elements and forced elements into groups regardless of whether properties matched",
        true
      ],
      [
        "Newlands arranged elements by atomic number rather than relative atomic mass",
        false
      ],
      [
        "The law of octaves was never published so other scientists couldn't evaluate it",
        false
      ],
      [
        "Newlands did not leave gaps for undiscovered elements — but neither did he need to",
        false
      ]
    ],
    "q": "Why did the scientific community initially reject Newlands' Law of Octaves?",
    "wrong_explanations": {
      "1": "Newlands arranged by RELATIVE ATOMIC MASS — atomic numbers were not yet known.",
      "2": "Newlands did publish his work — it was presented to the Chemical Society in 1866.",
      "3": "Not leaving gaps was a problem for Mendeleev too initially — but the bigger issue for Newlands was that his pattern broke down after the first 16 elements."
    }
  },
  {
    "opts": [
      [
        "He predicted properties of undiscovered elements — and when they were found, the predictions were accurate",
        true
      ],
      [
        "He was the first to arrange elements in order of atomic mass",
        false
      ],
      [
        "He discovered all the noble gases and added them to the table",
        false
      ],
      [
        "His table was the simplest and easiest to remember",
        false
      ]
    ],
    "q": "What was the key reason Mendeleev's periodic table was eventually accepted by scientists?",
    "wrong_explanations": {
      "1": "Newlands had also arranged by atomic mass — Mendeleev's key advance was leaving gaps and making testable predictions.",
      "2": "Noble gases were discovered by other scientists (Ramsay and others) after Mendeleev's original table — they were later added as Group 0.",
      "3": "Science accepts models based on EVIDENCE and PREDICTIVE POWER, not simplicity alone."
    }
  }
]
```
