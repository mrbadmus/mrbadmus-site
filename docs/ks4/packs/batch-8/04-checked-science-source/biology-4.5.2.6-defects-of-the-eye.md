# Defects of the Eye  (Biology, AQA 4.5.2.6)

**Appears on routes:** Triple Foundation, Triple Higher
**Route copies that differ from Triple Higher:** none (the route tags are to be set from the AQA spec's own HT / separate-science labels, not from these copies)

## Examiner's route tags (AQA spec, 2 Oct 2026)

| point | layer | spec ref |
|---|---|---|
| Myopia and hyperopia: rays do not focus on the retina; causes (theory 1, 2; key_note; common_mistake; q1) | triple | 8461 4.5.2.3 |
| Spectacle lenses refract rays to focus on the retina: concave for myopia, convex for hyperopia (theory 1–3; q1) | triple | 8461 4.5.2.3 |
| Interpret ray diagrams of both defects and their correction (not drawn in the file — diagram) | triple | 8461 4.5.2.3 |
| New technologies: hard and soft contact lenses, laser surgery on the cornea, replacement lens (theory 3; q2) — hard/soft and replacement lens missing, see below | triple | 8461 4.5.2.3 |
| Lens power sign, presbyopia, prevalence | context (true) | — (lenses: 8463 4.6.2.5, physics only) |
| RP, equations, `higher` | none — no HT statement | — |

True page routes: TF TH (no eye content in 8464). All triple, no higher layer.
Site currently ships: TF TH — matches.

## Spec core missing from the frozen data (written from the spec, examiner)

8461 4.5.2.3: "New technologies now include hard and soft contact lenses, laser surgery to change the shape of the cornea and **a replacement lens in the eye**." The file does not mention hard vs soft contact lenses, and does not mention lens replacement at all (the natural lens is removed and an artificial lens implanted).
"Students should be able to interpret ray diagrams, showing these two common defects of the eye and demonstrate how spectacle lenses correct them." The file is text only; the ray diagrams must be drawn.

This is SOURCE MATERIAL: checked science to draw from. Quiz questions (with their wrong-answer explanations), the examiner tip, worked examples (FIFA), equations and required-practical data are kept VERBATIM. The theory text may be re-cut. The matching activity is to be REPLACED (it prints its own answers). It is not a page structure to copy.

## summary

Describe the causes of long-sight and short-sight and how they are corrected.

## theory
```json
[
  {
    "content": "SHORT-SIGHT (MYOPIA) means being unable to see distant objects clearly — they appear blurred.\n\nCAUSE:\nThe eyeball is too LONG (front to back), OR the lens is too curved (too powerful).\nLight from distant objects is brought to a focus IN FRONT OF the retina — not on it.\nThe image on the retina is therefore blurred.\nClose objects can still be seen clearly — the lens can round up enough to focus them.\n\nCORRECTION:\nCONCAVE (diverging) LENS — diverges the light rays before they enter the eye.\nThis moves the focal point backwards — onto the retina.\nConcave lenses have a negative power value.\nCan also be corrected by: laser eye surgery (reshaping the cornea to reduce its curvature).\n\nPREVALENCE: short-sight has become more common globally — particularly in young people. Thought to be linked to increased close-up work (screens, reading) and less time outdoors.",
    "heading": "Short-Sightedness (Myopia)"
  },
  {
    "content": "LONG-SIGHT (HYPEROPIA) means being unable to see near objects clearly — they appear blurred.\n\nCAUSE:\nThe eyeball is too SHORT (front to back), OR the lens is too flat (not powerful enough).\nLight from nearby objects would be brought to a focus BEHIND the retina — but the retina intercepts the rays before they converge.\nThe image on the retina is blurred.\nDistant objects may be seen more clearly as they require less refraction.\n\nCORRECTION:\nCONVEX (converging) LENS — converges the light rays before they enter the eye.\nThis moves the focal point forward — onto the retina.\nConvex lenses have a positive power value.\nCan also be corrected by: laser eye surgery (reshaping the cornea to increase curvature).\n\nAGE-RELATED LONG-SIGHT (PRESBYOPIA):\nAs people age, the lens becomes less flexible → cannot round up as much → difficulty focusing on near objects.\nThis is why many people need reading glasses after the age of 40–50.",
    "heading": "Long-Sightedness (Hyperopia)"
  },
  {
    "content": "SPECTACLES (GLASSES):\nSafest option — no surgery involved.\nEasily updated as prescription changes.\nConvex lenses for long-sight; concave lenses for short-sight.\n\nCONTACT LENSES:\nSit directly on the cornea.\nInvisible when worn — cosmetic advantage.\nRisk of infection if not handled hygienically.\nSame lens types as glasses (concave or convex).\n\nLASER EYE SURGERY:\nUses a laser to reshape the CORNEA — permanently altering its curvature.\nShort-sight: cornea flattened → less refraction → focal point moves back.\nLong-sight: cornea made more curved → more refraction → focal point moves forward.\nPermanent correction — no need for glasses or contacts afterwards.\nRisks: dry eyes, glare, halos, rare complications. Only suitable for adults with stable prescription.",
    "heading": "Corrective Methods Compared"
  }
]
```

## common_mistake

Short-sight is corrected by a CONCAVE lens (diverging). Long-sight is corrected by a CONVEX lens (converging). Students often get these the wrong way round. Memory tip: Short-sight = Concave = diverging (spreads light out, moves focal point back). Long-sight = convex = converging (brings light together, moves focal point forward).

## key_note

Short-sight (myopia): eyeball too long, image in front of retina → correct with CONCAVE lens. Long-sight (hyperopia): eyeball too short, image behind retina → correct with CONVEX lens. Laser surgery reshapes cornea permanently.

## matching
```json
{
  "instruction": "Match each feature to short-sight or long-sight.",
  "pairs": [
    [
      "Short-sight",
      "Cannot see distant objects clearly — eyeball too long or lens too curved"
    ],
    [
      "Long-sight",
      "Cannot see near objects clearly — eyeball too short or lens too flat"
    ],
    [
      "Short-sight",
      "Corrected with a concave (diverging) lens"
    ],
    [
      "Long-sight",
      "Corrected with a convex (converging) lens"
    ],
    [
      "Short-sight",
      "Image forms in front of the retina"
    ],
    [
      "Long-sight",
      "Image would form behind the retina"
    ]
  ],
  "title": "Short-sight or Long-sight?"
}
```

## quiz
```json
[
  {
    "opts": [
      [
        "Short-sight (myopia) — corrected with concave (diverging) lenses",
        true
      ],
      [
        "Long-sight (hyperopia) — corrected with convex (converging) lenses",
        false
      ],
      [
        "Short-sight (myopia) — corrected with convex (converging) lenses",
        false
      ],
      [
        "Long-sight (hyperopia) — corrected with concave (diverging) lenses",
        false
      ]
    ],
    "q": "A student cannot see the board clearly but can read their textbook easily. What is the most likely condition and correction?",
    "wrong_explanations": {
      "1": "Cannot see far (board) but CAN see near (textbook) = LONG-SIGHT. Long-sight is corrected with CONVEX lenses.",
      "2": "Cannot see far but CAN see near = SHORT-SIGHT. Concave lenses correct short-sight, not convex.",
      "3": "Long-sight cannot see near objects and CAN see distant objects more easily. If near vision is fine, it's short-sight."
    }
  },
  {
    "opts": [
      [
        "The laser flattens the cornea — reducing its curvature and refractive power, moving the focal point back onto the retina",
        true
      ],
      [
        "The laser makes the cornea more curved — increasing refraction and moving the focal point forward",
        false
      ],
      [
        "The laser reshapes the lens — making it flatter to reduce refraction",
        false
      ],
      [
        "The laser shortens the eyeball — bringing the retina closer to the focal point",
        false
      ]
    ],
    "q": "How does laser eye surgery correct short-sight?",
    "wrong_explanations": {
      "1": "Making the cornea MORE curved = correcting LONG-SIGHT (needs more refraction). Short-sight needs LESS refraction = FLATTER cornea.",
      "2": "Laser surgery operates on the CORNEA — not the lens. The lens is not reshaped by laser treatment.",
      "3": "Laser surgery cannot change the physical length of the eyeball — it only reshapes the cornea's surface curvature."
    }
  }
]
```
