# Electronic Structure  (Chemistry, AQA 5.1.1.7)

**Appears on routes:** Combined Foundation, Combined Higher, Triple Foundation, Triple Higher
**Route copies that differ from Triple Higher:** Combined Foundation, Triple Foundation (the route tags are to be set from the AQA spec's own HT / separate-science labels, not from these copies)

## Examiner's route tags (AQA spec, 2 Oct 2026)
| point | layer | spec ref |
|---|---|---|
| Lowest levels fill first; 2, 8, 8; configurations H–Ca (theory 1–2; key_note; common_mistake) | base | 8464 5.1.1.7; 8462 4.1.1.7 |
| Diagram form of electronic structure | base. Missing from the frozen data (F3) | 8464 5.1.1.7; 8462 4.1.1.7 |
| Same group = same outer electrons = similar chemistry (theory 3; q1; q2) | base | 8464 5.1.2.1; 8462 4.1.2.1 |
| Noble gases full outer shell (helium 2) (theory 3) | base. Helium wording imprecise (F2) | 8464 5.1.2.4; 8462 4.1.2.4 |
| `higher`: configs 1–20; period = shells, group = outer electrons | **base, not HT** (F1) | 8464 5.1.1.7, 5.1.2.1 |
| quiz q1, q2 | base, usable as written | 8464 5.1.2.1 |

True page routes: CF CH TF TH, with no HT layer. Site currently ships: CF CH TF TH, which matches. The `higher` copy currently reaches CH/TH only; its content is base and is flagged (F1).

This is SOURCE MATERIAL: checked science to draw from. Quiz questions (with their wrong-answer explanations), the examiner tip, worked examples (FIFA), equations and required-practical data are kept VERBATIM. The theory text may be re-cut. The matching activity is to be REPLACED (it prints its own answers). It is not a page structure to copy.

## summary

Describe how electrons fill shells and write electronic configurations for the first 20 elements.

## theory
```json
[
  {
    "content": "Electrons occupy SHELLS (energy levels) around the nucleus. They always fill from the INNERMOST (lowest energy) shell outward.\n\nSHELL CAPACITIES (for first 20 elements):\n1st shell: maximum 2 electrons.\n2nd shell: maximum 8 electrons.\n3rd shell: maximum 8 electrons.\n\nElectrons are only added to the next shell when the current one is FULL.\n\nExample — Sodium (Na, atomic number 11):\n11 electrons to distribute.\n1st shell: 2 (full) → 2nd shell: 8 (full) → 3rd shell: 1 remaining.\nElectronic configuration written as: 2.8.1",
    "heading": "Electron Shells"
  },
  {
    "content": "H  (1):  1\nHe (2):  2\nLi (3):  2.1\nBe (4):  2.2\nB  (5):  2.3\nC  (6):  2.4\nN  (7):  2.5\nO  (8):  2.6\nF  (9):  2.7\nNe (10): 2.8\nNa (11): 2.8.1\nMg (12): 2.8.2\nAl (13): 2.8.3\nSi (14): 2.8.4\nP  (15): 2.8.5\nS  (16): 2.8.6\nCl (17): 2.8.7\nAr (18): 2.8.8\nK  (19): 2.8.8.1\nCa (20): 2.8.8.2\n\nNote: the 4th shell starts filling at potassium (K) and calcium (Ca) because the 3rd shell fills to 8 before the 4th begins (for these lighter elements).",
    "heading": "Electronic Configurations of the First 20 Elements"
  },
  {
    "content": "The NUMBER OF ELECTRONS IN THE OUTERMOST SHELL (valence electrons) determines an element's chemical properties.\n\nElements in the SAME GROUP of the periodic table have the SAME NUMBER of outer electrons:\nGroup 1: 1 outer electron (Li: 2.1, Na: 2.8.1, K: 2.8.8.1)\nGroup 7: 7 outer electrons (F: 2.7, Cl: 2.8.7)\nGroup 0: 8 outer electrons (full shell) — He: 2, Ne: 2.8, Ar: 2.8.8\n\nThis is why elements in the same group have similar chemical properties — they react in similar ways to achieve a full outer shell.\n\nATOMS REACT TO ACHIEVE A FULL OUTER SHELL:\nMETALS lose electrons → form positive ions (cations).\nNON-METALS gain electrons (or share) → form negative ions (anions) or covalent bonds.\nNOBLE GASES already have full outer shells → very unreactive.",
    "heading": "Electronic Structure and Chemical Properties"
  }
]
```

## higher

Electronic configurations for all elements 1–20. Predict chemical properties from electronic structure — elements in the same group have the same outer electron count. Explain why period number = number of shells, and group number = outer electrons.

## common_mistake

Always fill shells in ORDER — 2 in the first, then 8 in the second, then continue. The 3rd shell fills to 8 before the 4th shell starts. Students sometimes try to put more than 8 in the 3rd shell for early elements — for the first 20, the 3rd shell only goes up to 8.

## key_note

Shells fill innermost first: 2, 8, 8. Electronic configuration written as numbers separated by dots (e.g. 2.8.3 for Al). Same group = same outer electrons = similar chemistry. Full outer shell = stable (noble gas configuration).

## matching
```json
{
  "instruction": "Match each element to its correct electronic configuration.",
  "pairs": [
    [
      "Sodium (Na, 11)",
      "2.8.1 — 11 electrons: 2 in shell 1, 8 in shell 2, 1 in shell 3"
    ],
    [
      "Chlorine (Cl, 17)",
      "2.8.7 — 17 electrons: 2 in shell 1, 8 in shell 2, 7 in shell 3"
    ],
    [
      "Calcium (Ca, 20)",
      "2.8.8.2 — 20 electrons across four shells"
    ],
    [
      "Neon (Ne, 10)",
      "2.8 — full outer shell, noble gas, very unreactive"
    ],
    [
      "Magnesium (Mg, 12)",
      "2.8.2 — 2 outer electrons, Group 2 element"
    ]
  ],
  "title": "Match the Element to its Electronic Configuration"
}
```

## quiz
```json
[
  {
    "opts": [
      [
        "Group 6 — it has 6 electrons in its outermost shell",
        true
      ],
      [
        "Group 2 — there are 2 complete shells below the outer shell",
        false
      ],
      [
        "Group 16 — add all the electrons together",
        false
      ],
      [
        "Period 3 — it has 3 shells",
        false
      ]
    ],
    "q": "An element has the electronic configuration 2.8.6. Which group of the periodic table is it in?",
    "wrong_explanations": {
      "1": "The number of complete inner shells tells you the PERIOD — 2 inner shells means Period 3. Groups are determined by OUTER electrons.",
      "2": "16 is the total number of electrons (2+8+6) — this tells you the atomic number, not the group.",
      "3": "The NUMBER OF SHELLS tells you the PERIOD (3 shells = Period 3). The GROUP is determined by the number of OUTER electrons (6)."
    }
  },
  {
    "opts": [
      [
        "Both have 1 electron in their outer shell — they react in similar ways to achieve a full outer shell",
        true
      ],
      [
        "Both have the same total number of electrons",
        false
      ],
      [
        "Both are in the same period of the periodic table",
        false
      ],
      [
        "Both have the same mass number",
        false
      ]
    ],
    "q": "Why do lithium (2.1) and sodium (2.8.1) have similar chemical properties?",
    "wrong_explanations": {
      "1": "Li has 3 electrons total, Na has 11 — very different totals, but the same outer shell count (1) is what matters for reactivity.",
      "2": "Li is Period 2, Na is Period 3 — they are in different periods. Same GROUP, different periods.",
      "3": "Li has mass number 7, Na has mass number 23 — different mass numbers. Chemical similarity comes from electron configuration."
    }
  }
]
```

## higher — Combined Foundation copy (differs from the Triple Higher copy above)
```json
null
```

## higher — Triple Foundation copy (differs from the Triple Higher copy above)
```json
null
```
