"""Physics · Waves — visible-light (AQA 8463 4.6.2.6, physics only). Drafted 14 Nov 2026.

Twelve rows, authored in bank order: positions 0–3 easier, 4–7 standard, 8–11 harder. Audience
as ks4_data.classify() derives it: first taught in the Triple Foundation block, so tier
"foundation" and triple_only True. 4.6.2.6 has no (HT only) line. No stem leans on a drawing.

The colour model is the GCSE one: an opaque object reflects some wavelengths more strongly and
absorbs the rest; a filter transmits its own colour and absorbs the others; coloured light is
treated as a single colour. The distractors are the classic errors: a filter "adding" colour, an
object keeping its colour in any light, black as a colour that is reflected, and translucent for
transparent.
"""

TOPIC = "waves"
SUBJECT = "physics"

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "ks4-visible-light-e01",
        "subtopic_slug": "visible-light",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State what is meant by specular reflection.",
        "options": [
            "Scattering of light from a rough surface",
            "Light passing straight through clear glass",
            "Reflection one way from a smooth surface",
            "Light being absorbed by a dark, matt surface",
        ],
        "correct_index": 2,
        "why": "Reflection from a smooth surface in a single direction is called specular "
               "reflection. Scattering from a rough surface is diffuse reflection.",
    },
    {
        "id": "ks4-visible-light-e02",
        "subtopic_slug": "visible-light",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State why an opaque object looks black in white light.",
        "options": [
            "It absorbs all wavelengths of light",
            "It reflects only black light",
            "It reflects all wavelengths equally",
            "It transmits all of the light through it",
        ],
        "correct_index": 0,
        "why": "If all wavelengths are absorbed, no light is reflected from the object, so it "
               "appears black. Reflecting all wavelengths equally makes an object white.",
    },
    {
        "id": "ks4-visible-light-e03",
        "subtopic_slug": "visible-light",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State what a red filter does to white light.",
        "options": [
            "It adds red to the white light",
            "It absorbs red and transmits the rest",
            "It reflects all of the colours back",
            "It transmits red and absorbs the rest",
        ],
        "correct_index": 3,
        "why": "A colour filter transmits its own colour and absorbs the other wavelengths. It "
               "cannot add colour.",
    },
    {
        "id": "ks4-visible-light-e04",
        "subtopic_slug": "visible-light",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Name the word for a material that lets light through but scatters it, so you "
                "cannot see a clear image through it.",
        "options": [
            "Transparent",
            "Translucent",
            "Opaque",
            "Specular",
        ],
        "correct_index": 1,
        "why": "Objects that transmit light are transparent or translucent. A translucent one, "
               "such as frosted glass, scatters the light. A transparent one does not.",
    },
    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "ks4-visible-light-s01",
        "subtopic_slug": "visible-light",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "A green apple is lit by white light. Explain why it looks green.",
        "options": [
            "It reflects green light most strongly and absorbs the others",
            "It absorbs green light and reflects all the other colours",
            "It gives out green light of its own when light falls on it",
            "It transmits green light and reflects the other colours",
        ],
        "correct_index": 0,
        "why": "The colour of an opaque object is the wavelengths it reflects most strongly. The "
               "apple reflects green and absorbs the other colours, so green light reaches your "
               "eye.",
    },
    {
        "id": "ks4-visible-light-s02",
        "subtopic_slug": "visible-light",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "A white T-shirt is lit by red light only. Identify the colour it appears.",
        "options": [
            "White",
            "Black",
            "Red",
            "Pink",
        ],
        "correct_index": 2,
        "why": "A white object reflects all wavelengths equally, but only red light reaches it, so "
               "it reflects red and looks red.",
    },
    {
        "id": "ks4-visible-light-s03",
        "subtopic_slug": "visible-light",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why you can see your face in a mirror but not in a sheet of white paper.",
        "options": [
            "The paper absorbs all of the light that falls on it",
            "The paper transmits all of the light that falls on it",
            "The mirror makes light, but the paper does not",
            "The mirror is smooth and the paper is rough",
        ],
        "correct_index": 3,
        "why": "A smooth mirror reflects light in a single direction (specular reflection), so it "
               "forms a clear image. Rough paper scatters the light (diffuse reflection), so no "
               "image forms.",
    },
    {
        "id": "ks4-visible-light-s04",
        "subtopic_slug": "visible-light",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Green light is shone at a red filter. Describe what happens to the light.",
        "options": [
            "It passes through and comes out green",
            "It is absorbed, so no light gets through",
            "The filter changes it into red light",
            "It passes through and comes out yellow",
        ],
        "correct_index": 1,
        "why": "A red filter transmits only red light and absorbs the other colours, so it absorbs "
               "the green light and no light comes through.",
    },
    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "ks4-visible-light-h01",
        "subtopic_slug": "visible-light",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A blue costume is lit by a red spotlight on a dark stage. Explain what colour it "
                "appears.",
        "options": [
            "Blue, because the costume is blue in any light",
            "Purple, because the red and blue light mix together",
            "Red, because it reflects the red light that reaches it",
            "Black, because there is no blue light for it to reflect",
        ],
        "correct_index": 3,
        "why": "The costume reflects blue light and absorbs the other colours. The spotlight gives "
               "only red light, which the costume absorbs, so no light is reflected and it looks "
               "black.",
    },
    {
        "id": "ks4-visible-light-h02",
        "subtopic_slug": "visible-light",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "White light passes through a green filter and then a blue filter. Describe the "
                "light that comes out.",
        "options": [
            "Green light only",
            "Blue light only",
            "No light at all",
            "White light again",
        ],
        "correct_index": 2,
        "why": "The green filter transmits only green light. The blue filter absorbs green light, "
               "so nothing is transmitted by the second filter.",
    },
    {
        "id": "ks4-visible-light-h03",
        "subtopic_slug": "visible-light",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A white flower is looked at through a red filter in white light. Explain what "
                "colour it appears.",
        "options": [
            "Red, as only red light from the flower passes the filter",
            "White, as the flower reflects every wavelength",
            "Black, as the filter absorbs all the light",
            "Green, as the filter takes the red out of the white light",
        ],
        "correct_index": 0,
        "why": "The flower reflects all wavelengths equally. The filter transmits only the red "
               "part of that light and absorbs the rest, so only red light reaches your eye.",
    },
    {
        "id": "ks4-visible-light-h04",
        "subtopic_slug": "visible-light",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Describe how the colours of visible light differ from one another.",
        "options": [
            "Each colour travels at its own speed in a vacuum",
            "Each colour has its own narrow band of wavelength and frequency",
            "Each colour has its own amplitude, with red the largest",
            "Each colour is a different type of wave, and some are longitudinal",
        ],
        "correct_index": 1,
        "why": "Each colour within the visible light spectrum has its own narrow band of "
               "wavelength and frequency. All colours travel at the same speed in a vacuum, and "
               "all are transverse.",
    },
]
