"""C1 L2 — Solids, liquids and gases (CONTRAST).

Authored against Design's approved page,
`docs/ks3/design-reference/c1/c1-02-solids-liquids-and-gases.dc.html`
(809 lines), and its measured specification,
`docs/ks3/c1-inventory/PAYLOAD-MAP.md` §2.

Every student-facing string is byte-identical to the approved page. The
module-scope constants came out of `node tools/extract_design_payload.js`
(`scratchpad/payloads/c1/c1-02-solids-liquids-and-gases.json`); the strings that
live inside `renderVals()` — the eight bench notes, the three canvas
descriptions, the two piston banners and the reference-particle caption — were
lifted by hand from the line ranges §2.2 records.

── The one lesson with no dark ground but two ──────────────────────────

§2.3: this is the only C1 lesson with **no dark `practical` block**. Its only
ink grounds are the hook and the keynote. Both instruments — `state-bench` and
`state-matrix` — are LIGHT `check` shells, measured off Design's own markup
(`class="ks3-block"`, no `ks3-dark`), and painting either on ink would resolve
every text token wrong and lose the cream the particle drawing sits on.

── The reference particle is not decoration ────────────────────────────

NOTES §3 flag 3, and the build contract names it non-negotiable: the bench
draws ONE particle at fixed size, captioned, in every state and in every
setting. It is the whole argument of the lesson made visible — a gas particle
and a solid particle are the same object — so `reference_particle` is a
REQUIRED key and `r_state_bench` raises without it rather than quietly
rendering a bench that has lost its point.

── Two rail items: one reversed (MRB-249), one still a correction ──────

1. **`#s-matrix` STAYS ON the rail.** ⊕ **REVERSED 18 Aug 2026 (MRB-249).**
   This item used to say the opposite, and a dozen later lessons cited it.
   Design's stage 3 ticks on `Object.keys(seen).length >= 3` — stage 2's
   predicate, verbatim — and because `#s-matrix` is an eyebrow, a heading, a
   lede, a table and a footnote, emitting no control, no commit and no field,
   the argument was that MRB-208 confined the rail to sections requiring the
   student to do something, that there was no demand in the section to promote,
   and that inventing a control Design did not draw is closed to this build. So
   the lesson shipped FOUR stops, not five.

   Two things overrule that. MRB-205 binds and is not re-argued — Design draws,
   we render, nothing invented and nothing dropped, page wins over engine — and
   dropping a stop Design drew is as much a departure from the page as adding a
   control to it. And the repeated predicate is Design saying how stage 3
   ticks: `isDone()` is a rail-level function, and the same expression written
   for two consecutive ids is a declaration. The contrast table is the payoff
   of the bench beside it, and it carries no control because the bench already
   took the student's commitment. That is a MIRROR, resolved at rail level in
   `wireRail`'s `paint()`.

   So the stop is declared: anchor `s-matrix`, `mirrors: "s-bench"`,
   `done_when: "all_three_states_seen"` — stage 2's predicate, named as
   borrowed rather than smuggled, and gated by
   `ks3_parity.check_rail_matches_design` against `docs/ks3/rail-manifest.md`.
   FIVE stops, as Design drew. The section keeps its `scroll-margin-top`
   anchor, as it always did.

   ⚑ The note below was recorded here before the reversal and it turns out to
   have been describing the mechanism: the nearest thing to a demand of its own
   is the highlight, and the matrix lights a different row for squash, for
   paths and for neither — but those are the BENCH's toggles, in the bench's
   section. That is not a defect to route around; it is what a mirror IS. The
   section's state is the bench's state, which is why Design gives the two
   stops one predicate.

2. **`benchProgress` starts at ZERO.** Design computes
   `Object.keys(seen).length + (seen[st] ? 0 : 1)` (line 614), which counts the
   state the bench is *about* to show as already seen — so a page nobody has
   touched reads "1 of 3 states seen" above a bench that is still behind its
   gate. `head_counter.start` is 0 here, and the gate banks `solid` when it is
   answered, which is the first moment a student has actually seen anything.

── Three rows no bench setting can reach ───────────────────────────────

§2.5.2's finding, reproduced and not papered over: `shape`, `volume` and `pour`
can never be highlighted, because the highlight is driven by squash / paths /
neither and those three rows answer none of those. All six rows are authored —
the table is the lesson's reference — and the footnote's claim is true of the
three that can light. Reported for Design; no control was invented to reach
them.

⚑ For Mide's science gate:
  * §2.6 — the `#s-think` reveal argues *"If melting made particles smaller you
    would expect water to be less dense than ice, and it is the other way
    round."* The observation is right (water IS denser than ice) but the
    conditional reads backwards: smaller particles in the liquid would make
    water more dense, which is what is observed, so the sentence appears to
    offer the observation as a refutation of its own antecedent. **Design's
    wording is lifted unchanged.** This is a content call, not an engine one.
  * The bridge in the hook and the rail in rung 4 are the same phenomenon at two
    scales, deliberately — the hook opens it and the last rung asks for it back.
"""

# ── the contrast table (page lines 348–355) ─────────────────────────────
# 24 authored cells. Lifted from the extracted JSON, not retyped: `Takes the
# container’s` carries U+2019 and it is the only apostrophe in the table.
#
# `key` is the highlight handle — `highlight` below names three of these six and
# `wireStateMatrix` reads them off `data-row`. The other three are unreachable
# by any bench setting; see the module docstring.
MATRIX = [
    {"key": "arrangement", "label": "Arrangement",
     "solid": "Regular rows, all touching",
     "liquid": "Touching, but jumbled",
     "gas": "Far apart, random"},
    {"key": "movement", "label": "Movement",
     "solid": "Vibrating on the spot",
     "liquid": "Sliding over each other",
     "gas": "Fast, in all directions"},
    {"key": "shape", "label": "Shape",
     "solid": "Keeps its own",
     "liquid": "Takes the container’s",
     "gas": "Fills the container"},
    {"key": "volume", "label": "Volume",
     "solid": "Fixed",
     "liquid": "Fixed",
     "gas": "Fills whatever it is given"},
    {"key": "squash", "label": "Can it be squashed?",
     "solid": "Almost not at all",
     "liquid": "Almost not at all",
     "gas": "Easily"},
    {"key": "pour", "label": "Can it be poured?",
     "solid": "No",
     "liquid": "Yes",
     "gas": "It escapes instead"},
]

LESSON = {
    # ── identity ────────────────────────────────────────────────────────────
    # Matches ks3_data/structure.py line 159 character for character. §7.1: the
    # slug does not move, so no URL breaks and no `requires` repointing.
    "slug":        "solids-liquids-and-gases",
    "title":       "Solids, liquids and gases",
    "discipline":  "chemistry",
    "unit":        "particles-and-their-behaviour",
    "family":      "CONTRAST",

    # ── curriculum position ─────────────────────────────────────────────────
    # Carried across unchanged from the superseded body in
    # `ks3_data/chemistry_c1_particles.py`. `covers` is load-bearing: the build
    # validates exactly-once statutory coverage across the whole key stage, so
    # a wrong code here fails every unit and not only this one.
    "covers":      ["KS3.C.PNM.01b"],
    "touches":     [],
    "beyond_statutory": False,
    "threads":     [{"id": "particles", "level": 1},
                    {"id": "structure-function", "level": 1}],
    "typical_year": 7,
    "typical_minutes": 40,

    # ── progression edges ───────────────────────────────────────────────────
    # `requires` renders Design's "Before this lesson → The particle model"
    # (page line 309); `references` + `connects_heading` render its "Next in
    # this unit → Changes of state" (line 315), which `r_endmatter`'s default
    # heading of "Connects to" would have mislabelled.
    "requires":    ["particle-model"],
    "assumes":     [],
    "references":  ["changes-of-state"],
    "connects_heading": "Next in this unit",
    # ⚑ Carried across unchanged, per the unit's curriculum-position rule — and
    # it costs Design's third endmatter card its prose. `ks4_becomes` renders
    # only when `ks4_links` is EMPTY (build_ks3.py:5235), so with a live edge
    # here the card shows the link and Design's authored sentence — "Bonding,
    # structure and the properties of materials — why a state has the
    # properties it does, in terms of the forces between particles." (line 320)
    # — has no read site and is therefore not authored. Flagged in the report;
    # the fix, if the page is to win, is `"ks4_links": []` plus that sentence
    # as `ks4_becomes`.
    "ks4_links":   ["chemistry/bonding/states-of-matter"],

    # ── framing ─────────────────────────────────────────────────────────────
    "big_question": "Ice, water and steam are the same substance and the same "
                    "particles. So what exactly is different about them?",

    # ── the progress rail (§4.8.1 A) ────────────────────────────────────────
    # FIVE stops, as Design draws them. `s-matrix` is the third: no control of
    # its own, so it mirrors `s-bench` and ticks on the bench's predicate — see
    # the docstring. `short` is ≤6 characters and `label` is Design's own
    # sentence-case string from `RAIL` (page lines 338–344), both lifted.
    "rail": [
        {"anchor": "s-hook",   "short": "HOOK",   "label": "The long bridge",
         "done_when": "committed"},
        {"anchor": "s-bench",  "short": "BENCH",  "label": "State bench",
         "done_when": "all_three_states_seen"},
        {"anchor": "s-matrix", "short": "TABLE", "label": "The contrast",
         "mirrors": "s-bench", "done_when": "all_three_states_seen"},
        {"anchor": "s-think",  "short": "THINK",  "label": "Softening particles",
         "done_when": "committed"},
        {"anchor": "s-ladder", "short": "LADDER", "label": "Mastery ladder",
         "done_when": "ladder_complete"},
    ],

    # ── the hook (Law 1) ────────────────────────────────────────────────────
    # `kind` is read by nothing — build_ks3.py's `_hook_media` says so in as
    # many words and dispatches on which media key is present instead. Kept for
    # schema consistency with the other 182 lesson slots.
    "phenomenon": {
        "kind": "narrative",
        "title": "A steel girder on a hot day.",
        "prompt": "A bridge is longer in August than in January — by "
                  "centimetres, enough that bridges are built with gaps to "
                  "swallow it. The steel gains nothing and loses nothing. The "
                  "same iron particles are there in both months, and there are "
                  "exactly as many of them.",
        "commit": "So what got bigger?",
        "options": [
            "Each iron particle expanded in the heat",
            "The gaps between the particles got bigger",
            "The steel absorbed moisture from the summer air",
            "Extra particles were added by the heat",
        ],
        "reveal": "The gaps. Heating makes the particles vibrate harder, so "
                  "each one needs more elbow room, so the spaces between them "
                  "grow. Every particle is exactly the size it was in January. "
                  "Hold on to that, because it is the single idea this lesson "
                  "is built to defend.",
    },

    # ── misconceptions (Law 3) ──────────────────────────────────────────────
    # Both ids are the register's own (docs/ks3/misconception-register.md rows
    # PART-03 and PART-04, both already owned by this slug — §7.4 confirms the
    # rebuild moves no register row). What moves is the MECHANISM each one is
    # pointed at, because the blocks the register names are the superseded
    # lesson's and do not exist on Design's page:
    #
    #   PART-03  elicited_by `what-changed` → `same-particles-reveal`
    #            (Design's `#s-think` both elicits and confronts, in one commit)
    #   PART-04  elicited_by `predict-solid-motion` → `state-bench`
    #            confronted_by `vibration-sim`      → `state-bench`
    #            (the bench GATE offers "Nothing — they are completely still"
    #             as option A, and the bench's own resting note for a solid
    #             answers it: "A solid is not still.")
    "misconceptions": [
        {"id": "PART-03",
         "statement": "The particles themselves change — they melt, or get "
                      "softer, or expand — when a substance changes state.",
         "elicited_by": "same-particles-reveal",
         "confronted_by": "same-particles-reveal"},
        {"id": "PART-04",
         "statement": "Particles in a solid are completely still.",
         "elicited_by": "state-bench",
         "confronted_by": "state-bench"},
    ],

    # Carried from the superseded body. Design draws no keyword block anywhere
    # in C1 (PAYLOAD-MAP §0.7), so the definitions never reach the lesson body;
    # the TERMS do reach a student, as the unit page's "Words this unit gives
    # you" chips, and the reading-age gate reads them as its exclusion list.
    "vocabulary": [
        {"term": "solid",
         "definition": "A state of matter that keeps its own shape and cannot be "
                       "squashed much.",
         "note": None},
        {"term": "liquid",
         "definition": "A state of matter that takes the shape of its container "
                       "but keeps the same volume.",
         "note": None},
        {"term": "gas",
         "definition": "A state of matter that spreads out to fill its whole "
                       "container.",
         "note": "'Gas' is a state. 'Air' is a particular mixture of gases — "
                 "they are not the same word."},
        {"term": "vibrate",
         "definition": "To move quickly back and forth about a fixed position.",
         "note": None},
        # ⊕ ADDED by the rebuild. The other four entries all define themselves
        # as "a state of matter" and the word itself was never defined. The
        # rebuilt page cannot be read without it — the key fact is about what
        # sets a state, the bench's first control group is captioned "State",
        # and the head counter counts states seen. Worded so the stretch layer,
        # which names plasma as a fourth state and glass as neither, does not
        # contradict it.
        {"term": "state",
         "definition": "One of the forms a substance can take. Solid, liquid and "
                       "gas are the three you meet in this unit.",
         "note": "Ice, water and steam are one substance in three states — the "
                 "particles are identical in all three."},
    ],

    # Nothing on the rebuilt page references a figure. The superseded body's
    # `c1-arrangement-compare` — arrangement, movement and spacing side by side
    # — is exactly what the state bench animates and the contrast matrix
    # tabulates, so the drawing is not missing, it has been replaced by two
    # instruments. Declaring it would put a sourcing task in the diagram
    # manifest for a figure no block would show. Present and empty, never
    # absent.
    "figures": [],

    # ── core, in the approved page's document order ─────────────────────────
    "core": [
        {"type": "hook", "ref": "phenomenon", "anchor": "s-hook"},

        {"type": "explainer",
         "text": "Three states, one substance. The particles do not change "
                 "— not their size, not their mass, not what they are. "
                 "What changes is how close together they sit and how much they "
                 "move. Every difference you can see and feel between ice, "
                 "water and steam comes out of those two things."},

        # #s-bench — state-bench, an animated canvas in a LIGHT check shell.
        # Not `particle-states`: §2.6 shows that sim is a temperature slider,
        # and rendering the bench as one would hand the student a control
        # Design did not draw and hide the three Design did.
        {"type": "state-bench", "id": "state-bench", "anchor": "s-bench",
         "demand": "investigate",
         "eyebrow": "The state bench · watch one substance",
         "heading": "Same particles. Three arrangements.",
         # Opens at ZERO — see the docstring. `_head_counter` has no slot for a
         # bespoke FULL string, so Design's "all three seen" is carried on the
         # instrument as `progress_full` and written by `wireStateBench`.
         "head_counter": {"format": "{n} of 3 states seen", "total": 3,
                          "start": 0},
         "progress_full": "all three seen",

         # C6's commit gate (page lines 121–135). Answering it is also the
         # first state observation — the bench opens on the solid, so the gate
         # banks `solid` and the counter moves 0 → 1.
         "gate": {
             "prompt": "Commit first. In a block of ice sitting in a freezer, "
                       "what are the particles doing?",
             "options": [
                 "Nothing — they are completely still",
                 "Vibrating on the spot without moving anywhere",
                 "Sliding slowly past each other",
                 "Moving freely, just very slowly",
             ]},

         # The three states, in Design's order. `label` is the button face and
         # also the caption the canvas prints in mono uppercase; `alt` is the
         # canvas's whole `aria-label` for that state, authored as one finished
         # sentence rather than composed at runtime from a key.
         "states": [
             {"key": "solid", "label": "Solid",
              "alt": "A particle box showing the solid state: particles in "
                     "regular rows, vibrating in place."},
             {"key": "liquid", "label": "Liquid",
              "alt": "A particle box showing the liquid state: particles "
                     "touching but jumbled, sliding past each other below a "
                     "surface line."},
             {"key": "gas", "label": "Gas",
              "alt": "A particle box showing the gas state: widely separated "
                     "particles moving fast in all directions."},
         ],

         # The two control-group captions (lines 141, 147).
         "groups": {"states": "State", "instruments": "Instruments"},

         # Two toggles carrying a LABEL PAIR each, which §2.6 records as a
         # thing the schema could not hold, plus one single-label toggle.
         # The pair is keyed by the state the control is IN, not by what
         # pressing it does, so the renderer cannot mix them up.
         "controls": {
             "motion": {"running": "Freeze the motion",
                        "frozen":  "Start the motion"},
             "trails": {"shown":  "Hide the paths",
                        "hidden": "Show the paths"},
             "squash": {"label": "Try to squash it"},
         },

         # Drawn across the piston when the squash toggle is on (line 491).
         # Mono uppercase, on the canvas, in Design's own bytes.
         "squash_banner": {
             "gas":   "PISTON PUSHED IN — IT GAVE WAY",
             "other": "PISTON PUSHED HARD — IT BARELY MOVED",
         },

         # ⚖️ NON-NEGOTIABLE (NOTES §3 flag 3). One particle, drawn at the same
         # radius as every particle in every state, with this caption beside it.
         # `r_state_bench` raises if it is missing.
         "reference_particle": "ONE PARTICLE, ACTUAL SIZE — THE SAME IN "
                               "ALL THREE STATES",

         # The eight authored notes (lines 623–640). All eight are in the
         # document and seven are `hidden` — emit-both-show-one — so no
         # science-bearing sentence is ever rebuilt in JS from an attribute.
         "notes": {
             "squash": {
                 "gas": "The gas gave way immediately, because most of a gas "
                        "is empty space and squashing it just removes some of "
                        "that space. The particles did not get smaller — "
                        "they got closer.",
                 "other": "Barely a millimetre. The particles are already "
                          "touching, so there is no space left to remove, and "
                          "pushing harder only pushes particle against "
                          "particle. This is why you can compress air in a "
                          "syringe and not water.",
             },
             "trails": {
                 "solid": "Every particle has a home position and never leaves "
                          "it. The trails are tiny circles — that is "
                          "vibration, not travel, and it is why a solid keeps "
                          "its shape.",
                 "liquid": "The trails wander. Particles change neighbours "
                           "constantly but stay in contact, which is exactly "
                           "what pouring looks like from the inside.",
                 "gas": "Long straight runs between collisions. Nothing steers "
                        "a gas particle; it goes until it hits something.",
             },
             "rest": {
                 "solid": "A solid is not still. Every particle is vibrating "
                          "about a fixed point — switch the motion off "
                          "and on and watch the difference between vibrating "
                          "and travelling.",
                 "liquid": "The particles are still touching, exactly as in "
                           "the solid, but the neat rows have gone. Same "
                           "crowding, no order: that is the entire difference "
                           "between a solid and a liquid.",
                 "gas": "Almost all of this box is empty. That emptiness is "
                        "what lets you squash a gas, and nothing else about it "
                        "has changed.",
             },
         }},

        # #s-matrix — state-matrix, DOM, LIGHT check shell. Rail stop 3,
        # mirroring `s-bench`; see the docstring.
        # `r_comparison` is B1-06's two-column "one against the other" table
        # with a dark header row; this is a four-column property matrix whose
        # lit row is driven by another block's controls (§2.5.2).
        {"type": "state-matrix", "id": "contrast-matrix", "anchor": "s-matrix",
         "demand": "compare",
         "eyebrow": "The contrast, in one table",
         "heading": "What each arrangement forces to be true",
         "prompt": "Nothing in this table is a fact to memorise separately. "
                   "Every row is a consequence of the two rows above it.",
         "columns": ["Property", "Solid", "Liquid", "Gas"],
         "rows": MATRIX,
         # ⊕ CROSS-BLOCK STATE, and the first of it in the key stage. The
         # matrix does not keep a copy of the bench's settings — it reads them
         # off `[data-sbench]`'s own attributes inside the section named here,
         # so there is exactly one place the bench's state lives. `highlight`
         # maps a bench condition to a row `key`, checked at build time against
         # `rows` so a renamed row is a build error and never a table that
         # quietly stops lighting.
         "highlight_from": "s-bench",
         "highlight": {"squash": "squash",
                       "trails": "movement",
                       "rest":   "arrangement"},
         "footnote": "The highlighted row is the one your current bench "
                     "setting is showing."},

        {"type": "key-fact", "ref": "state-is-arrangement"},

        {"type": "misconception", "id": "same-particles-reveal",
         "anchor": "s-think", "targets": "PART-03"},
        {"type": "quiz", "ref": "ladder", "anchor": "s-ladder"},
        {"type": "summary", "ref": "key_note"},
    ],

    # ── the KEY FACT box (§4.8.1 B) ─────────────────────────────────────────
    # R3: `ground: "card"` and nothing else. Design's page draws 28px/22-26px/
    # 6px-shadow/25px-body; the shipped stylesheet's numbers win, because one
    # sheet serves 183 lesson slots and §1.6 (c) has already reopened drift 5
    # for a ruling that is not this build's to make.
    "key_facts": [
        {"id": "state-is-arrangement",
         "text": "The state of a substance is set by how its particles are "
                 "arranged and how fast they move — never by any change "
                 "in the particles themselves.",
         "placement": "top-level",
         "ground": "card",
         "eyebrow": "Key fact"},
    ],

    # ── activities (§5.5) ───────────────────────────────────────────────────
    # One entry. The two instruments are authored inline in `core` and lifted
    # here by `ks3_data/c1/__init__.py::_normalise`, which also leaves the right
    # SHELL behind each of them.
    "activities": [
        # ⊕ Ruling R1. Design's `#s-think` asks for a commitment before it
        # reveals anything, on all six C1 pages, so it is a `predict` and not
        # B1's static `confrontation` — and it ticks its rail stage, which the
        # `[data-reveal]:not([hidden])` limb of `doneByDom()` delivers without
        # an instrument. `statements` carries Design's own quote, which wins
        # over the register's wording for PART-03 (build_ks3.py:2504).
        {"id": "same-particles-reveal",
         "kind": "predict",
         "demand": "explain",
         "targets": "PART-03",
         "statements": ["When ice melts, the particles go soft and squash into "
                        "the new shape."],
         "prompt": "This is the most common wrong idea in the whole of KS3 "
                   "physical science, and it is worth catching now, because it "
                   "will follow you into pressure, expansion and density. "
                   "Commit before you read on.",
         "options": [
             "True — that is what melting is",
             "The particles stay identical; only their spacing and movement "
             "change",
             "The particles get smaller so they can fit the new shape",
             "Some particles break apart to make room",
         ],
         "reveal": [
             "A water particle in ice and a water particle in steam are "
             "identical. Same size, same mass, same three atoms joined the "
             "same way. Melting does not soften anything and boiling does not "
             "stretch anything.",
             # ⊕ RULED AND CUT — MRB-257 phase 4 (19 Aug 2026). This
             # opened with a freezer test: "ice floats. If melting made
             # particles smaller you would expect water to be less dense
             # than ice, and it is the other way round." This module already
             # flagged the conditional as reading backwards and parked it for
             # Mide, which was right. It is worse than backwards:
             #
             #   smaller particles in the liquid → the same number in less
             #   volume → the LIQUID is denser → the solid floats.
             #
             # Ice floating is exactly what the misconception predicts, so
             # the test CONFIRMED the wrong idea instead of refuting it.
             #
             # And it cannot be repaired by re-wording, because c1-06
             # `testing-the-model` lists "Ice floats on water" among the
             # seven things the model must account for and marks it FAILS —
             # "identical spheres cannot produce this". Any wording that
             # makes ice floating support the spacing account contradicts
             # that lesson, two lessons later in the same unit, and that
             # lesson is right. So the test is cut and the bridge carries
             # the paragraph, which it always could.
             "Test it against the bridge: the girder gets longer, and no "
             "one thinks the iron atoms inflate. What changes is always the "
             "spacing and the speed. <em>Soft</em>, <em>runny</em> and "
             "<em>squashy</em> are words about a crowd of particles, never "
             "about one.",
         ]},
    ],

    # ── the mastery ladder (Law 8, §5.8) ────────────────────────────────────
    # `title` carries Design's finished heading; `_rung_title` strips the
    # "Rung N · " prefix and the engine puts the number back, so the authored
    # bytes and the rendered bytes agree without "Rung 1 · Rung 1 · Recall".
    "ladder": {
        "recall": {
            "title": "Rung 1 · Recall",
            "q": "Which state has particles that are close together but not in "
                 "a regular pattern?",
            "options": [
                "Solid",
                "Gas",
                "All three are equally spaced",
                "Liquid",
            ],
            "answer": 3,
            "feedback": {
                0: "A solid is close together and regular. It is the pattern "
                   "that makes it a solid.",
                1: "A gas is not close together at all — the particles "
                   "are mostly far apart.",
                2: "The whole point of the three states is that spacing "
                   "differs.",
            }},
        "apply": {
            "title": "Rung 2 · The one that catches people",
            "q": "A gas can be squashed into a fifth of its volume. A liquid "
                 "cannot be squashed at all. Why not?",
            # ⚖️ **CORRECTED FROM DESIGN — the distractors were too short
            # (MRB-177 length parity, measured under MRB-228).**
            #
            # Design's set ran 14 / 7 / 4 / 6 words. The correct answer was
            # double the longest distractor, and a student who has worked out
            # that the long one is usually right — which a class works out
            # early — could take this rung without reading it. A question you
            # can score without knowing the science measures nothing.
            #
            # Each distractor keeps its misconception EXACTLY: hardness,
            # size, weight. Only the sentence is completed, so all four now
            # read as full claims at 13–14 words. The correct option is
            # unchanged, because it is the science.
            "options": [
                "Liquid particles are much harder than gas particles, so "
                "they resist being pressed together",
                "Liquid particles are bigger, so they take up all the room "
                "in the container",
                "Liquids are heavier than gases, so they push back harder "
                "against the squash",
                "A liquid’s particles are already touching, so there is "
                "no space to squash out",
            ],
            "answer": 3,
            "feedback": {
                0: "They are the same particles. Water vapour and water are "
                   "made of identical things.",
                1: "Size does not change with state — that is the "
                   "misconception this lesson exists to kill.",
                2: "Weight is not what resists the squash. Space is.",
            }},
        "explain": {
            "title": "Rung 3 · Explain",
            "q": "A gas fills any container it is put in; a liquid of the same "
                 "amount sits in a puddle at the bottom. Explain both, using "
                 "the arrangement and movement of the particles.",
            "field_label": "Your explanation",
            "placeholder": "In a gas the particles…",
            "success": [
                "Says gas particles are far apart with large spaces between "
                "them.",
                "Says gas particles move fast in random directions.",
                "Says nothing holds gas particles together, so they spread "
                "until the walls stop them.",
                "Says liquid particles are touching and attracted to each "
                "other, so they stay as one body.",
                "Says liquid particles can still slide past each other, which "
                "is why the puddle takes the shape of the floor.",
            ]},
        "produce": {
            "title": "Rung 4 · Take it somewhere new",
            "q": "A steel railway rail is 30 m long in winter and about 1 cm "
                 "longer on a hot summer day. Explain what has happened to the "
                 "particles, and say clearly what has NOT happened.",
            "field_label": "Your answer",
            "placeholder": "Heating the rail gives the particles…",
            "success": [
                "Says heating gives the particles more energy so they vibrate "
                "faster or further.",
                "Says the average spacing between the particles increases.",
                "Says the number of particles is unchanged.",
                "States explicitly that the particles themselves have NOT got "
                "bigger.",
                "Says the steel is still a solid — the particles are "
                "still in fixed positions, just further apart.",
            ]},
    },

    # ── the key note (fixed, last, photographable) ──────────────────────────
    "key_note": "Solid: touching, ordered, vibrating in place. Liquid: "
                "touching, disordered, sliding past each other. Gas: far "
                "apart, disordered, moving fast and freely. The particles are "
                "identical in all three.",

    # ── the stretch layer (§5.6) — visible and opt-in to all ────────────────
    # MRB-225: the model's edges live HERE, and nothing above is retracted by
    # it — the three-state model is not withdrawn, it is given a boundary.
    "stretch": [
        {"type": "explainer", "id": "edges-of-three-states",
         "text": "Three states is a school simplification, and a good one "
                 "— it covers almost everything you will meet. But glass "
                 "is a genuine embarrassment to it: it holds its shape like a "
                 "solid while its particles sit in the jumbled arrangement of "
                 "a liquid, so it is neither, and arguments about which box it "
                 "belongs in have been running for a century. Liquid crystals, "
                 "the material in the screen you may be reading this on, flow "
                 "like a liquid while staying lined up like a solid. And most "
                 "of the matter in the universe is in a fourth state, plasma, "
                 "which is what stars are made of. None of this makes the "
                 "three-state model wrong. It makes it a model, with edges, "
                 # ⚠️ A STRAIGHT apostrophe, and it is the page's own byte.
                 # Design writes `container’s` and `liquid’s` with U+2019 and
                 # `Dalton's` with U+0027 — inconsistent, and lifted as found
                 # rather than tidied, because tidying is retyping.
                 "exactly like Dalton's will turn out to be."},
    ],

    # Present and empty — §5.6's ruling: may be empty, never absent.
    "support": [],

    # ── end matter (§4.8.1 C, D) ────────────────────────────────────────────
    # Design heads the card "Ask Mr Badmus AI" and puts the question in the
    # paragraph under it (lines 323–325); the CTA points back up at the bench.
    "tutor": {"prompt": "Ask Mr Badmus AI",
              "body": "Not sure why a solid vibrates but does not move?",
              "cta": "Ask about this lesson",
              "anchor": "s-bench"},

    # ── working scientifically (§5.7) ───────────────────────────────────────
    "ws": ["experimental-skills-and-investigations"],

    # ── governance (§5.10) ──────────────────────────────────────────────────
    "review_state": "draft",
}
