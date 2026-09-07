"""Physics · Particle model — the MRB-335 extension.

All six subtopics of §6.3 are BASE, so Combined and Triple share one pool and
both HIGHER cells sat at 48 on the 7 Sep table while both Foundation cells
were comfortable at 72. That is a band problem rather than a coverage
problem: the Higher cell of a base topic is fed only by `standard` and
`harder`, so this file is fifteen rows of those two bands and two `easier`
ones, spread across all six subtopics.

The two `easier` additions are deliberate and are both the same question in
different clothes — which equation, ΔE = mcΔθ or E = mL. That confusion is
the declared common mistake in two subtopics at once, and a student who
picks the wrong one loses the whole calculation before they start.

Numbers are new throughout. None reuses a mass, a temperature or an answer
from the worked examples the lesson pages print — the 27 °C/327 °C pair in
particular is the page's own, so the pressure question here runs 20 °C to
313 °C instead.
"""

TOPIC = "particle-model"
SUBJECT = "physics"

QUESTIONS = [
    # ── density-of-materials ──────────────────── BASE (6.3.1.1) ── +2 ──
    {
        "id": "ks4-density-of-materials-s05",
        "subtopic_slug": "density-of-materials",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A 1.0 kg block of iron and a 1.0 kg block of wood have very "
                "different volumes. Explain why.",
        "options": [
            "Iron has a much greater density, so the same mass occupies a "
            "much smaller volume",
            "Iron particles are heavier, so 1.0 kg of iron holds fewer of "
            "them and takes up more space",
            "Wood has the greater density, so it takes up less room",
            "Two blocks of equal mass must have equal volumes",
        ],
        "correct_index": 0,
        "why": "Density is mass per unit volume, so for a fixed mass the "
               "denser material is the one that packs into the smaller "
               "space.",
    },
    {
        "id": "ks4-density-of-materials-h05",
        "subtopic_slug": "density-of-materials",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Ice has a density of 917 kg/m³ and liquid water 1000 kg/m³. "
                "Determine what happens to the volume when 1.0 kg of water "
                "freezes, and state one everyday consequence.",
        "options": [
            "The volume decreases, because a solid always takes up less "
            "space, which is why ice cubes sink",
            "The volume is unchanged, because mass is conserved on freezing",
            "The volume increases, because the mass of each particle rises "
            "as the particles slow down",
            "The volume increases, because the same mass now has a lower "
            "density — which is why pipes burst in a frost",
        ],
        "correct_index": 3,
        "why": "Volume is mass divided by density, so a fall in density at "
               "constant mass means the ice takes up more room than the "
               "water did.",
    },

    # ── changes-of-state ──────────────────────── BASE (6.3.1.2) ── +2 ──
    {
        "id": "ks4-changes-of-state-s05",
        "subtopic_slug": "changes-of-state",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Describe what happens to the arrangement, the spacing and "
                "the motion of the particles when a liquid boils.",
        "options": [
            "They become closely packed in a lattice and vibrate about "
            "fixed positions only",
            "They become far more widely spaced, arranged randomly, and "
            "move at high speed in all directions",
            "They stay the same distance apart but move considerably faster",
            "They become more widely spaced but keep a regular arrangement",
        ],
        "correct_index": 1,
        "why": "Boiling separates the particles completely, so a gas has no "
               "arrangement at all and its particles travel freely in every "
               "direction.",
    },
    {
        "id": "ks4-changes-of-state-h05",
        "subtopic_slug": "changes-of-state",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a wet towel dries on a washing line on a cold, "
                "windy day, even though the air is far below 100 °C.",
        "options": [
            "The wind must first warm the towel to 100 °C",
            "The water freezes and then sublimes straight into the air "
            "without melting",
            "Evaporation happens at any temperature, and the wind carries "
            "the escaping molecules away",
            "The wind blows the liquid water off the fibres as droplets",
        ],
        "correct_index": 2,
        "why": "Only the most energetic surface molecules need to escape, "
               "and moving air keeps the space above the towel clear so more "
               "of them can.",
    },

    # ── internal-energy ───────────────────────── BASE (6.3.2.1) ── +2 ──
    {
        "id": "ks4-internal-energy-s05",
        "subtopic_slug": "internal-energy",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A substance is heated at a constant 100 W. Its temperature "
                "rises for 60 s, stays constant for 200 s, then rises again. "
                "Calculate the energy absorbed during the change of state.",
        "options": [
            "6000 J",
            "20 000 J",
            "26 000 J",
            "200 J",
        ],
        "correct_index": 1,
        "why": "The flat section is the change of state, and at 100 W for "
               "200 s the energy transferred is 100 × 200 = 20 000 J.",
    },
    {
        "id": "ks4-internal-energy-h05",
        "subtopic_slug": "internal-energy",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Gas in a sealed cylinder is compressed quickly by a piston "
                "and its temperature rises, although nothing has heated it. "
                "Explain how its internal energy increased.",
        "options": [
            "The gas particles gained mass as they were pushed closer "
            "together by the piston",
            "Energy leaked in from the surroundings through the cylinder "
            "walls",
            "The internal energy did not increase — only the temperature "
            "did",
            "The piston did work on the gas, transferring energy to the "
            "kinetic energy of its molecules",
        ],
        "correct_index": 3,
        "why": "Internal energy can be raised by heating OR by doing work on "
               "a system, and squeezing a gas is doing work on it.",
    },

    # ── temperature-changes-shc ───────────────── BASE (6.3.2.2) ── +4 ──
    {
        "id": "ks4-temperature-changes-shc-e05",
        "subtopic_slug": "temperature-changes-shc",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the equation used to calculate the energy needed to "
                "change the TEMPERATURE of a substance.",
        "options": [
            "E = mL",
            "ρ = m ÷ V",
            "ΔE = mcΔθ",
            "p × V = constant",
        ],
        "correct_index": 2,
        "why": "ΔE = mcΔθ has a temperature term in it, which is what makes "
               "it the equation for a temperature change rather than a "
               "change of state.",
    },
    {
        "id": "ks4-temperature-changes-shc-s05",
        "subtopic_slug": "temperature-changes-shc",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A 3.0 kg block of lead cools from 180 °C to 30 °C. "
                "Calculate the energy released. The specific heat capacity "
                "of lead is 130 J/kg°C.",
        "options": [
            "11 700 J",
            "58 500 J",
            "70 200 J",
            "390 J",
        ],
        "correct_index": 1,
        "why": "Δθ is 180 − 30 = 150 °C, so ΔE = 3.0 × 130 × 150 = 58 500 J.",
    },
    {
        "id": "ks4-temperature-changes-shc-s06",
        "subtopic_slug": "temperature-changes-shc",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A kettle transfers 630 000 J of energy to 1.5 kg of water. "
                "Determine the temperature rise. The specific heat capacity "
                "of water is 4200 J/kg°C.",
        "options": [
            "10 °C",
            "150 °C",
            "420 °C",
            "100 °C",
        ],
        "correct_index": 3,
        "why": "Rearranging ΔE = mcΔθ gives Δθ = 630 000 ÷ (1.5 × 4200) = "
               "100 °C.",
    },
    {
        "id": "ks4-temperature-changes-shc-h05",
        "subtopic_slug": "temperature-changes-shc",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Two identical 200 W heaters run for the same time. One "
                "heats 1.0 kg of water (c = 4200 J/kg°C) and the other 1.0 "
                "kg of oil (c = 2100 J/kg°C). Compare the temperature rises "
                "and explain.",
        "options": [
            "The oil rises twice as far, because it needs half as much "
            "energy per kilogram for each degree",
            "The water rises twice as far, because it can hold more energy",
            "Both rise by the same amount, because the same energy was "
            "supplied to each",
            "The oil rises half as far, because its specific heat capacity "
            "is the lower of the two",
        ],
        "correct_index": 0,
        "why": "With ΔE and m the same, Δθ is inversely proportional to c, "
               "so halving the specific heat capacity doubles the "
               "temperature rise.",
    },

    # ── specific-latent-heat ──────────────────── BASE (6.3.2.3) ── +4 ──
    {
        "id": "ks4-specific-latent-heat-e05",
        "subtopic_slug": "specific-latent-heat",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the equation used to calculate the energy needed for "
                "a CHANGE OF STATE.",
        "options": [
            "ΔE = mcΔθ",
            "E = mL",
            "E = mgh",
            "p = F ÷ A",
        ],
        "correct_index": 1,
        "why": "E = mL has no temperature term, which is right because the "
               "temperature does not change while a substance changes state.",
    },
    {
        "id": "ks4-specific-latent-heat-s05",
        "subtopic_slug": "specific-latent-heat",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Liquid nitrogen has a specific latent heat of vaporisation "
                "of 199 000 J/kg. Calculate the energy needed to boil away "
                "2.5 kg of it that is already at its boiling point.",
        "options": [
            "79 600 J",
            "199 000 J",
            "497 500 J",
            "99 500 J",
        ],
        "correct_index": 2,
        "why": "E = mL = 2.5 × 199 000 = 497 500 J, and no mcΔθ term is "
               "needed because the nitrogen is already at its boiling point.",
    },
    {
        "id": "ks4-specific-latent-heat-s06",
        "subtopic_slug": "specific-latent-heat",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A block of ice at −10 °C is heated until it is water at "
                "20 °C. Describe the calculations needed and the equation "
                "used for each.",
        "options": [
            "E = mL for warming the ice up, and ΔE = mcΔθ for the melting "
            "at 0 °C",
            "ΔE = mcΔθ for all three parts, because the temperature changes "
            "overall on the way",
            "ΔE = mcΔθ to warm the ice to 0 °C and then the water to 20 °C, "
            "with E = mL for the melting at 0 °C",
            "E = mL for all three parts, because the state changes overall",
        ],
        "correct_index": 2,
        "why": "Use ΔE = mcΔθ wherever the temperature is changing and E = "
               "mL wherever the state is changing — this journey has both.",
    },
    {
        "id": "ks4-specific-latent-heat-h05",
        "subtopic_slug": "specific-latent-heat",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A 500 W heater melts ice that is already at 0 °C. Calculate "
                "the mass of ice melted in 5.0 minutes. The specific latent "
                "heat of fusion of water is 334 000 J/kg.",
        "options": [
            "2.2 kg",
            "0.45 kg",
            "4.5 kg",
            "0.0075 kg",
        ],
        "correct_index": 1,
        "why": "The heater supplies 500 × 300 = 150 000 J, and m = E ÷ L = "
               "150 000 ÷ 334 000 = 0.45 kg.",
    },

    # ── particle-motion-pressure ──────────────── BASE (6.3.3.1) ── +3 ──
    {
        "id": "ks4-particle-motion-pressure-s05",
        "subtopic_slug": "particle-motion-pressure",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A sealed rigid can of gas is at 20 °C and a pressure of "
                "150 kPa. Calculate the pressure after it is warmed to "
                "313 °C.",
        "options": [
            "75 kPa",
            "160 kPa",
            "300 kPa",
            "2350 kPa",
        ],
        "correct_index": 2,
        "why": "In kelvin the temperature goes from 293 K to 586 K, exactly "
               "doubling, so at constant volume the pressure doubles to "
               "300 kPa.",
    },
    {
        "id": "ks4-particle-motion-pressure-s06",
        "subtopic_slug": "particle-motion-pressure",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A gas syringe holds 60 cm³ of air at 100 kPa. The plunger "
                "is pushed in until the volume is 25 cm³, at constant "
                "temperature. Calculate the new pressure.",
        "options": [
            "42 kPa",
            "135 kPa",
            "240 kPa",
            "2400 kPa",
        ],
        "correct_index": 2,
        "why": "pV stays constant, so p₂ = 100 × 60 ÷ 25 = 240 kPa.",
    },
    {
        "id": "ks4-particle-motion-pressure-h05",
        "subtopic_slug": "particle-motion-pressure",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Two identical sealed rigid cans hold gas at the same "
                "temperature. Can A contains twice as many molecules as can "
                "B. Compare the pressures and explain in terms of "
                "collisions.",
        "options": [
            "The pressures are equal, because the temperature is the same "
            "in both",
            "B has twice the pressure, because its molecules have more room "
            "to build up speed",
            "A has half the pressure, because its molecules get in one "
            "another's way",
            "A has twice the pressure, because twice as many molecules hit "
            "the walls each second",
        ],
        "correct_index": 3,
        "why": "Pressure comes from the rate of collisions with the walls, "
               "and at the same temperature twice the molecules means twice "
               "the collisions.",
    },
]
