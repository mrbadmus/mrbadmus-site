# Development of the Model of the Atom  (Chemistry, AQA 5.1.1.3)

**Appears on routes:** Combined Foundation, Combined Higher, Triple Foundation, Triple Higher
**Route copies that differ from Triple Higher:** none (the route tags are to be set from the AQA spec's own HT / separate-science labels, not from these copies)

## Examiner's route tags (AQA spec, 2 Oct 2026)
| point | layer | spec ref |
|---|---|---|
| Models change with new evidence (theory 1; key_note) | base | 8464 5.1.1.3; 8462 4.1.1.3 |
| Indivisible spheres → plum pudding → nuclear → Bohr (theory 1–2; key_note; common_mistake) | base. Plum pudding date, "not solid" and "positive mass" are imprecise (F1–F3) | 8464 5.1.1.3; 8462 4.1.1.3 |
| Alpha scattering observations and conclusion | base. State that mass is concentrated (F3) | 8464 5.1.1.3; 8462 4.1.1.3 |
| Electrons jump shells by absorbing/emitting energy (theory 2) | context (physics 6.4.1.1, not chemistry) | 8464 6.4.1.1 |
| Bohr's line-spectra evidence (theory 3) | not required (F4) | 8464 5.1.1.3 |
| Protons (subdivided nuclear charge); Chadwick, neutron ~20 years later (theory 3) | base. Proton step missing (F5) | 8464 5.1.1.3; 8462 4.1.1.3 |
| quiz q1, q2 | base, usable as written | 8464 5.1.1.3; 8462 4.1.1.3 |

True page routes: CF CH TF TH. Site currently ships: CF CH TF TH, which matches. Common content with physics 8464 6.4.1.3 / 8463 4.4.1.3 (batch 5 `development-atomic-model`).

This is SOURCE MATERIAL: checked science to draw from. Quiz questions (with their wrong-answer explanations), the examiner tip, worked examples (FIFA), equations and required-practical data are kept VERBATIM. The theory text may be re-cut. The matching activity is to be REPLACED (it prints its own answers). It is not a page structure to copy.

## summary

Describe how the model of the atom developed as new evidence was discovered.

## theory
```json
[
  {
    "content": "Scientific models are the best current explanation of how something works — but they must change when new experimental evidence cannot be explained by the existing model.\n\nThe history of atomic models is a perfect example of how science works:\nA model is proposed → experiments are done → if results conflict with the model, the model is revised.\n\nThe key models in chronological order:\n1. Dalton's solid sphere (1803)\n2. Thomson's plum pudding model (1897)\n3. Rutherford's nuclear model (1911)\n4. Bohr's shell model (1913)",
    "heading": "Why Scientific Models Change"
  },
  {
    "content": "DALTON'S MODEL (1803):\nAtoms are solid, indivisible spheres.\nDifferent elements have differently sized spheres.\nAtoms cannot be split, created or destroyed.\nRevised when electrons were discovered.\n\nTHOMSON'S PLUM PUDDING MODEL (1897):\nDiscovery of the ELECTRON — a tiny negatively charged particle inside atoms — proved atoms were not solid or indivisible.\nThomson proposed: an atom is a ball of POSITIVE CHARGE with ELECTRONS dotted throughout — like plums in a pudding (or currants in a bun).\nRevised after Rutherford's gold foil experiment.\n\nRUTHERFORD'S NUCLEAR MODEL (1911):\nRutherford fired positively charged ALPHA PARTICLES at a very thin sheet of gold foil.\nExpected (plum pudding): all particles would pass through with small deflections.\nObserved:\nMOST particles passed STRAIGHT THROUGH — atoms are mostly empty space.\nSOME were deflected at large angles — something positive inside repelled them.\nA FEW bounced STRAIGHT BACK — hit something very dense and concentrated.\nConclusion: atoms have a tiny, dense, positively charged NUCLEUS at the centre, surrounded by mostly empty space with electrons.\n\nBOHR'S MODEL (1913):\nBohr proposed electrons orbit in fixed SHELLS (energy levels) at specific distances from the nucleus.\nEach shell has a fixed energy — electrons can jump between shells by absorbing or emitting energy.",
    "heading": "From Solid Sphere to Nuclear Model"
  },
  {
    "content": "After Bohr's model, further work led to the modern understanding:\n\nProtons and neutrons were later identified in the nucleus.\nNEUTRON discovery (Chadwick, 1932) explained why atomic mass was not just the number of protons.\n\nWhy each model was better:\nDalton → Thomson: discovery of the electron showed atoms had internal structure.\nThomson → Rutherford: gold foil experiment showed positive charge was concentrated in a tiny nucleus, not spread throughout.\nRutherford → Bohr: observed line spectra of hydrogen showed electrons could only occupy specific energy levels.\n\nThis chain of model improvements shows the power of the scientific method — each experiment built on previous knowledge and revealed new detail about atomic structure.",
    "heading": "The Modern Understanding"
  }
]
```

## common_mistake

In Rutherford's experiment, MOST particles passed STRAIGHT THROUGH — this is what shows atoms are mostly empty space. Only a FEW bounced back. Students often get this backwards and say most particles bounced back. The few that did bounce back were what proved the nucleus exists.

## key_note

Dalton: solid sphere. Thomson: plum pudding (electrons in positive mass). Rutherford: nuclear model — most particles pass through (empty space), a few bounce back (dense positive nucleus). Bohr: electrons in fixed shells. Each model revised due to new experimental evidence.

## matching
```json
{
  "instruction": "Match each atomic model to the scientist and what evidence led to it.",
  "pairs": [
    [
      "Dalton",
      "Solid indivisible sphere — no subatomic particles known at this time"
    ],
    [
      "Thomson",
      "Plum pudding — discovery of the electron showed atoms had internal structure"
    ],
    [
      "Rutherford",
      "Nuclear model — gold foil experiment showed a tiny dense positive nucleus"
    ],
    [
      "Bohr",
      "Shell model — electrons orbit in fixed energy levels around the nucleus"
    ]
  ],
  "title": "Match the Model to its Scientist and Evidence"
}
```

## quiz
```json
[
  {
    "opts": [
      [
        "Atoms are mostly empty space — most particles found no matter to deflect them",
        true
      ],
      [
        "Gold atoms are very large — the particles passed through the gaps between atoms",
        false
      ],
      [
        "Alpha particles are too fast to be deflected",
        false
      ],
      [
        "The plum pudding model was correct — the positive charge is spread out",
        false
      ]
    ],
    "q": "In Rutherford's gold foil experiment, most alpha particles passed straight through the foil. What does this tell us?",
    "wrong_explanations": {
      "1": "Atomic SIZE explains why particles might miss atoms, not why they pass THROUGH them. The key conclusion is that the atom is mostly empty space internally.",
      "2": "Alpha particles can be deflected — some WERE deflected at large angles, showing the nucleus exists.",
      "3": "The plum pudding model predicted only SMALL deflections. The large angle deflections and back-scattering DISPROVED the plum pudding model."
    }
  },
  {
    "opts": [
      [
        "The gold foil experiment produced results that could not be explained by the plum pudding model — the new model fitted the evidence",
        true
      ],
      [
        "Rutherford was more famous than Thomson, so his model was believed",
        false
      ],
      [
        "The plum pudding model was proposed before electrons were discovered",
        false
      ],
      [
        "Both models are still equally accepted today",
        false
      ]
    ],
    "q": "Why did the scientific community accept Rutherford's nuclear model over Thomson's plum pudding model?",
    "wrong_explanations": {
      "1": "Scientific acceptance is based on EVIDENCE, not reputation — the gold foil results clearly contradicted the plum pudding model.",
      "2": "Thomson's plum pudding model was specifically based on and designed to explain the discovery of electrons.",
      "3": "Rutherford's nuclear model replaced the plum pudding model — it is not still equally accepted, though both are discussed historically."
    }
  }
]
```
