"""P6 L5 — Frequency, pitch and loudness (QUANTITATIVE).

Authored against Claude Design's approved page,
`docs/ks3/design-reference/p6/p6-05-frequency-pitch-and-loudness.dc.html`.

Her page wins outright. The two guitar strings, the signal generator, the
oscilloscope, both worked examples and all four rungs are hers.

── ⚖️ MRB-204 · A TRIANGLE, AND IT IS THE UNIT-DEFINING PRODUCT ──────

`N = f × t` is a GENUINE PRODUCT, so `A = B × C` holds. It is also the
best possible first triangle for this topic, because it IS the definition
of the hertz: one vibration each second, so `t` seconds of it gives `f × t`
vibrations. The extra display line is exactly that unit pairing.

This is one of two triangles in P6; `p6-06`'s `d = v × t` is the other.

── ⚖️ RULED · THE SECOND SENTENCE IS ALWAYS PRESENT ──────────────────

Design's rule for this bench: every branch ends by saying what moving the
OTHER dial would do, with live figures. `WAVE-17` is *a loud note is a high
note*, and a bench that let a student move one dial, read one number and
stop would never confront it. `r_scope_trace` refuses a payload with no
`independence` sentence.

── ⚖️ RULED · THE WINDOW IS FIXED AND THE COUNT IS DERIVED ───────────

20 ms, always. The trace crowds as the frequency rises and the readout
count is `f × 0.02` rather than an authored number — which is what makes
the hertz mean something a student can see rather than a label.

── ⚠️ FOUR RAIL STOPS ────────────────────────────────────────────────

    s-hook · s-signal · s-formula · s-ladder

⚠️ **MRB-208** — the `s-formula` id goes on the attempt panel.

── ⚖️ FOUR MISCONCEPTIONS ────────────────────────────────────────────

    WAVE-17  a loud note is a high note
    WAVE-18  a higher note travels faster
    WAVE-19  turning the volume up adds vibrations each second
    WAVE-20  a hertz measures how loud something is
"""

LESSON = {
    "slug":  "frequency-pitch-and-loudness",
    "title": "Frequency, pitch and loudness",
    "discipline": "physics",
    "unit": "Waves and sound",
    "family": "QUANTITATIVE",

    "covers": ["KS3.P.SND.01a"],
    "touches": [],
    "beyond_statutory": False,
    "threads": [{"id": "waves", "level": 2}],
    "typical_year": 8,
    "typical_minutes": 60,

    "requires": ["sound-is-longitudinal"],
    "assumes": [],
    "references": ["how-sound-is-made", "hearing-and-auditory-range"],
    "ks4_links": [],

    "meta_description": "Two dials on a signal generator, and neither one "
                        "does anything the other does. One sets how high the "
                        "note is; one sets how loud. Getting them the wrong "
                        "way round is the commonest slip in this topic.",

    "big_question": "Two dials on a signal generator, and neither one does "
                    "anything the other one does. One sets how high the note "
                    "is. One sets how loud it is. Getting them the wrong way "
                    "round is the single most common slip in this topic.",

    "rail": [
        {"anchor": "s-hook",    "short": "GUITAR",
         "label": "Two strings, one guitar", "done_when": "committed"},
        {"anchor": "s-signal",  "short": "BENCH",
         "label": "Signal generator",  "done_when": "gate_and_a_control"},
        {"anchor": "s-formula", "short": "CFIFA",
         "label": "Triangle and five steps",
         "done_when": "attempt_checked"},
        {"anchor": "s-ladder",  "short": "LADDER",
         "label": "Mastery ladder",    "done_when": "ladder_complete"},
    ],

    "phenomenon": {
        "kind": "narrative",
        "title": "Two strings, one guitar, and only one of them is wrong.",
        "prompt": "Tighten a guitar string a little and the note goes up. "
                  "Pluck the same string harder and the note gets louder and "
                  "stays exactly where it was. Two different changes; two "
                  "different results; and students routinely swap them.",
        "commit": "A loudspeaker plays a steady note. You turn the volume up "
                  "and touch nothing else. What has changed about what the "
                  "cone is doing?",
        "options": [
            "The cone moves further and goes to and fro more times a second, "
            "because loudness needs both",
            "The cone pushes the sound out faster, so it reaches your ear "
            "sooner and seems louder",
            "The cone moves further from its rest place each time, and goes "
            "to and fro just as often",
            "The cone goes to and fro more times a second, without moving any "
            "further each time",
        ],
        "answer": 2,
        "reveal": "Louder means the cone moves FURTHER each time — a bigger "
                  "amplitude — and it makes that trip exactly as often as "
                  "before. The frequency is untouched, which is why the note "
                  "does not change. <strong>How far and how often are two "
                  "separate measurements</strong>, and neither one sets the "
                  "other.",
    },

    "misconceptions": [
        {"id": "WAVE-17",
         "statement": "A loud note is a high note.",
         "elicited_by": "s-hook",
         "confronted_by": "signal"},
        {"id": "WAVE-18",
         "statement": "A higher note travels faster.",
         "elicited_by": "s-ladder",
         "confronted_by": "s-think"},
        {"id": "WAVE-19",
         "statement": "Turning the volume up adds vibrations each second.",
         "elicited_by": "signal",
         "confronted_by": "signal"},
        {"id": "WAVE-20",
         "statement": "A hertz measures how loud something is.",
         "confronted_by": "s-think"},
    ],

    "core": [
        {"type": "hook", "id": "hook-commit", "anchor": "s-hook"},

        {"type": "explainer",
         "text": "A vibrating object goes to and fro over and over, and two "
                 "separate things can be measured about that. How "
                 "<em>often</em> it goes to and fro is its "
                 "<strong>frequency</strong>, measured in "
                 "<strong>hertz</strong>: 1 Hz is one complete vibration "
                 "each second. How <em>far</em> it moves each time is its "
                 "<strong>amplitude</strong>, measured in millimetres."},
        {"type": "explainer",
         "text": "Frequency decides the <strong>pitch</strong> you hear — a "
                 "higher frequency is a higher note. Amplitude decides the "
                 "<strong>loudness</strong> — a bigger movement pushes the "
                 "air harder and sounds louder. <strong>Neither one sets the "
                 "other.</strong> A quiet high note and a loud high note "
                 "have the same frequency; a quiet high note and a quiet low "
                 "note have the same amplitude."},

        # ── #s-signal · the signal generator ───────────────────────────
        {"type": "scope-trace",
         "id": "signal",
         "anchor": "s-signal",
         "eyebrow": "At the bench · a signal generator, a loudspeaker and an "
                    "oscilloscope",
         "heading": "Two dials. Two different things happen.",
         "progress": "Change a control to begin",
         "lead": "The oscilloscope draws how far the cone is from its rest "
                 "place against time, over a window of 20 milliseconds. Set "
                 "how often the cone goes to and fro, and set how far it "
                 "moves each time.",
         "window_ms": 20,
         "low_below": 200,
         "high_above": 600,
         "axis_label": "TIME — ONE WINDOW OF 20 ms",
         "gate": {
             "prompt": "Commit first. You double the frequency of the signal "
                       "and leave the volume dial alone. What happens to the "
                       "trace on the screen?",
             "options": [
                 "The trace moves across the screen twice as fast and looks "
                 "the same",
                 "Twice as many vibrations fit in the window, and the trace "
                 "gets twice as tall",
                 "Twice as many complete vibrations fit in the window, and "
                 "the trace stays the same height",
                 "The trace gets twice as tall and the number of vibrations "
                 "does not change",
             ],
             "answer": 2,
         },
         "freq": {"label": "How often the cone goes to and fro", "min": 50,
                  "max": 1000, "step": 50, "start": 300, "value": "300 Hz"},
         "amp": {"label": "How far the cone moves each time", "min": 2,
                 "max": 20, "step": 2, "start": 10, "value": "1.0 mm"},
         # ⚖️ THE SECOND SENTENCE, ALWAYS. Named with live figures.
         "independence": " Move the second dial to {other} mm and the trace "
                         "changes height and keeps exactly {cyc} vibrations "
                         "in the window: {f} Hz either way.",
         "branches": {
             "low": "{f} Hz is a low note — the cone goes to and fro {f} "
                    "times a second, and only {cyc} of those fit in this "
                    "20 ms window, so the trace is stretched out.",
             "middle": "{f} Hz sits in the middle of a singing voice, and "
                       "{cyc} complete vibrations fit in this 20 ms window.",
             "high": "{f} Hz is a high note, and {cyc} complete vibrations "
                     "are packed into this 20 ms window, so the trace is "
                     "crowded.",
         },
         "readouts": [
             {"id": "freq", "label": "Frequency",
              "sub": "complete vibrations each second"},
             {"id": "cycles", "label": "In this 20 ms window",
              "sub": "complete vibrations drawn"},
             {"id": "amp", "label": "How far the cone moves"},
             {"id": "verdict", "label": "What you would hear"},
         ]},

        {"type": "formula",
         "id": "frequency-rule",
         "eyebrow": "Writing it down · the shape of this relationship",
         "statement": "Number of vibrations = frequency × time",
         "triangle": {
             "eyebrow": "The triangle",
             "heading": "Cover the one you want",
             "aria_label": "A formula triangle. The number of vibrations N "
                           "sits above a dividing line; frequency f and time "
                           "t sit below it, multiplied together. Covering "
                           "one letter leaves the way to work it out.",
             "order": ["top", "left", "right"],
             "covered": "left",
             "top":   {"label": "N", "button": "Cover N",
                       "result": "N = f × t", "text": ""},
             "left":  {"label": "f", "button": "Cover f",
                       "result": "f = N ÷ t", "text": ""},
             "right": {"label": "t", "button": "Cover t",
                       "result": "t = N ÷ f", "text": ""},
             "close": {
                 "rule": "Two things side by side means multiply. One thing "
                         "over another means divide.",
                 "units": ["N · number of complete vibrations · no unit",
                           "f · frequency · Hz",
                           "t · time · s"],
                 "condition": "1 Hz is one complete vibration each second, "
                              "which is why the seconds and the hertz "
                              "cancel to leave a plain count.",
             },
         }},

        {"type": "worked-example", "id": "cfifa-freq-plain"},
        {"type": "worked-example", "id": "cfifa-freq-convert"},
        {"type": "check", "id": "your-turn-freq", "anchor": "s-formula"},

        {"type": "key-fact", "ref": "how-often-and-how-far"},

        {"type": "misconception", "id": "think-loud-is-high",
         "anchor": "s-think"},

        {"type": "quiz", "anchor": "s-ladder"},
        {"type": "summary", "id": "s-keynote"},
    ],

    "activities": [
        {"id": "cfifa-freq-plain",
         "kind": "worked-example",
         "demand": "calculate",
         "eyebrow": "Worked example · one step at a time",
         "heading": "A string is filmed and makes 1500 complete vibrations "
                    "in 5.0 seconds. What is its frequency?",
         "head_counter": {"format": "Step {n} of 5", "total": 5},
         "buttons": {"first": "Show the first step",
                     "next": "Show the next step",
                     "done": "All five shown",
                     "done_note": "Nothing needed converting there. Now the "
                                  "one that does."},
         "staged": True,
         "fifa": [
             {"letter": "C", "label": "Convert",
              "line": "1500 vibrations stays 1500 · 5.0 s stays 5.0 s",
              "note": "A hertz is counted per second, and the time is "
                      "already in seconds, so there is nothing to convert."},
             {"letter": "F", "label": "Formula",
              "line": "frequency = number of vibrations ÷ time",
              "note": "Cover f on the triangle: N sits over t, so you "
                      "divide."},
             {"letter": "I", "label": "Insert",
              "line": "frequency = 1500 vibrations ÷ 5.0 s",
              "note": "The count has no unit of its own; the second is what "
                      "makes it a hertz."},
             {"letter": "F", "label": "Fine-tune", "line": "1500 ÷ 5.0 = 300",
              "note": "Vibrations divided by seconds leaves vibrations each "
                      "second."},
             {"letter": "A", "label": "Answer", "line": "frequency = 300 Hz",
              "note": "Three hundred hertz, because 1 Hz is one vibration "
                      "each second."},
         ]},

        {"id": "cfifa-freq-convert",
         "kind": "worked-example",
         "demand": "calculate",
         "eyebrow": "Worked example · one step at a time",
         "heading": "A tuning fork makes 15 000 vibrations in 0.50 minutes. "
                    "What is its frequency?",
         "head_counter": {"format": "Step {n} of 5", "total": 5},
         "buttons": {"first": "Show the first step",
                     "next": "Show the next step",
                     "done": "All five shown",
                     "done_note": "Convert first, then the same four lines. "
                                  "Your turn below, on your own bench."},
         "staged": True,
         "fifa": [
             {"letter": "C", "label": "Convert",
              "line": "0.50 min × 60 = 30 s",
              "note": "A hertz is counted per second, so the minutes have to "
                      "become seconds first."},
             {"letter": "F", "label": "Formula",
              "line": "frequency = number of vibrations ÷ time",
              "note": "Cover f on the triangle: N sits over t, so you "
                      "divide."},
             {"letter": "I", "label": "Insert",
              "line": "frequency = 15 000 vibrations ÷ 30 s",
              "note": "The converted time goes in. The 0.50 never does."},
             {"letter": "F", "label": "Fine-tune",
              "line": "15 000 ÷ 30 = 500",
              "note": "Vibrations divided by seconds leaves vibrations each "
                      "second."},
             {"letter": "A", "label": "Answer", "line": "frequency = 500 Hz",
              "note": "Divide by 0.50 instead of 30 and the answer comes out "
                      "30 000 Hz — sixty times too big."},
         ]},

        {"id": "your-turn-freq",
         "kind": "p6-attempt",
         "demand": "calculate",
         "eyebrow": "Your turn · the same five steps",
         "rest": {"f": 300, "n": 900},
         "questions": [
             {"id": "q1", "tab": "Question 1",
              # ⊕ PHASE 3, 25 Aug 2026 — HER question, her lines and
              # her notes, with this engine's token names in place of
              # her state expressions.
              "head": "Your note: {f} Hz. How many complete vibrations in "
                      "3.0 seconds?",
              "lead": "Write all five lines before you check. The frequency "
                      "is the one your own bench is showing.",
              "steps": [
                  {"letter": "C", "label": "Convert",
                   "placeholder": "anything to convert?",
                   "line": "the count stays a count · the time is already "
                           "in seconds",
                   "note": "A hertz is counted per second, and the bench "
                           "times in seconds, so there is nothing to "
                           "convert."},
                  {"letter": "F", "label": "Formula",
                   "line": "N = f × t",
                   "note": "Cover N on the triangle: f and t sit side by "
                           "side, so you multiply."},
                  {"letter": "I", "label": "Insert",
                   "line": "N = {f} Hz × 3.0 s",
                   "note": "The frequency is the one your slider is set to; "
                           "the time is in seconds already."},
                  {"letter": "F", "label": "Fine-tune",
                   "line": "{f} × 3.0 = {n}",
                   "note": "Vibrations each second, multiplied by seconds, "
                           "leaves vibrations."},
                  {"letter": "A", "label": "Answer",
                   "line": "N = {n} vibrations",
                   "note": "A plain count, not a frequency — the seconds "
                           "have been used up."},
              ],
              "close": "The five lines above give {n} complete vibrations "
                       "in 3.0 s."},
             {"id": "q2", "tab": "Question 2",
              # ⊕ PHASE 3, 25 Aug 2026 — HER question, not one of
              # ours. The port had written a different second
              # question here with different numbers; hers is the
              # one a student is meant to meet.
              "head": "An insect wing beats 7200 times in 2.0 minutes. What "
                      "is its frequency?",
              "lead": "This one needs the Convert line to do some "
                      "work.",
              "steps": [
                  {"letter": "C", "label": "Convert",
                   "placeholder": "anything to convert?",
                   "line": "2.0 min × 60 = 120 s",
                   "note": "A hertz is counted per second, so the minutes "
                           "have to become seconds first."},
                  {"letter": "F", "label": "Formula",
                   "line": "frequency = number of vibrations ÷ time",
                   "note": "Cover f on the triangle: N sits over t, so you "
                           "divide."},
                  {"letter": "I", "label": "Insert",
                   "line": "frequency = 7200 beats ÷ 120 s",
                   "note": "The converted time goes in. The 2.0 never does."},
                  {"letter": "F", "label": "Fine-tune",
                   "line": "7200 ÷ 120 = 60",
                   "note": "Beats divided by seconds leaves beats each "
                           "second."},
                  {"letter": "A", "label": "Answer",
                   "line": "frequency = 60 Hz",
                   "note": "Divide by 2.0 instead of 120 and the answer "
                           "comes out 3600 Hz."},
              ],
              "close": "The five lines give 60 Hz. The whole question "
                       "turned on the first one."},
         ]},

        {"id": "think-loud-is-high",
         "kind": "predict",
         "demand": "explain",
         "targets": "WAVE-18",
         "statements": [
             {"quote": "A loud note is a high note.",
              "targets": "WAVE-18",
              "body": [
                  "Loud and high are answers to two different questions. "
                  "High is about how often the source goes to and fro; loud "
                  "is about how far it moves each time. A double bass "
                  "played hard is very loud and very low. A recorder played "
                  "gently is quiet and very high. On the bench above the "
                  "two dials do not talk to each other at all: move one and "
                  "the other reading does not budge. The confusion is "
                  "partly the fault of the English word big, which people "
                  "use for both, and partly of turning the volume up on a "
                  "speaker and hearing a thin sound get more present — "
                  "which is more of it, not more of a higher note.",
              ]},
             {"quote": "A higher note travels faster, which is why you hear "
                      "it first.",
              "targets": "WAVE-20",
              "body": [
                  "Every note in the same air travels at the same speed, "
                  "about 340 m/s, whatever its frequency. It has to: if "
                  "high notes outran low ones, a brass band a hundred "
                  "metres away would arrive scrambled, with the piccolo "
                  "half a bar ahead of the tuba, and it does not. What "
                  "frequency changes is how many times a second the air is "
                  "squeezed as the sound goes past, not how quickly the "
                  "squeezing travels.",
              ]},
         ]},
    ],

    "figures": [],

    "key_facts": [
        {"id": "how-often-and-how-far",
         "eyebrow": "Key fact",
         "ground": "card",
         "placement": "top-level",
         "text": "Frequency is the number of complete vibrations each second, "
                 "measured in hertz: 1 Hz is one vibration per second. "
                 "Frequency sets pitch and amplitude sets loudness, and the "
                 "two are independent — turning a note up does not raise it, "
                 "and raising it does not make it louder."},
    ],

    # ⚠️ MRB-278 · POSITION IS AUTHORED. This lesson takes indices 0 and 1.
    "ladder": {
        "recall": {
            "q": "A tuning fork of frequency 256 Hz is struck and rings for "
                 "4.0 seconds. How many complete vibrations does it make in "
                 "that time?",
            "options": [
                "64 vibrations — divide the frequency by the time",
                "1024 vibrations",
                "1024 Hz",
                "260 vibrations — add the four seconds on to the 256",
            ],
            "answer": 1,
            "feedback": {
                0: "Dividing is how you get a frequency when you already "
                   "have a count. Here the frequency is given, so each "
                   "second brings another 256 vibrations and you multiply.",
                2: "The arithmetic is right and the unit is wrong. Hertz "
                   "counts vibrations per second; this answer is a plain "
                   "count of vibrations, over a stated four seconds.",
                3: "Adding a time to a frequency is adding two different "
                   "quantities. The 256 is a rate: it happens again every "
                   "second, so four seconds means four helpings of it.",
            },
            "title": "Rung 1 · Calculate"},
        "apply": {
            "q": "A brass band plays a hundred metres away. A student says "
                 "the piccolo reaches you before the tuba, because higher "
                 "notes travel faster. Which statement is right?",
            "options": [
                "The tuba arrives first, because a louder, lower note "
                "carries more energy and pushes through the air more "
                "quickly, so the more energy a note is given the sooner it "
                "reaches you",
                "They arrive together, because the band members are all the "
                "same distance away.",
                "Both notes travel at about 340 m/s in the same air, so "
                "they arrive together — which is why the band sounds like a "
                "band and not a mess.",
                "The student is right: higher frequency means the wave gets "
                "along faster, so the piccolo arrives first.",
            ],
            "answer": 2,
            "feedback": {
                0: "The verdict is reversed and the rule is still wrong. "
                   "Loudness is amplitude, and amplitude does not change "
                   "the speed either.",
                1: "The verdict is right and the reason does not do the "
                   "work. Even from exactly the same spot the two notes "
                   "would only arrive together if they travelled at the "
                   "same speed, and that is the fact being tested.",
                3: "Frequency is how often the air is squeezed as the sound "
                   "goes past, not how fast the squeezing travels. If the "
                   "two differed, distant music would arrive scrambled.",
            },
            "title": "Rung 2 · The one that catches people"},
        "explain": {
            "q": "A loudspeaker plays a note. Explain what has to change "
                 "about the cone to make the note higher, and what has to "
                 "change to make it louder.",
            "field_label": "Your explanation",
            "placeholder": "To make the note higher, the cone…",
            "success": [
                "Says a higher note needs the cone to go to and fro more "
                "times each second.",
                "Names that as a higher frequency, measured in hertz.",
                "Says a louder note needs the cone to move further from its "
                "rest place each time.",
                "Names that as a bigger amplitude.",
                "Says the two are independent — changing one leaves the "
                "other as it was.",
            ],
            "title": "Rung 3 · Explain"},
        "produce": {
            "q": "On a guitar, the thin strings sound higher than the thick "
                 "ones, tightening a string raises its note, and pressing "
                 "it down at a fret raises it too. Plucking any of them "
                 "harder does none of those things. Explain what all three "
                 "of the first changes have in common, and why the fourth "
                 "is different.",
            "field_label": "Your answer",
            "placeholder": "A thinner, tighter or shorter string…",
            "success": [
                "Says all three of the first changes make the string "
                "vibrate more times each second.",
                "Says that is a higher frequency, which is heard as a "
                "higher pitch.",
                "Gives a reason for at least one of them — for example that "
                "a shorter or lighter string can go to and fro more "
                "quickly.",
                "Says plucking harder moves the string further from its "
                "rest place.",
                "Says that is a bigger amplitude, heard as louder, and that "
                "it leaves the number of vibrations each second unchanged.",
            ],
            "title": "Rung 4 · Take it somewhere new"},
    },

    "key_note": "Frequency is the number of complete vibrations each second, "
                "measured in hertz, where 1 Hz is one vibration per second. "
                "Frequency sets the pitch: more vibrations each second is a "
                "higher note. Amplitude is how far the source moves from its "
                "rest place each time, and it sets the loudness. The two are "
                "independent, and every frequency of sound travels at the "
                "same speed through the same material.",

    "stretch": [
        # ⊕ PHASE 3 REVERT, 25 Aug 2026 — Design's *Going further*,
        # verbatim, both paragraphs. What had been here was different
        # content of this lane's own: good physics, and not hers, and
        # "a different example" is not a defect anyone can name.
        {"id": "the-numbers-behind-musical",
         "type": "explainer",
         "text": "The numbers behind musical pitch are tidier than they "
                 "look. Double a frequency and you get the same note one "
                 "octave higher: 220 Hz, 440 Hz and 880 Hz are all the note "
                 "A. The concert A that orchestras tune to is fixed at 440 "
                 "Hz by international agreement, which is a convention "
                 "rather than a fact about the universe — "
                 "eighteenth-century instruments were tuned lower, and a "
                 "few orchestras still play at 415 Hz to suit the music."},
        {"id": "loudness-is-the-awkward",
         "type": "explainer",
         "text": "Loudness is the awkward one to put a number on, because "
                 "your ear does not respond in proportion. Doubling the "
                 "amplitude does not sound twice as loud, and doubling it "
                 "again adds much less than the first doubling did. That is "
                 "why loudness is measured on the decibel scale, which is "
                 "built on multiplying rather than adding: every 10 dB is "
                 "ten times the energy arriving, and roughly twice as loud "
                 "to a listener. A whisper sits near 30 dB, a conversation "
                 "near 60 dB, and a road drill near 100 dB — a million "
                 "times the energy of the whisper, and nothing like a "
                 "million times as loud."},
    ],

    "support": [],

    "vocabulary": [
        {"term": "frequency",
         "definition": "How many complete vibrations happen each second, "
                       "measured in hertz. It decides the pitch."},
        {"term": "hertz",
         "definition": "The unit of frequency, written Hz. 1 Hz is one "
                       "complete vibration each second."},
        {"term": "pitch",
         "definition": "How high or low a note sounds. Set by the frequency "
                       "and by nothing else."},
        {"term": "loudness",
         "definition": "How loud a note sounds. Set by the amplitude — how "
                       "far the source moves each time."},
    ],

    "tutor": {
        "anchor": "s-signal",
        "prompt": "Ask Mr Badmus AI",
        "body": "Not sure which dial does which?",
        "cta": "Ask about this lesson"},

    "ks4_becomes": "Period as the reciprocal of frequency, the wave equation, "
                   "the audible range, and reading frequency and amplitude "
                   "off an oscilloscope trace.",

    "convention_note": "The bench is a teaching model. The trace is a graph "
                       "of the cone's displacement against time over a fixed "
                       "20 millisecond window, drawn to one scale throughout: "
                       "44 pixels per millisecond across, and 45 pixels per "
                       "millimetre up. The cone is treated as making one pure "
                       "frequency, which no real instrument does — a real "
                       "guitar string or voice puts out a mixture, and that "
                       "mixture is what makes a violin and a flute at the "
                       "same pitch sound different. The words quiet, moderate "
                       "and loud are bands set for this bench and are not "
                       "decibel measurements. The speed of sound in air is "
                       "taken as about 340 m/s, which is the value at about "
                       "20 degrees Celsius and rises with temperature.",

    "ws": [],
}
