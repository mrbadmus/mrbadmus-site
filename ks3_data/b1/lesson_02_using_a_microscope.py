"""B1 L2 — Using a microscope (INVESTIGATION).

Authored against Design's approved page,
`docs/ks3/design-reference/b1/b1-02-using-a-microscope.dc.html`, and its measured
specification, `docs/ks3/b1-inventory/b1-02-using-a-microscope.md`. Schema per
architecture.md §4.8 as amended by §4.8.1 (rail, key_facts, tutor, before_this /
ks4_becomes / safety_note) and §4.8.2 (`activities[].fifa` is a LIST; `phenomenon`
carries `figures`; `figures[]` carries `slot_label`).

This record SUPERSEDES the L2 record in `ks3_data/biology_b1_cells.py`. The two
teach overlapping but different lessons — the old one opens on a bubble-covered
slide ("Why does almost everybody's first slide show nothing at all?"), the
approved page opens on two photographs of the same onion at ×100 and ×400 and
runs critique-the-method → the formula → the bench. Under standing law the
approved page wins, so every student-facing string below is lifted from it.

Every authored string is byte-identical to the approved page. The ONE exception
is deliberate and ruled:

    ⚑ MRB-210 — the ×100 sharpness note is corrected here.
    Design's page says: "At ×100 two layers are nearly sharp together. There is
    still depth to spare." Both halves are false under the ruled depth-of-field
    table `OBJ_DOF_MM = [0.100, 0.040, 0.008]` (shared/ks3.js, an engine constant,
    not a payload field). At ×100 the sharp window is SHARP_FRACTION × dof =
    0.6 × 0.040 = ±0.0240 mm; the onion layers sit 0.055 mm apart, so holding two
    at once needs ±0.0275 mm. Enumerated over all 101 focus-wheel positions with
    the engine's non-parfocal offset (OBJ_FOCUS_SHIFT[1] = 10): the maximum number
    of layers inside the window is 1, at EVERY position — 76 positions hold one,
    25 hold none. The sharp slice is thinner than the gap between the layers,
    which is the opposite of "depth to spare". The line was true on the page's own
    superseded inline table (0.30 / 0.09 / 0.012 mm); it became wrong when the two
    approved microscopes were reconciled onto one instrument. Corrected wording is
    in `sim["resolve_notes"]["100"]` below. ×40 and ×400 are untouched — both survive the
    ruled table (×40 holds all three layers at the lesson's starting focus of 50;
    ×400's window is ±0.0048 mm, ~24× thinner than one 0.115 mm cell).

Keys this record uses that §4.8 does not yet name are listed in the build report
and marked `# NEW` below. Every one sits INSIDE a component Design drew and
supplies words Design put on the page; none invents a component.
"""

# ── the six method steps, the four worked steps, the four fields, the two
#    marked rungs and the two self-marked rungs are lifted byte-identical from
#    the approved page's `<script data-dc-script>` block (source lines 518–616).
#    They are science-bearing and cross the examiner gate as written.

LESSON = {
    # ── identity ────────────────────────────────────────────────────────────
    # Matches ks3_data/structure.py's B1 slot 2 exactly.
    "slug":        "using-a-microscope",
    "title":       "Using a microscope",
    "discipline":  "biology",
    "unit":        "cells-and-organisation",
    "family":      "INVESTIGATION",

    # ── curriculum position ─────────────────────────────────────────────────
    # Unchanged from the superseded record. §5.7.1 requires an INVESTIGATION
    # lesson to anchor on WS, which KS3.WS.EXP.05 does; KS3.B.CELLS.01b is the
    # one subject clause this lesson owns and no other lesson teaches.
    "covers":      ["KS3.WS.EXP.05", "KS3.B.CELLS.01b"],
    "touches":     [],
    "beyond_statutory": False,
    "threads":     [{"id": "cells-and-systems", "level": 1}],
    "typical_year": 7,
    "typical_minutes": 50,

    # ── progression edges ───────────────────────────────────────────────────
    # `requires` is non-empty, so the endmatter's first card renders as a link
    # to L1 — which is exactly what the approved page draws, and why this lesson
    # needs no `before_this`.
    "requires":    ["life-processes"],
    "assumes":     [],
    "references":  [],
    "ks4_links":   ["biology/cell-biology/microscopy"],

    # ── framing ─────────────────────────────────────────────────────────────
    "big_question": "Turn it up to the highest magnification and you see almost "
                    "nothing. Why?",

    # ── the progress rail (§4.8.1 A) ────────────────────────────────────────
    # Six stages. `short` renders in the ≥1340px side rail's mono label, `label`
    # in the sub-1340px top bar; neither is derivable from the block titles.
    # Every `done_when` names state the block already owns — b1-01's F3 (a stage
    # that can never tick) does not recur here.
    #
    # ⚠ `attempt_checked` only means something if the Check button is gated on a
    # non-empty field (inventory §7.5 assert (a), F5). Design's page ticks this
    # stage on four blank boxes; §2.4's validation rule says a stage must not be
    # settable without the student producing something, so the renderer gates it.
    "rail": [
        {"anchor": "s-hook",   "short": "HOOK",   "label": "Two photographs",
         "done_when": "committed"},
        {"anchor": "s-method", "short": "METHOD", "label": "Sam’s method",
         "done_when": "steps_opened"},
        {"anchor": "s-worked", "short": "WATCH",  "label": "Watch it done",
         "done_when": "all_steps_shown"},
        {"anchor": "s-yours",  "short": "YOU",    "label": "Now you",
         "done_when": "attempt_checked"},
        {"anchor": "s-lab",    "short": "BENCH",  "label": "The bench",
         "done_when": "all_rows_recorded"},
        {"anchor": "s-ladder", "short": "LADDER", "label": "Mastery ladder",
         "done_when": "ladder_complete"},
    ],

    # ── the hook (Law 1) ────────────────────────────────────────────────────
    # `options` + `reveal` are NEW inside `phenomenon`: Design draws the four
    # commitment options and the gated reveal INSIDE the hook section, not as a
    # separate activity block. They are a wager, never marked — no `answer` key,
    # deliberately (R3: only the ladder marks). `figures` is §4.8.2's shape.
    "phenomenon": {
        "kind": "data",
        "title": "Same slide. Same microscope. Same person.",
        "prompt": "Two photographs, taken one minute apart, of one piece of "
                  "onion skin. In the first you can count the cells. In the "
                  "second there is a grey smear with one dark curve in it. "
                  "Nothing was changed except the objective lens.",
        "figures": ["b1-onion-epidermis-x100", "b1-onion-epidermis-x400"],
        "commit": "Which objective would you turn in first to find the cells?",
        "options": [                                              # NEW
            "The ×4 — the widest view",
            "The ×10",
            "The ×40 — the most detail",
            "It makes no difference which",
        ],
        "reveal": "Hold that. You will measure it yourself further down, and "     # NEW
                  "the number that settles it is how much of the slide you can "
                  "see at once.",
    },

    # ── figures (§4.10, extended by §4.8.2) ─────────────────────────────────
    # `kind: "micrograph"` follows the shipped precedent and inventory G4; the
    # §4.10 enum needs it adding (it is a live silent gap, nothing validates the
    # enum today). `slot_label` is §4.8.2's: a micrograph is not a diagram, so
    # the pending tag reads "Photo coming soon", and the two figures render on
    # the hook's ink ground as an equal-height 2-up pair.
    "figures": [
        {"id": "b1-onion-epidermis-x100",
         "kind": "micrograph",
         "caption": "Onion epidermis, ×100. Cells countable, edges sharp.",
         "slot_label": "Photo coming soon",
         "status": "needed"},
        {"id": "b1-onion-epidermis-x400",
         "kind": "micrograph",
         "caption": "The same spot, ×400. One cell wall crossing an empty grey "
                    "field.",
         "slot_label": "Photo coming soon",
         "status": "needed"},
    ],

    # ── misconceptions (Law 3) ──────────────────────────────────────────────
    # CELL-02's statement is the approved page's own `.ks3-mis-quote`, verbatim
    # and without its quote marks (the renderer adds them).
    #
    # CELL-01 survives from the superseded record but changes instrument: the
    # approved page confronts bubbles-as-cells in the method critique's step-1
    # verdict ("Bubbles are round, thick and black-edged, and they get drawn as
    # cells every year"), not on a second onion slide. See the F9 note on the
    # lab's `specimens` below.
    "misconceptions": [
        {"id": "CELL-01",
         "statement": "Those neat round circles in the field of view are the "
                      "cells.",
         "elicited_by": "sams-method",
         "confronted_by": "sams-method"},
        {"id": "CELL-02",
         "statement": "The highest magnification always shows you the most.",
         "elicited_by": "microscope-lab",
         "confronted_by": "microscope-lab"},
    ],

    # ── vocabulary (Law 7, required by §4.8) ────────────────────────────────
    # Declared because the field is required and these four terms are the ones
    # the lesson carries. The approved page renders NO keyword block, so `core`
    # holds no `keyword` segment — the terms are taught inside the blocks that
    # use them.
    "vocabulary": [
        {"term": "specimen",
         "definition": "The thing you are looking at under the microscope.",
         "note": "It has to be thin enough for light to get through it. That is "
                 "why onion skin works and a whole onion does not."},
        {"term": "coverslip",
         "definition": "The thin square of glass laid over a specimen.",
         "note": "Lower it slowly, at an angle. Dropping it flat is what traps "
                 "the air bubbles Sam’s method starts with."},
        {"term": "magnification",
         "definition": "How many times bigger than real life something looks.",
         "note": "Total magnification = eyepiece × objective. A ×10 eyepiece "
                 "with a ×40 objective gives ×400."},
        {"term": "field of view",
         "definition": "The circle of the specimen you can see down the "
                       "microscope at one time.",
         "note": "Turn to a higher magnification and the field of view gets "
                 "smaller. You see more detail of less."},
    ],

    # ── core, in the approved page's document order ─────────────────────────
    # 10 blocks → the page's 10 rendered lesson sections. Three of the six rail
    # stages sit inside MRB-204's formula trio (formula → worked → yours).
    #
    # ⊕NEW `anchor`. §4.8.1 A requires every rail `anchor` to name a section the
    # lesson actually emits, and Design's ids are not derivable from a block type
    # or an activity id. All NINE id-bearing sections carry one, not only the six
    # the rail references — `s-formula`, `s-think` and `s-keynote` are anchored
    # too, because a hash link from anywhere else must clear the sticky bar
    # (`scroll-margin-top: 92px`). The KEY FACT box is the one block with no
    # anchor: Design draws it as an unclassed, un-id'd `<div>` between sections.
    "core": [
        {"type": "hook", "ref": "phenomenon", "anchor": "s-hook"},

        # #s-method — the critique instrument. A `check` shell and not
        # `practical`: Design draws it as a light `.ks3-block`, and the
        # `practical` shell is ink-dark.
        {"type": "check", "id": "sams-method", "anchor": "s-method"},

        # #s-formula — ONE section holding TWO independently-shelled panels: the
        # statement and the triangle. MRB-204: "a formula stands alone in its own
        # block, not embedded in a paragraph, not inside a worked example, not
        # sharing a card." Inline in `core`, as b1-01's `rule` block is.
        #
        # Panel 1, the statement: centred with `max-width: none` and its own type
        # ramp, `clamp(26px, 3.6vw, 40px)`. Three measured differences from
        # b1-01's `rule` statement (left-aligned, 20ch, its own clamp), which is
        # why the two shells must not be merged.
        #
        # Panel 2, the triangle. The three cover boxes are NOT authored: they are
        # a function of the fixed 260×216 viewBox and the dividers at y=130 and
        # x=130 (top box = the upper cell, lower boxes = the halves of the lower
        # cell). Authoring twelve magic numbers per lesson is the hand-authoring
        # the generator removes, and it is what produced Design's four console
        # errors. `top` is the numerator and the default cover state; there is no
        # uncovered state, so the triangle is only ever taught covered.
        {"type": "formula", "anchor": "s-formula",
         "statement": "total magnification = eyepiece × objective",
         "triangle": {
             "eyebrow": "The triangle",
             "heading": "Cover the one you want",
             "aria_label": "Formula triangle: total magnification on top, "
                           "eyepiece and objective below",
             "top": {
                 "label": "total",
                 "button": "Cover total",
                 "text": "Total is on its own at the top, with the other two "
                         "side by side underneath. Cover it and you are left "
                         "with eyepiece × objective — multiply."},
             "left": {
                 "label": "eye",
                 "button": "Cover eyepiece",
                 "text": "Cover the eyepiece and you are left with total over "
                         "objective. Divide the total by the objective."},
             "right": {
                 "label": "obj",
                 "button": "Cover objective",
                 "text": "Cover the objective and you are left with total over "
                         "eyepiece. Divide the total by the eyepiece."},
             "close": "Two things side by side means multiply. One thing over "
                      "another means divide.",
         }},

        # the KEY FACT box — a direct child of .ks3-lesson, between two sections
        {"type": "key-fact", "ref": "multiply-never-add"},

        {"type": "worked-example", "id": "magnification-fifa",
         "anchor": "s-worked"},
        {"type": "check", "id": "magnification-fifa-do", "anchor": "s-yours"},
        {"type": "practical", "id": "microscope-lab", "anchor": "s-lab"},
        {"type": "misconception", "id": "highest-is-best", "anchor": "s-think",
         "targets": "CELL-02"},
        {"type": "quiz", "ref": "ladder", "anchor": "s-ladder"},
        {"type": "summary", "ref": "key_note", "anchor": "s-keynote"},
    ],

    # ── the KEY FACT box (§4.8.1 B) ─────────────────────────────────────────
    # `--ks3-band` ground per drift 5, never amber. `id` is carried so
    # `placement: "top-level"` has a position: `core` names it in document order.
    "key_facts": [
        {"id": "multiply-never-add",                               # NEW (id)
         "text": "Multiply the two, never add them. ×10 and ×40 give ×400, not "
                 "×50.",
         "placement": "top-level",
         "ground": "band",
         "eyebrow": "Key fact"},
    ],

    # ── activities (§5.5) ───────────────────────────────────────────────────
    "activities": [

        # ── #s-method · the critique instrument (inventory G3, §7.1) ────────
        # INVESTIGATION's spine: lead with a flawed piece of work, critique
        # before construct. A CHECKBOX SET, not a radio group — any number of
        # steps can be picked, and picks stay toggleable after opening.
        # Three of the six steps are faults, which is what the intro claims out
        # loud ("Three of the six steps will cost him") — the two must agree.
        {"id": "sams-method",
         "kind": "critique-steps",
         # §5.5's enum. The demand is to judge someone else's method against
         # what a microscope actually does.
         "demand": "explain",
         # ⊕NEW `eyebrow` + `heading`. Design's shells carry BOTH a scoped
         # eyebrow (not the generator's fixed "Your turn") and an <h2> above the
         # prose; today's `check` shell promotes the prompt itself to the
         # heading, which would lose one of the two lines.
         "eyebrow": "Your turn · judge it first",                  # NEW
         "heading": "Sam’s method",                                # NEW
         "prompt": "Sam wrote this up for a slide of onion skin. Three of the "
                   "six steps will cost him. Tap the ones you would change, "
                   "then open them up.",
         "steps": [                                                # NEW
             {"text": "Put a drop of water on the slide, then drop the "
                      "coverslip straight down onto it.",
              "fault": True,
              "word": "Costs him",
              "verdict": "Dropped flat, it traps air. Bubbles are round, thick "
                         "and black-edged, and they get drawn as cells every "
                         "year. Lower it slowly on one edge instead."},
             {"text": "Clip the slide onto the stage, over the hole in the "
                      "middle.",
              "fault": False,
              "word": "Sound",
              "verdict": "Light has to come up through the specimen, so it must "
                         "sit over the hole."},
             {"text": "Start on the ×40 objective, so there is as much detail "
                      "as possible from the beginning.",
              "fault": True,
              "word": "Costs him",
              "verdict": "That is 0.45 mm of slide in view. He is hunting for "
                         "something the width of a hair in the dark. Start on "
                         "×4, where he can see 4.5 mm at once."},
             {"text": "Look down the eyepiece and turn the coarse focus so the "
                      "objective comes down towards the slide.",
              "fault": True,
              "word": "Costs him",
              "verdict": "From the eyepiece he cannot see the gap closing. "
                         "Watch from the side, bring it down until it nearly "
                         "touches, then focus by moving it away."},
             {"text": "Draw what he sees in pencil, in clear single lines, with "
                      "no shading.",
              "fault": False,
              "word": "Sound",
              "verdict": "A biological drawing is a record, not a picture. "
                         "Single lines, no shading, no colouring in."},
             {"text": "Write the magnification he used next to the drawing.",
              "fault": False,
              "word": "Sound",
              "verdict": "Without it the drawing says nothing about size, and "
                         "no one can repeat what he did."},
         ],
         "reveal_label": "Open the steps I picked",                # NEW
         "progress_zero": "Pick at least one",                     # NEW
         "targets": "CELL-01"},

        # ── #s-worked · the staged FIFA worked example (G8, §7.4) ───────────
        # MRB-204 step 3 and §4.8.2's breaking change: `fifa` is a LIST of
        # {letter, name, line, note}, revealed one step at a time, not a dict of
        # four flat strings shown at once. The <h2> IS the question.
        # Law 5's pair is `magnification-fifa-do` below; the letters of the two
        # must match in order (F · I · F · A) and they do.
        {"id": "magnification-fifa",
         "kind": "worked-example",
         "demand": "apply",
         "eyebrow": "Watch it done · one step at a time",          # NEW
         # The <h2> IS the question here, and there is no prose under it — so
         # this block carries a `heading` and no `prompt`.
         "heading": "Riya’s eyepiece says ×10. The objective clicked into "     # NEW
                    "place says ×40. Calculate the total magnification.",
         "staged": True,                                           # NEW
         "fifa": [                                                 # LIST, §4.8.2
             {"letter": "F",
              "name": "Formula",
              "line": "total magnification = eyepiece × objective",
              "note": "Written down before any numbers. That is what stops the "
                      "next step going wrong."},
             {"letter": "I",
              "name": "Insert",
              "line": "total magnification = 10 × 40",
              "note": "Eyepiece where eyepiece goes, objective where objective "
                      "goes."},
             {"letter": "F",
              "name": "Fine-tune",
              "line": "nothing to convert — both are already “times”",
              "note": "Multiply, never add. 10 + 40 = 50 is the commonest wrong "
                      "answer on this calculation."},
             {"letter": "A",
              "name": "Answer",
              "line": "×400",
              "note": "Magnification has no unit — ×400 means four hundred "
                      "times bigger, never 400 mm."},
         ],
         # The stepper's three button labels. One-way: there is no collapse and
         # no reset, and the button is `disabled` at the end.
         "buttons": {                                              # NEW
             "first": "Show the first step",
             "next": "Show the next step",
             "done": "All four steps shown"},
         },

        # ── #s-yours · the parallel attempt (G9, §7.5) ──────────────────────
        # Law 5's "the same artifact, produced by the student". Same four
        # letters, different numbers (×4 objective, so ×40).
        # Two defects Design's page carries and this record does not license:
        # the model working must sit behind at least one non-empty field, and
        # the typed value must survive a re-render.
        {"id": "magnification-fifa-do",
         "kind": "fifa-construct",
         "demand": "apply",
         "eyebrow": "Now you · same four steps",                   # NEW
         "heading": "Your eyepiece says ×10. You click the ×4 objective into "  # NEW
                    "place. Calculate the total magnification.",
         "prompt": "Write each step out. Then check your working against "
                   "Riya’s and tick what you did.",
         "fields": [                                               # NEW
             {"id": "my-f", "letter": "F", "label": "Formula",
              "placeholder": "total magnification = …"},
             {"id": "my-i", "letter": "I", "label": "Insert",
              "placeholder": "total magnification = … × …"},
             {"id": "my-t", "letter": "F", "label": "Fine-tune",
              "placeholder": "anything to convert?"},
             {"id": "my-a", "letter": "A", "label": "Answer",
              "placeholder": "×…"},
         ],
         "check_label": "Check my working",                        # NEW
         "model_lead": "Riya’s working, with your numbers",        # NEW
         "model": [                                                # NEW
             "F   total magnification = eyepiece × objective",
             "I   total magnification = 10 × 4",
             "F   nothing to convert — multiply, do not add",
             "A   ×40",
         ],
         "success": [
             "I wrote the formula out before I put any numbers in.",
             "I put 10 in for the eyepiece and 4 in for the objective.",
             "I multiplied. I did not add.",
             "My answer is written ×40 — a number of times, with no unit after "
             "it.",
         ],
         # This block's own met-copy, NOT the ladder's "rung met" — and it never
         # feeds the ladder score.
         "tally_met": "All 4 ticked — you can do this one on your own."},  # NEW

        # ── #s-lab · the bench microscope (G10, §7.6) ───────────────────────
        # The instrument is the repo's one engine, `wireMicroscope` (shared/ks3.js),
        # reconciled against this page and B1-06 under MRB-210. Everything the
        # optics decides is an ENGINE CONSTANT and is deliberately absent here:
        # eyepiece ×10 (`EYEPIECE`), objectives [4, 10, 40], field of view
        # 180/magnification (`FIELD_AT_1X_MM`), depth of field
        # [0.100, 0.040, 0.008] mm (`OBJ_DOF_MM`), focus travel ±0.09 mm, the
        # sharp test |focal − depth| < 0.6 × dof, the non-parfocal offsets
        # [0, 10, 22], the 0.30 × 0.115 mm onion cell. Design's page authors
        # `fov` and `cells` as literals; an authored number can drift from the
        # optics and a derived one cannot, so the engine computes them and the
        # parity gate asserts its output equals the page's literals
        # (×40 → 4.50 mm → 15 cells · ×100 → 1.80 mm → 6 · ×400 → 0.45 mm → 1½).
        #
        # ⚑ F9 — the specimen selector. Design draws TWO controls, objective and
        # focus, on one slide ("a slide of onion skin", named in the aside). The
        # superseded record declared three specimens and a `specimen` control,
        # and its reveal depended on switching between two onion slides. Design's
        # page wins: `controls` omits `specimen`, so no selector is drawn.
        # `specimens` keeps ONE entry because both sides require it structurally
        # — `build_ks3.r_sim` hard-fails a microscope sim with no specimens[] and
        # `wireMicroscope` returns early on an empty payload — and because the
        # canvas has to know which slide to draw. "onion skin" classifies to the
        # `onion` slide model in both `_specimen_kind()` and `specimenKind()`.
        # Nothing is selectable, because there is nothing to select. Recorded as
        # a divergence: the bubble slide and the cheek slide leave the lesson
        # with the superseded record, and CELL-01 is confronted in the method
        # critique instead.
        {"id": "microscope-lab",
         "kind": "lab",
         "demand": "investigate",
         # The `practical` shell carries the generator's own eyebrow
         # ("Investigate"), which is what Design draws, so none is authored.
         # The <h2> and the right-aligned aside beside it are Design's and need
         # words from data.
         "heading": "The bench microscope",                        # NEW
         "aside": "Eyepiece fixed at ×10. Turret, focus and a slide of onion "   # NEW
                  "skin.",
         # Law 4's gate. Choosing an option unveils the instrument.
         # ⚑ F8, unresolved: Design's page never scores this prediction and
         # never answers it, so this record carries NO `answer` and NO `reveal`
         # — authoring either would put a marked verdict or a reveal panel on a
         # page Design did not draw. If Law 4's second clause is ruled to stand,
         # the right answer is option B ("You see less of the slide") and the
         # reveal is one line; both are one edit away.
         "prompt": "Turn from the ×4 objective to the ×40. What happens to the "
                   "amount of slide you can see?",
         "options": ["You see more of the slide",
                     "You see less of the slide",
                     "You see the same amount, bigger"],
         "sim": {
             "kind": "microscope",
             "controls": ["magnification", "focus"],
             "specimens": ["onion skin"],
             "eyepiece": 10,                                       # NEW
             # Design labels the turret by OBJECTIVE (×4 ×10 ×40), which is what
             # is written on a real one, and draws it as three aria-pressed
             # buttons — not the generator's <select> labelled by total.
             "objective_control": "segment",                       # NEW
             "focus_label": "Focus — rack through the layers",      # NEW
             "veil": "Answer the question underneath first. The lens will not "  # NEW
                     "tell you anything you have not already guessed at.",
             # Three big mono numerals. `id` names the quantity the ENGINE
             # computes; `label` is the word Design draws above it.
             "readouts": [                                         # NEW shape
                 {"id": "total-magnification", "label": "Total magnification"},
                 {"id": "field-of-view", "label": "Field of view"},
                 {"id": "cells-across", "label": "Cells across it"},
             ],
             # The per-objective teaching note, keyed by TOTAL magnification. It
             # is chosen by the objective and nothing else — it does not change
             # as the wheel turns.
             #
             # ⚑ The "100" line is MRB-210's correction. Design's page said "At
             # ×100 two layers are nearly sharp together. There is still depth
             # to spare." — false on both counts under OBJ_DOF_MM: the ×100
             # window is ±0.0240 mm against layers 0.055 mm apart, so exactly
             # one layer is sharp at every one of the 101 wheel positions and
             # the sharp slice is thinner than the gap between the layers.
             #
             # ⚠️ The key is `resolve_notes`, which is what `r_micro_bench`
             # reads (build_ks3.py) and what b1-06 authors. This record said
             # `notes` until 14 Aug 2026, and the generator has no such field —
             # so the whole block, INCLUDING Mide's approved ×100 correction,
             # was validated by nothing and dropped on the floor. The corrected
             # line was reported as delivered and appeared zero times in the
             # built page. Renaming is the entire fix; the copy was already right.
             "resolve_notes": {                                    # NEW
                 "40": "At ×40 the whole thickness of the skin is in focus at "
                       "once. Easy to find things; not much detail in them.",
                 "100": "At ×100 only one layer is sharp at a time. Rack the "
                        "focus and you swap one layer for another — the depth "
                        "you had at ×40 has already gone.",
                 "400": "At ×400 the slice in focus is thinner than one cell. "
                        "Rack the focus and the layers arrive one at a time — "
                        "that thin slice is the depth of field.",
             },
             # The recording table is a CHECKLIST OF LENSES VISITED, not a data
             # table the student fills in: rows are keyed by objective, every
             # cell is engine-derived, and recording is idempotent per objective.
             # Completion is one row per objective.
             "record": {                                           # NEW
                 "button": "Record this row",
                 "columns": [
                     {"id": "objective", "label": "Objective"},
                     {"id": "total", "label": "Total"},
                     {"id": "field-of-view", "label": "Field of view"},
                     {"id": "cells-across", "label": "Cells across"},
                 ],
                 "complete": "Ten times the magnification. A tenth of the field "
                             "of view. A tenth of the cells in front of you — "
                             "and a slice of depth so thin that most of the "
                             "cell is out of focus at once."},
         },
         "targets": "CELL-02"},

        # ── #s-think · the debrief (F13) ────────────────────────────────────
        # Deliberately quote + two paragraphs and NOTHING else. The confrontation
        # already happened at the bench — the student's own table is the
        # evidence this block cites — so the renderer must NOT synthesise a
        # prompt-and-reveal Design did not draw. Hence `paragraphs` and no
        # `prompt`, no `reveal`.
        {"id": "highest-is-best",
         "kind": "confrontation",
         "demand": "explain",
         "targets": "CELL-02",
         "paragraphs": [                                           # NEW
             "Magnification makes things bigger. It does not make them easier "
             "to find, and it takes away depth as fast as it adds size. Your "
             "own table says it: at ×400 there are fewer than two cells in "
             "front of you and only a slice of each one is sharp.",
             "So the method is: find it on the lowest power, get it in the "
             "middle, then climb.",
         ]},
    ],

    # ── the mastery ladder (Law 8, §5.8) ────────────────────────────────────
    # Two rungs the page marks, two the student marks — which is decided by the
    # data (options vs success), not by rung number.
    "ladder": {
        "recall": {
            "q": "You have just clipped a new slide onto the stage. Which "
                 "objective do you turn in first?",
            "options": ["The ×4 — the lowest power",
                        "The ×40 — the highest power",
                        "The ×10 — somewhere in the middle",
                        "Whichever one is already in place"],
            "answer": 0,
            "feedback": {
                1: "That is 0.45 mm of slide in view and almost no depth in "
                   "focus. Finding anything is luck.",
                2: "Better than starting at the top, but you still have less to "
                   "search. Start at the bottom every time, then climb.",
                3: "If the last person left the ×40 in, you start blind and "
                   "risk driving the lens into the glass. Turn to the lowest "
                   "first.",
            }},
        "apply": {
            "q": "A microscope has a ×15 eyepiece. You click the ×40 objective "
                 "into place. What is the total magnification?",
            # `.ks3-fifa` keeps the SCAFFOLD job Design gives it (§4.8.2, F11):
            # the method as instructions beside a question the student is about
            # to answer — never the worked answer, which lives in #s-worked's
            # stepper. Rendered as <strong>letter</strong> — text.
            "scaffold": [                                          # NEW
                {"letter": "F",
                 "text": "write the formula down before anything else."},
                {"letter": "I", "text": "insert the two numbers."},
                {"letter": "F",
                 "text": "fine-tune: convert any units, and rearrange the "
                         "equation if what you want is not on the left."},
                {"letter": "A", "text": "answer, written as “times”."},
            ],
            "options": ["×55", "×600", "×40", "×6000"],
            "answer": 1,
            "feedback": {
                0: "That is 15 + 40. The two magnifications multiply — the "
                   "objective makes an image and the eyepiece magnifies that "
                   "image again.",
                2: "That is the objective on its own. The eyepiece magnifies "
                   "again on top of it, so it must go into the sum.",
                3: "One zero too many: 15 × 40 = 600. Worth checking the size "
                   "of the answer against the ×400 you already know.",
            }},
        "explain": {
            "q": "Ade finds his cells on ×4, then turns straight to ×40 and "
                 "says they have vanished. Explain what has happened and what "
                 "he should do.",
            "field_label": "Your answer",                          # NEW
            "placeholder": "Write two or three sentences.",        # NEW
            "success": [
                "I said the field of view gets smaller as magnification goes "
                "up.",
                "I said that means less of the slide is in front of him — so "
                "what he wants can end up outside the view.",
                "I said the depth in focus shrinks too, so it can be there and "
                "still look blurred.",
                "I said he should go back to ×4, move what he wants into the "
                "middle, then climb through ×10 and refocus at each step.",
            ]},
        "produce": {
            "q": "Two students disagree about whether onion cells from the "
                 "outer layer are longer than cells from an inner layer. Write "
                 "the method you would give them.",
            "field_label": "Your answer",                          # NEW
            "placeholder": "Say what you would change, what you would keep the "  # NEW
                           "same, and what you would measure.",
            "success": [
                "I said which layer the onion strip comes from — that is the "
                "thing being changed.",
                "I said the magnification stays the same for every slide, or "
                "the comparison is worthless.",
                "I said what gets measured and how — cells counted across a "
                "known field of view, or measured against the field.",
                "I said measure several cells and repeat, rather than trusting "
                "one.",
            ]},
    },

    # ── the key note (fixed, last, photographable) ──────────────────────────
    "key_note": "Total magnification = eyepiece × objective. Every step up in "
                "magnification hands back field of view and depth, so find it "
                "low and climb.",

    # ── the stretch layer (§5.6) — visible and opt-in to all ────────────────
    # One paragraph, exactly as drawn. This is the only place in KS3 that says
    # where FIELD_AT_1X_MM = 180 comes from.
    "stretch": [
        {"type": "explainer", "id": "where-180-comes-from",
         "text": "Where does 180 come from? Printed on the eyepiece is a field "
                 "number — on these ones, 18. Divide it by the objective and "
                 "you get the field of view in millimetres. Because this "
                 "eyepiece is ×10, dividing 180 by the total magnification "
                 "gives the same answer. Change the eyepiece and the 180 "
                 "changes with it."},
    ],

    # Present and empty — §5.6's ruling: may be empty, never absent.
    "support": [],

    # ── end matter (§4.8.1 C, D) ────────────────────────────────────────────
    # The tutor CTA is a real in-page link, and it anchors at THIS lesson's
    # sticking point (the calculation), not a fixed section — the anchor is per
    # lesson.
    "tutor": {"prompt": "Stuck on the calculation?",
              "cta": "Ask about this lesson",
              "anchor": "s-worked"},

    # ⚠ §4.8.1 D renders `ks4_becomes` only when `ks4_links` is empty. This
    # lesson has BOTH: the KS4 bridge edge is real and worth keeping, and Design
    # draws prose in the "At GCSE this becomes" card rather than a link. Under
    # inventory G13 the prose is the field, not a fallback — flagged for the
    # amendment, and the data carries both so either ruling can be honoured
    # without re-authoring.
    "ks4_becomes": "Magnification = image size ÷ actual size, and the electron "
                   "microscope.",

    # Rendered alongside LEGAL_LINE, not instead of it (§4.8.1 D).
    "safety_note": "Microscope lamps get hot and slides are glass. Follow your "
                   "teacher’s instructions at the bench.",

    # ── working scientifically (§5.7) ───────────────────────────────────────
    "ws": ["experimental-skills-and-investigations", "measurement",
           "analysis-and-evaluation"],

    # ── governance (§5.10) ──────────────────────────────────────────────────
    # The approved page renders "Draft — not yet science-reviewed." The ×100
    # correction and ~1,139 words of new science-bearing content arrive with
    # this record and need the examiner gate.
    "review_state": "draft",
}
