# -*- coding: utf-8 -*-
"""Waves for detection and exploration, in the lean shape. LEGACY record: the Design batch-3 page
keeps its ladder (Ks4Ladder) and practice set, so their question ids survive. Spec table:
ks4-waves-detection-exploration.md (AQA 8463 4.6.1.5, physics only, HT only). TH only.

The practice set reads the route's quiz list (K.bank), and Rung 1 is the quiz item whose stem
contains "S-waves are not detected on the opposite side" (K.find): that stem is kept verbatim.

The old data's "d = v × t / 2" is not an AQA equation. AQA's is distance travelled = speed ×
time, s = v t (8463 4.5.6.1.2), then halve it for the echo's trip there and back; the page's own
worked examples already write "s = v t; depth = s ÷ 2". The shadow-zone angles (about 104° and
140°) are left out of the teaching (not in the spec); the legacy figure still labels the six
seismometer positions in degrees.

logic_edits:
  1. The first worked example was read from the sound-waves-hearing subtopic's frozen `fifas`
     ("d = v × t / 2", "ultrasound pulse" for a ship's echo sounder). Replaced by the page's own
     s = v t steps, same numbers (0.06 s, 1500 m/s, 45 m). The frozen field itself is untouched.
  2. "as on the equation sheet": s = v t is a recall equation, not on the sheet.
  3. quakeFig and scanFig drew only stage by stage through the (removed) benches: drawn always,
     each at its finished stage (records, S-wave and P-wave paths; echoes and the depth scale)."""

LESSON = {
    "slug": "waves-detection-exploration",
    "start": {
        "setup": "Nobody has ever drilled down to the Earth's core.",
        "question": "If you had to guess, what gives us evidence about what the core is like?",
        "options": [
            ("Lava from volcanoes",
             "Earthquake waves. They travel through the Earth, and instruments all over the "
             "world record them."),
            ("Earthquake waves",
             "Earthquake waves. They travel through the Earth, and instruments all over the "
             "world record them."),
        ],
        "answer": 1,
    },
    "words": ["ultrasound", "echo", "P-wave", "S-wave"],
    "knowledge": [
        {"kind": "card", "title": "Finding what is hidden",
         "body": ["The differences in velocity, absorption and reflection between different types "
                  "of wave in solids and liquids can be used both for detection and exploration of "
                  "structures which are hidden from direct observation."]},
        {"kind": "card", "title": "Ultrasound",
         "body": ["Ultrasound waves have a frequency higher than the upper limit of hearing for "
                  "humans, above 20 kHz.",
                  {"points": [
                      "Ultrasound waves are partially reflected when they meet a boundary between "
                      "two different media. The rest travels on.",
                      "The time taken for the reflections to reach a detector can be used to "
                      "determine how far away such a boundary is.",
                      "This allows ultrasound waves to be used for both medical and industrial "
                      "imaging, such as scanning an unborn baby or finding a crack inside a metal "
                      "beam.",
                  ]},
                  {"slot": "legacy-fig:scanFig"},
                  "The deeper the boundary, the later its echo arrives."]},
        {"kind": "card", "title": "Distance from an echo",
         "body": ["distance travelled = speed × time, s = v t",
                  {"points": ["s: distance travelled, in metres (m)",
                              "v: speed, in metres per second (m/s)",
                              "t: time, in seconds (s)"]},
                  {"slot": "triangle:EQ_S"},
                  "The echo travels to the boundary and back, so the depth is half of the distance "
                  "travelled.",
                  {"slot": "cfifa"}]},
        {"kind": "card", "title": "Echo sounding",
         "body": ["Echo sounding, using high frequency sound waves, is used to detect objects in "
                  "deep water and measure water depth.",
                  "A ship sends a pulse down and times the echo from the seabed or from a shoal "
                  "of fish."]},
        {"kind": "reveal", "title": "P-waves and S-waves",
         "cols": ["P-waves", "S-waves"],
         "rows": [
             ("Produced by", "Earthquakes", "Earthquakes"),
             ("Type of wave", "Longitudinal", "Transverse"),
             ("Through solids", "Yes", "Yes"),
             ("Through liquids", "Yes, at a different speed", "No"),
         ]},
        {"kind": "card", "title": "Evidence for the Earth's core",
         "body": [{"slot": "legacy-fig:quakeFig"},
                  {"points": [
                      "Seismometers around the world record the P-waves and S-waves from an "
                      "earthquake.",
                      "No S-waves are detected on the far side of the Earth. S-waves cannot "
                      "travel through a liquid, so part of the core must be liquid: the outer "
                      "core.",
                      "P-waves change speed as they enter and leave the core, so they refract. "
                      "This leaves a band of the surface where no P-waves arrive.",
                      "The size of these regions, called shadow zones, shows how big the core "
                      "is.",
                  ]},
                  "In the figure, blue paths are P-waves and gold paths are S-waves. A filled "
                  "letter at a seismometer means that wave was recorded there; a dashed one means "
                  "it was not."]},
        {"kind": "card", "title": "New evidence",
         "body": ["The study of seismic waves provided new evidence that led to discoveries about "
                  "parts of the Earth which are not directly observable."]},
        {"kind": "card", "title": "Easy mistakes",
         "body": [{"mistakes": [
             ("depth = speed × time.",
              "That is the distance there and back. The depth is half of it."),
             ("P-waves cannot travel through liquids.",
              "P-waves travel through solids and liquids. S-waves cannot travel through a "
              "liquid."),
             ("Ultrasound is reflected completely at the first boundary.",
              "It is partially reflected. The rest travels on to deeper boundaries."),
         ]}]},
    ],
    "key_fact": "Ultrasound is partially reflected at a boundary between two different media, and "
                "the time for the echo to return gives the distance to the boundary. P-waves are "
                "longitudinal and travel through solids and liquids, but S-waves are transverse "
                "and cannot travel through a liquid, so seismic waves give evidence for the "
                "structure and size of the Earth's core.",
    "deeper": [
        {"kind": "card", "title": "Curved paths",
         "body": ["Seismic waves travel on curved paths through the Earth. Their speed changes "
                  "gradually with depth, so they refract all the way."]},
        {"kind": "card", "title": "Scanning an unborn baby",
         "body": ["Ultrasound is used instead of X-rays to scan an unborn baby. X-rays are "
                  "ionising radiation, which can cause the mutation of genes."]},
        {"kind": "card", "title": "Command words",
         "body": [{"points": [
             "<strong>Calculate</strong> a depth: s = v t, then halve it for the trip there and "
             "back.",
             "<strong>Explain</strong> the evidence: name the wave, say what it can or cannot "
             "travel through, then say what that shows about the Earth.",
         ]}]},
    ],
    "try": None,
    "equations": {
        "EQ_S": {"name": "Distance travelled", "written": "distance travelled = speed × time",
                 "source": "none",
                 "top": {"s": "s", "name": "distance", "unit": "m"},
                 "bottom": [{"s": "v", "name": "speed", "unit": "m/s"},
                            {"s": "t", "name": "time", "unit": "s"}]},
    },
    "legacy": {
        "batch": "batch-3",
        "logic_edits": [
            ("{ tab: 'Nothing to convert', head: F0.question, steps: K.cfifa(F0, 'Nothing to "
             "convert: the time is in s and the speed in m/s.') },",
             "{ tab: 'Nothing to convert', head: 'A ship’s echo sounder sends a pulse of high "
             "frequency sound down to the seabed. The echo returns after 0.06 s. Sound travels at "
             "1500 m/s in sea water. Calculate the depth of the seabed.', steps: ST('Nothing to "
             "convert: the time is in s and the speed in m/s.', SF, 's = 1500 × 0.06', 's = 90 m; "
             "depth = 90 ÷ 2 = 45', 'depth = 45 m') },"),
            ("placeholder: 'as on the equation sheet, then the echo step'",
             "placeholder: 'write the equation, then the echo step'"),
            ("quakeFig: ready ? K.fig(this.earthSvg(view), '') : null,",
             "quakeFig: ready ? K.fig(this.earthSvg({ hidden: false, solidS: false, records: "
             "true, sRays: true, pRays: true, fadeS: false, bigCore: false, anim: false }), '') "
             ": null,"),
            ("scanFig: ready ? K.fig(this.scanSvg({ echoes: us > 1 || uShown, ruler: us === 2 && "
             "uShown, anim: us === 1 && uShown }), '') : null,",
             "scanFig: ready ? K.fig(this.scanSvg({ echoes: true, ruler: true, anim: false }), "
             "'') : null,"),
        ],
    },
}
