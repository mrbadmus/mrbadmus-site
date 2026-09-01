"""P8 L6 — Conductors and insulators (CLASSIFY).

Authored against Claude Design's approved page,
`docs/ks3/design-reference/p8/p8-06-conductors-and-insulators.dc.html`.

Her page wins outright. The cable with copper inside and plastic outside,
the test gap, the fourteen-decade chart, the triangle, both worked
examples, both attempts, all four rungs and the safeguarding block are
hers.

── ⚖️ MRB-204 · A TRIANGLE, RULED IN AGAINST HER OWN NOTES ───────────

⊕ Mide, 21 Aug 2026, on Design's FLAG 3. Her notes ask whether a page
that computes on every state must carry a block, and warn that the answer
means a second `R = V ÷ I` triangle three slots after `p8-05`'s. **The
answer is yes, and the duplication is ruled closed.** Repetition is the
feature here: this bench divides 6.0 V by an ammeter reading in five
different unit prefixes, and a student doing that without the shape in
front of them is doing arithmetic rather than physics.

⚠️ **HER DELIVERED PAGE HAD ALREADY DRAWN IT.** `#s-formula` — the
triangle, both worked examples and both attempts — is on the page;
`NOTES-P8-P9.md` §3 still lists the lesson as *no block*. The note is
older than the drawing. Recorded in `DEPARTURES-P8.md` as a
notes-vs-drawing contradiction, resolved by measuring the drawing.

⚠️ **`#s-formula` TAKES NO RAIL STOP.** Her `RAIL` is four entries —
`s-hook s-test s-scale s-ladder` — and the formula section is not among
them. Four stops, exactly as ruled.

── ⚖️ RULED · THE COPPER STATE PRINTS NO CURRENT ─────────────────────

⊕ Mide, 21 Aug 2026, on Design's FLAG 7. 6.0 V ÷ 0.05 Ω is 120 A, and
that is a division result rather than a reading: no school supply
delivers it, because the supply's own internal resistance is what limits
the current there. So the RESISTANCE readout keeps its real value and the
CURRENT readout reads *limited by the supply, not by the wire*. The
branch note, the chart and the legal line follow, and nothing on the page
says 120 A or implies the wire carried it.

⚠️ **THE COPPER BAR STILL DRAWS.** It is the reference every other
specimen is measured against, and a blank row would be worse than the
division was. Her own note says so.

⚠️ **HER DELIVERED PAGE HAD ALREADY DRAWN THIS TOO**, down to the
sentence in the tile and the disclosure in the legal line. Second
notes-vs-drawing contradiction; same resolution.

── ⚖️ SAFEGUARDING · THIS PAGE AND NO OTHER IN THE UNIT ──────────────

The lesson ends on why a cable is copper inside and plastic outside, and
mains cables and sockets at home are where that stops being an
abstraction. Her words go into the engine's `safeguarding_note` slot,
which §8.10 rules as one quiet foot line above the legal line rather than
a callout. `p8-07` carries none — practical safety on cells and a lamp,
no body at risk — and lab safety is not safeguarding.

── ⚠️ FOUR RAIL STOPS ───────────────────────────────────────────────

    s-hook · s-test · s-scale · s-ladder

⚠️ `s-scale` takes `gate !== null` while the bench also wants a control
touched, so the bench marks it through `band_anchor` / `band_at`.

── ⚖️ FOUR MISCONCEPTIONS ───────────────────────────────────────────

    CIRC-21  an insulator blocks current completely       (hers, §7)
    CIRC-22  materials are either conductors or insulators (hers, §7)
    CIRC-23  plastic has no charged particles in it at all (from rung 2 D)
    CIRC-24  a short enough piece of an insulator conducts (from the gate)

── ⚠️ POSITION IS AUTHORED. This lesson takes indices 1 and 3.
"""

LESSON = {
    "slug":  "conductors-and-insulators",
    "title": "Conductors and insulators",
    "discipline": "physics",
    "unit": "Electric circuits",
    "family": "CLASSIFY",

    "covers": ["KS3.P.CUR.03"],
    "touches": ["KS3.WS.ANA.01"],
    "beyond_statutory": False,
    "threads": [{"id": "electricity", "level": 3}],
    "typical_year": 8,
    "typical_minutes": 60,

    "requires": ["resistance"],
    "assumes": [],
    "references": ["current-and-circuits"],
    "ks4_links": [],

    "meta_description": "Conductor and insulator are not two kinds of thing. "
                        "They are the two ends of one number, and that number "
                        "runs across more than a million million.",

    "big_question": "Conductor and insulator are not two kinds of thing. They "
                    "are the two ends of one number, and that number runs "
                    "across more than a million million.",

    "rail": [
        {"anchor": "s-hook",   "short": "CABLE",
         "label": "One cable, two materials", "done_when": "committed"},
        {"anchor": "s-test",   "short": "BENCH",
         "label": "Clip a specimen in",   "done_when": "gate_and_a_control"},
        {"anchor": "s-scale",  "short": "SCALE",
         "label": "Fourteen zeros",       "done_when": "gate_committed"},
        {"anchor": "s-ladder", "short": "LADDER",
         "label": "Mastery ladder",       "done_when": "ladder_complete"},
    ],

    "phenomenon": {
        "kind": "narrative",
        "title": "One cable. Copper inside, plastic outside.",
        "prompt": "A lamp flex is a copper core in a plastic sheath, and the "
                  "two materials are touching along its whole length. Charge "
                  "pours down the copper and none of it comes out sideways "
                  "through a millimetre of plastic.",
        "commit": "Roughly how many times more does the plastic resist than "
                  "the copper?",
        # ⚑ Option C is FINISHED into a complete wrong comparison so that the
        # correct answer is no longer the longest by ratio. It names a real
        # near-miss — copper against tap water IS about a million — which is
        # exactly what a student reaching for it has in mind.
        # See DEPARTURES-P8.md row 1.
        "options": [
            "About ten times — one metal against another",
            "About a thousand times — a wire against a resistor",
            "About a million times — a metal against tap water",
            "More than a million million times",
        ],
        "answer": 3,
        "reveal": "More than a million million. A short piece of copper is a "
                  "few hundredths of an ohm; the same size of plastic is "
                  "thousands of billions of ohms. Nothing else in school "
                  "physics has a range like it, and that is what makes a "
                  "cable possible: two materials touching, one of them an "
                  "open road and the other so hard to cross that the "
                  "difference is not even worth measuring.",
    },

    "misconceptions": [
        {"id": "CIRC-21",
         "statement": "An insulator blocks electricity completely — "
                      "absolutely nothing gets through.",
         "elicited_by": "test",
         "confronted_by": "test"},
        {"id": "CIRC-22",
         "statement": "Materials are either conductors or insulators, with "
                      "nothing between.",
         "elicited_by": "s-hook",
         "confronted_by": "s-scale"},
        {"id": "CIRC-23",
         "statement": "Plastic insulates because it has no charged particles "
                      "in it at all.",
         "elicited_by": "s-ladder",
         "confronted_by": "s-ladder"},
        {"id": "CIRC-24",
         "statement": "A short enough piece of an insulator would conduct "
                      "properly.",
         "elicited_by": "test",
         "confronted_by": "test"},
    ],

    "core": [
        {"type": "hook", "id": "hook-commit", "anchor": "s-hook"},

        {"type": "explainer",
         "text": "A <strong>conductor</strong> is a material with charges "
                 "free to move. In a metal those are the loose electrons "
                 "every metal atom contributes to a shared pool; in salt "
                 "water they are dissolved ions. An <strong>insulator"
                 "</strong> has none free: every electron is locked into a "
                 "bond, so there is nothing available to drift."},
        {"type": "explainer",
         "text": "Because the difference is a matter of how many charges are "
                 "free and how easily they move, it comes out as a difference "
                 "in <strong>resistance</strong> — and the gap is not a small "
                 "one. A metre of copper is a fraction of an ohm. A metre of "
                 "dry wood is millions of ohms. A plastic ruler is millions "
                 "of millions. Written out, the range covers more than "
                 "fourteen zeros, which is why no single scale on a meter can "
                 "show both ends."},
        {"type": "explainer",
         "text": "There is no boundary line. Materials fill in the whole "
                 "range: graphite conducts but poorly, salt water conducts "
                 "but worse than any metal, tap water conducts far worse than "
                 "salt water, damp wood conducts far better than dry wood. "
                 "\"Insulator\" is a practical judgement — the current it "
                 "lets through is too small to matter for the job — not a "
                 "switch that is off."},

        # ── #s-test · a test gap on a fixed 6.0 V supply ───────────────
        {"type": "test-gap",
         "id": "test",
         "anchor": "s-test",
         "eyebrow": "At the bench · a test gap on a 6.0 V supply",
         "heading": "Clip a specimen in and divide.",
         # A MAP, NOT A STRING. `progress` authored as a string is
         # read as a COUNT FORMAT (MRB-248's widening), and these
         # are two named states rather than a tally.
         "progress": {"idle": "Change a control to begin",
                      "live": "Both controls live"},
         "lead": "Two crocodile clips, a supply fixed at 6.0 V and an ammeter "
                 "that can read from hundreds of amps down to millionths of a "
                 "millionth. Change the specimen, and change how long a piece "
                 "of it you clip in.",
         "volts": 6.0,
         "copper_ohms": 0.05,
         "good_below": 100,
         "poor_below": 100000,
         "start_spec": 2,
         "start_len": 0,
         "band_anchor": "s-scale",
         "band_at": 1,
         "supply_label_svg": "6.0 V FIXED",
         "gap_label": "THE TEST GAP",
         "spec_label": "The specimen in the gap",
         "len_label": "How much of it",
         # ⚖️ RULED 21 Aug 2026 — the copper state prints no current.
         "short_circuit": "copper",
         "short_reading": "limited by the supply, not by the wire",
         "short_sub": "a bare wire across a supply is a short circuit",
         "short_div": "the reference value for copper",
         "short_mark": "SUPPLY-LIMITED",
         # ⚠️ HER OWN SENTENCE, and it says "copper" rather than the
         # specimen's label. `{len}` is the only hole in it.
         "short_head": "Your gap holds {len} of copper, and the ammeter has "
                       "no reading to give here. Clip in another specimen at "
                       "the bench and these five steps will follow it.",
         "gate": {
             "prompt": "Commit first. A plastic ruler is clipped into the gap "
                       "on 6.0 V. What does the ammeter read?",
             # ⚑ Option D is FINISHED into a complete wrong rule so that the
             # correct answer is no longer a length tell. See DEPARTURES-P8.md.
             "options": [
                 "Exactly zero — plastic conducts no current at all",
                 "A few millionths of a millionth of an amp — real, but far "
                 "below what the meter can show",
                 "A few milliamps — small, but enough to feel",
                 "It depends on the length — a short enough piece of plastic "
                 "would conduct properly, because resistance is only ever "
                 "about how far the charge has to go",
             ],
             "answer": 1,
         },
         # ⊕ MRB-297 / P8-07, RULED 30 Aug 2026 — `use` IS PER SPECIMEN.
         # The conductor-band note used to end on one fixed clause, "which
         # is why it is used where you want heat rather than where you want
         # a wire", and that clause is NICHROME'S. It was printing verbatim
         # under a pencil, telling a Year 8 that graphite is a heating
         # element, in the lesson whose method is that the difference is
         # measured rather than declared. Every specimen now carries its
         # own closing sentence and the note fills `{use}` from it.
         "specimens": [
             {"id": "copper", "label": "Copper wire", "name": "COPPER WIRE",
              "ohms": 0.05, "carriers": "loose electrons, in huge numbers",
              "use": "That is why every connecting lead in the lab is made "
                     "of it."},
             {"id": "nichrome", "label": "Nichrome wire",
              "name": "NICHROME WIRE", "ohms": 1.1,
              "carriers": "loose electrons, harder going",
              "use": "That is why it is used where you want heat rather "
                     "than where you want a wire."},
             {"id": "pencil", "label": "Pencil lead",
              "name": "PENCIL LEAD (GRAPHITE)", "ohms": 30,
              "carriers": "electrons free along the carbon sheets",
              "use": "Graphite conducts along its carbon sheets, which is "
                     "why a pencil line carries a current at all, and why "
                     "graphite is used for brushes and electrodes rather "
                     "than for wiring."},
             {"id": "salt", "label": "Salt water", "name": "SALT WATER",
              "ohms": 400, "carriers": "dissolved ions, not electrons",
              "use": "That is why sea water conducts and distilled water "
                     "barely does."},
             {"id": "tap", "label": "Tap water", "name": "TAP WATER",
              "ohms": 40000, "carriers": "a few dissolved ions only",
              "use": "That is why wet hands make an electric shock far "
                     "worse."},
             {"id": "wood", "label": "Dry wood", "name": "DRY WOOD",
              "ohms": 5000000,
              "carriers": "almost nothing free to move",
              "use": "That is why dry wood is treated as safe and damp wood "
                     "is not."},
             {"id": "plastic", "label": "Plastic ruler",
              "name": "PLASTIC RULER", "ohms": 2000000000000,
              "carriers": "every electron locked in a bond",
              "use": "That is why it is wrapped round the copper in every "
                     "cable."},
         ],
         "lengths": [
             {"label": "10 cm of it", "mult": 1, "word": "10 cm"},
             {"label": "100 cm of it", "mult": 10, "word": "100 cm"},
         ],
         "readouts": [
             {"id": "i", "label": "The ammeter reads", "sub": "—",
              "alt": "limited by the supply, not by the wire"},
             {"id": "r", "label": "So the resistance is", "sub": "—"},
             {"id": "verdict", "label": "Which makes it", "sub": "—",
              "word": True},
             {"id": "ratio", "label": "Compared with copper"},
         ],
         "branches": {
             "short":
                 "{len} of copper measures {r}, the lowest resistance on the "
                 "chart and the value every other specimen here is compared "
                 "against. The ammeter is left without a reading on purpose: "
                 "a bare metal wire straight across a supply is a short "
                 "circuit, and what flows then is set by how much the supply "
                 "itself can deliver, not by the wire. Clip in any other "
                 "specimen and the wire is the thing that decides, so the "
                 "meter has something to say.",
             # ⊕ MRB-297 / P8-07 — `{lamp}` IS DERIVED FROM THE CURRENT AND
             # `{use}` FROM THE SPECIMEN. This note used to be one fixed
             # template over three specimens and was false about two of
             # them: 10 cm of nichrome passes 5.5 A here and was called
             # "enough to light a lamp comfortably" (eighteen times this
             # unit's own torch-lamp current, and 33 W in 10 cm of thin
             # wire), and the pencil carried nichrome's heating-element
             # clause. `p8Lamp` in `shared/ks3.js` fills `{lamp}`.
             "good":
                 "{len} of {name} measures {r} and passes {i} at 6.0 V — "
                 "{lamp}. It resists {times} than 10 cm of copper. {use}",
             "poor":
                 "{len} of {name} measures {r} and passes {i} at 6.0 V. The "
                 "meter can see it, so this is genuinely conducting — but "
                 "{times} than copper, so nothing in a circuit would work "
                 "through it. The charges are there and there are not many of "
                 "them: {carriers}.",
             "ins":
                 "{len} of {name} measures about {r} and passes {i} at 6.0 V. "
                 "That is not nothing, and it is not something either — no "
                 "school meter would show it, which is precisely what earns "
                 "the word insulator. It resists {times} than the same length "
                 "of copper, because {carriers}.",
             "longer":
                 " Ten times the length gives ten times the resistance, which "
                 "is the tenfold drop in the current you can see against the "
                 "shorter piece.",
         }},

        # ── #s-scale · fourteen zeros on one axis ──────────────────────
        {"type": "circ-band",
         "id": "fourteen-zeros",
         "anchor": "s-scale",
         "eyebrow": "The figure",
         "heading": "Fourteen zeros, one axis",
         "lead": "The same seven specimens, all 10 cm long, on an axis where "
                 "every mark is a thousand times the one before it. A ruler "
                 "scale could not draw this: on a scale that showed the "
                 "plastic, every conductor would be at zero.",
         "bars": {
             "aria_label": "A chart of resistance for seven specimens on a "
                           "logarithmic axis running from a hundredth of an "
                           "ohm to a hundred teraohms. Copper is the shortest "
                           "bar and the plastic ruler is by far the longest, "
                           "reaching almost the end of the axis.",
             # ⚠️ `axis_max` IS THE LAST TICK, NOT THE END OF THE RULE.
             # Design's scale is fixed by two points: 0.01 Ω at x=180 and
             # 1 TΩ at x=863, which is 14 decades over 683 px. Her axis LINE
             # then runs on to x=970 — about a hundred teraohms, which is
             # what her aria description says — and the plastic ruler's bar
             # legitimately overshoots the last tick. Measured off her SVG:
             # with 1e12 here the seven bars come out 34 / 100 / 170 / 224 /
             # 322 / 424 / 697 px and the boundary at 521, which is her
             # drawing to the pixel. With 1e14 they come out 30 / 87 / 148 /
             # 196 / 282 / 371 / 610 and the boundary at 479 — a chart that
             # is still internally consistent and is not hers.
             "axis_min": 0.01,
             "axis_max": 1e12,
             "axis_note": "EACH MARK IS A THOUSAND TIMES THE ONE BEFORE IT",
             "ticks": [
                 {"ohms": 0.01, "label": "0.01 Ω"},
                 {"ohms": 1, "label": "1 Ω"},
                 {"ohms": 1000, "label": "1 kΩ"},
                 {"ohms": 1000000, "label": "1 MΩ"},
                 {"ohms": 1000000000, "label": "1 GΩ"},
                 {"ohms": 1000000000000, "label": "1 TΩ"},
             ],
             "boundary": {
                 "ohms": 100000,
                 "label": ["NO SHARP LINE — ROUGHLY WHERE",
                           "USEFUL CONDUCTION GIVES OUT"],
             },
             "rows": [
                 {"label": "Copper wire", "ohms": 0.05, "value": "0.05 Ω"},
                 {"label": "Nichrome wire", "ohms": 1.1, "value": "1.1 Ω"},
                 {"label": "Pencil lead", "ohms": 30, "value": "30 Ω"},
                 {"label": "Salt water", "ohms": 400, "value": "400 Ω"},
                 {"label": "Tap water", "ohms": 40000, "value": "40 kΩ"},
                 {"label": "Dry wood", "ohms": 5000000, "value": "5 MΩ"},
                 {"label": "Plastic ruler", "ohms": 2000000000000,
                  "value": "2 TΩ"},
             ],
         },
         "close": "Read the gaps, not the bar lengths. Salt water resists "
                  "about four hundred times as much as nichrome; tap water "
                  "about a hundred times as much again; and the plastic ruler "
                  "about four hundred thousand times as much as the dry wood "
                  "beside it. Nothing on this axis is a switch that is off."},

        # ── #s-formula · the triangle Mide ruled in, and her CFIFA ─────
        {"type": "formula",
         "id": "resistance-rule-again",
         "eyebrow": "Writing it down · the shape of this relationship",
         "statement": "Potential difference = current × resistance",
         "triangle": {
             "eyebrow": "The triangle",
             "heading": "Cover the one you want",
             "aria_label": "A formula triangle. The potential difference V "
                           "sits above a dividing line; the current I and the "
                           "resistance R sit below it, multiplied together. "
                           "Covering one letter leaves the way to work it "
                           "out.",
             "order": ["top", "left", "right"],
             "covered": "right",
             "top":   {"label": "V", "button": "Cover V",
                       "result": "V = I × R",
                       "text": "Cover V and I and R are left side by side — "
                               "multiply them."},
             "left":  {"label": "I", "button": "Cover I",
                       "result": "I = V ÷ R",
                       "text": "Cover I on the triangle: V sits over R, so "
                               "you divide."},
             "right": {"label": "R", "button": "Cover R",
                       "result": "R = V ÷ I",
                       "text": "Cover R on the triangle: V sits over I, so "
                               "you divide."},
             "close": {
                 "rule": "Two things side by side means multiply. One thing "
                         "over another means divide.",
                 "units": ["V · potential difference across the test gap · V",
                           "I · current through the specimen in that gap · A",
                           "R · resistance of that specimen, at that length · "
                           "Ω"],
                 "condition": "1 Ω is 1 V for each 1 A",
             },
         }},

        {"type": "worked-example", "id": "cfifa-gap-plain"},
        {"type": "worked-example", "id": "cfifa-gap-convert"},
        {"type": "check", "id": "your-turn-gap", "anchor": "s-formula"},

        {"type": "key-fact", "ref": "one-continuous-range"},

        {"type": "misconception", "id": "think-insulators-block",
         "anchor": "s-think"},

        {"type": "quiz", "anchor": "s-ladder"},
        {"type": "summary", "id": "s-keynote"},
    ],

    "activities": [
        {"id": "cfifa-gap-plain",
         "kind": "worked-example",
         "demand": "calculate",
         "eyebrow": "Worked example · one step at a time",
         "heading": "The gap holds 10 cm of pencil lead on the 6.0 V supply, "
                    "and the ammeter reads 0.20 A. What is its resistance?",
         "head_counter": {"format": "Step {n} of 5", "total": 5},
         "buttons": {"first": "Show the first step",
                     "next": "Show the next step",
                     "done": "All five shown",
                     "done_note": "Nothing needed converting there. Now the "
                                  "one that does."},
         "staged": True,
         "fifa": [
             {"letter": "C", "label": "Convert",
              "line": "6.0 V stays 6.0 V · 0.20 A stays 0.20 A",
              "note": "The supply is in volts and the ammeter is in amps, so "
                      "there is nothing to convert."},
             {"letter": "F", "label": "Formula", "line": "R = V ÷ I",
              "note": "Cover R on the triangle: V sits over I, so you "
                      "divide."},
             {"letter": "I", "label": "Insert", "line": "R = 6.0 V ÷ 0.20 A",
              "note": "The p.d. is the supply across the gap; the current is "
                      "what the ammeter passes."},
             {"letter": "F", "label": "Fine-tune", "line": "6.0 ÷ 0.20 = 30",
              "note": "Volts divided by amps leaves ohms."},
             {"letter": "A", "label": "Answer", "line": "R = 30 Ω",
              "note": "That is the resistance of 10 cm of pencil lead."},
         ]},

        {"id": "cfifa-gap-convert",
         "kind": "worked-example",
         "demand": "calculate",
         "eyebrow": "Worked example · one step at a time",
         "heading": "A 12 cm strip of graphite on the 6.0 V supply, and the "
                    "ammeter reads 30 mA. What is its resistance?",
         "head_counter": {"format": "Step {n} of 5", "total": 5},
         "buttons": {"first": "Show the first step",
                     "next": "Show the next step",
                     "done": "All five shown",
                     "done_note": "Convert first, then the same four lines. "
                                  "Your turn below."},
         "staged": True,
         "fifa": [
             {"letter": "C", "label": "Convert",
              "line": "30 mA ÷ 1000 = 0.030 A",
              "note": "There are 1000 milliamps in an amp, so divide before "
                      "you go any further."},
             {"letter": "F", "label": "Formula", "line": "R = V ÷ I",
              "note": "Cover R on the triangle: V sits over I, so you "
                      "divide."},
             {"letter": "I", "label": "Insert", "line": "R = 6.0 V ÷ 0.030 A",
              "note": "The converted current goes in. The milliamp reading "
                      "never does."},
             {"letter": "F", "label": "Fine-tune", "line": "6.0 ÷ 0.030 = 200",
              "note": "Volts divided by amps leaves ohms."},
             {"letter": "A", "label": "Answer", "line": "R = 200 Ω",
              "note": "Put 30 in instead of 0.030 and you get 0.2 Ω — a "
                      "thousand times too small, and copper-like."},
         ]},

        {"id": "your-turn-gap",
         "kind": "p8-attempt",
         "demand": "calculate",
         "eyebrow": "Your turn · the same five steps",
         # The bench's opening state: 10 cm of pencil lead on 6.0 V, so the
         # ammeter reads 200.0 mA. `convline` and `convnote` are WHOLE
         # sentences rather than assembled ones, because Design computes the
         # Convert line from whatever unit the meter is showing, and the
         # divisor and the unit's name both change with it. `qhead` and
         # `qclose` are whole sentences for the same reason: the blocked
         # states replace them rather than filling them.
         #
         # ⊕ MRB-297, RULED 30 Aug 2026 — the line above used to read "mA,
         # µA, nA or pA". It no longer does: the practice is BOUNDED TO A AND
         # mA. Converting picoamps needs standard form, which is GCSE, so the
         # first practice item was harder than anything this page taught —
         # its own worked examples never go past milliamps. Six of the
         # fourteen reachable states did it (tap water, dry wood and the
         # plastic ruler, at both lengths); those now take the same blocked
         # path copper takes, with their own head naming the current and
         # saying it is below what a school ammeter shows. The eight A/mA
         # states are unchanged. Implemented in `wireTestGap` in
         # `shared/ks3.js` (`isShort || div > 1e3`), not here.
         "rest": {"len": "10 cm", "name": "pencil lead (graphite)",
                  "i": "200.0 mA", "iamps": "0.2 A", "ibare": "0.2",
                  "r": "30 Ω", "rohms": "30", "verdict": "a conductor",
                  "convline": "200.0 mA ÷ 1 000 = 0.2 A",
                  "convnote": "There are 1 000 milliamps in an amp, so divide "
                              "before you go any further.",
                  "qhead": "Your gap: 6.0 V across 10 cm of pencil lead "
                           "(graphite), and the ammeter reads 200.0 mA.",
                  "qclose": "The five lines give 30 Ω for 10 cm of pencil "
                            "lead (graphite)."},
         "questions": [
             {"id": "q1", "tab": "Question 1",
              "head": "{qhead}",
              "lead": "Write each line out yourself — starting by deciding "
                      "whether anything needs converting. Then check your "
                      "working and tick the lines you had.",
              # ⊕ HER `blockedProgress`, verbatim — the readout beside the
              # Check button while the copper short leaves nothing to divide.
              "blocked_progress": "Waiting on a specimen the ammeter can read",
              "blocked_lead": "Clip a specimen the ammeter can read into the "
                              "gap at the bench, and these five lines will "
                              "follow it.",
              "steps": [
                  {"letter": "C", "label": "Convert",
                   "placeholder": "anything to convert?",
                   "line": "{convline}",
                   "note": "{convnote}"},
                  {"letter": "F", "label": "Formula", "line": "R = V ÷ I",
                   "note": "Cover R on the triangle: V sits over I, so you "
                           "divide."},
                  {"letter": "I", "label": "Insert",
                   "line": "R = 6.0 V ÷ {iamps}",
                   "note": "The supply is fixed, so only the current changes "
                           "from specimen to specimen."},
                  {"letter": "F", "label": "Fine-tune",
                   "line": "6.0 ÷ {ibare} = {rohms}",
                   "note": "Volts divided by amps leaves ohms, however small "
                           "the current is."},
                  {"letter": "A", "label": "Answer",
                   "placeholder": "remember the unit",
                   "line": "R = {r}",
                   "note": "That is the resistance of {len} of {name}, which "
                           "is what makes it {verdict}."},
              ],
              "close": "{qclose}"},
             # ⚑ HER Q2 IS `mode: 'pick'` AND THE KIT IS WRITE-IT-OUT ONLY.
             # Her five model lines, her head and her closing sentence are
             # ported verbatim; the input shape is the kit's. Register row.
             {"id": "q2", "tab": "Question 2",
              "head": "A 15 cm strip of nichrome on the 6.0 V supply, and the "
                      "ammeter reads 24 mA.",
              "lead": "This one needs the Convert line to do some work.",
              "steps": [
                  {"letter": "C", "label": "Convert",
                   "placeholder": "anything to convert?",
                   "line": "24 mA ÷ 1000 = 0.024 A",
                   "note": "There are 1000 milliamps in an amp, so divide "
                           "before you go any further."},
                  {"letter": "F", "label": "Formula", "line": "R = V ÷ I",
                   "note": "Cover R on the triangle: V sits over I, so you "
                           "divide."},
                  {"letter": "I", "label": "Insert",
                   "line": "R = 6.0 V ÷ 0.024 A",
                   "note": "The converted current goes in. The milliamp "
                           "reading never does."},
                  {"letter": "F", "label": "Fine-tune",
                   "line": "6.0 ÷ 0.024 = 250",
                   "note": "Volts divided by amps leaves ohms."},
                  {"letter": "A", "label": "Answer",
                   "placeholder": "remember the unit",
                   "line": "R = 250 Ω",
                   "note": "Put 24 in instead of 0.024 and you get 0.25 Ω — a "
                           "thousand times too small."},
              ],
              "close": "The five lines give 250 Ω for 15 cm of nichrome."},
         ]},

        {"id": "think-insulators-block",
         "kind": "predict",
         "demand": "explain",
         "targets": "CIRC-21",
         "statements": [
             {"quote": "An insulator blocks electricity completely — "
                       "absolutely nothing gets through.",
              "targets": "CIRC-21",
              "body": [
                  "Not quite nothing. Put 6 V across a plastic ruler and a "
                  "current does flow: about three millionths of a millionth "
                  "of an amp. It is too small for any school meter to see and "
                  "far too small to do anything, which is exactly why we call "
                  "the plastic an insulator — but the word describes how "
                  "little, not none. The distinction matters at high "
                  "voltages, where \"too small to matter\" stops being true: "
                  "this is why overhead power lines hang from ceramic "
                  "insulators the size of a bucket rather than a strip of "
                  "tape.",
              ]},
             {"quote": "Materials are either conductors or insulators, with "
                       "nothing in between.",
              "targets": "CIRC-22",
              "body": [
                  "The middle of the range is crowded. Pencil lead conducts "
                  "well enough to light a bulb and badly enough to get hot "
                  "doing it. Tap water conducts a hundred times worse than "
                  "salt water and a thousand times better than dry wood. Damp "
                  "wood is a different material, electrically, from dry wood. "
                  "And silicon sits deliberately in the middle: a "
                  "semiconductor whose resistance can be controlled, which is "
                  "the entire basis of every chip ever made.",
              ]},
         ]},
    ],

    "figures": [],

    "key_facts": [
        {"id": "one-continuous-range",
         "eyebrow": "Key fact",
         "ground": "card",
         "placement": "top-level",
         "text": "A conductor has charges free to move — loose electrons in a "
                 "metal, dissolved ions in salt water — and a low resistance. "
                 "An insulator has none free and a resistance millions of "
                 "millions of times higher. The two are the ends of one "
                 "continuous range, not two separate kinds of material."},
    ],

    # ⚠️ MRB-278 · POSITION IS AUTHORED. This lesson takes indices 1 and 3.
    "ladder": {
        "recall": {
            "q": "A specimen is clipped across a 6.0 V supply and the ammeter "
                 "reads 0.15 A. What is its resistance, and how would you "
                 "classify it?",
            "options": [
                "0.9 Ω — a conductor",
                "40 Ω — a conductor",
                "40 Ω — an insulator",
                "0.025 Ω — a very good conductor",
            ],
            "answer": 1,
            "feedback": {
                0: "The classification is right but the arithmetic is a "
                   "multiplication. Resistance is volts divided by amps: "
                   "6.0 ÷ 0.15.",
                2: "The resistance is right. Forty ohms lets 0.15 A through "
                   "on six volts, which is enough to light a lamp — nothing "
                   "like the millions of ohms of an insulator.",
                3: "That is amps divided by volts, which is the division "
                   "upside down. Volts on top gives 40 Ω.",
            },
            "title": "Rung 1 · Calculate and classify"},
        "apply": {
            "q": "A student clips a plastic ruler across 6 V, sees the "
                 "ammeter stay on zero, and concludes that the resistance of "
                 "plastic is infinite. What is right?",
            # ⚑ Option A is FINISHED into a complete wrong rule so that the
            # correct answer is no longer a length tell. Her wrong idea and
            # her correction are untouched; the clause after the comma states
            # the rule the wrong idea depends on. See DEPARTURES-P8.md row 1.
            "options": [
                "The student is right: an insulator has infinite resistance, "
                "which is why the reading is exactly zero — a material either "
                "has free charges in it and conducts, or has none at all and "
                "stops the current dead.",
                "The resistance cannot be worked out at all, because dividing "
                "by a zero reading is impossible.",
                "The resistance is enormous, because plastic has no atoms "
                "that can carry charge.",
                "The resistance is enormous but finite — around 2 TΩ for that "
                "ruler, which passes a current of a few millionths of a "
                "millionth of an amp, far below what the meter can show.",
            ],
            "answer": 3,
            "feedback": {
                0: "The reading is zero because the meter cannot resolve a "
                   "current that small, not because there is none. Nothing "
                   "has an infinite resistance.",
                1: "The reading is not really zero — it is below the meter’s "
                   "resolution. With a sensitive enough instrument you get a "
                   "current, and a division.",
                2: "The verdict is right and the reason is not. Plastic is "
                   "full of electrons; the point is that they are all locked "
                   "into bonds rather than free to drift.",
            },
            "title": "Rung 2 · The one that catches people"},
        "explain": {
            "q": "Explain why a lamp flex is made of copper inside and "
                 "plastic outside, using resistance figures and the idea of "
                 "free charges.",
            "field_label": "Your explanation",
            "placeholder": "The copper has free electrons, so…",
            "success": [
                "Says copper has loose electrons free to move, so it has a "
                "very low resistance.",
                "Gives a figure for the copper — a fraction of an ohm for a "
                "short length.",
                "Says the plastic has no free charges because its electrons "
                "are locked into bonds.",
                "Gives a figure for the plastic, in millions of ohms or "
                "higher, or says it is millions of millions of times more.",
                "Concludes that the current stays in the copper because the "
                "sideways route resists so enormously more.",
            ],
            "title": "Rung 3 · Explain"},
        "produce": {
            "q": "A wooden ladder is often said to be safer than an aluminium "
                 "one near overhead cables, but electricians are taught that "
                 "a wet wooden ladder is not safe at all. Explain both "
                 "statements using resistance.",
            "field_label": "Your answer",
            "placeholder": "Dry wood has a resistance of about…",
            "success": [
                "Gives dry wood a resistance in the millions of ohms, and "
                "says that is high enough to pass a negligible current at "
                "ordinary voltages.",
                "Says aluminium is a metal with free electrons and a "
                "resistance below an ohm, so it conducts freely.",
                "Says water on or in the wood adds dissolved ions, which are "
                "charges free to move.",
                "Says that drops the resistance by a large factor — wet wood "
                "behaves far more like tap water than like dry wood.",
                "Concludes that the material has not changed its identity, "
                "only its resistance, and that \"insulator\" was always a "
                "judgement about how much current, not none.",
            ],
            "title": "Rung 4 · Take it somewhere new"},
    },

    "key_note": "A conductor has charges free to move and a low resistance; "
                "an insulator has almost none free and a resistance millions "
                "of millions of times higher. In a metal the free charges are "
                "loose electrons; in salt water they are dissolved ions. The "
                "difference is measured, not declared: put a known p.d. "
                "across a specimen, read the current, divide. The results "
                "fill a continuous range from hundredths of an ohm to "
                "millions of millions of ohms, with graphite, salt water, tap "
                "water and damp wood spread across the middle, so "
                "\"insulator\" means the current is too small to matter "
                "rather than that there is none.",

    "stretch": [
        {"id": "silicon-is-the-interesting-one",
         "type": "explainer",
         "text": "Silicon is the interesting one. On its own it is a poor "
                 "conductor, but add a few atoms of another element per "
                 "million — doping — and its resistance drops by orders of "
                 "magnitude in a way you can design. Put two differently "
                 "doped regions side by side and you have a component that "
                 "conducts one way and not the other; put three together and "
                 "you have a switch with no moving parts. Every transistor in "
                 "every chip is that trick, repeated. The whole of computing "
                 "rests on a material that refused to be either a conductor "
                 "or an insulator."},
        {"id": "some-metals-stop-resisting",
         "type": "explainer",
         "text": "At the other extreme, some metals stop resisting "
                 "altogether. Cool mercury below about 4 kelvin and its "
                 "resistance does not merely fall, it becomes zero: a current "
                 "started in a loop of it will still be going years later. "
                 "Superconductors are how MRI scanners make their enormous "
                 "magnetic fields, and the reason those machines need a tank "
                 "of liquid helium to work at all."},
    ],

    "support": [],

    "vocabulary": [
        {"term": "conductor",
         "definition": "A material with charges free to move — loose "
                       "electrons in a metal, dissolved ions in salt water — "
                       "and so a low resistance."},
        {"term": "insulator",
         "definition": "A material with almost no free charges, and a "
                       "resistance so high that the current it passes is too "
                       "small to matter."},
        {"term": "semiconductor",
         "definition": "A material in the middle of the range, like silicon, "
                       "whose resistance can be controlled on purpose."},
        {"term": "short circuit",
         "definition": "A path of almost no resistance straight across a "
                       "supply. What flows then is set by the supply, not by "
                       "the wire."},
    ],

    "tutor": {
        "anchor": "s-test",
        "prompt": "Ask Mr Badmus AI",
        "body": "Got a current and a p.d. and want to know whether it counts "
                "as a conductor?",
        "cta": "Ask about this lesson"},

    "ks4_becomes": "Resistivity as a property of the material rather than the "
                   "sample, semiconductors and doping, and thermistors as "
                   "resistance that reports temperature.",

    # ⊕ §8.10 rules the TREATMENT — one quiet foot line above the legal line,
    # never a callout. The WORDS are Design's, character for character, and
    # the number is not taken up: Childline on 0800 1111 is the same service
    # and the same digits the B5 and P6 lessons already carry.
    "safeguarding_note": "Mains electricity is not a bench supply, and a "
                         "scorched socket, a cable with the copper showing or "
                         "a plug that gets hot is worth telling an adult "
                         "about the same day — never test it yourself. If "
                         "there is no one at home you can tell, Childline is "
                         "free on 0800 1111, at any hour, and you do not have "
                         "to give your name.",

    "convention_note": "The bench is a teaching model. The seven resistances "
                       "are typical values for a 10 cm specimen and not "
                       "measurements of particular objects: real samples vary "
                       "widely with thickness, purity, temperature and, for "
                       "wood and water, how much moisture and dissolved salt "
                       "they contain. Lengthening a specimen tenfold is taken "
                       "to multiply its resistance by ten, which holds for a "
                       "sample of even cross-section. The supply, leads and "
                       "meter are treated as having no resistance, so the "
                       "reading is the specimen's alone. The copper state "
                       "deliberately reports no current: a bare copper wire "
                       "across a supply is a short circuit, and the current "
                       "then depends on what the supply can deliver rather "
                       "than on the wire, so there is no honest figure for "
                       "the meter to show. The boundary drawn on the figure "
                       "is a convenience and not a real dividing line.",

    "ws": ["measurement", "analysis"],
}
