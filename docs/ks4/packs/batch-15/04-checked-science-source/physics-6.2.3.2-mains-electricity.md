# Mains Electricity  (Physics, AQA 6.2.3.2)

**Appears on routes:** Combined Foundation, Combined Higher, Triple Foundation, Triple Higher
**Route copies that differ from Triple Higher:** none (the route tags are to be set from the AQA spec's own HT / separate-science labels, not from these copies)

## Examiner's route tags (AQA spec, 2 Oct 2026)

| point | layer | spec ref |
|---|---|---|
| three-core cable, colours, roles, live ~230 V, neutral ~0 V, earth 0 V / current only in a fault (theory 1; common_mistake; key_note; q2) | base | 8464 6.2.3.2; 8463 4.2.3.2 |
| live dangerous; body at 0 V; hazards (theory 3) | base | 8464 6.2.3.2; 8463 4.2.3.2 |
| fuses, ratings, circuit breakers, RCDs, double insulation (theory 2; key_note; q1) | beyond spec — not on 8463/8464 (ME-F1); q1 not usable | — |

True page routes: CF CH TF TH (all base). Matches the site.

This is SOURCE MATERIAL: checked science to draw from. Quiz questions (with their wrong-answer explanations), the examiner tip, worked examples (FIFA), equations and required-practical data are kept VERBATIM. The theory text may be re-cut. The matching activity is to be REPLACED (it prints its own answers). It is not a page structure to copy.

## summary

Describe three-core cable colour coding, the earth wire, fuses and electrical safety.

## theory
```json
[
  {
    "content": "Domestic appliances use THREE-CORE CABLE with three wires:\n\n1. LIVE WIRE — brown insulation\nCarries the alternating pd (~230 V relative to earth).\nDANGEROUS — carries current at high pd.\n\n2. NEUTRAL WIRE — blue insulation\nCompletes the circuit. Normally at 0 V.\nCan still carry current — still potentially dangerous.\n\n3. EARTH WIRE — green and yellow striped insulation\nSafety wire — carries NO CURRENT during normal operation.\nConnected to the metal case of appliances.\nIf fault connects live to metal case → current flows through earth → fuse blows → circuit breaks → safe.\n\nMEMORY: Live = Brown; Neutral = Blue; Earth = Green + Yellow.",
    "heading": "Three-Core Cable"
  },
  {
    "content": "FUSE: thin wire in series with live wire — MELTS if current exceeds safe level → circuit breaks.\nRated in amps. Choose just ABOVE normal operating current.\nCommon ratings: 1 A, 3 A, 5 A, 13 A.\n\nCIRCUIT BREAKER: trips instead of melting — can be reset.\nRCD (Residual Current Device): detects current imbalances — very fast response. Essential for bathrooms and outdoor use.\n\nDOUBLE INSULATION:\nTwo layers of insulation between live parts and outer case.\nNo earth wire needed. Symbol: square within a square.\n\nEXAMPLE — selecting fuse:\n1 kW kettle at 230 V: I = 1000 ÷ 230 ≈ 4.3 A → use 5 A fuse.",
    "heading": "Fuses, Circuit Breakers and Safety"
  },
  {
    "content": "WHY LIVE IS DANGEROUS:\nLive is at ~230 V. Touching it while connected to earth → current through body → electric shock.\n\nWHY FUSES AND SWITCHES GO IN THE LIVE WIRE:\nIf in the neutral wire → appliance still at 230 V when 'off' → dangerous.\nIn live wire → appliance fully isolated when switched off.\n\nCOMMON HAZARDS:\nFrayed cables — exposed live wire.\nOverloaded sockets — too many appliances → excess current → heat → fire.\nWater near appliances — water conducts electricity.\nDamaged plugs — loose connections.",
    "heading": "Electrical Safety"
  }
]
```

## common_mistake

Earth wire normally carries NO current — only activates in a fault. Neutral wire (blue) IS at ~0 V but CAN carry current. Fuses and switches must be in the LIVE wire so the appliance is fully isolated when switched off.

## key_note

Live = brown (~230 V). Neutral = blue (0 V). Earth = green/yellow (safety, no normal current). Fuse in live wire — just above operating current. Earth wire diverts fault current → blows fuse → safe. Double insulation = no earth needed. Switches in live wire only.

## matching
```json
{
  "instruction": "Match each wire to its colour, voltage and role.",
  "pairs": [
    [
      "Live wire",
      "Brown — carries ~230 V alternating pd from the supply"
    ],
    [
      "Neutral wire",
      "Blue — at 0 V, completes the circuit back to the supply"
    ],
    [
      "Earth wire",
      "Green and yellow — safety wire, normally carries no current"
    ],
    [
      "Fuse",
      "In the live wire — melts if current exceeds safe value"
    ]
  ],
  "title": "Three-Core Cable Wires"
}
```

## quiz
```json
[
  {
    "opts": [
      [
        "If in the neutral wire, the appliance remains at 230 V even when the fuse blows — still dangerous",
        true
      ],
      [
        "The neutral wire has too much resistance for a fuse to work",
        false
      ],
      [
        "Fuses only work with DC — neutral carries AC",
        false
      ],
      [
        "The neutral wire is at 230 V — it would blow constantly",
        false
      ]
    ],
    "q": "Why must a fuse be in the live wire, not the neutral wire?",
    "wrong_explanations": {
      "1": "Neutral wire resistance is very low — fuses work electrically in either wire. The reason is SAFETY ISOLATION.",
      "2": "Both wires carry AC — fuses work with AC. The reason is about isolating the appliance from the dangerous 230 V.",
      "3": "Neutral is at ~0 V, not 230 V. Live is the dangerous wire at high pd."
    }
  },
  {
    "opts": [
      [
        "Large current flows through earth wire, fuse blows, circuit breaks — case is made safe",
        true
      ],
      [
        "Current stays in the case — metal is a poor conductor",
        false
      ],
      [
        "Earth wire permanently absorbs the fault current",
        false
      ],
      [
        "Nothing — earth wire only activates in thunderstorms",
        false
      ]
    ],
    "q": "A metal-cased appliance develops a fault — live touches the case. What happens if it is properly earthed?",
    "wrong_explanations": {
      "1": "Metal is an excellent conductor — current flows easily through it.",
      "2": "Earth wire provides a low-resistance path. The resulting surge blows the fuse. Earth does not permanently carry current.",
      "3": "Earth wire activates whenever live connects to earth (e.g. through the metal case) — not only in storms."
    }
  }
]
```

## Spec core missing from the frozen data (written from the spec, examiner)

The frozen data covers the wires but teaches the spec's two "explain" points only indirectly (through fuse and switch placement, which is beyond the spec). Verbatim, AQA 8464 6.2.3.2 = 8463 4.2.3.2:

> "The live wire carries the alternating potential difference from the supply. The neutral wire completes the circuit. The earth wire is a safety wire to stop the appliance becoming live.
> The potential difference between the live wire and earth (0 V) is about 230 V. The neutral wire is at, or close to, earth potential (0 V). The earth wire is at 0 V, it only carries a current if there is a fault.
> Students should be able to explain:
> • that a live wire may be dangerous even when a switch in the mains circuit is open
> • the dangers of providing any connection between the live wire and earth."
