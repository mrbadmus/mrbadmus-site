# -*- coding: utf-8 -*-
"""Frequency, pitch and loudness, in the lean shape.
Spec table: docs/lessons/wave2/ks3-frequency-pitch-and-loudness.md."""

LESSON = {
    "slug": "frequency-pitch-and-loudness",
    "start": {
        "setup": "Pluck a guitar string gently and listen. Then pluck the same string much harder.",
        "question": "If you had to guess, does plucking harder make the note "
                    "higher as well as louder?",
        "options": [
            ("No, only louder",
             "Right. The note stays where it was. The string swings further, so it sounds louder."),
            ("Yes, higher too",
             "The note stays where it was. A harder pluck only makes the string swing further."),
        ],
        "answer": 0,
    },
    "words": ["frequency", "pitch", "amplitude", "loudness"],
    "word_defs": {
        "frequency": "The number of complete vibrations each second, measured in hertz (Hz).",
        "pitch": "How high or low a note sounds. A higher frequency gives a higher pitch.",
        "amplitude": "How far the vibrating source moves from its rest position each time.",
        "loudness": "How loud a sound is. A bigger amplitude gives a louder sound.",
    },
    "knowledge": [
        {"kind": "card", "title": "Frequency",
         "body": ["Frequency is the number of complete vibrations each second.",
                  "It is measured in hertz, Hz.",
                  "1 Hz is one complete vibration each second.",
                  "A string that vibrates 440 times each second has a frequency of 440 Hz."]},
        {"kind": "card", "title": "Seeing pitch and loudness",
         "body": [{"figure": "p6-05-traces"},
                  "A microphone and an oscilloscope can show a sound as a trace like these.",
                  "A taller wave has a bigger amplitude, so it sounds louder.",
                  "More waves across the screen means a higher frequency, so a higher pitch."]},
        {"kind": "reveal", "title": "What changes what",
         "cols": ["What the source does", "What you hear"],
         "rows": [
             ("Bigger amplitude", "Moves further each time", "A louder sound"),
             ("Smaller amplitude", "Moves less far each time", "A quieter sound"),
             ("Higher frequency", "More vibrations each second", "A higher pitch"),
             ("Lower frequency", "Fewer vibrations each second", "A lower pitch"),
         ]},
        {"kind": "card", "title": "Pitch and loudness are separate",
         "body": ["Turning the volume up makes a loudspeaker cone move further each time.",
                  "It still vibrates the same number of times each second.",
                  "So the sound gets louder, and the pitch stays the same."]},
        {"kind": "card", "title": "Frequency and wavelength",
         "body": ["All sounds travel at the same speed through air, about 340 m/s.",
                  "A higher frequency sound has a shorter wavelength.",
                  "Its compressions are closer together, because more are made each second."]},
        {"kind": "card", "title": "The frequency equation",
         "body": [{"figure": "p6-05-triangle"},
                  "number of vibrations = frequency (Hz) × time (s)",
                  "frequency (Hz) = number of vibrations ÷ time (s)",
                  "The number of vibrations is a count, so it has no unit.",
                  "Time must be in seconds, because 1 Hz is one vibration each second."]},
        {"kind": "card", "title": "Worked example: counting vibrations",
         "body": [{"figure": "p6-05-count"},
                  "A tuning fork of frequency 200 Hz rings for 3.0 s. "
                  "Find how many complete vibrations it makes.",
                  {"points": ["Convert: nothing. The time is already in seconds.",
                              "Formula: number of vibrations = frequency × time",
                              "Insert: number of vibrations = 200 Hz × 3.0 s",
                              "Fine-tune: 200 × 3.0 = 600",
                              "Answer: 600 vibrations"]}]},
        {"kind": "card", "title": "Worked example: finding a frequency",
         "body": [{"figure": "p6-05-rate"},
                  "A tuning fork makes 15 000 vibrations in 0.50 minutes. Find its frequency.",
                  {"points": ["Convert: 0.50 min × 60 = 30 s",
                              "Formula: frequency = number of vibrations ÷ time",
                              "Insert: frequency = 15 000 ÷ 30 s",
                              "Fine-tune: 15 000 ÷ 30 = 500",
                              "Answer: frequency = 500 Hz"]},
                  "Divide by 0.50 instead of 30, and the answer is sixty times too big."]},
        {"kind": "card", "title": "Easy mistakes",
         "body": [{"mistakes": [
             ("A loud note is a high note.",
              "Loudness depends on the amplitude. Pitch depends on the frequency.", "WAVE-17"),
             ("A higher note travels faster.",
              "All sounds travel at the same speed through the same material.", "WAVE-18"),
             ("Turning the volume up adds vibrations each second.",
              "Turning it up makes each vibration bigger. The frequency stays the same.", "WAVE-19"),
             ("A hertz measures how loud something is.",
              "A hertz measures frequency. 1 Hz is one vibration each second.", "WAVE-20"),
             ("Put 0.50 minutes straight into the equation.",
              "Change minutes to seconds first. 0.50 min × 60 = 30 s."),
         ]}]},
    ],
    "key_fact": "Frequency is the number of vibrations each second, measured in hertz (Hz). "
                "A higher frequency gives a higher pitch, and a bigger amplitude gives a louder sound.",
    "deeper": [
        {"kind": "card", "title": "Octaves",
         "body": ["Double the frequency and you hear the same note, one octave higher.",
                  "220 Hz, 440 Hz and 880 Hz are all the note A.",
                  "Orchestras tune to an A of 440 Hz."]},
        {"kind": "card", "title": "Measuring loudness",
         "body": ["Loudness is measured in decibels, dB.",
                  "A whisper is about 30 dB. Normal talking is about 60 dB.",
                  "A road drill is about 100 dB."]},
    ],
    "try": {"label": "Wave Motion Lab", "href": "/simulations/physics/wave-motion-lab/"},
    "tutor_body": "Not sure which change sets the pitch and which sets the loudness?",
    "connects_heading": None,
    "ks4_becomes": "The wave equation, period, and reading frequency and amplitude from an oscilloscope trace.",
    "figures": [
        {"id": "p6-05-traces", "kind": "diagram", "status": "drawn", "art": "p6-sound-traces",
         "title": "Four sound traces",
         "desc": "Four screens, each with a wave trace on a dashed rest line, time going across. Top row, "
                 "same frequency, different amplitude: quiet is a short wave, loud is a tall wave, both with "
                 "three waves across the screen. Bottom row, same amplitude, different frequency: low pitch "
                 "has two waves across the screen, high pitch has five.",
         "caption": "Taller waves sound louder. More waves across the screen sound higher.",
         "data": {"rows": [
             {"title": "Same frequency, different amplitude",
              "panels": [{"label": "Quiet", "amp": 10, "waves": 3},
                         {"label": "Loud", "amp": 28, "waves": 3}]},
             {"title": "Same amplitude, different frequency",
              "panels": [{"label": "Low pitch", "amp": 22, "waves": 2},
                         {"label": "High pitch", "amp": 22, "waves": 5}]},
         ]}},
        {"id": "p6-05-triangle", "kind": "diagram", "status": "drawn", "art": "formula-triangle",
         "title": "The formula triangle for frequency",
         "desc": "A triangle split by a horizontal line. The number of vibrations, N, sits in the top part. "
                 "Frequency, f, in hertz, and time, t, in seconds, sit side by side in the bottom part, with "
                 "a multiplication sign between them.",
         "caption": "Cover the one you want. Side by side means multiply. One over the other means divide.",
         "data": {"top": {"s": "N", "name": "number of vibrations", "unit": "no unit",
                          "caption": "number of vibrations"},
                  "bottom": [{"s": "f", "name": "frequency", "unit": "Hz", "caption": "frequency in hertz"},
                             {"s": "t", "name": "time", "unit": "s", "caption": "time in seconds"}]}},
        {"id": "p6-05-count", "kind": "diagram", "status": "drawn", "art": "p6-vibration-count",
         "title": "Counting the vibrations of a 200 Hz tuning fork in 3.0 s",
         "desc": "At the top: 200 Hz means 200 vibrations every second. A wave trace on a screen is "
                 "cut into three equal slices, one for each second. Under each slice is the number 200. "
                 "A double arrow under the whole screen is labelled 3.0 s. Under it: 200 × 3.0 = 600, "
                 "then 600 vibrations.",
         "caption": "Each second holds 200 vibrations. Three seconds hold 600.",
         "data": {"heading": "200 Hz means 200 vibrations every second", "slices": 3,
                  "slice_label": "200", "span": "3.0 s",
                  "lines": ["200 × 3.0 = 600", "600 vibrations"]}},
        {"id": "p6-05-rate", "kind": "diagram", "status": "drawn", "art": "p6-vibration-count",
         "title": "Finding the frequency from 15 000 vibrations in 0.50 minutes",
         "desc": "At the top: 15 000 vibrations in 0.50 min. A wave trace on a screen is cut into 30 "
                 "thin slices, one for each second. The first slice is picked out and labelled 1 s: "
                 "500 vibrations. A double arrow under the whole screen is labelled 0.50 min = 30 s. "
                 "Under it: 15 000 ÷ 30 = 500, then frequency = 500 Hz.",
         "caption": "Share the vibrations out over 30 seconds. Each second gets 500.",
         "data": {"heading": "15 000 vibrations in 0.50 min", "slices": 30,
                  "mark": "1 s: 500 vibrations", "span": "0.50 min = 30 s",
                  "lines": ["15 000 ÷ 30 = 500", "frequency = 500 Hz"]}},
    ],
    "figure_caption": {"p6-05-traces": None, "p6-05-count": None, "p6-05-rate": None},   # the card text already says it
    "ladder_ticks": [
        ["Says the two are independent — changing one leaves the other as it was.",
         "Says the two are separate: changing one leaves the other as it was."],
        ["Gives a reason for at least one of them — for example that a shorter or lighter string can go to and fro more quickly.",
         "Gives a reason for one of them, such as a shorter or lighter string vibrating more quickly."],
    ],
    "ladder_feedback": {
        "recall": {
            0: "Dividing finds a frequency. Here the frequency is given, so multiply by the time.",
            2: "The number is right, but it is a count of vibrations. Hertz is per second.",
            3: "The 256 happens every second. Four seconds means 256 × 4, so multiply.",
        },
        "apply": {
            0: "Loudness does not change the speed. All sounds travel at the same speed in air.",
            1: "Wavelength does not set the speed. All sounds travel at the same speed in air.",
            3: "Frequency is how often the air is squashed. It does not change the speed.",
        },
    },
}
