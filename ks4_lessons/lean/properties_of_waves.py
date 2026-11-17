# -*- coding: utf-8 -*-
"""Properties of waves, in the lean shape. New record, no legacy page.
Spec table: ks4-properties-of-waves.md (AQA 8464 6.6.1.2 + Required practical activity 20 /
8463 4.6.1.2 + Required practical activity 8). The one (Physics only) statement, sound passing
from one medium to another, is on TF TH only. The old data's "RP19" label is wrong: 8464 numbers
this practical 20 and 8463 numbers it 8, so each route's card carries its own number.

v = f λ is a recall equation (source "none", with a triangle). T = 1 / f is on the Physics
equation sheet and has no three-cell triangle (source "sheet")."""

_CFQ_PH = ["anything to convert?", "written out", "numbers in", "work it out", "with unit"]


def _q(lines, conv_ph=None):
    """A Ks4Cfifa question's five lines, in the legacy CFQ shape."""
    letters = [("C", "Convert"), ("F", "Formula"), ("I", "Insert"), ("F", "Fine-tune"), ("A", "Answer")]
    ph = list(_CFQ_PH)
    if conv_ph:
        ph[0] = conv_ph
    return [{"letter": l, "label": lab, "placeholder": p, "line": ln}
            for (l, lab), p, ln in zip(letters, ph, lines)]


_RP_BODY = [
    "Make observations to identify the suitability of apparatus to measure the frequency, "
    "wavelength and speed of waves in a ripple tank and waves in a solid, and take appropriate "
    "measurements.",
    "<strong>Waves in a ripple tank</strong>",
    {"points": [
        "A lamp above the tank makes the ripples cast shadows on a sheet of paper below it.",
        "Wavelength: measure the distance across 10 wavelengths with a ruler, then divide by 10. "
        "One wavelength is too small to measure accurately on its own.",
        "Frequency: count the waves passing a point in 10 seconds, then divide by 10.",
        "Speed: wave speed = frequency × wavelength. Or time one ripple across a measured "
        "distance, and use speed = distance ÷ time.",
    ]},
    "<strong>Waves on a stretched string</strong>",
    {"points": [
        "A vibration generator, driven by a signal generator, shakes one end of a string "
        "stretched over a pulley.",
        "Change the frequency until the string shows a clear, steady pattern of loops.",
        "Frequency: read it from the signal generator.",
        "Wavelength: each loop is half a wavelength. Measure across as many loops as you can with "
        "a metre ruler, divide by the number of loops, then double it.",
        "Speed: wave speed = frequency × wavelength.",
    ]},
]

LESSON = {
    "slug": "properties-of-waves",
    "start": {
        "setup": "You flick one end of a long rope to send waves along it.",
        "question": "If you had to guess, if you flick it more times each second, what happens to "
                    "the wavelength?",
        "options": [
            ("It gets shorter",
             "It gets shorter. The waves travel at the same speed, so more waves each second "
             "means each wave is shorter."),
            ("It gets longer",
             "It gets shorter. The waves travel at the same speed, so more waves each second "
             "means each wave is shorter."),
        ],
        "answer": 0,
    },
    "words": ["amplitude", "wavelength", "frequency", "period"],
    "knowledge": [
        {"kind": "card", "title": "Amplitude and wavelength",
         "body": [{"slot": "fig:wave-amplitude-wavelength"},
                  {"points": [
                      "The <strong>amplitude</strong> of a wave is the maximum displacement of a "
                      "point on a wave away from its undisturbed position.",
                      "The <strong>wavelength</strong> of a wave is the distance from a point on "
                      "one wave to the equivalent point on the adjacent wave.",
                  ]},
                  "On a diagram, measure the amplitude from the undisturbed position up to a "
                  "peak. Measure the wavelength from one peak to the next peak."]},
        {"kind": "card", "title": "Frequency and period",
         "body": ["The <strong>frequency</strong> of a wave is the number of waves passing a "
                  "point each second. It is measured in hertz (Hz).",
                  "The <strong>period</strong> is the time for one wave to pass a point. It is "
                  "measured in seconds (s).",
                  "period = 1 ÷ frequency, T = 1 / f",
                  {"points": ["T: period, in seconds (s)", "f: frequency, in hertz (Hz)"]},
                  "This equation is on the equation sheet."]},
        {"kind": "card", "title": "The wave equation",
         "body": ["The wave speed is the speed at which the energy is transferred (or the wave "
                  "moves) through the medium.",
                  "All waves obey the wave equation:",
                  "wave speed = frequency × wavelength, v = f λ",
                  {"points": ["v: wave speed, in metres per second (m/s)",
                              "f: frequency, in hertz (Hz)",
                              "λ: wavelength, in metres (m)"]},
                  "You must remember this equation. It is not on the equation sheet.",
                  {"slot": "triangle:EQ_V"}]},
        {"kind": "card", "title": "Worked examples",
         "body": [{"slot": "cfifa"}]},
        {"kind": "card", "title": "Measuring the speed of sound in air",
         "body": [{"points": [
             "Two people stand a measured distance apart on a large field, a few hundred metres.",
             "One bangs two blocks of wood together above their head.",
             "The other starts a stopwatch when they see the blocks hit, and stops it when they "
             "hear the bang.",
             "speed = distance ÷ time. Repeat several times and take a mean.",
         ]},
             "The light reaches the timer almost at once, so the time measured is the time the "
             "sound takes to travel."]},
        {"kind": "card", "title": "Required practical activity 20", "routes": ["CF", "CH"],
         "body": _RP_BODY},
        {"kind": "card", "title": "Required practical activity 8", "routes": ["TF", "TH"],
         "body": _RP_BODY},
        {"kind": "card", "title": "Sound passing from one medium to another",
         "routes": ["TF", "TH"],
         "body": ["When a sound wave passes from one medium into another, its frequency stays "
                  "the same.",
                  "Its speed changes, so its wavelength changes too: v = f λ.",
                  "Sound travels faster in water than in air. So in water the same sound has a "
                  "longer wavelength.",
                  {"points": [
                      "A 500 Hz sound travels at 340 m/s in air: λ = 340 ÷ 500 = 0.68 m.",
                      "The same 500 Hz sound travels at 1500 m/s in water: λ = 1500 ÷ 500 = 3.0 m.",
                  ]}]},
        {"kind": "card", "title": "Easy mistakes",
         "body": [{"mistakes": [
             ("The amplitude is the height from a trough to a peak.",
              "The amplitude is from the undisturbed position to a peak. That is half the trough "
              "to peak height."),
             ("The wavelength is the distance from a peak to the next trough.",
              "That is half a wavelength. Measure from one peak to the next peak."),
             ("Using 2 kHz as 2 in v = f λ.",
              "Convert first: 2 kHz = 2000 Hz."),
         ]}]},
    ],
    "key_fact": "The amplitude is the maximum displacement of a point on a wave from its "
                "undisturbed position, the wavelength is the distance from a point on one wave to "
                "the equivalent point on the next, and the frequency is the number of waves "
                "passing a point each second. All waves obey wave speed = frequency × wavelength "
                "(v = f λ), and period = 1 ÷ frequency.",
    "deeper": [
        {"kind": "card", "title": "A better way to time sound",
         "body": ["A stopwatch depends on your reaction time, which is large compared with the "
                  "time the sound takes.",
                  "Two microphones a measured distance apart, connected to a fast electronic "
                  "timer, avoid this. The sound starts the timer at the first microphone and "
                  "stops it at the second."]},
        {"kind": "card", "title": "Command words",
         "body": [{"points": [
             "<strong>Calculate</strong>: convert, write the equation, put the numbers in, "
             "rearrange, then give the answer with its unit.",
             "<strong>Describe a method</strong>: say what you measure, how you measure it, and "
             "how you work out the speed.",
         ]}]},
    ],
    "try": None,
    "legacy": None,
    "equations": {
        "EQ_V": {"name": "Wave speed", "written": "wave speed = frequency × wavelength",
                 "source": "none",
                 "top": {"s": "v", "name": "wave speed", "unit": "m/s"},
                 "bottom": [{"s": "f", "name": "frequency", "unit": "Hz"},
                            {"s": "λ", "name": "wavelength", "unit": "m"}]},
        "EQ_T": {"name": "Period", "written": "period = 1 ÷ frequency", "source": "sheet"},
    },
    "cfifa": {
        "examples": [
            {"tab": "Nothing to convert", "eq": "EQ_V", "find": "v",
             "head": "A water wave has a frequency of 4.0 Hz and a wavelength of 0.50 m. "
                     "Calculate its speed.",
             "steps": [["C", "Convert", "Nothing to convert: Hz and m."],
                       ["F", "Formula", "v = f λ"],
                       ["I", "Insert", "v = 4.0 × 0.50"],
                       ["F", "Fine-tune", "Nothing to rearrange: v = 2.0"],
                       ["A", "Answer", "v = 2.0 m/s"]]},
            {"tab": "Convert first", "eq": "EQ_V", "find": "λ",
             "head": "A sound wave has a frequency of 2.0 kHz. It travels at 340 m/s. Calculate "
                     "its wavelength.",
             "steps": [["C", "Convert", "2.0 kHz × 1000 = 2000 Hz"],
                       ["F", "Formula", "v = f λ"],
                       ["I", "Insert", "340 = 2000 × λ"],
                       ["F", "Fine-tune", "λ = 340 ÷ 2000 = 0.17",
                        "Rearrange: divide both sides by 2000."],
                       ["A", "Answer", "λ = 0.17 m"]]},
            {"tab": "The period", "eq": "EQ_T", "find": "T",
             "head": "A wave has a frequency of 50 Hz. Calculate its period.",
             "steps": [["C", "Convert", "Nothing to convert: Hz."],
                       ["F", "Formula", "T = 1 / f"],
                       ["I", "Insert", "T = 1 / 50"],
                       ["F", "Fine-tune", "T = 0.02"],
                       ["A", "Answer", "T = 0.02 s"]]},
        ],
        "questions": [
            {"tab": "Question 1", "id": "pw-q1",
             "head": "A wave on a string has a frequency of 25 Hz and a wavelength of 0.80 m. "
                     "Calculate its speed.",
             "close": "Check: 20 ÷ 25 = 0.80 m, the wavelength you started with.",
             "steps": _q(["Nothing to convert: Hz and m.", "v = f λ", "v = 25 × 0.80",
                          "v = 20", "v = 20 m/s"])},
            {"tab": "Question 2", "id": "pw-q2",
             "head": "Ripples in a ripple tank travel at 0.12 m/s. Their wavelength is 1.5 cm. "
                     "Calculate their frequency.",
             "close": "Unconverted, 0.12 ÷ 1.5 gives 0.08 Hz: a hundred times too small.",
             "steps": _q(["1.5 cm ÷ 100 = 0.015 m", "v = f λ", "0.12 = f × 0.015",
                          "f = 0.12 ÷ 0.015 = 8", "f = 8 Hz"], "cm to m?")},
        ],
    },
    "rungs": {
        "r1": [
            {"kind": "mcq", "command": "State", "marks": 1,
             "prompt": "State what is meant by the frequency of a wave.",
             "why": "The frequency is the number of waves passing a point each second.",
             "options": [
                 {"text": "The number of waves passing a point each second", "correct": True},
                 {"text": "The distance from one wave to the next", "correct": False,
                  "reply": "That is the wavelength."},
                 {"text": "The maximum displacement from the undisturbed position", "correct": False,
                  "reply": "That is the amplitude."},
                 {"text": "The time for one wave to pass a point", "correct": False,
                  "reply": "That is the period."},
             ]},
            {"kind": "mcq", "command": "Give", "marks": 1,
             "prompt": "Give the unit of frequency.",
             "why": "Frequency is measured in hertz (Hz).",
             "options": [
                 {"text": "seconds (s)", "correct": False,
                  "reply": "Seconds are the unit of the period."},
                 {"text": "hertz (Hz)", "correct": True},
                 {"text": "metres per second (m/s)", "correct": False,
                  "reply": "That is the unit of wave speed."},
                 {"text": "metres (m)", "correct": False,
                  "reply": "That is the unit of wavelength."},
             ]},
        ],
        "r2": [
            {"kind": "calc", "command": "Calculate", "marks": 2,
             "prompt": "A water wave has a frequency of 0.50 Hz and a wavelength of 3.0 m. "
                       "Calculate its speed.",
             "convOptions": ["Nothing to convert", "Convert Hz to kHz: divide by 1000",
                             "Convert m to cm: multiply by 100"],
             "convAnswer": 0, "answer": 1.5, "tol": 0.01, "unit": "m/s",
             "units": ["m/s", "Hz", "m", "s"],
             "right": "v = 0.50 × 3.0 = 1.5 m/s.",
             "wrong": "v = f λ, so v = 0.50 × 3.0 = 1.5 m/s.",
             "model": ["C · Nothing to convert", "F · v = f λ", "I · v = 0.50 × 3.0",
                       "F · v = 1.5", "A · v = 1.5 m/s"]},
            {"kind": "calc", "command": "Calculate", "marks": 2,
             "prompt": "A sound wave has a frequency of 0.40 kHz. Calculate its period.",
             "convOptions": ["Nothing to convert", "Convert kHz to Hz: multiply by 1000",
                             "Convert kHz to Hz: divide by 1000"],
             "convAnswer": 1, "answer": 0.0025, "tol": 0.00005, "unit": "s",
             "units": ["s", "Hz", "m/s", "m"],
             "right": "0.40 kHz = 400 Hz, and T = 1 / 400 = 0.0025 s.",
             "wrong": "Convert 0.40 kHz to 400 Hz first. Then T = 1 / f = 1 / 400 = 0.0025 s.",
             "model": ["C · 0.40 kHz × 1000 = 400 Hz", "F · T = 1 / f", "I · T = 1 / 400",
                       "F · T = 0.0025", "A · T = 0.0025 s"]},
        ],
        "r3": [
            {"kind": "chain", "command": "Describe", "marks": 3,
             "prompt": "Describe how to measure the wavelength of ripples in a ripple tank. Put "
                       "the links in order.",
             "links": ["Switch on the lamp above the tank so the ripples cast shadows on the "
                       "paper below.",
                       "Measure the distance across 10 wavelengths of the shadows with a ruler.",
                       "Divide this distance by 10 to find one wavelength."],
             "herrings": [{"text": "Measure one wavelength straight across the moving water.",
                           "why": "One wavelength is small and the ripples move. Measuring many "
                                  "on the paper, then dividing, is more accurate."},
                          {"text": "Divide the distance by the frequency.",
                           "why": "Divide by the number of waves you measured across."}]},
            {"kind": "chain", "command": "Describe", "marks": 3,
             "prompt": "Describe a method to measure the speed of sound in air. Put the links in "
                       "order.",
             "links": ["Measure a distance of a few hundred metres between two people on a field.",
                       "One person makes a loud bang. The other starts a stopwatch on seeing it and "
                       "stops it on hearing it.",
                       "Calculate the speed: speed = distance ÷ time."],
             "herrings": [{"text": "Start the stopwatch on hearing the bang.",
                           "why": "Start it on seeing the bang. The light arrives almost at once, "
                                  "so you time the sound's journey."},
                          {"text": "Stand close together so the bang is louder.",
                           "why": "A short distance gives a time too small to measure with a "
                                  "stopwatch."}]},
        ],
        "r4": [
            {"kind": "write", "command": "Describe", "marks": 4,
             "prompt": "Describe how to use a ripple tank to find the speed of water waves.",
             "levels": [
                 {"label": "Level 2 · 3–4", "text": "A clear method to measure both the wavelength "
                  "and the frequency, with v = f λ used to find the speed.", "max": 4},
                 {"label": "Level 1 · 1–2", "text": "Some relevant steps, for example how to "
                  "measure one quantity.", "max": 2},
                 {"label": "No relevant content · 0", "text": "", "max": 0}],
             "points": ["A lamp above the tank makes the ripples cast shadows on paper below.",
                        "Measure across several wavelengths (for example 10) with a ruler, and "
                        "divide to find one wavelength.",
                        "Count the waves passing a point in a measured time (for example 10 s), and "
                        "divide to find the frequency.",
                        "Calculate the speed with wave speed = frequency × wavelength.",
                        "Or: time one ripple over a measured distance, and use speed = distance ÷ "
                        "time."],
             "reject": ["“v = f ÷ λ.”",
                        "“Measure one wavelength in the water with a ruler.” This alone is not "
                        "accurate enough for the measuring mark."]},
        ],
    },
}
