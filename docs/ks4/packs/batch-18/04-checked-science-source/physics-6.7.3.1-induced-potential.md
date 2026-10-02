# Induced Potential and the Generator Effect  (Physics, AQA 6.7.3.1 (HT only, physics only))

**Appears on routes:** Triple Higher
**Route copies that differ from Triple Higher:** none (the route tags are to be set from the AQA spec's own HT / separate-science labels, not from these copies)

## Examiner's route tags (AQA spec, 2 Oct 2026)
True spec reference: **8463 4.7.3.1 Induced potential (HT only)**, under 4.7.3 "(physics only) (HT only)"; no 8464 equivalent. The `spec` field "6.7.3.1" is the site's internal number.

| point | layer | spec ref |
|---|---|---|
| Generator effect; induced pd / current; opposing field (theory 1; common_mistake; key_note; `higher`) | triple-higher | 8463 4.7.3.1 |
| Size factors: speed, field strength, turns (theory 1, 3; q1) | triple-higher | 8463 4.7.3.1 |
| Direction factors (direction of movement, polarity of field) | triple-higher — missing, see below | 8463 4.7.3.1 |
| Coil area factor; Fleming's right-hand rule; back-emf; "flux", "emf", Faraday/Lenz names | not in spec — F1, F2, F5 | — |
| Simple AC generator, slip rings, split-ring commutator (theory 2–3; q2) | triple-higher (belongs to `uses-generator-effect`) — F6 | 8463 4.7.3.2 |
| quiz q1 | triple-higher — usable | 8463 4.7.3.1 |
| quiz q2 | triple-higher — usable | 8463 4.7.3.2 |

True page routes: TH. Site currently ships: TH — matches.

## Spec core missing from the frozen data (written from the spec, examiner)
8463 4.7.3.1, verbatim — the source never states the first sentence's pd/current distinction plainly, and gives direction only through Fleming's right-hand rule (not in the spec):

> "If an electrical conductor moves relative to a magnetic field or if there is a change in the magnetic field around a conductor, a potential difference is induced across the ends of the conductor. If the conductor is part of a complete circuit, a current is induced in the conductor. This is called the generator effect."

> "Students should be able to recall the factors that affect the direction of the induced potential difference/induced current."

The factors, as AQA marks them: the direction of movement (in vs out; up vs down) and the direction of the magnetic field (which pole leads). Reverse either one and the induced pd/current reverses; reverse both and it is unchanged.

This is SOURCE MATERIAL: checked science to draw from. Quiz questions (with their wrong-answer explanations), the examiner tip, worked examples (FIFA), equations and required-practical data are kept VERBATIM. The theory text may be re-cut. The matching activity is to be REPLACED (it prints its own answers). It is not a page structure to copy.

## summary

Describe how a potential difference is induced when magnetic flux through a conductor changes.

## theory
```json
[
  {
    "content": "The GENERATOR EFFECT (electromagnetic induction): a POTENTIAL DIFFERENCE (voltage) is induced in a conductor when there is a CHANGE IN MAGNETIC FLUX through that conductor.\n\nFaraday's Law:\nThe magnitude of the induced pd is proportional to the RATE OF CHANGE of magnetic flux.\n\nLenz's Law:\nThe induced current produces a magnetic field that OPPOSES the change that caused it.\nThis is why generators require work to produce electricity.\n\nFACTORS AFFECTING INDUCED pd:\nMAGNET STRENGTH: stronger magnet → greater flux change → larger pd.\nSPEED OF MOVEMENT: faster movement → more rapid flux change → larger pd.\nNUMBER OF COIL TURNS: more turns → each cut by flux → larger pd (pd ∝ N).\nCROSS-SECTIONAL AREA: larger coil area → more flux → larger pd.\n\nDIRECTION OF INDUCED CURRENT (Fleming's right-hand rule):\nThumb = motion of conductor.\nIndex finger = field direction.\nMiddle finger = induced current direction.",
    "heading": "The Generator Effect"
  },
  {
    "content": "A GENERATOR converts kinetic energy into electrical energy using electromagnetic induction.\n\nSIMPLE AC GENERATOR:\nCoil of wire rotating in a magnetic field.\nAs coil rotates, it cuts through magnetic field lines.\nEmf (electromotive force) induced → current flows in the circuit.\n\nWHY AC IS PRODUCED:\nAs the coil rotates, the rate at which it cuts field lines varies.\nAt 0° to field: cutting rate maximum → maximum emf.\nAt 90° to field: parallel to field, cutting rate zero → zero emf.\nComplete rotation → sinusoidal AC output.\nFrequency of AC = frequency of rotation of coil.\n\nSLIP RINGS AND BRUSHES:\nAllow current to flow from rotating coil to external circuit.\nSlip rings rotate with the coil.\nBrushes (carbon) press against the rings — stationary contacts.",
    "heading": "Simple Generators"
  },
  {
    "content": "To INCREASE the induced pd from a generator:\nRotate the coil FASTER → increases rate of flux change.\nUse a STRONGER MAGNET → greater flux, greater rate of change.\nUse MORE TURNS on the coil → more conductors cutting the field.\nUse a LARGER COIL → more flux threading through.\n\nSPLIT-RING COMMUTATOR (for DC output):\nReplace slip rings with split-ring commutator.\nEvery half-turn, the connections swap → current in external circuit always flows in same direction → DC (pulsing).\nUsed in DC generators and electric motors.\n\nELECTRIC MOTORS vs GENERATORS:\nThe same device can be a motor OR a generator depending on energy input/output.\nMOTOR: electrical energy → kinetic energy (current in → rotation out).\nGENERATOR: kinetic energy → electrical energy (rotation in → current out).\nBack-emf: a motor generates a back-emf opposing the driving current — limits speed.",
    "heading": "Increasing Induced pd"
  }
]
```

## higher

HT only — describe the generator effect and factors affecting induced pd. Explain why AC is produced by a simple generator and how a split-ring commutator gives DC output. Apply Fleming's right-hand rule to find induced current direction.

## common_mistake

A potential difference is induced when the magnetic flux CHANGES — not just when a conductor is in a magnetic field. A conductor stationary in a magnetic field has no induced pd. The faster the change, the larger the induced pd (Faraday's Law). Lenz's Law: the induced current OPPOSES the change — not just in any direction.

## key_note

Generator effect: changing magnetic flux induces pd. Faraday: pd ∝ rate of flux change. Lenz: induced current opposes change. Increase pd: faster movement, stronger magnet, more coil turns, larger area. AC generator: rotating coil → sinusoidal output. DC: split-ring commutator reverses connections each half-turn.

## matching
```json
{
  "instruction": "Match each change to its effect on the induced pd.",
  "pairs": [
    [
      "Magnet moved faster",
      "Increased rate of flux change → larger induced pd"
    ],
    [
      "Fewer coil turns",
      "Less conductor cutting field per rotation → smaller induced pd"
    ],
    [
      "Larger magnet",
      "Greater magnetic flux → greater change → larger induced pd"
    ],
    [
      "Coil stationary in field",
      "No change in flux → no induced pd"
    ]
  ],
  "title": "Generator Effect"
}
```

## quiz
```json
[
  {
    "opts": [
      [
        "The changing magnetic flux as the magnet moves induces the current. Push faster, use stronger magnet, or use more coil turns to increase it.",
        true
      ],
      [
        "The magnetic field alone induces the current. A stronger static field gives more current.",
        false
      ],
      [
        "Friction between the magnet and coil generates the current. Push harder for more current.",
        false
      ],
      [
        "The proximity to the coil induces current. Bring the magnet closer without moving it for maximum effect.",
        false
      ]
    ],
    "q": "A bar magnet is pushed into a coil of wire. What induces a current, and how can the induced current be increased?",
    "wrong_explanations": {
      "1": "A static magnetic field — however strong — induces NO current. The field must CHANGE to induce a current.",
      "2": "Friction is irrelevant — electromagnetic induction is caused by changing flux, not mechanical friction.",
      "3": "A stationary magnet close to a coil induces NO current — the flux must be CHANGING (the magnet must be moving)."
    }
  },
  {
    "opts": [
      [
        "As the coil rotates, the rate at which it cuts field lines varies sinusoidally — the emf and current reverse direction every half-turn",
        true
      ],
      [
        "AC generators use alternating magnets that switch polarity regularly — this produces AC",
        false
      ],
      [
        "The slip rings swap connections every half-turn — reversing the current direction",
        false
      ],
      [
        "Generators always produce AC — there is no physical way to make DC from rotation",
        false
      ]
    ],
    "q": "Why does a simple AC generator produce alternating current rather than direct current?",
    "wrong_explanations": {
      "1": "Generator magnets are permanent — they don't switch polarity. The AC arises from the coil's rotation geometry.",
      "2": "Slip rings maintain continuous connection without reversal — it's the SPLIT-RING COMMUTATOR (not slip rings) that produces DC by swapping connections each half-turn.",
      "3": "DC CAN be produced from rotation — using a split-ring commutator instead of slip rings."
    }
  }
]
```
