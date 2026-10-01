# Reflex Actions  (Biology, AQA 4.5.2)

**Appears on routes:** Combined Foundation, Combined Higher, Triple Foundation, Triple Higher
**Route copies that differ from Triple Higher:** none (the route tags are to be set from the AQA spec's own HT / separate-science labels, not from these copies)

## Examiner's route tags (AQA spec, 2 Oct 2026)

| point | layer | spec ref |
|---|---|---|
| Reflex = automatic, rapid, no conscious part of the brain; why important (theory 1, 3; key_note; q1, q2) | base | 8464 4.5.2 / 8461 4.5.2.1 |
| Reflex arc: receptor → sensory → synapse → relay → synapse → motor → effector (theory 2; key_note; q3) | base | 8464 4.5.2 / 8461 4.5.2.1 |
| Reflex vs voluntary pathway; why faster (theory 3; q1, q2) | base | 8464 4.5.2 / 8461 4.5.2.1 |
| Cerebral cortex, cerebellum, medulla (theory 3 gloss; q3 distractors) | triple vocabulary | 8461 4.5.2.2 (biology only) |

True page routes: CF CH TF TH, all base. Site currently ships the same.

## Spec core missing from the frozen data (written from the spec, examiner)

The synapse is never placed in the reflex arc. The spec names it as an arc structure:

> "Students should be able to explain how the various structures in a reflex arc – including the sensory neurone, synapse, relay neurone and motor neurone – relate to their function. Students should understand why reflex actions are important. Reflex actions are automatic and rapid; they do not involve the conscious part of the brain." (8464 4.5.2; 8461 4.5.2.1)

This is SOURCE MATERIAL: checked science to draw from. Quiz questions (with their wrong-answer explanations), the examiner tip, worked examples (FIFA), equations and required-practical data are kept VERBATIM. The theory text may be re-cut. The matching activity is to be REPLACED (it prints its own answers). It is not a page structure to copy.

## summary

Describe reflex actions, the reflex arc and why reflexes are faster than voluntary responses.

## theory
```json
[
  {
    "content": "A REFLEX is a rapid, automatic response to a stimulus that does not require conscious thought.\n\nReflexes are protective — they allow the body to respond to potentially harmful stimuli BEFORE the conscious brain can process the situation.\n\nKey features of a reflex:\nAUTOMATIC — happens without thinking.\nRAPID — much faster than a voluntary response.\nINVOLUNTARY — you cannot choose not to do it.\nSTEREOTYPED — always the same response to the same stimulus.\n\nExamples:\nWithdrawing your hand from a hot surface.\nKnee-jerk reflex (tapping the patellar tendon).\nPupil constricting in bright light (pupil reflex).\nSneezing and coughing.\nBlinking when an object moves towards the eye.\nBaby's grasp reflex.",
    "heading": "What is a Reflex?"
  },
  {
    "content": "A reflex arc is the specific nerve pathway along which a reflex signal travels. Crucially, it passes through the SPINAL CORD rather than up to the conscious brain — this is what makes it so fast.\n\nThe pathway of a reflex arc:\n1. STIMULUS — a change detected by a sense organ (e.g. heat on the skin).\n2. RECEPTOR — specialised cells detect the stimulus and generate an electrical impulse.\n3. SENSORY NEURONE — carries the impulse to the spinal cord (part of the CNS).\n4. RELAY NEURONE — in the spinal cord, receives the impulse and passes it on. Also sends a signal UP to the brain — so the brain becomes aware AFTER the reflex has already occurred.\n5. MOTOR NEURONE — carries impulse from spinal cord to the effector.\n6. EFFECTOR — the muscle contracts (or gland secretes) to produce the response.\n7. RESPONSE — e.g. the hand moves away from the heat source.\n\nThe brain is aware of the reflex — but AFTER the response has already happened.",
    "heading": "The Reflex Arc"
  },
  {
    "content": "VOLUNTARY response pathway:\nReceptor → sensory neurone → spinal cord → UP to brain → conscious processing → DOWN from brain → motor neurone → effector.\n\nREFLEX pathway:\nReceptor → sensory neurone → spinal cord (relay neurone) → motor neurone → effector.\n\nThe reflex bypasses the conscious brain (cerebral cortex) — this eliminates the time needed for:\nSignal travelling up to the brain.\nConscious processing and decision-making.\nSignal travelling back down from the brain.\n\nTypical voluntary reaction time: 0.2–0.3 seconds.\nTypical reflex reaction time: 0.04–0.1 seconds.\n\nThis 3–5× speed advantage can prevent serious injury — for example, moving your hand away from a sharp object or flame before the pain signal has even reached consciousness.",
    "heading": "Why Reflexes are Faster than Voluntary Responses"
  }
]
```

## common_mistake

A reflex bypasses the CONSCIOUS BRAIN (cerebral cortex) — it is processed in the SPINAL CORD. The brain does receive the signal (that's why you become aware of it), but it does NOT initiate the reflex. Students often say 'the brain controls reflexes' — the brain is only aware of them afterwards.

## key_note

Reflex arc: stimulus → receptor → sensory neurone → relay neurone (spinal cord) → motor neurone → effector → response. Faster than voluntary because it bypasses the conscious brain. Involuntary and automatic.

## matching
```json
{
  "instruction": "Match each component to its role in the reflex arc.",
  "pairs": [
    [
      "Stimulus",
      "The change that triggers the reflex — e.g. touching a sharp object"
    ],
    [
      "Receptor",
      "Detects the stimulus and generates an electrical impulse"
    ],
    [
      "Sensory neurone",
      "Carries the impulse from the receptor to the spinal cord"
    ],
    [
      "Relay neurone",
      "In the spinal cord — connects sensory to motor neurone"
    ],
    [
      "Motor neurone",
      "Carries impulse from spinal cord to the effector"
    ],
    [
      "Effector",
      "Muscle contracts or gland secretes — produces the response"
    ]
  ],
  "title": "Match Each Step of the Reflex Arc"
}
```

## quiz
```json
[
  {
    "opts": [
      [
        "They bypass the conscious brain — the signal is processed in the spinal cord using a shorter pathway",
        true
      ],
      [
        "Reflex neurones conduct impulses faster than voluntary neurones",
        false
      ],
      [
        "Reflexes use fewer neurotransmitters so synaptic delay is reduced",
        false
      ],
      [
        "The brain prioritises reflex signals over other information",
        false
      ]
    ],
    "q": "Why are reflexes faster than voluntary responses?",
    "wrong_explanations": {
      "1": "Neurone conduction speed varies by myelination — not fundamentally by whether it's a reflex or voluntary pathway.",
      "2": "Synaptic delay is similar in both — the key saving is the elimination of the brain processing step entirely.",
      "3": "The brain doesn't 'prioritise' reflexes — it is simply not involved in initiating them."
    }
  },
  {
    "opts": [
      [
        "The reflex arc bypasses the conscious brain — the withdrawal response occurred before pain was processed",
        true
      ],
      [
        "Pain receptors in the hand don't work under extreme heat",
        false
      ],
      [
        "The brain sends an emergency signal faster than normal in dangerous situations",
        false
      ],
      [
        "Motor neurones are faster than sensory neurones",
        false
      ]
    ],
    "q": "You touch a hot surface and pull your hand away before you feel pain. What does this demonstrate?",
    "wrong_explanations": {
      "1": "Pain receptors DO work — you feel the pain a fraction of a second after your hand has already moved away.",
      "2": "The brain doesn't speed up for emergencies — the reflex works independently of conscious brain processing.",
      "3": "Motor and sensory neurones have similar conduction speeds — the key is the PATHWAY length, not individual neurone speed."
    }
  },
  {
    "opts": [
      [
        "The spinal cord — relay neurones connect sensory and motor neurones here",
        true
      ],
      [
        "The cerebral cortex — the thinking part of the brain",
        false
      ],
      [
        "The cerebellum — which coordinates movement",
        false
      ],
      [
        "The medulla oblongata — which controls heart rate and breathing",
        false
      ]
    ],
    "q": "In which part of the CNS is a spinal reflex arc processed?",
    "wrong_explanations": {
      "1": "The cerebral cortex is the conscious thinking brain — reflex arcs specifically BYPASS this to be fast.",
      "2": "The cerebellum coordinates balance and smooth movement — it is not the site of spinal reflex processing.",
      "3": "The medulla oblongata controls automatic functions like heart rate — but reflex arcs for quick withdrawal responses are processed in the spinal cord."
    }
  }
]
```
