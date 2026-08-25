"""P10 L2 — Magnetic fields (INVESTIGATION).

Authored against Claude Design's approved page,
`docs/ks3/design-reference/p10/p10-02-magnetic-fields.dc.html`.

Her page wins outright. The filings on the paper, the four layouts, the
twenty-five plotting positions, the four rules and all four rungs are hers.

── ⚖️ THE LESSON IS A MEASUREMENT, AND THE LINES ARE A DRAWING ────────

That is the sentence the whole page turns on and it appears three times: in
the explainer (*"the lines themselves are a drawing"*), on the fourth rule
card (*"the compass is the measurement; the line is the drawing"*) and in the
key note. `MAG-05` and `MAG-06` are both versions of forgetting it — the field
is only where the lines are, or the filings made it — and the bench is what
settles them, because the student puts the compass down and reads a direction
in the gaps between the drawn arrows as easily as on them.

── ⚖️ THE MODEL, AND WHAT IT LEAVES OUT ──────────────────────────────

Each bar magnet is a PAIR OF POINT POLES, which is the standard way of
constructing a field map by hand and gives the right shape everywhere except
very close to the metal. The legal line says so, and it also says that the
Earth's own field is left out — a real plotting compass adds it and points
somewhere between. Both hedges are load-bearing (her §8) and both stay.

── ⚠️ TWO MEASURED CORRECTIONS TO HER MODEL, AND WHY ─────────────────

Both were found by enumerating her own `renderVals` over all 100 states rather
than by reading her §4, and both are `DEPARTURES-P10.md` rows.

**1. THE NEUTRAL POINT WAS A THRESHOLD, AND IT FIRED SIXTEEN TIMES TOO OFTEN.**
Her test is `rel < 0.6`. Measured: it is true in 17 of the 100 states, and
exactly ONE of them is a neutral point. Ten of the false positives are on the
horseshoe, which has no neutral point at all, and the note printed at every
one of them reads *"they cancel and the total is zero — not weak, zero"* and
*"This is called a neutral point."* That is the exact distinction her own
*Going further* calls *"one of very few places in physics where a quantity is
exactly nothing rather than merely small"*, so a page that prints it at a
merely-small reading teaches the opposite of its own stretch paragraph. The
test here is a CANCELLATION: the vector sum of the poles' contributions
against the sum of their sizes. At the true null that ratio is 0.000; at the
next-nearest state it is 0.298. The two populations are two orders of
magnitude apart with nothing in between.

**2. 100 WAS A PLACE THE COMPASS COULD NOT BE PUT.** Her reference is the
strongest point on the 13 × 7 arrow lattice, which sits hard against a pole
where no button on the grid can go. Measured across all four layouts, the
highest reading a student could ever obtain on her scale is 18.05, her top
band (`very strong`, ≥ 40) is unreachable, and 78 of the 96 readings fall into
the single bottom band. The reference here is the strongest of the
twenty-five spots the compass can actually be put on — which is what the
readout says it is — and the four bands then hold 20, 24, 27 and 24 states.
The readout's own wording moves with it: *"the strongest spot you can reach
here"*.

── ⚖️ THE STATE SPACE ────────────────────────────────────────────────

    4 layouts × 25 positions        100
      on the metal                    4   no reading, and the needle is not
                                          drawn
      the neutral point               1   reachable, at the centre of the
                                          like-poles layout
      a reading                      95   every one with a real bearing

── ⚠️ MRB-278 · POSITION IS AUTHORED ─────────────────────────────────

Design's rungs both put the correct answer at index 0; her commit gate does
NOT, and puts it at 2, which is why the gate is left exactly as she wrote it.
**Her option TEXT and every correction are verbatim; only the ORDER moves.**
This lesson takes indices 0 (hook, hers), 2 (gate, hers), 3 (rung 1) and 0
(rung 2). Engine policy, not a register row.

── ⚠️ NO DRAFT MARKINGS. NO SAFEGUARDING BLOCK. ─────────────────────
"""

LESSON = {
    "slug": "magnetic-fields",
    "title": "Magnetic fields",
    "discipline": "physics",
    "unit": "Magnetism and electromagnetism",
    "family": "INVESTIGATION",

    "covers": ["KS3.P.MAG.02"],
    "touches": ["KS3.WS.MEA.01", "KS3.WS.ANA.01"],
    "beyond_statutory": False,
    "threads": [{"id": "forces-and-fields", "level": 3}],
    "typical_year": 9,
    "typical_minutes": 60,

    # ⚠️ THE EDGE IS DECLARED AND NOTHING IS ASSUMED. Design's §3: this page
    # defines a pole from nothing, so a school running P10 in another order
    # strands nobody. The edge is still declared, because it is the honest
    # reading order.
    "requires": ["magnets-and-poles"],
    "assumes": [],
    "references": [{"unit": "P9", "lesson": "electric-fields"},
                   {"unit": "P9", "lesson": "forces-between-charges"}],
    "ks4_links": [],

    "meta_description": "A magnetic field is the region where a magnet would "
                        "feel a force — and a field line is nothing more than "
                        "a row of compass readings joined up.",

    # ⊕ Integration, 25 Aug 2026 — HER LEDE, verbatim (Phase 3 revert; the
    # authored question was a paraphrase no row claimed).
    "big_question": "The space around a magnet is not empty. A compass needle "
                    "finds a direction at every point in it, and joining those "
                    "directions up is the whole of what a field line is.",

    "rail": [
        {"anchor": "s-hook",  "short": "FILINGS",
         "label": "Filings on paper",      "done_when": "committed"},
        {"anchor": "s-bench", "short": "BENCH",
         "label": "Plot it with a compass", "done_when": "gate_and_a_control"},
        # ⚠️ Design's `DONE` gives this stop the GATE alone, before the bench
        # beside it is finished. The bench marks it through `band_anchor` /
        # `band_at`; see `ks3_art/p10.py`.
        {"anchor": "s-rules", "short": "RULES",
         "label": "Four rules",            "done_when": "gate_committed"},
        {"anchor": "s-ladder", "short": "LADDER",
         "label": "Mastery ladder",        "done_when": "ladder_complete"},
    ],

    "phenomenon": {
        "kind": "narrative",
        "title": "Sprinkle iron filings on the paper and a pattern appears.",
        "prompt": "A bar magnet sits under a sheet of paper. Scatter iron "
                  "filings on top, tap the sheet once, and they arrange "
                  "themselves into curved lines that loop from one end of the "
                  "magnet round to the other. Nobody moved them into place.",
        "commit": "Where did the lines come from?",
        # ⚠️ MRB-278 — position 0 is Design's own here, and it is kept: this
        # unit takes 2, 0, 3, 1, 2 across its five hooks, so index 0 is used
        # once rather than five times.
        "options": [
            "Each filing turns into a tiny magnet and lines up with a field "
            "that was already there",
            "The magnet draws the lines onto the paper, and the filings fall "
            "into the grooves",
            "The filings are pushed to wherever the field is strongest and "
            "pile up in ridges",
            "Tapping the paper gives the filings a charge, and charged specks "
            "repel into rows",
        ],
        "answer": 0,
        "reveal": "The field was there before the filings were. Each filing "
                  "is a scrap of iron, so sitting in the field turns it into "
                  "a small magnet, and a small magnet turns until it lies "
                  "along the field — the same thing a compass needle does. "
                  "Thousands of them do it at once and join up end to end, "
                  "and the chains they make are the pattern you see. Sweep "
                  "them off and the field is exactly as it was.",
    },

    "misconceptions": [
        {"id": "MAG-05",
         "statement": "The field is only where the lines are drawn. In "
                      "between the lines there is nothing.",
         "elicited_by": "plot",
         "confronted_by": "s-think"},
        {"id": "MAG-06",
         "statement": "The iron filings make the field.",
         "elicited_by": "s-hook",
         "confronted_by": "s-think"},
        {"id": "MAG-07",
         "statement": "Field lines can cross if the field is strong enough.",
         "elicited_by": "s-ladder",
         "confronted_by": "rules"},
        # ⊕ MINTED FROM RUNG 1'S SECOND OPTION, which has its own correction
        # on her page: *"Every line that leaves the north pole arrives at the
        # south pole, so the count is the same everywhere. What differs is how
        # much space they are spread over."* Separate from `MAG-05`: a student
        # can accept that the field fills the gaps and still believe the
        # magnet grows extra lines at its ends, and that belief is what makes
        # crowding look like a count instead of a comparison.
        {"id": "MAG-08",
         "statement": "Where the lines are crowded there are more of them, "
                      "because the magnet makes extra lines at its ends.",
         "elicited_by": "s-ladder",
         "confronted_by": "rules"},
    ],

    "core": [
        {"type": "hook", "id": "hook-commit", "anchor": "s-hook"},

        {"type": "explainer",
         "text": "A <strong>magnetic field</strong> is the region around a "
                 "magnet where another magnet, or a piece of iron, steel, "
                 "nickel or cobalt, would feel a force. It is there whether "
                 "or not anything is in it to feel it, and it fills space in "
                 "three dimensions — the filings only show you one flat slice "
                 "of it."},
        {"type": "explainer",
         "text": "We draw the field with <strong>field lines</strong>. A line "
                 "shows the direction a compass needle's north-seeking end "
                 "would point if you put it at that spot, and the rule is "
                 "that lines run <strong>out of a north pole and into a south "
                 "pole</strong> on the outside of a magnet. Where the lines "
                 "are <strong>crowded together the field is strong</strong>; "
                 "where they spread apart it is weak. Field lines never "
                 "cross, because a compass at any one point can only point "
                 "one way."},
        {"type": "explainer",
         "text": "Plotting a field means doing exactly that, by hand: put a "
                 "small compass down, mark the direction it settles to, move "
                 "it along, mark again, and join up the marks. That is the "
                 "measurement. The lines themselves are a drawing — useful, "
                 "agreed on by everybody, and not something you would find if "
                 "you went looking with a microscope."},

        # ── #s-bench · a plotting compass on a field map ───────────────
        {"type": "compass-plot",
         "id": "plot",
         "anchor": "s-bench",
         "eyebrow": "At the bench · a plotting compass on a field map",
         "heading": "Put the compass down and read it.",
         "progress": {"idle": "Change a control to begin",
                      "live": "Two controls live"},
         # ⚠️ HER FIRST SENTENCE IS CUT. It read "Choose what is laid out on
         # the bench, then choose where on the paper the plotting compass
         # goes" — two clauses naming two controls that are already on screen
         # (5A.1). The convention sentence stays, because it is the only thing
         # that makes a bearing readable at all.
         "lead": "Bearings are measured clockwise from the top of the page.",
         "band_anchor": "s-rules",
         "band_at": 1,
         # ⚖️ THE CANCELLATION TEST. A spot counts as a neutral point when the
         # VECTOR sum of the poles' contributions falls below this fraction of
         # the sum of their SIZES — which is a test for cancelling rather than
         # for smallness. Measured on this payload: 0.000 at the true null,
         # 0.298 at the next nearest state.
         "null_ratio": 0.02,
         "spot_x": [180, 340, 500, 660, 820],
         "spot_y": [56, 128, 200, 272, 344],
         "start_setup": 0,
         "start_x": 3,
         "start_y": 1,
         "setup_label": "On the paper",
         "spot_label": "Where the compass goes",
         "gate": {
             "prompt": "Commit first. Two bar magnets are laid end to end "
                       "with their north poles facing each other, a few "
                       "centimetres apart. A compass is put down exactly half "
                       "way between them. What does the needle do?",
             # ⚠️ Design's own order, and her own index 2 — the one marked set
             # in the whole delivery that does not sit at 0.
             "options": [
                 "It settles pointing straight from one magnet to the other, "
                 "along the gap",
                 "It spins continuously, because both magnets keep pulling it "
                 "round",
                 "It does not settle anywhere in particular and stays "
                 "wherever you leave it",
                 "It points at right angles to the magnets, towards the top "
                 "of the page",
             ],
             "answer": 2,
         },
         # ⚖️ EACH BAR IS A PAIR OF POINT POLES, `q` = +1 north, −1 south.
         # `bars` is the drawing and `poles` is the model; the two are
         # separate because the drawn bar is wider than the two points that
         # make its field, which is exactly the approximation the legal line
         # discloses.
         "setups": [
             {"id": "single", "label": "One bar magnet",
              "word": "a single bar magnet lying across the middle of the "
                      "paper",
              "bars": [{"x1": 390, "x2": 610, "y": 200, "left_pole": "S"}],
              "poles": [{"x": 400, "y": 200, "q": -1},
                        {"x": 600, "y": 200, "q": 1}],
              "note": "Move out to the sides and the arrows get shorter and "
                      "further apart; move back towards either end and they "
                      "crowd in and lengthen. The map is the same shape "
                      "whichever way up you draw it."},
             {"id": "unlike", "label": "Two magnets, N facing S",
              "word": "two bar magnets end to end with a north pole facing a "
                      "south pole across the gap",
              "bars": [{"x1": 130, "x2": 350, "y": 200, "left_pole": "S"},
                       {"x1": 650, "x2": 870, "y": 200, "left_pole": "S"}],
              "poles": [{"x": 140, "y": 200, "q": -1},
                        {"x": 340, "y": 200, "q": 1},
                        {"x": 660, "y": 200, "q": -1},
                        {"x": 860, "y": 200, "q": 1}],
              "note": "With a north pole facing a south pole the lines run "
                      "straight across the gap from one to the other, which "
                      "is why that gap is the strongest part of the whole "
                      "map."},
             {"id": "like", "label": "Two magnets, N facing N",
              "word": "two bar magnets end to end with their north poles "
                      "facing each other across the gap",
              "bars": [{"x1": 130, "x2": 350, "y": 200, "left_pole": "S"},
                       {"x1": 650, "x2": 870, "y": 200, "left_pole": "N"}],
              "poles": [{"x": 140, "y": 200, "q": -1},
                        {"x": 340, "y": 200, "q": 1},
                        {"x": 660, "y": 200, "q": 1},
                        {"x": 860, "y": 200, "q": -1}],
              "note": "With two north poles facing each other the lines "
                      "refuse to cross the gap and turn away sideways "
                      "instead, and somewhere on the centre line between them "
                      "they cancel altogether."},
             {"id": "horseshoe", "label": "A horseshoe magnet",
              "word": "a horseshoe magnet with its north jaw above the gap "
                      "and its south jaw below it",
              "bars": [{"x1": 340, "x2": 660, "y": 96, "left_pole": "N"},
                       {"x1": 340, "x2": 660, "y": 304, "left_pole": "S"}],
              "poles": [{"x": 420, "y": 110, "q": 1},
                        {"x": 580, "y": 110, "q": 1},
                        {"x": 420, "y": 290, "q": -1},
                        {"x": 580, "y": 290, "q": -1}],
              "note": "Between the jaws of a horseshoe the arrows are close "
                      "to parallel and close to the same length, which is "
                      "what a nearly uniform field looks like — the reason a "
                      "horseshoe is the shape chosen when a steady field is "
                      "wanted in a gap."},
         ],
         # ⚠️ FOUR WORDS, READ HIGHEST-FIRST, AND EVERY ONE OF THEM IS
         # REACHABLE. Against the strongest spot a compass can be put on,
         # these hold 20, 24, 27 and 24 of the 95 reading states. Against
         # Design's own reference they held 0, 3, 15 and 78, which is what
         # made the correction worth making.
         "strength_bands": [
             {"at_least": 45, "word": "very strong"},
             {"at_least": 18, "word": "strong"},
             {"at_least": 6, "word": "moderate"},
             {"at_least": 0, "word": "weak"},
         ],
         # ⚠️ THE CROWDING WORD IS A SECOND READING OF THE SAME NUMBER, and it
         # is derived from it rather than authored beside it — so the tile
         # that says `weak` can never sit next to a tile that says `packed
         # tightly` (5A.1).
         "crowd_bands": [
             {"at_least": 45, "word": "packed tightly together"},
             {"at_least": 18, "word": "fairly close together"},
             {"at_least": 6, "word": "opening out"},
             {"at_least": 0, "word": "far apart"},
         ],
         "readouts": [
             {"id": "bearing", "label": "The needle points", "sub": "—"},
             {"id": "strength", "label": "Field strength here", "sub": "—"},
             {"id": "crowd", "label": "Lines near the compass"},
         ],
         # ⚠️ `{bearing}` is the bearing in whole degrees, `{compass}` the
         # eight-point name for it, `{rel}` the relative reading and `{setup}`
         # the sentence the chosen layout carries.
         "branches": {
             "on_magnet": {
                 "verdict": "no reading here",
                 "sub": "the compass is on the metal",
                 "crowd": "not drawn inside the metal",
                 "note": "The compass is sitting on the magnet itself, so "
                         "there is no reading to take. Field maps are drawn "
                         "for the space around a magnet, not through the "
                         "metal — and the lines you would draw inside run the "
                         "other way, from the south pole back to the north, "
                         "which is what makes every line a closed loop. Move "
                         "the compass off the bar and the needle settles "
                         "again."},
             "neutral": {
                 "verdict": "nothing to turn it",
                 "sub": "the two fields cancel here",
                 "crowd": "curving away on both sides",
                 "note": "Here the needle has nothing to turn it. Both "
                         "magnets reach this spot and their fields point in "
                         "opposite directions with the same strength, so they "
                         "cancel and the total is zero — not weak, zero. "
                         "Leave the compass at any angle and it stays there. "
                         "Scatter iron filings over this point and you get a "
                         "bare patch with lines curving away on either side "
                         "of it. This is called a neutral point."},
             "reading": {
                 "note": "At this spot the needle settles on a bearing of "
                         "{bearing}, which is {compass} on the page, and the "
                         "field here reads {rel} against the strongest spot "
                         "you can reach on this map. {setup} Drop the compass "
                         "anywhere on the paper and it points along the arrow "
                         "it lands on — that is all a field line ever was."},
         },
         "words": {
             "no_reading": "no reading",
             "on_metal": "the compass is on the magnet",
             "no_direction": "no settled direction",
             "is_zero": "the field here is zero",
             "scale": "{rel} where 100 is the strongest spot you can reach "
                      "here",
             "on_page": "{compass} on the page",
             # ⚠️ EIGHT NAMES, IN ORDER FROM NORTH, READ AS A LIST BY THE
             # WIRING. They are words a student reads, so they are authored
             # here rather than typed into `shared/ks3.js`.
             "compass_points": "north · north-east · east · south-east · "
                               "south · south-west · west · north-west",
         }},

        # ── #s-rules · four rules that let you draw any field ──────────
        {"type": "mag-band",
         "id": "rules",
         "anchor": "s-rules",
         "eyebrow": "The figure",
         "heading": "Four rules that let you draw any field",
         "lead": "Every field map in physics obeys these four, and every one "
                 "of them comes straight from what a plotting compass does.",
         "tiles": [
             {"id": "rule-outin", "art": "out-in",
              "aria_label": "A bar magnet with a line leaving the north end "
                            "and curving round into the south end.",
              "body": "Outside the magnet, every line leaves the north pole "
                      "and arrives at the south pole. The arrow is the way a "
                      "compass points."},
             {"id": "rule-crowd", "art": "crowd",
              "aria_label": "Lines packed tightly at one end of a diagram and "
                            "spread widely at the other.",
              "body": "Crowded lines mean a strong field. Spread-out lines "
                      "mean a weak one. That is why lines bunch at the "
                      "poles."},
             {"id": "rule-nocross", "art": "no-cross",
              "aria_label": "Two lines crossing, marked as impossible.",
              "body": "Lines never cross. A compass at a crossing point would "
                      "have to face two ways at once, and it cannot."},
             {"id": "rule-readings", "art": "readings", "accent": True,
              "aria_label": "A curved line with three small compasses sitting "
                            "along it, each aligned with the line.",
              "body": "A line is nothing more than a row of compass readings "
                      "joined up. The compass is the measurement; the line is "
                      "the drawing."},
         ]},

        {"type": "key-fact", "ref": "the-field-is-the-region"},

        {"type": "misconception", "id": "think-only-where-drawn",
         "anchor": "s-think"},

        {"type": "quiz", "anchor": "s-ladder"},
        {"type": "summary", "id": "s-keynote"},
    ],

    "activities": [
        {"id": "think-only-where-drawn",
         "kind": "predict",
         "demand": "explain",
         "targets": "MAG-05",
         "statements": [
             {"quote": "The field is only where the lines are drawn. In "
                       "between the lines there is nothing.",
              "targets": "MAG-05",
              "body": [
                  "The field is everywhere around the magnet, at full "
                  "strength, in the gaps as much as on the lines. How many "
                  "lines get drawn is a decision made by whoever is drawing: "
                  "draw eight and the map looks sparse, draw eighty and it "
                  "looks dense, and the magnet has not changed. What the "
                  "spacing carries is a comparison — this part of the map is "
                  "stronger than that part — not a count of anything real. "
                  "Put your compass down between two drawn lines and it still "
                  "swings to a definite direction, because there was a "
                  "direction there all along.",
              ]},
             {"quote": "The filings make the field.",
              "targets": "MAG-06",
              "body": [
                  "Reverse it. The field was there before the filings arrived "
                  "and stays after you sweep them off. Each filing is a small "
                  "piece of iron, so being in the field turns it into a tiny "
                  "magnet, and a tiny magnet in a field turns until it lies "
                  "along the direction of the field — exactly what a compass "
                  "needle does, only there are thousands of them and they are "
                  "free to touch. They line up end to end and the chains they "
                  "make are what you see. The filings are the detector, not "
                  "the cause.",
              ]},
         ]},
    ],

    "figures": [],

    "key_facts": [
        {"id": "the-field-is-the-region",
         "eyebrow": "Key fact",
         "ground": "card",
         "placement": "top-level",
         "text": "A magnetic field is the region where a magnet or a magnetic "
                 "material would feel a force, and it is there whether or not "
                 "anything is in it. Field lines show which way a compass "
                 "needle points; outside a magnet they run from north pole to "
                 "south pole, they are crowded where the field is strong, and "
                 "they never cross."},
    ],

    # ⚠️ MRB-278 · POSITION IS AUTHORED. This lesson's rungs take indices 3
    # and 0. Design put both at 0; her option TEXT and every correction are
    # verbatim and only the ORDER moves.
    "ladder": {
        "recall": {
            "q": "On a field map of one bar magnet, the lines near the ends "
                 "are packed close together and the lines out at the sides "
                 "are far apart. What does that tell you?",
            "options": [
                "There are more field lines near the ends than out at the "
                "sides",
                "The field only exists near the ends, because that is where "
                "lines were drawn",
                "The field is stronger out at the sides, because it has "
                "spread further",
                "The field is stronger near the ends than out at the sides",
            ],
            "answer": 3,
            "feedback": {
                0: "Every line that leaves the north pole arrives at the "
                   "south pole, so the count is the same everywhere. What "
                   "differs is how much space they are spread over.",
                1: "The field fills the whole region, including the gaps "
                   "between drawn lines. Spacing compares strengths; it does "
                   "not mark where the field stops.",
                2: "Spreading out is what a field does as it weakens. Crowded "
                   "lines mean strong, not weak.",
            },
            "title": "Rung 1 · Read the map"},
        "apply": {
            "q": "A student draws a field map in which two lines meet and "
                 "cross at a point. Why must the drawing be wrong?",
            "options": [
                "A compass at that point would have to settle in two "
                "directions at once",
                "Lines are not allowed to cross because the field is too "
                "strong at a crossing point",
                "Lines can cross, but only outside the magnet, and this "
                "crossing is inside it",
                "The lines would cancel each other out where they cross, "
                "leaving a gap",
            ],
            "answer": 0,
            "feedback": {
                1: "Field strength has nothing to do with it. The problem is "
                   "direction: a compass settles to one direction and can "
                   "only do that if one line passes through the point.",
                2: "Lines never cross anywhere, inside or outside. There is "
                   "no place where the field points two ways.",
                3: "Fields do add and can cancel — a neutral point is exactly "
                   "that — but the result is still one direction, or none. It "
                   "is never two.",
            },
            "title": "Rung 2 · Apply the rule"},
        "explain": {
            "q": "Explain how you would plot the field around a bar magnet "
                 "using a plotting compass and a pencil, and say what each "
                 "pencil mark actually records.",
            "field_label": "Your method",
            "placeholder": "Put the magnet on the paper and draw round it, "
                           "then…",
            "success": [
                "Puts the magnet on paper and draws round it, so the map can "
                "be repeated.",
                "Places the small compass near one pole and waits for the "
                "needle to settle.",
                "Says each mark records the direction the needle settled to "
                "at that spot.",
                "Moves the compass along so it starts where the last mark "
                "ended, and repeats.",
                "Joins the marks into a smooth line and adds an arrow running "
                "out of the north pole and into the south.",
            ],
            "title": "Rung 3 · Explain"},
        "produce": {
            "q": "Two bar magnets are laid end to end with their north poles "
                 "facing each other, and iron filings are scattered over "
                 "them. There is a small bare patch on the paper between the "
                 "two magnets where no filings settle. Explain what is "
                 "happening there, and say what a compass placed on that "
                 "patch would do.",
            "field_label": "Your answer",
            "placeholder": "Each magnet has its own field, and between them…",
            "success": [
                "Says both magnets produce a field in the gap and the two "
                "fields point in opposite directions there.",
                "Says at one particular point the two are equal in size, so "
                "they cancel exactly.",
                "Says the total field at that point is zero, not merely weak.",
                "Says a filing there has no field to line it up, which is why "
                "the patch is bare.",
                "Says a compass there would not settle to any particular "
                "direction and would stay wherever it is left.",
            ],
            "title": "Rung 4 · Take it somewhere new"},
    },

    "key_note": "The field is the region around a magnet where a magnet or a "
                "magnetic material would feel a force, and it exists whether "
                "or not anything is there to feel it. You plot it with a "
                "small compass: the needle settles along the field at that "
                "point, and joining those directions up gives a field line. "
                "Outside the magnet the lines run out of the north pole and "
                "into the south. Where they crowd, the field is strong; where "
                "they spread, it is weak; and they never cross, because a "
                "compass cannot point two ways at once.",

    "stretch": [
        {"id": "the-neutral-point",
         "type": "explainer",
         "text": "Put two north poles facing each other and somewhere between "
                 "them is a point where the two fields cancel exactly. A "
                 "compass there has nothing to turn it and will sit wherever "
                 "you leave it. Iron filings show the same thing as a bare "
                 "patch on the paper with lines curving away from it on both "
                 "sides. It is called a neutral point, and it is worth "
                 "noticing because it is a place where the field really is "
                 "zero — which is a different claim from the field being "
                 "weak, and one of very few places in physics where a "
                 "quantity is exactly nothing rather than merely small."},
        {"id": "every-line-is-a-loop",
         "type": "explainer",
         "text": "The field lines drawn here stop at the ends of the magnet, "
                 "but they do not really stop: inside the magnet they carry "
                 "on from the south pole back round to the north, so every "
                 "line is a closed loop with no beginning and no end. That is "
                 "a genuine difference from an electric field, whose lines "
                 "start on positive charges and finish on negative ones. It "
                 "is the same fact as poles always coming in pairs, seen from "
                 "another angle — you cannot have a loose end of a loop."},
    ],

    "support": [],

    "vocabulary": [
        {"term": "magnetic field",
         "definition": "The region around a magnet where another magnet, or a "
                       "piece of iron, steel, nickel or cobalt, would feel a "
                       "force. It is there whether or not anything is in it "
                       "to feel it, and it fills space in three dimensions."},
        {"term": "field line",
         "definition": "A line drawn to show which way a compass needle's "
                       "north-seeking end would point along it. Outside a "
                       "magnet the lines run out of the north pole and into "
                       "the south; crowded lines mean a strong field, and no "
                       "two lines ever cross."},
        {"term": "plotting compass",
         "definition": "A small compass used to measure the direction of a "
                       "field one point at a time. You mark where the needle "
                       "settles, move it along, mark again, and join the "
                       "marks up — and that joined-up line is the drawing."},
        {"term": "neutral point",
         "definition": "A place where two fields point in opposite directions "
                       "and are the same size, so they cancel and the total "
                       "is zero — not weak, zero. A compass there has nothing "
                       "to turn it and stays wherever it is left."},
    ],

    "tutor": {
        "anchor": "s-bench",
        "prompt": "Ask Mr Badmus AI",
        "body": "Stuck on which way the arrows go on a field line?",
        "cta": "Ask about this lesson"},

    "ks4_becomes": "Magnetic flux density measured in tesla, the field round "
                   "a current-carrying wire and a solenoid, and field maps "
                   "used to work out the force on a conductor.",

    "convention_note": "The bench is a teaching model. Each bar magnet is "
                       "treated as a pair of point poles at its two ends, "
                       "which is the standard way of constructing a field map "
                       "by hand and gives the right shape everywhere except "
                       "very close to the metal, where a real magnet's field "
                       "is set by the whole body rather than by its ends. The "
                       "Earth's own field is left out, so the readings show "
                       "only what the magnets on the paper do; a real "
                       "plotting compass adds the Earth's field to them and "
                       "points somewhere between. Strength is given as a "
                       "relative figure with the strongest spot the compass "
                       "can be put on this map set to 100, and no value in "
                       "tesla is given because that unit is beyond this "
                       "stage. The arrows drawn across the paper are clamped "
                       "to a shortest and a longest length, so the crowded "
                       "regions and the empty ones are both readable rather "
                       "than drawn to scale. Bearings are clockwise from the "
                       "top of the page and are rounded to the nearest "
                       "degree.",

    "ws": ["measurement", "analysis"],
}
