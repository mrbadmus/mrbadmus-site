"""P6 L6 — Sound needs a medium (INVESTIGATION).

Authored against Claude Design's approved page,
`docs/ks3/design-reference/p6/p6-06-sound-needs-a-medium.dc.html`.

Her page wins outright. The buzzer in the jar, the striker and microphone,
both worked examples and all four rungs are hers.

── ⚖️ MRB-204 · A TRIANGLE, AND IT IS THE ONE THE STATUTE NEEDS ──────

`d = v × t` is a genuine product, and the speed of sound is the statutory
content of `SND.02`. The triangle is what makes the number usable.

⚠️ **HER FLAG 5: THIS RELATIONSHIP APPEARS THREE TIMES ACROSS TWO UNITS**
— here, inside `p6-07`'s worked example as given data, and again in
`p7-01` for light. No lesson assumes the others; each states it from
nothing and carries the others as edges. She asks a reviewer to check it
reads as reinforcement rather than as a missing single-source ruling.
Nothing here changes it.

── ⚖️ RULED · THE VACUUM REPORTS NOTHING, AND SAYS SO IN WORDS ───────

Not a very small number and not a very long time: **no sound, at any
distance, for any length of time.** A bench that printed `0 m/s` and a
time would teach that sound crosses a vacuum slowly, which is `WAVE-21`
exactly. `r_medium_range` requires a zero-speed medium in the deck and
refuses to compute a time for it.

── ⚖️ RULED · THE PARTICLES ARE THE EXPLANATION, NOT DECORATION ──────

Scattered dots for a gas, close rows for a liquid, a linked lattice for a
solid — and each material's note names the same arrangement in words. The
pattern IS why the speed is what it is, and the renderer refuses a
material that does not declare one.

── ⊖ HER FLAG 6 · STEEL IS 5000 m/s AND STAYS ───────────────────────

Published values run 5000–5900. She uses 5000 here and in `p6-09` for
consistency, and `p6-09`'s legal line states the range. Kept: the number
is declared, the two pages agree, and standardising on 5900 would need
both pages and one rung changing together — a corpus decision, not a P6
one.

── ⚠️ FOUR RAIL STOPS ────────────────────────────────────────────────

    s-hook · s-range · s-formula · s-ladder

⚠️ **MRB-208** — the `s-formula` id goes on the attempt panel.

── ⚖️ FOUR MISCONCEPTIONS ────────────────────────────────────────────

    WAVE-21  sound crosses a vacuum, faintly
    WAVE-22  sound is fastest in air, because air is easiest to get through
    WAVE-23  a vacuum stops sound because there is nothing to push against
    WAVE-24  sound needs air specifically, not just any material
"""

LESSON = {
    "slug":  "sound-needs-a-medium",
    "title": "Sound needs a medium",
    "discipline": "physics",
    "unit": "Waves and sound",
    "family": "INVESTIGATION",

    "covers": ["KS3.P.SND.02"],
    "touches": ["KS3.WS.ANA.01"],
    "beyond_statutory": False,
    "threads": [{"id": "waves", "level": 3}],
    "typical_year": 8,
    "typical_minutes": 60,

    "requires": ["frequency-pitch-and-loudness"],
    "assumes": [],
    "references": ["sound-is-longitudinal",
                   "echoes-reflection-and-absorption"],
    "ks4_links": [],

    "meta_description": "A buzzer in a jar goes quiet while you watch it "
                        "still ringing. Nothing was done to the buzzer — "
                        "something was taken away from the space around it.",

    "big_question": "A buzzer in a jar goes quiet while you watch it still "
                    "ringing. Nothing has been done to the buzzer at all — "
                    "something has been taken away from the space around it.",

    "rail": [
        {"anchor": "s-hook",    "short": "JAR",
         "label": "The buzzer in the jar",   "done_when": "committed"},
        {"anchor": "s-range",   "short": "RANGE",
         "label": "Striker and microphone",  "done_when": "gate_and_a_control"},
        {"anchor": "s-formula", "short": "CFIFA",
         "label": "Triangle and five steps", "done_when": "attempt_checked"},
        {"anchor": "s-ladder",  "short": "LADDER",
         "label": "Mastery ladder",          "done_when": "ladder_complete"},
    ],

    "phenomenon": {
        "kind": "narrative",
        "title": "The buzzer is still going. The sound is not.",
        "prompt": "A small buzzer hangs on a thread inside a thick glass "
                  "jar, ringing away. A pump starts pulling the air out of "
                  "the jar. Through the glass you can still see the little "
                  "hammer beating against the bell, exactly as fast as "
                  "before.",
        "commit": "As the last of the air leaves the jar, what happens to "
                  "what you hear?",
        "options": [
            "The buzzer keeps vibrating and the sound fades away to nothing",
            "The buzzer stops working, because it needs air around it to run "
            "at all",
            "The note gets higher as the air thins out, and then climbs past "
            "what you can hear",
            "The sound gets quieter but never disappears, because it crosses "
            "empty space slowly",
        ],
        "answer": 0,
        "reveal": "The hammer never stops. What stops is the delivery: sound "
                  "is a squeeze handed from one particle to the next, and "
                  "the pump is taking the particles away. Let the air back "
                  "in and the ringing returns at once, exactly as loud as "
                  "before, <strong>which proves the buzzer was working the "
                  "whole time.</strong>",
    },

    "misconceptions": [
        {"id": "WAVE-21",
         "statement": "Sound crosses a vacuum, faintly.",
         "elicited_by": "s-hook",
         "confronted_by": "range"},
        {"id": "WAVE-22",
         "statement": "Sound is fastest in air, because air is easiest to "
                      "get through.",
         "elicited_by": "range",
         "confronted_by": "range"},
        {"id": "WAVE-23",
         "statement": "A vacuum stops sound because there is nothing for the "
                      "source to push against.",
         "confronted_by": "s-think"},
        {"id": "WAVE-24",
         "statement": "Sound needs air specifically, rather than any "
                      "material at all.",
         "elicited_by": "s-ladder",
         "confronted_by": "range"},
    ],

    "core": [
        {"type": "hook", "id": "hook-commit", "anchor": "s-hook"},

        {"type": "explainer",
         "text": "Sound is a disturbance passed from one particle of a "
                 "material to the next. A vibrating surface pushes the "
                 "particles touching it, those push the next ones along, and "
                 "the squeeze travels. Take the particles away and there is "
                 "nothing to do the passing on: <strong>sound cannot travel "
                 "through a vacuum</strong>. The buzzer is still vibrating, "
                 "and the vibration has nowhere to go."},
        {"type": "explainer",
         "text": "Give it particles and it travels — through gases, through "
                 "liquids and through solids. How fast depends on the "
                 "material, and the pattern is the same one every time: the "
                 "closer the particles sit and the more strongly they are "
                 "held to each other, the more quickly each one passes the "
                 "shove on. <strong>Sound is slowest in gases, faster in "
                 "liquids, and fastest in solids.</strong> In air it manages "
                 "about 340 metres every second; in steel, about 5000."},

        # ── #s-range · striker and microphone ──────────────────────────
        {"type": "medium-range",
         "id": "range",
         "anchor": "s-range",
         "eyebrow": "At the bench · a striker and a microphone, with a "
                    "measured gap between them",
         "heading": "Same bang. Change what is in the way.",
         "progress": "Change a control to begin",
         "lead": "A hammer strikes a plate at one end and a microphone "
                 "records the arrival at the other. Set what fills the gap, "
                 "and set how long the gap is.",
         "air_v": 340,
         "start_mat": 0,
         "mat_label": "What fills the gap",
         "gate": {
             "prompt": "Commit first. The same striker and microphone are "
                       "set 100 m apart, once through air and once through "
                       "steel. Which arrives first, and why?",
             "options": [
                 "Through the air, because a gas puts less in the way of "
                 "the sound and a shove crosses an empty space faster than "
                 "a crowded one",
                 "Through the steel, because its particles are close "
                 "together and strongly linked, so each passes the shove on "
                 "sooner",
                 "They arrive together, because the sound is the same sound "
                 "in both",
                 "Through the steel, because a solid makes a louder sound "
                 "than a gas does",
             ],
             "answer": 1,
         },
         "dist": {"label": "How long the gap is", "min": 50, "max": 1000,
                  "step": 50, "start": 200, "value": "200 m"},
         # ⚠️ SLOWEST FIRST. The tab row itself teaches the pattern, and
         # `r_medium_range` refuses a deck out of speed order.
         "materials": [
             {"id": "air", "label": "Air", "v": 340, "pattern": "gas",
              "state": "a gas at about 20 °C",
              "caption": "AIR — PARTICLES FAR APART AND FREE",
              "note": "Air is a gas: its particles are far apart and barely "
                      "hold on to each other, so each one travels a good way "
                      "before it reaches the next. That is the slowest "
                      "arrangement here, and about 340 m/s is the result."},
             {"id": "water", "label": "Water", "v": 1500,
              "pattern": "liquid", "state": "a liquid at about 20 °C",
              "caption": "WATER — PARTICLES TOUCHING BUT FREE TO SLIDE",
              "note": "In water the particles are already touching, so a "
                      "shove reaches the next one almost immediately, and "
                      "sound manages about 1500 m/s — more than four times "
                      "its speed in air. Whales use that: a call can carry "
                      "for tens of kilometres through the sea."},
             {"id": "oak", "label": "Oak", "v": 3800, "pattern": "lattice",
              "state": "a solid, measured along the grain",
              "caption": "OAK — PARTICLES LOCKED IN PLACE",
              "note": "Oak is a solid, so its particles are both close "
                      "together and strongly linked, and the shove is handed "
                      "on at about 3800 m/s along the grain. Across the "
                      "grain it is far slower, which is why the direction "
                      "has to be stated."},
             {"id": "steel", "label": "Steel", "v": 5000,
              "pattern": "lattice", "state": "a solid, strongly bonded",
              "caption": "STEEL — PARTICLES PACKED AND STRONGLY LINKED",
              "note": "Steel has its particles packed tight and held to each "
                      "other very strongly, which is the fastest arrangement "
                      "here at about 5000 m/s — roughly fifteen times the "
                      "speed in air. Tap one end of a long steel fence and "
                      "the sound reaches the far end through the metal well "
                      "before it arrives through the air."},
             {"id": "vacuum", "label": "Vacuum", "v": 0, "pattern": "none",
              "state": "no particles at all",
              "caption": "VACUUM — NOTHING TO PASS THE SHOVE ON",
              "note": "There is nothing in the gap to be squeezed, so the "
                      "striker vibrates and nothing at all leaves it. This "
                      "is not a very slow or very quiet sound: it is no "
                      "sound, at any distance, for any length of time."},
         ],
         "readouts": [
             {"id": "gap", "label": "The gap",
              "sub": "measured striker to microphone"},
             {"id": "speed", "label": "Speed of sound in it", "sub": "—"},
             {"id": "time", "label": "Time to arrive", "sub": "—"},
             {"id": "verdict", "label": "At the microphone"},
         ]},

        # ── #s-figure · all five, to one scale ─────────────────────────
        #
        # ⊕ PHASE 3 ADDITION, 25 Aug 2026. Design's page carries this figure
        # inside `#s-range` and the port had left it out ALTOGETHER — not a
        # paraphrase but a whole block of hers absent, found by comparing
        # the built page against her drawing rather than against the
        # register. It takes no rail stop: her RAIL for this page is four
        # entries and the figure is not among them.
        {"type": "wave-band",
         "id": "five-materials",
         "anchor": "s-figure",
         "eyebrow": "The figure",
         "heading": "All five side by side, to one scale",
         "speeds": {
             "aria_label": "A bar chart of the speed of sound in five "
                           "materials, all to one scale: vacuum, no sound at "
                           "all; air about 340 metres per second; water "
                           "about 1500; oak about 3800; steel about 5000. "
                           "Beside each bar the particles are drawn at their "
                           "spacing, from empty for a vacuum to a locked "
                           "lattice for steel.",
             "name_label": "MATERIAL",
             "particle_label": "PARTICLES",
             "speed_label": "SPEED OF SOUND",
             "rows": [
                 {"label": "Vacuum", "v": 0, "value": "no sound at all",
                  "pattern": "none", "particle_note": "NOTHING HERE"},
                 {"label": "Air", "v": 340, "value": "about 340 m/s",
                  "pattern": "gas"},
                 {"label": "Water", "v": 1500, "value": "about 1500 m/s",
                  "pattern": "liquid"},
                 {"label": "Oak", "v": 3800, "value": "about 3800 m/s",
                  "pattern": "lattice"},
                 {"label": "Steel", "v": 5000, "value": "about 5000 m/s",
                  "pattern": "lattice"},
             ],
         },
         "close": "The order runs with the particles, not against them. A "
                  "gas has its particles far apart and free, so each shove "
                  "takes a while to reach the next one. A solid has them "
                  "close and strongly linked, so the shove is handed on "
                  "almost at once. A vacuum has none, and the bar has "
                  "nothing to draw."},

        {"type": "formula",
         "id": "speed-rule",
         "eyebrow": "Writing it down · the shape of this relationship",
         "statement": "Distance = speed × time",
         "triangle": {
             "eyebrow": "The triangle",
             "heading": "Cover the one you want",
             "aria_label": "A formula triangle. Distance d sits above a "
                           "dividing line; speed v and time t sit below it, "
                           "multiplied together. Covering one letter leaves "
                           "the way to work it out.",
             "order": ["top", "left", "right"],
             "covered": "left",
             "top":   {"label": "d", "button": "Cover d",
                       "result": "d = v × t", "text": ""},
             "left":  {"label": "v", "button": "Cover v",
                       "result": "v = d ÷ t", "text": ""},
             "right": {"label": "t", "button": "Cover t",
                       "result": "t = d ÷ v", "text": ""},
             "close": {
                 "rule": "Two things side by side means multiply. One thing "
                         "over another means divide.",
                 "units": ["d · distance · m",
                           "v · speed of sound in that material · m/s",
                           "t · time · s"],
                 "condition": "The speed belongs to the MATERIAL, not to the "
                              "sound: change what fills the gap and v "
                              "changes, whatever the note.",
             },
         }},

        {"type": "worked-example", "id": "cfifa-speed-plain-p6"},
        {"type": "worked-example", "id": "cfifa-speed-convert-p6"},
        {"type": "check", "id": "your-turn-speed", "anchor": "s-formula"},

        {"type": "key-fact", "ref": "sound-needs-particles"},

        {"type": "misconception", "id": "think-vacuum-carries-sound",
         "anchor": "s-think"},

        {"type": "quiz", "anchor": "s-ladder"},
        {"type": "summary", "id": "s-keynote"},
    ],

    "activities": [
        {"id": "cfifa-speed-plain-p6",
         "kind": "worked-example",
         "demand": "calculate",
         "eyebrow": "Worked example · one step at a time",
         "heading": "A hammer strikes one end of a steel rail 1000 m long. "
                    "The blow is heard through the rail 0.20 s later. What "
                    "is the speed of sound in steel?",
         "head_counter": {"format": "Step {n} of 5", "total": 5},
         "buttons": {"first": "Show the first step",
                     "next": "Show the next step",
                     "done": "All five shown",
                     "done_note": "Nothing needed converting there. Now the "
                                  "one that does."},
         "staged": True,
         "fifa": [
             {"letter": "C", "label": "Convert",
              "line": "1000 m stays 1000 m · 0.20 s stays 0.20 s",
              "note": "The length is already in metres and the time already "
                      "in seconds, so there is nothing to convert."},
             {"letter": "F", "label": "Formula",
              "line": "speed = distance ÷ time",
              "note": "Cover v on the triangle: d sits over t, so you "
                      "divide."},
             {"letter": "I", "label": "Insert",
              "line": "speed = 1000 m ÷ 0.20 s",
              "note": "The distance is the length of the rail, because the "
                      "sound went through the steel."},
             {"letter": "F", "label": "Fine-tune",
              "line": "1000 ÷ 0.20 = 5000",
              "note": "Metres divided by seconds leaves metres per second."},
             {"letter": "A", "label": "Answer", "line": "speed = 5000 m/s",
              "note": "About fifteen times the speed of the same blow "
                      "through the air."},
         ]},

        {"id": "cfifa-speed-convert-p6",
         "kind": "worked-example",
         "demand": "calculate",
         "eyebrow": "Worked example · one step at a time",
         "heading": "A blow travels 2.4 km along a steel pipe in 0.48 s. "
                    "What is the speed of sound in the pipe?",
         "head_counter": {"format": "Step {n} of 5", "total": 5},
         "buttons": {"first": "Show the first step",
                     "next": "Show the next step",
                     "done": "All five shown",
                     "done_note": "Convert first, then the same four lines. "
                                  "Your turn below, on your own gap."},
         "staged": True,
         "fifa": [
             {"letter": "C", "label": "Convert",
              "line": "2.4 km × 1000 = 2400 m",
              "note": "Metres per second needs the distance in metres, and a "
                      "kilometre is a thousand of them."},
             {"letter": "F", "label": "Formula",
              "line": "speed = distance ÷ time",
              "note": "Cover v on the triangle: d sits over t, so you "
                      "divide."},
             {"letter": "I", "label": "Insert",
              "line": "speed = 2400 m ÷ 0.48 s",
              "note": "The converted distance goes in. The 2.4 never does."},
             {"letter": "F", "label": "Fine-tune",
              "line": "2400 ÷ 0.48 = 5000",
              "note": "Metres divided by seconds leaves metres per second."},
             {"letter": "A", "label": "Answer", "line": "speed = 5000 m/s",
              "note": "Insert 2.4 instead of 2400 and the answer comes out "
                      "5 m/s — slower than walking."},
         ]},

        {"id": "your-turn-speed",
         "kind": "p6-attempt",
         "demand": "calculate",
         "eyebrow": "Your turn · the same five steps",
         # The bench's opening state: 200 m of air at 340 m/s. `timenum` is
         # the bare number the Fine-tune line divides out to, and `time` is
         # the same value with its unit — two tokens because the two lines
         # want different things, and the guard in `kit._rest_fill` caught
         # the missing one before it could ship a brace to a reader with no
         # JavaScript.
         "rest": {"headline": "Your gap: 200 m of air.", "dist": 200, "v": 340,
                  "name": "air", "timenum": 0.5882, "time": "0.588 s"},
         "questions": [
             {"id": "q1", "tab": "Question 1",
              # ⊕ PHASE 3, 25 Aug 2026 — HER question, and HER
              # handling of the vacuum. She does not block the
              # panel: she says the vacuum has nothing to time and
              # runs the five steps on AIR across the same gap, so
              # the student still gets the practice and the physics
              # point is made in the head rather than by an absence.
              "head": "{headline}",
              "lead": "Write all five lines before you check. The gap and "
                      "the material are the ones your own bench is showing.",
              "steps": [
                  {"letter": "C", "label": "Convert",
                   "placeholder": "anything to convert?",
                   "line": "the distance is already in metres · the time is "
                           "already in seconds",
                   "note": "The bench measures in metres and seconds, which "
                           "is what m/s needs, so there is nothing to "
                           "convert."},
                  {"letter": "F", "label": "Formula",
                   "line": "t = d ÷ v",
                   "note": "Cover t on the triangle: d sits over v, so you "
                           "divide."},
                  {"letter": "I", "label": "Insert",
                   "line": "t = {dist} m ÷ {v} m/s",
                   "note": "The gap comes from your slider; the speed is "
                           "the one for {name}."},
                  {"letter": "F", "label": "Fine-tune",
                   "line": "{dist} ÷ {v} = {timenum}",
                   "note": "Metres divided by metres per second leaves "
                           "seconds."},
                  {"letter": "A", "label": "Answer",
                   "line": "t = {time}",
                   "note": "Seconds, because that is what is left when the "
                           "metres cancel."},
              ],
              "close": "The five lines above give {time} for {dist} m of "
                       "{name}."},
             {"id": "q2", "tab": "Question 2",
              # ⊕ PHASE 3, 25 Aug 2026 — HER question, not one of
              # ours. The port had written a different second
              # question here with different numbers; hers is the
              # one a student is meant to meet.
              "head": "A sound travels 1.5 km through sea water in 1.0 s. "
                      "What is its speed?",
              "lead": "This one needs the Convert line to do some "
                      "work.",
              "steps": [
                  {"letter": "C", "label": "Convert",
                   "placeholder": "anything to convert?",
                   "line": "1.5 km × 1000 = 1500 m",
                   "note": "Metres per second needs the distance in metres, "
                           "so multiply the kilometres by 1000."},
                  {"letter": "F", "label": "Formula",
                   "line": "speed = distance ÷ time",
                   "note": "Cover v on the triangle: d sits over t, so you "
                           "divide."},
                  {"letter": "I", "label": "Insert",
                   "line": "speed = 1500 m ÷ 1.0 s",
                   "note": "The converted distance goes in. The 1.5 never "
                           "does."},
                  {"letter": "F", "label": "Fine-tune",
                   "line": "1500 ÷ 1.0 = 1500",
                   "note": "Metres divided by seconds leaves metres per "
                           "second."},
                  {"letter": "A", "label": "Answer",
                   "line": "speed = 1500 m/s",
                   "note": "Insert 1.5 instead of 1500 and the answer comes "
                           "out 1.5 m/s."},
              ],
              "close": "The five lines give 1500 m/s — about four times the "
                       "speed of sound in air."},
         ]},

        {"id": "think-vacuum-carries-sound",
         "kind": "predict",
         "demand": "explain",
         "targets": "WAVE-23",
         "statements": [
             {"quote": "Sound crosses a vacuum, just very slowly and "
                      "faintly.",
              "targets": "WAVE-23",
              "body": [
                  "There is no slow, faint version. Sound is particles "
                  "shoving their neighbours, so with no particles there is "
                  "no mechanism at all, and the loudness does not tail off "
                  "towards a whisper — it goes to nothing. That is why an "
                  "astronaut outside a spacecraft hears their own breathing "
                  "and their radio and nothing else, no matter how violent "
                  "the thing happening a few metres away, and why the "
                  "explosions in space films are a sound-effects decision "
                  "rather than physics. Light does cross a vacuum, which is "
                  "why you can see the thing you cannot hear.",
              ]},
             {"quote": "Sound goes fastest through air, because air is the "
                      "easiest thing to get through.",
              "targets": "WAVE-22",
              "body": [
                  "Easy to walk through is not the same as easy to pass a "
                  "shove along. Getting through the air is easy precisely "
                  "because its particles are far apart and barely hold on "
                  "to each other — and that is exactly what makes it slow "
                  "at handing a disturbance on. In steel every particle is "
                  "packed tight against its neighbours and firmly linked to "
                  "them, so the shove is passed on almost immediately and "
                  "sound manages about 5000 m/s, roughly fifteen times its "
                  "speed in air. Put your ear to a long metal fence and "
                  "have someone tap the far end: you hear it through the "
                  "metal first and through the air a moment later.",
              ]},
         ]},
    ],

    "figures": [],

    "key_facts": [
        {"id": "sound-needs-particles",
         "eyebrow": "Key fact",
         "ground": "card",
         "placement": "top-level",
         "text": "Sound needs a material to travel through and cannot cross a "
                 "vacuum, because there are no particles to pass the "
                 "disturbance on. It goes fastest where the particles are "
                 "closest together and most strongly linked: about 340 m/s in "
                 "air, about 1500 m/s in water and about 5000 m/s in steel."},
    ],

    # ⚠️ MRB-278 · POSITION IS AUTHORED. This lesson takes indices 2 and 3.
    "ladder": {
        "recall": {
            "q": "A shout crosses 680 m of still air. Sound travels at "
                 "about 340 m/s in air. How long does it take?",
            "options": [
                "About 0.50 s — divide the speed by the distance",
                "About 2.0 m",
                "About 2.0 s",
                "About 231 000 s — multiply the distance by the speed",
            ],
            "answer": 2,
            "feedback": {
                0: "That is the calculation upside down. Cover t on the "
                   "triangle and d sits over v, so the distance is the one "
                   "being divided.",
                1: "The arithmetic is right and the unit is wrong. Metres "
                   "divided by metres per second leaves seconds, and the "
                   "question asked how long.",
                3: "Multiplying gives you a distance back when you already "
                   "know one. To find a time you share the distance out at "
                   "so many metres each second, so you divide.",
            },
            "title": "Rung 1 · Calculate"},
        "apply": {
            "q": "A spacecraft explodes a hundred metres from an astronaut "
                 "on a spacewalk. Which statement is right?",
            "options": [
                "The astronaut hears a faint, delayed bang, because space "
                "is very thin rather than completely empty, and a thin "
                "material carries a weakened sound rather than none at all",
                "The astronaut sees it and hears nothing at all, because "
                "there are no particles between them to pass the "
                "disturbance on.",
                "The astronaut hears it immediately, because with nothing "
                "in the way sound is not slowed down.",
                "The astronaut hears nothing, because the explosion is too "
                "far away for sound to carry.",
            ],
            "answer": 1,
            "feedback": {
                0: "Faint is not what happens. With no particles there is "
                   "no way for a disturbance to be handed along at all, so "
                   "the sound does not arrive weakened — it does not "
                   "arrive.",
                2: "Nothing in the way is exactly the problem. Sound is not "
                   "something that flies through a gap — it is a "
                   "disturbance in a material, and it needs the material.",
                3: "The verdict is right and the rule is wrong. A hundred "
                   "metres is nothing for sound in air; what stops it is "
                   "the absence of a material, not the distance.",
            },
            "title": "Rung 2 · The one that catches people"},
        "explain": {
            "q": "A ringing buzzer hangs inside a glass jar. A pump slowly "
                 "removes the air. Describe what happens and explain why, "
                 "using the word particles.",
            "field_label": "Your explanation",
            "placeholder": "As the air is pumped out…",
            "success": [
                "Says the sound gets quieter as the air is removed and "
                "fades to nothing.",
                "Says the buzzer can still be seen vibrating throughout.",
                "Says sound is passed from particle to particle through a "
                "material.",
                "Says removing the air removes the particles, so there is "
                "nothing left to pass the disturbance on.",
                "Says letting the air back in brings the sound back, which "
                "shows the buzzer never stopped.",
            ],
            "title": "Rung 3 · Explain"},
        "produce": {
            "q": "Standing beside a long steel railway rail, you hear a "
                 "hammer blow from far down the track twice: once through "
                 "the rail and once through the air. The rail is 1700 m "
                 "long. Work out both arrival times and the gap between "
                 "them, then say which arrives first and why.",
            "field_label": "Your answer",
            "placeholder": "Through the steel, time = distance ÷ speed…",
            "success": [
                "Uses time = distance ÷ speed for both journeys.",
                "Gets about 0.34 s through the steel, using about 5000 m/s.",
                "Gets about 5.0 s through the air, using about 340 m/s.",
                "Gives the gap as about 4.7 s, with the unit.",
                "Says the steel arrives first because its particles are "
                "closer together and more strongly linked, so each one "
                "passes the shove on sooner.",
            ],
            "title": "Rung 4 · Take it somewhere new"},
    },

    "key_note": "Sound is a disturbance passed from particle to particle, so "
                "it needs a material to travel through and cannot cross a "
                "vacuum at all. It travels through gases, liquids and solids, "
                "and it goes faster where the particles are closer together "
                "and more strongly linked: about 340 m/s in air, about 1500 "
                "m/s in water and about 5000 m/s in steel. Distance = speed "
                "of sound × time.",

    "stretch": [
        # ⊕ PHASE 3 REVERT, 25 Aug 2026 — Design's *Going further*,
        # verbatim, both paragraphs. What had been here was different
        # content of this lane's own: good physics, and not hers, and
        # "a different example" is not a defect anyone can name.
        {"id": "sound-going-faster-in",
         "type": "explainer",
         "text": "Sound going faster in solids is what makes a stethoscope, "
                 "a train-track trick and a whole branch of engineering "
                 "work. Ultrasonic testers send a pulse into a steel "
                 "casting and time what comes back: a crack inside sends a "
                 "reflection home early, and the timing gives its depth to "
                 "within a millimetre. Nobody has to cut the casting open."},
        {"id": "the-speed-in-air",
         "type": "explainer",
         "text": "The speed in air is not quite a constant. It rises with "
                 "temperature, by roughly 0.6 m/s for every degree Celsius, "
                 "because warmer particles are already moving faster and "
                 "hand the shove on more quickly. On a hot day sound "
                 "outruns its cold-morning self by several metres a second, "
                 "and on a cold clear night the layer of warm air above can "
                 "bend sound back down to the ground and carry a distant "
                 "conversation much further than it has any right to go."},
    ],

    "support": [],

    "vocabulary": [
        {"term": "medium",
         "definition": "The material a wave travels through. Sound needs "
                       "one; a vacuum is the absence of one."},
        {"term": "vacuum",
         "definition": "A space with no particles in it. Sound cannot cross "
                       "one at all — not slowly, not faintly."},
        {"term": "speed of sound",
         "definition": "How fast the disturbance travels through a "
                       "particular material. A property of the material, not "
                       "of the note."},
    ],

    "tutor": {
        "anchor": "s-range",
        "prompt": "Ask Mr Badmus AI",
        "body": "Got a gap of your own to time?",
        "cta": "Ask about this lesson"},

    "ks4_becomes": "Measuring the speed of sound in air and in solids, "
                   "ultrasound imaging and non-destructive testing, and the "
                   "wave equation applied to sound.",

    "convention_note": "The bench is a teaching model. Every speed in it is "
                       "an approximate value for one ordinary sample at about "
                       "20 degrees Celsius: air varies by roughly 0.6 m/s per "
                       "degree, sea water differs from fresh, oak differs "
                       "across the grain from along it, and steel differs "
                       "with its alloy. The particle drawings show relative "
                       "spacing only and are not to scale in size or number, "
                       "and real particles are in constant random motion "
                       "rather than in rows. The gap is treated as filled "
                       "with one material end to end, with no losses, so the "
                       "blow arrives at full strength however far away it is; "
                       "over long distances in real air a sound both spreads "
                       "out and is absorbed.",

    "ws": ["measurement"],
}
