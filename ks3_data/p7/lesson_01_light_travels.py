"""P7 L1 — Light travels (MODEL).

Authored against Claude Design's approved page,
`docs/ks3/design-reference/p7/p7-01-light-travels.dc.html`.

Her page wins outright. The lightning hook, the flash-and-bang bench, the
comparison table, both worked examples, both attempt questions and all
four rungs are hers, ported from her JavaScript constants rather than
from her HTML — a `.dc.html` renders every one of them from a `{{ }}`
hole and an HTML comparison would have reported a match against anything.

── ⚖️ MRB-204 · A TRIANGLE, AND THE STATUTE ASKS FOR IT ──────────────

`d = c × t` is a genuine product and the speed of light is the statutory
content of `LGT.02`. The triangle is what makes 300 000 000 usable.

⚠️ **HER FLAG 5: `d = v × t` APPEARS THREE TIMES ACROSS TWO UNITS** —
`p6-06` teaches it for sound, `p6-07` uses it as given data, and this
page teaches it again for light. No lesson assumes the others; each
states the relationship from nothing and carries the others as edges.
She asks a reviewer to check it reads as reinforcement rather than as a
missing single-source ruling. Nothing here changes it.

── ⚖️ RULED · THE VACUUM REPORTS "IT NEVER ARRIVES" FOR THE BANG ─────

Not a very large time and not a very small number. The light reading is
UNCHANGED by taking the air away, which is the whole lesson: one of the
two waves needs particles and the other does not. Her branch names the
air time for the same gap so the difference is never implicit.

── ⚖️ HER HEDGES, AND THEY ARE LOAD-BEARING ─────────────────────────

300 000 000 m/s is stated as a ROUNDED figure; the exact 299 792 458 m/s
is in the legal line and in *Going further*, where the 1983 definition of
the metre explains why it is exact rather than measured. The speed of
sound is "about 340 m/s" at "around 20 degrees Celsius".

── ⚠️ FOUR RAIL STOPS ────────────────────────────────────────────────

    s-hook · s-race · s-formula · s-ladder

⚠️ **MRB-208** — the `s-formula` id goes on the attempt panel, because
Design's own `DONE` for it reads `s.buildOpen`.

⊕ **HER RAIL LABEL SAID "four steps" AND THE BLOCK BELOW IT IS FIVE.**
See `DEPARTURES-P7.md` row 1: the page contradicts its own instrument,
which says "All five shown" and "the same five steps".

── ⚖️ FOUR MISCONCEPTIONS ────────────────────────────────────────────

    LIGHT-01  light is instant — it takes no time at all
    LIGHT-02  space is empty, so light must be slowed down by it
    LIGHT-03  light is longitudinal, like sound
    LIGHT-04  the thunder is made a moment after the flash

⚠️ MRB-278 · POSITION IS AUTHORED. This lesson's two marked rungs take
indices 2 and 3. Design's own `RUNGS` put the correct option at index 0
on all fourteen marked rungs in P7, which is the answer-position defect
`verify_ks3` fails a unit for. Every option's TEXT and every correction
is hers and untouched; only the ORDER changes, and the distractors keep
their relative order. Engine policy, recorded here rather than in the
departure register.
"""

LESSON = {
    "slug":  "light-travels",
    "title": "Light travels",
    "discipline": "physics",
    "unit": "Light",
    "family": "MODEL",

    "covers": ["KS3.P.LGT.01", "KS3.P.LGT.02"],
    "touches": ["KS3.WS.ANA.01"],
    "beyond_statutory": False,
    "threads": [{"id": "waves", "level": 3}],
    "typical_year": 8,
    "typical_minutes": 60,

    "requires": ["ultrasound-at-work"],
    "assumes": [],
    "references": ["sound-needs-a-medium", "sound-is-longitudinal",
                   "refraction"],
    "ks4_links": [],

    "meta_description": "A flash and a bang leave the same hillside at the "
                        "same instant and arrive six seconds apart. One of "
                        "them needed air to get to you.",

    "big_question": "A flash and a bang leave the same hillside at the same "
                    "instant and arrive six seconds apart. One of them needed "
                    "air to get to you. The other did not need anything.",

    "rail": [
        {"anchor": "s-hook",    "short": "STORM",
         "label": "Flash, then thunder",     "done_when": "committed"},
        {"anchor": "s-race",    "short": "RACE",
         "label": "A flash and a bang",      "done_when": "gate_and_a_control"},
        {"anchor": "s-formula", "short": "FIFA",
         "label": "Triangle and five steps", "done_when": "attempt_checked"},
        {"anchor": "s-ladder",  "short": "LADDER",
         "label": "Mastery ladder",          "done_when": "ladder_complete"},
    ],

    "phenomenon": {
        "kind": "narrative",
        "title": "You see the strike. You wait for the bang.",
        "prompt": "Lightning hits a hillside two kilometres away. The flash "
                  "is instant. The thunder takes about six seconds. It was "
                  "one event: the flash and the bang left the same place at "
                  "the same moment.",
        "commit": "Why does one of them get to you six seconds before the "
                  "other?",
        "options": [
            "The light is much faster than the sound, so it covers the same "
            "two kilometres far sooner",
            "The thunder is made a few seconds after the flash, further down "
            "the strike",
            "The sound has to travel round obstacles, so it takes a longer "
            "route",
            "The light goes straight to you and the sound spreads out in "
            "every direction first",
        ],
        "answer": 0,
        "reveal": "One event, two messengers, wildly different speeds. Light "
                  "covers two kilometres in about seven millionths of a "
                  "second; sound in air needs about six seconds for the same "
                  "trip. Counting the gap is a real method: every three "
                  "seconds between flash and bang is roughly one kilometre.",
    },

    "misconceptions": [
        {"id": "LIGHT-01",
         "statement": "Light is instant — it takes no time at all.",
         "elicited_by": "s-hook",
         "confronted_by": "s-think"},
        {"id": "LIGHT-02",
         "statement": "Space is empty, so light has nothing to travel in and "
                      "must be slowed down by it.",
         "elicited_by": "s-ladder",
         "confronted_by": "s-think"},
        {"id": "LIGHT-03",
         "statement": "Light is longitudinal, like sound is.",
         "confronted_by": "light-vs-waves"},
        {"id": "LIGHT-04",
         "statement": "The thunder is made a moment after the flash, so the "
                      "two did not start together.",
         "elicited_by": "s-hook",
         "confronted_by": "s-hook"},
    ],

    "core": [
        {"type": "hook", "id": "hook-commit", "anchor": "s-hook"},

        {"type": "explainer",
         "text": "Light is a wave, and much of what you know about waves on "
                 "water and about sound carries straight over. It has a "
                 "wavelength and an amplitude, it carries energy from one "
                 "place to another without carrying material with it, it "
                 "reflects off surfaces and it can be absorbed. Like a water "
                 "wave and unlike sound, it is <strong>transverse</strong>."},
        {"type": "explainer",
         "text": "Two things about it are genuinely different, and both "
                 "matter. First, <strong>light needs no medium</strong>. "
                 "Sound is particles shoving their neighbours, so it stops "
                 "dead in a vacuum; light crosses empty space perfectly well, "
                 "which is why the Sun warms a planet 150 million kilometres "
                 "away across nothing at all. Second, light is very much "
                 "faster. In a vacuum it travels at <strong>300 000 000 "
                 "metres every second</strong> — close to a million times the "
                 "speed of sound in air — and it is the fastest anything can "
                 "go."},
        {"type": "explainer",
         "text": "Light does travel in straight lines through anything even "
                 "and unchanging, which is why shadows have sharp edges and "
                 "why a ray drawn with a ruler is a good enough model for "
                 "most of what light does."},

        # ── #s-race · a flash and a bang, set off together ─────────────
        {"type": "two-speed-race",
         "id": "race",
         "anchor": "s-race",
         "eyebrow": "At the bench · a flash and a bang, set off together",
         "heading": "Same start. Two arrivals.",
         "head_counter": {"format": "Both controls live",
                          "zero": "Change a control to begin", "total": 1},
         "prompt": "A lamp and a starting pistol fire at the same instant, "
                   "and two detectors at the far end record when each "
                   "arrives. Set how far away they are, and set what is in "
                   "between.",
         "gate": {
             "prompt": "Commit first. The same flash and bang are set off on "
                       "the Moon, where there is no air. What do the two "
                       "detectors record?",
             "options": [
                 "Both arrive, with the light first, exactly as on Earth",
                 "The light arrives and the bang never does, because there "
                 "is no air to carry it",
                 "Neither arrives, because a vacuum stops all waves",
                 "They arrive together, because with no air there is nothing "
                 "to slow the sound down",
             ],
             "answer": 1,
         },
         # Design's own model constants, and her own log axis: the slider is
         # 0–100 and the gap is 10^(s/100 × 5) metres, so 1 m to 100 km over
         # five decades. Her decade labels are literal text on the drawing.
         "c": 300000000,
         "v_sound": 340,
         "dist": {"label": "How far away the detectors are",
                  "min": 0, "max": 100, "step": 1, "start": 60},
         "decades": 5,
         "decade_labels": ["1 m", "10 m", "100 m", "1 km", "10 km",
                           "100 km"],
         "axis_label": "EACH MARK IS TEN TIMES THE ONE BEFORE IT",
         "light_label": "LIGHT",
         "sound_label": "SOUND",
         "med_label": "What is in between",
         "media": [
             {"id": "air", "label": "Air", "vacuum": False,
              "caption": "ordinary air at about 20 °C",
              "sound_sub": "at about 340 m/s in air"},
             {"id": "vacuum", "label": "Vacuum", "vacuum": True,
              "caption": "nothing at all in between",
              "sound_sub": "no particles to pass it on"},
         ],
         "readouts": [
             {"id": "gap", "label": "The gap", "sub": "—"},
             {"id": "light", "label": "The light arrives after",
              "sub": "at 300 000 000 m/s"},
             {"id": "sound", "label": "The bang arrives after", "sub": "—"},
             {"id": "verdict", "label": "Which wins, and by how much"},
         ],
         # Two branches, keyed to whether there is a medium. Her vacuum
         # branch names the air time for the SAME gap, so the difference is
         # never left implicit.
         "branches": {
             "air": "Over {dist} of air the light takes {tlight} and the "
                    "bang takes {tsound}, a gap of {tgap}. Light is close to "
                    "a million times faster, so the light time barely "
                    "changes on this scale while the sound time climbs with "
                    "every step. Take the air away and the light reading is "
                    "unchanged and the bang stops arriving.",
             "vacuum": "With nothing in the gap the light crosses {dist} in "
                       "{tlight} and the bang never arrives at all — not "
                       "faintly, not late. Put air in the same gap and the "
                       "bang lands after {tsound}. That single difference is "
                       "what separates light from every wave in matter.",
         }},

        # ── #s-figure · light beside the waves you can see ─────────────
        #
        # Her table sits between the bench and the formula block and takes
        # no rail stop: her RAIL for this page is four entries and the
        # figure is not among them.
        {"type": "light-band",
         "id": "light-vs-waves",
         "anchor": "s-figure",
         "eyebrow": "The figure",
         "heading": "Light beside the waves you can see",
         "table": {
             "aria_label": "A table comparing waves on water, sound and "
                           "light on six properties. The first three rows "
                           "are the same for all three; the last three "
                           "differ, and the row that does the most work is "
                           "whether the wave needs a material to travel "
                           "through.",
             "columns": ["", "Waves on water", "Sound", "Light"],
             "rows": [
                 ["Carries energy without carrying material",
                  "Yes", "Yes", "Yes"],
                 ["Has a wavelength and an amplitude", "Yes", "Yes", "Yes"],
                 ["Reflects, and can be absorbed", "Yes", "Yes", "Yes"],
                 ["Transverse or longitudinal", "Transverse",
                  "<strong>Longitudinal</strong>", "Transverse"],
                 ["Needs a material to travel through", "Yes — water",
                  "Yes — any solid, liquid or gas",
                  "<strong>No — crosses a vacuum</strong>"],
                 ["How fast", "A few m/s", "About 340 m/s in air",
                  "<strong>300 000 000 m/s in a vacuum</strong>"],
             ],
         },
         "close": "Three rows the same, three rows different. The row that "
                  "does the most work is the fifth: needing a material is "
                  "what makes sound a wave in matter and light a wave that "
                  "does not care."},

        {"type": "formula",
         "id": "light-speed-rule",
         "eyebrow": "Writing it down · the shape of this relationship",
         "statement": "Distance = speed of light × time",
         "triangle": {
             "eyebrow": "The triangle",
             "heading": "Cover the one you want",
             "aria_label": "A formula triangle. The distance d sits above a "
                           "dividing line; the speed of light c and the time "
                           "t sit below it, multiplied together. Covering "
                           "one letter leaves the way to work it out.",
             "order": ["top", "left", "right"],
             "covered": "top",
             "top":   {"label": "d", "button": "Cover d",
                       "result": "d = c × t", "text": ""},
             "left":  {"label": "c", "button": "Cover c",
                       "result": "c = d ÷ t", "text": ""},
             "right": {"label": "t", "button": "Cover t",
                       "result": "t = d ÷ c", "text": ""},
             "close": {
                 "rule": "Two things side by side means multiply. One thing "
                         "over another means divide.",
                 "units": ["d · distance the light travels · m",
                           "c · speed of light in a vacuum · m/s",
                           "t · time it takes · s"],
                 "condition": "The speed is the one for a vacuum, and air is "
                              "close enough to make no difference at this "
                              "scale.",
             },
         }},

        {"type": "worked-example", "id": "cfifa-light-plain-p7"},
        {"type": "worked-example", "id": "cfifa-light-convert-p7"},
        {"type": "check", "id": "your-turn-light", "anchor": "s-formula"},

        {"type": "key-fact", "ref": "light-needs-nothing"},

        {"type": "misconception", "id": "think-light-is-instant",
         "anchor": "s-think"},

        {"type": "quiz", "anchor": "s-ladder"},
        {"type": "summary", "id": "s-keynote"},
    ],

    "activities": [
        {"id": "cfifa-light-plain-p7",
         "kind": "worked-example",
         "demand": "calculate",
         "eyebrow": "Worked example · one step at a time",
         "heading": "Light from the Sun takes 500 s to reach the Earth. "
                    "Light travels at 300 000 000 m/s. How far away is the "
                    "Sun?",
         "head_counter": {"format": "Step {n} of 5", "total": 5},
         "buttons": {"first": "Show the first step",
                     "next": "Show the next step",
                     "done": "All five shown",
                     "done_note": "Nothing needed converting there. Now the "
                                  "one that does."},
         "staged": True,
         "fifa": [
             {"letter": "C", "label": "Convert",
              "line": "300 000 000 m/s stays as it is · 500 s stays 500 s",
              "note": "The speed is in metres per second and the time is in "
                      "seconds, so there is nothing to convert."},
             {"letter": "F", "label": "Formula",
              "line": "distance = speed of light × time",
              "note": "Cover d on the triangle: c and t sit side by side, so "
                      "you multiply."},
             {"letter": "I", "label": "Insert",
              "line": "distance = 300 000 000 m/s × 500 s",
              "note": "The speed is the one for a vacuum, and space is very "
                      "close to one."},
             {"letter": "F", "label": "Fine-tune",
              "line": "300 000 000 × 500 = 150 000 000 000",
              "note": "Metres per second multiplied by seconds leaves "
                      "metres."},
             {"letter": "A", "label": "Answer",
              "line": "distance = 150 000 000 000 m",
              "note": "A hundred and fifty billion metres, which is 150 "
                      "million kilometres."},
         ]},

        {"id": "cfifa-light-convert-p7",
         "kind": "worked-example",
         "demand": "calculate",
         "eyebrow": "Worked example · one step at a time",
         "heading": "Light takes 8.0 minutes to reach us from the Sun. How "
                    "far away is it?",
         "head_counter": {"format": "Step {n} of 5", "total": 5},
         "buttons": {"first": "Show the first step",
                     "next": "Show the next step",
                     "done": "All five shown",
                     "done_note": "Convert first, then the same four lines. "
                                  "Your turn below."},
         "staged": True,
         "fifa": [
             {"letter": "C", "label": "Convert",
              "line": "8.0 min × 60 = 480 s",
              "note": "The speed is metres per second, so the time has to be "
                      "in seconds before it can multiply."},
             {"letter": "F", "label": "Formula",
              "line": "distance = speed of light × time",
              "note": "Cover d on the triangle: c and t sit side by side, so "
                      "you multiply."},
             {"letter": "I", "label": "Insert",
              "line": "distance = 300 000 000 m/s × 480 s",
              "note": "The converted time goes in. The 8.0 never does."},
             {"letter": "F", "label": "Fine-tune",
              "line": "300 000 000 × 480 = 144 000 000 000",
              "note": "Metres per second multiplied by seconds leaves "
                      "metres."},
             {"letter": "A", "label": "Answer",
              "line": "distance = 144 000 000 000 m",
              "note": "Insert 8.0 instead of 480 and the Sun comes out 2.4 "
                      "billion metres away — sixty times too close."},
         ]},

        {"id": "your-turn-light",
         "kind": "p7-attempt",
         "demand": "calculate",
         "eyebrow": "Your turn · the same five steps",
         "check_label": "Check your working",
         "reveal_label": "The five lines · tick what you had",
         # The bench's opening state: the slider rests at 60, which is
         # 10^3 = 1000 m of air. `dgrp` is the distance with Design's own
         # narrow-no-break-space grouping, `texp` is her `toExponential(2)`
         # and `tlight` / `tsound` are her `fmtT`.
         "rest": {"dlabel": "1.0 km", "dgrp": "1000", "texp": "3.33e-6",
                  "tlight": "3.33 millionths of a second",
                  "tsound": "2.94 s"},
         "questions": [
             {"id": "q1", "tab": "Question 1",
              "head": "Your gap: {dlabel}, which is {dgrp} m.",
              "lead": "Write each line out yourself — starting by deciding "
                      "whether anything needs converting. Then check your "
                      "working and tick the lines you had.",
              "steps": [
                  {"letter": "C", "label": "Convert",
                   "placeholder": "anything to convert?",
                   "line": "the speed is in m/s · the time is already in "
                           "seconds",
                   "note": "Metres per second multiplied by seconds gives "
                           "metres, so there is nothing to convert."},
                  {"letter": "F", "label": "Formula",
                   "line": "t = d ÷ c",
                   "note": "Cover t on the triangle: d sits over c, so you "
                           "divide."},
                  {"letter": "I", "label": "Insert",
                   "line": "t = {dgrp} m ÷ 300 000 000 m/s",
                   "note": "The gap comes from your slider; the speed is "
                           "light in a vacuum, and air is close enough to "
                           "make no difference here."},
                  {"letter": "F", "label": "Fine-tune",
                   "line": "{dgrp} ÷ 300 000 000 = {texp}",
                   "note": "Metres divided by metres per second leaves "
                           "seconds."},
                  {"letter": "A", "label": "Answer",
                   "line": "t = {tlight}",
                   "note": "Over the same gap the bang would take {tsound} "
                           "through air."},
              ],
              "close": "The five lines above give {tlight} for the light "
                       "across {dlabel}."},
             {"id": "q2", "tab": "Question 2",
              "head": "Light from the Moon reaches the Earth in 1300 ms. "
                      "How far away is the Moon?",
              "lead": "Write each line out yourself — starting by deciding "
                      "whether anything needs converting. Then check your "
                      "working and tick the lines you had.",
              "steps": [
                  {"letter": "C", "label": "Convert",
                   "placeholder": "anything to convert?",
                   "line": "1300 ms ÷ 1000 = 1.3 s",
                   "note": "The speed is metres per second, and a "
                           "millisecond is a thousandth of a second."},
                  {"letter": "F", "label": "Formula",
                   "line": "distance = speed of light × time",
                   "note": "Cover d on the triangle: c and t sit side by "
                           "side, so you multiply."},
                  {"letter": "I", "label": "Insert",
                   "line": "distance = 300 000 000 m/s × 1.3 s",
                   "note": "The converted time goes in. The 1300 never "
                           "does."},
                  {"letter": "F", "label": "Fine-tune",
                   "line": "300 000 000 × 1.3 = 390 000 000",
                   "note": "Metres per second multiplied by seconds leaves "
                           "metres."},
                  {"letter": "A", "label": "Answer",
                   "line": "distance = 390 000 000 m",
                   "note": "Insert 1300 instead of 1.3 and the Moon comes "
                           "out a thousand times further away than the "
                           "Sun."},
              ],
              "close": "The five lines give 390 000 000 m — 390 000 km, "
                       "which is close to the real figure."},
         ]},

        {"id": "think-light-is-instant",
         "kind": "predict",
         "demand": "explain",
         "targets": "LIGHT-01",
         "statements": [
             {"quote": "Light is instant — it takes no time at all.",
              "targets": "LIGHT-01",
              "body": [
                  "It is fast, not instant, and over a room the difference "
                  "is undetectable. Over a distance it matters a great "
                  "deal: the Moon is 1.3 seconds away, the Sun 8 minutes "
                  "and 20 seconds, and a radio command to a spacecraft at "
                  "Mars takes several minutes to arrive, which is why they "
                  "cannot be flown by joystick. Because nothing beats the "
                  "speed of light, looking at anything far away is looking "
                  "into the past — the Sun you can see is the Sun of eight "
                  "minutes ago, and if it went out you would have no way of "
                  "knowing for eight minutes.",
              ]},
             {"quote": "Space is empty, so light has nothing to travel in "
                       "and must be slowed down by it.",
              "targets": "LIGHT-02",
              "body": [
                  "Empty is exactly the condition light likes. Sound needs "
                  "particles because it is particles shoving their "
                  "neighbours; light is not made of pushed material at all, "
                  "and a material is something for it to be slowed and "
                  "absorbed by rather than something it needs. Light is "
                  "fastest in a vacuum and slower in glass or water, which "
                  "is the opposite of the pattern for sound.",
              ]},
         ]},
    ],

    "figures": [],

    "key_facts": [
        {"id": "light-needs-nothing",
         "eyebrow": "Key fact",
         "ground": "card",
         "placement": "top-level",
         "text": "Light is a transverse wave that needs no material to travel "
                 "through, and in a vacuum it moves at 300 000 000 m/s — "
                 "close to a million times the speed of sound in air. Like "
                 "every wave it carries energy without carrying material, and "
                 "it reflects and can be absorbed. Distance = speed of light "
                 "× time."},
    ],

    # ⚠️ MRB-278 · POSITION IS AUTHORED. This lesson takes indices 2 and 3.
    "ladder": {
        "recall": {
            "q": "The Moon is about 384 000 000 m away. Light travels at "
                 "300 000 000 m/s. How long does light from the Moon take to "
                 "reach us?",
            "options": [
                "About 0.8 s — divide the speed by the distance",
                "About 115 000 000 000 000 000 s — multiply the distance by "
                "the speed",
                "About 1.3 s",
                "About 1.3 m/s",
            ],
            "answer": 2,
            "feedback": {
                0: "That is the calculation upside down. Cover t on the "
                   "triangle and d sits over c, so the distance is the one "
                   "being divided.",
                1: "Multiplying gives a distance back when you already have "
                   "one. To find a time you share the distance out at so "
                   "many metres per second, so you divide.",
                3: "The number is right and the unit is wrong. Metres "
                   "divided by metres per second leaves seconds, and the "
                   "question asked how long.",
            },
            "title": "Rung 1 · Calculate"},
        "apply": {
            "q": "A student says light must be slower in space than in air, "
                 "because space is empty and there is nothing to carry it. "
                 "Which statement is right?",
            "options": [
                "The student is right: a wave needs something to travel in, "
                "so light struggles in a vacuum and speeds up in air — the "
                "more material there is, the better it carries.",
                "The speed of light is the same everywhere, because it is a "
                "constant of nature.",
                "Light is faster in space, because there is no gravity there "
                "to hold it back.",
                "Light is fastest in a vacuum and slower in air, water or "
                "glass — it needs no material, and a material only gets in "
                "its way.",
            ],
            "answer": 3,
            "feedback": {
                0: "That is true of sound, which is particles shoving their "
                   "neighbours. Light is not, and it crosses empty space at "
                   "its full speed.",
                1: "The speed of light in a vacuum is a constant, and light "
                   "genuinely does travel more slowly through glass and "
                   "water. That slowing is what makes refraction happen.",
                2: "The verdict is right and the reason is not. What slows "
                   "light is passing through a material, and space has "
                   "almost none of it.",
            },
            "title": "Rung 2 · The one that catches people"},
        "explain": {
            "q": "Lightning strikes two kilometres away. Explain why you see "
                 "the flash almost at once but wait about six seconds for "
                 "the thunder, naming the speed of each.",
            "field_label": "Your explanation",
            "placeholder": "The flash and the bang start together, but…",
            "success": [
                "Says the flash and the bang leave at the same moment.",
                "Gives the speed of light as 300 000 000 m/s, or says it is "
                "enormously faster.",
                "Gives the speed of sound in air as about 340 m/s.",
                "Says light covers the 2000 m in a tiny fraction of a "
                "second.",
                "Works out or states that sound takes about six seconds to "
                "cover the same 2000 m.",
            ],
            "title": "Rung 3 · Explain"},
        "produce": {
            "q": "A rover on Mars is being driven from Earth. At its "
                 "closest, Mars is about 55 000 000 000 m away. Work out how "
                 "long a command takes to reach it, then explain why the "
                 "rover has to be able to stop itself rather than being "
                 "steered live.",
            "field_label": "Your answer",
            "placeholder": "Time = distance ÷ speed of light…",
            "success": [
                "Uses time = distance ÷ speed of light.",
                "Gets about 183 s, or about 3 minutes, with the unit.",
                "Says the reply from the rover takes the same time again, so "
                "a round trip is about six minutes.",
                "Says a driver on Earth is always seeing where the rover was "
                "several minutes ago.",
                "Concludes that the rover must detect an obstacle and stop "
                "on its own, because a command sent on seeing one would "
                "arrive far too late.",
            ],
            "title": "Rung 4 · Take it somewhere new"},
    },

    "key_note": "Light is a transverse wave. Like waves on water and like "
                "sound it carries energy without carrying material, has a "
                "wavelength and an amplitude, reflects and can be absorbed. "
                "Unlike sound, it needs no material at all and crosses a "
                "vacuum, which is how sunlight reaches the Earth. In a vacuum "
                "it travels at 300 000 000 m/s, close to a million times the "
                "speed of sound in air, and distance = speed of light × time.",

    "stretch": [
        {"id": "every-telescope-is-a-time-machine",
         "type": "explainer",
         "text": "Because light takes time, every telescope is a time "
                 "machine. Looking at the Moon is looking 1.3 seconds into "
                 "the past, at the Sun about eight minutes, and at the "
                 "nearest star beyond the Sun about four years. Some of the "
                 "galaxies photographed by the largest telescopes are seen as "
                 "they were before the Earth existed, and a few of the stars "
                 "visible tonight may already have died — the news is still "
                 "in transit."},
        {"id": "the-metre-is-defined-by-the-second",
         "type": "explainer",
         "text": "The number 300 000 000 m/s is a rounded one, and the exact "
                 "figure is stranger than it looks. Since 1983 the metre has "
                 "been <em>defined</em> as the distance light travels in "
                 "1/299 792 458 of a second, which makes the speed of light "
                 "exactly 299 792 458 m/s by definition rather than by "
                 "measurement. It cannot be measured more accurately, because "
                 "measuring it more accurately would only make the metre more "
                 "accurate."},
    ],

    "support": [],

    "vocabulary": [
        {"term": "transverse",
         "definition": "A wave whose vibration is at right angles to the "
                       "direction it travels. Light is transverse; sound is "
                       "not."},
        {"term": "vacuum",
         "definition": "A space with no particles in it. Light crosses one "
                       "at full speed; sound does not cross one at all."},
        {"term": "speed of light",
         "definition": "300 000 000 m/s in a vacuum, as a rounded figure. "
                       "Nothing goes faster, and light is slower in glass or "
                       "water."},
    ],

    "tutor": {
        "anchor": "s-race",
        "prompt": "Ask Mr Badmus AI",
        "body": "Got a distance and want to know how long light takes to "
                "cross it?",
        "cta": "Ask about this lesson"},

    "ks4_becomes": "The electromagnetic spectrum, the wave equation applied "
                   "to light, and light-years as a unit of astronomical "
                   "distance.",

    "convention_note": "The bench is a teaching model. The speed of light is "
                       "taken as 300 000 000 m/s, a rounded value; the exact "
                       "figure in a vacuum is 299 792 458 m/s, and light in "
                       "air is very slightly slower than that. The speed of "
                       "sound is taken as about 340 m/s, its value in air at "
                       "around 20 degrees Celsius. The distance axis "
                       "multiplies by ten at every mark because the two "
                       "travel times are about a million times apart and a "
                       "ruler scale could not show both. Neither wave is "
                       "drawn losing any strength with distance, which real "
                       "light and real sound both do.",

    "ws": ["measurement"],
}
