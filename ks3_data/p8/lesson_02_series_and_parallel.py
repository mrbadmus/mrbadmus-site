"""P8 L2 — Series and parallel (CONTRAST).

Authored against Claude Design's approved page,
`docs/ks3/design-reference/p8/p8-02-series-and-parallel.dc.html`.

Her page wins outright. The blown kitchen bulb, the two rewireable bulbs,
the five-way comparison table and all four rungs are hers.

── ⚖️ MRB-204 · NO FORMULA BLOCK ────────────────────────────────────

Both rules this lesson teaches are qualitative — how many paths there
are, and what happens to the others when one breaks. The arithmetic of
adding branch currents is `p8-03`'s and is carried here as an edge.

── ⚖️ RULED · EVERY BRIGHTNESS WORD IS COMPUTED ─────────────────────

`CIRC-05` is *in parallel the current is shared out, so each bulb is
dimmer*, and the only thing that kills it is reading `at full brightness`
twice beside a total that has doubled. An authored word per control would
be a second source for a fact the numbers already carry, and the two would
drift the moment a state was added.

── ⚖️ RULED · A REMOVED BULB IS A DASHED EMPTY SOCKET, NOT A GAP ────

The socket is still there; what has gone is the filament. In series that
empty socket is a break in the only path, and a student has to be able to
see the difference between *the bulb is out* and *the bulb is dark* — they
are the two different things the same arrangement does to the two bulbs.

── ⚠️ FOUR RAIL STOPS ───────────────────────────────────────────────

    s-hook · s-bench · s-compare · s-ladder

⚠️ `s-compare` takes `gate !== null` while the bench also wants a control
touched, so the bench marks it through `band_anchor` / `band_at`.

── ⚖️ FOUR MISCONCEPTIONS ───────────────────────────────────────────

    CIRC-05  in parallel the current is shared, so each bulb is dimmer
    CIRC-06  in series the first bulb gets the current first
    CIRC-07  two bulbs in series are each as bright as one
    CIRC-08  a fuse box is what keeps the other lights on   (from content)

`CIRC-06` has no `elicited_by`, which §5.3 allows: nothing on the page
asks the student to commit to it, and it is confronted because it sits
underneath one that is.

── ⚠️ POSITION IS AUTHORED. This lesson takes indices 1 and 3.
"""

LESSON = {
    "slug":  "series-and-parallel",
    "title": "Series and parallel",
    "discipline": "physics",
    "unit": "Electric circuits",
    "family": "CONTRAST",

    "covers": ["KS3.P.CUR.01b"],
    "touches": [],
    "beyond_statutory": False,
    "threads": [{"id": "electricity", "level": 1}],
    "typical_year": 8,
    "typical_minutes": 60,

    "requires": ["current-and-circuits"],
    "assumes": [],
    "references": ["potential-difference", "resistance"],
    "ks4_links": [],

    "meta_description": "Two bulbs, one battery, two ways to join them up. "
                        "One arrangement dims both bulbs and fails completely "
                        "if either one goes. The other keeps them bright and "
                        "survives.",

    "big_question": "Two bulbs, one battery, two ways to join them up. One "
                    "arrangement dims both bulbs and fails completely if "
                    "either one goes. The other keeps them bright and "
                    "survives.",

    "rail": [
        {"anchor": "s-hook",    "short": "HOUSE",
         "label": "One blown bulb",  "done_when": "committed"},
        {"anchor": "s-bench",   "short": "BENCH",
         "label": "Rewire it",       "done_when": "gate_and_a_control"},
        {"anchor": "s-compare", "short": "TABLE",
         "label": "Judged five ways", "done_when": "gate_committed"},
        {"anchor": "s-ladder",  "short": "LADDER",
         "label": "Mastery ladder",  "done_when": "ladder_complete"},
    ],

    "phenomenon": {
        "kind": "narrative",
        "title": "One blown bulb. The whole room stays lit.",
        "prompt": "A bulb goes in the kitchen. Nothing else in the house "
                  "notices — the hall stays lit, the fridge keeps running. "
                  "Yet a cheap string of decorations can lose one bulb and go "
                  "dark from end to end.",
        "commit": "What is different about the way those two sets of lamps "
                  "are joined to their supply?",
        "options": [
            "The house lamps each have their own path to the supply; the "
            "decorations are all threaded onto one path",
            "House wiring runs at a much higher voltage, and a higher "
            "voltage keeps working across a broken bulb",
            "The decorations use much smaller bulbs, and small bulbs are all "
            "made to fail together in a batch",
            "A house has a fuse box that keeps the other rooms going whenever "
            "one of its bulbs burns out",
        ],
        "answer": 0,
        "reveal": "It is the number of paths. Every light in a house has its "
                  "own branch off the supply, so a broken filament breaks one "
                  "branch and nothing else. A cheap decoration string threads "
                  "every bulb onto a single loop, so one broken filament is a "
                  "gap in the only path there is, and all hundred go out at "
                  "once.",
    },

    "misconceptions": [
        {"id": "CIRC-05",
         "statement": "In parallel the current has to split between the two "
                      "bulbs, so each one is dimmer.",
         "elicited_by": "bench",
         "confronted_by": "bench"},
        {"id": "CIRC-06",
         "statement": "In series the first bulb gets the current first, so "
                      "it is brighter than the second one.",
         "confronted_by": "s-think"},
        {"id": "CIRC-07",
         "statement": "Two bulbs in series are each as bright as one, because "
                      "the battery has not changed.",
         "elicited_by": "s-ladder",
         "confronted_by": "bench"},
        {"id": "CIRC-08",
         "statement": "A fuse box is what keeps the other lights on when one "
                      "bulb fails.",
         "elicited_by": "s-hook",
         "confronted_by": "s-hook"},
    ],

    "core": [
        {"type": "hook", "id": "hook-commit", "anchor": "s-hook"},

        {"type": "explainer",
         "text": "There are exactly two ways to add a second component to a "
                 "circuit. You can put it <strong>in the same loop</strong>, "
                 "so the charge has to go through one and then the other — "
                 "that is <strong>series</strong>. Or you can give it <strong>"
                 "a loop of its own</strong> off the same battery, so the "
                 "charge can go through one <em>or</em> the other — that is "
                 "<strong>parallel</strong>."},
        {"type": "explainer",
         "text": "Counting paths is how you tell them apart, and it is more "
                 "reliable than looking at the shape of the drawing. Follow a "
                 "route from one end of the battery to the other. If there is "
                 "only one route, everything on it is in series. If there is "
                 "a point where the route divides and later joins back up, "
                 "the branches are in parallel."},
        {"type": "explainer",
         "text": "The consequences are large. In series there is one current, "
                 "and every extra component makes it harder for the charge to "
                 "get round, so everything dims. In parallel each branch gets "
                 "the battery's full push, so two lamps are as bright as one "
                 "— and each branch is independent, so a break in one leaves "
                 "the others working."},

        # ── #s-bench · the same two bulbs, wired two ways ──────────────
        {"type": "two-arrangement-loop",
         "id": "bench",
         "anchor": "s-bench",
         "eyebrow": "At the bench · two identical bulbs, one 3.0 V battery",
         "heading": "Rewire it. Then take one out.",
         # A MAP, NOT A STRING. `progress` authored as a string is
         # read as a COUNT FORMAT (MRB-248's widening), and these
         # are two named states rather than a tally.
         "progress": {"idle": "Change a control to begin",
                      "live": "Both controls live"},
         "lead": "The same two bulbs and the same battery every time. Only "
                 "the wiring changes. An ammeter beside the battery reads the "
                 "total current leaving it.",
         "volts": 3.0,
         "one_amps": 0.30,
         "start_wire": "series",
         "start_out": 0,
         "band_anchor": "s-compare",
         "band_at": 1,
         "battery_label": "3.0 V",
         "bulb1_label": "BULB 1",
         "bulb2_label": "BULB 2",
         "series_caption": "ONE PATH ROUND",
         "parallel_caption": "TWO PATHS, ONE JUNCTION EACH END",
         "gate": {
             "prompt": "Commit first. One bulb on this battery draws 0.30 A. "
                       "You wire the two bulbs in parallel. What total "
                       "current leaves the battery?",
             "options": [
                 "0.30 A — the same as one bulb, shared between the two",
                 "0.15 A — each bulb gets half",
                 "0.60 A — each branch draws its own 0.30 A and they add at "
                 "the battery",
                 "0.30 A — the battery can only ever supply what it supplied "
                 "before",
             ],
             "answer": 2,
         },
         "wire_label": "How they are wired",
         "out_label": "Unscrew a bulb",
         "arrangements": [
             {"id": "series", "label": "In series"},
             {"id": "parallel", "label": "In parallel"},
         ],
         "removals": [
             {"id": 0, "label": "Both in"},
             {"id": 1, "label": "Bulb 1 out"},
             {"id": 2, "label": "Bulb 2 out"},
         ],
         "readouts": [
             {"id": "paths", "label": "Paths from + to −", "sub": "—"},
             {"id": "total", "label": "Total current from the battery"},
             {"id": "b1", "label": "Bulb 1", "sub": "—", "word": True},
             {"id": "b2", "label": "Bulb 2", "sub": "—", "word": True},
         ],
         "branches": {
             "series_both":
                 "One path round, so one current: {half} through the "
                 "battery, through bulb 1 and through bulb 2 alike. That is "
                 "half what a single bulb draws on this battery, because the "
                 "charge now has two bulbs to push through instead of one. "
                 "Both bulbs are equally dim, and swapping them over would "
                 "change nothing.",
             "series_out":
                 "Bulb {out} is out, and the meter reads {total}. There is "
                 "only one path from one end of the battery to the other, and "
                 "the missing bulb is a gap in it, so the other bulb is dark "
                 "as well — not dim, dark. It does not matter which of the "
                 "two you take out; the reading is the same.",
             "parallel_both":
                 "Two paths, so two currents that meet at the junctions: "
                 "{one} in each branch and {total} leaving the battery. Each "
                 "branch has the whole {volts} across it, which is why each "
                 "bulb is as bright as it would be on its own. Adding the "
                 "second bulb did not dim the first — it made the battery "
                 "work twice as hard.",
             "parallel_out":
                 "Bulb {out} is out and its branch carries nothing, but the "
                 "other branch is untouched: still {one}, still fully bright. "
                 "The total leaving the battery has dropped to {total}, which "
                 "is the honest signal that one lamp has gone. This is why a "
                 "house is wired this way.",
         }},

        # ── #s-compare · the same two bulbs, judged five ways ──────────
        {"type": "circ-band",
         "id": "compare-five-ways",
         "anchor": "s-compare",
         "eyebrow": "The figure",
         "heading": "The same two bulbs, judged five ways",
         "table": {
             "corner": "",
             "min_width": 620,
             "columns": ["Series", "Parallel"],
             "rows": [
                 {"head": "Paths the charge can take",
                  "cells": ["One, through both bulbs",
                            "Two, one through each bulb"]},
                 {"head": "Current from the battery",
                  "cells": ["0.15 A — <strong>halved</strong> by the second "
                            "bulb",
                            "0.60 A — <strong>doubled</strong> by the second "
                            "branch"]},
                 {"head": "Brightness of each bulb",
                  "cells": ["Both dim", "Both at full brightness"]},
                 {"head": "If one bulb fails",
                  "cells": ["<strong>Both go out</strong> — the only path is "
                            "broken",
                            "<strong>The other stays lit</strong> — its path "
                            "is untouched"]},
                 {"head": "Where you meet it",
                  "cells": ["A torch, a set of fairy lights, a dimmer chain, "
                            "a fuse",
                            "Every socket and light in a house, every lamp in "
                            "a car"]},
             ],
         },
         "close": "Series is not a worse circuit — it is a different tool. "
                  "Anything that has to switch or protect a whole loop "
                  "belongs in series with it, which is exactly where a switch "
                  "and a fuse go. Anything that has to work on its own "
                  "belongs in parallel."},

        {"type": "key-fact", "ref": "one-path-or-a-path-each"},

        {"type": "misconception", "id": "think-parallel-shares",
         "anchor": "s-think"},

        {"type": "quiz", "anchor": "s-ladder"},
        {"type": "summary", "id": "s-keynote"},
    ],

    "activities": [
        {"id": "think-parallel-shares",
         "kind": "predict",
         "demand": "explain",
         "targets": "CIRC-05",
         "statements": [
             {"quote": "In parallel the current has to split between the two "
                       "bulbs, so each one is dimmer.",
              "targets": "CIRC-05",
              "body": [
                  "The current does split — but it is not a fixed amount "
                  "being shared out. Each branch decides for itself how much "
                  "it draws, because each branch has the battery's full push "
                  "across it, and one bulb on 3.0 V draws 0.30 A whether or "
                  "not there is another bulb next to it. The battery does not "
                  "ration the current; it supplies whatever the branches ask "
                  "for, which here is 0.60 A. That is why adding lamps in "
                  "parallel makes the battery flatten sooner rather than "
                  "making the lamps dimmer.",
              ]},
             {"quote": "In series the first bulb gets the current first, so "
                       "it is brighter than the second one.",
              "targets": "CIRC-06",
              "body": [
                  "There is no first. The current is the same at every point "
                  "of a single loop, at the same instant, so two identical "
                  "bulbs in series are equally dim and swapping them over "
                  "changes nothing. The charge does not queue up and arrive "
                  "somewhere sooner: it is already spread all the way round, "
                  "and it all starts moving together.",
              ]},
         ]},
    ],

    "figures": [],

    "key_facts": [
        {"id": "one-path-or-a-path-each",
         "eyebrow": "Key fact",
         "ground": "card",
         "placement": "top-level",
         "text": "In series there is one path: one current through "
                 "everything, and a break anywhere stops the lot. In parallel "
                 "there is a path for each branch: every branch gets the "
                 "battery's full push, the battery supplies the branch "
                 "currents added together, and a break in one branch leaves "
                 "the others working."},
    ],

    # ⚠️ MRB-278 · POSITION IS AUTHORED. This lesson takes indices 1 and 3.
    "ladder": {
        "recall": {
            "q": "Three identical lamps are wired in parallel across a 6 V "
                 "battery. Each one on its own draws 0.20 A. What total "
                 "current leaves the battery, and what happens if the middle "
                 "lamp is unscrewed?",
            "options": [
                "0.20 A shared between the three, so about 0.07 A each, and "
                "the other two get brighter",
                "0.60 A, and the other two stay at full brightness",
                "0.60 A, and all three go out",
                "0.20 A, and the other two stay lit",
            ],
            "answer": 1,
            "feedback": {
                0: "Nothing is shared. Each branch has the full 6 V across it "
                   "and draws its own 0.20 A, so the battery supplies 0.60 A. "
                   "Removing one lamp does not change the other two at all.",
                2: "The total is right. But three parallel branches are three "
                   "separate paths, and breaking one leaves the other two "
                   "complete — that is the point of wiring in parallel.",
                3: "The verdict on the other lamps is right and the current "
                   "is not. Three branches each drawing 0.20 A add up at the "
                   "battery to 0.60 A.",
            },
            "title": "Rung 1 · Read the circuit"},
        "apply": {
            "q": "A student adds a second identical bulb in series with the "
                 "first and predicts each bulb will be as bright as before, "
                 "because the battery has not changed. What is wrong?",
            # ⚑ Option B is FINISHED into a complete wrong rule so that the
            # correct answer is no longer a length tell. Her wrong idea and
            # her correction are untouched; the clause after the comma states
            # the rule the wrong idea depends on. See DEPARTURES-P8.md row 1.
            "options": [
                "Nothing is wrong — in series the current is the same "
                "everywhere, so both bulbs must be as bright as the single "
                "bulb was, because a bulb's brightness is set by the current "
                "passing through it and that current has not changed anywhere "
                "in the loop.",
                "The first bulb will be as bright as before and the second "
                "will be dim, because the current reaches the first bulb "
                "first.",
                "The bulbs will be dimmer because the battery has to divide "
                "its charge between two bulbs and each gets half as much.",
                "A second bulb in series makes it harder for the charge to "
                "get round the one loop, so the current everywhere falls — "
                "here from 0.30 A to 0.15 A — and both bulbs are dim.",
            ],
            "answer": 3,
            "feedback": {
                0: "The current is the same at every point of the loop, but "
                   "that shared value is smaller than it was with one bulb. "
                   "Same everywhere does not mean unchanged.",
                1: "There is no first. One loop means one current at every "
                   "point at the same instant, so two identical bulbs are "
                   "equally dim.",
                2: "The verdict is right and the reason is not. Charge is not "
                   "divided up in series — all of it goes through both bulbs. "
                   "What has changed is how hard it is to push, so the flow "
                   "slows down.",
            },
            "title": "Rung 2 · The one that catches people"},
        "explain": {
            "q": "Two identical bulbs are wired in series and then rewired in "
                 "parallel across the same battery. Explain what happens to "
                 "the brightness of each bulb and to the current leaving the "
                 "battery, and why.",
            "field_label": "Your explanation",
            "placeholder": "In series there is one path, so…",
            "success": [
                "Says series is one path and parallel is two paths from the "
                "battery.",
                "Says in series both bulbs share one current, which is "
                "smaller than a single bulb would draw.",
                "Says in parallel each branch has the battery’s full push "
                "across it, so each bulb draws its full current.",
                "Says the current leaving the battery is larger in parallel, "
                "because the branch currents add.",
                "Concludes that both bulbs are dim in series and both are at "
                "full brightness in parallel.",
            ],
            "title": "Rung 3 · Explain"},
        "produce": {
            "q": "A car has two headlamps, two brake lamps and one ignition "
                 "switch that must kill everything. Say how you would wire "
                 "it, and justify each choice by what would happen if you did "
                 "it the other way.",
            "field_label": "Your answer",
            "placeholder": "The headlamps go in parallel because…",
            "success": [
                "Puts the headlamps in parallel with each other, and the "
                "brake lamps in parallel.",
                "Justifies it: one lamp failing must not take the other out, "
                "and each needs the full 12 V to be bright.",
                "Says that in series the lamps would be dim and one failure "
                "would blind the car completely.",
                "Puts the ignition switch in series with the whole set, so it "
                "can break the only shared path.",
                "Says a switch wired in parallel with the lamps would not cut "
                "them off — it would short them out instead.",
            ],
            "title": "Rung 4 · Take it somewhere new"},
    },

    "key_note": "Components in series sit in one loop, so one current passes "
                "through all of them and a break anywhere stops everything. "
                "Components in parallel sit on separate branches of the same "
                "battery: each branch has the battery's full push across it, "
                "the battery supplies the branch currents added together, and "
                "a break in one branch leaves the others working. To tell "
                "which you have, count the paths from one end of the battery "
                "to the other.",

    "stretch": [
        {"id": "cheap-light-strings-are-series",
         "type": "explainer",
         "text": "Cheap decorative light strings are wired in series, and the "
                 "reason is money: in series the supply voltage is shared out "
                 "between all the lamps, so each one can be a tiny "
                 "low-voltage bulb instead of a mains-rated one. The price is "
                 "the failure you know about. Better strings hide a trick — "
                 "each bulb carries a small piece of coated wire called a "
                 "shunt, which does nothing while the filament works and "
                 "conducts once the filament breaks, keeping the loop closed. "
                 "The string stays lit, and the surviving bulbs each get a "
                 "slightly bigger share of the voltage, which is why the "
                 "failures then start to come faster."},
        {"id": "a-house-is-parallel-from-the-meter",
         "type": "explainer",
         "text": "A house is parallel from the meter outwards, and every "
                 "branch runs at the same 230 V. That is what makes "
                 "appliances interchangeable: a kettle designed for 230 V "
                 "works in any socket, in any room, whatever else is switched "
                 "on. It also means the currents add up at the fuse box, "
                 "which is the whole reason a house has fuses and circuit "
                 "breakers at all."},
    ],

    "support": [],

    "vocabulary": [
        {"term": "series",
         "definition": "Components in the same loop, one after another. One "
                       "current goes through all of them."},
        {"term": "parallel",
         "definition": "Components on separate branches of the same supply. "
                       "Each branch gets the whole push and works on its "
                       "own."},
        {"term": "branch",
         "definition": "One of the separate paths in a parallel section, "
                       "between the point where they divide and the point "
                       "where they rejoin."},
    ],

    "tutor": {
        "anchor": "s-bench",
        "prompt": "Ask Mr Badmus AI",
        "body": "Got a circuit diagram and not sure whether it is series or "
                "parallel?",
        "cta": "Ask about this lesson"},

    "ks4_becomes": "Adding resistances in series and in parallel, the rules "
                   "for current and potential difference in each, and why a "
                   "parallel combination resists less than either branch "
                   "alone.",

    "convention_note": "The bench is a teaching model. Both bulbs are treated "
                       "as identical and as having a fixed resistance of 10 "
                       "ohms, so one on 3.0 V draws 0.30 A exactly; a real "
                       "filament's resistance rises as it heats, so two real "
                       "bulbs in series draw somewhat more than a quarter of "
                       "the power of one and the dimming is less extreme than "
                       "the arithmetic suggests. The battery is treated as "
                       "having no resistance of its own, which is why the "
                       "parallel reading doubles cleanly; a real cell sags a "
                       "little under the larger current. An unscrewed bulb is "
                       "drawn as a clean gap.",

    "ws": ["measurement"],
}
