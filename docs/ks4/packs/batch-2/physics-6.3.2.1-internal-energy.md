# Internal Energy  (Physics, AQA 6.3.2.1)

**Appears on routes:** Combined Foundation, Combined Higher, Triple Foundation, Triple Higher
**Route copies that differ from Triple Higher:** none (the route tags are to be set from the AQA spec's own HT / separate-science labels, not from these copies)

This is SOURCE MATERIAL: checked science to draw from. Quiz questions (with their wrong-answer explanations), the examiner tip, worked examples (FIFA), equations and required-practical data are kept VERBATIM. The theory text may be re-cut. The matching activity is to be REPLACED (it prints its own answers). It is not a page structure to copy.

## summary

Define internal energy and explain how heating affects a system.

## theory
```json
[
  {
    "content": "INTERNAL ENERGY is the total kinetic energy and potential energy of all the particles in a system.\n\nINTERNAL ENERGY = sum of:\nKINETIC ENERGY of particles — from their random motion (vibration, translation, rotation).\nPOTENTIAL ENERGY of particles — stored in the bonds and intermolecular forces between them.\n\nWhen a substance is heated, the energy supplied goes into the internal energy of the system.\n\nThis increased internal energy can produce TWO EFFECTS:\n1. TEMPERATURE RISE — particles move faster (higher average KE).\n2. CHANGE OF STATE — particles gain enough PE to overcome intermolecular forces (bonds break/form).\n\nNOTE: Both effects cannot happen simultaneously for a pure substance at its melting or boiling point — during a change of state, temperature stays constant even as energy is supplied.",
    "heading": "What Is Internal Energy?"
  },
  {
    "content": "TEMPERATURE is a measure of the AVERAGE KINETIC ENERGY of the particles.\n\nHigher temperature = faster-moving particles = higher average KE.\nLower temperature = slower-moving particles = lower average KE.\n\nAt the same temperature:\nDifferent materials have different internal energies because they have different numbers of particles and different potential energy arrangements.\n\nIMPORTANT DISTINCTION:\nTEMPERATURE (°C or K) — measures average KE per particle.\nTHERMAL ENERGY (J) — total energy transferred — depends on temperature difference AND mass AND specific heat capacity.\n\nExample:\nA large cool lake and a small hot cup of tea:\nThe tea is hotter (higher temperature = higher average KE per particle).\nBut the lake has far greater total internal energy (more particles, more total KE + PE).",
    "heading": "Temperature and Kinetic Energy"
  },
  {
    "content": "When energy is SUPPLIED to a substance:\nEFFECT 1 — TEMPERATURE RISES:\nParticles move faster (KE increases).\nThis happens when no change of state is occurring.\nCalculated using ΔE = mcΔθ.\n\nEFFECT 2 — CHANGE OF STATE:\nTemperature stays CONSTANT while state changes.\nEnergy goes into increasing POTENTIAL ENERGY — breaking intermolecular bonds.\nCalculated using E = mL (latent heat equation).\n\nOn a HEATING CURVE (temperature vs time for constant energy input):\nSloping sections: temperature rising (KE increasing).\nFLAT sections: change of state occurring (temperature constant, PE increasing).\nFlat section during melting = melting point.\nFlat section during boiling = boiling point.\n\nOn a COOLING CURVE: the reverse — flat sections at condensation and freezing points.",
    "heading": "Heating and Cooling — Two Effects"
  }
]
```

## common_mistake

During a CHANGE OF STATE, temperature stays CONSTANT — energy goes into potential energy (breaking bonds), not kinetic energy. Students often think heating always raises temperature — but at melting/boiling point, temperature is flat on the heating curve until the change is complete.

## key_note

Internal energy = KE + PE of all particles. Heating → increases internal energy → either raises temperature (KE) or causes change of state (PE). Temperature = average KE per particle. During change of state: temperature constant, PE increasing. Heating curve: slopes = temperature rise; flat sections = changes of state.

## matching
```json
{
  "instruction": "Match each statement to the correct concept.",
  "pairs": [
    [
      "Internal energy",
      "Total kinetic + potential energy of ALL particles in the system"
    ],
    [
      "Temperature",
      "Measure of AVERAGE kinetic energy per particle"
    ],
    [
      "Flat section on heating curve",
      "Change of state — temperature constant, energy increasing PE (breaking bonds)"
    ],
    [
      "Sloping section on heating curve",
      "Temperature rising — energy increasing KE of particles"
    ]
  ],
  "title": "Internal Energy Concepts"
}
```

## quiz
```json
[
  {
    "opts": [
      [
        "A change of state — energy is increasing potential energy to break intermolecular bonds, not raising temperature",
        true
      ],
      [
        "The heater has broken — no energy is being supplied",
        false
      ],
      [
        "The substance has reached its maximum possible temperature",
        false
      ],
      [
        "The substance is losing heat to the surroundings at exactly the same rate as energy is supplied",
        false
      ]
    ],
    "q": "A substance is heated at constant power. Its temperature stays constant for several minutes. What is happening?",
    "wrong_explanations": {
      "1": "If no energy were being supplied, temperature would fall (cool to room temperature) — a constant temperature at the melting/boiling point specifically indicates a change of state.",
      "2": "There is no maximum temperature concept for most substances in normal conditions — temperature can always rise further if energy is supplied.",
      "3": "While heat loss to surroundings can cause apparent temperature plateaus, in exam context a flat section on a heating curve always indicates a change of state — the temperature is pinned at the melting or boiling point."
    }
  },
  {
    "opts": [
      [
        "The swimming pool — despite lower temperature, it has vastly more particles so its total KE + PE is much greater",
        true
      ],
      [
        "The cup of tea — higher temperature means more internal energy",
        false
      ],
      [
        "They have the same — internal energy depends only on temperature",
        false
      ],
      [
        "Cannot compare — internal energy requires knowing density as well",
        false
      ]
    ],
    "q": "A large cool swimming pool and a small hot cup of tea — which has greater internal energy?",
    "wrong_explanations": {
      "1": "Higher temperature means higher AVERAGE KE per particle — but internal energy is the TOTAL for all particles. The pool has far more particles, so total internal energy is greater.",
      "2": "Internal energy depends on temperature, mass AND specific heat capacity — not temperature alone.",
      "3": "Density is relevant to calculating particle numbers but the main point is that internal energy is an EXTENSIVE property — it scales with the amount of matter."
    }
  }
]
```
