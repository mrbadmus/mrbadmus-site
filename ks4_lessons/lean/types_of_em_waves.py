# -*- coding: utf-8 -*-
"""Types of electromagnetic waves, in the lean shape. LEGACY record: the Design batch-3 page keeps
its ladder (Ks4Ladder) and practice set, so their question ids survive. Spec table:
ks4-types-of-em-waves.md (AQA 8464 6.6.2.1 / 8463 4.6.2.1, word for word the same).

The practice set reads the route's quiz list (K.bank), and Rung 1 is the quiz item whose stem
contains "have the same what?" (K.find): that stem is kept verbatim on every route in
quiz-types-of-em-waves.json.

logic_edits:
  1. spectrumFig drew only after the (removed) spectrum bench was built (`p1`): drawn always,
     still, so the card can show it.
  2. "as on the equation sheet": v = f λ is a recall equation, not on the sheet.
  3. Rung 3's chain had two right orders (its first two links were both premises). Rewritten so
     cause and effect force one order. Same rung position, same id."""

LESSON = {
    "slug": "types-of-em-waves",
    "start": {
        "setup": None,
        "question": "If you had to guess, how much of the electromagnetic spectrum can your eyes "
                    "detect?",
        "options": [
            ("Most of it",
             "Only a small part. Our eyes only detect visible light, a limited range of "
             "electromagnetic waves."),
            ("Only a small part",
             "Only a small part. Our eyes only detect visible light, a limited range of "
             "electromagnetic waves."),
        ],
        "answer": 1,
    },
    "words": ["electromagnetic spectrum", "transverse", "wavelength", "frequency"],
    "knowledge": [
        {"kind": "card", "title": "Electromagnetic waves",
         "body": ["Electromagnetic waves are transverse waves that transfer energy from the source "
                  "of the waves to an absorber.",
                  "Electromagnetic waves form a continuous spectrum.",
                  "All types of electromagnetic wave travel at the same velocity through a vacuum "
                  "(space) or air.",
                  # Added 14 Nov 2026 on Mide's ruling (UNSURE.md): the speed of light as a fact.
                  "In a vacuum, that velocity is 3 × 10⁸ m/s (300 000 000 m/s)."]},
        {"kind": "card", "title": "The spectrum in order",
         "body": ["The waves that form the electromagnetic spectrum are grouped in terms of their "
                  "wavelength and their frequency.",
                  {"slot": "legacy-fig:spectrumFig"},
                  "Going from long to short wavelength (or from low to high frequency) the groups "
                  "are: radio waves, microwaves, infrared, visible light (red to violet), "
                  "ultraviolet, X-rays and gamma rays."]},
        {"kind": "reveal", "title": "From one end to the other",
         "cols": ["Radio waves", "Gamma rays"],
         "rows": [
             ("Wavelength", "Longest", "Shortest"),
             ("Frequency", "Lowest", "Highest"),
             ("Speed in a vacuum", "The same as every other group", "The same as every other group"),
         ]},
        {"kind": "card", "title": "What our eyes detect",
         "body": ["Our eyes only detect visible light and so detect a limited range of "
                  "electromagnetic waves.",
                  "Visible light runs from red, with the longest wavelength, to violet, with the "
                  "shortest."]},
        {"kind": "card", "title": "Transferring energy",
         "body": ["Electromagnetic waves transfer energy from a source to an absorber.",
                  {"points": [
                      "The Sun emits infrared. Your skin absorbs it, and warms up.",
                      "A microwave oven emits microwaves. The food absorbs them, and heats up.",
                      "A radio transmitter emits radio waves. The aerial of a radio absorbs them.",
                  ]}]},
        {"kind": "card", "title": "Using v = f λ",
         "body": ["Electromagnetic waves obey the wave equation, wave speed = frequency × "
                  "wavelength.",
                  {"slot": "triangle:EQ_V"},
                  "A question gives you the speed of the waves. Every group has the same speed, "
                  "so a shorter wavelength means a higher frequency.",
                  {"slot": "cfifa"}]},
        {"kind": "card", "title": "Easy mistakes",
         "body": [{"mistakes": [
             ("Gamma rays travel fastest.",
              "All electromagnetic waves travel at the same speed in a vacuum."),
             ("Radio waves have the highest frequency.",
              "Radio waves have the lowest frequency and the longest wavelength."),
             ("Electromagnetic waves are longitudinal.",
              "Electromagnetic waves are transverse."),
         ]}]},
    ],
    "key_fact": "Electromagnetic waves are transverse waves that transfer energy from a source to "
                "an absorber, and all of them travel at the same velocity through a vacuum or air. "
                "Going from long to short wavelength (low to high frequency) the groups are: radio "
                "waves, microwaves, infrared, visible light, ultraviolet, X-rays and gamma rays.",
    "deeper": [
        {"kind": "card", "title": "Remembering the order",
         "body": ["One way to remember it, from radio waves to gamma rays: Rich Men In Vegas Use "
                  "X-ray Glasses.",
                  "Radio, Microwaves, Infrared, Visible, Ultraviolet, X-rays, Gamma."]},
        {"kind": "card", "title": "A continuous spectrum",
         "body": ["The groups join with no gaps between them. Where one group ends and the next "
                  "begins is a choice people make, so the edges are not sharp."]},
        {"kind": "card", "title": "Command words",
         "body": [{"points": [
             "<strong>Describe</strong> the spectrum: give the order, say what changes from one "
             "end to the other, and what stays the same.",
             "<strong>Calculate</strong>: convert to Hz and m first, then use v = f λ.",
         ]}]},
    ],
    "try": None,
    "equations": {
        "EQ_V": {"name": "Wave speed", "written": "wave speed = frequency × wavelength",
                 "source": "none",
                 "top": {"s": "v", "name": "wave speed", "unit": "m/s"},
                 "bottom": [{"s": "f", "name": "frequency", "unit": "Hz"},
                            {"s": "λ", "name": "wavelength", "unit": "m"}]},
    },
    "legacy": {
        "batch": "batch-3",
        "logic_edits": [
            ("spectrumFig: ready && p1 ? K.fig(this.spectrumSvg(specMode), '') : null,",
             "spectrumFig: ready ? K.fig(this.spectrumSvg('still'), '') : null,"),
            ("placeholder: 'as on the equation sheet'", "placeholder: 'write the equation'"),
            ("links: ['Gamma rays have a much shorter wavelength than radio waves.', 'All "
             "electromagnetic waves travel at the same speed in a vacuum.', 'v = f λ, so at the "
             "same speed a shorter wavelength means more waves pass a point each second: a higher "
             "frequency.'],",
             "links: ['All electromagnetic waves travel at the same speed in a vacuum.', 'As their "
             "speed is the same, v = f λ means a shorter wavelength gives a higher frequency.', 'Gamma "
             "rays have a much shorter wavelength than radio waves, so by this rule they have the "
             "higher frequency.'],"),
            # Blind-pass fixes (blind/RESULT.md), applied after the edits above.
            ("convOptions: ['Nothing to convert', 'Convert GHz to Hz: multiply by 10⁹', 'Convert GHz to Hz: multiply by 10⁶']",
             "convOptions: ['Nothing to convert', 'Convert GHz to Hz (× 10⁹), then m to cm (× 100)', 'Convert GHz to Hz (× 10⁶), then m to cm (× 100)']"),
        ],
    },
}
