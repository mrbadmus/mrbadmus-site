"""P4 L8 — Springs and Hooke's law (INVESTIGATION).

Authored against Claude Design's approved page,
`docs/ks3/design-reference/p4/p4-08-springs-and-hookes-law.dc.html`.

Her page wins outright. The 10 N prediction, the loading bench, the beam
and graph, both worked examples and all four rungs are hers.

── ⚖️ MRB-204 · A BEAM AND A GRAPH, NOT A TRIANGLE ───────────────────

`extension ∝ load` is a PROPORTIONALITY read off a straight line — two
quantities keeping the same ratio — not a three-quantity product. Design
draws bars (three newtons of extension is three equal helpings of one
newton's worth) beside a graph, and writes the reason into the block. A
triangle over `extension`, `load` and `mm per newton` would be arithmetic
that works and pedagogy that lies: the mm-per-newton is not a third
measured quantity, it is the ratio itself.

── ⚖️ RULED · THE GRAPH SHOWS ONLY RECORDED READINGS ─────────────────

Design plots the points the student chose to record and nothing else, so
an incomplete investigation LOOKS incomplete. A bench that drew the whole
curve on load would answer the question the investigation exists to ask
— where does the line stop being straight — before a single reading was
taken. The rail does not count the bench done until two readings are
plotted, and `r_spring_plot` refuses a target below two: one point defines
no line.

── ⚖️ RULED · THE RISK ASSESSMENT STAYS ON THE PAGE ──────────────────

Design's flag 6. This is the unit's only risk assessment and its only
piece of instructional prose — everywhere else a practical is described,
not instructed. Finding a limit of proportionality means loading a spring
until it stops behaving, so the block is a real safety requirement rather
than a formality: eye protection, a padded landing, nothing underneath the
hanger, a clamped or weighted stand, and loading to destruction as a
screened demonstration rather than a class activity.

It is a **deliberate departure from describe-don't-instruct**, and it is
kept because the alternative is a page that tells a class to overload a
spring and says nothing about the spring leaving at speed. A reviewer
should either ratify it or move the block into teacher-facing material.
It ships through the engine's `safety_note` slot, which puts it in the
foot with `ks3-safety` treatment.

⊕ **AMENDED IN THE PORT, AND THIS IS A REGISTER ROW.** Design draws the
five lines as an amber callout ABOVE the formula block. The engine has no
amber-callout block type and inventing one for a single page would be an
MRB-205 violation in the other direction. The five lines are unchanged,
in order, and land in the `safety_note` foot slot instead. See
`DEPARTURES-P4.md`.

── ⚖️ RULED · "WHILE THE SPRING OBEYS HOOKE'S LAW" IS NOT TIDIED ─────

Every scaling-up sentence carries the clause. Without it the statement is
FALSE above 6 N, and the page's own bench disproves it — which would be
a page contradicting its own instrument.

── ⚠️ FOUR RAIL STOPS ────────────────────────────────────────────────

    s-hook · s-bench · s-formula · s-ladder

⚠️ **`s-bench` NEEDS TWO PLOTTED READINGS**, not a control touched. Design:
`s.gate !== null && s.readings.length >= 2`.

── ⚖️ FOUR MISCONCEPTIONS ────────────────────────────────────────────

    FORCE-40  extension is how long the spring is
    FORCE-41  double the load always doubles the extension
    FORCE-42  past the limit of proportionality the spring snaps
    FORCE-43  an overstretched spring recovers if you leave it long enough
"""

LESSON = {
    "slug":  "springs-and-hookes-law",
    "title": "Springs and Hooke's law",
    "discipline": "physics",
    "unit": "Forces",
    "family": "INVESTIGATION",

    "covers": ["KS3.P.FORCES.04a", "KS3.P.FORCES.05b",
               "KS3.P.FORCES.06", "KS3.P.FORCES.07"],
    "touches": ["KS3.WS.ANA.01"],
    "beyond_statutory": False,
    "threads": [{"id": "forces", "level": 3}],
    "typical_year": 7,
    "typical_minutes": 75,

    "requires": ["moments"],
    "assumes": [],
    "references": ["balanced-and-unbalanced", "what-a-force-is"],
    "ks4_links": [],

    "meta_description": "A spring turns a force into a length you can read "
                        "with a ruler. Take the readings, plot them, and "
                        "find the load where the straight line gives out.",

    "big_question": "A spring is the only instrument in the lab that turns a "
                    "force into a length you can read with a ruler. It works "
                    "beautifully — right up until it does not.",

    "rail": [
        {"anchor": "s-hook",   "short": "HOOK",
         "label": "Predict 10 N",     "done_when": "committed"},
        {"anchor": "s-bench",  "short": "PLOT",
         "label": "Loading a spring", "done_when": "two_readings_plotted"},
        {"anchor": "s-formula", "short": "CFIFA",
         "label": "Beam, graph, five steps",
         "done_when": "attempt_checked"},
        {"anchor": "s-ladder", "short": "LADDER",
         "label": "Mastery ladder",   "done_when": "ladder_complete"},
    ],

    "phenomenon": {
        "kind": "narrative",
        "title": "1 N stretched it 20 mm. 2 N stretched it 40 mm.",
        "prompt": "Two readings, one spring, a ruler clamped alongside it. "
                  "The pattern looks obvious, so make it do some work: "
                  "predict the extension when you hang 10 N on the same "
                  "spring.",
        "commit": "What will the extension be at 10 N?",
        "options": [
            "200 mm — every newton adds another 20 mm, all the way",
            "More than 200 mm — the pattern stops holding at some load",
            "Less than 200 mm — a spring gets harder to stretch as it goes",
            "Nothing — it will have snapped long before 10 N",
        ],
        "answer": 1,
        "reveal": "For the first few newtons the pattern holds exactly: "
                  "every newton adds the same 20 mm, so the extension is "
                  "proportional to the load. But every spring has a load "
                  "beyond which that stops being true, and after that each "
                  "newton adds more than the last. <strong>Two readings can "
                  "tell you the rule. They cannot tell you how far the rule "
                  "goes</strong> — only more readings can do that, which "
                  "is what the bench below is for.",
    },

    "misconceptions": [
        {"id": "FORCE-40",
         "statement": "Extension is how long the spring is.",
         "confronted_by": "s-think"},
        {"id": "FORCE-41",
         "statement": "Double the load always doubles the extension.",
         "elicited_by": "s-hook",
         "confronted_by": "plot"},
        {"id": "FORCE-42",
         "statement": "Past the limit of proportionality the spring snaps.",
         "elicited_by": "s-hook",
         "confronted_by": "s-think"},
        {"id": "FORCE-43",
         "statement": "An overstretched spring goes back to its natural "
                      "length if you leave it long enough.",
         "elicited_by": "s-ladder",
         "confronted_by": "s-ladder"},
    ],

    "core": [
        {"type": "hook", "id": "hook-commit", "anchor": "s-hook"},

        {"type": "explainer",
         "text": "<strong>Extension</strong> is how much longer the spring "
                 "has become, not its total length: extension = stretched "
                 "length − natural length. While the extension is "
                 "proportional to the load, the spring is obeying "
                 "<strong>Hooke's law</strong>, and a graph of extension "
                 "against load is a straight line through the origin. The "
                 "load where that stops is the <strong>limit of "
                 "proportionality</strong>."},

        # ── #s-bench · loading a spring ────────────────────────────────
        {"type": "spring-plot",
         "id": "plot",
         "anchor": "s-bench",
         "eyebrow": "At the bench · loading a spring",
         "heading": "Take the readings. Plot them. Find where it bends.",
         "progress": "No readings plotted yet",
         "lead": "One spring, a clamped ruler, and loads from 0 to 10 N. Set "
                 "a load, record the reading, and the point goes on the "
                 "graph. The dashed line is the straight line the first "
                 "readings make.",
         "per_n": 20,
         "limit": 6,
         "spoil": 9,
         "past": 32,
         "target": 2,
         "load": {"label": "Load on the spring", "min": 0, "max": 10,
                  "step": 1, "start": 2},
         "record_label": "Record this reading",
         "clear_label": "Clear the readings",
         "x_label": "Load in newtons",
         "y_label": "Extension in millimetres",
         "gate": {
             "prompt": "Commit first. Which two readings would you take to "
                       "test whether the extension is proportional to the "
                       "load?",
             "options": [
                 "Two readings anywhere — any two will show the pattern",
                 "The zero reading and one more, so the line has a starting "
                 "point",
                 "As many as possible, spread across the range, including "
                 "zero",
                 "Two readings at the same load, to check they agree",
             ],
             "answer": 2,
         },
         "branches": {
             "zero": "No load, no extension — and this reading matters as "
                     "much as any of them. It is the zero the whole "
                     "investigation is measured from, and a graph plotted "
                     "without it usually goes through the wrong place.",
             "on_line": "{load} N gives {ext} mm, which is 20 mm for every "
                        "newton — the same as every reading before it. On "
                        "the graph the point sits exactly on the dashed "
                        "line, which is what proportional looks like.",
             "at_limit": "At 6 N the extension is {ext} mm, still 20 mm per "
                         "newton and still on the line. This is the last "
                         "reading that obeys Hooke's law: the limit of "
                         "proportionality for this spring. Nothing about the "
                         "spring looks any different.",
             "past_limit": "Past the limit. {load} N gives {ext} mm, but the "
                           "straight line predicted {predicted} mm, so this "
                           "point sits above it — each newton now adds "
                           "32 mm instead of 20 mm. The spring will still "
                           "shorten when you unload it, but not quite all "
                           "the way.",
             "deformed": "Above 9 N this spring is permanently deformed. It "
                         "is at {ext} mm now, and taking the load off will "
                         "not bring it back to where it started — the "
                         "coils have been pulled apart for good. A spring "
                         "balance treated like this reads wrongly at every "
                         "load afterwards.",
         },
         "readouts": [
             {"id": "load", "label": "Load"},
             {"id": "ext", "label": "Extension"},
             {"id": "pern", "label": "Extension per newton"},
             {"id": "verdict", "label": "The spring"},
         ]},

        {"type": "formula",
         "id": "hookes-law",
         "eyebrow": "The relationship · a beam and a graph, not a triangle",
         "statement": "While a spring obeys Hooke's law, extension is "
                      "proportional to load.",
         "support": [
             "extension in mm = stretched length in mm − natural length "
             "in mm",
             "extension ÷ load stays the same for every reading on the "
             "straight line",
             "past the limit of proportionality, that ratio stops being "
             "constant",
         ],
         "figure": {
             "art": "p4-spring-beam",
             # ⊕ PHASE 3, 25 Aug 2026 — Design's caption and note, restored.
             "caption": "Each newton adds the same amount, until it does "
                        "not.",
             "note": "This is a beam and a graph rather than a triangle, "
                     "because what is being taught is a proportionality "
                     "read off a straight line: two quantities that keep "
                     "the same ratio. The bars show it as a part\u2013whole "
                     "\u2014 three newtons of extension is three equal "
                     "helpings of one newton\u2019s worth \u2014 and the "
                     "graph shows the same fact as a straight line through "
                     "the origin, with the bend where the law gives out.",
             "aria_label": "Three bars drawn to one scale. One newton gives "
                           "a bar of twenty millimetres, two newtons gives a "
                           "bar of forty millimetres made of two equal "
                           "parts, and three newtons gives sixty "
                           "millimetres made of three equal parts. Beside "
                           "them, a graph of extension against load is a "
                           "straight line through the origin that bends "
                           "upwards past the limit of proportionality.",
             "title": "EVERY NEWTON, THE SAME 20 mm",
             "per_n": 20,
             "px_per_mm": 5.0,
             "rows": [{"newtons": 1}, {"newtons": 2}, {"newtons": 3}],
             "ratio_line": "extension ÷ load is the same every time",
             "ratio_sums": "20 ÷ 1 = 40 ÷ 2 = 60 ÷ 3 = 20 mm per newton",
             "limit_label": "limit",
             "y_label": "EXTENSION",
             "x_label": "LOAD",
         }},

        {"type": "worked-example", "id": "cfifa-spring-plain"},
        {"type": "worked-example", "id": "cfifa-spring-convert"},
        {"type": "check", "id": "your-turn-spring", "anchor": "s-formula"},

        {"type": "key-fact", "ref": "extension-proportional-to-load"},

        {"type": "misconception", "id": "think-extension-is-length",
         "anchor": "s-think"},

        {"type": "quiz", "anchor": "s-ladder"},
        {"type": "summary", "id": "s-keynote"},
    ],

    "activities": [
        {"id": "cfifa-spring-plain",
         "kind": "worked-example",
         "demand": "calculate",
         "eyebrow": "Worked example · one step at a time",
         "heading": "A spring extends 40 mm under a 2 N load. Staying on the "
                    "straight line, what is the extension under 5 N?",
         "head_counter": {"format": "Step {n} of 5", "total": 5},
         "buttons": {"first": "Show the first step",
                     "next": "Show the next step",
                     "done": "All five shown",
                     "done_note": "Nothing needed converting there. Now the "
                                  "one that does."},
         "staged": True,
         "fifa": [
             {"letter": "C", "label": "Convert",
              "line": "40 mm stays 40 mm · 2 N stays 2 N",
              "note": "Both extensions are in millimetres and both loads in "
                      "newtons, so there is nothing to convert."},
             {"letter": "F", "label": "Formula",
              "line": "extension ÷ load is the same for every reading",
              "note": "That is what proportional means, and it is why the "
                      "graph is a straight line."},
             {"letter": "I", "label": "Insert",
              "line": "extension ÷ load = 40 mm ÷ 2 N",
              "note": "Using the one reading given, and extension means the "
                      "increase in length."},
             {"letter": "F", "label": "Fine-tune",
              "line": "40 ÷ 2 = 20 mm for each newton",
              "note": "Millimetres divided by newtons leaves millimetres per "
                      "newton."},
             {"letter": "A", "label": "Answer",
              "line": "5 N × 20 mm/N = 100 mm",
              "note": "A hundred millimetres, as long as 5 N is still on the "
                      "straight line."},
         ]},

        {"id": "cfifa-spring-convert",
         "kind": "worked-example",
         "demand": "calculate",
         "eyebrow": "Worked example · one step at a time",
         "heading": "A spring extends 6.0 cm under 3 N. Staying on the "
                    "straight line, what is the extension under 8 N, in "
                    "millimetres?",
         "head_counter": {"format": "Step {n} of 5", "total": 5},
         "buttons": {"first": "Show the first step",
                     "next": "Show the next step",
                     "done": "All five shown",
                     "done_note": "Convert first, then the same four lines. "
                                  "Your turn below, on your own readings."},
         "staged": True,
         "fifa": [
             {"letter": "C", "label": "Convert",
              "line": "6.0 cm × 10 = 60 mm",
              "note": "The answer is wanted in millimetres, and a centimetre "
                      "is ten of them, so multiply by 10."},
             {"letter": "F", "label": "Formula",
              "line": "extension ÷ load is the same for every reading",
              "note": "Proportional, so one ratio describes every point on "
                      "the line."},
             {"letter": "I", "label": "Insert",
              "line": "extension ÷ load = 60 mm ÷ 3 N",
              "note": "The converted extension goes in. The 6.0 never does."},
             {"letter": "F", "label": "Fine-tune",
              "line": "60 ÷ 3 = 20 mm for each newton",
              "note": "Millimetres divided by newtons leaves millimetres per "
                      "newton."},
             {"letter": "A", "label": "Answer",
              "line": "8 N × 20 mm/N = 160 mm",
              "note": "Leave the 6.0 in centimetres and the answer reads 16 "
                      "— ten times too small for the unit asked for."},
         ]},

        {"id": "your-turn-spring",
         "kind": "p4-attempt",
         "demand": "calculate",
         "eyebrow": "Your turn · the same five steps",
         # The bench opens at 2 N, which is 40 mm on the straight line.
         # Doubling to 4 N is still under the 6 N limit, so the resting
         # closing line is the one where the proportionality held.
         "rest": {"ext": 40, "load": 2, "dbl": 4, "pern": 20,
                  "predicted": 80,
                  "checkclose": "The five lines predict 80 mm, and setting "
                                "the bench to 4 N gives exactly 80 mm. The "
                                "proportionality held, because both loads "
                                "are on the straight line."},
         "questions": [
             {"id": "q1", "tab": "Question 1",
              "head": "Your reading: {ext} mm under {load} N. Predict the "
                      "extension at {dbl} N.",
              "lead": "Write all five lines before you check, then set the "
                      "bench to {dbl} N and see whether the prediction "
                      "held.",
              "blocked_lead": "Put a load on the spring first — a zero "
                              "reading has nothing to scale up.",
              "steps": [
                  {"letter": "C", "label": "Convert",
                   "placeholder": "anything to convert?",
                   "line": "{ext} mm stays {ext} mm · {load} N stays "
                           "{load} N",
                   "note": "The extension is already in millimetres and the "
                           "load already in newtons, so there is nothing to "
                           "convert."},
                  {"letter": "F", "label": "Formula",
                   "line": "extension ÷ load is the same for every reading",
                   "note": "True while the spring is on the straight line."},
                  {"letter": "I", "label": "Insert",
                   "line": "extension ÷ load = {ext} mm ÷ {load} N",
                   "note": "Both figures come from the reading on your own "
                           "bench."},
                  {"letter": "F", "label": "Fine-tune",
                   "line": "{ext} ÷ {load} = {pern} mm for each newton",
                   "note": "Millimetres divided by newtons leaves "
                           "millimetres per newton."},
                  {"letter": "A", "label": "Answer",
                   "line": "{dbl} N × {pern} mm/N = {predicted} mm",
                   "note": "Double the load, so the prediction is double the "
                           "extension."},
              ],
              "close": "{checkclose}"},
             {"id": "q2", "tab": "Question 2",
              "head": "A spring stretches 2.4 cm under a 4 N load. Staying "
                      "on the straight line, what is the extension under "
                      "10 N, in millimetres?",
              "lead": "This one needs the Convert line to do some work.",
              "steps": [
                  {"letter": "C", "label": "Convert",
                   "placeholder": "anything to convert?",
                   "line": "2.4 cm × 10 = 24 mm",
                   "note": "The answer is wanted in millimetres, so multiply "
                           "the centimetres by 10."},
                  {"letter": "F", "label": "Formula",
                   "line": "extension ÷ load is the same for every reading",
                   "note": "Proportional, so one ratio describes the whole "
                           "line."},
                  {"letter": "I", "label": "Insert",
                   "line": "extension ÷ load = 24 mm ÷ 4 N",
                   "note": "The converted extension goes in. The 2.4 never "
                           "does."},
                  {"letter": "F", "label": "Fine-tune",
                   "line": "24 ÷ 4 = 6 mm for each newton",
                   "note": "Millimetres divided by newtons leaves "
                           "millimetres per newton."},
                  {"letter": "A", "label": "Answer",
                   "line": "10 N × 6 mm/N = 60 mm",
                   "note": "Leave it in centimetres and the answer reads 6 "
                           "— right number, wrong unit, no marks."},
              ],
              "close": "The five lines give 60 mm, provided 10 N is still on "
                       "the straight part of the line."},
         ]},

        {"id": "think-extension-is-length",
         "kind": "predict",
         "demand": "explain",
         "targets": "FORCE-40",
         "statements": [
             {"quote": "Extension is how long the spring is.",
              "targets": "FORCE-40",
              "body": [
                  "It is how much longer it has become. A spring with a "
                  "natural length of 50 mm holding a load at 90 mm has an "
                  "extension of 40 mm, not 90 mm, and a graph plotted with "
                  "total length on the axis does not go through the origin "
                  "— it starts at 50 mm with no load on it at all. That is "
                  "why the first measurement in this investigation is taken "
                  "before anything is hung on the spring, and why the "
                  "sentence <em>extension = stretched length − natural "
                  "length</em> is worth writing out every time until it is "
                  "automatic. <strong>Nearly every wrong Hooke's law graph "
                  "is this mistake.</strong>",
              ]},
             {"quote": "Past the limit, the spring snaps.",
              "targets": "FORCE-42",
              "body": [
                  "The limit of proportionality is not a breaking point, and "
                  "passing it is not dramatic. What stops is the neat "
                  "arithmetic: each extra newton now adds more extension "
                  "than the newton before it, so the graph curves away from "
                  "the straight line, and the spring no longer springs all "
                  "the way back. Take the load off and it is left "
                  "permanently longer than it started, <strong>which is why "
                  "an overstretched spring balance reads wrongly for ever "
                  "afterwards even though it looks perfectly all "
                  "right.</strong> Snapping happens much later, if at all.",
              ]},
         ]},
    ],

    "figures": [],

    "key_facts": [
        {"id": "extension-proportional-to-load",
         "eyebrow": "Key fact",
         "ground": "card",
         "placement": "top-level",
         "text": "While a spring obeys Hooke's law, its extension is "
                 "proportional to the load: a graph of extension against "
                 "load is a straight line through the origin, and every "
                 "newton adds the same extension. Past the limit of "
                 "proportionality the line bends, and the spring may not "
                 "return to its original length."},
    ],

    # ⚠️ MRB-278 · POSITION IS AUTHORED. This lesson takes indices 2 and 3.
    "ladder": {
        "recall": {
            "q": "A spring extends 30 mm under a 3 N load. Staying within "
                 "the straight line, what is its extension under 7 N?",
            "options": [
                "10 mm — divide the extension by the load",
                "70 N — the answer describes how hard the spring pulls",
                "70 mm",
                "34 mm — add the extra 4 N on to the 30 mm",
            ],
            "answer": 2,
            "feedback": {
                0: "10 mm is the extension for one newton, which is a useful "
                   "step. The question asks for seven of them.",
                1: "The arithmetic is right and the quantity is wrong. An "
                   "extension is a length, so it is in millimetres.",
                3: "That treats load and extension as if they add together. "
                   "They are proportional: four extra newtons add four "
                   "helpings of 10 mm.",
            },
            "title": "Rung 1 · Calculate"},
        "apply": {
            "q": "A spring is loaded past its limit of proportionality, then "
                 "the load is taken off completely. What happens?",
            "options": [
                "It goes back to its natural length, because that is what "
                "springs do.",
                "It goes back to its natural length, but takes much longer "
                "to get there.",
                "It snaps, because the limit of proportionality is the "
                "breaking point.",
                "It does not go back to its natural length — it stays "
                "permanently longer than it started.",
            ],
            "answer": 3,
            "feedback": {
                0: "True only while it is within the limit. Past it, some of "
                   "the stretching is permanent.",
                1: "It is not a matter of time. Wait as long as you like and "
                   "it is still longer than it was.",
                2: "The limit is where the arithmetic stops being neat, not "
                   "where the metal fails. Breaking happens much later, if "
                   "at all.",
            },
            "title": "Rung 2 · The one that catches people"},
        "explain": {
            "q": "A newton meter has a scale of equally spaced marks "
                 "alongside its spring. Explain why the marks can be equally "
                 "spaced, and why the instrument becomes useless if it is "
                 "badly overloaded.",
            "field_label": "Your explanation",
            "placeholder": "The extension is proportional to…",
            "success": [
                "Says the extension is proportional to the force while the "
                "spring obeys Hooke’s law.",
                "Says equal increases in force therefore give equal "
                "increases in extension.",
                "Says that is what allows the marks to be equally spaced all "
                "the way along.",
                "Says overloading takes the spring past its limit of "
                "proportionality.",
                "Says the spring is then permanently stretched, so every "
                "later reading is wrong even at zero load.",
            ],
            "title": "Rung 3 · Explain"},
        "produce": {
            "q": "A set of kitchen scales weighs up to 5 kg and its dial is "
                 "marked in equal steps of 100 g the whole way round. "
                 "Someone stands on it with one foot. Explain what must be "
                 "true of the spring inside for the dial to work, and what "
                 "the owner should check afterwards.",
            "field_label": "Your answer",
            "placeholder": "For equal steps on the dial…",
            "success": [
                "Says the spring inside must be squashed or stretched in "
                "proportion to the force on it.",
                "Says that proportionality must hold across the whole range "
                "the dial covers, up to 5 kg.",
                "Says the weight of a person is far more than 5 kg allows "
                "— around 700 N rather than 50 N.",
                "Says the spring has probably been taken past its limit of "
                "proportionality.",
                "Says to check that the dial still reads zero with nothing "
                "on it, because a permanently deformed spring reads wrongly "
                "for ever.",
            ],
            "title": "Rung 4 · Take it somewhere new"},
    },

    "key_note": "Forces deform objects as well as move them: they stretch "
                "and squash. For a spring, extension — the increase in "
                "length, not the length — is proportional to the load while "
                "the spring obeys Hooke's law, so the graph is a straight "
                "line through the origin and equal loads add equal "
                "extensions. That is what makes a spring a usable measuring "
                "instrument. Beyond the limit of proportionality the line "
                "bends and the spring stops returning to its original "
                "length.",

    "stretch": [
        {"id": "hooke-in-an-anagram",
         "type": "explainer",
         "text": "Robert Hooke published this relationship in 1678, and he "
                 "published it first as a scrambled anagram — a way of "
                 "claiming a discovery without giving it away while he "
                 "checked it. Unscrambled it says, in Latin, <em>as the "
                 "extension, so the force</em>: nine words, no equation, no "
                 "graph, because neither had been invented as a way of "
                 "presenting results. Reading it now, the striking thing is "
                 "how narrow the claim is. Hooke did not say all materials "
                 "do this; he said that within a certain range, springs and "
                 "wires do. <strong>Every honest law in physics comes with a "
                 "range attached, and the interesting science usually starts "
                 "at the edge of it.</strong>"},
        {"id": "a-stretched-spring-stores-energy",
         "type": "explainer",
         "text": "Stretching a spring also stores energy. That is why a "
                 "wound clock runs, a mousetrap goes off, a bow fires an "
                 "arrow and a trampoline throws you back up — the work you "
                 "do pulling it out of shape comes back when it returns. At "
                 "GCSE you will find that the energy stored is the area "
                 "under that straight line, which is a neat piece of "
                 "reasoning: the further you stretch it, the harder each "
                 "extra millimetre becomes, so the energy grows faster than "
                 "the extension does. Squashing works the same way, which is "
                 "what the springs in a car's suspension, the foam in a "
                 "running shoe and the crumple zone of a car all rely on "
                 "— though a crumple zone is designed to deform "
                 "permanently and never come back, absorbing the energy "
                 "instead of returning it."},
    ],

    "support": [],

    "vocabulary": [
        {"term": "extension",
         "definition": "How much LONGER the spring has become: stretched "
                       "length − natural length. Not the total length."},
        {"term": "Hooke's law",
         "definition": "While a spring obeys it, extension is proportional "
                       "to load, so the graph is a straight line through the "
                       "origin."},
        {"term": "limit of proportionality",
         "definition": "The load beyond which the graph stops being "
                       "straight. Not a breaking point."},
        {"term": "proportional",
         "definition": "Two quantities that keep the same ratio: double one "
                       "and the other doubles, and a graph of the two is a "
                       "straight line through the origin."},
    ],

    "tutor": {
        "anchor": "s-bench",
        "prompt": "Ask Mr Badmus AI",
        "body": "Got a set of readings that will not make a straight line?",
        "cta": "Ask about this lesson"},

    "ks4_becomes": "Hooke's law with a spring constant, elastic and "
                   "inelastic deformation, and the energy stored in a "
                   "stretched spring as the area under a force–extension "
                   "graph.",

    # ⚖️ DESIGN'S FLAG 6 · THE UNIT'S ONLY RISK ASSESSMENT, KEPT WHOLE.
    # Five lines, in her order, in the engine's safety slot. See the module
    # docstring and `DEPARTURES-P4.md`.
    # ⊕ PHASE 3 CORRECTION, 25 Aug 2026. Her five items were run together
    # into one sentence and her opening line — "this is the one
    # investigation in the unit that needs a risk assessment" — was
    # dropped. The slot takes one string, so the bulleting cannot survive;
    # the SENTENCES can, and they are hers. `DEPARTURES-P4.md` row 1 used
    # to claim no content changed. It did, and the row now says so.
    "safety_note": "Before this one is done for real: this is the one "
                   "investigation in the unit that needs a risk assessment, "
                   "because finding the limit of proportionality means "
                   "loading a spring until it stops behaving. Eye protection "
                   "for everyone at the bench — an overloaded spring can let "
                   "go, and it leaves at speed. A tray of sand or a padded "
                   "box directly under the load, so a falling mass lands on "
                   "something soft. Nobody's hands, feet or knees under the "
                   "hanger at any point. The stand clamped or its base "
                   "weighted, so the whole set-up cannot topple towards "
                   "anyone. Loading to destruction is a demonstration, done "
                   "once, behind a safety screen — not a class activity.",

    "convention_note": "The spring bench is a teaching model. This spring is "
                       "given 20 mm of extension for each newton, a limit of "
                       "proportionality at 6 N, and permanent deformation "
                       "above 9 N; all three are chosen so that the bend in "
                       "the graph is reachable, not measured from a real "
                       "spring. Real readings scatter by a millimetre or "
                       "two, and a real spring's limit is not a sharp line. "
                       "Loads are treated as exact newtons.",

    "ws": ["measurement", "analysis-and-evaluation"],
}
