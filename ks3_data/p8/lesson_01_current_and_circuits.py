"""P8 L1 — Current and circuits (MODEL).

Authored against Claude Design's approved page,
`docs/ks3/design-reference/p8/p8-01-current-and-circuits.dc.html`.

Her page wins outright. The torch with the snipped strip, the loop with
three meter sockets, the eight-symbol key and all four rungs are hers.

── ⚖️ MRB-204 · NO FORMULA BLOCK, AND NOT BY OVERSIGHT ───────────────

Nothing on this page is calculated. The charge that flows in a coulomb is
GCSE, `Q = I t` is GCSE, and the one number the bench produces — an
ammeter reading — is read rather than worked out. A block here would be a
relationship invented to fill a slot.

── ⚖️ RULED · THE METER POSITION IS A CONTROL THAT CHANGES NO NUMBER ─

That is the lesson, and it is the one place in the key stage where a dial
with no effect on the readout is the point rather than a defect. Every
branch note names the live reading AND says the other two positions give
the same, because a bench that merely failed to move the number would
teach nothing at all.

── ⚠️ FOUR RAIL STOPS, AND THE THIRD IS THE `Think again` BLOCK ──────

    s-hook · s-loop · s-think · s-ladder

Design's `DONE('s-think', s)` reads `s.gate !== null`, so the
misconception block ticks on the bench's commitment. It is the only
misconception block on a rail in the key stage, and it takes the
`circ-think` family for the reason `ks3_art/p8.py` gives at length: the
section has to carry `data-stage-done="0"` in the BUILT BYTES, and
neither `confrontation` nor `predict` emits one.

⚠️ **THE SYMBOL KEY TAKES NO ANCHOR.** Design's own section carries no
`id`, and her `RAIL` is four entries with the figure not among them.

── ⚖️ FOUR MISCONCEPTIONS ────────────────────────────────────────────

    CIRC-01  the bulb uses up the current               (hers, §7)
    CIRC-02  the electricity has to travel to the bulb  (hers, §7)
    CIRC-03  a circuit only has to reach the bulb       (from the hook)
    CIRC-04  the cell stores current and sends it out   (from rung 2 D)

── ⚠️ POSITION IS AUTHORED. This lesson takes indices 2 and 0.
"""

LESSON = {
    "slug":  "current-and-circuits",
    "title": "Current and circuits",
    "discipline": "physics",
    "unit": "Electric circuits",
    "family": "MODEL",

    "covers": ["KS3.P.CUR.01a"],
    "touches": [],
    "beyond_statutory": False,
    "threads": [{"id": "electricity", "level": 1}],
    "typical_year": 8,
    "typical_minutes": 60,

    "requires": [],
    "assumes": [],
    "references": ["current-at-a-junction",
                   "building-and-measuring-a-circuit"],
    "ks4_links": [],

    "meta_description": "Put an ammeter in front of a bulb and behind it. "
                        "Both read exactly the same. Whatever the bulb is "
                        "doing, it is not using up the thing that flows.",

    "big_question": "Put an ammeter in front of the bulb and behind it. Both "
                    "read exactly the same. Whatever the bulb is doing, it is "
                    "not using up the thing that flows.",

    "rail": [
        {"anchor": "s-hook",   "short": "TORCH",
         "label": "Snip the wire",     "done_when": "committed"},
        {"anchor": "s-loop",   "short": "BENCH",
         "label": "Move the meter",    "done_when": "gate_and_a_control"},
        {"anchor": "s-think",  "short": "THINK",
         "label": "Nothing is used up", "done_when": "gate_committed"},
        {"anchor": "s-ladder", "short": "LADDER",
         "label": "Mastery ladder",    "done_when": "ladder_complete"},
    ],

    "phenomenon": {
        "kind": "narrative",
        "title": "Snip the wire anywhere. The bulb goes out.",
        "prompt": "A torch has a cell, a bulb and two strips of metal joining "
                  "them into a ring. Cut the ring on the way to the bulb and "
                  "it goes dark. Cut it on the way back from the bulb and it "
                  "goes dark just the same.",
        "commit": "Why does a gap on the far side of the bulb matter, when "
                  "the electricity has already been past it?",
        "options": [
            "A current is a flow all the way round the ring, so a gap "
            "anywhere stops the whole flow at once",
            "The electricity has to reach the bulb, and a gap on the return "
            "side stops the next lot arriving",
            "The cell can only push electricity out of one end, and a gap "
            "lets it leak away",
            "The bulb needs somewhere to send the used-up electricity, and "
            "the gap blocks it",
        ],
        "answer": 0,
        "reveal": "A current is a flow round a ring, not a delivery from one "
                  "place to another. The wire is already full of free "
                  "electrons before you switch anything on, and the cell "
                  "pushes on all of them together. Open a gap and there is "
                  "nowhere for the charge to go and nothing to take its "
                  "place, so the whole ring stops — both sides of the bulb, "
                  "instantly.",
    },

    "misconceptions": [
        {"id": "CIRC-01",
         "statement": "The bulb uses up the current, so there is less of it "
                      "coming back than going in.",
         "elicited_by": "loop",
         "confronted_by": "loop"},
        {"id": "CIRC-02",
         "statement": "The electricity has to get from the cell to the "
                      "bulb, which is why there is a tiny delay when you "
                      "flick the switch.",
         "elicited_by": "s-hook",
         "confronted_by": "s-think"},
        {"id": "CIRC-03",
         "statement": "A circuit only has to reach the bulb; what happens on "
                      "the way back does not matter.",
         "elicited_by": "s-hook",
         "confronted_by": "loop"},
        {"id": "CIRC-04",
         "statement": "A cell holds a store of current and sends it out into "
                      "the wire.",
         "elicited_by": "s-ladder",
         "confronted_by": "s-think"},
    ],

    "core": [
        {"type": "hook", "id": "hook-commit", "anchor": "s-hook"},

        {"type": "explainer",
         "text": "Every metal is full of <strong>electrons</strong> that are "
                 "free to move. They are already there, spread all the way "
                 "round the wire, before anything is switched on. A cell does "
                 "not fill the wire with them; it pushes on the ones already "
                 "in it. When they all shuffle along together in the same "
                 "direction you have an <strong>electric current</strong>: a "
                 "flow of charge."},
        {"type": "explainer",
         "text": "Because the flow has to be a flow all the way round, a "
                 "circuit must be a <strong>complete loop</strong>. Break it "
                 "anywhere and everything stops everywhere, instantly — there "
                 "is nowhere for the charge to go and nothing to take its "
                 "place. That is why a gap behind the bulb is as fatal as a "
                 "gap in front of it."},
        {"type": "explainer",
         "text": "Current is measured in <strong>amperes</strong>, shortened "
                 "to <strong>amps</strong> and written <strong>A</strong>. "
                 "You measure it with an <strong>ammeter</strong>, which goes "
                 "<em>in</em> the loop so the current runs through it. One "
                 "amp is a big current for a classroom circuit; a torch bulb "
                 "usually draws a few tenths of an amp, so readings like 0.30 "
                 "A are normal."},

        # ── #s-loop · one loop, one meter, three places to put it ───────
        {"type": "circuit-loop",
         "id": "loop",
         "anchor": "s-loop",
         "eyebrow": "At the bench · one loop, one meter, three places to put "
                    "it",
         "heading": "Move the meter. Watch the reading.",
         # A MAP, NOT A STRING. `progress` authored as a string is
         # read as a COUNT FORMAT (MRB-248's widening), and these
         # are two named states rather than a tally.
         "progress": {"idle": "Change a control to begin",
                      "live": "Three controls live"},
         "lead": "One cell holder, one bulb, one switch and one ammeter. The "
                 "meter can go in three places round the loop. Add cells, "
                 "open and close the switch, and move the meter.",
         "volts_per_cell": 1.5,
         "amps_per_cell": 0.15,
         "start_cells": 1,
         "start_closed": True,
         "start_slot": 0,
         # ⊕ Design's `DONE('s-think', s)` is `s.gate !== null`, so the
         # confrontation ticks on the commitment alone while this bench
         # also wants a control touched.
         "band_anchor": "s-think",
         "band_at": 1,
         "gate": {
             "prompt": "Commit first. The meter sits between the switch and "
                       "the bulb and reads 0.30 A. You move it to the far "
                       "side of the bulb, on the way back to the cell. What "
                       "does it read there?",
             "options": [
                 "Less than 0.30 A, because some of the current has been used "
                 "up in the bulb",
                 "Exactly 0.30 A, because the current is the same all the way "
                 "round one loop",
                 "Zero, because everything that flowed has already been spent",
                 "More than 0.30 A, because the bulb has given the flow a "
                 "push",
             ],
             "answer": 1,
         },
         "cells": {"label": "Cells in the holder", "max": 4, "start": 1,
                   "one_label": "1 cell", "many_label": "%d cells"},
         "switch_label": "The switch",
         "closed_label": "Closed",
         "open_label": "Open",
         "slot_label": "Where the ammeter goes",
         "cells_label_svg": "CELLS",
         "switch_label_svg": "SWITCH",
         "bulb_label_svg": "BULB",
         # Design's own three sockets, with her viewBox coordinates and her
         # overlay percentages.
         "slots": [
             {"id": "between", "label": "Between switch and bulb",
              "x": 650, "y": 100, "caption": "on the way to the bulb",
              "name": "between the switch and the bulb", "lx": 65, "ly": 4},
             {"id": "after", "label": "After the bulb",
              "x": 650, "y": 300, "caption": "on the way back from the bulb",
              "name": "on the far side of the bulb", "lx": 65, "ly": 90},
             {"id": "beside", "label": "Next to the cells",
              "x": 300, "y": 300, "caption": "right beside the cells",
              "name": "right beside the cells", "lx": 30, "ly": 90},
         ],
         "readouts": [
             {"id": "volts", "label": "The cells push with", "sub": "—"},
             {"id": "loop", "label": "The loop is", "sub": "—", "word": True},
             {"id": "reading", "label": "The ammeter reads", "sub": "—"},
             {"id": "bright", "label": "The bulb is", "word": True},
         ],
         "branches": {
             "open": "The switch is open, so the loop is not a loop. Every "
                     "one of the three meter positions reads 0.00 A — not a "
                     "small current, none at all — and the bulb is dark. A "
                     "gap at the switch is no different from a gap anywhere "
                     "else: the flow needs the whole ring.",
             "one": "One cell, 1.5 V, and the meter {name} reads {reading}. "
                    "Move it to either of the other two positions and it "
                    "reads {reading} there as well. The bulb is dim because "
                    "one cell gives the smallest push this bench offers, but "
                    "whatever it is doing to the charge it is not reducing "
                    "how much of it goes past.",
             "many": "With {n} cells the push is {volts} and the meter {name} "
                     "reads {reading}. That is {n} times the reading with one "
                     "cell, and it is the same reading at all three positions "
                     "— in front of the bulb, behind it, and beside the "
                     "cells. More push means a faster flow everywhere at "
                     "once, never a bigger flow on one side than the other.",
         }},

        # ── the symbol key · no anchor, because Design's section has none ──
        {"type": "circ-band",
         "id": "symbol-key",
         "eyebrow": "The figure",
         "heading": "The symbols a circuit diagram is written in",
         "lead": "A circuit diagram is not a drawing of the apparatus. It is "
                 "a set of agreed symbols joined by straight lines, so that "
                 "anyone anywhere can build the same circuit from the same "
                 "picture. These eight cover almost everything in this unit.",
         "symbols": [
             {"id": "cell", "label": "Cell", "note": "long line is +",
              "aria_label": "Cell symbol: one long line and one short line.",
              "paths": [{"d": "M10 40 H78 M102 40 H170", "w": 5},
                        {"d": "M78 14 V66", "w": 6},
                        {"d": "M102 26 V54", "w": 6}]},
             {"id": "battery", "label": "Battery",
              "note": "two or more cells",
              "aria_label": "Battery symbol: two cells in a row.",
              "paths": [{"d": "M6 40 H58 M82 40 H98 M122 40 H174", "w": 5},
                        {"d": "M58 14 V66 M98 14 V66", "w": 6},
                        {"d": "M82 26 V54 M122 26 V54", "w": 6}]},
             {"id": "lamp", "label": "Lamp", "note": "a bulb",
              "aria_label": "Lamp symbol: a circle with a cross inside it.",
              "paths": [{"d": "M10 40 H62 M118 40 H170", "w": 5},
                        {"d": "M70 20 L110 60 M110 20 L70 60", "w": 5}],
              "circles": [{"cx": 90, "cy": 40, "r": 28, "w": 5}]},
             {"id": "switch", "label": "Switch", "note": "drawn open",
              "aria_label": "Open switch symbol: two contacts with a lever "
                            "lifted away from one of them.",
              "paths": [{"d": "M10 52 H62 M118 52 H170", "w": 5},
                        {"d": "M62 52 L114 22", "w": 5}],
              "circles": [{"cx": 62, "cy": 52, "r": 6, "w": 0},
                          {"cx": 118, "cy": 52, "r": 6, "w": 0}]},
             {"id": "ammeter", "label": "Ammeter", "note": "goes in the loop",
              "aria_label": "Ammeter symbol: a circle with the letter A "
                            "inside it.",
              "paths": [{"d": "M10 40 H62 M118 40 H170", "w": 5}],
              "circles": [{"cx": 90, "cy": 40, "r": 28, "w": 5}],
              "letter": "A"},
             {"id": "voltmeter", "label": "Voltmeter",
              "note": "goes across a part",
              "aria_label": "Voltmeter symbol: a circle with the letter V "
                            "inside it.",
              "paths": [{"d": "M10 40 H62 M118 40 H170", "w": 5}],
              "circles": [{"cx": 90, "cy": 40, "r": 28, "w": 5}],
              "letter": "V"},
             {"id": "resistor", "label": "Resistor", "note": "a fixed value",
              "aria_label": "Resistor symbol: a plain rectangle in the wire.",
              "paths": [{"d": "M10 40 H54 M126 40 H170", "w": 5}],
              "rects": [{"x": 54, "y": 22, "w": 72, "h": 36, "rx": 4,
                         "sw": 5}]},
             {"id": "vres", "label": "Variable resistor",
              "note": "you can turn it up",
              "aria_label": "Variable resistor symbol: a rectangle in the "
                            "wire with a sloping arrow drawn across it.",
              "paths": [{"d": "M10 48 H54 M126 48 H170", "w": 5},
                        {"d": "M48 62 L136 18 M136 18 L118 18 M136 18 V36",
                         "w": 5}],
              "rects": [{"x": 54, "y": 30, "w": 72, "h": 36, "rx": 4,
                         "sw": 5}]},
         ],
         "close": "Two of these already tell you something. An "
                  "<strong>ammeter</strong> is drawn in the line, so the "
                  "current goes through it. A <strong>voltmeter</strong> is "
                  "drawn as a loop off to one side, across a component, "
                  "because it is not measuring a flow at all."},

        {"type": "key-fact", "ref": "current-is-a-flow-of-charge"},

        # ── #s-think · the one confrontation on a P8 rail ───────────────
        {"type": "circ-think",
         "id": "think-nothing-used-up",
         "anchor": "s-think",
         "demand": "explain",
         "quotes": [
             {"quote": "The bulb uses up the current, so there is less of it "
                       "coming back than going in.",
              "body": [
                  "Two ammeters, one either side of the bulb, read the same "
                  "to the last digit. Nothing is consumed. What the bulb "
                  "takes is <em>energy</em>, which is carried by the moving "
                  "charge and left behind as light and heat, and energy is "
                  "not the same thing as the charge doing the carrying. "
                  "Think of a bicycle chain: the chain is not used up by the "
                  "back wheel, but it does deliver something on every turn.",
              ]},
             {"quote": "The electricity has to get from the cell to the bulb, "
                       "which is why there is a tiny delay when you flick the "
                       "switch.",
              "body": [
                  "The electrons were already there, all the way round, "
                  "standing in the wire like water in a full pipe. Closing "
                  "the switch pushes on all of them at once, so the far end "
                  "starts moving almost the instant the near end does. The "
                  "individual electrons drift astonishingly slowly — well "
                  "under a millimetre a second in a lamp wire — while the "
                  "push that sets them going travels at close to the speed "
                  "of light.",
              ]},
         ]},

        {"type": "quiz", "anchor": "s-ladder"},
        {"type": "summary", "id": "s-keynote"},
    ],

    "activities": [],

    "figures": [],

    "key_facts": [
        {"id": "current-is-a-flow-of-charge",
         "eyebrow": "Key fact",
         "ground": "card",
         "placement": "top-level",
         "text": "An electric current is a flow of charge — electrons already "
                 "in the metal, all drifting the same way. It needs a "
                 "complete loop, and in a single loop it is the same size "
                 "everywhere. It is measured in amperes (A) on an ammeter, "
                 "which is placed in the loop."},
    ],

    # ⚠️ MRB-278 · POSITION IS AUTHORED. This lesson takes indices 2 and 0.
    # Design's own order puts BOTH correct answers at index 0; her options
    # and her corrections are verbatim and only the ORDER moved.
    "ladder": {
        "recall": {
            "q": "A single loop holds a cell, a switch, a bulb and two "
                 "ammeters, one either side of the bulb. The first reads "
                 "0.24 A. What does the second read?",
            "options": [
                "0.12 A — the bulb uses up about half of it",
                "0 A — the current has already been spent on the bulb",
                "0.24 A — the current is the same everywhere in a single loop",
                "0.48 A — the bulb pushes the current on and it speeds up",
            ],
            "answer": 2,
            "feedback": {
                0: "Nothing is used up. The bulb takes energy from the charge "
                   "going through it, and energy is not the same thing as "
                   "the charge. Both meters read 0.24 A.",
                1: "If no charge came back the loop would not be a loop, and "
                   "the bulb could not stay lit for a second. The flow is a "
                   "full ring.",
                3: "A bulb adds nothing. It resists the flow, and what it "
                   "resists it resists equally on both sides: one loop, one "
                   "current.",
            },
            "title": "Rung 1 · Read the meters"},
        "apply": {
            "q": "A student wires a lamp on a very long cable, then says the "
                 "light will come on a moment late because the electricity "
                 "has to travel down the wire first. What is wrong with that?",
            "options": [
                "The wire is already full of free electrons, so closing the "
                "switch pushes on all of them at once and the far end starts "
                "moving almost immediately.",
                "Nothing is wrong — there is a delay, but it is too small to "
                "notice because electricity travels at the speed of light.",
                "The student is right, and on a cable a few kilometres long "
                "you would see the lamp light up noticeably late.",
                "There is no delay because a cell does not send electrons out "
                "— it makes new ones in the wire as they are needed.",
            ],
            "answer": 0,
            "feedback": {
                1: "The push does travel at close to the speed of light, but "
                   "the electrons do not: they drift under a millimetre a "
                   "second. The reason there is no delay is that they were "
                   "already there.",
                2: "You would not. The wire is full before you start, so "
                   "nothing has to make the journey before the lamp can "
                   "light.",
                3: "The verdict is right and the reason is not. No electrons "
                   "are made or destroyed; a cell pushes the ones the metal "
                   "already has.",
            },
            "title": "Rung 2 · The one that catches people"},
        "explain": {
            "q": "A torch bulb goes out when the metal strip behind it is "
                 "broken, even though the current has already been through "
                 "the bulb. Explain why, using the words current, charge and "
                 "loop.",
            "field_label": "Your explanation",
            "placeholder": "A current is a flow of…",
            "success": [
                "Says a current is a flow of charge, carried by electrons "
                "already in the metal.",
                "Says the circuit has to be a complete loop for anything to "
                "flow.",
                "Says a gap means there is nowhere for the charge to go and "
                "nothing to replace it.",
                "Says the whole loop stops, not just the part after the gap.",
                "Says the position of the gap makes no difference — in front "
                "of the bulb or behind it, the bulb goes out.",
            ],
            "title": "Rung 3 · Explain"},
        "produce": {
            "q": "A string of forty fairy lights is wired as one loop. One "
                 "bulb fails and the whole string goes dark, and you cannot "
                 "tell which bulb it was. Explain why the string fails like "
                 "this, and describe how you would find the dead bulb with an "
                 "ammeter, a cell and some wire.",
            "field_label": "Your answer",
            "placeholder": "All forty are in one loop, so…",
            "success": [
                "Says all forty bulbs are in the same single loop.",
                "Says a broken filament is a gap in that loop, so the current "
                "stops everywhere.",
                "Says every bulb goes out at once, which is why the fault "
                "gives no clue about its position.",
                "Describes testing bulbs one at a time in a small test loop "
                "with the cell and the ammeter.",
                "Says the dead bulb is the one that gives a reading of zero "
                "when the others read a current.",
            ],
            "title": "Rung 4 · Take it somewhere new"},
    },

    "key_note": "An electric current is a flow of charge: the free electrons "
                "already present in a metal, all drifting the same way when a "
                "cell pushes on them. A current only flows in a complete "
                "loop, so a gap anywhere stops it everywhere. In a single "
                "loop the current is the same size at every point — an "
                "ammeter reads the same before and after a bulb — because "
                "charge is not used up. Energy is. Current is measured in "
                "amperes (A), and an ammeter is placed in the loop so the "
                "current runs through it.",

    "stretch": [
        {"id": "the-unit-is-named-after-ampere",
         "type": "explainer",
         "text": "The unit is named after André-Marie Ampère, and one amp is "
                 "defined as one coulomb of charge going past each second. A "
                 "coulomb is a strange quantity to picture: it is the charge "
                 "on about six million million million electrons. So an "
                 "ordinary 0.30 A torch bulb has roughly two million million "
                 "million electrons going past the filament every second — "
                 "which is why nobody counts them and everybody uses amps."},
        {"id": "the-electrons-themselves-crawl",
         "type": "explainer",
         "text": "The electrons themselves crawl. In a lamp flex carrying an "
                 "ordinary current they drift at well under a millimetre per "
                 "second, so an electron leaving the plug would take hours to "
                 "reach the bulb. Nothing waits for it. The wire is already "
                 "full, and the push travels through the standing electrons "
                 "at a large fraction of the speed of light, which is why a "
                 "light comes on the instant the switch closes even on a long "
                 "cable."},
    ],

    "support": [],

    "vocabulary": [
        {"term": "electric current",
         "definition": "A flow of charge. In a metal it is the free electrons "
                       "already in the wire, all drifting the same way."},
        {"term": "circuit",
         "definition": "A complete loop for the charge to go round. Break it "
                       "anywhere and everything stops everywhere."},
        {"term": "ampere",
         "definition": "The unit of current, shortened to amp and written A. "
                       "A torch bulb draws a few tenths of one."},
        {"term": "ammeter",
         "definition": "The instrument that measures current. It goes IN the "
                       "loop, so the current runs through it."},
    ],

    "tutor": {
        "anchor": "s-loop",
        "prompt": "Ask Mr Badmus AI",
        "body": "Not sure why an ammeter goes in the loop and a voltmeter "
                "goes across?",
        "cta": "Ask about this lesson"},

    "ks4_becomes": "Charge flow = current × time, the coulomb as a unit, and "
                   "the difference between conventional current and the "
                   "direction the electrons actually move.",

    "convention_note": "The bench is a teaching model. Each cell is taken as "
                       "1.5 V and the bulb's current is drawn as a straight "
                       "multiple of the number of cells; in a real filament "
                       "lamp the resistance rises as it heats, so doubling "
                       "the cells gives somewhat less than double the "
                       "current. The readings are rounded to two decimal "
                       "places, and the meter itself is treated as having no "
                       "resistance of its own. Conventional current is drawn "
                       "from + to − by long-standing convention; the "
                       "electrons in a metal drift the other way.",

    "ws": ["measurement"],
}
