# -*- coding: utf-8 -*-
"""Visible light, in the lean shape. New record, created from nothing (no legacy page, no old
subtopic data). Spec table: ks4-visible-light.md (AQA 8463 4.6.2.6 (physics only), all tiers).
Not on 8464. Routes TF TH.

4.6.2.6 has no (HT only) line, so every card is on both Triple routes. The order of the spectrum
is taught by types-of-em-waves: this page names red and violet only and links there.

The colour model is the GCSE one: an object reflects (or transmits) some wavelengths more
strongly and absorbs the rest; coloured light is treated as a single colour; filters only take
colours away. Beyond the spec words: "white light is a mixture of all the colours" and the
colour-in-coloured-light table (see NEW-LESSONS.md)."""

LESSON = {
    "slug": "visible-light",
    "start": {
        "setup": "A red apple sits on a table in white light.",
        "question": "If you had to guess, why does the apple look red?",
        "options": [
            ("It reflects red and absorbs the rest",
             "It reflects red light most strongly and absorbs the other colours. Only the red "
             "light reaches your eye."),
            ("It gives out red light of its own",
             "It reflects red light most strongly and absorbs the other colours. Only the red "
             "light reaches your eye."),
        ],
        "answer": 0,
    },
    "words": ["specular reflection", "diffuse reflection", "opaque", "colour filter"],
    "knowledge": [
        {"kind": "card", "title": "Colours of light",
         "body": ["Each colour within the visible light spectrum has its own narrow band of "
                  "wavelength and frequency.",
                  "Red light has the longest wavelength and the lowest frequency. Violet light has "
                  "the shortest wavelength and the highest frequency.",
                  "White light is a mixture of all the colours."]},
        {"kind": "card", "title": "Specular and diffuse reflection",
         "body": [{"slot": "fig:specular-diffuse"},
                  "Reflection from a smooth surface in a single direction is called specular "
                  "reflection.",
                  "Reflection from a rough surface causes scattering: this is called diffuse "
                  "reflection.",
                  {"points": [
                      "A mirror gives specular reflection, so you see a clear image in it.",
                      "Paper gives diffuse reflection. You see the paper, but no image in it.",
                      "In both, each part of the light reflects with the angle of reflection "
                      "equal to the angle of incidence. On a rough surface the normal points a "
                      "different way at each point, so the light spreads out.",
                  ]}]},
        {"kind": "card", "title": "The colour of an opaque object",
         "body": ["An opaque object does not let light through.",
                  "The colour of an opaque object is determined by which wavelengths of light are "
                  "more strongly reflected. Wavelengths that are not reflected are absorbed.",
                  {"points": [
                      "If all wavelengths are reflected equally, the object appears white.",
                      "If all wavelengths are absorbed, the object appears black.",
                      "A red object reflects red light most strongly and absorbs the other "
                      "colours.",
                  ]}]},
        {"kind": "reveal", "title": "What colour does it look",
         "cols": ["In white light", "In red light", "In green light"],
         "rows": [
             ("A red object", "Red", "Red", "Black"),
             ("A green object", "Green", "Black", "Green"),
             ("A white object", "White", "Red", "Green"),
             ("A black object", "Black", "Black", "Black"),
         ]},
        {"kind": "card", "title": "Transparent and translucent",
         "body": ["Objects that transmit light are either transparent or translucent.",
                  {"points": [
                      "<strong>Transparent</strong>: light passes through without being "
                      "scattered, so you can see clearly through it. Clear glass is transparent.",
                      "<strong>Translucent</strong>: light passes through but is scattered, so "
                      "you cannot see a clear image. Frosted glass is translucent.",
                  ]},
                  "A coloured transparent object, such as green bottle glass, transmits its own "
                  "colour most strongly and absorbs the others."]},
        {"kind": "card", "title": "Colour filters",
         "body": ["Colour filters work by absorbing certain wavelengths (and colour) and "
                  "transmitting other wavelengths (and colour).",
                  {"points": [
                      "A red filter transmits red light and absorbs the other colours.",
                      "White light through a red filter comes out red.",
                      "Green light meets a red filter: the filter absorbs it, so no light comes "
                      "through.",
                  ]},
                  "Looking through a filter works the same way. Only the filter's own colour "
                  "reaches your eye, so a white object looks the colour of the filter."]},
        {"kind": "reveal", "title": "Through a filter",
         "cols": ["What comes through"],
         "rows": [
             ("White light through a red filter", "Red light"),
             ("Red light through a red filter", "Red light"),
             ("Red light through a green filter", "No light"),
             ("White light through a red filter, then a green filter", "No light"),
         ]},
        {"kind": "card", "title": "Easy mistakes",
         "body": [{"mistakes": [
             ("A red filter turns white light red by adding red to it.",
              "A filter only takes colours away. It absorbs the other colours and transmits red."),
             ("A black object reflects black light.",
              "No light is reflected from it. A black object absorbs all wavelengths."),
             ("Translucent means you can see clearly through it.",
              "That is transparent. A translucent object scatters the light."),
         ]}]},
    ],
    "key_fact": "Each colour of visible light has its own narrow band of wavelength and frequency. "
                "An opaque object's colour is decided by which wavelengths it reflects most "
                "strongly, and it absorbs the rest: white reflects all wavelengths equally, black "
                "absorbs them all. A colour filter transmits some wavelengths and absorbs the "
                "others.",
    "deeper": [
        {"kind": "card", "title": "On the stage",
         "body": ["A blue costume under a red spotlight looks black. There is no blue light in "
                  "the spotlight for it to reflect, and it absorbs the red."]},
        {"kind": "card", "title": "Where visible light sits",
         "body": ["Visible light is one group in the electromagnetic spectrum, between infrared "
                  "and ultraviolet. The spectrum is in the lesson on types of electromagnetic "
                  "waves."]},
        {"kind": "card", "title": "Ray diagrams",
         "body": ["Ray diagrams for reflection, with the angle of incidence equal to the angle of "
                  "reflection, are in the lesson on reflection of waves."]},
        {"kind": "card", "title": "Command words",
         "body": [{"points": [
             "<strong>Explain why an object looks a colour</strong>: say which wavelengths it "
             "reflects or transmits, which it absorbs, and which reach your eye.",
             "<strong>Explain a filter</strong>: say which colour it transmits and which it "
             "absorbs, then what is left.",
         ]}]},
    ],
    "try": None,
    "legacy": None,
    "rungs": {
        "r1": [
            {"kind": "mcq", "command": "Name", "marks": 1,
             "prompt": "Name the type of reflection from a smooth surface in a single direction.",
             "why": "Reflection from a smooth surface in a single direction is specular "
                    "reflection.",
             "options": [
                 {"text": "Diffuse reflection", "correct": False,
                  "reply": "Diffuse reflection is the scattering from a rough surface."},
                 {"text": "Specular reflection", "correct": True},
                 {"text": "Refraction", "correct": False,
                  "reply": "Refraction is a change of direction as light crosses a boundary."},
             ]},
            {"kind": "mcq", "command": "State", "marks": 1,
             "prompt": "State why an opaque object looks white in white light.",
             "why": "If all wavelengths are reflected equally, the object appears white.",
             "options": [
                 {"text": "It absorbs all the wavelengths equally", "correct": False,
                  "reply": "An object that absorbs every wavelength looks black."},
                 {"text": "It transmits all of the wavelengths", "correct": False,
                  "reply": "An opaque object does not transmit light."},
                 {"text": "It reflects only a white wavelength", "correct": False,
                  "reply": "There is no single white wavelength. White light is a mixture of all "
                           "the colours."},
                 {"text": "It reflects all wavelengths equally", "correct": True},
             ]},
        ],
        "r2": [
            {"kind": "mcq", "command": "Identify", "marks": 2,
             "prompt": "A blue book is lit by red light only. Identify the colour it appears.",
             "why": "The book reflects blue light and absorbs the other colours. There is no blue "
                    "light to reflect, and it absorbs the red, so it looks black.",
             "options": [
                 {"text": "Blue", "correct": False,
                  "reply": "There is no blue light in the red light for the book to reflect."},
                 {"text": "Red", "correct": False,
                  "reply": "A blue book absorbs red light, so no red is reflected."},
                 {"text": "Black", "correct": True},
                 {"text": "Purple", "correct": False,
                  "reply": "Nothing mixes. The book absorbs the red and reflects nothing."},
             ]},
            {"kind": "mcq", "command": "Identify", "marks": 2,
             "prompt": "A bathroom window lets light through, but you cannot see a clear image "
                       "through it. Identify the best description of the glass.",
             "why": "It transmits light but scatters it, so it is translucent.",
             "options": [
                 {"text": "Transparent, because it transmits light without scattering it",
                  "correct": False,
                  "reply": "Then you could see a clear image through it."},
                 {"text": "Translucent, because it transmits light but scatters it", "correct": True},
                 {"text": "Transparent, because it transmits most of the light", "correct": False,
                  "reply": "Transmitting light is not enough. A transparent object does not scatter "
                           "the light, so you could see clearly through it."},
                 {"text": "Translucent, because it absorbs most of the light", "correct": False,
                  "reply": "Frosted glass lets most of the light through. It is translucent because "
                           "it scatters the light."},
             ]},
        ],
        "r3": [
            {"kind": "chain", "command": "Explain", "marks": 3,
             "prompt": "Explain why a leaf looks green in white light. Put the links in order.",
             "links": ["White light, a mixture of all the colours, falls on the leaf.",
                       "The leaf reflects green light most strongly and absorbs the other "
                       "colours.",
                       "So mainly green light is reflected into your eye, and the leaf looks "
                       "green."],
             "herrings": [{"text": "The leaf adds green to the white light.",
                           "why": "An object cannot add colour. It reflects some wavelengths "
                                  "and absorbs the rest."},
                          {"text": "The leaf absorbs green light.",
                           "why": "It reflects green. The colours it absorbs do not reach your "
                                  "eye."}]},
            {"kind": "chain", "command": "Explain", "marks": 4,
             "prompt": "White light passes through a red filter and then a green filter. Explain "
                       "why no light comes out. Put the links in order.",
             "links": ["The red filter transmits red light and absorbs the other colours.",
                       "So only red light reaches the green filter.",
                       "The green filter absorbs this red light.",
                       "So no light is transmitted by the green filter."],
             "herrings": [{"text": "The green filter turns the red light into green light.",
                           "why": "A filter does not change colour. It absorbs or transmits."},
                          {"text": "The red filter reflects all of the light back.",
                           "why": "A red filter transmits red light."}]},
        ],
        "r4": [
            {"kind": "write", "command": "Explain", "marks": 4,
             "prompt": "A footballer wears a red shirt and white shorts. Explain what colour each "
                       "looks in white light, and then in green light only.",
             "levels": [
                 {"label": "Level 2 · 3–4", "text": "Both items in both lights, each colour "
                  "explained by which wavelengths are reflected and which are absorbed.",
                  "max": 4},
                 {"label": "Level 1 · 1–2", "text": "Some correct colours, with little or no "
                  "explanation.", "max": 2},
                 {"label": "No relevant content · 0", "text": "", "max": 0}],
             "points": ["In white light the shirt reflects red light and absorbs the other "
                        "colours, so it looks red.",
                        "In white light the shorts reflect all wavelengths equally, so they look "
                        "white.",
                        "In green light the shirt absorbs the green and has no red to reflect, "
                        "so it looks black.",
                        "In green light the shorts reflect the green light, so they look green."],
             "reject": ["“The shirt still looks red in green light, because it is a red shirt.”",
                        "“The shorts look white in green light.”"]},
        ],
    },
}
