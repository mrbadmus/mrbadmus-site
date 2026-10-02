# Poles of a Magnet and Permanent Magnetism  (Physics, AQA 6.7.1.1)

**Appears on routes:** Combined Foundation, Combined Higher, Triple Foundation, Triple Higher
**Route copies that differ from Triple Higher:** none (the route tags are to be set from the AQA spec's own HT / separate-science labels, not from these copies)

## Examiner's route tags (AQA spec, 2 Oct 2026)
| point | layer | spec ref |
|---|---|---|
| Poles; like repel, unlike attract; non-contact force (theory 1; key_note) | base | 8464 6.7.1.1 = 8463 4.7.1.1 |
| Poles are where the forces are strongest | base — missing from this file (POLES-OF-A-MAGNET-F4) | 8464 6.7.1.1 |
| Magnetic materials iron, steel, nickel, cobalt (theory 1; common_mistake) | base | 8464 6.7.1.2 |
| Permanent vs induced; induced always attracts, loses magnetism quickly (theory 2; key_note) | base — "induced = iron" is IMPRECISE (F2) | 8464 6.7.1.1 |
| Hard/soft materials, alnico (theory 2) | not in spec (enrichment) | — |
| Magnetising, demagnetising, Curie temperature, domains (theory 3) | not in spec (enrichment) — F5 | — |
| quiz q1 | base | 8464 6.7.1.1 |
| quiz q2 | base — WRONG, do not use as written (F1) | 8464 6.7.1.1 |

True page routes: CF CH TF TH. Site currently ships: CF CH TF TH — matches.

This is SOURCE MATERIAL: checked science to draw from. Quiz questions (with their wrong-answer explanations), the examiner tip, worked examples (FIFA), equations and required-practical data are kept VERBATIM. The theory text may be re-cut. The matching activity is to be REPLACED (it prints its own answers). It is not a page structure to copy.

## summary

Describe the properties of magnets, distinguish permanent from induced magnetism, and describe magnetic forces.

## theory
```json
[
  {
    "content": "Every magnet has a NORTH POLE and a SOUTH POLE.\n\nRULES FOR MAGNETIC FORCES:\nLIKE POLES REPEL — N and N repel; S and S repel.\nOPPOSITE POLES ATTRACT — N and S attract.\n\nMagnetic force is a NON-CONTACT FORCE — acts at a distance without touching.\n\nMAGNETIC MATERIALS:\nFerromagnetic materials are attracted to magnets.\nMain ferromagnetic materials at GCSE: IRON, STEEL, NICKEL, COBALT.\nAluminium, copper, plastic, wood — NOT magnetic.\n\nOnly iron, steel, nickel and cobalt can become magnetised or be attracted to magnets.",
    "heading": "Poles and Magnetic Forces"
  },
  {
    "content": "PERMANENT MAGNETS:\nProduce their own persistent magnetic field — they don't need an external field to be magnetic.\nRetain magnetism when the external field is removed.\nMade from HARD magnetic materials — steel, alnico alloys.\nHard materials are harder to magnetise but retain magnetism better.\nExamples: bar magnets, horseshoe magnets, fridge magnets, compass needles.\n\nINDUCED MAGNETS:\nTemporarily magnetised by placing them in a magnetic field.\nWhen the external field is removed, they LOSE their magnetism quickly.\nMade from SOFT magnetic materials — IRON.\nSoft materials are easier to magnetise and demagnetise.\nExamples: iron nail picked up by a magnet; iron core in an electromagnet.\n\nINDUCED MAGNETISM DIRECTION:\nThe induced pole nearest to the magnet's pole is ALWAYS OPPOSITE to that pole.\nThis is why magnets ATTRACT ferromagnetic materials — the near end becomes the opposite pole.",
    "heading": "Permanent and Induced Magnetism"
  },
  {
    "content": "MAGNETISING a material:\nRub with a permanent magnet always in the same direction (stroking method).\nPlace in a SOLENOID carrying DC — the field aligns the magnetic domains.\nHammer while held in the Earth's magnetic field (unreliable).\n\nDEMAGNETISING:\nHEAT — heating above the CURIE TEMPERATURE destroys magnetic domain alignment.\nHAMMERING/VIBRATION — disrupts domain alignment.\nALTERNATING CURRENT (AC) in a solenoid — reverses field repeatedly, randomising domains.\n\nMAGNETIC DOMAINS:\nA magnet is made of tiny regions called DOMAINS — each domain acts like a mini-magnet.\nIn an UNMAGNETISED material: domains point in random directions → overall effect cancels.\nIn a MAGNETISED material: domains are aligned in the same direction → net magnetic field.\nMagnetising aligns the domains; demagnetising randomises them.",
    "heading": "Magnetising and Demagnetising"
  }
]
```

## common_mistake

Only IRON, STEEL, NICKEL and COBALT are magnetic materials. Aluminium and copper are NOT attracted to magnets. Permanent magnets (steel) retain magnetism. Induced magnets (iron) lose it when the field is removed.

## key_note

Like poles repel; opposite poles attract. Permanent magnets: retain magnetism (steel — hard). Induced magnets: temporary, lose magnetism when external field removed (iron — soft). Magnetic materials: iron, steel, nickel, cobalt. Domains: aligned = magnetised, random = unmagnetised.

## matching
```json
{
  "instruction": "Match each statement to permanent magnet or induced magnet.",
  "pairs": [
    [
      "Permanent magnet",
      "Made from steel — retains magnetism without an external field"
    ],
    [
      "Induced magnet",
      "Made from iron — temporary, loses magnetism when external field removed"
    ],
    [
      "Both attract",
      "The near end always becomes the opposite pole — both are attracted to the magnet"
    ],
    [
      "Demagnetising",
      "Heating above Curie temperature or using AC solenoid — randomises domain alignment"
    ]
  ],
  "title": "Magnetic Properties"
}
```

## quiz
```json
[
  {
    "opts": [
      [
        "The steel becomes an induced magnet — the end nearest the magnet becomes opposite in polarity, so they attract",
        true
      ],
      [
        "Steel is made from iron which is naturally magnetic — it has its own permanent field that attracts",
        false
      ],
      [
        "The paper clip gains an electric charge from the magnetic field — opposite charges attract",
        false
      ],
      [
        "The magnetic field passes through the paper clip, pulling it forward",
        false
      ]
    ],
    "q": "A steel paper clip is brought near a bar magnet. Why is the paper clip attracted?",
    "wrong_explanations": {
      "1": "Steel is a MAGNETIC MATERIAL (ferromagnetic) but not permanently magnetised until it is magnetised. The attraction is due to INDUCED MAGNETISM from the bar magnet.",
      "2": "Magnetism and electric charge are separate — magnetic fields don't charge objects with static electricity.",
      "3": "Magnetic forces act on magnetic materials — they don't 'push' the clip forward. The attraction is between the magnetic poles of the induced magnet and the bar magnet."
    }
  },
  {
    "opts": [
      [
        "Fridge magnet: permanent — retains field indefinitely. Compass: also permanent — compass needle must always point north reliably",
        true
      ],
      [
        "Fridge magnet: temporary — it loses magnetism each day. Compass: permanent",
        false
      ],
      [
        "Fridge magnet: stronger field — household magnets are more powerful than compass needles",
        false
      ],
      [
        "Fridge magnet: induced. Compass: permanent — all small magnets are induced magnets",
        false
      ]
    ],
    "q": "A fridge magnet and a compass are both magnets. What is the key difference between them regarding their magnetism?",
    "wrong_explanations": {
      "1": "Both ARE permanent magnets — but the question is testing understanding that both fridge magnets and compass needles are permanent (made from hard magnetic materials).",
      "2": "Strength varies between magnets but strength is not the distinguishing feature the question asks about.",
      "3": "Both the fridge magnet and compass needle are PERMANENT magnets — they must retain their magnetism to function."
    }
  }
]
```
