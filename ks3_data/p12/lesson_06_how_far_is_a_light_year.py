"""P12 L6 — How far is a light year? (QUANTITATIVE, CFIFA).

Authored against Claude Design's approved page,
`docs/ks3/design-reference/p12/p12-06-how-far-is-a-light-year.dc.html`.

Her page wins outright. The Proxima Centauri hook, the five light
journeys, the d = c × t triangle, both worked examples, both attempts and
all four rungs are hers. This is the last physics lesson in the key stage
and her end-matter says so.

── ⚖️ THE BENCH HAS NO SLIDER, AND THAT IS DRAWN ────────────────────

Her `SLIDER` on this page is the empty array, exactly as on `p12-04`, so
`Bench.dc.html` draws none. `r_space_bench` refuses a `light-time` payload
that grows one.

── ⚖️ ONE FORMATTER IS A THOUSAND TIMES OUT, AND IT IS ON THE PAGE ──

Her `fmtD` reaches the "million km" branch by dividing METRES by 10^12,
which is a thousand times too many. Neptune's light-distance is
4.5 × 10^12 m — four and a half thousand million kilometres, and her own
`p12-04` legal line says so (*"Neptune's orbit about 4.5 billion km from
the Sun"*) — and the bar under Neptune on her page reads **"4.50 million
km"**. The same function has no million-light-year branch, so Andromeda
reads **"2501458.99 light years"**.

Both are fixed and her VALUES are untouched. Registered in
`DEPARTURES-P12.md`. This is 5A.1's rule read the other way round: usually
the instrument is the measurement and the prose moves, but here the
instrument contradicts the unit's own legal line and the page's own
sibling, and the arithmetic is simply wrong.

── ⚖️ `10^0` IS NOT A POWER OF TEN A STUDENT NEEDS ──────────────────

Her question head runs `T.t.toExponential(2).replace('e+', ' × 10^')` over
every object including the Moon, whose light takes 1.28 s — so the first
thing a student meets in the attempt panel is *"1.28 × 10^0 s"*. The
exponent-zero case now prints the plain number. Registered.

── ⚠️ MRB-278 · POSITION IS AUTHORED ─────────────────────────────────

This lesson takes indices **2 and 0**. Her option TEXT and every
correction are verbatim; only the ORDER moves. Across the unit the twelve
marked rungs use each of the four indices three times.

── ⚠️ MRB-177 · ONE LENGTH TELL, REMEDIED AT THE DISTRACTOR ──────────

Rung 2's correct option is 36 words against a longest distractor of 12 —
the widest gap in the unit. All three distractors are FINISHED into
complete wrong rules; the correct answer and every correction are
untouched.

── ⚠️ NO SAFEGUARDING BLOCK. NO DRAFT MARKINGS. ──────────────────────
"""

LESSON = {
    "slug": "how-far-is-a-light-year",
    "title": "How far is a light year?",
    "discipline": "physics",
    "unit": "Space",
    "family": "QUANTITATIVE",

    "covers": ["KS3.P.SPACE.04"],
    "touches": ["KS3.WS.ANA.01"],
    "beyond_statutory": False,
    "threads": [{"id": "waves", "level": 3}],
    "typical_year": 9,
    "typical_minutes": 60,

    "requires": ["seasons-and-the-tilt"],
    "assumes": [],
    "references": [{"unit": "P7", "lesson": "light-travels"},
                   {"unit": "P3", "lesson": "speed"}],
    "ks4_links": [],

    "meta_description": "A light year is a distance, not a time: how far "
                        "light travels in a year, about 9.46 × 10^15 m — and "
                        "it tells you how old the light is as well.",

    "big_question": "It sounds like a length of time and it is a distance. "
                    "Getting that one word straight is the difference between "
                    "understanding the scale of the universe and having no "
                    "idea at all.",

    "rail": [
        {"anchor": "s-hook",    "short": "HOOK",
         "label": "A year that is a distance", "done_when": "committed"},
        {"anchor": "s-bench",   "short": "BENCH",
         "label": "Five light journeys",  "done_when": "gate_and_a_control"},
        {"anchor": "s-formula", "short": "CFIFA",
         "label": "Triangle and five steps", "done_when": "attempt_checked"},
        {"anchor": "s-ladder",  "short": "LADDER",
         "label": "Mastery ladder",       "done_when": "ladder_complete"},
    ],

    "phenomenon": {
        "kind": "narrative",
        "title": "Proxima Centauri is 4.24 light years away.",
        "prompt": "That is the nearest star to the Sun, and the sentence is "
                  "the standard way of saying how far off it is.",
        "commit": "What kind of quantity is a light year?",
        "options": [
            "A long time — about twelve months",
            "A distance — how far light gets in a year",
            "A speed — how fast light travels",
            "A brightness — how much light a star gives out",
        ],
        "answer": 1,
        "reveal": "A distance. It is how far light travels in one year, and "
                  "light is fast enough that the answer is about 9.5 million "
                  "million kilometres. The word “year” in the name is "
                  "doing the same job as the word “hour” in “a "
                  "two-hour drive” — it is a way of saying how far, by "
                  "saying how long it takes something to get there at a known "
                  "speed. Anyone who says a spacecraft will arrive in four "
                  "light years has turned a distance back into a time by "
                  "mistake.",
    },

    "misconceptions": [
        {"id": "SPACE-19",
         "statement": "A light year is a very long time.",
         "elicited_by": "s-hook",
         "confronted_by": "think-a-year-that-is-a-distance"},
        {"id": "SPACE-20",
         "statement": "Because light is so fast, we see distant things as "
                      "they are now.",
         "elicited_by": "bench",
         "confronted_by": "think-a-year-that-is-a-distance"},
        {"id": "SPACE-21",
         "statement": "A light year measures how fast light travels.",
         "elicited_by": "s-hook",
         "confronted_by": "bench"},
        {"id": "SPACE-22",
         "statement": "A spacecraft that can reach a star four light years "
                      "away would get there in about four years.",
         "elicited_by": "s-ladder",
         "confronted_by": "s-ladder"},
    ],

    "core": [
        {"type": "hook", "id": "hook-commit", "anchor": "s-hook"},

        {"type": "explainer",
         "text": "Light travels at <strong>300 000 000 metres every "
                 "second</strong> in a vacuum — fast enough to go round the "
                 "Earth seven and a half times while you say the word. "
                 "Nothing carries information faster, and the speed does not "
                 "vary."},
        {"type": "explainer",
         "text": "Because the speed is fixed, a time of travel and a distance "
                 "are two ways of saying the same thing. A <strong>light "
                 "year</strong> is the distance light covers in one year: "
                 "about 9 460 000 000 000 kilometres, or 9.46 × 10^15 m. A "
                 "light second, a light minute and a light hour work the same "
                 "way, and are useful closer to home."},
        {"type": "explainer",
         "text": "The unit does two jobs at once. It gives a distance in a "
                 "number you can hold in your head, and it tells you how old "
                 "the light is. Andromeda is 2.5 million light years away, so "
                 "the light arriving tonight left before there were people. "
                 "Looking out into space is looking back in time, and there "
                 "is no way to do one without the other."},

        # ── #s-bench · five light journeys, one speed ──────────────────
        {"type": "space-bench",
         "id": "bench",
         "anchor": "s-bench",
         "eyebrow": "At the bench · five journeys, one speed",
         "heading": "Everything here is measured by how long light takes.",
         "progress": {"idle": "Change a control to begin",
                      "live": "Controls live"},
         "lead": "Pick something and see how long its light has been "
                 "travelling to reach you. Because light has one fixed speed, "
                 "that time is also a distance — and it is also a look into "
                 "the past.",
         "model": "light-time",
         # Her own constant. The legal line records that the exact value is
         # 299 792 458 m/s by definition.
         "c": 3.0e8,
         "scale": {"log_offset": 1, "log_span": 15, "min_pct": 4},
         "gate": {
             "prompt": "Commit first. A star is 30 light years away. What are "
                       "you seeing when you look at it?",
             "options": [
                 "The star as it is right now",
                 "The star as it was 30 years ago",
                 "The star as it will be in 30 years",
                 "Nothing — 30 light years is too far to see",
             ],
             "answer": 1,
         },
         "tabs_label": "What you are looking at",
         "start_tab": 0,
         "tabs": [
             {"id": "moon",      "label": "The Moon",
              "name": "the Moon",              "t": 1.28},
             {"id": "sun",       "label": "The Sun",
              "name": "the Sun",               "t": 499},
             {"id": "neptune",   "label": "Neptune",
              "name": "Neptune",               "t": 15000},
             {"id": "proxima",   "label": "Proxima Centauri",
              "name": "Proxima Centauri",      "t": 1.338e8},
             {"id": "andromeda", "label": "Andromeda",
              "name": "the Andromeda galaxy",  "t": 7.889e13},
         ],
         "bars_caption": "How long light has been travelling — each bar step "
                         "is ten times the one before",
         "bars_alt": "Five bars on a ten-times scale showing light travel "
                     "time: {list}. {label} is highlighted.",
         "bars": [
             {"id": "moon",      "label": "The Moon"},
             {"id": "sun",       "label": "The Sun"},
             {"id": "neptune",   "label": "Neptune"},
             {"id": "proxima",   "label": "Proxima Centauri"},
             {"id": "andromeda", "label": "Andromeda"},
         ],
         "readouts": [
             {"id": "takes",    "label": "Light takes"},
             {"id": "distance", "label": "So the distance is"},
             {"id": "metres",   "label": "In metres"},
             {"id": "seeing",   "label": "You are seeing it"},
         ],
         "words": {
             "takes_sub":    "to reach you from {name}",
             "distance_sub": "300 000 000 m/s × the time",
             "metres_sub":   "the same number, written out",
             "seeing_value": "as it was {time} ago",
             "seeing_sub":   "there is no other way to see anything",
             "list_join":    "and",
         },
         "notes": {
             "journey": "Light from {name} takes {time} to arrive, and "
                        "because it travels at a fixed 300 000 000 m/s that "
                        "time converts straight into a distance of {dist}. "
                        "This is why astronomers measure space in light years "
                        "rather than kilometres: the kilometre figures run to "
                        "fifteen digits and tell you nothing you can picture, "
                        "while “4.24 light years” tells you both how "
                        "far and how long ago at once. Every bar is also a "
                        "delay. Nothing you see anywhere is current — you are "
                        "simply close enough to most things for the delay not "
                        "to matter.",
         }},

        # ── #s-formula · d = c × t ────────────────────────────────────
        {"type": "formula",
         "id": "light-distance-rule",
         "eyebrow": "Writing it down · the shape of this relationship",
         "statement": "Distance = speed of light × time",
         "triangle": {
             "eyebrow": "The triangle",
             "heading": "Cover the one you want",
             "aria_label": "A formula triangle. The distance d sits above a "
                           "dividing line; the speed of light c and the time "
                           "t sit below it, multiplied together. Covering one "
                           "letter leaves the way to work it out.",
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
                 "condition": "m/s with s gives m, and km/s with s gives km — "
                              "so the time goes in as seconds.",
             },
         }},

        {"type": "worked-example", "id": "cfifa-light-plain-p12"},
        {"type": "worked-example", "id": "cfifa-light-convert-p12"},
        {"type": "check", "id": "your-turn-lightyear", "anchor": "s-formula"},

        {"type": "key-fact", "ref": "a-light-year-is-a-distance"},

        {"type": "misconception", "id": "think-a-year-that-is-a-distance",
         "anchor": "s-think"},

        {"type": "quiz", "anchor": "s-ladder"},
        {"type": "summary", "id": "s-keynote"},
    ],

    "activities": [
        {"id": "cfifa-light-plain-p12",
         "kind": "worked-example",
         "demand": "calculate",
         "eyebrow": "Worked example · one step at a time",
         "heading": "Light takes 1.28 s to reach us from the Moon. How far "
                    "away is it?",
         "head_counter": {"format": "Step {n} of 5", "total": 5},
         "buttons": {"first": "Show the first step",
                     "next": "Show the next step",
                     "done": "All five shown",
                     "done_note": "Nothing needed converting there. Now the "
                                  "one that does."},
         "staged": True,
         "fifa": [
             {"letter": "C", "label": "Convert",
              "line": "300 000 000 m/s stays as it is · 1.28 s stays 1.28 s",
              "note": "The speed is in metres per second and the time is in "
                      "seconds, so there is nothing to convert."},
             {"letter": "F", "label": "Formula",
              "line": "d = c × t",
              "note": "Cover d on the triangle: c sits beside t, so you "
                      "multiply."},
             {"letter": "I", "label": "Insert",
              "line": "d = 300 000 000 m/s × 1.28 s",
              "note": "The speed of light in a vacuum, which space very "
                      "nearly is."},
             {"letter": "F", "label": "Fine-tune",
              "line": "300 000 000 × 1.28 = 384 000 000",
              "note": "Metres per second times seconds leaves metres."},
             {"letter": "A", "label": "Answer",
              "line": "d = 384 000 000 m",
              "note": "Which is 384 000 km — the familiar figure for the "
                      "Moon."},
         ]},

        {"id": "cfifa-light-convert-p12",
         "kind": "worked-example",
         "demand": "calculate",
         "eyebrow": "Worked example · one step at a time",
         "heading": "Light takes 8.3 minutes to reach us from the Sun. How "
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
              "line": "8.3 min × 60 = 498 s",
              "note": "The speed is metres per second, so the time has to be "
                      "in seconds before it can multiply."},
             {"letter": "F", "label": "Formula",
              "line": "d = c × t",
              "note": "Cover d on the triangle: c sits beside t, so you "
                      "multiply."},
             {"letter": "I", "label": "Insert",
              "line": "d = 300 000 000 m/s × 498 s",
              "note": "The converted time goes in. The 8.3 never does."},
             {"letter": "F", "label": "Fine-tune",
              "line": "300 000 000 × 498 = 149 400 000 000",
              "note": "Metres per second times seconds leaves metres."},
             {"letter": "A", "label": "Answer",
              "line": "d = 1.494 × 10^11 m",
              "note": "Insert 8.3 instead of 498 and the Sun comes out sixty "
                      "times too close — nearer than Venus."},
         ]},

        {"id": "your-turn-lightyear",
         "kind": "p12-attempt",
         "demand": "calculate",
         "eyebrow": "Your turn · the same five steps",
         "check_label": "Check your working",
         "reveal_label": "The five lines · tick what you had",
         # The bench opens on the Moon, whose light takes 1.28 s. Her own
         # formatter would print that as "1.28 × 10^0 s"; see the module note.
         "rest": {"name": "the Moon", "texp": "1.28",
                  "d": "3.84 × 10^8", "mant": "1.28", "prod": "3.84",
                  "dist": "384,000 km"},
         "questions": [
             {"id": "q1", "tab": "Question 1",
              "head": "Your object: {name}, whose light takes {texp} s to "
                      "arrive.",
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
                   "line": "d = c × t",
                   "note": "Cover d on the triangle: c sits beside t, so you "
                           "multiply."},
                  {"letter": "I", "label": "Insert",
                   "line": "d = 3.0 × 10^8 m/s × {texp} s",
                   "note": "The speed of light in a vacuum."},
                  {"letter": "F", "label": "Fine-tune",
                   "line": "3.0 × {mant} = {prod}, and the powers add",
                   "note": "Metres per second times seconds leaves metres."},
                  {"letter": "A", "label": "Answer",
                   "line": "d = {d} m",
                   "note": "Which is {dist}."},
              ],
              "close": "The five lines give the distance to {name}. Pick "
                       "another object and only the time changes — the speed "
                       "never does."},
             {"id": "q2", "tab": "Question 2",
              "head": "A radio signal takes 22 minutes to reach a probe near "
                      "Mars. How far away is the probe?",
              "lead": "Write each line out yourself — starting by deciding "
                      "whether anything needs converting. Then check your "
                      "working and tick the lines you had.",
              "steps": [
                  {"letter": "C", "label": "Convert",
                   "placeholder": "anything to convert?",
                   "line": "22 min × 60 = 1320 s",
                   "note": "The speed is in metres per second, so the time "
                           "has to be in seconds first. Radio travels at the "
                           "speed of light."},
                  {"letter": "F", "label": "Formula",
                   "line": "d = c × t",
                   "note": "Cover d on the triangle: c sits beside t, so you "
                           "multiply."},
                  {"letter": "I", "label": "Insert",
                   "line": "d = 300 000 000 m/s × 1320 s",
                   "note": "The converted time goes in. The 22 never does."},
                  {"letter": "F", "label": "Fine-tune",
                   "line": "300 000 000 × 1320 = 396 000 000 000",
                   "note": "Metres per second times seconds leaves metres."},
                  # ⊕ MRB-297 · 1 Sep 2026. The note said the wrong insert
                  # puts the probe "closer than the Moon". It does not:
                  # 3.0 × 10^8 × 22 = 6.6 × 10^9 m, and the Moon is
                  # 3.84 × 10^8 m away on this page's own first worked
                  # example, so it lands seventeen times FURTHER out. What
                  # is true is the factor the slip costs — 1320 ÷ 22 = 60 —
                  # and 6.6 × 10^9 m is exactly 22 light seconds, which
                  # names the mistake better than a wrong comparison did.
                  {"letter": "A", "label": "Answer",
                   "line": "d = 3.96 × 10^11 m",
                   "note": "Insert 22 instead of 1320 and the answer comes "
                           "out sixty times too small — 22 light "
                           "seconds away instead of 22 light minutes."},
              ],
              "close": "The five lines give 3.96 × 10^11 m — about 396 "
                       "million km, and the reason a rover cannot be driven "
                       "with a joystick."},
         ]},

        {"id": "think-a-year-that-is-a-distance",
         "kind": "predict",
         "demand": "explain",
         "targets": "SPACE-19",
         "statements": [
             {"quote": "A light year is a very long time.",
              "targets": "SPACE-19",
              "body": [
                  "It is a distance, and the giveaway is the sentence it "
                  "appears in. “The star is four light years away” "
                  "is a statement about how far, in exactly the same grammar "
                  "as “the shop is two miles away”. The year in "
                  "the name is describing the light’s journey, not yours. The "
                  "confusion is common enough that science fiction gets it "
                  "wrong regularly, and once you notice it you will not be "
                  "able to stop noticing it.",
              ]},
             {"quote": "Because light is so fast, we see distant things as "
                       "they are now.",
              "targets": "SPACE-20",
              "body": [
                  "Light is fast compared with everything on Earth and slow "
                  "compared with the size of space. The Sun you see is eight "
                  "minutes and nineteen seconds old; if it stopped shining "
                  "you would carry on seeing it for that long. Proxima "
                  "Centauri is seen as it was four years ago and Andromeda as "
                  "it was before the first humans. For a galaxy at the edge "
                  "of what telescopes can reach, the light is older than the "
                  "Earth.",
              ]},
         ]},
    ],

    "figures": [],

    "key_facts": [
        {"id": "a-light-year-is-a-distance",
         "eyebrow": "Key fact",
         "ground": "card",
         "placement": "top-level",
         "text": "A light year is a distance: how far light travels in one "
                 "year, about 9.46 × 10^15 m. Distance = speed of light × "
                 "time, so a travel time and a distance are the same "
                 "statement. Light takes time to arrive, so everything you "
                 "see in space is seen as it was."},
    ],

    # ⚠️ MRB-278 · POSITION IS AUTHORED. This lesson takes indices 2 and 0,
    # which completes the unit at three uses of each of the four indices.
    #
    # ⚠️ MRB-177 · RUNG 2'S THREE DISTRACTORS ARE FINISHED into complete
    # wrong rules — the widest gap in the unit, 36 words against 11. The
    # correct answer and every correction are untouched.
    "ladder": {
        "recall": {
            "q": "Light takes 500 s to reach the Earth from the Sun, and "
                 "travels at 3.0 × 10^8 m/s. How far away is the Sun?",
            "options": [
                "6.0 × 10^5 m — divide the speed by the time",
                "1.5 × 10^11 s — the answer is in seconds",
                "1.5 × 10^11 m",
                "500 light seconds, which cannot be converted to metres",
            ],
            "answer": 2,
            "feedback": {
                0: "Cover d on the triangle and c sits beside t, so you "
                   "multiply. Dividing gives you a speed or a time, not a "
                   "distance.",
                1: "The number is right and the unit is wrong. Metres per "
                   "second times seconds leaves metres.",
                3: "500 light seconds is right, and it converts perfectly "
                   "well — multiply by the speed of light and you get "
                   "1.5 × 10^11 m.",
            },
            "title": "Rung 1 · Calculate"},
        "apply": {
            "q": "A spacecraft is described as being able to reach a star "
                 "“in four light years”. What is wrong with that?",
            "options": [
                "A light year is a distance, not a time. The sentence says "
                "the craft can travel four light years, without saying how "
                "long it would take — which at current speeds is about "
                "70 000 years.",
                "Nothing is wrong — a light year is a unit of time, so a "
                "craft that arrives in four light years arrives in four "
                "years, in exactly the way a two-hour drive takes two hours.",
                "It is wrong because no star is four light years away, and a "
                "sentence that names a distance nothing actually sits at "
                "cannot describe a real journey to anywhere.",
                "It is wrong because nothing can travel a whole light year, "
                "so no craft could ever cover four of them however long it "
                "was given to try.",
            ],
            "answer": 0,
            "feedback": {
                1: "A light year is how far light travels in a year. The year "
                   "in the name describes the light, not the journey.",
                2: "Proxima Centauri is 4.24 light years away. The problem is "
                   "with the unit, not the number.",
                3: "Light travels one every year, and starlight crosses far "
                   "more than that. The error is treating a distance as a "
                   "duration.",
            },
            "title": "Rung 2 · The one that catches people"},
        "explain": {
            "q": "Explain what a light year is and why astronomers use it "
                 "instead of kilometres.",
            "field_label": "Your explanation",
            "placeholder": "A light year is the distance…",
            "success": [
                "Says a light year is a distance, not a time.",
                "Says it is how far light travels in one year, at "
                "300 000 000 m/s.",
                "Gives the figure — about 9.5 million million kilometres.",
                "Says distances in kilometres run to unmanageable numbers of "
                "digits.",
                "Says the light year also tells you how long ago the light "
                "set out, which the kilometre figure does not.",
            ],
            "title": "Rung 3 · Explain"},
        "produce": {
            "q": "A rover on Mars is between 4 and 24 light minutes from "
                 "Earth depending on where the two planets are. Explain why "
                 "it cannot be driven with a joystick, and what engineers do "
                 "instead.",
            "field_label": "Your answer",
            "placeholder": "A command sent from Earth takes…",
            "success": [
                "Says a command takes between 4 and 24 minutes to arrive.",
                "Says the picture confirming what happened takes the same "
                "again to come back.",
                "Says the round trip is therefore up to about 48 minutes.",
                "Says the rover could have driven into a hazard long before "
                "any correction arrived.",
                "Says engineers send a plan for the rover to carry out on its "
                "own, with onboard hazard detection, rather than steering it "
                "live.",
            ],
            "title": "Rung 4 · Take it somewhere new"},
    },

    "key_note": "Light travels at 300 000 000 m/s in a vacuum, and a light "
                "year is the distance it covers in one year — about "
                "9.46 × 10^15 m, or 9.5 million million kilometres. It is a "
                "unit of distance, not of time, and it is used because "
                "distances in space are unmanageable in kilometres. Because "
                "light takes time to arrive, every observation is of the "
                "past: the Sun is seen as it was 8 minutes ago, Proxima "
                "Centauri as it was 4.24 years ago, and Andromeda as it was "
                "2.5 million years ago.",

    "stretch": [
        {"id": "the-delay-is-an-engineering-problem",
         "type": "explainer",
         "text": "The delay is a working engineering problem, not a "
                 "curiosity. A signal to a Mars rover takes between 4 and 24 "
                 "minutes each way, so nothing there can be driven live; the "
                 "rover is sent a plan and left to carry it out, with onboard "
                 "software to stop it falling into anything. The Voyager 1 "
                 "probe is over 22 light hours out, and a round trip of "
                 "instructions and confirmation takes nearly two days."},
        {"id": "not-merely-a-fast-speed",
         "type": "explainer",
         "text": "The speed of light is not a speed limit that happens to be "
                 "very high; it is built into the structure of space and "
                 "time. Nothing carrying information can exceed it, which is "
                 "why the nearest star is genuinely out of reach — the "
                 "fastest object humans have ever launched would take about "
                 "70 000 years to cover those 4.24 light years. Every serious "
                 "proposal for interstellar travel is really a proposal about "
                 "getting closer to that limit."},
    ],

    "support": [],

    "vocabulary": [
        {"term": "light year",
         "definition": "The distance light travels in one year, about "
                       "9.46 × 10^15 m. It is a distance and never a length "
                       "of time, whatever the name suggests."},
        {"term": "speed of light",
         "definition": "300 000 000 m/s in a vacuum. Nothing carrying "
                       "information travels faster, and the value does not "
                       "vary."},
        {"term": "vacuum",
         "definition": "Space with no matter in it. Light crosses one at its "
                       "full speed, which is why the figure quoted for space "
                       "is the vacuum value."},
        {"term": "light minute",
         "definition": "The distance light travels in one minute. Light "
                       "seconds, minutes and hours work exactly as light "
                       "years do, and are the useful units close to home."},
    ],

    "tutor": {
        "anchor": "s-formula",
        "prompt": "Ask Mr Badmus AI",
        "body": "Got a light travel time and want the distance in metres?",
        "cta": "Ask about this lesson"},

    "ks4_becomes": "The scale of the universe in astronomical units, light "
                   "years and parsecs, red shift and the recession of distant "
                   "galaxies, and the finite age of the observable universe.",

    "convention_note": "The bench is a teaching model. The speed of light is "
                       "taken as 3.0 × 10^8 m/s; the exact value is "
                       "299 792 458 m/s by definition. Light travel times are "
                       "current accepted figures: the Moon 1.28 s, the Sun "
                       "499 s, Neptune about 15 000 s at mean distance, "
                       "Proxima Centauri 4.24 years and Andromeda about 2.5 "
                       "million years. The Moon, Neptune and Mars distances "
                       "vary substantially over their orbits, so the figures "
                       "are means rather than fixed values. One light year is "
                       "taken as 9.461 × 10^15 m.",

    "ws": ["measurement"],
}
