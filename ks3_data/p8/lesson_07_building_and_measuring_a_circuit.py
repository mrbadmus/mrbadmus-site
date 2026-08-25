"""P8 L7 — Building and measuring a circuit (INVESTIGATION).

Authored against Claude Design's approved page,
`docs/ks3/design-reference/p8/p8-07-building-and-measuring-a-circuit.dc.html`.

Her page wins outright. The two pairs with the same diagram, the bench you
wire wrong on purpose, the six-row fault table and all four rungs are
hers.

── ⚖️ HER FLAG 2 · THIS LESSON OWNS NO SUBJECT-CONTENT CLAUSE ────────

Her sentence: *"It is the unit's INVESTIGATION slot and it teaches Working
Scientifically … Every quantity it uses is owned by `p8-01`, `p8-04` or
`p8-05`. The single-source rule requires each STATEMENT to have exactly
one owner, not each LESSON to own a statement, so this is legal — but a
gate that checks the reverse will fail it."*

The gate does check the reverse: §10.2 requires non-empty `covers`. So the
lesson claims `KS3.WS.EXP.03` — *select, plan and carry out the most
appropriate types of scientific enquiries to test predictions, including
identifying independent, dependent and control variables* — which is
exactly what rung 4 asks for and exactly what the lesson teaches. §5.7
exempts Working Scientifically statements from the exactly-once rule, so
nothing else in the key stage is disturbed by the claim.

⚠️ **THE OTHER LEGAL SHAPE WOULD HAVE BEEN WRONG.** §7.6's exemption —
`beyond_statutory: True` with empty `covers` — is for OFF-SPEC content,
and Working Scientifically is on the spec. It would have passed the gate
and misfiled the lesson.

── ⚖️ MRB-204 · NO FORMULA BLOCK ────────────────────────────────────

A method lesson. The one division it mentions — 3.00 V ÷ 0.30 A for the
lamp's ten ohms — is `p8-05`'s relationship used as given data, and that
lesson is carried as an edge.

── ⚖️ RULED · THE LOOSE CONNECTION DOMINATES ────────────────────────

Three booleans give eight states and Design authors five sentences,
because a break in the loop makes both meter positions irrelevant. That
is `CIRC-25` met head-on: the commonest failure in the whole practical
looks exactly like a broken instrument.

⚠️ **THE SHORTED AMMETER READS `off the scale`, NEVER A FIGURE.** What a
real supply and a real meter do in that state depends on the equipment and
none of it is a measurement; her legal line says so and the renderer
refuses a numeric reading there.

── ⚠️ FOUR RAIL STOPS ───────────────────────────────────────────────

    s-hook · s-wire · s-fault · s-ladder

⚠️ `s-fault` takes `gate !== null` while the bench also wants a control
touched, so the bench marks it through `band_anchor` / `band_at`.

── ⚖️ NO SAFEGUARDING BLOCK, DELIBERATELY ───────────────────────────

Her own judgement, and it is ratified: this is a practical-safety lesson,
the whole practical runs on cells, and the only hazard modelled is a meter
being damaged. No student's body is at risk on the page. `p8-06` is where
the block belongs, because that lesson reaches mains cables and sockets at
home.

── ⚖️ FOUR MISCONCEPTIONS ───────────────────────────────────────────

    CIRC-25  if a meter reads zero the meter is broken     (hers, §7)
    CIRC-26  it cannot matter which way round the leads go (hers, §7)
    CIRC-27  the order of the components round a loop matters (from the hook)
    CIRC-28  a near-full voltmeter reading means it works  (from rung 2)

⚠️ **THIS PAGE ELICITS `CIRC-14` and does not re-declare it.** Design's §7
gives `CIRC-14` — *a voltmeter goes in the loop, like an ammeter* — an
`elicited_by` of `r1` of THIS page while the entry belongs to `p8-04`.
MRB-248 makes that pointer unresolvable from `p8-04`, so it is absent
there; and the register's standing rule is CITE, DO NOT RE-DECLARE, so it
is not minted a second time here. It is recorded as a reappearance in the
register instead.

── ⚠️ POSITION IS AUTHORED. This lesson takes indices 0 and 2.
"""

LESSON = {
    "slug":  "building-and-measuring-a-circuit",
    "title": "Building and measuring a circuit",
    "discipline": "physics",
    "unit": "Electric circuits",
    "family": "INVESTIGATION",

    # ⊕ HER FLAG 2, ANSWERED. See the module docstring: this is the unit's
    # Working Scientifically slot, §5.7 exempts WS from the exactly-once
    # rule, and §7.6's beyond-statutory shape would have misfiled it.
    "covers": ["KS3.WS.EXP.03"],
    "touches": ["KS3.WS.EXP.04", "KS3.WS.ANA.05"],
    "beyond_statutory": False,
    "threads": [{"id": "electricity", "level": 3}],
    "typical_year": 8,
    "typical_minutes": 60,

    "requires": ["conductors-and-insulators"],
    "assumes": [],
    "references": ["current-and-circuits", "potential-difference",
                   "resistance"],
    "ks4_links": [],

    "meta_description": "A meter in the wrong place does not give you a wrong "
                        "reading. It gives you a different circuit, and then "
                        "a perfectly correct reading of that.",

    "big_question": "A meter in the wrong place does not give you a wrong "
                    "reading. It gives you a different circuit, and then a "
                    "perfectly correct reading of that.",

    "rail": [
        {"anchor": "s-hook",   "short": "HOOK",
         "label": "Same diagram, two answers", "done_when": "committed"},
        {"anchor": "s-wire",   "short": "BENCH",
         "label": "Wire it wrong on purpose",
         "done_when": "gate_and_a_control"},
        {"anchor": "s-fault",  "short": "FAULTS",
         "label": "Six things that go wrong", "done_when": "gate_committed"},
        {"anchor": "s-ladder", "short": "LADDER",
         "label": "Mastery ladder",           "done_when": "ladder_complete"},
    ],

    "phenomenon": {
        "kind": "narrative",
        "title": "Same diagram. Same box of parts. Two answers.",
        "prompt": "Two pairs work from the identical circuit diagram with "
                  "identical apparatus. One pair gets a lit lamp and 0.30 A. "
                  "The other gets a dark lamp and an ammeter reading zero, "
                  "and swears they have followed the drawing.",
        "commit": "Before you look at anything clever, what is most likely "
                  "wrong?",
        "options": [
            "A connection somewhere in the loop is not gripping",
            "Their ammeter is faulty and needs replacing",
            "Their lamp is a different rating from the first pair’s",
            "They read the diagram in the wrong order, so the components are "
            "in the wrong sequence",
        ],
        "answer": 0,
        "reveal": "Almost always a connection. A loop only works if every "
                  "joint in it works, and a crocodile clip biting insulation "
                  "instead of copper looks perfectly convincing. The "
                  "sequence, incidentally, does not matter at all in a single "
                  "loop — one current, the same everywhere — so putting the "
                  "ammeter before or after the lamp changes nothing. What "
                  "does matter is whether each meter is in the loop or across "
                  "a component, which is the rest of this lesson.",
    },

    "misconceptions": [
        {"id": "CIRC-25",
         "statement": "The meter reads zero, so the meter must be broken.",
         "elicited_by": "s-hook",
         "confronted_by": "wire"},
        {"id": "CIRC-26",
         "statement": "It cannot matter which way round the leads go on a "
                      "meter.",
         "confronted_by": "s-think"},
        {"id": "CIRC-27",
         "statement": "The order the components come in round a single loop "
                      "changes what the meters read.",
         "elicited_by": "s-hook",
         "confronted_by": "s-hook"},
        {"id": "CIRC-28",
         "statement": "A voltmeter reading close to the battery's value means "
                      "the circuit is working.",
         "elicited_by": "s-ladder",
         "confronted_by": "wire"},
    ],

    "core": [
        {"type": "hook", "id": "hook-commit", "anchor": "s-hook"},

        {"type": "explainer",
         "text": "The two meters are opposites, and it is their own "
                 "resistance that decides where they go. An <strong>ammeter"
                 "</strong> is built to have almost no resistance, so that "
                 "putting it <em>in</em> the loop barely changes the current "
                 "it is there to measure. A <strong>voltmeter</strong> is "
                 "built to have an enormous resistance, so that hanging it "
                 "<em>across</em> a component draws almost nothing and barely "
                 "changes the p.d. it is there to measure."},
        {"type": "explainer",
         "text": "Swap them over and both of those virtues become disasters. "
                 "An ammeter across a lamp offers the charge a route with no "
                 "resistance at all, so the lamp is bypassed and goes out "
                 "while a dangerous current pours through the meter. A "
                 "voltmeter in the loop puts a million ohms in series with "
                 "everything, so almost nothing flows and the lamp is dark."},
        {"type": "explainer",
         "text": "Which is why building a circuit has an order to it. Follow "
                 "the diagram, put the loop together with the switch open, "
                 "check every connection by eye and by hand, close the "
                 "switch, then read. Take each reading twice, and if one "
                 "value refuses to sit with the others, go back and take it "
                 "again rather than writing it down."},

        # ── #s-wire · one lamp, two meters to place ────────────────────
        {"type": "meter-placement",
         "id": "wire",
         "anchor": "s-wire",
         "eyebrow": "At the bench · one lamp, two cells, two meters to place",
         "heading": "Wire it wrong on purpose.",
         # A MAP, NOT A STRING. `progress` authored as a string is
         # read as a COUNT FORMAT (MRB-248's widening), and these
         # are two named states rather than a tally.
         "progress": {"idle": "Change a control to begin",
                      "live": "Three controls live"},
         "lead": "A 3.0 V battery and a 10 Ω lamp. Choose where each meter "
                 "goes, and choose whether one connection is properly "
                 "tightened.",
         "start_a": 0,
         "start_v": 0,
         "start_j": 0,
         "band_anchor": "s-fault",
         "band_at": 1,
         "short_reading": "off the scale",
         "battery_label": "3.0 V",
         "lamp_label": "LAMP, 10 OHMS",
         "a_label": "The ammeter",
         "v_label": "The voltmeter",
         "j_label": "The connection at the far corner",
         "gate": {
             "prompt": "Commit first. Someone connects the ammeter across the "
                       "lamp instead of in the loop. What happens?",
             # ⚑ Option D is FINISHED into a complete wrong rule so that the
             # correct answer is no longer a length tell. It states the
             # even-splitting belief `CIRC-09` is about, met again here.
             # See DEPARTURES-P8.md row 1.
             "options": [
                 "It reads the current as usual, because a meter reads "
                 "whatever passes through it",
                 "It offers a route with no resistance, so the lamp is "
                 "bypassed and goes out while a huge current pours through "
                 "the meter",
                 "It reads zero, because no current can get into it from the "
                 "side",
                 "It reads half the current, because the charge arriving at "
                 "the junction splits evenly between the meter and the lamp, "
                 "whatever the two are made of",
             ],
             "answer": 1,
         },
         "ammeter": [
             {"v": 0, "label": "In the loop"},
             {"v": 1, "label": "Across the lamp"},
         ],
         "voltmeter": [
             {"v": 0, "label": "Across the lamp"},
             {"v": 1, "label": "In the loop"},
         ],
         "joint": [
             {"v": 0, "label": "Tight"},
             {"v": 1, "label": "Loose"},
         ],
         "readouts": [
             {"id": "a", "label": "The ammeter reads", "sub": "—"},
             {"id": "v", "label": "The voltmeter reads", "sub": "—"},
             {"id": "lamp", "label": "The lamp is", "word": True},
             {"id": "verdict", "label": "Verdict on this build", "word": True},
         ],
         "branches": {
             "loose":
                 "One connection at the far corner is not gripping, and that "
                 "is the end of it: the loop is not a loop, so both meters "
                 "read zero and the lamp is dark. This is the commonest "
                 "failure in the whole practical and it looks exactly like a "
                 "broken instrument. Check every clip and terminal by hand "
                 "before you suspect anything else — and note that it makes "
                 "no difference where the break is, or how the meters are "
                 "wired.",
             "shorted":
                 "The ammeter is across the lamp, and an ammeter has almost "
                 "no resistance — so it is now a piece of wire bridging the "
                 "lamp. All the charge takes that route, the lamp gets "
                 "nothing and goes out, and the current is limited only by "
                 "the battery. Open the switch: this is the one wiring "
                 "mistake in this practical that can damage a meter.",
             "strangled":
                 "The voltmeter is in the loop, and a voltmeter has an "
                 "enormous resistance — about a million ohms against the "
                 "lamp's ten. Almost nothing gets round, so the lamp is dark "
                 "and the ammeter reads zero, while the voltmeter reads "
                 "2.94 V because nearly the whole battery p.d. is now across "
                 "the voltmeter itself. That reading is correct and "
                 "completely misleading: it is measuring the fault.",
             "both":
                 "Both meters are in the wrong place, and the voltmeter wins: "
                 "its million ohms in the loop hold the current down to a few "
                 "millionths of an amp, so the ammeter bridging the lamp has "
                 "almost nothing to carry and reads zero. The lamp is dark "
                 "for two reasons at once. Fix them one at a time — changing "
                 "both and re-reading tells you nothing about which was the "
                 "problem.",
             "correct":
                 "This is the build the diagram asked for. The ammeter is in "
                 "the loop so the whole current passes through it: 0.30 A. "
                 "The voltmeter is across the lamp so it reads the p.d. the "
                 "lamp is getting: 3.00 V, the battery's whole value, because "
                 "the lamp is the only component in the loop. Divide the two "
                 "and you have the lamp's resistance, 10 Ω — which is the "
                 "reason for taking both readings at once.",
         }},

        # ── #s-fault · six things that go wrong ────────────────────────
        {"type": "circ-band",
         "id": "six-faults",
         "anchor": "s-fault",
         "eyebrow": "The figure",
         "heading": "Six things that go wrong, and what each looks like",
         "lead": "Work from the symptom, not from a hunch. Almost every "
                 "failure in this practical is one of these, and the first "
                 "two account for most of them.",
         "table": {
             "corner": "What you see",
             "min_width": 700,
             "columns": ["Most likely cause", "What to check first"],
             "rows": [
                 {"head": "Nothing at all — both meters on zero, lamp dark",
                  "cells": ["A break somewhere in the loop",
                            "Every crocodile clip and terminal, the switch, "
                            "and that the cells are the right way round in "
                            "the holder"]},
                 {"head": "Lamp dark, but the voltmeter reads nearly the "
                          "whole battery p.d.",
                  "cells": ["The voltmeter is in the loop instead of across "
                            "the lamp — or the filament is broken",
                            "That the voltmeter has one lead on each side of "
                            "the lamp and is not carrying the loop"]},
                 {"head": "Lamp goes out and the ammeter slams off the scale",
                  "cells": ["The ammeter is across the lamp, shorting it out",
                            "Open the switch at once, then check the ammeter "
                            "is in the line and not bridging anything"]},
                 {"head": "Lamp dim, both readings lower than expected",
                  "cells": ["A tired cell, one cell too few, or an extra "
                            "resistance in the loop",
                            "Put the voltmeter across the battery and compare "
                            "with what it should supply"]},
                 {"head": "Readings drift downwards while you watch",
                  "cells": ["The cells are running down, or the filament is "
                            "still heating",
                            "Read both meters at the same moment, quickly, "
                            "and open the switch between settings"]},
                 {"head": "One value refuses to sit with the rest",
                  "cells": ["A misread scale, or a clip that moved between "
                            "readings",
                            "Repeat that one setting before writing it down — "
                            "never smooth it over on the graph"]},
             ],
         },
         "close": "Notice that three of the six are not faults in the "
                  "apparatus at all. They are faults in the <em>method</em> — "
                  "reading at the wrong moment, reading the wrong scale, or "
                  "accepting a value you have not repeated."},

        {"type": "key-fact", "ref": "ammeter-in-voltmeter-across"},

        {"type": "misconception", "id": "think-meter-is-broken",
         "anchor": "s-think"},

        {"type": "quiz", "anchor": "s-ladder"},
        {"type": "summary", "id": "s-keynote"},
    ],

    "activities": [
        {"id": "think-meter-is-broken",
         "kind": "predict",
         "demand": "explain",
         "targets": "CIRC-25",
         "statements": [
             {"quote": "The meter reads zero, so the meter must be broken.",
              "targets": "CIRC-25",
              "body": [
                  "A zero is a reading, and usually a true one. It says there "
                  "is no current where the meter is sitting, which is exactly "
                  "what a break in the loop produces — and a break is far "
                  "more common than a faulty instrument. Swapping the meter "
                  "for another one is the last thing to try, not the first: "
                  "it costs a minute, tells you nothing if the fault is a "
                  "loose clip, and hides the fault from the next pair who use "
                  "the same box.",
              ]},
             {"quote": "It cannot matter which way round the leads go on a "
                       "meter.",
              "targets": "CIRC-26",
              "body": [
                  "On a digital meter it barely does — you get the right "
                  "number with a minus sign in front. On an analogue meter "
                  "with a needle it matters a great deal, because the needle "
                  "is driven backwards off the end of its travel and can be "
                  "bent. The terminals are marked, red to the side nearer the "
                  "positive end of the battery, and getting into that habit "
                  "costs nothing and saves a meter.",
              ]},
         ]},
    ],

    "figures": [],

    "key_facts": [
        {"id": "ammeter-in-voltmeter-across",
         "eyebrow": "Key fact",
         "ground": "card",
         "placement": "top-level",
         "text": "An ammeter has almost no resistance, so it goes in the "
                 "loop. A voltmeter has an enormous resistance, so it goes "
                 "across a component. Swap them and you have not taken a bad "
                 "reading — you have built a different circuit. Build with "
                 "the switch open, check the loop, then read, and repeat "
                 "every reading."},
    ],

    # ⚠️ MRB-278 · POSITION IS AUTHORED. This lesson takes indices 0 and 2.
    "ladder": {
        "recall": {
            "q": "A group reports: the lamp is dark, the ammeter reads "
                 "0.00 A, and the voltmeter reads 2.94 V. Every clip is "
                 "tight. What have they most likely done?",
            "options": [
                "Wired the voltmeter into the loop instead of across the lamp",
                "Wired the ammeter across the lamp instead of in the loop",
                "Left the switch open",
                "Put the cells in the holder the wrong way round",
            ],
            "answer": 0,
            "feedback": {
                1: "That fault gives a huge ammeter reading, not zero, and "
                   "the ammeter would have gone off the scale. A near-full "
                   "voltmeter reading with no current is the signature of a "
                   "voltmeter in the loop.",
                2: "An open switch gives zero on both meters. Here the "
                   "voltmeter is reading almost the whole battery p.d., so "
                   "something is completing the loop — through the "
                   "voltmeter.",
                3: "Reversed cells still drive the lamp; a digital meter "
                   "would just show a minus sign. Nothing here points at "
                   "polarity.",
            },
            "title": "Rung 1 · Read the symptom"},
        "apply": {
            "q": "A student wires the voltmeter into the loop, sees it read "
                 "2.94 V on a 3.0 V battery, and concludes the circuit is "
                 "working properly. What is right?",
            # ⚑ Option A is FINISHED into a complete wrong rule so that the
            # correct answer is no longer a length tell. Her wrong idea and
            # her correction are untouched; the clause after the dash states
            # the rule the wrong idea depends on. See DEPARTURES-P8.md row 1.
            "options": [
                "The student is right — 2.94 V out of 3.0 V is close enough, "
                "so the circuit is fine, because a voltmeter that reads "
                "almost the whole supply is showing that almost the whole "
                "supply is reaching the component it is measuring.",
                "The reading is wrong — a voltmeter in the loop cannot "
                "measure anything.",
                "The reading is correct and the circuit is not. The "
                "voltmeter’s huge resistance is now the only thing in the "
                "loop that matters, so it takes almost all the p.d. and "
                "almost no current flows.",
                "The reading is correct and the circuit is not, because a "
                "voltmeter has no resistance and short-circuits the lamp.",
            ],
            "answer": 2,
            "feedback": {
                0: "The number looks reassuring and the lamp is dark. A "
                   "reading close to the battery’s value tells you the "
                   "voltmeter is holding the p.d., not that the lamp is "
                   "getting it.",
                1: "It measures perfectly well; it is measuring the p.d. "
                   "across itself. The fault is in what the circuit has "
                   "become, not in the instrument.",
                3: "The verdict is right and the reason is inside out — that "
                   "describes an ammeter. A voltmeter has an enormous "
                   "resistance, which is why it strangles the loop instead of "
                   "shorting it.",
            },
            "title": "Rung 2 · The one that catches people"},
        "explain": {
            "q": "Explain why an ammeter is connected in the loop and a "
                 "voltmeter across a component, referring to the resistance "
                 "of each meter and to what would happen if they were "
                 "swapped.",
            "field_label": "Your explanation",
            "placeholder": "An ammeter has almost no resistance, so…",
            "success": [
                "Says an ammeter has almost no resistance, so it can sit in "
                "the loop without changing the current.",
                "Says a voltmeter has an enormous resistance, so it can sit "
                "across a component without drawing much current.",
                "Says a p.d. is a difference between two points, so a "
                "voltmeter needs a lead on each side.",
                "Says an ammeter across a lamp offers a route with no "
                "resistance, shorting the lamp out and taking a dangerous "
                "current.",
                "Says a voltmeter in the loop adds an enormous resistance, so "
                "almost no current flows and the lamp stays dark.",
            ],
            "title": "Rung 3 · Explain"},
        "produce": {
            "q": "Plan an investigation into how the current through a lamp "
                 "depends on the number of cells driving it. Say what you "
                 "would change, what you would measure, what you would keep "
                 "the same, and how you would make the result trustworthy.",
            "field_label": "Your plan",
            "placeholder": "I would change the number of cells from one to "
                           "four…",
            "success": [
                "Names the variable to change: the number of cells, in equal "
                "steps.",
                "Names what to measure: the current on an ammeter in the "
                "loop, and the p.d. across the lamp on a voltmeter.",
                "Names what to keep the same: the same lamp, the same leads, "
                "the same connections.",
                "Says each reading is repeated, and describes what to do with "
                "an odd value — take it again rather than smooth it over.",
                "Says how the results are recorded and shown: a table with "
                "units in the headings, and a graph of current against p.d. "
                "or against the number of cells.",
            ],
            "title": "Rung 4 · Take it somewhere new"},
    },

    "key_note": "An ammeter is made with almost no resistance so that it can "
                "sit in the loop without changing the current; a voltmeter is "
                "made with an enormous resistance so that it can sit across a "
                "component without changing the p.d. Putting either in the "
                "other's place builds a different circuit: an ammeter across "
                "a lamp shorts it out, and a voltmeter in the loop stops "
                "almost all the current. Build from the diagram with the "
                "switch open, check the loop, close the switch, take both "
                "readings at the same moment, and repeat any value that "
                "refuses to sit with the rest.",

    "stretch": [
        {"id": "neither-meter-is-innocent",
         "type": "explainer",
         "text": "Neither meter is quite innocent. An ammeter has a small "
                 "resistance, so putting it in the loop lowers the current a "
                 "little; a voltmeter has a large but finite resistance, so "
                 "hanging it across a component draws a little current away. "
                 "Both effects are tiny in a school circuit and neither is "
                 "zero, which is why a careful experimenter reports what the "
                 "meters were as well as what they read. The art of "
                 "instrument design is making that disturbance small enough "
                 "to ignore — and the art of measurement is knowing when it "
                 "no longer is."},
        {"id": "a-multimeter-is-the-same-instrument",
         "type": "explainer",
         "text": "A multimeter is the same instrument with a switch. Turn the "
                 "dial to amps and it puts a tiny resistance in the circuit; "
                 "turn it to volts and it puts an enormous one; turn it to "
                 "ohms and it supplies its own small current and does the "
                 "division for you. That last setting is exactly the "
                 "calculation of the resistance lesson, wired into a box — "
                 "which is why an ohms setting only ever works on a component "
                 "that has been disconnected from everything else."},
    ],

    "support": [],

    "vocabulary": [
        {"term": "in the loop",
         "definition": "Wired so that the whole current passes through it. "
                       "Where an ammeter goes, and a switch, and a fuse."},
        {"term": "across a component",
         "definition": "Wired with one lead on each side of it, in parallel "
                       "with it. Where a voltmeter goes."},
        {"term": "anomalous result",
         "definition": "A value that refuses to sit with the rest. Repeat "
                       "that setting before writing it down; never smooth it "
                       "over on the graph."},
    ],

    "tutor": {
        "anchor": "s-wire",
        "prompt": "Ask Mr Badmus AI",
        "body": "Got a circuit that will not work and a symptom to describe?",
        "cta": "Ask about this lesson"},

    "ks4_becomes": "The required practical on current–p.d. characteristics, "
                   "systematic and random error, and how a meter's own "
                   "resistance limits the measurement.",

    "convention_note": "The bench is a teaching model. The lamp is treated as "
                       "a fixed 10 ohms, the battery and leads as having no "
                       "resistance, the ammeter as having none and the "
                       "voltmeter as having one megohm; real components "
                       "differ, a real filament's resistance rises as it "
                       "heats, and a real ammeter and battery both have a "
                       "small resistance of their own. The short-circuit "
                       "reading is shown as off the scale rather than as a "
                       "figure, because what a real supply and a real meter "
                       "do in that state depends on the equipment and none of "
                       "it is a measurement. Readings are rounded to two "
                       "decimal places.",

    "ws": ["planning", "measurement", "evaluation"],
}
