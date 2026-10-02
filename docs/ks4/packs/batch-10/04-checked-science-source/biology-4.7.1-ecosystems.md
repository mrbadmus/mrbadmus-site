# Ecosystems  (Biology, AQA 4.7.1)

**Appears on routes:** Combined Foundation, Combined Higher, Triple Foundation, Triple Higher
**Route copies that differ from Triple Higher:** Combined Foundation, Triple Foundation (the route tags are to be set from the AQA spec's own HT / separate-science labels, not from these copies)

## Examiner's route tags (AQA spec, 2 Oct 2026)
| point | layer | spec ref |
|---|---|---|
| Organism, population, community, habitat, ecosystem (theory 1; common_mistake; key_note) | base | 8464/8461 4.7.1.1 |
| Interdependence; removing a species; stable community (theory 2; key_note) | base | 8464/8461 4.7.1.1 |
| Natural vs artificial ecosystems; monoculture (theory 3) | base (context) | 8464/8461 4.7.3.1 |
| "Level of productivity" (theory 3) | not in spec | — |
| `higher` — effect of abiotic/biotic changes on communities, from data | base — not HT | 8464/8461 4.7.1.2, 4.7.1.3 |
| `higher` — "self-sustaining unit with inputs … and outputs" | not in spec | — |
| quiz q1 | base | 8464/8461 4.7.1.1 |
| quiz q2 | base | 8464/8461 4.7.1.1 |
| quiz q3 | base | 8464/8461 4.7.3.1 |

True page routes: CF CH TF TH. Site currently ships: CF CH TF TH — matches (but the `higher` data skill is hidden from CF and TF — flagged ECO-F1).

This is SOURCE MATERIAL: checked science to draw from. Quiz questions (with their wrong-answer explanations), the examiner tip, worked examples (FIFA), equations and required-practical data are kept VERBATIM. The theory text may be re-cut. The matching activity is to be REPLACED (it prints its own answers). It is not a page structure to copy.

## summary

Define ecosystem, population, community and habitat, and explain how organisms depend on each other.

## theory
```json
[
  {
    "content": "Ecology is the study of how organisms interact with each other and with their environment.\n\nORGANISM — an individual living thing (e.g. one robin, one oak tree, one earthworm).\n\nPOPULATION — all the individuals of ONE SPECIES living in the same area at the same time (e.g. all the robins in a woodland).\n\nCOMMUNITY — all the populations of DIFFERENT SPECIES living together in the same area (e.g. all the animals, plants, fungi and microorganisms in a woodland).\n\nHABITAT — the specific place where an organism lives within an ecosystem (e.g. the woodland floor, the canopy, a particular pond).\n\nECOSYSTEM — a community of organisms PLUS all the non-living (abiotic) factors in the same area. An ecosystem includes everything — living and non-living — in a defined area.",
    "heading": "Key Ecology Terms"
  },
  {
    "content": "All species within a community are INTERDEPENDENT — they depend on each other directly or indirectly for their survival.\n\nIf one species changes significantly, it affects others — sometimes the effects ripple through the whole ecosystem (called a CASCADE EFFECT).\n\nExamples of interdependence:\nPlants depend on bees for POLLINATION — without bees, many plants cannot reproduce.\nBees depend on flowering plants for NECTAR and POLLEN — their food source.\nShrews depend on earthworms for food.\nEarthworms depend on leaf litter (decomposing plant material) for food.\nDeer depend on grass and shrubs for food.\nWolves depend on deer as prey.\nIf wolves are removed → deer population explodes → vegetation is overgrazed → many plant species decline → animals that depend on those plants also decline.\n\nA STABLE COMMUNITY is one where populations remain roughly constant over time — because the various checks and balances (predation, competition, disease) keep each population within its range.",
    "heading": "Interdependence in Ecosystems"
  },
  {
    "content": "Ecosystems exist at many scales and in many environments.\n\nNATURAL ECOSYSTEMS include: tropical rainforests, coral reefs, temperate woodlands, grasslands, deserts, tundra, deep ocean.\n\nARTIFICIAL ECOSYSTEMS created by humans include: farmland (agricultural fields), fish farms, ornamental gardens, nature reserves.\n\nArtificial ecosystems tend to have LOWER BIODIVERSITY than natural ones — they are often dominated by one or a few species (monocultures).\n\nDifferent ecosystems are characterised by their specific:\nABIOTIC CONDITIONS (temperature, rainfall, light levels, soil type).\nBIOTIC FACTORS (which species live there, what eats what).\nLEVEL OF PRODUCTIVITY (how much energy is fixed by plants).",
    "heading": "Types of Ecosystem"
  }
]
```

## higher

Students should be able to explain how changes to abiotic and biotic factors affect communities, using data as evidence. Stable communities have balanced interactions — changes to one component ripple through the whole system. The concept of the ecosystem as a self-sustaining unit with inputs (sunlight, inorganic nutrients) and outputs (heat, waste) is important for understanding sustainability.

## common_mistake

Students often confuse COMMUNITY and ECOSYSTEM. A community is all the LIVING ORGANISMS in an area. An ecosystem includes the community PLUS all the non-living (abiotic) factors. Remember: Ecosystem = Community + Abiotic environment.

## key_note

Organism → Population (one species) → Community (all species) → Ecosystem (community + abiotic factors). All species are interdependent — changes to one affect others (cascade effect). Stable community = populations roughly constant over time.

## matching
```json
{
  "instruction": "Match each term to its correct definition.",
  "pairs": [
    [
      "Population",
      "All individuals of ONE species in a given area"
    ],
    [
      "Community",
      "ALL populations of different species living together in the same area"
    ],
    [
      "Ecosystem",
      "Community PLUS all the non-living (abiotic) factors in the same area"
    ],
    [
      "Habitat",
      "The specific place where an organism lives"
    ],
    [
      "Interdependence",
      "All species in a community depend on each other directly or indirectly"
    ]
  ],
  "title": "Match the Ecology Term"
}
```

## quiz
```json
[
  {
    "opts": [
      [
        "A community is all the living organisms in an area. An ecosystem is the community PLUS all the non-living (abiotic) factors.",
        true
      ],
      [
        "A community is larger than an ecosystem — it includes several ecosystems.",
        false
      ],
      [
        "They are the same thing — both describe all organisms in an area.",
        false
      ],
      [
        "An ecosystem only includes animals. A community includes all living things.",
        false
      ]
    ],
    "q": "What is the difference between a community and an ecosystem?",
    "wrong_explanations": {
      "1": "An ECOSYSTEM is larger — it includes the community PLUS all abiotic factors. A community is just the living part.",
      "2": "They are NOT the same — a community is the living component only. An ecosystem adds the non-living environment.",
      "3": "An ecosystem includes ALL living organisms (animals, plants, fungi, microorganisms) plus abiotic factors — not just animals."
    }
  },
  {
    "opts": [
      [
        "Deer population increases — deer overgraze vegetation — plant diversity declines — other animals that depend on those plants also decline",
        true
      ],
      [
        "The ecosystem immediately collapses — all species die without wolves",
        false
      ],
      [
        "Other predators increase in number to compensate for the wolves",
        false
      ],
      [
        "Nothing changes — deer populations regulate themselves",
        false
      ]
    ],
    "q": "Wolves are removed from a woodland ecosystem. What is the most likely consequence?",
    "wrong_explanations": {
      "1": "Ecosystems rarely collapse immediately — they often shift to a new, less diverse stable state. But the cascade of effects described is accurate.",
      "2": "Some compensation by other predators may occur — but wolves are often keystone predators, so full compensation is rare.",
      "3": "Without predators, prey populations often grow beyond what the habitat can support — leading to overgrazing and eventual population crash."
    }
  },
  {
    "opts": [
      [
        "They are dominated by one or a few crop species — most other species are excluded or removed",
        true
      ],
      [
        "Artificial ecosystems are physically smaller than natural ones",
        false
      ],
      [
        "Artificial ecosystems have less sunlight because they are sheltered",
        false
      ],
      [
        "Animals avoid artificial ecosystems because they can detect human presence",
        false
      ]
    ],
    "q": "Why do artificial ecosystems (like farmland) tend to have lower biodiversity than natural ecosystems?",
    "wrong_explanations": {
      "1": "Some farms are physically large — size is not the primary reason. MONOCULTURE (one crop species) and removal of 'weeds' and 'pests' dramatically reduces biodiversity.",
      "2": "Farmland typically receives as much sunlight as natural ecosystems — light is not the reason for lower biodiversity.",
      "3": "Many animals do live on farmland — but the monoculture crop structure and use of pesticides/herbicides removes habitat and food for most species."
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
