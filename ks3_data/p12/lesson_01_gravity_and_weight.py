"""P12 L1 — Gravity and weight (QUANTITATIVE, CFIFA).

Authored against Claude Design's approved page,
`docs/ks3/design-reference/p12/p12-01-gravity-and-weight.dc.html`.

Her page wins outright. The Everest hook, the five places to stand, the
W = m × g triangle, both worked examples, both attempts and all four rungs
are hers.

── ⚖️ THE BENCH IS A ZERO STATE WITH FOUR OTHERS AROUND IT ───────────

Five locations × five masses is twenty-five reachable states, and the one
that carries the lesson is `deep space`, where `g = 0`:

  * the weight readout goes to `0 N`;
  * the ratio-to-Earth readout refuses a figure and says so in words —
    there is no number, because dividing by nothing is not a small
    number;
  * the mass readout does not move;
  * Question 1 of the CFIFA block BLOCKS, because every line of it would
    be a multiplication by nothing. Design draws that state herself,
    with her own sentence for it and her own progress string.

"Weightless does not mean massless" is the sentence the bench exists to
earn, and it is only earnable because a student can drive it to a place
where one number goes to nothing and the other one does not.

── ⚖️ `g = 10 N/kg` IS STATUTORY, AND THE LEGAL LINE SAYS WHAT IT IS ─

`KS3.P.SPACE.01` names it. Earth's true mean value is 9.81 N/kg and it
varies by about 0.5% between the poles and the equator; 10 is the figure
used throughout KS3 and the legal line records both facts. Jupiter's
figure is quoted at the cloud tops, because Jupiter has no surface.

── ⚠️ MRB-278 · POSITION IS AUTHORED ─────────────────────────────────

Design's two marked rungs both put the correct answer at index 0, as do
all twelve across P12. **Her option TEXT and every correction are
verbatim; only the ORDER moves.** This lesson takes indices **1 and 3**.
Engine policy, not a register row.

── ⚠️ MRB-177 · ONE LENGTH TELL, REMEDIED AT THE DISTRACTOR ──────────

Rung 2's correct option is 30 words against a longest distractor of 15 —
a tell at both thresholds, and a tell on the rung that carries the whole
free-fall idea. All three distractors are FINISHED so that each states a
complete wrong rule rather than a short wrong reason; the correct answer
is untouched and so is every correction. Registered in
`DEPARTURES-P12.md`.

── ⚠️ NO SAFEGUARDING BLOCK. NO DRAFT MARKINGS. ──────────────────────
"""

LESSON = {
    "slug": "gravity-and-weight",
    "title": "Gravity and weight",
    "discipline": "physics",
    "unit": "Space",
    "family": "QUANTITATIVE",

    "covers": ["KS3.P.SPACE.01a"],
    "touches": ["KS3.WS.ANA.01"],
    "beyond_statutory": False,
    "threads": [{"id": "forces", "level": 3}],
    "typical_year": 9,
    "typical_minutes": 60,

    "requires": [],
    "assumes": [],
    "references": [{"unit": "P4", "lesson": "non-contact-forces"},
                   {"unit": "P4", "lesson": "balanced-and-unbalanced"}],
    "ks4_links": [],

    "meta_description": "Weight is a force in newtons and mass is an amount "
                        "of matter in kilograms — and a bathroom scale "
                        "quietly converts one into the other.",

    "big_question": "Bathroom scales are marked in kilograms and measure "
                    "newtons. That single piece of everyday dishonesty is "
                    "behind almost every mistake made in this topic.",

    "rail": [
        {"anchor": "s-hook",    "short": "HOOK",
         "label": "The falling lift",        "done_when": "committed"},
        {"anchor": "s-bench",   "short": "BENCH",
         "label": "Five places to stand",    "done_when": "gate_and_a_control"},
        {"anchor": "s-formula", "short": "CFIFA",
         "label": "Triangle and five steps", "done_when": "attempt_checked"},
        {"anchor": "s-ladder",  "short": "LADDER",
         "label": "Mastery ladder",          "done_when": "ladder_complete"},
    ],

    "phenomenon": {
        "kind": "narrative",
        "title": "You climb Everest. What has changed about you?",
        "prompt": "You weigh yourself at sea level, then again on the summit "
                  "of Everest, 8849 m higher up, using the same scales and "
                  "wearing the same clothes.",
        "commit": "What has changed — your mass, your weight, both or "
                  "neither?",
        "options": [
            "Your mass gets smaller, because you are further from the Earth",
            "Your weight gets smaller, because gravity is weaker up there",
            "Both get smaller, because everything weighs less high up",
            "Neither changes, because 8849 m is nothing to the Earth",
        ],
        "answer": 1,
        "reveal": "Your weight changes and your mass does not. Mass is how "
                  "much matter there is in you, and carrying it up a mountain "
                  "does not remove any. Weight is the force gravity pulls on "
                  "that matter with, and gravity is very slightly weaker at "
                  "the top of Everest — about 0.3% weaker, so a 70 kg climber "
                  "weighs roughly 2 N less. Take the same climber to the Moon "
                  "and the mass is still 70 kg while the weight falls from "
                  "about 700 N to about 112 N.",
    },

    "misconceptions": [
        # ⚠️ FORCE-45 IS NOT RE-MINTED. "There is no gravity in space" is
        # already `FORCE-45`, opened by `p4-09 non-contact-forces`; this page
        # re-confronts it, so it takes a second row in the register with the
        # IDENTICAL statement (the `CELL-08` precedent) and no new number.
        {"id": "FORCE-45",
         "statement": "There is no gravity in space.",
         "elicited_by": "s-ladder",
         "confronted_by": "think-no-gravity-in-space"},
        {"id": "SPACE-01",
         "statement": "Weight is measured in kilograms.",
         "elicited_by": "s-ladder",
         "confronted_by": "think-no-gravity-in-space"},
        {"id": "SPACE-02",
         "statement": "Where gravity is weaker you have less mass, because "
                      "you are lighter there.",
         "elicited_by": "s-hook",
         "confronted_by": "bench"},
        {"id": "SPACE-03",
         "statement": "A kilogram is a kilogram everywhere, so nothing about "
                      "it changes on the Moon.",
         "elicited_by": "bench",
         "confronted_by": "bench"},
    ],

    "core": [
        {"type": "hook", "id": "hook-commit", "anchor": "s-hook"},

        {"type": "explainer",
         "text": "<strong>Mass</strong> is how much matter something is made "
                 "of. It is measured in kilograms, it is the same everywhere "
                 "in the universe, and nothing but adding or removing "
                 "material will change it."},
        {"type": "explainer",
         "text": "<strong>Weight</strong> is a force: the pull of gravity on "
                 "that matter. It is measured in newtons, it has a direction "
                 "— towards the centre of whatever is pulling — and it "
                 "changes completely depending on where you are. <strong>W = "
                 "m × g</strong>, where g is the gravitational field strength "
                 "of the place you are standing, in newtons for each "
                 "kilogram."},
        {"type": "explainer",
         "text": "On Earth g is about 10 N/kg, so every kilogram is pulled "
                 "with about 10 N. On the Moon it is 1.6, on Mars 3.7, on "
                 "Jupiter 24.8. The same 70 kg astronaut weighs about 700 N "
                 "on Earth, 112 N on the Moon and 1740 N on Jupiter, and is "
                 "made of exactly the same amount of matter throughout."},

        # ── #s-bench · one set of bathroom scales, five places to stand ──
        {"type": "space-bench",
         "id": "bench",
         "anchor": "s-bench",
         "eyebrow": "At the bench · one set of bathroom scales, five places "
                    "to stand",
         "heading": "Same person. Same mass. Five different weights.",
         # ⚠️ A MAP OF NAMED STATES, NOT A STRING — the shell owns this row.
         "progress": {"idle": "Change a control to begin",
                      "live": "Controls live"},
         "lead": "Choose where to stand and how much mass to put on the "
                 "scales. The bars are the gravitational field strength at "
                 "each place — and they are the only thing that changes.",
         "model": "field-strength",
         # `g = 10 N/kg` on Earth. Statutory, and the divisor behind every
         # comparison the bench makes.
         "earth_g": 10,
         "gate": {
             "prompt": "Commit first. You take a 1 kg bag of sugar to the "
                       "Moon. What happens to it?",
             "options": [
                 "Its mass and its weight both fall to a sixth",
                 "Its mass stays 1 kg and its weight falls to about a sixth",
                 "Its weight stays the same and its mass falls",
                 "Nothing changes — a kilogram is a kilogram everywhere",
             ],
             "answer": 1,
         },
         "tabs_label": "Where you are standing",
         "start_tab": 0,
         "tabs": [
             {"id": "earth",  "label": "Earth",      "name": "Earth",
              "g": 10.0},
             {"id": "moon",   "label": "The Moon",   "name": "the Moon",
              "g": 1.6},
             {"id": "mars",   "label": "Mars",       "name": "Mars",
              "g": 3.7},
             {"id": "jupiter", "label": "Jupiter",   "name": "Jupiter",
              "g": 24.8},
             {"id": "deep",   "label": "Deep space", "name": "deep space",
              "g": 0.0},
         ],
         "slider": {
             "id": "mass",
             "label": "Mass on the scales",
             "value_label": "{label} kg",
             "start": 2,
             "values": [
                 {"id": "m1",   "label": "1",   "v": 1},
                 {"id": "m10",  "label": "10",  "v": 10},
                 {"id": "m50",  "label": "50",  "v": 50},
                 {"id": "m70",  "label": "70",  "v": 70},
                 {"id": "m100", "label": "100", "v": 100},
             ],
         },
         "bars_caption": "Gravitational field strength, in newtons for each "
                         "kilogram",
         # ⚠️ `{list}` IS COMPOSED FROM THE BARS THEMSELVES, so the label
         # names every bar that is drawn. Design's own label lists four of
         # the five — deep space is the one it leaves out, and it is the
         # state the whole second half of the lesson turns on.
         "bars_alt": "Bars of gravitational field strength in newtons for "
                     "each kilogram: {list}. {name} is highlighted.",
         "bars": [
             {"id": "earth",   "label": "Earth"},
             {"id": "moon",    "label": "The Moon"},
             {"id": "mars",    "label": "Mars"},
             {"id": "jupiter", "label": "Jupiter"},
             {"id": "deep",    "label": "Deep space"},
         ],
         "readouts": [
             {"id": "mass",    "label": "Mass on the scales"},
             {"id": "g",       "label": "Field strength here"},
             {"id": "weight",  "label": "So the weight is"},
             {"id": "vsearth", "label": "Compared with Earth"},
         ],
         "words": {
             "mass_sub":   "the same everywhere",
             "g_sub":      "newtons of pull for each kilogram",
             "weight_sub": "{v} × {g}",
             "ratio_sub":  "weight only, never mass",
             "zero_ratio": "nothing at all",
             "bar_sub":    "{w} N for {v} kg",
             "list_join":  "and",
         },
         "notes": {
             "field": "On {name} the gravitational field pulls with {g} N on "
                      "every kilogram, so {v} kg weighs {w} N. Move the mass "
                      "slider and the weight moves with it, because weight is "
                      "mass × field strength. Change where you are standing "
                      "and the weight changes without the mass moving at all "
                      "— the matter is untouched, and only the strength of "
                      "the pull on it has altered.",
             "zero": "Far from any star or planet the field strength is "
                     "effectively zero, so {v} kg of matter weighs nothing at "
                     "all. It still has {v} kg of mass: push it and it "
                     "resists exactly as hard as it would on Earth, and it "
                     "will hurt exactly as much if it drifts into you. "
                     "Weightless does not mean massless, and that is the "
                     "distinction the whole lesson turns on.",
         }},

        # ── #s-formula · W = m × g ────────────────────────────────────
        {"type": "formula",
         "id": "weight-rule",
         "eyebrow": "Writing it down · the shape of this relationship",
         "statement": "Weight = mass × gravitational field strength",
         "triangle": {
             "eyebrow": "The triangle",
             "heading": "Cover the one you want",
             "aria_label": "A formula triangle. The weight W sits above a "
                           "dividing line; the mass m and the field strength "
                           "g sit below it, multiplied together. Covering one "
                           "letter leaves the way to work it out.",
             "order": ["top", "left", "right"],
             "covered": "top",
             "top":   {"label": "W", "button": "Cover W",
                       "result": "W = m × g", "text": ""},
             "left":  {"label": "m", "button": "Cover m",
                       "result": "m = W ÷ g", "text": ""},
             "right": {"label": "g", "button": "Cover g",
                       "result": "g = W ÷ m", "text": ""},
             "close": {
                 "rule": "Two things side by side means multiply. One thing "
                         "over another means divide.",
                 "units": ["W · weight, the force gravity pulls with · N",
                           "m · mass of the object · kg",
                           "g · gravitational field strength where you are · "
                           "N/kg"],
                 "condition": "The field strength is the one for the place "
                              "you are standing, never automatically the "
                              "Earth's.",
             },
         }},

        {"type": "worked-example", "id": "cfifa-weight-plain-p12"},
        {"type": "worked-example", "id": "cfifa-weight-convert-p12"},
        {"type": "check", "id": "your-turn-weight", "anchor": "s-formula"},

        {"type": "key-fact", "ref": "weight-is-a-force"},

        {"type": "misconception", "id": "think-no-gravity-in-space",
         "anchor": "s-think"},

        {"type": "quiz", "anchor": "s-ladder"},
        {"type": "summary", "id": "s-keynote"},
    ],

    "activities": [
        {"id": "cfifa-weight-plain-p12",
         "kind": "worked-example",
         "demand": "calculate",
         "eyebrow": "Worked example · one step at a time",
         "heading": "What is the weight of a 6 kg toolbox on Earth?",
         "head_counter": {"format": "Step {n} of 5", "total": 5},
         "buttons": {"first": "Show the first step",
                     "next": "Show the next step",
                     "done": "All five shown",
                     "done_note": "Nothing needed converting there. Now the "
                                  "one that does."},
         "staged": True,
         "fifa": [
             {"letter": "C", "label": "Convert",
              "line": "6 kg stays 6 kg · 10 N/kg stays 10 N/kg",
              "note": "The mass is already in kilograms, which is what N/kg "
                      "needs, so there is nothing to convert."},
             {"letter": "F", "label": "Formula",
              "line": "W = m × g",
              "note": "Cover W on the triangle: m sits beside g, so you "
                      "multiply."},
             {"letter": "I", "label": "Insert",
              "line": "W = 6 kg × 10 N/kg",
              "note": "The field strength on Earth is 10 newtons for each "
                      "kilogram."},
             {"letter": "F", "label": "Fine-tune",
              "line": "6 × 10 = 60",
              "note": "Kilograms times newtons per kilogram leaves newtons."},
             {"letter": "A", "label": "Answer",
              "line": "W = 60 N",
              "note": "Sixty newtons, downwards — weight is a force and "
                      "always has a direction."},
         ]},

        {"id": "cfifa-weight-convert-p12",
         "kind": "worked-example",
         "demand": "calculate",
         "eyebrow": "Worked example · one step at a time",
         "heading": "What is the weight of a 450 g bag of flour on Earth?",
         "head_counter": {"format": "Step {n} of 5", "total": 5},
         "buttons": {"first": "Show the first step",
                     "next": "Show the next step",
                     "done": "All five shown",
                     "done_note": "Convert first, then the same four lines. "
                                  "Your turn below."},
         "staged": True,
         "fifa": [
             {"letter": "C", "label": "Convert",
              "line": "450 g ÷ 1000 = 0.450 kg",
              "note": "× 10 N/kg wants kilograms, and a gram is a thousandth "
                      "of one, so divide by 1000."},
             {"letter": "F", "label": "Formula",
              "line": "W = m × g",
              "note": "Cover W on the triangle: m sits beside g, so you "
                      "multiply."},
             {"letter": "I", "label": "Insert",
              "line": "W = 0.450 kg × 10 N/kg",
              "note": "The converted mass goes in. The 450 never does."},
             {"letter": "F", "label": "Fine-tune",
              "line": "0.450 × 10 = 4.5",
              "note": "Kilograms times newtons per kilogram leaves newtons."},
             {"letter": "A", "label": "Answer",
              "line": "W = 4.5 N",
              "note": "Insert 450 instead of 0.450 and the bag comes out "
                      "weighing 4500 N — about half a tonne."},
         ]},

        {"id": "your-turn-weight",
         "kind": "p12-attempt",
         "demand": "calculate",
         "eyebrow": "Your turn · the same five steps",
         "check_label": "Check your working",
         "reveal_label": "The five lines · tick what you had",
         # The bench's opening state: Earth, and the mass slider resting at
         # its third position, 50 kg.
         "rest": {"v": "50", "name": "Earth", "g": "10.0", "w": "500"},
         # Design's own readout beside the Check button when the question is
         # blocked. The kit draws the blocked PARAGRAPH from `blocked_lead`;
         # this is the little progress string, and it travels as a span of
         # this unit's own rather than as an edit to `ks3_art/kit.py`.
         "blocked_hint": "No field to multiply by",
         "questions": [
             {"id": "q1", "tab": "Question 1",
              "head": "Your scales: {v} kg standing on {name}, where g is "
                      "{g} N/kg.",
              "lead": "Write each line out yourself — starting by deciding "
                      "whether anything needs converting. Then check your "
                      "working and tick the lines you had.",
              # ⚖️ HER OWN BLOCKED STATE. In deep space every weight comes
              # out as nothing, so the five lines have nothing to say and
              # she replaces them with one sentence rather than showing a
              # student five multiplications by zero.
              "blocked_lead": "In deep space the field strength is zero, so "
                              "every weight comes out as nothing. Stand "
                              "somewhere with a field and the five lines come "
                              "back.",
              "steps": [
                  {"letter": "C", "label": "Convert",
                   "placeholder": "anything to convert?",
                   "line": "{v} kg stays {v} kg · {g} N/kg stays {g} N/kg",
                   "note": "The mass is already in kilograms and the field "
                           "strength already in newtons per kilogram, so "
                           "there is nothing to convert."},
                  {"letter": "F", "label": "Formula",
                   "line": "W = m × g",
                   "note": "Cover W on the triangle: m sits beside g, so you "
                           "multiply."},
                  {"letter": "I", "label": "Insert",
                   "line": "W = {v} kg × {g} N/kg",
                   # ⚠️ HER TEMPLATE IS `'…the one for ' + T.name + ', not
                   # for Earth.'`, WHICH READS "the one for Earth, not for
                   # Earth" ON THE OPENING TAB — the first sentence of the
                   # attempt panel, in the state every student lands on. One
                   # clause, true in all five places. Q2's own notes still
                   # carry the explicit "not the Earth one" warning, and the
                   # bench's fourth readout tile makes the Earth comparison
                   # live a few centimetres above.
                   "note": "The field strength is the one for {name} — the "
                           "place you are standing, never a default."},
                  {"letter": "F", "label": "Fine-tune",
                   "line": "{v} × {g} = {w}",
                   "note": "Kilograms times newtons per kilogram leaves "
                           "newtons."},
                  {"letter": "A", "label": "Answer",
                   "line": "W = {w} N",
                   "note": "Downwards, towards the centre of {name}."},
              ],
              # ⚠️ HER CLOSING LINE IS `'The five lines give ' + W + ' N on '
              # + T.name + '. The same ' + V + ' kg on Earth would weigh ' +
              # earthW + ' N.'`, which on the opening tab says the same thing
              # twice: "give 500 N on Earth. The same 50 kg on Earth would
              # weigh 500 N." Rewritten to the point the unit is making, and
              # true in every state.
              "close": "The five lines give {w} N on {name}, for a mass of "
                       "{v} kg that is the same everywhere."},
             {"id": "q2", "tab": "Question 2",
              "head": "A rover of mass 185 kg is landed on Mars, where g is "
                      "3.7 N/kg. What does it weigh there?",
              "lead": "Write each line out yourself — starting by deciding "
                      "whether anything needs converting. Then check your "
                      "working and tick the lines you had.",
              "steps": [
                  {"letter": "C", "label": "Convert",
                   "placeholder": "anything to convert?",
                   "line": "185 kg stays 185 kg · 3.7 N/kg stays 3.7 N/kg",
                   "note": "Both quantities are already in the units the "
                           "formula wants, so there is nothing to convert."},
                  {"letter": "F", "label": "Formula",
                   "line": "W = m × g",
                   "note": "Cover W on the triangle: m sits beside g, so you "
                           "multiply."},
                  {"letter": "I", "label": "Insert",
                   "line": "W = 185 kg × 3.7 N/kg",
                   "note": "Use the Martian field strength, not the Earth "
                           "one."},
                  {"letter": "F", "label": "Fine-tune",
                   "line": "185 × 3.7 = 684.5",
                   "note": "Kilograms times newtons per kilogram leaves "
                           "newtons."},
                  {"letter": "A", "label": "Answer",
                   "line": "W = 685 N",
                   "note": "Reach for 10 N/kg out of habit and the rover "
                           "comes out weighing 1850 N — the mistake is using "
                           "the wrong planet, not the wrong unit."},
              ],
              "close": "The five lines give 685 N on Mars. On Earth the same "
                       "rover would weigh 1850 N, which is why the landing "
                       "legs could be built lighter."},
         ]},

        # ⚠️ PLAIN `predict`. `#s-think` is NOT a rail stop on this page —
        # Design's third stop is `#s-formula` — so the section needs no
        # completion contract of its own.
        {"id": "think-no-gravity-in-space",
         "kind": "predict",
         "demand": "explain",
         "targets": "FORCE-45",
         "statements": [
             {"quote": "Astronauts float because there is no gravity in "
                       "space.",
              "targets": "FORCE-45",
              "body": [
                  "The International Space Station orbits about 400 km up, "
                  "where the Earth’s gravitational field is still around 90% "
                  "as strong as it is at the surface. If gravity were absent "
                  "the station would fly off in a straight line instead of "
                  "going round. What the astronauts have lost is not the pull "
                  "but the push — the floor is falling at exactly the same "
                  "rate they are, so nothing presses on them. That is free "
                  "fall, not the absence of gravity, and the correct name for "
                  "the sensation is weightlessness.",
              ]},
             {"quote": "Weight is measured in kilograms.",
              "targets": "SPACE-01",
              "body": [
                  "Weight is a force, and forces are measured in newtons. The "
                  "scales in your bathroom really do measure a force, then "
                  "quietly divide it by 10 N/kg and print a mass, because a "
                  "mass is what you wanted to know and the assumption is that "
                  "you are on Earth. It is a reasonable shortcut and a bad "
                  "habit: the moment the question moves off this planet, the "
                  "difference between the 70 kg and the 700 N is the whole "
                  "answer.",
              ]},
         ]},
    ],

    "figures": [],

    "key_facts": [
        {"id": "weight-is-a-force",
         "eyebrow": "Key fact",
         "ground": "card",
         "placement": "top-level",
         "text": "Weight = mass × gravitational field strength, W = m × g. "
                 "Mass is in kilograms and never changes; weight is a force "
                 "in newtons and changes with where you are. On Earth g is "
                 "about 10 N/kg, so a 1 kg bag of sugar weighs about 10 N."},
    ],

    # ⚠️ MRB-278 · POSITION IS AUTHORED. This lesson takes indices 1 and 3.
    # Design put both at 0; her option TEXT and every correction are verbatim
    # and only the ORDER moves.
    #
    # ⚠️ MRB-177 · RUNG 2'S THREE DISTRACTORS ARE FINISHED. Her correct
    # option is 30 words against a longest distractor of 16, which is a tell
    # at both thresholds. Each distractor now states a COMPLETE WRONG RULE
    # rather than a short wrong reason — the construct MRB-177 was ruled on —
    # and the correct answer and every correction are untouched.
    "ladder": {
        "recall": {
            "q": "A crate has a mass of 24 kg. What is its weight on Earth, "
                 "where g = 10 N/kg?",
            "options": [
                "2.4 N — divide the mass by the field strength",
                "240 N",
                "240 kg — the crate is what you weighed",
                "24 N — weight and mass are the same number on Earth",
            ],
            "answer": 1,
            "feedback": {
                0: "Cover W on the triangle and m sits beside g, so you "
                   "multiply. Dividing gives you a mass back, not a force.",
                2: "The number is right and the unit is wrong. Kilograms "
                   "times newtons per kilogram leaves newtons, and weight is "
                   "always a force.",
                3: "They are not. On Earth every kilogram is pulled with "
                   "about 10 N, so the weight in newtons is about ten times "
                   "the mass in kilograms.",
            },
            "title": "Rung 1 · Calculate"},
        "apply": {
            "q": "An astronaut floats inside the International Space "
                 "Station. What is true of them?",
            "options": [
                "There is no gravity that far out, so they have no weight "
                "and no mass — far enough from the Earth, matter stops being "
                "pulled and stops resisting a push.",
                "Their mass has become zero, which is why they float — an "
                "object in orbit is matter with the amount of matter taken "
                "out of it.",
                "They are beyond the Earth’s field, so weight and mass no "
                "longer apply — the two quantities only mean anything while "
                "you are standing on a planet.",
                "Their mass is unchanged and gravity is still pulling on them "
                "— they are falling around the Earth together with the "
                "station, which is why nothing presses on the floor.",
            ],
            "answer": 3,
            "feedback": {
                0: "Gravity at that height is about 90% of its value at the "
                   "surface. What is missing is not the pull but anything "
                   "pushing back.",
                1: "Mass never changes. Push an astronaut in orbit and they "
                   "resist exactly as much as they would on the ground.",
                2: "The station is only about 400 km up — well inside the "
                   "field. It is in orbit precisely because gravity is still "
                   "pulling it.",
            },
            "title": "Rung 2 · The one that catches people"},
        "explain": {
            "q": "A set of bathroom scales is marked in kilograms. Explain "
                 "what it is actually measuring, and why the reading would be "
                 "wrong if you took it to the Moon.",
            "field_label": "Your explanation",
            "placeholder": "The scales measure the force pressing down, so…",
            "success": [
                "Says the scales measure a force — how hard you press down on "
                "them.",
                "Says that force is your weight, in newtons.",
                "Says the scale divides by 10 N/kg to display a mass in "
                "kilograms.",
                "Says the division assumes Earth’s field strength, which is "
                "built into the dial.",
                "Says on the Moon the same person presses with about a sixth "
                "of the force, so the scales would show about a sixth of the "
                "mass — and be wrong, because the mass has not changed.",
            ],
            "title": "Rung 3 · Explain"},
        "produce": {
            "q": "Jupiter’s field strength is about 24.8 N/kg. Explain what "
                 "would be hard about walking there, and what would be "
                 "exactly as hard as on Earth.",
            "field_label": "Your answer",
            "placeholder": "Everything would weigh about two and a half times "
                           "more, so…",
            "success": [
                "Says every object would weigh about 2.5 times what it does "
                "on Earth.",
                "Works out a specific weight — for example a 70 kg person at "
                "about 1740 N against 700 N.",
                "Says legs and skeletons would have to support far more "
                "force, so standing and walking would be exhausting.",
                "Says the mass of everything is unchanged.",
                "Says that starting, stopping and changing direction sideways "
                "would take exactly the same force as on Earth, because that "
                "depends on mass rather than weight.",
            ],
            "title": "Rung 4 · Take it somewhere new"},
    },

    "key_note": "Mass is the amount of matter in an object, measured in "
                "kilograms and unchanged by location. Weight is the force of "
                "gravity acting on that mass, measured in newtons and given "
                "by W = m × g. Gravitational field strength g is the pull in "
                "newtons on each kilogram: about 10 N/kg on Earth, 1.6 on the "
                "Moon, 3.7 on Mars and 24.8 on Jupiter. Bathroom scales "
                "measure a force and display a mass by assuming Earth’s field "
                "strength.",

    "stretch": [
        {"id": "mass-and-distance-together",
         "type": "explainer",
         "text": "Field strength depends on the mass of the body you are "
                 "standing on and on how far you are from its centre. Jupiter "
                 "is over three hundred times the mass of the Earth and pulls "
                 "only about two and a half times as hard at its cloud tops, "
                 "because those cloud tops are eleven times further from the "
                 "middle than the Earth’s surface is from ours. Distance is "
                 "doing as much work in that comparison as mass."},
        {"id": "why-the-kilogram-had-a-lump",
         "type": "explainer",
         "text": "Because g varies slightly across the Earth — with altitude, "
                 "latitude and the density of the rock underneath — a "
                 "laboratory balance that compares an unknown mass against a "
                 "known one gives the same answer anywhere, while a spring "
                 "scale does not. That is why the kilogram was defined by a "
                 "physical object for 130 years, and why gravimeters "
                 "sensitive enough to detect a few parts per billion are used "
                 "to hunt for oil and for buried voids."},
    ],

    "support": [],

    "vocabulary": [
        {"term": "mass",
         "definition": "How much matter something is made of, measured in "
                       "kilograms. It is the same everywhere in the universe, "
                       "and only adding or removing material changes it."},
        {"term": "weight",
         "definition": "The force of gravity pulling on an object’s mass, "
                       "measured in newtons. It points towards the centre of "
                       "whatever is doing the pulling, and it changes with "
                       "where the object is."},
        {"term": "gravitational field strength",
         "definition": "The pull in newtons on each kilogram at a particular "
                       "place, written g and measured in N/kg. On Earth it is "
                       "about 10 N/kg."},
        {"term": "weightlessness",
         "definition": "The sensation of nothing pressing on you, felt in "
                       "free fall. It is not the absence of gravity: an "
                       "astronaut in orbit is being pulled almost as hard as "
                       "they would be on the ground."},
    ],

    "tutor": {
        "anchor": "s-formula",
        "prompt": "Ask Mr Badmus AI",
        "body": "Got a mass in one unit and want the weight in newtons?",
        "cta": "Ask about this lesson"},

    "ks4_becomes": "Gravitational field strength in N/kg, weight measured "
                   "with a calibrated spring balance, and gravitational "
                   "potential energy as mass × g × height.",

    "convention_note": "The bench is a teaching model. Gravitational field "
                       "strengths are surface values rounded to one decimal "
                       "place: Earth 10.0, the Moon 1.6, Mars 3.7 and Jupiter "
                       "24.8 N/kg. Earth’s true mean value is 9.81 N/kg and "
                       "varies by about 0.5% between the poles and the "
                       "equator; 10 is the figure used throughout KS3. "
                       "Jupiter has no solid surface, so its figure is quoted "
                       "at the top of the cloud layer. Deep space is treated "
                       "as zero field, which is an idealisation — no point in "
                       "the universe is entirely free of gravity.",

    "ws": ["measurement"],
}
