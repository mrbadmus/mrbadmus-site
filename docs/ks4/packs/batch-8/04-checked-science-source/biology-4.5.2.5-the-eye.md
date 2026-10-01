# The Eye  (Biology, AQA 4.5.2.5)

**Appears on routes:** Triple Foundation, Triple Higher
**Route copies that differ from Triple Higher:** none (the route tags are to be set from the AQA spec's own HT / separate-science labels, not from these copies)

## Examiner's route tags (AQA spec, 2 Oct 2026)

| point | layer | spec ref |
|---|---|---|
| Eye = sense organ with receptors sensitive to light intensity and colour; rods/cones (theory 1) | triple | 8461 4.5.2.3 |
| Structures and functions: retina, optic nerve, sclera, cornea, iris, ciliary muscles, suspensory ligaments (theory 1; key_note) — sclera missing, see below | triple | 8461 4.5.2.3 |
| Accommodation, near and distant (theory 2; common_mistake; key_note; q1) | triple | 8461 4.5.2.3 |
| Adaptation to dim light / pupil reflex (theory 2; q2) | triple | 8461 4.5.2.3 |
| Fovea, blind spot, "70%" figure, radial/circular muscles | context (true) | — |
| RP, equations, `higher` | none — no HT statement in 4.5.2.3 | — |

True page routes: TF TH (no eye content in 8464). All triple, no higher layer.
Site currently ships: TF TH — matches.

## Spec core missing from the frozen data (written from the spec, examiner)

8461 4.5.2.3: "Students should be able to identify the following structures on a diagram of the eye and explain how their structure is related to their function: • retina • optic nerve • **sclera** • cornea • iris • ciliary muscles • suspensory ligaments." The sclera appears nowhere in the file. Sclera: the tough white outer layer of the eyeball; protects the eye and keeps its shape (muscles that move the eye attach to it).

This is SOURCE MATERIAL: checked science to draw from. Quiz questions (with their wrong-answer explanations), the examiner tip, worked examples (FIFA), equations and required-practical data are kept VERBATIM. The theory text may be re-cut. The matching activity is to be REPLACED (it prints its own answers). It is not a page structure to copy.

## summary

Describe the structure of the eye and the function of each part.

## theory
```json
[
  {
    "content": "The eye is a sense organ — it detects light stimuli and converts them into electrical impulses sent to the brain via the optic nerve.\n\nKey structures:\n\nCORNEA — transparent, curved front surface. Refracts (bends) light — does most of the focusing (about 70% of total refraction).\n\nIRIS — the coloured ring of muscle around the pupil. Controls the size of the PUPIL to regulate how much light enters.\n\nPUPIL — the hole in the centre of the iris. Not a structure itself — just the opening. Lets light into the eye.\n\nLENS — a flexible, transparent disc behind the iris. Fine-tunes focusing by changing shape (ACCOMMODATION). Held in place by suspensory ligaments attached to the ciliary body.\n\nCILIARY MUSCLE — ring of muscle surrounding the lens. Contracts or relaxes to change the tension on the lens via the suspensory ligaments, altering the lens shape and focal length.\n\nSUSPENSORY LIGAMENTS — fibres connecting the lens to the ciliary muscle. When ciliary muscle contracts → ligaments loosen → lens becomes more rounded (for near vision).\n\nRETINA — the light-sensitive layer at the back of the eye. Contains two types of photoreceptor cells: RODS (sensitive to light intensity — monochrome, dim conditions) and CONES (sensitive to colour — need bright light, concentrated in the fovea).\n\nFOVEA (yellow spot) — area of highest cone density on the retina — sharpest colour vision.\n\nOPTIC NERVE — carries electrical impulses from the retina to the brain for processing.\n\nBLIND SPOT — where the optic nerve exits — no photoreceptors here, so no vision in this area.",
    "heading": "Structure of the Eye"
  },
  {
    "content": "ACCOMMODATION is the process by which the lens changes shape to focus on objects at different distances.\n\nFOCUSING ON A NEAR OBJECT:\nCiliary muscles CONTRACT.\nSuspensory ligaments SLACKEN (less tension on lens).\nLens becomes more ROUNDED (more curved, fatter).\nMore refraction → shorter focal length → image focused on retina.\n\nFOCUSING ON A DISTANT OBJECT:\nCiliary muscles RELAX.\nSuspensory ligaments become TAUT (pull on lens).\nLens becomes FLATTER (less curved, thinner).\nLess refraction → longer focal length → image focused on retina.\n\nMEMORY AID:\nNear = ciliary contracts, lens round.\nFar = ciliary relaxes, lens flat.\n\nTHE PUPIL REFLEX (controlling light entry):\nBRIGHT LIGHT → circular muscles of iris CONTRACT → pupil CONSTRICTS (gets smaller) → less light enters → prevents damage to retina.\nDIM LIGHT → radial muscles of iris CONTRACT → pupil DILATES (gets larger) → more light enters → improves vision in low light.",
    "heading": "How the Eye Focuses — Accommodation"
  }
]
```

## common_mistake

For near vision: ciliary muscles CONTRACT and lens becomes more ROUNDED. For far vision: ciliary muscles RELAX and lens becomes FLATTER. Students often get this backwards. Remember: when you look at something NEAR, the ciliary muscle has to work hard (CONTRACT) to make the lens rounder.

## key_note

Cornea: main refraction. Lens: fine focus (accommodation). Near: ciliary contracts → lens round. Far: ciliary relaxes → lens flat. Retina: rods (dim/mono), cones (colour/bright). Fovea: sharpest vision. Optic nerve → brain.

## matching
```json
{
  "instruction": "Match each structure to what it does.",
  "pairs": [
    [
      "Cornea",
      "Transparent curved surface — provides most of the eye's refraction"
    ],
    [
      "Iris",
      "Coloured ring of muscle — controls pupil size and light entry"
    ],
    [
      "Lens",
      "Flexible disc — fine-tunes focus by changing shape (accommodation)"
    ],
    [
      "Ciliary muscle",
      "Contracts or relaxes to change lens shape via suspensory ligaments"
    ],
    [
      "Retina",
      "Light-sensitive layer — contains rods and cones that convert light to electrical signals"
    ],
    [
      "Optic nerve",
      "Carries electrical impulses from the retina to the brain"
    ]
  ],
  "title": "Match the Eye Structure to its Function"
}
```

## quiz
```json
[
  {
    "opts": [
      [
        "Ciliary muscles contract → suspensory ligaments slacken → lens becomes more rounded for near vision",
        true
      ],
      [
        "Ciliary muscles relax → suspensory ligaments become taut → lens becomes flatter for near vision",
        false
      ],
      [
        "Ciliary muscles contract → suspensory ligaments become taut → lens becomes flatter",
        false
      ],
      [
        "Ciliary muscles relax → suspensory ligaments slacken → lens becomes more rounded",
        false
      ]
    ],
    "q": "A student looks from a distant window to a book close to them. What happens to the ciliary muscles and lens?",
    "wrong_explanations": {
      "1": "Relaxing ciliary muscles = FAR vision (flat lens). For NEAR vision, ciliary muscles must CONTRACT.",
      "2": "When ciliary muscles contract, ligaments SLACKEN (not become taut). The lens rounds up because tension is removed.",
      "3": "Relaxing ciliary muscles causes ligaments to become taut — but the lens becomes FLAT, not rounded."
    }
  },
  {
    "opts": [
      [
        "To reduce the amount of light entering the eye — preventing damage to the sensitive retina",
        true
      ],
      [
        "To increase the amount of light entering — bright light improves vision",
        false
      ],
      [
        "To improve colour vision — cones work better with a smaller pupil",
        false
      ],
      [
        "The lens expands when bright and blocks more of the pupil",
        false
      ]
    ],
    "q": "Why do the pupils constrict in bright light?",
    "wrong_explanations": {
      "1": "Constriction REDUCES light entry — pupils dilate to INCREASE light entry in dim conditions.",
      "2": "Cones work well in bright light regardless of pupil size — the pupil reflex is about PROTECTING the retina from excessive light.",
      "3": "The lens doesn't change size or block the pupil — accommodation changes lens shape, not size."
    }
  }
]
```
