"""P8 L4 — Potential difference (MODEL).

Authored against Claude Design's approved page,
`docs/ks3/design-reference/p8/p8-04-potential-difference.dc.html`.

Her page wins outright. The number stamped on a bulb, the loop with four
voltmeter positions, the ratings table, the part–whole bar, both worked
examples, both attempts and all four rungs are hers.

── ⚖️ MRB-204 · A PART–WHOLE BAR, AND IT KEEPS ITS COVER BUTTONS ─────

`V = a + b` is a SUM: the battery's push is SHARED OUT round a series
loop. `a = b = V` in parallel is the one permitted extra display line, and
the physics needs it, because the same quantity behaves oppositely in the
other arrangement.

⚖️ **THE PARTS ARE UNEQUAL, AND THE WEIGHTS ARE MEASURED OFF HER SVG.**
177 against 373 of a 560-wide whole — the bigger share to the thing that
resists more, drawn rather than asserted.

⚠️ **HER FLAG 5: TWO PART–WHOLE BARS THREE SLOTS APART.** `p8-03`'s and
this one. The visual similarity is deliberate — current splits at a
junction, p.d. splits round a loop, and they are the pair of rules
students most often swap — and each block states its own relationship
from nothing. She asks a reviewer to confirm it reads as a designed
pairing rather than a copied component. Nothing here changes it.

── ⚖️ RULED · THE WIRE LINK IS A REAL COMPONENT AND READS 0.00 V ─────

Not a degenerate state to be avoided: it is the cleanest demonstration in
the lesson that a p.d. is a DIFFERENCE, and that something with almost
nothing to resist the flow has almost no difference across its ends.

── ⚠️ FOUR RAIL STOPS ───────────────────────────────────────────────

    s-hook · s-volt · s-bar · s-ladder

⚠️ **MRB-208** — the `s-bar` id goes on the ATTEMPT PANEL, because
Design's own `DONE` reads `s.q[0].open && s.q[1].open`.

⚠️ **THE RATINGS FIGURE TAKES NO ANCHOR.** Design's own section carries no
`id`, and her `RAIL` is four entries with the figure not among them.

── ⚖️ FOUR MISCONCEPTIONS ───────────────────────────────────────────

    CIRC-13  voltage flows round the circuit and is used up  (hers, §7)
    CIRC-14  a voltmeter goes in the loop, like an ammeter   (hers, §7)
    CIRC-15  a full-battery reading across one component is a fault (hers)
    CIRC-16  a rating says how much electricity a bulb uses  (from the hook)

⚠️ **`CIRC-14` HAS NO `elicited_by`, AND THAT IS A CORRECTION TO DESIGN'S
TABLE RATHER THAN AN OMISSION.** Her §7 gives it `r1` of `p8-07` — a
cross-page pointer. MRB-248 requires `elicited_by` to resolve on its OWN
built page, so it is left absent here, which §5.3 allows. The belief is
still elicited on `p8-07`; what it may not do is claim that from this
page.

`CIRC-13` has no `elicited_by` either, and that one is hers: nothing on
this page asks the student to commit to it.

── ⚠️ POSITION IS AUTHORED. This lesson takes indices 3 and 1.
"""

LESSON = {
    "slug":  "potential-difference",
    "title": "Potential difference",
    "discipline": "physics",
    "unit": "Electric circuits",
    "family": "MODEL",

    "covers": ["KS3.P.CUR.02a"],
    "touches": ["KS3.WS.ANA.01"],
    "beyond_statutory": False,
    "threads": [{"id": "electricity", "level": 2}],
    "typical_year": 8,
    "typical_minutes": 60,

    "requires": ["current-at-a-junction"],
    "assumes": [],
    "references": ["series-and-parallel",
                   "building-and-measuring-a-circuit"],
    "ks4_links": [],

    "meta_description": "A voltmeter never goes in a circuit. It goes across "
                        "a part of one, and it answers a different question "
                        "from an ammeter: not how much is flowing, but how "
                        "hard it was pushed through there.",

    "big_question": "A voltmeter never goes in a circuit. It goes across a "
                    "part of one, and it answers a different question from an "
                    "ammeter: not how much is flowing, but how hard it was "
                    "pushed through there.",

    "rail": [
        {"anchor": "s-hook",   "short": "RATING",
         "label": "The number on a bulb",  "done_when": "committed"},
        {"anchor": "s-volt",   "short": "BENCH",
         "label": "Move the voltmeter",    "done_when": "gate_and_a_control"},
        {"anchor": "s-bar",    "short": "CFIFA",
         "label": "The bar and five steps", "done_when": "attempt_checked"},
        {"anchor": "s-ladder", "short": "LADDER",
         "label": "Mastery ladder",        "done_when": "ladder_complete"},
    ],

    "phenomenon": {
        "kind": "narrative",
        "title": "Every bulb has a number stamped on it.",
        "prompt": "A torch bulb says 2.5 V. A car headlamp says 12 V. A mains "
                  "lamp says 230 V. Put the 2.5 V bulb on a 12 V battery and "
                  "it flares once and dies; put the 12 V lamp on a single "
                  "cell and nothing visible happens at all.",
        "commit": "What is that number telling you?",
        "options": [
            "The potential difference it is designed to have across it",
            "How much electricity it uses up in every second it is on",
            "The current that will flow through it, measured in volts",
            "How bright it is when it is working the way it should",
        ],
        "answer": 0,
        "reveal": "It is the p.d. the maker designed it for — the push it "
                  "expects to have across it. Give it much less and the "
                  "filament never gets hot enough to glow properly; give it "
                  "much more and the current through it is too big and the "
                  "filament burns out. The rating is a specification, not a "
                  "measurement of what the bulb is doing at any moment.",
    },

    "misconceptions": [
        {"id": "CIRC-13",
         "statement": "Voltage flows round the circuit and gets used up by "
                      "each bulb.",
         "confronted_by": "s-think"},
        {"id": "CIRC-14",
         "statement": "A voltmeter goes in the circuit, like an ammeter.",
         "confronted_by": "s-think"},
        {"id": "CIRC-15",
         "statement": "A reading equal to the battery's p.d. across one "
                      "component must be a fault.",
         "elicited_by": "s-ladder",
         "confronted_by": "volt"},
        {"id": "CIRC-16",
         "statement": "The number stamped on a bulb says how much electricity "
                      "it uses up while it is on.",
         "elicited_by": "s-hook",
         "confronted_by": "s-hook"},
    ],

    "core": [
        {"type": "hook", "id": "hook-commit", "anchor": "s-hook"},

        {"type": "explainer",
         "text": "A cell does not make charge. It gives the charge <strong>"
                 "energy</strong>, and pushes it out into the circuit "
                 "carrying that energy. <strong>Potential difference</strong> "
                 "— p.d. for short, often just called voltage — measures how "
                 "much energy each bit of charge gives up between two points. "
                 "It is measured in <strong>volts</strong>, written "
                 "<strong>V</strong>."},
        {"type": "explainer",
         "text": "Because it is a difference between two points, you can only "
                 "ever measure it <em>across</em> something. That is why a "
                 "<strong>voltmeter</strong> is connected in parallel with a "
                 "component, with a lead to each side of it — not in the "
                 "loop. An ammeter asks \"how much is going past here?\"; a "
                 "voltmeter asks \"how much energy was given up between here "
                 "and there?\""},
        {"type": "explainer",
         "text": "In a series loop the battery's p.d. is <strong>shared "
                 "out</strong> between the components: whatever the charge "
                 "was given, it hands back on its way round, and the shares "
                 "add up to the battery's value. The bigger share goes to "
                 "whatever resists more. In parallel it is different — each "
                 "branch is connected straight across the battery, so each "
                 "branch gets the <em>whole</em> p.d."},

        # ── #s-volt · one loop, one voltmeter, four places to put it ───
        {"type": "voltmeter-tap",
         "id": "volt",
         "anchor": "s-volt",
         "eyebrow": "At the bench · one series loop, one voltmeter, four "
                    "places to put it",
         "heading": "Move the voltmeter across.",
         # A MAP, NOT A STRING. `progress` authored as a string is
         # read as a COUNT FORMAT (MRB-248's widening), and these
         # are two named states rather than a tally.
         "progress": {"idle": "Change a control to begin",
                      "live": "Three controls live"},
         "lead": "A lamp and a second component in one loop. Change the "
                 "battery, change the second component, and connect the "
                 "voltmeter across each thing in turn.",
         "lamp_ohms": 10,
         "volts_per_cell": 1.5,
         "start_cells": 2,
         "start_comp": 0,
         "start_pos": 1,
         "battery_label": "BATTERY",
         "loop_label": "ONE LOOP, ONE CURRENT",
         "batt_label": "The battery",
         "comp_label": "The second component",
         "pos_label": "The voltmeter goes across",
         "gate": {
             "prompt": "Commit first. Two identical lamps sit in series on a "
                       "3.0 V battery. A voltmeter across the first lamp "
                       "reads 1.5 V. What will it read across both lamps "
                       "together?",
             "options": [
                 "3.0 V — the two shares add back to the battery's value",
                 "1.5 V — the same as across one lamp",
                 "0.0 V — the two shares cancel each other out",
                 "6.0 V — two lamps at 1.5 V each, doubled",
             ],
             "answer": 0,
         },
         "batteries": [
             {"cells": 2, "label": "2 cells (3.0 V)",
              "sub": "2 cells at 1.5 V each"},
             {"cells": 3, "label": "3 cells (4.5 V)",
              "sub": "3 cells at 1.5 V each"},
         ],
         "components": [
             {"id": "lamp", "label": "A second lamp", "name": "LAMP",
              "ohms": 10, "sub": "10 ohms", "shape": "lamp"},
             {"id": "res", "label": "A 20 ohm resistor", "name": "RESISTOR",
              "ohms": 20, "sub": "20 ohms", "shape": "res"},
             {"id": "wire", "label": "A plain wire link", "name": "WIRE LINK",
              "ohms": 0, "sub": "almost no resistance", "shape": "wire"},
         ],
         # Design's own four lead routings, at two y levels so they never
         # cross, with the tap dots at the points each pair measures.
         "positions": [
             {"id": "batt", "label": "The battery",
              "caption": "across the battery", "name": "the battery",
              "lead": "M454 270 V225 H200 V110 M546 270 V330 H200 V380",
              "taps": "200,110 200,380"},
             {"id": "lamp", "label": "The lamp",
              "caption": "across the lamp", "name": "the lamp",
              "lead": "M454 270 V225 H340 V110 M546 270 V200 H420 V110",
              "taps": "340,110 420,110"},
             {"id": "comp", "label": "The second component",
              "caption": "across the second component",
              "name": "the second component",
              "lead": "M454 270 V200 H620 V110 M546 270 V225 H700 V110",
              "taps": "620,110 700,110"},
             {"id": "both", "label": "Both components",
              "caption": "across both components at once",
              "name": "both components together",
              "lead": "M454 270 V225 H340 V110 M546 270 V200 H700 V110",
              "taps": "340,110 700,110"},
         ],
         "readouts": [
             {"id": "batt", "label": "The battery gives", "sub": "—"},
             {"id": "a", "label": "Across the lamp", "sub": "10 ohms"},
             {"id": "b", "label": "Across the second one", "sub": "—"},
             {"id": "reading", "label": "The voltmeter reads", "sub": "—"},
         ],
         "branches": {
             "battery":
                 "Across the battery the meter reads {v}, which is what {n} "
                 "cells at 1.5 V each supply. That whole amount is shared out "
                 "round the loop: {a} across the lamp and {b} across the "
                 "{name}. Add those two and you are back at {v}.",
             "both":
                 "Across both components together the meter reads {v} — "
                 "exactly what it read across the battery. That is the "
                 "sharing rule seen in one measurement: everything the "
                 "battery gave, the two components between them give back. "
                 "Individually they read {a} and {b}.",
             "zero":
                 "Across the wire link the meter reads 0.00 V. A plain wire "
                 "has almost nothing to resist the flow, so the charge gives "
                 "up almost no energy crossing it and there is almost no "
                 "difference between its two ends. The lamp is left holding "
                 "the entire {v}, which is why swapping a component for a "
                 "piece of wire makes everything else in the loop work "
                 "harder.",
             "share":
                 "Across {this} the meter reads {reading}. That is {cmp}. The "
                 "other share, across {other}, is {otherv}, and the two add "
                 "to the {v} the battery supplies. The current is the same "
                 "through both — one loop, one current — so the difference is "
                 "entirely in the resistance.",
         }},

        # ── the ratings figure · no anchor, because her section has none ──
        {"type": "circ-band",
         "id": "what-a-rating-means",
         "eyebrow": "The figure",
         "heading": "What a rating means",
         "lead": "A rating is not a measurement of the component. It is the "
                 "p.d. the maker designed it to run at — the value at which "
                 "it is as bright, or as loud, or as warm as it is meant to "
                 "be.",
         "table": {
             "corner": "Component",
             "min_width": 640,
             "columns": ["Rating", "Run under it", "Run over it"],
             "rows": [
                 {"head": "Torch bulb",
                  "cells": ["2.5 V", "Dim, or a dull red glow",
                            "One bright flash, then a broken filament"]},
                 {"head": "Car headlamp",
                  "cells": ["12 V",
                            "Yellow and weak — a flat battery looks like this",
                            "A much shorter life"]},
                 {"head": "Mains lamp",
                  "cells": ["230 V", "Nothing you would notice on a cell",
                            "Fails at once"]},
                 {"head": "A single cell",
                  "cells": ["1.5 V",
                            {"text": "A battery's rating is what it "
                                     "<em>supplies</em>, not what it needs. "
                                     "Cells in series add: four of them give "
                                     "6.0 V.",
                             "span": True}]},
             ],
         },
         "close": "The last row is the one to watch. A component's rating "
                  "says what it wants; a battery's rating says what it gives. "
                  "Matching them is the whole job — and in a series loop what "
                  "a component actually gets is only its <em>share</em>, not "
                  "the battery's full value."},

        # ── #s-bar · the relationship, the two examples, the attempt ───
        {"type": "formula",
         "id": "sharing-rule",
         "eyebrow": "Writing it down · the shape of this relationship",
         "statement": "The battery's push is shared out round a series loop",
         "support": ["In parallel each branch gets the whole: a = b = V",
                     "V · potential difference of the battery · V",
                     "a · potential difference across the first component · V",
                     "b · potential difference across the second component · "
                     "V"],
         "cover": {
             "shape": "bar",
             "eyebrow": "The bar",
             "heading": "Cover the one you want",
             "aria_label": "A part-whole bar. One long bar labelled V sits "
                           "above two unequal bars, a and b, which together "
                           "fill exactly the length of V.",
             "whole": {"id": "V", "label": "V", "button": "Cover V"},
             "parts": [
                 {"id": "a", "label": "a", "button": "Cover a", "weight": 177},
                 {"id": "b", "label": "b", "button": "Cover b", "weight": 373},
             ],
             "covered": "V",
             "results": {
                 "V": {"result": "V = a + b",
                       "sentence": "Cover the battery and the two shares are "
                                   "left side by side — add them."},
                 "a": {"result": "a = V − b",
                       "sentence": "Cover the first share and the battery and "
                                   "the second share are left — take the "
                                   "second share away from the whole."},
                 "b": {"result": "b = V − a",
                       "sentence": "Cover the second share and the battery "
                                   "and the first share are left — take the "
                                   "first share away from the whole."},
             },
             "close": "Two parts side by side make the whole. Cover the part "
                      "you want and take the other one away from the whole.",
         }},

        {"type": "worked-example", "id": "cfifa-pd-plain"},
        {"type": "worked-example", "id": "cfifa-pd-convert"},
        {"type": "check", "id": "your-turn-pd", "anchor": "s-bar"},

        {"type": "key-fact", "ref": "pd-is-energy-per-charge"},

        {"type": "misconception", "id": "think-voltage-flows",
         "anchor": "s-think"},

        {"type": "quiz", "anchor": "s-ladder"},
        {"type": "summary", "id": "s-keynote"},
    ],

    "activities": [
        {"id": "cfifa-pd-plain",
         "kind": "worked-example",
         "demand": "calculate",
         "eyebrow": "Worked example · one step at a time",
         "heading": "A 4.5 V battery drives a lamp and a buzzer in series. A "
                    "voltmeter across the lamp reads 1.8 V. What is the p.d. "
                    "across the buzzer?",
         "head_counter": {"format": "Step {n} of 5", "total": 5},
         "buttons": {"first": "Show the first step",
                     "next": "Show the next step",
                     "done": "All five shown",
                     "done_note": "Nothing needed converting there. Now the "
                                  "one that does."},
         "staged": True,
         "fifa": [
             {"letter": "C", "label": "Convert",
              "line": "4.5 V stays 4.5 V · 1.8 V stays 1.8 V",
              "note": "The battery and the voltmeter are both quoted in "
                      "volts, so there is nothing to convert."},
             {"letter": "F", "label": "Formula", "line": "b = V − a",
              "note": "Cover b on the bar: the battery’s value with the other "
                      "share taken away."},
             {"letter": "I", "label": "Insert", "line": "b = 4.5 V − 1.8 V",
              "note": "The whole is the battery, 4.5 V. The share you know is "
                      "the lamp’s, 1.8 V."},
             {"letter": "F", "label": "Fine-tune", "line": "4.5 − 1.8 = 2.7",
              "note": "Volts take away volts leaves volts."},
             {"letter": "A", "label": "Answer", "line": "b = 2.7 V",
              "note": "Check it: 1.8 V and 2.7 V add to the 4.5 V of the "
                      "battery."},
         ]},

        {"id": "cfifa-pd-convert",
         "kind": "worked-example",
         "demand": "calculate",
         "eyebrow": "Worked example · one step at a time",
         "heading": "A 12 V supply drives two resistors in series. The "
                    "voltmeter across the first reads 4500 mV. What is the "
                    "p.d. across the second?",
         "head_counter": {"format": "Step {n} of 5", "total": 5},
         "buttons": {"first": "Show the first step",
                     "next": "Show the next step",
                     "done": "All five shown",
                     "done_note": "Convert first, then the same four lines. "
                                  "Your turn below."},
         "staged": True,
         "fifa": [
             {"letter": "C", "label": "Convert",
              "line": "4500 mV ÷ 1000 = 4.5 V",
              "note": "There are 1000 millivolts in a volt, so divide before "
                      "you take anything away."},
             {"letter": "F", "label": "Formula", "line": "b = V − a",
              "note": "Cover b on the bar: the whole with the other share "
                      "taken away."},
             {"letter": "I", "label": "Insert", "line": "b = 12 V − 4.5 V",
              "note": "The converted share goes in. The millivolt reading "
                      "never does."},
             {"letter": "F", "label": "Fine-tune", "line": "12 − 4.5 = 7.5",
              "note": "Volts take away volts leaves volts."},
             {"letter": "A", "label": "Answer", "line": "b = 7.5 V",
              "note": "Take 4500 from 12 instead and you get − 4488 V, which "
                      "no supply in the room could give."},
         ]},

        {"id": "your-turn-pd",
         "kind": "p8-attempt",
         "demand": "calculate",
         "eyebrow": "Your turn · the same five steps",
         # The bench's opening state: two cells and a second lamp, so 3.0 V
         # shared evenly. `v1` is the one-decimal form her closing line uses
         # and `v2` the two-decimal form her Convert and Insert lines use —
         # two tokens because her own strings ask for both.
         "rest": {"v1": "3.0", "v2": "3.00", "a": "1.50 V", "b": "1.50 V",
                  "anum": "1.50", "bnum": "1.50", "name": "lamp"},
         "questions": [
             {"id": "q1", "tab": "Question 1",
              "head": "Your loop: the battery gives {v1} V and the voltmeter "
                      "across the lamp reads {a}.",
              "lead": "Write each line out yourself — starting by deciding "
                      "whether anything needs converting. Then check your "
                      "working and tick the lines you had.",
              "steps": [
                  {"letter": "C", "label": "Convert",
                   "placeholder": "anything to convert?",
                   "line": "{v2} V stays {v2} V · {a} stays {a}",
                   "note": "The battery and the voltmeter are both in volts, "
                           "so nothing changes."},
                  {"letter": "F", "label": "Formula", "line": "b = V − a",
                   "note": "Cover b on the bar: the whole with the other "
                           "share taken away."},
                  {"letter": "I", "label": "Insert",
                   "line": "b = {v2} V − {a}",
                   "note": "The whole is the battery; the share you know is "
                           "the lamp’s."},
                  {"letter": "F", "label": "Fine-tune",
                   "line": "{v2} − {anum} = {bnum}",
                   "note": "Volts take away volts leaves volts."},
                  {"letter": "A", "label": "Answer",
                   "placeholder": "remember the unit",
                   "line": "b = {b}",
                   "note": "Put the voltmeter across the second component and "
                           "it reads {b}."},
              ],
              "close": "The five lines give {b} across the {name}, and {a} + "
                       "{b} is the {v1} V of the battery."},
             {"id": "q2", "tab": "Question 2",
              "head": "A 6.0 V battery drives a lamp and a buzzer in series. "
                      "The voltmeter across the lamp reads 1500 mV.",
              "lead": "This one needs the Convert line to do some work.",
              "steps": [
                  {"letter": "C", "label": "Convert",
                   "placeholder": "anything to convert?",
                   "line": "1500 mV ÷ 1000 = 1.5 V",
                   "note": "There are 1000 millivolts in a volt, so divide "
                           "before you take anything away."},
                  {"letter": "F", "label": "Formula", "line": "b = V − a",
                   "note": "Cover b on the bar: the whole with the other "
                           "share taken away."},
                  {"letter": "I", "label": "Insert",
                   "line": "b = 6.0 V − 1.5 V",
                   "note": "The converted share goes in. The millivolt "
                           "reading never does."},
                  {"letter": "F", "label": "Fine-tune",
                   "line": "6.0 − 1.5 = 4.5",
                   "note": "Volts take away volts leaves volts."},
                  {"letter": "A", "label": "Answer",
                   "placeholder": "remember the unit",
                   "line": "b = 4.5 V",
                   "note": "Take 1500 from 6.0 instead and the buzzer comes "
                           "out at − 1494 V."},
              ],
              "close": "The five lines give 4.5 V across the buzzer, and "
                       "1.5 V + 4.5 V is the 6.0 V of the battery."},
         ]},

        {"id": "think-voltage-flows",
         "kind": "predict",
         "demand": "explain",
         "targets": "CIRC-13",
         "statements": [
             {"quote": "Voltage flows round the circuit and gets used up by "
                       "each bulb.",
              "targets": "CIRC-13",
              "body": [
                  "Nothing flows except charge. Potential difference is not a "
                  "substance travelling anywhere — it is a difference between "
                  "two places, like the drop between the top and the bottom "
                  "of a hill. You would not say the height flows down the "
                  "hill. The reason p.d. sounds like something being used up "
                  "is that the shares do add to the battery's value, which is "
                  "true and useful; but the thing being handed over is "
                  "<em>energy</em>, and the thing carrying it is the current.",
              ]},
             {"quote": "A voltmeter goes in the circuit, like an ammeter.",
              "targets": "CIRC-14",
              "body": [
                  "It cannot. A p.d. is a difference between two points, so a "
                  "voltmeter needs a lead on each of them — it goes across a "
                  "component, in parallel with it. Wire one into the loop "
                  "instead and the circuit stops: a voltmeter is built to let "
                  "almost no current through, which is exactly what makes it "
                  "safe to hang across things without changing them. An "
                  "ammeter is the opposite, built to let current through as "
                  "freely as a piece of wire, which is why putting one across "
                  "a battery is a short circuit.",
              ]},
         ]},
    ],

    "figures": [],

    "key_facts": [
        {"id": "pd-is-energy-per-charge",
         "eyebrow": "Key fact",
         "ground": "card",
         "placement": "top-level",
         "text": "Potential difference is the energy each unit of charge "
                 "gives up between two points, measured in volts (V) on a "
                 "voltmeter connected across a component. Round a series loop "
                 "the battery's p.d. is shared out and the shares add to it: "
                 "V = a + b. In parallel every branch gets the whole of it."},
    ],

    # ⚠️ MRB-278 · POSITION IS AUTHORED. This lesson takes indices 3 and 1.
    "ladder": {
        "recall": {
            "q": "Three components sit in series on a 6.0 V battery. "
                 "Voltmeters across the first two read 1.5 V and 3.0 V. What "
                 "is the p.d. across the third?",
            "options": [
                "10.5 V — add all three readings together",
                "2.0 V — share the 6.0 V equally between the three",
                "6.0 V — every component in a loop gets the battery’s full "
                "p.d.",
                "1.5 V",
            ],
            "answer": 3,
            "feedback": {
                0: "You have added the parts to the whole. The whole is "
                   "already given as 6.0 V; the third share is what is left "
                   "of it.",
                1: "The shares are not equal here — two of them are measured "
                   "at 1.5 V and 3.0 V. The bigger share goes to whatever "
                   "resists more.",
                2: "That is the rule for parallel branches. In series the "
                   "p.d. is shared out, which is why the first two readings "
                   "are smaller than 6.0 V.",
            },
            "title": "Rung 1 · Calculate"},
        "apply": {
            "q": "A student measures 3.0 V across a battery and 3.0 V across "
                 "the single lamp in its loop, and concludes the meter must "
                 "be broken because the voltage should have been used up. "
                 "What is right?",
            # ⚑ Option A is FINISHED into a complete wrong rule so that the
            # correct answer is no longer a length tell. Her wrong idea and
            # her correction are untouched; the clause after the dash states
            # the rule the wrong idea depends on. See DEPARTURES-P8.md row 1.
            "options": [
                "The student is right — the reading across the lamp should be "
                "smaller, because the lamp uses some of the voltage up on its "
                "way round, so what is left over is what the voltmeter across "
                "the battery is showing.",
                "Both readings are correct. With one component in the loop it "
                "takes the whole share, so the p.d. across it equals the p.d. "
                "across the battery.",
                "The reading across the lamp should be 1.5 V, because half "
                "the p.d. is lost in the connecting wires.",
                "Both readings are correct, because a voltmeter always reads "
                "the battery’s value wherever you put it.",
            ],
            "answer": 1,
            "feedback": {
                0: "The shares have to add to the battery’s value, and with "
                   "only one component there is nothing else to share with. "
                   "It gets all of it.",
                2: "Connecting wires do take a share, but a tiny one — "
                   "nothing like half. In a school circuit it is too small to "
                   "read.",
                3: "The verdict is right and the reason is not. Put a second "
                   "component in the loop and the voltmeter across the lamp "
                   "reads less than the battery does.",
            },
            "title": "Rung 2 · The one that catches people"},
        "explain": {
            "q": "A 3.0 V battery drives a lamp and a 20 ohm resistor in "
                 "series. A voltmeter across the lamp reads 1.0 V. Explain "
                 "what it reads across the resistor, what it reads across "
                 "both together, and why the shares are not equal.",
            "field_label": "Your explanation",
            "placeholder": "The shares have to add to…",
            "success": [
                "Gives 2.0 V across the resistor, with the unit.",
                "Gives 3.0 V across both together, and says this is the same "
                "as across the battery.",
                "Says the shares add up to the battery’s p.d.",
                "Says the resistor takes the bigger share because it resists "
                "more.",
                "Says the current is the same through both, so the difference "
                "is in the resistance and not in the flow.",
            ],
            "title": "Rung 3 · Explain"},
        "produce": {
            "q": "You have a 6 V battery and one 6 V bulb, and you need to "
                 "run two of those bulbs at full brightness at the same time. "
                 "Explain how you would wire them and why, and say what would "
                 "go wrong with the other arrangement.",
            "field_label": "Your answer",
            "placeholder": "Each bulb needs the full 6 V across it, so…",
            "success": [
                "Says each bulb needs 6 V across it to be at full "
                "brightness.",
                "Wires the two bulbs in parallel across the battery.",
                "Says each parallel branch gets the whole 6 V, so both run at "
                "their rating.",
                "Says in series the 6 V would be shared, giving about 3 V "
                "each, so both would be dim.",
                "Notes the cost of parallel: the battery supplies both "
                "currents added together, so it goes flat sooner.",
            ],
            "title": "Rung 4 · Take it somewhere new"},
    },

    "key_note": "Potential difference measures how much energy each unit of "
                "charge gives up between two points, in volts (V). Because it "
                "is a difference, a voltmeter is connected across a component "
                "rather than in the loop. Round a series loop the battery's "
                "p.d. is shared out between the components and the shares add "
                "up to it, with the bigger share going to whatever resists "
                "more; in parallel each branch is connected straight across "
                "the battery and gets the whole of it. A component's rating "
                "is the p.d. it was designed to run at; a battery's rating is "
                "the p.d. it supplies.",

    "stretch": [
        {"id": "one-volt-is-one-joule-per-coulomb",
         "type": "explainer",
         "text": "One volt means one joule of energy given up by every "
                 "coulomb of charge. That is the whole definition, and it "
                 "explains something that sounds impossible: a 400 000 V "
                 "power line is not dangerous because of the number, and a "
                 "car battery at 12 V can weld metal. The volts say how much "
                 "energy each bit of charge carries; the amps say how many "
                 "bits go past each second. Damage needs both."},
        {"id": "the-sharing-rule-is-a-tool",
         "type": "explainer",
         "text": "The sharing rule is a tool as well as a fact. Put two "
                 "resistors in series across a supply and you can tap off any "
                 "fraction of it you like from the point between them — a "
                 "potential divider. It is how a volume slider, a joystick, a "
                 "fuel gauge and a light-dependent sensor all work: something "
                 "varies one resistance, the share of the voltage moves, and "
                 "a circuit reads the change."},
    ],

    "support": [],

    "vocabulary": [
        {"term": "potential difference",
         "definition": "How much energy each unit of charge gives up between "
                       "two points. Measured in volts, and always across "
                       "something."},
        {"term": "volt",
         "definition": "The unit of potential difference, written V. One volt "
                       "is one joule given up by every coulomb of charge."},
        {"term": "voltmeter",
         "definition": "The instrument that measures p.d. It goes ACROSS a "
                       "component, with one lead on each side of it."},
        {"term": "rating",
         "definition": "The p.d. a component was designed to run at. A "
                       "battery's rating is what it supplies instead."},
    ],

    "tutor": {
        "anchor": "s-volt",
        "prompt": "Ask Mr Badmus AI",
        "body": "Got a series loop and one voltmeter reading, and want the "
                "rest?",
        "cta": "Ask about this lesson"},

    "ks4_becomes": "Energy transferred = charge × p.d., the potential divider "
                   "equation, and Kirchhoff's second law round a loop.",

    "convention_note": "The bench is a teaching model. Every component is "
                       "treated as having a fixed resistance — lamp 10 ohms, "
                       "resistor 20 ohms, wire link 0 ohms — so the shares "
                       "are exact fractions; a real filament's resistance "
                       "rises as it heats and a real wire link is not quite "
                       "zero. The battery is treated as having no resistance "
                       "of its own, and the voltmeter as drawing no current "
                       "at all, so neither of them disturbs the reading. "
                       "Cells are taken as 1.5 V each. Readings are rounded "
                       "to two decimal places. The ratings in the figure are "
                       "typical values, and a bulb marked with a p.d. is "
                       "usually marked with a current or a power as well.",

    "ws": ["measurement", "analysis"],
}
