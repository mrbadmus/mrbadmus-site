# -*- coding: utf-8 -*-
"""Colour and the spectrum, in the lean shape. Also teaches Rainford 24b (the
electromagnetic spectrum), which has no page of its own.
Spec table: docs/lessons/wave2/ks3-colour-and-the-spectrum.md."""

LESSON = {
    "slug": "colour-and-the-spectrum",
    "start": {
        "setup": "Sunlight shines through a clear glass prism. A band of colours appears on the wall.",
        "question": "If you had to guess, were the colours already in the sunlight, or did the glass "
                    "add them?",
        "options": [
            ("Already in the sunlight",
             "Right. White light is a mixture of colours. The prism spreads them out."),
            ("Added by the glass",
             "Clear glass has no colour to add. It spreads out the colours already in sunlight."),
        ],
        "answer": 0,
    },
    "words": ["spectrum", "dispersion", "frequency", "electromagnetic spectrum"],
    "word_defs": {
        "spectrum": "The band of colours that white light splits into, from red to violet.",
        "dispersion": "The splitting of white light into colours, because each colour refracts by a different amount.",
        "frequency": "The number of waves passing a point each second. For light, it decides the colour.",
        "electromagnetic spectrum": "The family of waves that light belongs to, from radio waves to gamma rays.",
    },
    "knowledge": [
        {"kind": "card", "title": "White light is a mixture",
         "body": [{"figure": "p7-prism"},
                  "White light, such as sunlight, is a mixture of colours.",
                  "A prism splits white light into a band of colours called a spectrum.",
                  "The colours are red, orange, yellow, green, blue and violet.",
                  "The colours change smoothly from one to the next. There are no lines between them."]},
        {"kind": "card", "title": "Why the colours spread out",
         "body": ["Each colour is light of a different frequency.",
                  "Red light has the lowest frequency. Violet light has the highest.",
                  "All the colours slow down and refract when they go into the glass.",
                  "Higher frequencies refract more. So violet bends the most, and red bends the least.",
                  "The colours fan out. This is dispersion."]},
        {"kind": "card", "title": "The prism adds nothing",
         "body": [{"figure": "p7-prism-two"},
                  "A second prism, the other way up, bends each colour back again.",
                  "The colours join up, and white light comes out.",
                  "So the colours were in the white light all along.",
                  "Send red light alone into a prism, and only red light comes out."]},
        {"kind": "card", "title": "The electromagnetic spectrum",
         "body": ["Visible light is one small part of a family of waves.",
                  "This family is called the electromagnetic spectrum.",
                  "All of these waves are transverse, and all can travel through a vacuum.",
                  "In a vacuum, they all travel at the same speed, 300 000 000 m/s.",
                  "They differ in frequency. Higher frequency waves have shorter wavelengths.",
                  "In order of frequency, lowest first:",
                  {"points": ["radio waves", "microwaves", "infrared", "visible light",
                              "ultraviolet", "X-rays", "gamma rays"]}]},
        {"kind": "reveal", "title": "Uses and dangers",
         "cols": ["A use", "A danger"],
         "rows": [
             ("Radio waves", "TV and radio broadcasts", "Little harm at normal levels"),
             ("Microwaves", "Cooking food, and mobile phones", "Can heat body tissue"),
             ("Infrared", "Heaters and TV remote controls", "Can burn the skin"),
             ("Visible light", "Seeing, and taking photos", "Very bright light can harm the eyes"),
             ("Ultraviolet", "Spotting fake banknotes", "Sunburn and skin cancer"),
             ("X-rays", "Seeing broken bones", "Can damage cells and cause cancer"),
             ("Gamma rays", "Killing cancer cells", "Can damage cells and cause cancer"),
         ]},
        {"kind": "card", "title": "Easy mistakes",
         "body": [{"mistakes": [
             ("The prism adds the colours to the light.",
              "The colours were already in the white light. The prism separates them.", "LIGHT-21"),
             ("A rainbow is six separate colours, with lines between them.",
              "The colours change smoothly. The six names are labels along one band.", "LIGHT-22"),
             ("High frequency light is bent the least.",
              "High frequency light is bent the most. Violet bends more than red.", "LIGHT-23"),
             ("The colours come from the coloured edges of the prism.",
              "The prism is clear glass. The colours come from the white light.", "LIGHT-24"),
             ("X-rays travel faster than radio waves.",
              "In a vacuum, every electromagnetic wave travels at the same speed."),
         ]}]},
    ],
    "key_fact": "White light is a mixture of colours, which a prism splits into a spectrum. "
                "Violet has the highest frequency and is refracted most, and red is refracted least.",
    "deeper": [
        {"kind": "card", "title": "A seventh colour",
         "body": ["Some books also name indigo, between blue and violet, as a seventh colour."]},
        {"kind": "card", "title": "Just past each end",
         "body": ["Infrared lies just below red in frequency. You feel it as warmth.",
                  "Ultraviolet lies just above violet. Bees can see it, but people cannot."]},
        {"kind": "card", "title": "Why the dangerous end is dangerous",
         "body": ["Higher frequency electromagnetic waves carry more energy.",
                  "Ultraviolet, X-rays and gamma rays can damage the cells they pass through.",
                  "This is why X-ray staff stand behind a screen."]},
    ],
    "try": None,
    "connects_heading": None,
    "safety_note": "Never look directly at the Sun, with your eyes, through a lens or through a pinhole camera. "
                   "A lens gathers sunlight to a point hot enough to scorch paper. "
                   "It will do the same to the back of your eye. "
                   "The damage does not hurt while it happens, and it does not heal.",
    "ks4_becomes": "The electromagnetic spectrum in full: the properties, uses and dangers of each part.",
    "connects": {
        "Refraction": "Dispersion is refraction by a slightly different amount for each colour.",
        "Hearing and auditory range": "Frequency decides the pitch of a sound and the colour of light.",
        "Waves on water: what a wave is": "Frequency and wavelength mean the same for light as for water waves.",
    },
    "figures": [
        {"id": "p7-prism", "kind": "diagram", "status": "drawn", "art": "p7-prism",
         "title": "White light through a prism",
         "desc": "A ray of white light comes in from the left and enters a triangular glass prism. "
                 "Inside the prism it starts to split. Six coloured rays leave the far side and fan "
                 "out onto a screen. From top to bottom the screen shows red, orange, yellow, green, "
                 "blue and violet, each named in words. Red is bent the least and violet the "
                 "most.",
         "caption": "Red is bent the least. Violet is bent the most.",
         "data": {"colours": ["red", "orange", "yellow", "green", "blue", "violet"],
                  "second": False}},
        {"id": "p7-prism-two", "kind": "diagram", "status": "drawn", "art": "p7-prism",
         "title": "A second prism joins the colours back together",
         "desc": "White light enters a first prism and fans out into colours, from red at the top to "
                 "violet at the bottom. The colours enter a second prism, which is upside down. Inside "
                 "it each colour bends towards the normal, violet the most, so the colours come back "
                 "together. They leave as one ray of white light, going the way the white light first went.",
         "caption": "The second prism puts the colours back into white light.",
         "data": {"colours": ["red", "orange", "yellow", "green", "blue", "violet"],
                  "second": True}},
    ],
    "ladder_feedback": {
        "recall": {
            1: "Violet has the highest frequency, so it is refracted the most.",
            2: "Green lands in the middle of the spectrum. Red is refracted the least.",
            3: "If every colour bent the same amount, there would be no spectrum at all.",
        },
        "apply": {
            0: "Clear glass has no colour to add. A second prism joins the colours back into white.",
            2: "Nothing is turned into a new colour. Red light in gives only red light out.",
            3: "The whole beam spreads into colours. The colours were already in the white light.",
        },
    },
}
