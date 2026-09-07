"""Physics · Waves — the MRB-335 extension.

Only Combined Higher was short here (48 on the 7 Sep table); Combined
Foundation stood at 72 and both Triple cells were comfortable, because four
of this topic's twelve subtopics are Triple-only Higher and feed Triple
Higher generously. So the whole of this file is `standard` and `harder`
rows in the six BASE subtopics — the only rows that reach the Combined
Higher cell — and it adds no `easier` questions at all.

⚠️ No question here needs a figure, and that constraint bites harder in
waves than anywhere else in the KS4 pool: refraction, ray diagrams and
oscilloscope traces are all normally SHOWN. Every angle, every trace and
every boundary below is described in words instead — 'a ray meets the water
surface at 40° to the normal', not 'the ray shown'.
"""

TOPIC = "waves"
SUBJECT = "physics"

QUESTIONS = [
    # ── transverse-longitudinal-waves ─────────── BASE (6.6.1.1) ── +2 ──
    {
        "id": "ks4-transverse-longitudinal-waves-s05",
        "subtopic_slug": "transverse-longitudinal-waves",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare the direction of the oscillations with the "
                "direction of energy transfer for a transverse wave and for "
                "a longitudinal wave.",
        "options": [
            "In both, the oscillations are at right angles to the energy "
            "transfer",
            "Transverse: the oscillations are at right angles to the energy "
            "transfer; longitudinal: they are along the same direction",
            "In both, the oscillations are along the direction of energy "
            "transfer",
            "Transverse: the oscillations are along the direction of energy "
            "transfer; longitudinal: they are at right angles",
        ],
        "correct_index": 1,
        "why": "The two types are defined by that relationship: transverse "
               "oscillates across the direction of travel, longitudinal "
               "along it.",
    },
    {
        "id": "ks4-transverse-longitudinal-waves-h05",
        "subtopic_slug": "transverse-longitudinal-waves",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Sound cannot travel through a vacuum but light can. "
                "Explain this difference in terms of the two types of wave.",
        "options": [
            "Sound is transverse and cannot bend around a vacuum",
            "Light travels faster, so it crosses a vacuum before it can be "
            "absorbed",
            "Sound needs air pressure to push it along, and a vacuum has no "
            "pressure at all",
            "Sound is longitudinal and needs particles; light is "
            "electromagnetic and needs no medium",
        ],
        "correct_index": 3,
        "why": "A sound wave IS a pattern of particle movement, so with no "
               "particles there is nothing to carry it; light is a "
               "disturbance in fields, which exist in empty space.",
    },

    # ── properties-of-waves ───────────────────── BASE (6.6.1.2) ── +5 ──
    {
        "id": "ks4-properties-of-waves-e05",
        "subtopic_slug": "properties-of-waves",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the equation linking wave speed, frequency and "
                "wavelength.",
        "options": [
            "v = f ÷ λ",
            "v = λ ÷ f",
            "v = f λ",
            "f = v λ",
        ],
        "correct_index": 2,
        "why": "Speed is how many waves pass each second multiplied by the "
               "length of each one, so v = f λ.",
    },
    {
        "id": "ks4-properties-of-waves-s05",
        "subtopic_slug": "properties-of-waves",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A wave of frequency 250 Hz travels through water at "
                "1500 m/s. Calculate its wavelength.",
        "options": [
            "6.0 m",
            "0.17 m",
            "1250 m",
            "375 000 m",
        ],
        "correct_index": 0,
        "why": "Rearranging v = f λ gives λ = 1500 ÷ 250 = 6.0 m.",
    },
    {
        "id": "ks4-properties-of-waves-s06",
        "subtopic_slug": "properties-of-waves",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why the frequency of a wave is unchanged when it "
                "passes from one material into another.",
        "options": [
            "The source decides how many waves are made each second, and no "
            "material changes that",
            "The wavelength always adjusts so as to keep the speed the same",
            "Frequency depends only on the amplitude, and the amplitude "
            "does not change",
            "The frequency does change, but by too little to measure",
        ],
        "correct_index": 0,
        "why": "Waves arrive at the boundary at the same rate as they were "
               "produced, and they must leave it at that same rate, so f is "
               "fixed and v and λ change together.",
    },
    {
        "id": "ks4-properties-of-waves-h05",
        "subtopic_slug": "properties-of-waves",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A wave has a period of 0.020 s and a wavelength of 1.6 m. "
                "Determine its speed.",
        "options": [
            "0.032 m/s",
            "32 m/s",
            "80 m/s",
            "0.013 m/s",
        ],
        "correct_index": 2,
        "why": "Frequency is 1 ÷ 0.020 = 50 Hz, so v = f λ = 50 × 1.6 = "
               "80 m/s.",
    },
    {
        "id": "ks4-properties-of-waves-h06",
        "subtopic_slug": "properties-of-waves",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "The frequency of a wave on a rope is doubled while the "
                "tension, and so the wave speed, stays the same. Predict the "
                "effect on the wavelength and on the period.",
        "options": [
            "The wavelength doubles and the period halves",
            "The wavelength halves and the period doubles",
            "Both are unchanged, because the speed did not change",
            "The wavelength halves and the period halves",
        ],
        "correct_index": 3,
        "why": "With v fixed, λ = v ÷ f halves when f doubles, and the "
               "period is 1 ÷ f, which also halves.",
    },

    # ── types-of-em-waves ─────────────────────── BASE (6.6.2.1) ── +2 ──
    {
        "id": "ks4-types-of-em-waves-s05",
        "subtopic_slug": "types-of-em-waves",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the seven groups of the electromagnetic spectrum in "
                "order, from the longest wavelength to the shortest.",
        "options": [
            "Gamma, X-ray, ultraviolet, visible, infrared, microwave, radio",
            "Radio, microwave, infrared, visible, ultraviolet, X-ray, gamma",
            "Radio, infrared, microwave, visible, X-ray, ultraviolet, gamma",
            "Microwave, radio, infrared, visible, ultraviolet, gamma, X-ray",
        ],
        "correct_index": 1,
        "why": "Wavelength falls and frequency rises across the spectrum in "
               "that order, with visible light sitting between infrared and "
               "ultraviolet.",
    },
    {
        "id": "ks4-types-of-em-waves-h05",
        "subtopic_slug": "types-of-em-waves",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A microwave has a wavelength of 0.12 m. Calculate its "
                "frequency in a vacuum and state how its speed compares with "
                "that of a gamma ray. The speed of electromagnetic waves in "
                "a vacuum is 3.0 × 10⁸ m/s.",
        "options": [
            "2.5 × 10⁹ Hz, and the gamma ray travels faster",
            "3.6 × 10⁷ Hz, and both travel at the same speed",
            "2.5 × 10⁹ Hz, and both travel at the same speed in a vacuum",
            "2.5 × 10⁷ Hz, and the gamma ray travels faster",
        ],
        "correct_index": 2,
        "why": "f = v ÷ λ = 3.0 × 10⁸ ÷ 0.12 = 2.5 × 10⁹ Hz, and every "
               "electromagnetic wave travels at the same speed in a vacuum.",
    },

    # ── properties-em-waves-1 ─────────────────── BASE (6.6.2.2) ── +3 ──
    {
        "id": "ks4-properties-em-waves-1-s05",
        "subtopic_slug": "properties-em-waves-1",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a straw standing in a glass of water looks bent "
                "at the water surface.",
        "options": [
            "Light from the submerged part refracts at the surface, so it "
            "reaches the eye from a new direction",
            "The water pushes the straw sideways where it enters the "
            "surface",
            "The water absorbs some of the light, which shortens the image "
            "of the straw",
            "The straw really does bend, because water is much denser than "
            "the air above it",
        ],
        "correct_index": 0,
        "why": "The eye assumes light travelled in a straight line, so a ray "
               "that changed direction at the surface makes the straw appear "
               "displaced.",
    },
    {
        "id": "ks4-properties-em-waves-1-s06",
        "subtopic_slug": "properties-em-waves-1",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Radio waves are sent towards a distant hillside and some "
                "are reflected back. State the relationship between the "
                "angle of incidence and the angle of reflection.",
        "options": [
            "The angle of reflection is always the larger of the two",
            "They are equal, both measured from the surface itself",
            "They are equal, both measured from the normal",
            "The angle of reflection is always the smaller of the two",
        ],
        "correct_index": 2,
        "why": "Reflection is symmetrical about the normal, and both angles "
               "in the law of reflection are measured from the normal, not "
               "from the surface.",
    },
    {
        "id": "ks4-properties-em-waves-1-h05",
        "subtopic_slug": "properties-em-waves-1",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Light travels at 3.0 × 10⁸ m/s in air and 2.2 × 10⁸ m/s in "
                "water. A ray meets a water surface at 40° to the normal. "
                "Predict the angle of refraction and what happens to the "
                "wavelength, with reasons.",
        "options": [
            "Greater than 40°, and the wavelength increases, because the "
            "light slows down",
            "Less than 40°, and the wavelength increases, because the "
            "frequency falls",
            "Greater than 40°, and the wavelength decreases, because the "
            "light speeds up",
            "Less than 40°, and the wavelength decreases, because the light "
            "slows down on entering the water",
        ],
        "correct_index": 3,
        "why": "Slowing down bends a ray TOWARDS the normal, and since the "
               "frequency is fixed, a lower speed means a shorter "
               "wavelength.",
    },

    # ── properties-em-waves-2 ─────────────────── BASE (6.6.2.3) ── +3 ──
    {
        "id": "ks4-properties-em-waves-2-s05",
        "subtopic_slug": "properties-em-waves-2",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why ultraviolet radiation can cause skin cancer "
                "but infrared radiation cannot.",
        "options": [
            "Ultraviolet is ionising and can damage the DNA in cells; "
            "infrared is not and only heats tissue",
            "Ultraviolet penetrates far deeper into the body than infrared "
            "does",
            "Infrared is absorbed by the skin, while ultraviolet passes "
            "straight through it",
            "Ultraviolet travels faster than infrared and so strikes cells "
            "harder",
        ],
        "correct_index": 0,
        "why": "Cancer follows from damage to DNA, and only radiation "
               "energetic enough to ionise can do that damage.",
    },
    {
        "id": "ks4-properties-em-waves-2-h05",
        "subtopic_slug": "properties-em-waves-2",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Two materials are placed in front of the same source. "
                "Material P heats up strongly; material Q does not change "
                "temperature and the radiation continues past it. Deduce "
                "what each material does and what happens to the energy.",
        "options": [
            "P transmits and Q absorbs, so the energy stays inside Q",
            "P absorbs the radiation and gains its energy; Q transmits it, "
            "so the energy carries on past",
            "Both reflect the radiation, so no energy is transferred at all",
            "P reflects and Q absorbs, so the energy is shared between the "
            "two materials",
        ],
        "correct_index": 1,
        "why": "A material that warms has absorbed the energy; one that lets "
               "the radiation through unchanged has transmitted it, keeping "
               "none.",
    },
    {
        "id": "ks4-properties-em-waves-2-h06",
        "subtopic_slug": "properties-em-waves-2",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why the risk from an electromagnetic radiation "
                "depends on the type of radiation AND on the dose received.",
        "options": [
            "The risk depends only on which part of the electromagnetic "
            "spectrum the radiation comes from",
            "The risk depends only on how long the exposure lasted",
            "Only ionising radiation carries any risk at all, whatever the "
            "dose",
            "A more ionising radiation damages more per unit energy, but a "
            "small dose can be safer than a large one",
        ],
        "correct_index": 3,
        "why": "Hazard is a property of the radiation and dose is a property "
               "of the exposure; the harm done depends on both together.",
    },

    # ── uses-em-waves ─────────────────────────── BASE (6.6.2.4) ── +2 ──
    {
        "id": "ks4-uses-em-waves-s05",
        "subtopic_slug": "uses-em-waves",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why microwaves rather than visible light are used "
                "to send signals to and from a satellite.",
        "options": [
            "Microwaves pass through cloud with little absorption; visible "
            "light is scattered and blocked",
            "Microwaves travel faster than visible light does through the "
            "atmosphere",
            "Microwaves are the only waves that a satellite's aerial does "
            "not absorb",
            "Visible light cannot travel through the vacuum of space",
        ],
        "correct_index": 0,
        "why": "A communication link has to work in all weather, and the "
               "atmosphere is far more transparent to microwaves than to "
               "visible light.",
    },
    {
        "id": "ks4-uses-em-waves-h05",
        "subtopic_slug": "uses-em-waves",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A radar pulse returns from an aircraft 0.00040 s after it "
                "was sent. The pulse travels at 3.0 × 10⁸ m/s. Calculate the "
                "distance to the aircraft.",
        "options": [
            "120 km",
            "60 km",
            "30 km",
            "1200 km",
        ],
        "correct_index": 1,
        "why": "The pulse covers 3.0 × 10⁸ × 0.00040 = 120 000 m, but that "
               "is there AND back, so the aircraft is 60 km away.",
    },
]
