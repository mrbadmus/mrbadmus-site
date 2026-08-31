"""P6 L7 — Echoes, reflection and absorption (PROCESS).

Authored against Claude Design's approved page,
`docs/ks3/design-reference/p6/p6-07-echoes-reflection-and-absorption.dc.html`.

Her page wins outright. The cliff, the five surfaces, the bar, both worked
examples and all four rungs are hers.

── ⚖️ MRB-204 · A BAR, AND SHE DREW IT AS ONE ───────────────────────

The total path is `s = d + d`. That is a SUM, not a product, so MRB-204
forbids the triangle and requires a part-whole bar — and Design's own
drawing is a bar with two equal parts, captioned *"Two parts side by side
make the whole."* Nothing to correct. It is worth recording that she got
this right unprompted, because it is the one shape in the unit a
find-and-replace would have got wrong.

── ⚖️ CONSIDERED, NOT CHANGED · `d = s − d` ─────────────────────────

The bar's generic cover-rule reads `d = s − d`, which is true but circular
as a recipe. Her page resolves it in the very next line — *"Both parts are
equal, so d = s ÷ 2"* — and every worked example, every rung and the key
fact use `d = s ÷ 2`. The generic rule is the BAR's rule, correct for any
part-whole bar; the special case is named on the same card. Nothing is
wrong, so nothing changes. Row logged in `DEPARTURES-P6.md`.

── ⚖️ RULED · THE VERDICT NAMES WHICH CONDITION FAILED ──────────────

An echo needs enough sound back AND enough delay. `r_echo_range` refuses a
payload without all three branches — `too_quiet`, `too_close`, `heard` —
because a single verdict word lets a student in a bedroom conclude the
room is too small and in a sports hall that the walls are too soft.

── ⚠️ FOUR RAIL STOPS ────────────────────────────────────────────────

    s-hook · s-cliff · s-bar · s-ladder

⚠️ **MRB-208** — `s-bar` goes on the attempt panel, and the surfaces
figure at `#s-figure` is NOT a stop. Design's rail has four entries and
the figure is not one of them.

⚖️ **THE BAND IS TICKED BY THE BENCH.** `#s-figure` carries no control, so
`echo-range` marks it through `data-sibling`. `mirrors` would tick it late.

── ⚖️ FOUR MISCONCEPTIONS ────────────────────────────────────────────

    WAVE-25  an echo is a new sound the wall makes
    WAVE-26  soft materials stop sound travelling
    WAVE-27  the echo distance is the whole path
    WAVE-28  a small room gives no echo because sound cannot fit in it
"""

LESSON = {
    "slug":  "echoes-reflection-and-absorption",
    "title": "Echoes, reflection and absorption",
    "discipline": "physics",
    "unit": "Waves and sound",
    "family": "PROCESS",

    "covers": ["KS3.P.SND.01b"],
    "touches": [],
    "beyond_statutory": False,
    "threads": [{"id": "waves", "level": 3}],
    "typical_year": 8,
    "typical_minutes": 60,

    "requires": ["sound-needs-a-medium"],
    "assumes": [],
    "references": ["transverse-waves-and-superposition", "ultrasound-at-work",
                   "waves-on-water"],
    "ks4_links": [],

    "meta_description": "The same shout comes straight back at you off a "
                        "cliff and vanishes without trace in a bedroom. Two "
                        "things decide which: what the surface is made of, "
                        "and how far away it is.",

    "big_question": "The same shout comes straight back at you off a cliff "
                    "and vanishes without trace in a bedroom. Two things "
                    "decide which happens: what the surface is made of, and "
                    "how far away it is.",

    "rail": [
        {"anchor": "s-hook",   "short": "SHOUT",
         "label": "Shout at a cliff", "done_when": "committed"},
        {"anchor": "s-cliff",  "short": "CLIFF",
         "label": "Move the wall",    "done_when": "gate_and_a_control"},
        {"anchor": "s-bar",    "short": "CFIFA",
         "label": "The bar and five steps",
         "done_when": "attempt_checked"},
        {"anchor": "s-ladder", "short": "LADDER",
         "label": "Mastery ladder",   "done_when": "ladder_complete"},
    ],

    "phenomenon": {
        "kind": "narrative",
        "title": "Shout at a cliff and count.",
        "prompt": "Stand a few hundred metres from a rock face on a still "
                  "day and shout once. A moment later your own voice comes "
                  "back at you, a little quieter and unmistakably yours. "
                  "Shout the same word in a carpeted bedroom and nothing "
                  "comes back at all.",
        "commit": "You are 170 m from the cliff and the echo reaches you "
                  "1.0 s after you shout. How far has the sound travelled "
                  "in that second?",
        "options": [
            "It depends on how loudly you shout",
            "170 m — the distance out to the cliff",
            "85 m — half the distance, the return half",
            "340 m — out to the cliff and back again",
        ],
        "answer": 3,
        "reveal": "The sound made two journeys of 170 m: out to the cliff, "
                  "and back to you. So it covered 340 m in that second — "
                  "which is exactly the speed of sound in air. <strong>The "
                  "total path is always twice the distance to the "
                  "surface</strong>, and forgetting to halve is the "
                  "commonest way to get an echo question wrong.",
    },

    "misconceptions": [
        {"id": "WAVE-25",
         "statement": "An echo is a new sound the wall makes.",
         "elicited_by": "s-hook",
         "confronted_by": "s-think"},
        {"id": "WAVE-26",
         "statement": "Soft materials stop sound travelling.",
         "confronted_by": "s-think"},
        # ⚖️ HER WORDING, from `NOTES-P6-P7.md` §7, not a paraphrase of it.
        # She pre-allocated WAVE-01…WAVE-36 and authored 22 of them; every
        # one she wrote is used exactly as she wrote it, and only the gaps
        # are minted here from the real lesson content.
        {"id": "WAVE-27",
         "statement": "The distance to the cliff is speed × time.",
         "elicited_by": "s-hook",
         "confronted_by": "your-turn-echo"},
        {"id": "WAVE-28",
         "statement": "A small room gives no echo because there is not "
                      "enough room for the sound.",
         "elicited_by": "s-ladder",
         "confronted_by": "cliff"},
    ],

    "core": [
        {"type": "hook", "id": "hook-commit", "anchor": "s-hook"},

        {"type": "explainer",
         "text": "Sound that meets a surface does one of three things, and "
                 "usually all three at once. Some of it is "
                 "<strong>reflected</strong> — sent back the way it came. "
                 "Some of it is <strong>absorbed</strong> — its energy taken "
                 "up by the material and turned into a tiny amount of "
                 "heating. Some of it is <strong>transmitted</strong>, "
                 "carrying on into and through the material."},
        {"type": "explainer",
         "text": "An <strong>echo</strong> is reflected sound arriving back "
                 "at you late enough to be heard as a separate sound. Two "
                 "things have to be true. Enough of it has to come back: a "
                 "hard, flat, heavy surface reflects most of what hits it, "
                 "while something soft and open-textured absorbs most of it. "
                 "And it has to take long enough: if the reflection returns "
                 "within about a tenth of a second your ear runs it together "
                 "with the original and hears one sound, a bit fuller. Since "
                 "sound covers about 340 m every second, that tenth of a "
                 "second means the surface has to be roughly 17 m away or "
                 "more."},

        # ── #s-cliff · the echo bench ──────────────────────────────────
        {"type": "echo-range",
         "id": "cliff",
         "anchor": "s-cliff",
         "eyebrow": "At the bench · one shout, one flat surface, a stopwatch",
         "heading": "Move the wall. Change the wall.",
         "progress": "Change a control to begin",
         "lead": "One shout in still air, and a flat surface facing you. Set "
                 "how far away it is, and set what it is made of.",
         "v": 340,
         "min_frac": 15,
         "min_time": 0.10,
         "start_surf": 0,
         "surf_label": "What the surface is",
         # ⚠️ NO BAND SIBLING HERE, AND IT IS WORTH SAYING WHY. `#s-figure`
         # carries the five-surface chart, and Design's RAIL for this page
         # is four entries — s-hook, s-cliff, s-bar, s-ladder — with the
         # figure NOT among them. A sibling would tick a stop that is not
         # on the rail. `p6-08` and `p6-09` do have one, because on those
         # two pages the band section IS a stop.
         "gate": {
             "prompt": "Commit first. You move twice as far from the same "
                       "rock face and shout again. What happens to the time "
                       "before the echo returns?",
             "options": [
                 "It halves, because you are further from the reflection",
                 "It is four times as long, because both journeys have "
                 "doubled",
                 "It stays the same, because the speed of sound has not "
                 "changed",
                 "It doubles, because the sound has twice as far to go each "
                 "way",
             ],
             "answer": 3,
         },
         "dist": {"label": "How far away the surface is", "min": 10,
                  "max": 500, "step": 10, "start": 170, "value": "170 m"},
         "surfaces": [
             {"id": "rock", "label": "Bare rock", "frac": 90,
              "caption": "BARE ROCK — HARD, FLAT AND HEAVY",
              "use": "a quarry face"},
             {"id": "brick", "label": "Brick wall", "frac": 70,
              "caption": "BRICK WALL — HARD BUT SLIGHTLY POROUS",
              "use": "a bare sports hall"},
             {"id": "grass", "label": "Mown grass", "frac": 20,
              "caption": "MOWN GRASS — SOFT AND OPEN-TEXTURED",
              "use": "a playing field"},
             {"id": "curtain", "label": "Heavy curtain", "frac": 10,
              "caption": "HEAVY CURTAIN — SOFT, THICK AND FOLDED",
              "use": "a theatre"},
             {"id": "foam", "label": "Foam wedges", "frac": 3,
              "caption": "FOAM WEDGES — BUILT TO ABSORB",
              "use": "a recording booth"},
         ],
         # ⚖️ THREE BRANCHES. The verdict says WHICH condition failed.
         "branches": {
             # ⊕ PHASE 3, 25 Aug 2026 — HER three notes, verbatim, with this
             # engine's token names. Hers were in her page's JS, which the
             # HTML comparison could not see, so the port had written its own.
             "too_quiet":
                 "{surf} sends only about {frac}% of the sound back, and "
                 "below roughly 15% there is not enough returning to hear "
                 "as a separate sound. The timing is not the problem: at "
                 "{dist} m the reflection would arrive {time} s after you "
                 "shout, which is late enough. Put bare rock at the same "
                 "{dist} m and about 90% comes back, and you hear it.",
             "too_close":
                 "At {dist} m the reflection is back in {time3} s, and your "
                 "ear runs anything inside about 0.10 s together with the "
                 "original. Plenty is coming back — about {frac}% off "
                 "{lower} — so the room sounds live rather than silent. "
                 "Move out past about 17 m and the same reflection "
                 "separates into an echo.",
             "heard":
                 "About {frac}% of your shout comes back off {lower}, and "
                 "the journey is {dist} m out and {dist} m back — {path} m "
                 "in all, which at about 340 m/s takes {time} s. Both "
                 "conditions are met: enough returns, and it returns late "
                 "enough to hear on its own.",
         },
         "readouts": [
             {"id": "dist", "label": "Distance to the surface",
              "sub": "in still air at about 340 m/s"},
             {"id": "path", "label": "Total path, out and back"},
             {"id": "time", "label": "Time before it returns"},
             {"id": "verdict", "label": "What you hear"},
         ]},

        # ── #s-figure · the five surfaces, side by side ────────────────
        {"type": "wave-band",
         "id": "surfaces-figure",
         "anchor": "s-figure",
         "eyebrow": "The figure",
         "heading": "Five surfaces, one shout each",
         "bars": {
             "aria_label": "A bar chart of five surfaces against roughly how "
                           "much of a shout each one sends back. Bare rock "
                           "about 90 per cent, brick wall about 70, mown "
                           "grass about 20, heavy curtain about 10 and foam "
                           "wedges about 3. A dashed line at 15 per cent "
                           "marks the level below which no separate echo is "
                           "heard.",
             "axis_label": "ROUGHLY HOW MUCH COMES BACK",
             "name_label": "SURFACE",
             "threshold": 15,
             "threshold_label": "15% — BELOW THIS, NO SEPARATE ECHO",
             "rows": [
                 {"label": "Bare rock",    "pct": 90, "value": "about 90%",
                  "use": "a quarry"},
                 {"label": "Brick wall",   "pct": 70, "value": "about 70%",
                  "use": "a bare sports hall"},
                 {"label": "Mown grass",   "pct": 20, "value": "about 20%",
                  "use": "a playing field"},
                 {"label": "Heavy curtain", "pct": 10, "value": "about 10%",
                  "use": "a theatre, a bedroom"},
                 {"label": "Foam wedges",  "pct": 3,  "value": "about 3%",
                  "use": "a recording booth"},
             ],
         },
         "close": "What sends sound back is hard, flat and heavy. What "
                  "absorbs it is soft and full of holes, so the air can be "
                  "pushed into the gaps and rub its way to a stop. Both ends "
                  "of the list are wanted by somebody: a swimming pool has "
                  "the first problem and a recording booth is built to have "
                  "the second."},

        {"type": "formula",
         "id": "echo-rule",
         "eyebrow": "Writing it down · the shape of this relationship",
         "statement": "Total path = distance + distance",
         # ⚖️ MRB-204 · A SUM TAKES A BAR. Design drew a bar; it stays one.
         # ⚖️ MRB-204 · A SUM TAKES A BAR, AND DESIGN DREW ONE. The total
         # path is `s = d + d`, which is not a product, so the triangle is
         # forbidden and the part-whole bar is what the rule asks for. She
         # got this right before anyone asked, which is worth recording
         # because it is the one shape in the unit a find-and-replace
         # would have got wrong.
         #
         # ⚠️ ONLY THE FIRST PART CARRIES A BUTTON. The two parts are the
         # same distance, so a second button would offer the student a
         # choice with no difference in it.
         "support": ["d · distance to the surface · m",
                     "s · total path, out and back · m"],
         "cover": {
             "shape": "bar",
             "eyebrow": "The bar",
             "heading": "Cover the one you want",
             "aria_label": "A bar model. One long bar is the total path the "
                           "shout takes, out and back. Underneath, the same "
                           "length is split into two equal parts, each the "
                           "distance to the surface. Covering one leaves "
                           "the way to work it out.",
             "whole": {"id": "s", "label": "s — out and back",
                       "button": "Cover s"},
             "parts": [
                 {"id": "d1", "label": "d", "button": "Cover d",
                  "weight": 1},
                 {"id": "d2", "label": "d", "weight": 1},
             ],
             "covered": "d1",
             "results": {
                 "s": {"result": "s = d + d",
                       "sentence": "Cover the whole bar and the two equal "
                                   "parts are left side by side — add "
                                   "them."},
                 "d1": {"result": "d = s − d",
                        "sentence": "Cover one part and the whole bar and "
                                    "the other part are left. Both parts "
                                    "are equal, so this is the same as "
                                    "d = s \u00f7 2 — and that is the form "
                                    "every echo calculation uses."},
                 "d2": {"result": "d = s − d",
                        "sentence": "The same either way round: the two "
                                    "parts are the same distance, because "
                                    "the sound comes back the way it "
                                    "went."},
             },
             "close": "Two parts side by side make the whole. Cover the part "
                      "you want and take the other one away from the whole "
                      "— and because the sound comes back the way it went, "
                      "the two parts are always equal, so d = s \u00f7 2.",
         }},

        {"type": "worked-example", "id": "cfifa-echo-plain"},
        {"type": "worked-example", "id": "cfifa-echo-convert"},
        {"type": "check", "id": "your-turn-echo", "anchor": "s-bar"},

        {"type": "key-fact", "ref": "what-an-echo-needs"},

        {"type": "misconception", "id": "think-wall-makes-sound",
         "anchor": "s-think"},

        {"type": "quiz", "anchor": "s-ladder"},
        {"type": "summary", "id": "s-keynote"},
    ],

    "activities": [
        {"id": "cfifa-echo-plain",
         "kind": "worked-example",
         "demand": "calculate",
         "eyebrow": "Worked example · one step at a time",
         "heading": "A cliff echo comes back 2.0 s after you shout. In that "
                    "time the sound covers 680 m. How far away is the cliff?",
         "head_counter": {"format": "Step {n} of 5", "total": 5},
         "buttons": {"first": "Show the first step",
                     "next": "Show the next step",
                     "done": "All five shown",
                     "done_note": "Nothing needed converting there. Now the "
                                  "one that does."},
         "staged": True,
         "fifa": [
             {"letter": "C", "label": "Convert", "line": "680 m stays 680 m",
              "note": "The distance is already in metres and the answer is "
                      "wanted in metres, so there is nothing to convert."},
             {"letter": "F", "label": "Formula", "line": "d = s ÷ 2",
              "note": "The shout goes out and comes back, so the total path "
                      "is two equal helpings of the distance."},
             {"letter": "I", "label": "Insert", "line": "d = 680 m ÷ 2",
              "note": "The 680 m is the whole journey, out to the cliff and "
                      "back — not the distance to the cliff."},
             {"letter": "F", "label": "Fine-tune", "line": "680 ÷ 2 = 340",
              "note": "Metres divided by a plain number leaves metres."},
             {"letter": "A", "label": "Answer", "line": "d = 340 m",
              "note": "Forgetting to halve is the commonest way to get this "
                      "wrong."},
         ]},

        {"id": "cfifa-echo-convert",
         "kind": "worked-example",
         "demand": "calculate",
         "eyebrow": "Worked example · one step at a time",
         "heading": "An echo returns after the sound has travelled 1.02 km. "
                    "How far away is the wall?",
         "head_counter": {"format": "Step {n} of 5", "total": 5},
         "buttons": {"first": "Show the first step",
                     "next": "Show the next step",
                     "done": "All five shown",
                     "done_note": "Convert first, then the same four lines. "
                                  "Your turn below, on your own wall."},
         "staged": True,
         "fifa": [
             {"letter": "C", "label": "Convert",
              "line": "1.02 km × 1000 = 1020 m",
              "note": "The answer is wanted in metres, and a kilometre is a "
                      "thousand of them."},
             {"letter": "F", "label": "Formula", "line": "d = s ÷ 2",
              "note": "Out and back, so the path is two equal helpings of "
                      "the distance."},
             {"letter": "I", "label": "Insert", "line": "d = 1020 m ÷ 2",
              "note": "The converted total goes in. The 1.02 never does."},
             {"letter": "F", "label": "Fine-tune", "line": "1020 ÷ 2 = 510",
              "note": "Metres divided by a plain number leaves metres."},
             {"letter": "A", "label": "Answer", "line": "d = 510 m",
              "note": "Halve 1.02 instead and the answer comes out 0.51 m — "
                      "half a metre from a wall you shouted at."},
         ]},

        {"id": "your-turn-echo",
         "kind": "p6-attempt",
         "demand": "calculate",
         "eyebrow": "Your turn · the same five steps",
         "rest": {"dist": 170, "path": 340, "time": "1.00"},
         "questions": [
             {"id": "q1", "tab": "Question 1",
              # ⊕ PHASE 3, 25 Aug 2026 — HER question, her lines and
              # her notes, with this engine's token names in place of
              # her state expressions.
              "head": "Your surface is {dist} m away.",
              "lead": "Write all five lines before you check. The distance "
                      "is the one your own bench is showing.",
              "steps": [
                  {"letter": "C", "label": "Convert",
                   "placeholder": "anything to convert?",
                   "line": "the round trip is already in metres",
                   "note": "The bench gives the whole path in metres and "
                           "the answer is wanted in metres, so there is "
                           "nothing to convert."},
                  {"letter": "F", "label": "Formula",
                   "line": "s = d + d",
                   "note": "Two equal parts, out and back, make the whole "
                           "path."},
                  {"letter": "I", "label": "Insert",
                   "line": "s = {dist} m + {dist} m",
                   "note": "Both parts are the distance to the surface, "
                           "which your slider sets."},
                  {"letter": "F", "label": "Fine-tune",
                   "line": "{dist} + {dist} = {path}",
                   "note": "Metres added to metres leave metres."},
                  {"letter": "A", "label": "Answer",
                   "line": "s = {path} m",
                   "note": "At about 340 m/s that takes {time} s, which is "
                           "what the stopwatch on the bench reads."},
              ],
              "close": "The five lines above give {path} m for a surface "
                       "{dist} m away."},
             {"id": "q2", "tab": "Question 2",
              # ⊕ PHASE 3, 25 Aug 2026 — HER question, not one of
              # ours. The port had written a different second
              # question here with different numbers; hers is the
              # one a student is meant to meet.
              "head": "A sonar ping covers 2.4 km on its round trip to the "
                      "sea bed and back. How deep is the water?",
              "lead": "This one needs the Convert line to do some "
                      "work.",
              "steps": [
                  {"letter": "C", "label": "Convert",
                   "placeholder": "anything to convert?",
                   "line": "2.4 km × 1000 = 2400 m",
                   "note": "The answer is wanted in metres, so multiply the "
                           "kilometres by 1000."},
                  {"letter": "F", "label": "Formula",
                   "line": "d = s ÷ 2",
                   "note": "Down and back, so the path is two equal "
                           "helpings of the depth."},
                  {"letter": "I", "label": "Insert",
                   "line": "d = 2400 m ÷ 2",
                   "note": "The converted total goes in. The 2.4 never "
                           "does."},
                  {"letter": "F", "label": "Fine-tune",
                   "line": "2400 ÷ 2 = 1200",
                   "note": "Metres divided by a plain number leaves metres."},
                  {"letter": "A", "label": "Answer",
                   "line": "d = 1200 m",
                   "note": "Halve 2.4 instead and the sea bed comes out 1.2 "
                           "m down."},
              ],
              "close": "The five lines give 1200 m. The whole question "
                       "turned on the first one."},
         ]},

        {"id": "think-wall-makes-sound",
         "kind": "predict",
         "demand": "explain",
         "targets": "WAVE-25",
         "statements": [
             {"quote": "An echo is a new sound the wall makes.",
              "targets": "WAVE-25",
              "body": [
                  "The wall makes nothing. Your shout arrives, pushes on "
                  "the surface, and most of it is sent straight back the "
                  "way it came \u2014 which is why an echo is recognisably "
                  "your own voice, your own words, in your own accent, and "
                  "why it is a little quieter rather than a little "
                  "different. A wall that made sounds of its own would be a "
                  "very odd wall, and it would still be making them when "
                  "you were silent.",
              ]},
             {"quote": "Soft materials stop sound travelling.",
              "targets": "WAVE-26",
              "body": [
                  "Soft materials absorb sound, which is not the same as "
                  "stopping it. Absorbing means the energy is taken up by "
                  "the material and ends as a very small amount of heating; "
                  "the sound stops existing rather than being turned back. "
                  "Blocking is a different job and is done by mass, not "
                  "softness: a thin foam panel kills an echo beautifully "
                  "and does almost nothing to stop your neighbour hearing "
                  "the television, while a solid brick wall does the "
                  "opposite. A recording studio needs both, and uses "
                  "different materials for each.",
              ]},
         ]},
    ],

    "figures": [],

    "key_facts": [
        {"id": "what-an-echo-needs",
         "eyebrow": "Key fact",
         "ground": "card",
         "placement": "top-level",
         "text": "An echo is sound reflected back and heard as a separate "
                 "sound. It needs a surface that sends enough of it back — "
                 "hard, flat and heavy rather than soft and open — and it "
                 "needs the surface to be far enough away, roughly 17 m or "
                 "more in air, so that the reflection arrives more than about "
                 "a tenth of a second late. The sound travels out and back, "
                 "so the total path is twice the distance to the surface."},
    ],

    # ⚠️ MRB-278 · POSITION IS AUTHORED. This lesson takes indices 3 and 0.
    "ladder": {
        "recall": {
            "q": "You shout at a cliff and the echo returns 3.0 s later. "
                 "Sound travels at about 340 m/s in air. How far away is "
                 "the cliff?",
            "options": [
                "About 113 m — divide the speed by the time",
                "About 255 m — halve the time first, then halve the "
                "distance",
                "About 1020 m — multiply the speed by the time and that is "
                "the distance to the cliff",
                "About 510 m — 340 m/s for 3.0 s is the there-and-back "
                "path, so halve it",
            ],
            "answer": 3,
            "feedback": {
                0: "That is the calculation upside down, and it gives "
                   "metres per second squared rather than metres. Distance "
                   "is speed multiplied by time.",
                1: "Halving twice takes a quarter. Do one or the other: "
                   "either halve the time to get 1.5 s each way, or work "
                   "out the whole 1020 m path and halve that.",
                2: "That is the whole journey, out and back. The sound "
                   "reached the cliff halfway through, so the distance to "
                   "it is half of the 1020 m.",
            },
            "title": "Rung 1 · Calculate"},
        "apply": {
            "q": "A bedroom with a carpet, curtains and a bed gives no echo "
                 "at all. Which statement is right?",
            "options": [
                "The soft surfaces absorb most of the sound instead of "
                "reflecting it, and the room is also too small for a "
                "reflection to arrive late enough to be heard separately.",
                "Sound cannot travel through a room full of soft things.",
                "There is no echo because the room is warm, and warm air "
                "absorbs sound.",
                "The sound is reflected just as strongly as in a sports "
                "hall, but the walls are too close for you to notice it, "
                "because how much comes back off a surface is the same "
                "whatever the surface is made of",
            ],
            "answer": 0,
            "feedback": {
                1: "Sound crosses the room perfectly well — you can hear "
                   "someone talking in it. What the soft surfaces change is "
                   "how much comes back off them.",
                2: "Temperature changes the speed of sound slightly and "
                   "does not absorb it. The absorbing is done by the "
                   "carpet, curtains and bedding.",
                3: "Half right, and the half that is missing matters. The "
                   "distance really is too short, but soft furnishings also "
                   "send far less back — an empty room the same size sounds "
                   "noticeably live.",
            },
            "title": "Rung 2 · The one that catches people"},
        "explain": {
            "q": "A school sports hall with bare brick walls and a hard "
                 "floor is so echoey that announcements are hard to make "
                 "out. Explain why, and describe one change that would fix "
                 "it and why it would work.",
            "field_label": "Your explanation",
            "placeholder": "The hard walls…",
            "success": [
                "Says hard, flat, heavy surfaces reflect most of the sound "
                "that hits them.",
                "Says the reflections arrive after the original sound, so "
                "words overlap with earlier words.",
                "Says the hall is large enough for the delay to be long "
                "enough to hear as separate sound.",
                "Names a soft, open-textured material to add — curtains, "
                "carpet, acoustic panels or similar.",
                "Says that material absorbs the sound instead of reflecting "
                "it, so less comes back.",
            ],
            "title": "Rung 3 · Explain"},
        "produce": {
            "q": "A ship measures the depth of the sea by sending a pulse "
                 "of sound straight down and timing what comes back. The "
                 "pulse returns after 0.40 s, and sound travels at about "
                 "1500 m/s in sea water. Work out the depth, and say why "
                 "the answer would be wrong if you forgot that the pulse "
                 "makes two journeys.",
            "field_label": "Your answer",
            "placeholder": "The total path is speed × time…",
            "success": [
                "Works out the total path as about 1500 × 0.40 = 600 m.",
                "Says that 600 m is down to the sea bed and back up again.",
                "Halves it to give a depth of about 300 m, with the unit.",
                "Says forgetting to halve would give 600 m, twice the real "
                "depth.",
                "Uses the speed of sound in water rather than in air, and "
                "says why that matters here.",
            ],
            "title": "Rung 4 · Take it somewhere new"},
    },

    "key_note": "Sound meeting a surface is partly reflected, partly absorbed "
                "and partly transmitted. An echo is reflected sound heard as "
                "a separate sound, and it needs both a surface that sends "
                "enough back — hard, flat and heavy rather than soft and open "
                "— and a distance of roughly 17 m or more, so the reflection "
                "arrives more than about a tenth of a second late. The sound "
                "travels out and back, so the total path is twice the "
                "distance to the surface.",

    "stretch": [
        {"id": "timing-an-echo-measures-the-world",
         "type": "explainer",
         "text": "Timing an echo is how a great deal of the world gets "
                 "measured. A ship's echo sounder pings the sea bed and "
                 "halves the answer; a bat does the same thing in air, fast "
                 "enough to catch a moth in flight; an ultrasound scanner "
                 "reads the reflections from the boundaries inside a body. "
                 "<strong>Every one of them has to halve</strong>, and every "
                 "one of them has to know the speed of sound in the material "
                 "it is looking through — which is why a scanner set up for "
                 "soft tissue would misplace everything if it were used on "
                 "bone."},
        {"id": "designing-a-room-for-sound",
         "type": "explainer",
         "text": "Designing a room for sound is a balancing act rather than "
                 "a hunt for silence. A concert hall with no reflections at "
                 "all sounds dead and lifeless, and musicians hate it; a "
                 "hall with too many sounds like a swimming pool. Architects "
                 "aim for a reverberation time — how long a sound takes to "
                 "die away — of roughly two seconds for an orchestra, under "
                 "a second for speech, and they get there by choosing how "
                 "much of each surface is hard and how much is soft. Nothing "
                 "about it stops sound reaching the audience; it only "
                 "controls how much of it arrives late."},
    ],

    "support": [],

    "vocabulary": [
        {"term": "reflected",
         "definition": "Sent back the way it came when it meets a surface."},
        {"term": "absorbed",
         "definition": "Taken up by the material and turned into a very "
                       "small amount of heating, so the sound stops "
                       "existing."},
        {"term": "transmitted",
         "definition": "Carried on into and through the material rather than "
                       "sent back."},
        {"term": "echo",
         "definition": "Reflected sound arriving late enough to be heard as "
                       "a separate sound."},
    ],

    "tutor": {
        "anchor": "s-cliff",
        "prompt": "Ask Mr Badmus AI",
        "body": "Got an echo to time, or a room that sounds wrong?",
        "cta": "Ask about this lesson"},

    "ks4_becomes": "Reverberation time, ultrasound and echo sounding "
                   "calculations, and the reflection, absorption and "
                   "transmission of waves at a boundary.",

    "convention_note": "The bench is a teaching model. The percentages of "
                       "sound sent back are round teaching figures for a "
                       "typical surface of each kind: real reflection depends "
                       "strongly on the frequency of the sound and on the "
                       "angle it arrives at, and a curtain that absorbs a "
                       "high note well may do almost nothing to a low one. "
                       "The 15% below which no separate echo is heard, and "
                       "the tenth of a second inside which your ear runs two "
                       "sounds together, are both approximate thresholds "
                       "fixed here so that the states can be reached and "
                       "compared. The speed of sound is taken as about 340 "
                       "m/s, its value in air at around 20 degrees Celsius. "
                       "The surface is treated as flat and facing you "
                       "squarely, with no sound lost on the way there and "
                       "back; over hundreds of metres a real shout both "
                       "spreads and is absorbed by the air.",

    "ws": ["measurement"],
}
