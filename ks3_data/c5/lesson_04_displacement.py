"""C5 L4 — Displacement (PROCESS).

Authored against Claude Design's approved page,
`docs/ks3/design-reference/c5/c5-04-displacement.dc.html` (727 lines), and her
author's notes `docs/ks3/design-reference/c5/NOTES-C5.md` §1, §2, §3, §4
flags 16 and 17, §5 (`REACT-16`, `REACT-17`), §6 and §7.

Every student-facing string is byte-identical to the approved page. `RAIL`,
`METALS`, `SERIES`, `USES`, `RUNGS` and `SELF_RUNGS` came out of the node
extractor; the hook options and reveal, both explainer paragraphs, the whole of
`#s-series` (eyebrow, heading and its two paragraphs), the grid's lede, every
cell template, the pattern panel's four paragraphs, the key fact, the
`#s-think` options and its two reveal paragraphs, the key note and both "Going
further" paragraphs were lifted from `lessonVals(s)` and from the markup, which
is where most of this lesson's words live and where a lift of the top-level
constants alone loses them.

Where a string is NOT Design's it is marked ⊕ at the point it appears, with the
reason. There are eight such places and they are all in the report.

── THE GRID IS ONE PAYLOAD AND SIXTEEN GENERATED CELLS ─────────────────

NOTES §3: `reactivity-grid` "is the one worth building properly … Every cell's
observation text is **generated** from the two metals' data, so adding a fifth
metal is a one-line change. C8 `patterns-in-reactions` and C9
`the-reactivity-series` both want it with more rows."

So `_METALS` below is the whole of the bench, and NOT ONE CELL'S SENTENCE IS
WRITTEN OUT. `templates` carries the six observation shapes; the renderer fills
them for all sixteen pairs at build time and emits every one, showing the cell
the page opens on (EMIT-BOTH-SHOW-ONE). The wiring composes nothing at all.

⚠️ `order` IS DATA AND IS NEVER INFERRED FROM ARRAY POSITION (NOTES §6). C9
adds metals in the MIDDLE of this list, and a renderer that read reactivity off
the index would silently re-rank every existing cell the moment it did.

⚠️ THE DIAGONAL IS PART OF THE STATE SPACE, NOT AN EXCEPTION. A metal in its
own solution is one of the sixteen, it is enumerated like any other pair, and
its panel says why nothing could have happened. §5A forbids special-casing it
away, and Design's own lede says it is "worth running too".

── THE REACTIVITY SERIES IS SHOWN UP FRONT (Mide, 18 Aug 2026) ─────────

NOTES §7, overriding §3's discovery framing: `#s-series` sits BEFORE the grid
and `showSeriesUpFront` defaults true, so the static build always emits it.

⚠️ `#s-series` IS NOT AN INSTRUMENT AND TAKES NO RAIL STOP. It is absent from
Design's own `RAIL` and NOTES §7 gives the reason in as many words: the rail
ticks ACTIVITIES only, so a stop that could never tick is not added. It is
authored from the closed §5.1.1 vocabulary as a `rule` block (Design's eyebrow,
her heading, and her first paragraph as the rule panel's `close`) followed by a
drawn `figure` whose caption is her second paragraph. That is c3-03's own
pattern — a `rule` head over a drawn plate — and it is the only shape in the
closed vocabulary that carries an eyebrow, a heading, prose and a drawing in
that order. The whole section carries NO `data-stage-done`, no family and no
wiring.

⚠️ AND THE COST OF THAT RULING LANDS ON RUNG 4. With the list on the page a
student can complete sixteen predictions by consulting it and never reason from
evidence at all, so rung 4 — place an unknown metal — is now the only place the
DERIVATION is assessed. Its criteria are re-authored below to credit the
reasoning rather than a recalled list; see the ⊕ note there.

⚑ For Mide's science gate, from Design's NOTES §4 — both already ruled:
  * flag 16 — thermite at "around 2500 °C". CONFIRMED. The hedge is kept and
    the paragraph is Design's, whole, in `stretch`.
  * flag 17 — carbon above iron and below aluminium. CORRECT, and wanted here
    as a consequence question. It drives `USES` item 2 and question `h01`, and
    the figure REFUSES TO DRAW a series that contradicts it (`must_sit_above`
    below), so the claim cannot drift out from under the two places that lean
    on it.

⚑ Three science corrections made under §18 standing authority, applied
  everywhere in the lesson and reported:
  1. A COLOURLESS SOLUTION CANNOT FADE. Design's single `why_reacts` sentence
     opens "The {colour} solution fades…", which is true of five of the six
     reacting cells and false of magnesium in zinc sulfate — both solutions
     there are colourless. A second template branches on the data; see
     `templates` below.
  2. The key note said "the solution changes colour as one dissolved metal is
     replaced by another", which the corrected cell then contradicts on the
     same page. §14 forbids a lesson retracting itself, so the key note now
     says colour changes *whenever the two dissolved metals are different
     colours*.
  3. "that is the rule from two lessons ago" is cut from the `#s-think`
     reveal. It is a §14 sequence claim (a school teaches these units in its
     own order), and it is also simply wrong — the rule it points at is in the
     reactions unit, not two lessons back. The rule is now STATED instead of
     dated, which is what it was doing there for.

── Where the misconception joins land (MRB-244 / MRB-248) ──────────────

Both resolve against markup this page really emits, and both were checked
against the renderer rather than against NOTES:

  REACT-16  elicited_by / confronted_by → `think-commit-nail`, emitted as
            `data-activity="think-commit-nail"` on the `#s-think` section.
            NOTES §5 proposes `think-commit-nail` / `think-reveal-solution`,
            and the register's own note under REACT says why the second cannot
            resolve from inside a content lane: `build_ks3.py` emits a
            confrontation's reveal as `<div class="ks3-reveal
            ks3-reveal-panel" hidden data-reveal>` with NO `id`, so there is no
            name to point at. This names the ACTIVITY that owns BOTH the
            commitment and the reveal, exactly as C4 did three times over, and
            it is a real activity id, so Law 3 is satisfied here.

  REACT-17  elicited_by `grid-predict`, confronted_by `grid-reveal` — both
            `id="…"` emitted by `r_reactivity_grid`. `grid-reveal` is NOTES'
            own proposed name and it resolves because THIS reveal is drawn by
            the unit's own renderer rather than by the generic engine panel, so
            it can carry an id. ⚖️ ONE RENAME, AND IT IS REPORTED: NOTES
            proposes `grid-lower-cells` for the elicitation. The lower cells
            are six buttons scattered under the diagonal and are not one
            element, and the commitment is not made on the cell at all — it is
            made on the predict row, which is where a student says "a reaction
            happens" about a pair that cannot give one. `grid-predict` names
            that row. Same reconciliation as c4-03's `think-commit-arrow`.
"""

# ── the bench (Design's `METALS`) ───────────────────────────────────────
#
# ONE object, read by the grid instrument for the table, all sixteen cell
# panels, the pattern panel's computed order line and tally, AND by the
# reactivity-series figure, which refuses to draw a list that puts these four
# in a different order from the one their `order` claims. So the drawing and
# the sixteen tubes cannot come apart.
#
# ⚠️ `order` is the reactivity rank and it is DATA (NOTES §6). Nothing anywhere
# reads reactivity off the position in this list.
#
# `solColour` / `solution` / `deposit` are Design's keys, snake-cased; they are
# payload names, not student-facing strings, and every sentence built from them
# is in `templates` below.
_METALS = [
    {"id": "mg", "name": "Magnesium", "order": 0,
     "solution": "magnesium sulfate", "sol_colour": "colourless",
     "deposit": "silvery-grey magnesium"},
    {"id": "zn", "name": "Zinc", "order": 1,
     "solution": "zinc sulfate", "sol_colour": "colourless",
     "deposit": "grey zinc"},
    {"id": "fe", "name": "Iron", "order": 2,
     "solution": "iron sulfate", "sol_colour": "pale green",
     "deposit": "dark grey iron"},
    {"id": "cu", "name": "Copper", "order": 3,
     "solution": "copper sulfate", "sol_colour": "blue",
     "deposit": "orange-brown copper"},
]

# ── the reference list (Design's `SERIES`) ──────────────────────────────
#
# The full KS3 twelve, potassium down to gold. Carbon and hydrogen are in it
# because they displace on the same rule — that is the whole reason `non_metal`
# exists as a flag rather than the rows simply being omitted, and it is what
# makes flag 17's consequence question askable at all.
_SERIES = [
    {"name": "Potassium", "symbol": "K"},
    {"name": "Sodium", "symbol": "Na"},
    {"name": "Calcium", "symbol": "Ca"},
    {"name": "Magnesium", "symbol": "Mg", "bench": True},
    {"name": "Aluminium", "symbol": "Al"},
    {"name": "Carbon", "symbol": "C", "non_metal": True},
    {"name": "Zinc", "symbol": "Zn", "bench": True},
    {"name": "Iron", "symbol": "Fe", "bench": True},
    {"name": "Hydrogen", "symbol": "H", "non_metal": True},
    {"name": "Copper", "symbol": "Cu", "bench": True},
    {"name": "Silver", "symbol": "Ag"},
    {"name": "Gold", "symbol": "Au"},
]

# Design's own eyebrow and heading for `#s-series`. Held as constants because
# they are needed in TWO places and must never come apart: the `rule` block
# that renders the head, and the figure's `title`, so the drawing announces
# itself with the same words the section does.
_SERIES_EYEBROW = "Reference · keep this one open"
_SERIES_HEADING = "The reactivity series"

LESSON = {
    # ── identity ────────────────────────────────────────────────────────────
    # Matches ks3_data/structure.py line 219 character for character.
    "slug":        "displacement",
    "title":       "Displacement",
    "discipline":  "chemistry",
    "unit":        "types-of-reaction",
    "family":      "PROCESS",

    # ── curriculum position ─────────────────────────────────────────────────
    # NOTES §1: `KS3.C.CR.03` names four reaction types in one bullet and this
    # unit gives each a lesson. Clause `d` is displacement and is already
    # minted in `ks3_data/substatements.py` with its reasoning; it is not
    # re-minted and not edited here.
    "covers":      ["KS3.C.CR.03d"],
    "touches":     [],
    "beyond_statutory": False,
    "threads":     [{"id": "substances-and-reactions", "level": 4},
                    {"id": "particles", "level": 1}],
    "typical_year": 8,
    "typical_minutes": 55,

    # ── progression edges ───────────────────────────────────────────────────
    # The page's "Before this lesson" card links to oxidation. `references`
    # names the rearrangement lesson because the `#s-think` reveal leans on its
    # rule — iron atoms do not become copper atoms — and now STATES that rule
    # rather than dating it (see the docstring, correction 3).
    "requires":    ["oxidation"],
    "assumes":     [],
    "references":  ["reactions-rearrange-atoms"],
    "connects_heading": "Next in this unit",
    "ks4_links":   [],

    # ── framing ─────────────────────────────────────────────────────────────
    "big_question": "An iron nail in blue solution comes out plated with "
                    "copper. Two metals swapped places — and which way round "
                    "they swap is never a matter of chance.",

    # ── the progress rail (§4.8.1 A) ────────────────────────────────────────
    # Five stops, Design's `RAIL` in her order with her ids and her shorts.
    # `done_when` restates her own `DONE()` (page line 463): the hook on a
    # commitment, the grid at twelve of the sixteen cells run, the consequences
    # when all three are decided, `#s-think` on a commitment, the ladder when
    # every rung is answered and both self-marked rungs checked.
    #
    # ⚠️ `#s-series` IS DELIBERATELY ABSENT. It is a reference block, it is
    # absent from Design's `RAIL`, and NOTES §7 rules it: a stop that could
    # never tick is not added. Four is the floor and this clears it at five.
    "rail": [
        {"anchor": "s-hook",   "short": "HOOK",
         "label": "The plated nail", "done_when": "committed"},
        {"anchor": "s-grid",   "short": "GRID",
         "label": "Sixteen tubes", "done_when": "twelve_cells_run"},
        {"anchor": "s-uses",   "short": "USES",
         "label": "Three consequences", "done_when": "all_uses_decided"},
        {"anchor": "s-think",  "short": "THINK",
         "label": "Where the copper came from", "done_when": "committed"},
        {"anchor": "s-ladder", "short": "LADDER",
         "label": "Mastery ladder", "done_when": "ladder_complete"},
    ],

    # ── the hook (Law 1) ────────────────────────────────────────────────────
    # `kind` is unread by the generator and is authored for consistency.
    #
    # ⚑ MRB-177, measured: the four options are 8 / 10 / 9 / 6 words. The
    # correct option is longest by ONE word at 1.11×, which clears both
    # thresholds, so nothing here was touched.
    "phenomenon": {
        "kind": "narrative",
        "title": "Leave an iron nail in blue copper sulfate. Come back to a "
                 "copper-plated nail and a pale green solution.",
        "prompt": "Nothing was added and nothing was heated. The nail is now "
                  "furry and orange-brown. The blue has drained out of the "
                  "solution and been replaced by a faint green. Weigh the "
                  "nail: it has gained mass.",
        "commit": "Where did the copper on the nail come from?",
        "options": [
            "The iron turned into copper on the surface",
            "It came out of the solution, where it was dissolved",
            "It was already on the nail under the grey",
            "The blue colour became solid copper",
        ],
        "reveal": "Out of the solution. The copper was dissolved in it all "
                  "along — that is what made it blue — and the iron has "
                  "<strong>taken its place</strong>, pushing the copper out as "
                  "solid metal and dissolving in its stead. The green is iron "
                  "sulfate, which was not there before. Two metals swapped "
                  "positions, and the more reactive one won.",
    },

    # ── misconceptions (Law 3) ──────────────────────────────────────────────
    # ⚠️ `REACT-16`'s `statement` is the PAGE's quoted line (page line 241),
    # not NOTES §5's shorter register handle ("The displaced metal came out of
    # the metal you added."). `r_confrontation` prints `statement` as the
    # `#s-think` quote and Design's line is the one that must render — the same
    # reconciliation c3-03 made for MIX-06 and c4-03 for REACT-05. `REACT-17`
    # is not quoted anywhere on the page, so it keeps the register's wording.
    #
    # Both joins, and the one rename, are set out in the module docstring.
    "misconceptions": [
        {"id": "REACT-16",
         "statement": "The copper on the nail came out of the nail — the iron "
                      "turned into copper on the outside.",
         "elicited_by": "think-commit-nail",
         "confronted_by": "think-commit-nail"},
        {"id": "REACT-17",
         "statement": "A less reactive metal will displace a more reactive "
                      "one if you heat it or wait longer.",
         "elicited_by": "grid-predict",
         "confronted_by": "grid-reveal"},
    ],

    # ── core, in the approved page's document order ─────────────────────────
    "core": [
        {"type": "hook", "ref": "phenomenon", "anchor": "s-hook"},

        # Page lines 106-107. Two paragraphs, two blocks: the second is the
        # turn the whole lesson makes — displacement as an INSTRUMENT — and
        # running it into the definition would bury it.
        {"type": "explainer",
         "text": "A <strong>displacement</strong> reaction is one metal taking "
                 "the place of another in its compound. It happens in one "
                 "direction only: a <strong>more reactive</strong> metal "
                 "displaces a <strong>less reactive</strong> one, and never "
                 "the other way round."},
        {"type": "explainer",
         "text": "Which means displacement is also a measuring instrument. Put "
                 "every metal into every other metal's solution and the "
                 "results put them in order of reactivity — an order nobody "
                 "had to be told."},

        # ── #s-series — THE REFERENCE BLOCK. No family, no stop, no wiring.
        # Design's eyebrow, her heading and her first paragraph. The anchor
        # sits here because this is where her section begins.
        {"type": "rule", "anchor": "s-series",
         "eyebrow": _SERIES_EYEBROW,
         "statement": _SERIES_HEADING,
         "close": "Most reactive at the top, least reactive at the bottom. A "
                  "metal higher in this list will displace any metal below "
                  "it, and will never be displaced by one below it. The four "
                  "metals on the bench below are marked — and two non-metals "
                  "are in the list because they take part in exactly the same "
                  "way."},
        {"type": "figure", "ref": "reactivity-series"},

        # ── #s-grid — the flagship. Light `ks3-block` → `check`.
        #
        # ⚠️ The activity id is `grid-sixteen` and not the anchor, so that
        # `#s-grid` stays the SECTION name the rail points at while the
        # instrument has a name of its own. REACT-17 names two ids INSIDE it
        # (`grid-predict`, `grid-reveal`), both emitted by the renderer.
        {"type": "reactivity-grid", "id": "grid-sixteen", "anchor": "s-grid",
         "eyebrow": "Your turn · sixteen combinations",
         "heading": "Four metals, four solutions. Pick a cell, predict, then "
                    "run it.",
         "demand": "investigate",
         # ⊕ Design draws ONE paragraph here: "{n} of 16 run. The four cells
         # down the diagonal…". The seam is re-authored AT A SENTENCE BOUNDARY,
         # never as a raw string cut (§5A): the live count sentence goes to the
         # block's head-row readout, which is where every live count in the key
         # stage goes, and the standing instruction stays as the block's lede.
         # Neither half is reworded and no word is lost.
         "prompt": "The four cells down the diagonal put a metal in its own "
                   "solution, and they are worth running too — a test that "
                   "cannot give a result is still worth having done once.",
         # ⚠️ `total` IS AUTHORED AND THEN CHECKED, rather than derived. The
         # shell reads this counter BEFORE the instrument's renderer runs, so a
         # `KIND_HEAD_TOTAL` derivation would put the number somewhere the
         # instrument's own guard could not see it — and a missing derivation
         # is silent: the counter simply ships as "0 of 0 run", which is a
         # wrong number in the bytes that every other gate reads as a rendered
         # page and passes. So it is written here, beside the metals it counts,
         # and `r_reactivity_grid` refuses to draw a grid whose denominator is
         # not its own number of cells.
         "head_counter": {"format": "{n} of {total} run", "start": 0,
                          "total": 16},

         "metals": _METALS,
         # The cell the page opens on, and Design's own opening state
         # (`metal: 'fe', sol: 'cu'`). The RESTING DOM is this cell selected,
         # nothing run, the counter at zero and the stop unticked.
         "open_at": {"metal": "fe", "sol": "cu"},
         # Design's `DONE` and her `patternOpen` are the same number, so it is
         # authored once. Twelve of sixteen; the renderer refuses a threshold
         # larger than the grid.
         "done_at": 12,

         "column_head": "Metal added to",
         # The three states a cell can be in. `mark` is what is printed in the
         # button; `say` is the same state as a screen reader hears it, and the
         # two are separate elements in the button rather than one `aria-label`
         # the wiring would have to rewrite — a label composed in JS is a
         # sentence in an attribute, which §9 forbids.
         "states": {
             "unrun":  {"mark": "?",      "say": "not yet run"},
             "reacts": {"mark": "reacts", "say": "reaction"},
             "none":   {"mark": "none",   "say": "no reaction"},
         },
         "cell_label": "{Metal} in {solution}",

         "predict": {
             "prompt": "Predict before you run it.",
             "options": [
                 {"id": "yes", "label": "A reaction happens"},
                 {"id": "no", "label": "Nothing happens"},
             ]},

         # ── THE SIXTEEN CELLS, AS SIX SHAPES ───────────────────────────
         #
         # Not one cell's sentence is written out anywhere. The renderer fills
         # these for every pair at build time and emits all sixteen.
         #
         # Placeholders: `{Metal}` / `{metal}` the metal added, as written and
         # lower-cased; `{Other}` / `{other}` the metal in the solution;
         # `{solution}` the solution it is in; `{own_solution}` the solution
         # the added metal makes; `{colour}` the solution's colour; `{Deposit}`
         # the solid that appears, capitalised.
         #
         # ⚑ SCIENCE, corrected under §18 — `why_reacts_colourless`. Design
         # has one reacting sentence and it opens "The {colour} solution
         # fades". That is true of five of the six reacting cells and FALSE of
         # magnesium in zinc sulfate: both solutions are colourless and nothing
         # fades. The branch is on the DATA, not on the cell — a payload where
         # the added metal's own solution is coloured and the one it is put
         # into is not would need a third shape, and the renderer says so
         # loudly rather than printing a false sentence.
         "templates": {
             "title": "{Metal} in {solution}",
             "setup_same": "A piece of {metal} in a {colour} solution of its "
                           "own sulfate.",
             "setup_other": "A piece of {metal} in a {colour} solution of "
                            "{solution}.",

             "result_same": "Nothing, and nothing could have happened.",
             "result_reacts": "A reaction. {Deposit} appears on the metal.",
             "result_none": "Nothing, after twenty minutes and after a week.",

             "why_same": "The metal and the dissolved metal are the same "
                         "element, so there is nobody to displace. Blank "
                         "cells down the diagonal are not failed experiments; "
                         "they are the shape of the question.",
             "why_reacts": "The {colour} solution fades as the {metal} "
                           "dissolves in place of the {other}, and the "
                           "mixture warms slightly. {Metal} is more reactive "
                           "than {other}, so it takes its place.",
             "why_reacts_colourless": "There is no colour to watch — "
                                      "{own_solution} is as colourless as "
                                      "{solution} — but the {metal} dissolves "
                                      "in place of the {other} and the "
                                      "mixture warms slightly. {Metal} is "
                                      "more reactive than {other}, so it "
                                      "takes its place.",
             "why_none": "{Metal} is less reactive than {other}, so it cannot "
                         "push it out of its compound. No amount of waiting, "
                         "warming or stirring changes that — the reaction has "
                         "no way to run.",

             "eq_left": "{metal} + {solution}",
             "eq_right": "{own_solution} + {other}",
         },

         # ── the payoff, and every figure in it COMPUTED ─────────────────
         #
         # §5A forbids hard-coding a figure the instrument computes, and this
         # panel is nothing but figures: how many metals, how many tubes, which
         # order they came out in, and how many each one displaced. Every one
         # of them is filled from `_METALS` at build time, so Design's exact
         # sentences are reproduced today and a fifth metal rewrites them.
         #
         # ⭐ `compare` IS THE PARAGRAPH MIDE RULED (NOTES §7). It used to say
         # "You did not look this up", which is false now the list is on the
         # page. Design has already made the change; this is her new wording
         # and it is not reverted.
         "pattern": {
             "title": "Now look at the shape of the table.",
             "shape": "Every reaction is on one side of the diagonal and "
                      "every blank is on the other. That is not a coincidence "
                      "about these {count} metals — it is what an "
                      "<strong>order</strong> looks like when you draw it as "
                      "a grid. Read the rows: {rows}.",
             "row": "{metal} displaced {tally}",
             "rows_join": ", ",
             "tally_all": "everything",
             "tally_none": "nothing",
             "order": "{order} — most reactive to least",
             "order_join": " · ",
             "compare": "Compare that with the reference list above: your "
                        "{count} metals sit in exactly that order. The list "
                        "is not something to be believed — {cells} test tubes "
                        "have just reproduced the part of it you can reach, "
                        "and the same method extended down the list is where "
                        "the whole of it came from.",
         }},

        {"type": "key-fact", "ref": "which-metal-wins"},

        # ── #s-uses — three consequences. Light `ks3-block` → `check`.
        {"type": "reactivity-use", "id": "uses-three", "anchor": "s-uses",
         "eyebrow": "Three consequences",
         "heading": "One rule, three places it decides the answer",
         "demand": "explain",
         # Two options, and the pair IS the question on every card, so there is
         # no lettered list and no §13 length gate to clear. `correct` reaches
         # NO markup — R3 reserves marking for the ladder — and is read once,
         # at build time, as a guard that the answer paragraph opens with the
         # word the card was decided by. See `r_reactivity_use`.
         "options": [{"id": "yes", "label": "Yes"},
                     {"id": "no", "label": "No"}],
         "uses": [
             {"id": "u1",
              "q": "A works stores copper sulfate solution. Would a "
                   "galvanised steel tank do the job?",
              "correct": "no",
              "answer": "No. Zinc and iron are both more reactive than "
                        "copper, so the tank itself would displace copper out "
                        "of the solution — plating the tank, weakening it, "
                        "and ruining the solution. Copper sulfate is stored "
                        "in plastic or glass."},
             # ⚑ Science flag 17 lives here, RULED CORRECT and kept: carbon
             # above iron and below aluminium. It is C9's content arriving
             # early and it is wanted, because it is the reason iron is smelted
             # with carbon and aluminium cannot be. The figure asserts the same
             # two orderings, so this answer cannot outlive the drawing.
             {"id": "u2",
              "q": "Iron is obtained from iron oxide by heating it with "
                   "carbon in a blast furnace. Would the same trick get "
                   "aluminium out of aluminium oxide?",
              "correct": "no",
              "answer": "No. Carbon can displace iron because carbon sits "
                        "above iron in the reactivity order — but aluminium "
                        "is above carbon, so carbon cannot displace it. "
                        "Aluminium needs electricity, which is why it was the "
                        "last common metal to be discovered."},
             {"id": "u3",
              "q": "An unknown metal X is put into copper sulfate and copper "
                   "appears. It is then put into magnesium sulfate and "
                   "nothing happens. Can you place X in the order?",
              "correct": "yes",
              "answer": "Yes — between the two. X displaced copper, so it is "
                        "above copper. It failed to displace magnesium, so it "
                        "is below magnesium. Two tubes and X is bracketed, "
                        "which is exactly how the reactivity series was "
                        "assembled."},
         ]},

        {"type": "misconception", "id": "think-commit-nail",
         "anchor": "s-think", "targets": "REACT-16"},
        {"type": "quiz", "ref": "ladder", "anchor": "s-ladder"},
        {"type": "summary", "ref": "key_note"},
    ],

    # ── the figure (§5.4) ───────────────────────────────────────────────────
    # Design draws the series as a DOM list beside an arrow. Drawn here as one
    # inline SVG plate because that is what a `figure` is and because it keeps
    # the twelve rows, the four bench marks and the two non-metal notes in ONE
    # object that the drawer can walk and check.
    #
    # ⚠️ `desc` IS COMPOSED BY THE DRAWER from what is actually drawn, and
    # overrides this key on every build (MRB-254). This one is kept short and
    # true as the fallback any future non-drawing path would take.
    #
    # ⚖️ THE CONTENT-TRUTH ASSERTIONS ARE THE POINT OF DRAWING IT HERE. The
    # drawer walks EVERY row, not a sample, and refuses to draw:
    #   · a row with no name or no symbol;
    #   · a `bench` row naming a metal the grid does not have, or a grid metal
    #     that is not marked on the list;
    #   · a list whose four bench metals do not fall in their `order` — the
    #     drawing's own label says "most reactive at the top", and a plate that
    #     contradicts the sixteen tubes below it is worse than no plate;
    #   · a list that breaks any pair in `must_sit_above`.
    "figures": [
        {"id": "reactivity-series",
         "kind": "diagram",
         "status": "drawn",
         "art": "reactivity-series",
         "title": _SERIES_HEADING,
         "desc": "A numbered list of twelve substances in order of "
                 "reactivity, most reactive at the top, with an arrow beside "
                 "it pointing down the list. Carbon and hydrogen are marked "
                 "as non-metals; magnesium, zinc, iron and copper are "
                 "highlighted as the four on the bench.",
         # Design's own closing paragraph, whole. It sits directly under the
         # list and describes exactly what the list is, so it is the figure's
         # caption rather than a separate explainer.
         "caption": "Nobody was told this order. It was assembled by doing "
                    "what you are about to do — putting metals into each "
                    "other's solutions and recording which way the swap went. "
                    "The bench below covers four of these twelve; the same "
                    "method extended down the list produces the rest of it.",
         "data": {
             "series": _SERIES,
             "bench": _METALS,
             "note": "non-metal",
             # Design's two mono captions on the arrow column, at her own
             # wording. They are drawn on two lines each because a 148px column
             # wraps them and SVG text does not.
             "top": "Most reactive at the top",
             "bottom": "Least reactive at the bottom",
             # ⚑ Science flag 17, as an assertion rather than as a hope. These
             # are the order claims the PAGE'S OWN PROSE depends on: `USES`
             # item 2 and question `h01` both argue from carbon sitting between
             # aluminium and iron. If the list is ever edited so that it does
             # not, the build stops here rather than shipping two paragraphs
             # arguing from a drawing that contradicts them.
             "must_sit_above": [["Aluminium", "Carbon"],
                                ["Carbon", "Iron"]],
         }},
    ],

    # ── the KEY FACT box (§4.8.1 B) ─────────────────────────────────────────
    "key_facts": [
        {"id": "which-metal-wins",
         "text": "A more reactive metal displaces a less reactive metal from "
                 "its compound — and never the reverse. Which metal wins "
                 "tells you their order of reactivity.",
         "placement": "top-level",
         "ground": "card",
         "eyebrow": "Key fact"},
    ],

    # ── activities (§5.5) ───────────────────────────────────────────────────
    # `#s-think` only. The two instrument blocks are lifted out of `core` into
    # this list by `_normalise()` and are never authored here.
    #
    # ⚑ MRB-177, measured and FIXED AT THE DISTRACTORS. Design's four options
    # are 7 / 13 / 6 / 7 words: the correct one is strictly longest by six
    # words at 1.86×, and a student could take it without reading the quote.
    # Her B is untouched and the answer stays where it was; A, C and D are
    # re-authored to make the SAME wrong rule in the correct option's own
    # shape — a verdict, then the mechanism it claims. The set now measures
    # 12 / 13 / 13 / 13, so the correct option is no longer strictly longest.
    "activities": [
        {"id": "think-commit-nail",
         "kind": "predict",
         "demand": "explain",
         "targets": "REACT-16",
         "prompt": "The copper is on the nail, and nothing else was put in "
                   "the tube. Commit before you read on.",
         "options": [
             "Right — the iron on the outside of the nail turned into copper",
             "Wrong — the copper came out of the solution, and iron went "
             "into it",
             "Right, because the nail gained mass and only new copper could "
             "add it",
             "Wrong — the copper came out of the water rather than from "
             "anything dissolved",
         ],
         # ⊕ The first sentence is re-authored: Design writes "that is the
         # rule from two lessons ago", which is a §14 sequence claim and is
         # also pointing at the wrong lesson. The rule is now STATED, which is
         # what the clause was there to do. Nothing else in either paragraph
         # moves.
         "reveal": [
             "Iron atoms cannot become copper atoms — reactions rearrange "
             "atoms and never turn one element into another, and no beaker of "
             "blue solution overturns it. The copper came from the solution, "
             "where it was dissolved and invisible. The evidence is the "
             "colour: the blue drained away because the dissolved copper "
             "left, and the new green is dissolved iron that was not there "
             "before.",
             "And the swap is exact. Weigh the nail and the mass gained is "
             "copper deposited; weigh what is left and iron has gone into "
             "solution. <strong>Two metals changed places. Neither changed "
             "identity.</strong>",
         ]},
    ],

    # ── the mastery ladder (Law 8, §5.8) ────────────────────────────────────
    # Design's RUNGS → recall + apply, SELF_RUNGS → explain + produce. Her four
    # headings are the engine's own defaults character for character, so no
    # rung authors a `title`. `feedback` is keyed by the INT index of each
    # wrong option, which is what `_rung_marked` reads.
    "ladder": {
        # ⚑ MRB-177, measured and FIXED AT THE DISTRACTORS. Design's set is
        # 15 / 11 / 5 / 8 words: the correct option is strictly longest by
        # FOUR, which is the gate exactly. Nothing about the correct option
        # moved and the answer sat at index 0 when this was written — MRB-278
        # moved it to index 1 on 21 Aug 2026 without retyping a word; the three distractors were
        # lengthened into the correct option's own shape and each still states
        # the same wrong rule, so its correction still lands. The set now
        # measures 15 / 15 / 12 / 13.
        "recall": {
            "q": "What happens in a displacement reaction?",
            "options": [
                "A less reactive metal takes the place of a more reactive "
                "metal in its compound",
                "A more reactive metal takes the place of a less reactive "
                "metal in its compound",
                "Two compounds swap the metals in them, so both reactants "
                "are compounds",
                "A metal is broken down into the simpler substances it is "
                "made of",
            ],
            "answer": 1,
            "feedback": {
                0: "It only runs one way. A less reactive metal cannot push "
                   "out a more reactive one — that is what makes the grid "
                   "half empty.",
                2: "One of the reactants is a metal on its own. It is the "
                   "metal that does the displacing.",
                3: "A metal is an element and cannot be broken down. "
                   "Displacement swaps partners; it does not split anything.",
            }},
        # ⚑ REACT-17, marked. This is the rung the "heat it or wait longer"
        # belief is caught by, and two of its three distractors are that belief
        # in its two commonest disguises.
        #
        # ⚑ MRB-177, measured: 11 / 13 / 13 / 16 words. The correct option is
        # the SHORTEST, so there is no tell and nothing was touched.
        "apply": {
            "q": "A copper wire is left in zinc sulfate solution for a week "
                 "and nothing happens. What does that tell you?",
            "options": [
                "A dilute solution reacts slowly, so a stronger one would "
                "show the reaction",
                "Copper takes no part in displacement, so it never reacts "
                "with a salt solution",
                "Heating speeds up any reaction, so warming the tube would "
                "make the copper displace the zinc",
                "Copper is less reactive than zinc, so it cannot displace it",
            ],
            "answer": 3,
            "feedback": {
                0: "Concentration changes the speed of a reaction that can "
                   "happen. This one cannot happen at all.",
                1: "Copper is displaced by zinc, iron and magnesium. It takes "
                   "part constantly — always on the losing side.",
                2: "Heat speeds reactions up; it does not reverse the "
                   "reactivity order. Zinc stays above copper at every "
                   "temperature.",
            }},
        # Design's criteria, with the two mangled possessives restored —
        # "that solution s metal" is "that solution's metal", and the apostrophe
        # was lost on the way through the extractor, not authored away.
        "explain": {
            "q": "An iron nail is left in blue copper sulfate solution. "
                 "Describe everything you would observe, and explain each "
                 "observation in terms of which metal is where.",
            "field_label": "Your explanation",
            "placeholder": "The nail becomes coated with…",
            "success": [
                "Says an orange-brown coating of copper forms on the nail.",
                "Says the blue colour fades, because the dissolved copper is "
                "leaving the solution.",
                "Says the solution becomes pale green, because iron sulfate "
                "has formed.",
                "Says iron is more reactive than copper, which is why it can "
                "take its place.",
                "Says the copper came from the solution and not from the "
                "nail.",
            ]},
        # ⭐ RUNG 4 IS NOW THE ONLY PLACE THE DERIVATION IS ASSESSED, and the
        # criteria are re-authored for it. NOTES §7 flags exactly this: with
        # the reactivity series printed above, a student can complete sixteen
        # predictions by consulting it and never reason from evidence — so the
        # one rung that cannot be answered from the list has to be the one that
        # tests the reasoning.
        #
        # The unknown metal is not on the list, by construction. Design's
        # QUESTION already asks for "the smallest set of tests" and "how you
        # would know when you had finished", so it is kept byte-identical; it
        # was her criteria that credited a method rather than an argument.
        # What changed, and why:
        #
        #   · her 1 credited putting the metal "into each solution" — which is
        #     running all four, the opposite of the smallest set the question
        #     asks for. It now credits the fair comparison only.
        #   · her 2 and 3 are the two inference rules and they are KEPT, with
        #     the possessives restored. They are the heart of the derivation.
        #   · her 4 ("explains how the results bracket the metal") is folded
        #     into 5, and 4 now credits WHICH PAIRS TO TEST — choosing the next
        #     solution from the last result instead of running the set blind.
        #     That is the reasoning the printed list cannot supply.
        #   · her 5's stopping rule is KEPT and now carries its reason: why two
        #     results that name neighbours are enough to bracket the metal.
        "produce": {
            "q": "You are given an unknown metal and solutions of magnesium "
                 "sulfate, zinc sulfate, iron sulfate and copper sulfate. "
                 "Design the smallest set of tests that would place the "
                 "unknown metal in the reactivity order, and say how you "
                 "would know when you had finished.",
            "field_label": "Your plan",
            "placeholder": "I would put a piece of the metal into…",
            "success": [
                "Says a piece of the unknown goes into each solution it "
                "tests, using the same amount and the same conditions every "
                "time so the results can be compared.",
                "Says a reaction means the unknown is more reactive than that "
                "solution's metal.",
                "Says no reaction means the unknown is less reactive than "
                "that solution's metal.",
                "Chooses the next solution from the result of the last one "
                "— further up the order after a reaction, further down after "
                "none — instead of running all four.",
                "Says it is finished when the highest metal the unknown "
                "displaces and the lowest it fails to displace are next to "
                "each other, because two results that close leave it nowhere "
                "else to sit.",
            ]},
    },

    # ── the key note (fixed, last, photographable) ──────────────────────────
    # ⚑ SCIENCE, corrected under §18. Design's middle sentence reads "the
    # solution changes colour as one dissolved metal is replaced by another",
    # which the grid contradicts on the same page for magnesium in zinc
    # sulfate — both solutions colourless, nothing to change. §14 forbids a
    # lesson retracting itself later on the same page, so the claim is
    # conditioned on the thing that decides it. Nothing else in the paragraph
    # moves.
    "key_note": "In a displacement reaction a more reactive metal takes the "
                "place of a less reactive metal in its compound, and never "
                "the other way round. The displaced metal appears as a solid, "
                "and the solution changes colour whenever the two dissolved "
                "metals are different colours. Testing every metal against "
                "every solution puts them in order of reactivity — which is "
                "how the reactivity series was built.",

    # ── the stretch layer (§5.6) — visible and opt-in to all ────────────────
    # Design's two "Going further" paragraphs, whole and unedited.
    #
    # ⚑ Science flag 16 is the first paragraph's "around 2500 °C". CONFIRMED
    # and the hedge is kept exactly as she wrote it.
    #
    # The second paragraph is flag 17 again, as history rather than as
    # chemistry: gold and copper found as metals, iron displaced with carbon,
    # aluminium out of reach of any furnace because it is above carbon. It is
    # the same claim `USES` item 2 makes and the same one the figure asserts.
    "stretch": [
        {"type": "explainer", "id": "thermite",
         "text": "Displacement is how railway track is welded in the middle "
                 "of nowhere. A crucible of iron oxide mixed with aluminium "
                 "powder is lit; aluminium is more reactive than iron, so it "
                 "takes the oxygen and the iron is displaced as a white-hot "
                 "liquid that pours straight into the gap between the rails. "
                 "It reaches around 2500 °C, needs no power supply, and is "
                 "the same rule you have just measured with test tubes and a "
                 "wire."},
        {"type": "explainer", "id": "which-metals-came-first",
         "text": "It is also why some metals were known to the ancient world "
                 "and others were not. Gold and copper are unreactive enough "
                 "to be found as the metal, so they were used thousands of "
                 "years before anyone understood chemistry. Iron needs "
                 "displacing from its ore with carbon in a furnace, which is "
                 "a Bronze-Age-ending piece of technology. Aluminium is more "
                 "reactive than carbon, so no furnace will do it — it stayed "
                 "undiscovered until electricity could be used to break the "
                 "ore apart, which is why aluminium was once more valuable "
                 "than silver."},
    ],

    # Present and empty — §5.6's ruling: may be empty, never absent.
    "support": [],

    # ── vocabulary (§10.2) ──────────────────────────────────────────────────
    # ⚠️ The key is `definition`, not `gloss`: build_ks3.py:939 hard-indexes it.
    # No `keyword` block is placed — Design draws none on this page — so these
    # render nowhere today and are authored for the register and the tutor.
    "vocabulary": [
        {"term": "displacement",
         "definition": "A reaction in which a more reactive metal takes the "
                       "place of a less reactive metal in its compound."},
        {"term": "reactivity",
         "definition": "How readily a metal takes part in a reaction. A more "
                       "reactive metal holds on to a partner more strongly "
                       "and gives it up less easily."},
        {"term": "reactivity series",
         "definition": "A list of metals in order of reactivity, most "
                       "reactive first, with carbon and hydrogen included "
                       "because they displace on the same rule.",
         "note": "Nobody was told the order. It was measured."},
        {"term": "sulfate",
         "definition": "The partner in the compounds used on this bench. "
                       "Copper sulfate, iron sulfate and zinc sulfate each "
                       "hold a different metal with the same partner, which "
                       "is what makes them comparable."},
        {"term": "ore",
         "definition": "A rock containing enough of a metal's compound to be "
                       "worth extracting the metal from."},
    ],

    # ── safety (§1.5) — not a callout, and not a safeguarding block ─────────
    # ⊕ NEW PROSE, and the only new prose in this file outside the distractor
    # fixes. §16 rules no safeguarding block here and that is right: this is a
    # substance lesson and it touches nothing about a student's own body,
    # health or risk. A `safety_note` is a different thing, and this lesson
    # earns one for one reason: the "Going further" paragraph describes
    # thermite enthusiastically, by name, with its temperature, and thermite is
    # the one thing on this page a student could try to reproduce and be badly
    # hurt by. The line closes it and answers the question the paragraph
    # provokes, rather than leaving it open.
    #
    # It names no method and no proportions, and it is scoped to thermite
    # alone: a blanket warning about the bench work would be a warning about a
    # practical the page never asks the student to set up.
    "safety_note": "Thermite is an industrial process, not a bench reaction. "
                   "It reaches temperatures no school equipment can hold and "
                   "is never set up in a school laboratory.",

    # ── end matter (§4.8.1 C, D) ────────────────────────────────────────────
    "tutor": {"prompt": "Ask Mr Badmus AI",
              "body": "Still not sure why half the grid is empty?",
              "cta": "Ask about this lesson",
              "anchor": "s-grid"},

    "ks4_becomes": "The reactivity series in full, extracting metals with "
                   "carbon and by electrolysis, and displacement as electron "
                   "transfer.",

    # ── working scientifically (§5.7) ───────────────────────────────────────
    "ws": ["experimental-skills-and-investigations", "analysis-and-evaluation"],

    # ── governance (§5.10) ──────────────────────────────────────────────────
    "review_state": "draft",
}
