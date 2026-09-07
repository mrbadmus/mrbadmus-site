"""Physics · Particle model (6.3) — density, changes of state, internal
energy, specific heat capacity, specific latent heat and gas pressure.

Seventy-two assignment questions across the topic's six subtopics. Every
subtopic here is BASE (tier='foundation', triple_only=False), so a Foundation
Combined class sits all of it and nothing higher-tier-only appears in a stem
or an option.

Where the distractors come from. The calculation subtopics are carried by the
declared mistakes in the curriculum data, because those are the errors a
teacher actually marks:

  · density            — mixing g/cm³ with kg/m³, and inverting m ÷ V
  · changes of state   — treating a state change as a chemical change, and
                         expecting mass to change when it does not
  · internal energy    — assuming heating always raises temperature, and
                         reading temperature as *total* rather than *average*
                         particle energy
  · ΔE = mcΔθ          — using the final temperature instead of Δθ, leaving
                         the mass in grams, dividing where you should
                         multiply, and defaulting to water's c of 4200
  · E = mL             — reaching for ΔE = mcΔθ when the temperature is
                         constant, and swapping Lf for Lv
  · gas pressure       — doing gas-law arithmetic in Celsius, and believing
                         that compressing a gas speeds its molecules up

⚠️ The `particle-motion-pressure` numeric items stay inside the shapes the
lesson page's own BASE theory works through (one p₁V₁ = p₂V₂ substitution and
one p/T substitution, both mirroring its worked examples). The rearranged
pV work named in that subtopic's Higher extension is deliberately absent —
the subtopic is flagged foundation, and a Foundation Combined class is served
this file.

None of these restates a lesson page "Test yourself" question; those are a
different pool under the one-pool-per-surface law.
"""

TOPIC = "particle-model"
SUBJECT = "physics"

QUESTIONS = [
    # ── density-of-materials ────────────────────────────────────────────
    {
        "id": "ks4-density-of-materials-e01",
        "subtopic_slug": "density-of-materials",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "A block of material has a mass of 6.0 kg and a volume of "
                "2.0 m³. Calculate its density.",
        "options": [
            "0.33 kg/m³",
            "12 kg/m³",
            "3.0 kg/m³",
            "4.0 kg/m³",
        ],
        "correct_index": 2,
        "why": "Density is mass per unit volume, so ρ = m ÷ V = 6.0 ÷ 2.0 = "
               "3.0 kg/m³.",
    },
    {
        "id": "ks4-density-of-materials-e02",
        "subtopic_slug": "density-of-materials",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the SI unit of density.",
        "options": [
            "kg/m³",
            "m³/kg",
            "kg/m²",
            "N/m³",
        ],
        "correct_index": 0,
        "why": "Density is mass divided by volume, so its SI unit is "
               "kilograms per cubic metre, kg/m³.",
    },
    {
        "id": "ks4-density-of-materials-e03",
        "subtopic_slug": "density-of-materials",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Aluminium has a density of 2700 kg/m³ and water has a "
                "density of 1000 kg/m³. Predict what happens when a solid "
                "aluminium cube is lowered into water.",
        "options": [
            "It floats, because metals are held up by the surface of water",
            "It floats, because its density is greater than that of water",
            "It sinks, because its density is lower than that of water",
            "It sinks, because its density is greater than that of water",
        ],
        "correct_index": 3,
        "why": "An object sinks when its density is greater than the density "
               "of the fluid, and 2700 kg/m³ is greater than 1000 kg/m³.",
    },
    {
        "id": "ks4-density-of-materials-e04",
        "subtopic_slug": "density-of-materials",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Which statement best defines the density of a material?",
        "options": [
            "The total mass of a sample of the material, in kilograms",
            "The mass of the material per unit volume, in kg/m³",
            "The amount of space a sample of the material fills, in m³",
            "The weight of the material per unit area, in N/m²",
        ],
        "correct_index": 1,
        "why": "Density tells you how much mass is packed into each cubic "
               "metre of a material, so it is mass per unit volume.",
    },
    {
        "id": "ks4-density-of-materials-s01",
        "subtopic_slug": "density-of-materials",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A sample of copper has a density of 8.9 g/cm³. Determine "
                "its density in kg/m³.",
        "options": [
            "0.0089 kg/m³",
            "8900 kg/m³",
            "890 kg/m³",
            "8 900 000 kg/m³",
        ],
        "correct_index": 1,
        "why": "1 g/cm³ is 1000 kg/m³, so a density in g/cm³ is multiplied "
               "by 1000: 8.9 × 1000 = 8900 kg/m³.",
    },
    {
        "id": "ks4-density-of-materials-s02",
        "subtopic_slug": "density-of-materials",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A cooking oil has a density of 920 kg/m³. Calculate the "
                "mass of 0.50 m³ of the oil.",
        "options": [
            "460 kg",
            "1840 kg",
            "920 kg",
            "5.4 × 10⁻⁴ kg",
        ],
        "correct_index": 0,
        "why": "Rearranging ρ = m ÷ V gives m = ρ × V = 920 × 0.50 = 460 kg.",
    },
    {
        "id": "ks4-density-of-materials-s03",
        "subtopic_slug": "density-of-materials",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student finds the density of a small stone. Its mass "
                "is 48 g, and the water level in a measuring cylinder "
                "rises from 25 cm³ to 45 cm³ when the stone is lowered "
                "in. Calculate the density of the stone.",
        "options": [
            "1.1 g/cm³",
            "1.9 g/cm³",
            "0.42 g/cm³",
            "2.4 g/cm³",
        ],
        "correct_index": 3,
        "why": "The volume of the stone is the rise in level, 45 − 25 = "
               "20 cm³, so ρ = m ÷ V = 48 ÷ 20 = 2.4 g/cm³.",
    },
    {
        "id": "ks4-density-of-materials-s04",
        "subtopic_slug": "density-of-materials",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Two blocks have the same mass. Block A has twice the volume "
                "of block B. Compare their densities.",
        "options": [
            "Block A has twice the density of block B",
            "The two blocks have the same density, because they have the "
            "same mass",
            "Block A has half the density of block B",
            "Block A has four times the density of block B",
        ],
        "correct_index": 2,
        "why": "The same mass spread through twice the volume gives half the "
               "mass in each cubic metre, so half the density.",
    },
    {
        "id": "ks4-density-of-materials-h01",
        "subtopic_slug": "density-of-materials",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A steel cuboid measures 5.0 cm by 5.0 cm by 10.0 cm "
                "and has a mass of 1.95 kg. Calculate its density in "
                "kg/m³.",
        "options": [
            "0.0078 kg/m³",
            "7.8 kg/m³",
            "7800 kg/m³",
            "78 000 kg/m³",
        ],
        "correct_index": 2,
        "why": "The volume is 250 cm³, and 1 cm³ = 1 × 10⁻⁶ m³, so V = "
               "2.5 × 10⁻⁴ m³ and ρ = 1.95 ÷ 2.5 × 10⁻⁴ = 7800 kg/m³.",
    },
    {
        "id": "ks4-density-of-materials-h02",
        "subtopic_slug": "density-of-materials",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student measures the density of a stone by displacement, "
                "but does not notice an air bubble trapped underneath it in "
                "the measuring cylinder. Explain the effect on the density "
                "the student calculates.",
        "options": [
            "The density is unaffected, because the bubble adds no mass to "
            "the stone",
            "The density is too low, because the measured volume is larger "
            "than the true volume",
            "The density is too high, because the measured volume is smaller "
            "than the true volume",
            "The density is too high, because the bubble makes the measured "
            "mass larger",
        ],
        "correct_index": 1,
        "why": "The bubble adds to the rise in water level, so V is "
               "overestimated, and dividing the true mass by too large a "
               "volume gives too small a density.",
    },
    {
        "id": "ks4-density-of-materials-h03",
        "subtopic_slug": "density-of-materials",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A sealed hollow plastic ball has a volume of 1.0 × 10⁻³ m³ "
                "and a mass of 0.20 kg. Determine its average density and "
                "predict whether it floats in water (1000 kg/m³).",
        "options": [
            "200 kg/m³, and it floats, because this is less than 1000 kg/m³",
            "200 kg/m³, and it sinks, because a hollow ball holds no material",
            "2000 kg/m³, and it sinks, because this is more than 1000 kg/m³",
            "0.20 kg/m³, and it floats, because this is less than 1000 kg/m³",
        ],
        "correct_index": 0,
        "why": "Average density uses the whole outside volume: ρ = 0.20 ÷ "
               "1.0 × 10⁻³ = 200 kg/m³, well below water, so it floats.",
    },
    {
        "id": "ks4-density-of-materials-h04",
        "subtopic_slug": "density-of-materials",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "When water at 100 °C boils, the same amount of substance "
                "occupies roughly 1600 times the volume as steam. Explain "
                "what happens to its density and to the mass of its "
                "particles.",
        "options": [
            "The density is unchanged, because it is the same substance "
            "throughout, and the mass is unchanged",
            "The density falls to about 1/1600 of its value, and the mass of "
            "the particles falls by the same factor",
            "The density rises by about 1600 times, because the particles "
            "are moving much faster, and the mass is unchanged",
            "The density falls to about 1/1600 of its value, and the mass of "
            "the particles is unchanged",
        ],
        "correct_index": 3,
        "why": "The same particles now fill 1600 times the volume, so mass "
               "per unit volume drops by that factor, but no particles are "
               "created or destroyed so their mass is unchanged.",
    },

    # ── changes-of-state ────────────────────────────────────────────────
    {
        "id": "ks4-changes-of-state-e01",
        "subtopic_slug": "changes-of-state",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the change of state in which a gas turns directly into "
                "a solid.",
        "options": [
            "Sublimation",
            "Deposition",
            "Condensation",
            "Freezing",
        ],
        "correct_index": 1,
        "why": "Deposition is the direct gas-to-solid change; sublimation is "
               "the same route in the opposite direction.",
    },
    {
        "id": "ks4-changes-of-state-e02",
        "subtopic_slug": "changes-of-state",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Which change of state happens when energy is removed from a "
                "gas?",
        "options": [
            "Melting",
            "Boiling",
            "Sublimation",
            "Condensation",
        ],
        "correct_index": 3,
        "why": "Removing energy from a gas lets the intermolecular forces "
               "pull the particles together into a liquid — condensation.",
    },
    {
        "id": "ks4-changes-of-state-e03",
        "subtopic_slug": "changes-of-state",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "A puddle of water on a playground slowly disappears on a "
                "warm day, although the air is far below 100 °C. Name the "
                "process.",
        "options": [
            "Evaporation",
            "Boiling",
            "Sublimation",
            "Condensation",
        ],
        "correct_index": 0,
        "why": "Evaporation happens from the surface of a liquid at any "
               "temperature, when the fastest particles escape into the air.",
    },
    {
        "id": "ks4-changes-of-state-e04",
        "subtopic_slug": "changes-of-state",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State which quantity changes when a pure solid melts.",
        "options": [
            "The total mass of the substance",
            "The number of particles present",
            "The arrangement and spacing of the particles",
            "The mass of each individual particle",
        ],
        "correct_index": 2,
        "why": "Melting rearranges the particles and lets them move "
               "past one another; it creates and destroys nothing, so "
               "the mass and the number of particles are unchanged.",
    },
    {
        "id": "ks4-changes-of-state-s01",
        "subtopic_slug": "changes-of-state",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Describe what happens to the forces between the particles "
                "of a substance as it condenses.",
        "options": [
            "The particles move close enough for the intermolecular forces "
            "to hold them together, and energy is released",
            "The intermolecular forces are overcome, and energy is absorbed "
            "from the surroundings",
            "The forces between the particles are unchanged, because "
            "condensation only changes the shape of the substance",
            "New chemical bonds form inside each molecule, and energy is "
            "released",
        ],
        "correct_index": 0,
        "why": "Condensing means the particles slow and come close enough "
               "for the intermolecular forces to bind them, releasing energy.",
    },
    {
        "id": "ks4-changes-of-state-s02",
        "subtopic_slug": "changes-of-state",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A sealed flask holding 50 g of solid iodine is warmed until "
                "all the solid has turned into purple gas. The sealed flask "
                "stays on the balance throughout. Predict the balance "
                "reading, and explain your answer.",
        "options": [
            "Less than before, because a gas has a lower density than a solid",
            "More than before, because the gas fills a much larger volume",
            "Unchanged, because the same particles are still in the flask — "
            "they have only rearranged",
            "Unchanged, because the gas presses down on the balance just as "
            "hard as the solid did before it was warmed",
        ],
        "correct_index": 2,
        "why": "A change of state creates and destroys no particles, so the "
               "mass in a sealed container cannot change.",
    },
    {
        "id": "ks4-changes-of-state-s03",
        "subtopic_slug": "changes-of-state",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain, in terms of particles, what happens as a solid "
                "melts.",
        "options": [
            "The particles themselves soften and change shape, so the solid "
            "can flow",
            "Energy makes the particles vibrate more until the forces holding "
            "the lattice are overcome and they can flow",
            "The chemical bonds inside each molecule are broken, so the "
            "substance becomes a new liquid substance with new properties",
            "The particles gain mass as energy is supplied, so they can no "
            "longer stay in the lattice",
        ],
        "correct_index": 1,
        "why": "Energy supplied increases the vibration of the particles "
               "until the lattice can no longer hold them in fixed positions.",
    },
    {
        "id": "ks4-changes-of-state-s04",
        "subtopic_slug": "changes-of-state",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare evaporation and boiling.",
        "options": [
            "Both happen only at the boiling point, but evaporation is slower "
            "because it needs less energy",
            "Evaporation happens throughout the whole liquid at any "
            "temperature; boiling happens only at the surface of the liquid",
            "Evaporation forms a new substance, while boiling leaves the "
            "substance chemically unchanged",
            "Evaporation happens at the surface at any temperature; boiling "
            "happens throughout the liquid at its boiling point",
        ],
        "correct_index": 3,
        "why": "Only the fastest surface particles can escape below the "
               "boiling point; at the boiling point bubbles of gas form "
               "throughout the liquid.",
    },
    {
        "id": "ks4-changes-of-state-h01",
        "subtopic_slug": "changes-of-state",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student writes: 'A candle's wax melts and then burns, so "
                "both changes are physical, because wax can always be "
                "recovered.' Evaluate this statement.",
        "options": [
            "Correct — both changes can be reversed, so both are physical",
            "Incorrect — both changes are chemical, because energy is "
            "transferred in each one",
            "Partly correct — melting is physical, but burning is chemical "
            "because new substances form and cannot be recovered",
            "Partly correct — burning is physical, but melting is chemical "
            "because the structure is permanently altered",
        ],
        "correct_index": 2,
        "why": "Melting keeps the wax chemically the same, but burning "
               "produces carbon dioxide and water, which are new substances.",
    },
    {
        "id": "ks4-changes-of-state-h02",
        "subtopic_slug": "changes-of-state",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Naphthalene freezes at 80 °C. Describe what happens to the "
                "arrangement of its particles and to the energy of the "
                "substance as it freezes.",
        "options": [
            "The particles spread further apart, and energy is absorbed from "
            "the surroundings",
            "The particles themselves shrink and pack closer together, and "
            "the total energy of the substance is unchanged",
            "The particles speed up into a fixed lattice, and energy is "
            "absorbed from the surroundings",
            "The particles settle into fixed positions in a lattice, and "
            "energy is transferred to the surroundings",
        ],
        "correct_index": 3,
        "why": "Freezing forms intermolecular forces as the particles take "
               "fixed lattice positions, and forming them releases energy to "
               "the surroundings.",
    },
    {
        "id": "ks4-changes-of-state-h03",
        "subtopic_slug": "changes-of-state",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A block of dry ice (solid carbon dioxide) is left on an "
                "open balance in a laboratory. The reading falls steadily. "
                "Explain why this does not break the rule that mass is "
                "conserved in a change of state.",
        "options": [
            "The carbon dioxide sublimes and the gas disperses into the room "
            "— the particles still exist, they have just left the balance",
            "Mass really is lost here, because the rule about conserving mass "
            "applies only to melting and freezing, not to the sublimation of "
            "a solid",
            "The solid turns into energy as it warms, so some of its mass is "
            "genuinely destroyed",
            "Carbon dioxide gas has less mass per particle than the solid, so "
            "the total mass falls",
        ],
        "correct_index": 0,
        "why": "Mass is conserved in the change itself; the balance reading "
               "falls only because the gas has left the balance pan.",
    },
    {
        "id": "ks4-changes-of-state-h04",
        "subtopic_slug": "changes-of-state",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare the change in particle separation when a mass of "
                "solid melts with the change when the same mass of that "
                "liquid boils.",
        "options": [
            "Melting separates the particles far more, because the rigid "
            "lattice is destroyed all at once",
            "Boiling separates the particles far more, because they must "
            "escape the intermolecular forces completely",
            "Both change the separation by the same amount, because both are "
            "changes of state",
            "Neither of them changes the separation — only the speed at which "
            "the particles move changes in a change of state",
        ],
        "correct_index": 1,
        "why": "Melting only frees particles from fixed positions while they "
               "stay close; boiling pulls them right apart against the "
               "intermolecular forces.",
    },

    # ── internal-energy ─────────────────────────────────────────────────
    {
        "id": "ks4-internal-energy-e01",
        "subtopic_slug": "internal-energy",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Define the internal energy of a system.",
        "options": [
            "The total kinetic energy and potential energy of all the "
            "particles in the system",
            "The total kinetic energy of all the particles in the system",
            "The temperature of the system, measured on the Celsius scale",
            "The total energy supplied to the system by a heater or another "
            "source, measured in joules",
        ],
        "correct_index": 0,
        "why": "Internal energy is the sum of the particles' kinetic energy "
               "from their motion and their potential energy stored in the "
               "forces between them.",
    },
    {
        "id": "ks4-internal-energy-e02",
        "subtopic_slug": "internal-energy",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what the temperature of a substance measures.",
        "options": [
            "The total energy of all the particles in the substance",
            "The average kinetic energy of the particles in the substance",
            "The total kinetic energy of the particles in the substance",
            "The potential energy stored in the forces between the particles",
        ],
        "correct_index": 1,
        "why": "Temperature is a measure of the average kinetic energy per "
               "particle, which is why it does not depend on how much "
               "substance you have.",
    },
    {
        "id": "ks4-internal-energy-e03",
        "subtopic_slug": "internal-energy",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "A block of copper is heated but does not melt. State what "
                "happens to the kinetic energy of its particles.",
        "options": [
            "It decreases, because the energy is stored as potential energy "
            "instead",
            "It stays the same, because the copper has not changed state",
            "It increases, so the temperature of the copper rises",
            "It increases, but the temperature stays the same until the "
            "copper melts",
        ],
        "correct_index": 2,
        "why": "With no change of state, the energy supplied makes the "
               "particles move faster, and faster particles mean a higher "
               "temperature.",
    },
    {
        "id": "ks4-internal-energy-e04",
        "subtopic_slug": "internal-energy",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Which of these quantities is measured in joules?",
        "options": [
            "Temperature",
            "Density",
            "Specific heat capacity",
            "Internal energy",
        ],
        "correct_index": 3,
        "why": "Internal energy is an energy, so it is measured in joules; "
               "temperature is measured in °C or K.",
    },
    {
        "id": "ks4-internal-energy-s01",
        "subtopic_slug": "internal-energy",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Beaker A holds 100 g of water at 90 °C and beaker B holds "
                "500 g of water at 90 °C. Compare the average kinetic energy "
                "of their particles and their internal energies.",
        "options": [
            "B has the higher average kinetic energy and the greater "
            "internal energy",
            "A has the higher average kinetic energy, but B has the greater "
            "internal energy",
            "They have the same average kinetic energy and the same internal "
            "energy",
            "They have the same average kinetic energy, but B has the "
            "greater internal energy",
        ],
        "correct_index": 3,
        "why": "Equal temperature means equal average kinetic energy per "
               "particle, but B has five times as many particles, so its "
               "total energy is far greater.",
    },
    {
        "id": "ks4-internal-energy-s02",
        "subtopic_slug": "internal-energy",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Ice at −20 °C is heated steadily until it becomes water at "
                "20 °C. Describe how the temperature and the internal energy "
                "change over the whole process.",
        "options": [
            "The internal energy rises throughout; the temperature rises, "
            "stays at 0 °C while the ice melts, then rises again",
            "Both the temperature and the internal energy rise steadily "
            "throughout the whole process",
            "The temperature rises throughout, while the internal energy "
            "stays constant during the melting",
            "The internal energy rises throughout the whole process, and the "
            "temperature also rises at a steady rate the entire time",
        ],
        "correct_index": 0,
        "why": "Energy is supplied the whole time, so internal energy always "
               "rises, but at 0 °C it goes into potential energy to break "
               "the lattice rather than into raising the temperature.",
    },
    {
        "id": "ks4-internal-energy-s03",
        "subtopic_slug": "internal-energy",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why the internal energy of a substance includes "
                "potential energy as well as kinetic energy.",
        "options": [
            "Because the particles are pulled downwards by gravity, which "
            "stores gravitational potential energy",
            "Because the particles have weight, and weight is a store of "
            "potential energy",
            "Because there are intermolecular forces between the particles, "
            "and energy is stored in them",
            "Because the chemical bonds inside each molecule store energy "
            "that is released when the substance is heated",
        ],
        "correct_index": 2,
        "why": "Pulling particles apart against the intermolecular forces "
               "stores energy, and that store is the potential energy part "
               "of internal energy.",
    },
    {
        "id": "ks4-internal-energy-s04",
        "subtopic_slug": "internal-energy",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A cup of tea cools from 70 °C to room temperature. Describe "
                "what happens to the internal energy of the tea and to the "
                "internal energy of the surroundings.",
        "options": [
            "The internal energy of both the tea and the surroundings falls",
            "The internal energy of the tea falls, and the internal energy "
            "of the surroundings rises by the same amount",
            "The internal energy of the tea falls, and that energy is "
            "destroyed as the tea reaches room temperature",
            "The internal energy of the tea stays the same, because only its "
            "temperature has changed",
        ],
        "correct_index": 1,
        "why": "Energy is conserved: what the tea's particles lose is "
               "transferred to the particles of the cup, the air and the "
               "table around it.",
    },
    {
        "id": "ks4-internal-energy-h01",
        "subtopic_slug": "internal-energy",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A 1.0 kg block of aluminium and a 1.0 kg block of copper "
                "are both at 60 °C. Compare the average kinetic energy of "
                "their particles.",
        "options": [
            "The aluminium particles have the greater average kinetic "
            "energy, because aluminium has the higher specific heat capacity",
            "The particles of the two blocks have the same average kinetic "
            "energy, because the two blocks are at the same temperature",
            "The copper particles have the greater average kinetic energy, "
            "because copper is the denser of the two metals",
            "The comparison cannot be made without knowing the volume of "
            "each of the two blocks",
        ],
        "correct_index": 1,
        "why": "Temperature is the measure of average kinetic energy per "
               "particle, so equal temperatures mean equal average kinetic "
               "energy whatever the material.",
    },
    {
        "id": "ks4-internal-energy-h02",
        "subtopic_slug": "internal-energy",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Steam at 100 °C condenses to water at 100 °C. Describe what "
                "happens to the kinetic energy and to the potential energy "
                "of the particles.",
        "options": [
            "The kinetic energy is unchanged, and the potential energy "
            "decreases as the particles are drawn closer together",
            "Both the kinetic energy and the potential energy of the "
            "particles decrease as the steam condenses",
            "The kinetic energy decreases, and the potential energy is "
            "unchanged because the temperature is constant",
            "Both the kinetic energy and the potential energy increase, "
            "because energy is released to the surroundings",
        ],
        "correct_index": 0,
        "why": "The temperature is constant, so the average kinetic energy "
               "cannot change; the energy released comes from the fall in "
               "potential energy as the particles come together.",
    },
    {
        "id": "ks4-internal-energy-h03",
        "subtopic_slug": "internal-energy",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Two identical vacuum flasks of soup are left for an hour. "
                "The full flask cools by 5 °C; the half-full flask cools by "
                "9 °C. Explain, using internal energy, why the half-full "
                "flask cools by more.",
        "options": [
            "The half-full soup has a lower specific heat capacity, so its "
            "temperature falls faster",
            "The air trapped above the half-full soup is at a lower "
            "temperature, so it starts cooler",
            "The half-full flask loses far more energy per hour, because "
            "half of its lid is not in contact with soup",
            "The half-full flask holds fewer particles, so the same energy "
            "lost produces a bigger drop in temperature",
        ],
        "correct_index": 3,
        "why": "With less mass there is less internal energy stored, so "
               "transferring a similar amount of energy away costs a larger "
               "temperature drop.",
    },
    {
        "id": "ks4-internal-energy-h04",
        "subtopic_slug": "internal-energy",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why 1 kg of water at 0 °C has a greater internal "
                "energy than 1 kg of ice at 0 °C.",
        "options": [
            "The water is at a slightly higher temperature than the ice, "
            "even though both are recorded as 0 °C",
            "The water particles are moving faster, so their average kinetic "
            "energy is greater than that of the ice particles",
            "The particles have the same average kinetic energy, but the "
            "water particles have more potential energy after melting",
            "The ice actually has the greater internal energy, because it is "
            "the denser of the two and holds its particles more tightly",
        ],
        "correct_index": 2,
        "why": "Both are at 0 °C so the average kinetic energy is the same, "
               "but melting supplied energy that is now stored as potential "
               "energy in the more separated particles.",
    },

    # ── temperature-changes-shc ─────────────────────────────────────────
    {
        "id": "ks4-temperature-changes-shc-e01",
        "subtopic_slug": "temperature-changes-shc",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "The specific heat capacity of aluminium is 900 J/kg°C. "
                "State what this value means.",
        "options": [
            "900 J of energy will raise the temperature of 1 g of aluminium "
            "by 1 °C",
            "900 J of energy will raise the temperature of any mass of "
            "aluminium by 1 °C",
            "900 J of energy will raise the temperature of 1 kg of aluminium "
            "by 1 °C",
            "900 J of energy will melt 1 kg of aluminium at its melting point",
        ],
        "correct_index": 2,
        "why": "Specific heat capacity is the energy needed per kilogram per "
               "degree Celsius, so 900 J heats 1 kg of aluminium by 1 °C.",
    },
    {
        "id": "ks4-temperature-changes-shc-e02",
        "subtopic_slug": "temperature-changes-shc",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Which quantity does the symbol Δθ represent in the equation "
                "ΔE = mcΔθ?",
        "options": [
            "The change in temperature, in °C",
            "The final temperature reached, in °C",
            "The specific heat capacity, in J/kg°C",
            "The energy transferred to the substance, in J",
        ],
        "correct_index": 0,
        "why": "Δθ is the temperature change — final temperature minus "
               "starting temperature — not the final temperature itself.",
    },
    {
        "id": "ks4-temperature-changes-shc-e03",
        "subtopic_slug": "temperature-changes-shc",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Calculate the energy needed to raise the temperature "
                "of 2.0 kg of water by 15 °C. The specific heat "
                "capacity of water is 4200 J/kg°C.",
        "options": [
            "8400 J",
            "126 000 J",
            "63 000 J",
            "2100 J",
        ],
        "correct_index": 1,
        "why": "ΔE = mcΔθ = 2.0 × 4200 × 15 = 126 000 J — all three "
               "factors are multiplied together.",
    },
    {
        "id": "ks4-temperature-changes-shc-e04",
        "subtopic_slug": "temperature-changes-shc",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the unit of specific heat capacity.",
        "options": [
            "J/kg°C",
            "J/kg",
            "J/°C",
            "J",
        ],
        "correct_index": 0,
        "why": "It is the energy per kilogram per degree Celsius, so both "
               "the kilogram and the °C appear on the bottom: J/kg°C. J/kg "
               "is the unit of specific latent heat.",
    },
    {
        "id": "ks4-temperature-changes-shc-s01",
        "subtopic_slug": "temperature-changes-shc",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A 0.50 kg copper block is heated from 18 °C to 78 °C. "
                "Calculate the energy transferred to the block. The specific "
                "heat capacity of copper is 385 J/kg°C.",
        "options": [
            "15 015 J",
            "3465 J",
            "23 100 J",
            "11 550 J",
        ],
        "correct_index": 3,
        "why": "Δθ is 78 − 18 = 60 °C, not 78 °C, so ΔE = 0.50 × 385 × 60 = "
               "11 550 J.",
    },
    {
        "id": "ks4-temperature-changes-shc-s02",
        "subtopic_slug": "temperature-changes-shc",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A 500 g aluminium block is heated and its temperature rises "
                "by 20 °C. Calculate the energy transferred to the block. "
                "The specific heat capacity of aluminium is 900 J/kg°C.",
        "options": [
            "9000 J",
            "9 000 000 J",
            "18 000 J",
            "42 000 J",
        ],
        "correct_index": 0,
        "why": "500 g must be converted to 0.50 kg before substituting: "
               "ΔE = 0.50 × 900 × 20 = 9000 J.",
    },
    {
        "id": "ks4-temperature-changes-shc-s03",
        "subtopic_slug": "temperature-changes-shc",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "In a required practical, 24 000 J of energy is supplied to "
                "a 2.0 kg metal block and its temperature rises by 30 °C. "
                "Calculate the specific heat capacity of the metal.",
        "options": [
            "800 J/kg°C",
            "12 000 J/kg°C",
            "400 J/kg°C",
            "1 440 000 J/kg°C",
        ],
        "correct_index": 2,
        "why": "Rearranging ΔE = mcΔθ gives c = ΔE ÷ (m × Δθ) = 24 000 ÷ "
               "(2.0 × 30) = 400 J/kg°C.",
    },
    {
        "id": "ks4-temperature-changes-shc-s04",
        "subtopic_slug": "temperature-changes-shc",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "In the required practical to determine the specific heat "
                "capacity of a metal block, explain why the block is wrapped "
                "in insulation.",
        "options": [
            "To slow the heating down so that the thermometer reading can "
            "keep up with the block",
            "To reduce the energy transferred to the surroundings, so the "
            "energy supplied is closer to the energy that heats the block",
            "To stop the electric heater from overheating and changing its "
            "power output during the experiment",
            "To raise the specific heat capacity of the metal block, so that "
            "the temperature rise becomes large enough to measure accurately",
        ],
        "correct_index": 1,
        "why": "The calculation assumes all the heater's energy went into "
               "the block, so energy lost to the room makes the measured c "
               "too large; insulation reduces that loss.",
    },
    {
        "id": "ks4-temperature-changes-shc-h01",
        "subtopic_slug": "temperature-changes-shc",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A 50 W immersion heater is switched on for 6.0 minutes in "
                "0.40 kg of oil, and the temperature of the oil rises by "
                "25 °C. Assuming no energy is transferred to the "
                "surroundings, calculate the specific heat capacity of the "
                "oil.",
        "options": [
            "30 J/kg°C",
            "1800 J/kg°C",
            "720 J/kg°C",
            "180 000 J/kg°C",
        ],
        "correct_index": 1,
        "why": "The energy supplied is E = Pt = 50 × 360 s = 18 000 J, so "
               "c = 18 000 ÷ (0.40 × 25) = 1800 J/kg°C — the time must be in "
               "seconds.",
    },
    {
        "id": "ks4-temperature-changes-shc-h02",
        "subtopic_slug": "temperature-changes-shc",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A 0.20 kg aluminium block at 100 °C (c = 900 J/kg°C) is "
                "dropped into 0.50 kg of water at 20 °C (c = 4200 J/kg°C) in "
                "an insulated cup. The block cools to 30 °C. Calculate the "
                "energy it transfers, and hence the rise in the temperature "
                "of the water.",
        "options": [
            "18 000 J, so the water warms by 8.6 °C",
            "5400 J, so the water warms by 2.6 °C",
            "12 600 J, so the water warms by 3.0 °C",
            "12 600 J, so the water warms by 6.0 °C",
        ],
        "correct_index": 3,
        "why": "The block's Δθ is 100 − 30 = 70 °C, giving 0.20 × 900 × 70 = "
               "12 600 J, and that energy warms the water by 12 600 ÷ (0.50 "
               "× 4200) = 6.0 °C.",
    },
    {
        "id": "ks4-temperature-changes-shc-h03",
        "subtopic_slug": "temperature-changes-shc",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A storage heater holds 60 kg of concrete (c = 800 J/kg°C). "
                "A rival design holds 60 kg of water (c = 4200 J/kg°C). Both "
                "are heated through 40 °C. Calculate how much more energy "
                "the water design stores.",
        "options": [
            "0 MJ",
            "1.92 MJ",
            "8.16 MJ",
            "10.08 MJ",
        ],
        "correct_index": 2,
        "why": "The water stores 60 × 4200 × 40 = 10.08 MJ and the concrete "
               "60 × 800 × 40 = 1.92 MJ, so the water stores 8.16 MJ more.",
    },
    {
        "id": "ks4-temperature-changes-shc-h04",
        "subtopic_slug": "temperature-changes-shc",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "An electric shower transfers 84 kJ of energy to the water "
                "flowing through it every 10 s. The water enters at 15 °C "
                "and leaves at 35 °C. Determine the mass of water heated "
                "every 10 s. The specific heat capacity of water is "
                "4200 J/kg°C.",
        "options": [
            "0.57 kg",
            "0.0010 kg",
            "1.3 kg",
            "1.0 kg",
        ],
        "correct_index": 3,
        "why": "84 kJ is 84 000 J and Δθ is 35 − 15 = 20 °C, so m = 84 000 ÷ "
               "(4200 × 20) = 1.0 kg.",
    },

    # ── specific-latent-heat ────────────────────────────────────────────
    {
        "id": "ks4-specific-latent-heat-e01",
        "subtopic_slug": "specific-latent-heat",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what is meant by the specific latent heat of fusion "
                "of a substance.",
        "options": [
            "The energy needed to raise the temperature of 1 kg of the solid "
            "by 1 °C",
            "The energy needed to change 1 kg of the liquid into a gas at "
            "its boiling point",
            "The energy needed to heat the solid from room temperature up to "
            "its melting point",
            "The energy needed to change 1 kg of the solid into a liquid "
            "with no change in temperature",
        ],
        "correct_index": 3,
        "why": "Fusion is melting, and the latent heat is the energy per "
               "kilogram to make that change happen at constant temperature.",
    },
    {
        "id": "ks4-specific-latent-heat-e02",
        "subtopic_slug": "specific-latent-heat",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the unit of specific latent heat.",
        "options": [
            "J/kg",
            "J/kg°C",
            "J",
            "°C/kg",
        ],
        "correct_index": 0,
        "why": "Specific latent heat is energy per kilogram with no "
               "temperature change involved, so its unit is J/kg.",
    },
    {
        "id": "ks4-specific-latent-heat-e03",
        "subtopic_slug": "specific-latent-heat",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Calculate the energy needed to melt 3.0 kg of ice that "
                "is already at 0 °C. The specific latent heat of fusion "
                "of water is 334 000 J/kg.",
        "options": [
            "334 000 J",
            "111 000 J",
            "1 002 000 J",
            "6 780 000 J",
        ],
        "correct_index": 2,
        "why": "E = mL = 3.0 × 334 000 = 1 002 000 J — the mass "
               "multiplies the latent heat, and melting uses the latent "
               "heat of fusion, not of vaporisation.",
    },
    {
        "id": "ks4-specific-latent-heat-e04",
        "subtopic_slug": "specific-latent-heat",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Which change requires the specific latent heat of "
                "vaporisation?",
        "options": [
            "Ice melting into liquid water at 0 °C",
            "Water boiling into steam at 100 °C",
            "Liquid water freezing into ice at 0 °C",
            "Water cooling from 100 °C down to 20 °C",
        ],
        "correct_index": 1,
        "why": "Vaporisation is the liquid-to-gas change, so boiling is the "
               "change that needs the latent heat of vaporisation.",
    },
    {
        "id": "ks4-specific-latent-heat-s01",
        "subtopic_slug": "specific-latent-heat",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Ethanol has a specific latent heat of vaporisation of "
                "840 000 J/kg. Calculate the energy needed to boil away "
                "0.50 kg of ethanol that is already at its boiling point.",
        "options": [
            "1 680 000 J",
            "420 000 J",
            "840 000 J",
            "0 J",
        ],
        "correct_index": 1,
        "why": "E = mL = 0.50 × 840 000 = 420 000 J; energy is still needed "
               "even though the temperature does not change.",
    },
    {
        "id": "ks4-specific-latent-heat-s02",
        "subtopic_slug": "specific-latent-heat",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A freezer removes 167 000 J of energy from water that is "
                "already at 0 °C. Calculate the mass of ice formed. The "
                "specific latent heat of fusion of water is 334 000 J/kg.",
        "options": [
            "2.0 kg",
            "0.074 kg",
            "0.50 kg",
            "0.050 kg",
        ],
        "correct_index": 2,
        "why": "Rearranging E = mL gives m = E ÷ L = 167 000 ÷ 334 000 = "
               "0.50 kg.",
    },
    {
        "id": "ks4-specific-latent-heat-s03",
        "subtopic_slug": "specific-latent-heat",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A 0.40 kg block of a pure solid is melted completely by "
                "52 000 J of energy at its melting point. Determine the "
                "specific latent heat of fusion of the solid.",
        "options": [
            "130 000 J/kg",
            "20 800 J/kg",
            "52 000 J/kg",
            "130 J/kg",
        ],
        "correct_index": 0,
        "why": "Rearranging E = mL gives L = E ÷ m = 52 000 ÷ 0.40 = "
               "130 000 J/kg.",
    },
    {
        "id": "ks4-specific-latent-heat-s04",
        "subtopic_slug": "specific-latent-heat",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A beaker of water already at 100 °C is boiled dry by a "
                "heater. Explain which equation should be used to calculate "
                "the energy the heater must supply.",
        "options": [
            "ΔE = mcΔθ, because the heater is transferring thermal energy to "
            "the water",
            "ΔE = mcΔθ and E = mL added together, because boiling always "
            "involves both",
            "ΔE = mcΔθ and E = mL multiplied together, because both apply at "
            "the boiling point",
            "E = mL, because the temperature stays at 100 °C while the state "
            "changes",
        ],
        "correct_index": 3,
        "why": "ΔE = mcΔθ needs a temperature change, and there is none "
               "here — the energy is all going into changing state, so "
               "E = mL is the right equation.",
    },
    {
        "id": "ks4-specific-latent-heat-h01",
        "subtopic_slug": "specific-latent-heat",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Calculate the total energy needed to change 0.50 kg of ice "
                "at 0 °C into water at 40 °C. The specific latent heat of "
                "fusion of water is 334 000 J/kg and the specific heat "
                "capacity of water is 4200 J/kg°C.",
        "options": [
            "251 000 J",
            "167 000 J",
            "84 000 J",
            "418 000 J",
        ],
        "correct_index": 0,
        "why": "The ice must melt (0.50 × 334 000 = 167 000 J) and then the "
               "water must be heated (0.50 × 4200 × 40 = 84 000 J), giving "
               "251 000 J in total.",
    },
    {
        "id": "ks4-specific-latent-heat-h02",
        "subtopic_slug": "specific-latent-heat",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student says that 50 g of ice at 0 °C and 50 g of "
                "water at 0 °C will cool a drink by the same amount, "
                "'because they start at the same temperature'. Evaluate "
                "this statement.",
        "options": [
            "Correct — the cooling depends only on the temperature of "
            "what is added to the drink",
            "Correct — each takes in the same energy as it warms up to "
            "the temperature of the drink",
            "Wrong — the water cools the drink more, because a liquid "
            "mixes with the drink and a solid cannot",
            "Wrong — the ice cools the drink far more, because it must "
            "take in the latent heat of fusion to melt before it warms "
            "at all",
        ],
        "correct_index": 3,
        "why": "Melting 50 g of ice takes 0.050 × 334 000 = 16 700 J "
               "out of the drink before the melted water even begins to "
               "warm up.",
    },
    {
        "id": "ks4-specific-latent-heat-h03",
        "subtopic_slug": "specific-latent-heat",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A kettle transfers energy to water at a rate of 2000 W. "
                "Calculate the time it takes to boil away 0.10 kg of water "
                "that is already at 100 °C. The specific latent heat of "
                "vaporisation of water is 2 260 000 J/kg.",
        "options": [
            "1130 s",
            "113 s",
            "11.3 s",
            "0.0088 s",
        ],
        "correct_index": 1,
        "why": "E = mL = 0.10 × 2 260 000 = 226 000 J, and t = E ÷ P = "
               "226 000 ÷ 2000 = 113 s.",
    },
    {
        "id": "ks4-specific-latent-heat-h04",
        "subtopic_slug": "specific-latent-heat",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "The specific latent heat of vaporisation of water is "
                "2 260 000 J/kg, but its specific latent heat of fusion is "
                "only 334 000 J/kg. Explain why vaporisation needs so much "
                "more energy.",
        "options": [
            "Because the boiling point is at a much higher temperature, and "
            "more energy is always needed at a higher temperature",
            "Because 1 kg of steam contains more particles than 1 kg of "
            "liquid water at the same temperature",
            "Because boiling must separate the particles completely, while "
            "melting only frees them from their fixed lattice positions",
            "Because the gas has a far greater specific heat capacity than "
            "either the liquid or the solid",
        ],
        "correct_index": 2,
        "why": "Melting leaves the particles close together, so only some of "
               "the intermolecular forces are overcome; boiling must "
               "overcome them all.",
    },

    # ── particle-motion-pressure ────────────────────────────────────────
    {
        "id": "ks4-particle-motion-pressure-e01",
        "subtopic_slug": "particle-motion-pressure",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what causes the pressure a gas exerts on the walls of "
                "its container.",
        "options": [
            "The weight of the gas pressing down on the container",
            "The gas molecules pushing each other apart inside the container",
            "The collisions of the gas molecules with the walls",
            "The temperature of the gas pressing outwards on the walls",
        ],
        "correct_index": 2,
        "why": "Each molecule that bounces off a wall exerts a tiny force, "
               "and billions of such collisions every second add up to the "
               "measured pressure.",
    },
    {
        "id": "ks4-particle-motion-pressure-e02",
        "subtopic_slug": "particle-motion-pressure",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Convert a temperature of 50 °C into kelvin.",
        "options": [
            "50 K",
            "223 K",
            "273 K",
            "323 K",
        ],
        "correct_index": 3,
        "why": "The kelvin scale is shifted by 273, so T (K) = T (°C) + 273 = "
               "50 + 273 = 323 K.",
    },
    {
        "id": "ks4-particle-motion-pressure-e03",
        "subtopic_slug": "particle-motion-pressure",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the temperature of absolute zero in degrees Celsius.",
        "options": [
            "−273 °C",
            "0 °C",
            "273 °C",
            "−100 °C",
        ],
        "correct_index": 0,
        "why": "Absolute zero is 0 K, and since T (K) = T (°C) + 273 this is "
               "−273 °C, where the particles have the least possible energy.",
    },
    {
        "id": "ks4-particle-motion-pressure-e04",
        "subtopic_slug": "particle-motion-pressure",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Describe the motion of the molecules in a gas.",
        "options": [
            "They vibrate about fixed positions and cannot travel through "
            "the container",
            "They move constantly and randomly in all directions at high "
            "speeds",
            "They all travel in straight lines in the same direction until "
            "they hit a wall",
            "They stay still until the gas is heated, and then begin to move",
        ],
        "correct_index": 1,
        "why": "Gas molecules are in constant random motion in every "
               "direction, which is why a gas fills any container it is put "
               "into.",
    },
    {
        "id": "ks4-particle-motion-pressure-s01",
        "subtopic_slug": "particle-motion-pressure",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A gas is cooled until its temperature is 173 K. Determine "
                "this temperature in degrees Celsius.",
        "options": [
            "−100 °C",
            "446 °C",
            "173 °C",
            "100 °C",
        ],
        "correct_index": 0,
        "why": "Rearranging T (K) = T (°C) + 273 gives T (°C) = 173 − 273 = "
               "−100 °C.",
    },
    {
        "id": "ks4-particle-motion-pressure-s02",
        "subtopic_slug": "particle-motion-pressure",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A fixed mass of gas is squeezed into half its original "
                "volume, at constant temperature. Explain what happens to "
                "its pressure.",
        "options": [
            "It halves, because there is less room for the molecules to "
            "spread out in",
            "It stays the same, because the number of molecules in the "
            "container has not changed",
            "It doubles, because the molecules are forced to move faster when "
            "they are squeezed into a much smaller space",
            "It doubles, because the molecules travel less far between "
            "collisions, so they hit the walls more often",
        ],
        "correct_index": 3,
        "why": "At constant temperature the molecules keep the same average "
               "speed; halving the volume simply makes their collisions with "
               "the walls twice as frequent.",
    },
    {
        "id": "ks4-particle-motion-pressure-s03",
        "subtopic_slug": "particle-motion-pressure",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A fixed mass of gas has a volume of 0.80 m³ at a "
                "pressure of 150 kPa. Calculate its pressure when it is "
                "compressed to 0.30 m³ at constant temperature.",
        "options": [
            "150 kPa",
            "56 kPa",
            "400 kPa",
            "120 kPa",
        ],
        "correct_index": 2,
        "why": "At constant temperature p × V stays constant, so 150 × "
               "0.80 = p × 0.30, giving p = 120 ÷ 0.30 = 400 kPa.",
    },
    {
        "id": "ks4-particle-motion-pressure-s04",
        "subtopic_slug": "particle-motion-pressure",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A sealed rigid metal can of gas is placed in a freezer. "
                "Explain why the pressure inside it falls.",
        "options": [
            "The gas molecules shrink as they cool, so they take up less room "
            "inside the can",
            "The molecules lose kinetic energy and move more slowly, so they "
            "hit the walls less often and less hard",
            "Some of the gas molecules are destroyed by the extreme cold, so "
            "far fewer of them are left to hit the walls",
            "The can contracts in the cold, and a smaller volume always means "
            "a lower pressure",
        ],
        "correct_index": 1,
        "why": "Lower temperature means lower average kinetic energy, so the "
               "collisions with the walls are both less frequent and less "
               "forceful.",
    },
    {
        "id": "ks4-particle-motion-pressure-h01",
        "subtopic_slug": "particle-motion-pressure",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A rigid sealed cylinder holds gas at 127 °C and a pressure "
                "of 240 kPa. Calculate the pressure after the gas has cooled "
                "to 27 °C, the volume staying constant.",
        "options": [
            "51 kPa",
            "180 kPa",
            "320 kPa",
            "240 kPa",
        ],
        "correct_index": 1,
        "why": "The temperatures must be in kelvin: 400 K cooling to 300 K, "
               "so the pressure falls in the same ratio, 240 × 300 ÷ 400 = "
               "180 kPa.",
    },
    {
        "id": "ks4-particle-motion-pressure-h02",
        "subtopic_slug": "particle-motion-pressure",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why the kelvin scale, and not the Celsius scale, "
                "must be used when relating the pressure of a gas to its "
                "temperature.",
        "options": [
            "Because pressure is proportional to the absolute temperature, "
            "and only the kelvin scale starts at absolute zero",
            "Because the kelvin scale has no negative values anywhere on it, "
            "which makes the arithmetic much simpler to carry out",
            "Because the kelvin is the SI unit, and every answer in physics "
            "must be given in SI units",
            "Because one kelvin is a larger interval than one degree Celsius, "
            "so the numbers come out smaller",
        ],
        "correct_index": 0,
        "why": "Pressure falls to zero only when particle motion stops, at "
               "0 K, so proportionality holds only on a scale that starts "
               "there.",
    },
    {
        "id": "ks4-particle-motion-pressure-h03",
        "subtopic_slug": "particle-motion-pressure",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "The air in a bicycle pump is compressed slowly to a quarter "
                "of its original volume with the outlet blocked, at constant "
                "temperature. Predict what happens to the pressure and to "
                "the average kinetic energy of the molecules.",
        "options": [
            "The pressure falls to a quarter, and the average kinetic energy "
            "is unchanged",
            "The pressure rises to four times its value, and the average "
            "kinetic energy also rises",
            "The pressure rises to four times its value, and the average "
            "kinetic energy is unchanged",
            "The pressure rises to four times its value, and the average "
            "kinetic energy falls",
        ],
        "correct_index": 2,
        "why": "p × V stays constant, so quartering the volume quadruples "
               "the pressure — but the temperature is constant, so the "
               "molecules' average kinetic energy does not change.",
    },
    {
        "id": "ks4-particle-motion-pressure-h04",
        "subtopic_slug": "particle-motion-pressure",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student writes: 'Heating a gas in a sealed rigid can from "
                "20 °C to 40 °C doubles the Celsius temperature, so it "
                "doubles the pressure.' Evaluate this statement.",
        "options": [
            "It is correct — at constant volume the pressure is proportional "
            "to the temperature on any scale",
            "It is wrong — at constant volume the pressure of a gas does not "
            "depend on its temperature at all",
            "It is wrong — doubling the temperature halves the pressure, "
            "because the molecules spread further apart",
            "It is wrong — pressure follows the kelvin temperature, and "
            "293 K to 313 K is a rise of only about 7%",
        ],
        "correct_index": 3,
        "why": "Pressure is proportional to the absolute temperature, and in "
               "kelvin the change from 293 K to 313 K is small, so the "
               "pressure rises only slightly.",
    },
]
