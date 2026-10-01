# The Brain  (Biology, AQA 4.5.2.4)

**Appears on routes:** Triple Foundation, Triple Higher
**Route copies that differ from Triple Higher:** none (the route tags are to be set from the AQA spec's own HT / separate-science labels, not from these copies)

## Examiner's route tags (AQA spec, 2 Oct 2026)

| point | layer | spec ref |
|---|---|---|
| Brain = billions of interconnected neurones; regions with different functions (theory 1) | triple | 8461 4.5.2.2 |
| Cerebral cortex, cerebellum, medulla: identify on a diagram, describe functions (theory 1; key_note 1st half; common_mistake; q1) | triple | 8461 4.5.2.2 |
| Mapping regions: brain-damage patients, electrical stimulation, MRI (theory 2; key_note "Studied by") | triple-higher | 8461 4.5.2.2 (HT only) |
| Difficulties of investigating and treating brain damage/disease (theory 3; key_note "Hard to treat"; q2) | triple-higher | 8461 4.5.2.2 (HT only) |
| EEG, blood-brain barrier, Gage, HM, gyri/sulci, hemispheres | context only (true, off-spec) | — |
| RP, equations, `higher` | none | — |

True page routes: TF TH (Combined has no brain statement: 8464 4.5.2 names the brain only as part of the CNS). Triple layer = whole page; HT layer = theory 2, theory 3, q2.
Site currently ships: TF TH, with no `higher` section — the HT content (theory 2, theory 3, q2) is shown to TF. Flagged (THE-BRAIN-F1).

This is SOURCE MATERIAL: checked science to draw from. Quiz questions (with their wrong-answer explanations), the examiner tip, worked examples (FIFA), equations and required-practical data are kept VERBATIM. The theory text may be re-cut. The matching activity is to be REPLACED (it prints its own answers). It is not a page structure to copy.

## summary

Describe the structure of the brain, the functions of its main regions and how the brain is studied.

## theory
```json
[
  {
    "content": "The BRAIN is the most complex organ in the human body — containing approximately 86 billion neurones, each connected to thousands of others.\n\nThe brain has several distinct regions, each responsible for different functions:\n\nCEREBRAL CORTEX (cerebrum):\nThe largest part of the brain — the highly folded outer layer.\nResponsible for: consciousness, intelligence, memory, language, personality, voluntary movement, sensory perception.\nDivided into left and right hemispheres — each processes information from the opposite side of the body.\nThe folded structure (gyri and sulci) increases surface area for more neurones.\n\nCEREBELLUM:\nLocated at the back and base of the brain.\nResponsible for: coordination of movement, balance, posture, fine motor control.\nDamage → loss of coordination and balance.\n\nMEDULLA OBLONGATA:\nAt the base of the brain, continuous with the spinal cord.\nControls: unconscious vital functions — heart rate, breathing rate, blood pressure, swallowing, vomiting.\nDamage is life-threatening — these functions are essential for survival.",
    "heading": "Structure of the Brain"
  },
  {
    "content": "The brain is extremely complex and difficult to study — it cannot easily be biopsied or experimented on safely.\n\nMETHODS:\n\nELECTROENCEPHALOGRAPHY (EEG):\nElectrodes placed on the scalp record electrical activity of the brain as patterns of waves.\nUsed to diagnose epilepsy and sleep disorders.\nShows which areas are active but with limited spatial resolution.\n\nFUNCTIONAL MRI (fMRI):\nDetects changes in blood flow to different brain regions — more active regions need more blood and oxygen.\nProduces detailed 3D images showing which brain regions are active during different tasks.\nAllows mapping of brain function non-invasively.\nUsed in research to understand language, memory, emotion and decision-making.\n\nELECTRICAL STIMULATION:\nNeurosurgeons can stimulate specific brain regions electrically during brain surgery (patient kept awake).\nThe patient reports what they experience — helping identify which areas control which functions.\nLed to early mapping of sensory and motor areas.\n\nSTUDYING BRAIN DAMAGE:\nCase studies of patients with specific brain injuries have provided crucial insights.\nFamous case: Phineas Gage — a railway worker whose personality changed dramatically after a rod passed through his frontal lobe (1848).\nPatient HM — removal of hippocampus to treat epilepsy caused inability to form new long-term memories.",
    "heading": "How We Study the Brain"
  },
  {
    "content": "Treating brain conditions is extremely challenging:\n\nBLOOD-BRAIN BARRIER:\nA layer of tightly packed cells around brain blood vessels that prevents many substances from crossing from blood into brain tissue.\nProtects the brain from pathogens and toxins — but also prevents many drugs from reaching brain tissue.\nDrug delivery to the brain is a major challenge in neurology and psychiatry.\n\nNEURONE REPAIR:\nUnlike most body tissues, adult brain neurones cannot regenerate if damaged.\nThis is why brain injuries (stroke, trauma) often cause permanent deficits.\nStem cell research aims to find ways to regenerate damaged brain tissue.\n\nETHICAL CONSTRAINTS:\nBrain tissue cannot be biopsied safely — unlike a tumour elsewhere.\nExperimentation is limited by the ethical requirement to protect patients.\nMuch of our knowledge comes from accidents, disease and animal studies.",
    "heading": "Why the Brain is Difficult to Treat"
  }
]
```

## common_mistake

Students often mix up the three main brain regions. CEREBRAL CORTEX = thinking, memory, language, voluntary movement. CEREBELLUM = coordination and balance. MEDULLA = heart rate and breathing (vital automatic functions). A useful memory trick: 'Cerebellum = coordination' (both start with C and 'coordination').

## key_note

Cerebral cortex: consciousness, intelligence, memory, personality. Cerebellum: coordination, balance. Medulla: heart rate, breathing — vital automatic functions. Studied by: MRI, EEG, electrical stimulation, brain damage case studies. Hard to treat: no neurone regeneration, blood-brain barrier.

## matching
```json
{
  "instruction": "Match each brain region to what it controls.",
  "pairs": [
    [
      "Cerebral cortex",
      "Consciousness, memory, language, intelligence, voluntary movement"
    ],
    [
      "Cerebellum",
      "Coordination of movement, balance and posture"
    ],
    [
      "Medulla oblongata",
      "Heart rate, breathing rate — unconscious vital functions"
    ],
    [
      "fMRI scan",
      "Shows which brain regions are active by detecting changes in blood flow"
    ],
    [
      "EEG",
      "Records electrical activity of the brain via electrodes on the scalp"
    ]
  ],
  "title": "Match the Brain Region to its Function"
}
```

## quiz
```json
[
  {
    "opts": [
      [
        "Coordination and balance — the cerebellum controls smooth, coordinated movement",
        true
      ],
      [
        "Heart rate — the cerebellum controls autonomic functions",
        false
      ],
      [
        "Memory and language — the cerebellum controls higher cognitive functions",
        false
      ],
      [
        "Breathing — the cerebellum controls respiratory rate",
        false
      ]
    ],
    "q": "A patient suffers a stroke affecting the cerebellum. Which function is most likely to be impaired?",
    "wrong_explanations": {
      "1": "Heart rate and breathing are controlled by the MEDULLA OBLONGATA — not the cerebellum.",
      "2": "Memory and language are controlled by the CEREBRAL CORTEX — not the cerebellum.",
      "3": "Breathing rate is controlled by the MEDULLA — the cerebellum coordinates movement."
    }
  },
  {
    "opts": [
      [
        "Adult brain neurones cannot regenerate — unlike most other body cells, damaged neurones are not replaced",
        true
      ],
      [
        "The blood-brain barrier prevents blood from reaching damaged areas",
        false
      ],
      [
        "Strokes destroy the entire brain — there is no undamaged tissue to repair from",
        false
      ],
      [
        "The immune system attacks any new neurones, preventing recovery",
        false
      ]
    ],
    "q": "Why is it difficult to repair brain damage caused by a stroke?",
    "wrong_explanations": {
      "1": "The blood-brain barrier restricts what substances cross from blood to brain — it doesn't prevent blood from reaching the brain (in fact strokes are often caused by blood supply being cut off).",
      "2": "Strokes affect specific regions — not the whole brain. The challenge is neurone regeneration in those regions.",
      "3": "The immune system does play a role in brain inflammation after injury — but the primary reason for poor recovery is the inability of neurones to regenerate."
    }
  }
]
```
