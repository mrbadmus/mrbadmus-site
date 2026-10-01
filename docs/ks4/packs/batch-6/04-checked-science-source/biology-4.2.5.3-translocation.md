# Translocation  (Biology, AQA 4.2.5.3)

**Appears on routes:** Combined Foundation, Combined Higher, Triple Foundation, Triple Higher
**Route copies that differ from Triple Higher:** Combined Foundation, Triple Foundation (the route tags are to be set from the AQA spec's own HT / separate-science labels, not from these copies)

## Examiner's route tags (AQA spec, 2 Oct 2026)
| point | layer | spec ref |
|---|---|---|
| Translocation: dissolved sugars in phloem, leaves → use or storage (theory 1, key_note, q1) | base | 8464/8461 4.2.3.2 |
| Both directions vs xylem upwards only (theory 1, theory 3, common_mistake, q2) | base | 4.2.3.2 |
| "Source/sink" words (theory 1, q3) | idea base; words beyond spec | 4.2.3.2 |
| Mechanism: active loading, ATP, companion cells, pressure (theory 2, theory 3 "Driving force"/"Energy", `higher`) | OFF-SPEC — "mechanism of transport is not required" | 4.2.3.2 |
| Phloem/xylem structure (absent — spec core missing) | base | 4.2.3.2 |

True page routes: CF CH TF TH (matches the site). No HT or biology-only content; the frozen `higher` is excluded content and must not be shown. The frozen spec "4.2.5.3" is site numbering; AQA is 4.2.3.2. Flags: `_flags/translocation.md`.

## Spec core missing from the frozen data (written from the spec, examiner)
8464 = 8461, 4.2.3.2: "Students should be able to explain how the structure of root hair cells, xylem and phloem are adapted to their functions." "Xylem tissue transports water and mineral ions from the roots to the stems and leaves. It is composed of hollow tubes strengthened by lignin adapted for the transport of water in the transpiration stream." "Phloem tissue transports dissolved sugars from the leaves to the rest of the plant for immediate use or storage. The movement of food molecules through phloem tissue is called translocation. Phloem is composed of tubes of elongated cells. Cell sap can move from one phloem cell to the next through pores in the end walls. Detailed structure of phloem tissue or the mechanism of transport is not required."

This is SOURCE MATERIAL: checked science to draw from. Quiz questions (with their wrong-answer explanations), the examiner tip, worked examples (FIFA), equations and required-practical data are kept VERBATIM. The theory text may be re-cut. The matching activity is to be REPLACED (it prints its own answers). It is not a page structure to copy.

## summary

Describe translocation and how it differs from transpiration.

## theory
```json
[
  {
    "content": "Translocation is the transport of dissolved SUGARS (mainly SUCROSE) through the PHLOEM from where they are produced to where they are needed or stored.\n\nSource → Sink:\nSOURCE — the place where sugars are made or released (mainly the LEAVES, where photosynthesis takes place).\nSINK — any place where sugars are used or stored:\nGrowing shoot tips — sugars needed for cell division and growth.\nRoots — sugars needed for respiration and converted to starch for storage.\nFruits and seeds — sugars needed for development.\nFlowers — sugars needed for reproduction.\n\nUnlike the transpiration stream, translocation can move sugars in BOTH DIRECTIONS in the phloem — up to growing tips AND down to roots and storage organs.",
    "heading": "What is Translocation?"
  },
  {
    "content": "Sucrose is ACTIVELY LOADED into phloem sieve tubes at the source (leaves) using energy (ATP) from companion cells.\n\nThis creates a high concentration of sucrose in the phloem at the source end.\n\nWater enters the phloem by osmosis (moving from xylem, where it's more dilute) → increases pressure at the source end.\n\nThis pressure drives the flow of sugar solution THROUGH the phloem towards the sink.\n\nAt the sink, sucrose is actively UNLOADED from the phloem and used or converted to starch for storage.\n\nThis reduces the concentration at the sink end, maintaining the pressure difference and keeping the flow going.",
    "heading": "How Translocation Works"
  },
  {
    "content": "Students often confuse these two transport processes. Here is a clear comparison:\n\nTRANSPIRATION:\nSubstance moved: WATER (and dissolved minerals)\nVessel: XYLEM\nDirection: UPWARDS ONLY (roots → leaves)\nCells: DEAD cells\nDriving force: evaporation from leaves creating transpiration pull\nEnergy: PASSIVE (no ATP needed)\n\nTRANSLOCATION:\nSubstance moved: SUGARS (sucrose)\nVessel: PHLOEM\nDirection: BOTH DIRECTIONS (source → sink)\nCells: LIVING cells\nDriving force: active loading of sucrose creates pressure\nEnergy: ACTIVE (ATP required to load/unload sucrose)",
    "heading": "Transpiration vs Translocation — Key Differences"
  }
]
```

## higher

Active loading of sucrose into phloem sieve tubes at source cells (leaves) requires ATP from companion cells. This creates high osmotic pressure — water enters by osmosis from adjacent xylem, increasing hydrostatic pressure. The pressure gradient drives sucrose solution toward sink cells (roots, fruits, growing tips) where sucrose is actively unloaded — maintaining the gradient.

## common_mistake

Translocation = SUGARS in PHLOEM. Transpiration = WATER in XYLEM. These are the two most commonly confused terms in plant biology. Translocation moves in BOTH directions — transpiration only goes UPWARDS. Phloem cells are LIVING — xylem cells are DEAD.

## key_note

Translocation: sucrose in phloem, source (leaves) to sink (roots, fruits, tips), both directions, living cells, uses ATP. NOT the same as transpiration (water in xylem, upwards only, dead cells, passive).

## matching
```json
{
  "instruction": "Sort each statement into transpiration or translocation.",
  "pairs": [
    [
      "Transpiration",
      "Water moves up through xylem from roots to leaves — pulled by evaporation"
    ],
    [
      "Translocation",
      "Sucrose moves through phloem from leaves to growing roots and fruits"
    ],
    [
      "Transpiration",
      "Involves dead, hollow, lignified cells"
    ],
    [
      "Translocation",
      "Can move substances both upwards and downwards in the plant"
    ],
    [
      "Transpiration",
      "Rate increases in hot, bright, dry and windy conditions"
    ],
    [
      "Translocation",
      "Requires ATP energy — companion cells supply energy to sieve tubes"
    ]
  ],
  "title": "Transpiration or Translocation?"
}
```

## quiz
```json
[
  {
    "opts": [
      [
        "Sucrose (dissolved sugar) — from leaves to other parts of the plant",
        true
      ],
      [
        "Water and dissolved mineral ions — from roots to leaves",
        false
      ],
      [
        "Oxygen produced by photosynthesis",
        false
      ],
      [
        "Carbon dioxide for use in photosynthesis",
        false
      ]
    ],
    "q": "What is the main substance transported in phloem?",
    "wrong_explanations": {
      "1": "Water and minerals = XYLEM transport (transpiration stream). Phloem carries sugars.",
      "2": "Oxygen diffuses through air spaces and out through stomata — it is not transported in phloem.",
      "3": "CO₂ diffuses through stomata into the leaf — it is not transported in phloem."
    }
  },
  {
    "opts": [
      [
        "Both upwards and downwards — from source (leaves) to any sink where sugar is needed",
        true
      ],
      [
        "Upwards only — like the transpiration stream in xylem",
        false
      ],
      [
        "Downwards only — gravity pulls the sugar solution down to the roots",
        false
      ],
      [
        "Outwards only — from the centre of the stem to the leaf surfaces",
        false
      ]
    ],
    "q": "In which direction does translocation move?",
    "wrong_explanations": {
      "1": "Upwards only = TRANSPIRATION in XYLEM. Translocation in phloem moves in both directions depending on where the sink is.",
      "2": "If translocation were downwards only, growing shoot tips at the top of the plant could never receive sugars — but they clearly do.",
      "3": "Translocation moves along the length of the plant (up and down), not outwards from centre to leaf surface."
    }
  },
  {
    "opts": [
      [
        "Any part of the plant where sugars are used or stored — e.g. roots, fruits, growing tips",
        true
      ],
      [
        "The leaves — where sugars are produced by photosynthesis",
        false
      ],
      [
        "The phloem vessels that transport sugars through the plant",
        false
      ],
      [
        "The stomata — where water and gases are exchanged",
        false
      ]
    ],
    "q": "What is a 'sink' in the context of translocation?",
    "wrong_explanations": {
      "1": "The leaves are the SOURCE — where sugars are MADE. A sink is the DESTINATION where sugars are used or stored.",
      "2": "The phloem is the VESSEL — not the destination. Sinks are the organs that USE or STORE the sugars.",
      "3": "Stomata are gas exchange pores — they have no role in the source-sink relationship of translocation."
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
