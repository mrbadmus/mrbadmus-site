"""B4 L3 — Alveoli: built for exchange (MODEL).

Authored against Claude Design's approved page,
`docs/ks3/design-reference/b4/b4-03-alveoli-built-for-exchange.dc.html` (569 lines), its
author's notes `docs/ks3/design-reference/b4/NOTES-B4.md` §3.3 and flags 4 and 20, and the
MRB-220 build contract. Schema per architecture.md §4.8 as amended by §4.8.1
and §4.8.2; shape follows `ks3_data/b3/lesson_02_food_tests.py`.

Every student-facing string is lifted byte-identical from the approved page
except the three listed under "What could not be lifted", none of which is a
sentence of science.

── `KS3.B.GAS.01b`, not the parent ─────────────────────────────────────

The bullet is compound — *"the structure and functions of the gas exchange
system in humans, including adaptations to function"* — and its own "including"
is the seam. `ks3_data/substatements.py` mints `01a` (the parts air passes
through) for `the-gas-exchange-system` and `01b` (adaptations of the exchange
surface) for this lesson. Claiming `GAS.01` whole here would collide with L1
under §5.7's exactly-once rule, and would claim the anatomy this lesson
deliberately does not teach.

── The flagship is a LOOKUP TABLE and the outward bar is never zero ────

`#s-gradient` is `crossing-counter`, on `ks3-block ks3-dark ks3-practical`
(page line 105) — `practical` is measured, per the table in
`ks3_data/b4/__init__.py`, not inherited.

⚖️ **The four states are authored, not computed.** NOTES-B4 §3.3 and §6 are
explicit: two switches, four states, four hand-written notes, and the notes are
where the lesson's argument lives. A computed version would collapse them into
one sentence with numbers in it.

⚖️ **`blood_kpa` is never zero in any of the four states** — 5.3, 13.1, 5.6,
9.3, giving outward counts of 477, 1179, 504 and 837 per second. The outward
bar staying visible in every state IS the confrontation: a student who watches
it disappear has learnt that diffusion is one-way, which is precisely the belief
`BREATH-06` and `BREATH-07` exist to remove. The renderer raises on a
non-positive `blood_kpa` for the same reason.

⚠️ The both-flows-running note quotes its own numbers — *"1197 in, 477 out"* —
and those are `13.3 × 90` and `5.3 × 90`. If a science review moves either kPa
figure, that sentence moves with it. No gate can check a number inside prose.

── FOUR rail stops — Design's fourth restored (MRB-249) ────────────────

⊕ **REVERSED 18 Aug 2026 (MRB-249).** This section used to read "the rail is
THREE stops, not Design's four", on MRB-208 rule 2, taking `b3/lesson_07`'s
`#s-four` and `c1/lesson_02`'s `#s-matrix` with it. Design's rail lists
`s-hook`, `s-gradient`, `s-built`, `s-ladder`, and its own tick function reads:

    if (id === 's-gradient') return s.tried;
    if (id === 's-built')    return s.tried;

— stage three's predicate is stage two's, character for character. Because
`#s-built` is an eyebrow, a display statement, a four-row comparison and a key
fact with no control, no commitment and no field, the argument was that there
was no demand in it to promote, that inventing one Design did not draw is
closed to this build, and so the stop came off rather than ticking on its
neighbour's state.

The OBSERVATION stands and is worth keeping:
`docs/ks3/b4-inventory/PAYLOAD-SCHEMA.md` independently lists `#s-built` among
the five B4 band sections with "no control, a commitment or any state". It is
the CONCLUSION drawn from it that is overruled, on two grounds.

MRB-205 was cited for the wrong half of itself. It says Design draws and we
render, with no invented and no dropped page structure, and page winning over
engine. It forbids inventing a control; it equally forbids dropping a stop.

And the two lines above are Design stating how `#s-built` ticks. `isDone()` is
a rail-level function, and the same expression written for two consecutive ids
is a declaration. The same four features is the payoff of the crossings the
student just counted; the section holds no control because `#s-gradient`
already took the commitment. That is a MIRROR, resolved at rail level in
`wireRail`'s `paint()`.

So the stop is declared: anchor `s-built`, `mirrors: "s-gradient"`,
`done_when: "either_switch_used"` — stage two's predicate, named as borrowed,
and gated by `ks3_parity.check_rail_matches_design` against
`docs/ks3/rail-manifest.md`. `#s-built` keeps its anchor and its scroll-margin,
as it always did. `#s-think` is still not a stop — Design draws none on it, and
on this page it is three quotes and three paragraphs with nothing to answer, so
MRB-220 R1 (which promotes a *committing* `#s-think` to `predict`) does not
reach it.

⚑ NOTES-B4 §6 says "Rail stops: four in every lesson." That is Design's
intention and it is recorded here rather than silently met: a fourth stop on
this page could only ever tick on the bench's state.

── What could not be lifted byte-identical, and why ────────────────────

1. **The `#s-built` lede paragraph.** Design writes *"You met this list in
   <a href="b3-07-…">Absorption and the small intestine</a>. Nothing has been
   added — the same four requirements, met by a different structure. That
   repetition is the point."* `r_comparison` has an eyebrow, a statement, rows
   and a nested key fact, and no lede slot. The sentence naming the link is a
   pointer at another lesson, which §4.6's single-source rule says is an EDGE
   and not repeated prose — so it becomes the `references` edge below, and
   Design's own two remaining sentences ride on that edge as its `why`, which
   `r_endmatter` prints under the link. Nothing is retyped and nothing is lost.

2. **The inline link inside `#s-think`.** Design writes *"the whole transfer is
   diffusion, which you met with bromine in <a href="c1-05-diffusion.html">
   Diffusion</a>"*. `rich()` permits `<em>` and `<strong>` and nothing else, so
   an anchor would render as visible tag soup. The WORDS are unchanged and the
   hyperlink is dropped; the destination is not lost, because `references`
   renders it in the end matter, which is where the engine puts cross-lesson
   navigation. Same resolution as b3-07.

3. **Two endmatter cards become one.** Design draws "Next in this unit"
   (`b4-04`) and "Connects to" (`b3-07`, `c1-05`); the engine's end matter is a
   fixed three (prereqs / connects / KS4). All three links are kept, under
   "Connects to", because dropping the forward link would lose navigation
   Design drew and heading the card "Next in this unit" would describe
   *Diffusion* — another discipline entirely — as the next lesson. Same
   resolution as b3-07.

── ⊕ THE RUNG 2 LENGTH TELL — RULED AND FIXED, 17 Aug 2026 ──────────────

MRB-177 was ruled by Mide on 17 Aug 2026. The ruling: on a recall or apply
rung the correct answer states a RULE (subject, condition, consequence) while
distractors stated one-clause wrong REASONS, so the correct answer was longer
BY CONSTRUCTION and could be scored without being read. The fix is that
distractors state wrong RULES — the same shape as the correct answer, with the
misconception as the consequence. Length parity then follows from the
construct.

Rung 2's three distractors are Mide's own replacements, applied verbatim. The
correct option is unchanged, its index is unchanged, and the `length_tell()`
threshold in `verify_ks3.py` is unchanged.

    rung 1 · untouched. correct 9w against distractors of 4 / 5 / 7 — clears
             the longest by 2 words and by ×1.29. Under both thresholds.
    rung 2 · correct 14w (unchanged) against distractors now 16 / 17 / 13.
             The correct option is no longer the longest. PASSES.

⛔ SUPERSEDED, kept for the record — this block used to read "⚑ A LENGTH TELL
IS PRESENT ON RUNG 2, AND IT IS AUTHORED AS DRAWN", measured the tell (correct
14w against 6 / 7 / 5, failing the ≥4-word gap), and argued the fix was not
this file's to make because rewriting a distractor changes what a marked
question measures — Mide's gate, not a script's — and the `KNOWN_TELLS`
register lives in `verify_ks3.py`, which an authoring pass does not edit
(build contract §0). That reasoning was correct at the time and held the
finding open until Mide ruled. He has now ruled, and the rewrite is his.

⚑ For Mide's science gate — NOTES-B4 flags this lesson carries:
  * **flag 4** — ~500 million alveoli and ~70 m² total surface. Both are quoted
    with wide ranges in the literature (270–790 million; 50–100 m²). Both
    numbers are load-bearing here: the hook's *"about seventy"*, the key fact,
    the key note and comparison row 1 all carry one of them, and the hook's
    *"roughly a hundredth of a square metre"* is the smooth bag against the
    same 70. Same class of problem as B3 flag 17.
  * **flag 20** — this unit has no anatomical diagrams. This page's legal line
    names **no** figure slot (the one B4 slot, `b4-gas-exchange-labelled`, is
    named in b4-01's legal line, not this one), so `figures` is EMPTY here and
    nothing is invented to fill it. Checked against the page's `.ks3-legal`
    line, which is entirely about the illustrative crossing counts.
"""

# ── the four requirements (page lines 330–343, COMPARE) ─────────────────
#
# ⚠️ This list is B3's, deliberately. NOTES-B4 §2 makes the repetition the
# teaching point — the same four requirements, a second organ, nothing added.
# The `gut` column is not a restatement of b3-07's content for its own sake; it
# is the left-hand side of a discrimination the student makes on this page.
COMPARE = [
    {"need": "Requirement 1 · Large surface area",
     "gut": "Folds, villi and microvilli — about 30 m² in six metres of "
            "tube.",
     "lung": "About 500 million alveoli — roughly 70 m² inside a chest you "
             "can put your arms around."},
    {"need": "Requirement 2 · Short diffusion distance",
     "gut": "Villus wall one cell thick, with the capillary immediately "
            "behind it.",
     "lung": "Alveolus wall one cell thick and capillary wall one cell thick "
             "— two cells between air and blood."},
    {"need": "Requirement 3 · Steep concentration difference maintained",
     "gut": "Blood flows past constantly, carrying absorbed glucose away.",
     "lung": "Blood flow drains one side and breathing refreshes the other. "
             "Two flows instead of one, because gas moves both ways."},
    {"need": "Requirement 4 · Moist surface",
     "gut": "Everything is already in solution in the gut contents.",
     "lung": "A film of liquid lines every alveolus, so gases dissolve before "
             "they cross."},
]

# ── the four bench states (page lines 429–450) ──────────────────────────
#
# ⚠️ A LOOKUP TABLE. Keyed on both switches, all four combinations present
# exactly once — `r_crossing_counter` raises otherwise, because four states is
# 2² and a missing row is a switch position with nothing behind it.
#
# ⚠️ `blood_kpa` > 0 in all four. See the docstring; the renderer enforces it.
STATES = [
    {"breathing": True, "blood_flow": True,
     "alveolar_kpa": 13.3, "blood_kpa": 5.3,
     "note": "Both flows running. Crossings happen in both directions  and "
             "you gain the difference. Neither number is zero, and the "
             "outward one never stops."},
    {"breathing": True, "blood_flow": False,
     "alveolar_kpa": 13.3, "blood_kpa": 13.1,
     "note": "Blood flow stopped. Oxygen keeps crossing inwards until the "
             "blood side has almost caught up, then the two counts nearly "
             "match and net absorption collapses. The surface, the thin wall "
             "and the fresh air are all still there."},
    {"breathing": False, "blood_flow": True,
     "alveolar_kpa": 6.0, "blood_kpa": 5.6,
     "note": "Breathing stopped. The blood keeps draining oxygen away, so the "
             "alveolar level falls until the difference is almost gone. Note "
             "that stopping either side has the same effect for the same "
             "reason."},
    {"breathing": False, "blood_flow": False,
     "alveolar_kpa": 9.3, "blood_kpa": 9.3,
     "note": "Both stopped. The two sides have equalised in the middle. "
             "Molecules are still crossing in both directions at exactly the "
             "same rate — nothing has finished, nothing has settled, the "
             "imbalance has simply gone."},
]

LESSON = {
    # ── identity ────────────────────────────────────────────────────────────
    # Matches ks3_data/structure.py line 116 character for character. Slugs are
    # permanent (§8.4) and are the join for every `requires` edge.
    "slug":        "alveoli-built-for-exchange",
    "title":       "Alveoli: built for exchange",
    "discipline":  "biology",
    "unit":        "breathing-and-gas-exchange",
    "family":      "MODEL",

    # ── curriculum position ─────────────────────────────────────────────────
    # ⚑ The `b` clause, not the parent — see the docstring. `the-gas-exchange-
    # system` owns `01a`; owning `GAS.01` whole here would claim the anatomy
    # this lesson does not teach and would collide with L1 under §5.7.
    "covers":      ["KS3.B.GAS.01b"],
    "touches":     [],
    "beyond_statutory": False,
    "threads":     [{"id": "structure-function", "level": 3},
                    {"id": "particles", "level": 2}],
    "typical_year": 8,
    "typical_minutes": 50,

    # ── progression edges ───────────────────────────────────────────────────
    # No `requires`: Design draws no "Before this lesson" card on this page and
    # the engine omits an empty one. All three of her forward and sideways
    # links live in the middle card — see "What could not be lifted" 3.
    "requires":    [],
    "assumes":     [],
    # ⊕ §4.6 — the villus comparison is an EDGE, not repeated prose. Design's
    # own two closing sentences ride on it as `why`, which `r_endmatter` prints
    # under the link. See "What could not be lifted" 1.
    "references":  ["exercise-asthma-and-smoking",
                    {"unit": "B3",
                     "lesson": "absorption-and-the-small-intestine",
                     "why": "Nothing has been added — the same four "
                            "requirements, met by a different structure. That "
                            "repetition is the point."},
                    {"unit": "C1", "lesson": "diffusion"}],
    "ks4_links":   [],
    # Renders only because `ks4_links` is empty — Design's third endmatter card
    # is prose, not a link, and this is the slot §4.8.1 D added for it.
    "ks4_becomes": "Exchange surfaces and surface area to volume ratio, plus "
                   "Fick's law relating rate to area, concentration difference "
                   "and thickness.",

    # ── framing ─────────────────────────────────────────────────────────────
    "big_question": "Oxygen molecules cross from your alveoli into your blood, "
                    "and at the same moment other oxygen molecules cross the "
                    "other way. You survive on the difference between two "
                    "numbers.",

    # ── the progress rail (§4.8.1 A) ────────────────────────────────────────
    # FOUR stops, as Design draws them. `s-built` is the third: no control of
    # its own, so it mirrors `s-gradient` and ticks on that section's predicate
    # — see the docstring. `short` and `label` are Design's own `RAIL_SHORT`
    # and `RAIL` strings (page lines 322–328).
    "rail": [
        {"anchor": "s-hook",     "short": "HOOK",   "label": "One smooth bag",
         "done_when": "committed"},
        # Design's own predicate, kept: `s.tried` goes true the moment either
        # switch is pressed. One press is a real commitment here — it is the
        # act of taking a flow away — so this is not the b3-02 case where a
        # bench of twenty would have ticked after one.
        {"anchor": "s-gradient", "short": "CROSS",
         "label": "Count crossings", "done_when": "either_switch_used"},
        {"anchor": "s-built", "short": "FOUR", "label": "Same four",
         "mirrors": "s-gradient", "done_when": "either_switch_used"},
        {"anchor": "s-ladder",   "short": "LADDER", "label": "Mastery ladder",
         "done_when": "ladder_complete"},
    ],

    # ── the hook (Law 1) ────────────────────────────────────────────────────
    # Options are a wager, never marked — no `answer` key (R3).
    "phenomenon": {
        "kind": "narrative",
        "title": "Replace 500 million alveoli with one smooth bag of the same "
                 "volume.",
        "prompt": "Same total air, same six litres of chest, same clear "
                  "airway, same blood supply arriving. The only change is that "
                  "the sponge has been replaced by a single smooth-walled "
                  "cavity.",
        "commit": "How long would you survive?",
        "options": [
            "Normally — the same air is still in there",
            "A few hours, breathing much faster",
            "Minutes — almost all the exchange surface has gone",
            "Indefinitely, as long as you kept the airway clear",
        ],
        "reveal": "Minutes. The bag holds the same air and offers roughly a "
                  "hundredth of a square metre of exchange surface instead of "
                  "about seventy. Volume is not what keeps you alive — surface "
                  "is, and a bag is the worst possible shape for it.",
    },

    # ── misconceptions (Law 3) ──────────────────────────────────────────────
    # ⚠️ The `BREATH` family is NOT yet in `docs/ks3/misconception-register.md`.
    # NOTES-B4 §5 says thirteen entries were minted, `BREATH-01` to
    # `BREATH-13`, and the register has no `BREATH` row at all — so the family
    # is the unit's to register in ONE pass, by whoever owns the unit, and this
    # module deliberately does not write it (five lessons were authored in
    # parallel and the register is the one file they would all have edited).
    # Nothing fails meanwhile: `_misconception_quote` resolves from THIS list,
    # and the block below carries its own `statements`, which win over the
    # register (build_ks3.py:2504).
    #
    # `BREATH-06` and `BREATH-07` are PINNED by NOTES-B4 §5: they are
    # `PART-10`/`PART-11` in biological costume "for the third time", and the
    # register's own `PART-10` row already names this lesson as a required
    # re-confrontation site. What B4 adds and the earlier two lack is the
    # two-way crossing counter — molecules crossing OUTWARDS stay visible in
    # every state. `BREATH-08` is the adjacent slot for this page's third wrong
    # idea, which is this lesson's alone; reported for registration.
    "misconceptions": [
        {"id": "BREATH-06",
         "statement": "Oxygen is pumped across into the blood.",
         # The bench elicits all three: a student who believes any of them is
         # watching a display that contradicts it before the block names it.
         "elicited_by": "count-the-crossings",
         "confronted_by": "think-crossings"},
        {"id": "BREATH-07",
         "statement": "Oxygen moves in because it wants to spread out evenly.",
         "elicited_by": "count-the-crossings",
         "confronted_by": "think-crossings"},
        {"id": "BREATH-08",
         "statement": "Alveoli are where the air is stored.",
         "elicited_by": "count-the-crossings",
         "confronted_by": "think-crossings"},
    ],

    # Design draws no keyword block anywhere in B4, so these definitions never
    # reach the lesson body. The TERMS do reach a student, as the unit page's
    # "Words this unit gives you" chips, and the reading-age gate reads them as
    # its exclusion list — which matters here, because "alveolus", "diffusion"
    # and "capillary" would otherwise all count against the page.
    "vocabulary": [
        {"term": "alveolus",
         "definition": "One of the roughly 500 million tiny air sacs where gas "
                       "crosses between the lungs and the blood.",
         "note": "One alveolus, many alveoli. The wall is a single cell "
                 "thick."},
        {"term": "gas exchange surface",
         "definition": "The surface where oxygen and carbon dioxide cross "
                       "between air and blood.",
         "note": None},
        {"term": "diffusion",
         "definition": "The net movement of particles from where they are more "
                       "concentrated to where they are less concentrated, "
                       "caused by their random motion.",
         "note": "Particles cross in both directions all the time. Only the "
                 "difference between the two counts is net movement."},
        {"term": "concentration difference",
         "definition": "How much more of a substance there is on one side of a "
                       "surface than on the other.",
         "note": "This is what diffusion depends on — not on either side's "
                 "value by itself."},
        {"term": "capillary",
         "definition": "The smallest blood vessel, with a wall one cell thick, "
                       "carrying blood past every alveolus.",
         "note": None},
    ],

    # ── figures (§4.10) ─────────────────────────────────────────────────────
    # ⊕ EMPTY, and that is measured rather than assumed. This page's
    # `.ks3-legal` line (page line 311) names no figure slot — it is entirely
    # about the illustrative crossing counts and the kPa values — and the page
    # draws no figure anywhere. NOTES-B4 flag 20's one named slot,
    # `b4-gas-exchange-labelled`, is in b4-01's legal line and belongs to that
    # lesson's record, not this one. Nothing is invented to fill a slot Design
    # did not open.
    "figures": [],

    # ── core, in the approved page's document order ─────────────────────────
    "core": [
        {"type": "hook", "ref": "phenomenon", "anchor": "s-hook"},

        # #s-gradient — the flagship. Ink-dark `practical`, per the measured
        # table in `ks3_data/b4/__init__.py`: every B4 flagship sits on
        # `ks3-block ks3-dark ks3-practical`, and this one is no exception.
        # Authored inline here, where its position in the document is obvious,
        # and lifted into `activities[]` by `_normalise`.
        #
        # Payload authored against `docs/ks3/b4-inventory/PAYLOAD-SCHEMA.md` §3.
        # It elicits BREATH-06, -07 and -08; the confrontation below names and
        # kills them, and `misconceptions[].elicited_by` above carries the link.
        {"type": "crossing-counter", "id": "count-the-crossings",
         "anchor": "s-gradient", "demand": "investigate",
         "eyebrow": "At the bench · count the crossings",
         "heading": "Both directions, all the time",
         # The two-state shape: Design's `benchProgress` is a label, not a
         # count, and it opens on the resting truth rather than on zero.
         "head_counter": {"off": "both flows running", "on": "switches used"},
         "prompt": "Oxygen molecules cross the alveolus wall in both "
                   "directions every second. Switch breathing and blood flow "
                   "on and off and watch what happens to the two counts — and "
                   "to the difference between them.",

         # Both open ON, so the resting page is a working lung and the student
         # takes something away rather than adding it.
         "switches": [
             {"id": "breathing", "on_label": "Breathing: on",
              "off_label": "Breathing: stopped", "start": True},
             {"id": "blood_flow", "on_label": "Blood flow: on",
              "off_label": "Blood flow: stopped", "start": True},
         ],
         "states": STATES,

         # 90 crossings per second per kPa, on a track of 1250. The largest
         # count is 1197 (13.3 × 90), so the track holds it — the renderer
         # raises if it ever does not.
         "crossings_per_kpa": 90,
         "max_crossings": 1250,

         "tiles": {"alveolar": "Oxygen in the alveolus",
                   "blood": "Oxygen in the blood",
                   "net": "Net oxygen absorbed"},
         "kpa_format": "{v} kPa",
         "crossing_format": "{n} per second",
         # ⚖️ The NET tile hedges below 20 crossings a second and the two bars
         # never do. "About zero" is honest about a difference that has
         # collapsed; a bar reading zero would be a lie about a flow that has
         # not stopped.
         "net_zero": "about zero",
         "net_zero_below": 20,
         "bars": {"into": "Crossing INTO the blood",
                  "out_of": "Crossing OUT of the blood"}},

        # #s-built — Design's band-on-3px-ink panel with the four-row table.
        # That IS the `comparison` shell (§5.1.1): band ground, accent-text
        # eyebrow, display statement, dark header row, zebra rows, a nested key
        # fact. Rail stop 3, mirroring `s-gradient`, but NOT a `check` — there
        # is nothing to do in it, which is why it borrows its predicate. The
        # lede paragraph becomes the `references` edge above; see "What could
        # not be lifted" 1.
        {"type": "comparison", "anchor": "s-built",
         "eyebrow": "Same four features, second organ",
         "eyebrow_tone": "accent-text",
         "statement": "A villus and an alveolus solve the same problem the "
                      "same way.",
         "ground": "band",
         "columns": [
             {"caption": "In the small intestine", "tone": "on-dark"},
             {"caption": "In the lungs", "tone": "on-dark"},
         ],
         # Design paints both cells at the same weight and colour — neither
         # organ is the quiet one, which is the whole point of the row.
         "row_tones": ["ink", "ink"],
         "rows": [{"name": r["need"], "cells": [r["gut"], r["lung"]]}
                  for r in COMPARE],
         # Design nests the box inside the panel, on the card ground with the
         # accent offset shadow. `r_comparison` is the one block with a nested
         # key-fact slot, so this renders exactly where she drew it.
         "key_fact": {"ref": "both-ways-at-once", "ground": "card"}},

        {"type": "misconception", "id": "think-crossings",
         "anchor": "s-think",
         "targets": ["BREATH-06", "BREATH-07", "BREATH-08"]},
        {"type": "quiz", "ref": "ladder", "anchor": "s-ladder"},
        {"type": "summary", "ref": "key_note", "anchor": "s-keynote"},
    ],

    # ── the KEY FACT box (§4.8.1 B) ─────────────────────────────────────────
    # One per lesson, nested in the comparison above. Never amber (MRB-208).
    "key_facts": [
        {"id": "both-ways-at-once",
         "text": "Alveoli give a huge surface area, a wall one cell thick, a "
                 "dense capillary network and a moist lining. Oxygen and "
                 "carbon dioxide cross by diffusion, in both directions at "
                 "once, and the net movement follows the difference in "
                 "concentration.",
         "ground": "card",
         "eyebrow": "Key fact"},
    ],

    # ── activities (§5.5) ───────────────────────────────────────────────────
    # One entry beyond the flagship, which is authored inline in `core` and
    # lifted here by `ks3_data/b4/__init__.py::_normalise`.
    "activities": [
        # Design's `#s-think` is STATIC on this page — three quotes and three
        # paragraphs, separated by amber-topped dividers, with nothing to
        # answer. That is measured off the markup and not assumed: the section
        # contains no `ks3-options`, no commit and no reveal. So it is a
        # `confrontation` and not MRB-220 R1's `predict`; it carries no
        # completion contract and is correctly absent from the rail.
        #
        # ⚠️ The first answer drops an inline `<a href>` and keeps every word.
        # See "What could not be lifted" 2.
        {"id": "think-crossings",
         "kind": "confrontation",
         "demand": "confront all three faces of one-way diffusion in a single "
                   "pass: the pump, the intention, and the tank",
         "targets": ["BREATH-06", "BREATH-07", "BREATH-08"],
         "statements": [
             {"quote": "Oxygen is pumped across into the blood.",
              "answer": "There is no pump anywhere in the alveolus, no channel "
                        "that grabs oxygen, and nothing that spends energy "
                        "moving it. The whole transfer is diffusion, which you "
                        "met with bromine in Diffusion, and it is worth being "
                        "exact about what that means here. Oxygen molecules "
                        "are moving randomly in every direction. Some happen "
                        "to hit the alveolus wall from the air side and cross; "
                        "some happen to hit it from the blood side and cross "
                        "the other way. There are more of them on the air "
                        "side, so more crossings happen inwards than outwards, "
                        "and the difference is what your body gains. Nothing "
                        "is aimed and nothing is pushed."},
             {"quote": "Oxygen moves in because it wants to spread out "
                       "evenly.",
              "answer": "This one you also met in C1, and it is worth killing "
                        "twice because the biological version feels so much "
                        "more reasonable. A molecule has no aim, no preference "
                        "and no information about where it is. Look at the "
                        "bench above with the blood flow switched off: within "
                        "seconds the two sides equalise and the net absorption "
                        "drops to zero — not because the molecules have "
                        "finished spreading, but because crossings inwards and "
                        "crossings outwards have become equally likely. "
                        "Molecules are still moving at hundreds of metres per "
                        "second and still crossing constantly in both "
                        "directions. What has stopped is the imbalance, and "
                        "the imbalance is the only thing that was ever doing "
                        "anything."},
             {"quote": "Alveoli are where the air is stored.",
              "answer": "Nothing is stored. About half a litre of air moves in "
                        "and out with each quiet breath, and the alveolar air "
                        "is partly replaced roughly twelve times a minute — "
                        "which is precisely what keeps the alveolar oxygen "
                        "high and the gradient open. Switch breathing off on "
                        "the bench and you can watch the alveolar figure fall "
                        "as the blood takes oxygen away. The alveoli are not a "
                        "tank; they are a surface being continually refreshed "
                        "on one side and continually drained on the other. "
                        "Both flows exist to hold the difference open."},
         ]},
    ],

    # ── the mastery ladder (Law 8, §5.8) ────────────────────────────────────
    #
    # ⊕ MRB-177 RULED 17 Aug 2026 — rung 2's three distractors now state wrong
    # RULES, the same shape as the correct option, and parity follows from the
    # construct. Superseded note, kept: "⚖️ MRB-177 LENGTH PARITY — MEASURED.
    # Rung 1 passes; RUNG 2 DOES NOT, and is authored as drawn." The correct
    # option, its index and the threshold were not touched. See the docstring.
    "ladder": {
        "recall": {
            "title": "Rung 1 · Why so many",
            "q": "Why are there 500 million small alveoli rather than one "
                 "large cavity of the same total volume?",
            "options": [
                "To hold more air",
                "To give a far greater surface area for diffusion",
                "To make the lungs lighter",
                "So air can be stored for longer",
            ],
            "answer": 1,
            "feedback": {
                0: "The volume is the same in the question — that is what "
                   "makes it a fair comparison. What differs is surface.",
                2: "Mass is not the constraint. Gas exchange is limited by how "
                   "much surface the blood and air can meet across.",
                3: "Alveolar air is partly replaced about twelve times a "
                   "minute. Storing it would close the gradient rather than "
                   "help.",
            }},
        "apply": {
            "title": "Rung 2 · The one that catches people",
            "q": "You hold your breath. Blood keeps flowing. After a while, "
                 "net oxygen absorption falls close to zero. Why?",
            "options": [
                "Diffusion stops when the molecules stop moving, and with no "
                "fresh air they come to rest",
                "Oxygen moves in order to spread out evenly, and once it "
                "has, the process is finished",
                "The alveolar and blood concentrations have become nearly "
                "equal, so crossings each way balance",
                "The alveolus wall closes when no air arrives, so nothing "
                "can cross it",
            ],
            "answer": 2,
            "feedback": {
                0: "They are moving at hundreds of metres per second and still "
                   "crossing the wall constantly — in both directions.",
                1: "Nothing is trying to spread. What has changed is that "
                   "crossings in each direction have become equally likely.",
                3: "The wall is unchanged. What has disappeared is the "
                   "difference across it.",
            }},
        "explain": {
            "title": "Rung 3 · Explain the two flows",
            "q": "Explain why gas exchange needs both breathing and blood "
                 "flow, and what happens if either one stops. Use the words "
                 "diffusion and concentration difference, and do not use the "
                 "words pump, suck or want.",
            "field_label": "Your explanation",
            "placeholder": "Breathing does… blood flow does…",
            "success": [
                "Says breathing refreshes the alveolar air, keeping the oxygen "
                "concentration high on the air side.",
                "Says blood flow carries absorbed oxygen away, keeping the "
                "concentration low on the blood side.",
                "States that diffusion depends on the difference between the "
                "two sides, not on either value alone.",
                "Predicts that stopping either flow lets the two sides "
                "equalise and net exchange fall to zero.",
                "Avoids pump, suck and want, and does not describe molecules "
                "as having an aim.",
            ]},
        "produce": {
            "title": "Rung 4 · Take it somewhere new",
            "q": "At the top of a high mountain the air still contains 21% "
                 "oxygen, yet climbers become short of oxygen. Using the "
                 "bench, explain why — and why breathing faster helps a little "
                 "but does not solve it.",
            "field_label": "Your answer",
            "placeholder": "The percentage is the same, but…",
            "success": [
                "Says the air is thinner — fewer molecules in the same volume, "
                "so a lower oxygen concentration despite the same percentage.",
                "Explains that this lowers the alveolar oxygen level and so "
                "reduces the concentration difference.",
                "Says the reduced difference means slower net diffusion into "
                "the blood.",
                "Explains that breathing faster raises alveolar oxygen towards "
                "the outside value but cannot exceed it, so the difference "
                "stays smaller than at sea level.",
            ]},
    },

    # ── the key note (fixed, last, photographable) ──────────────────────────
    "key_note": "Around 500 million alveoli give a total gas exchange surface "
                "of roughly 70 m². Each has a wall one cell thick, a moist "
                "lining and a dense capillary network. Oxygen diffuses from "
                "alveolar air into the blood and carbon dioxide diffuses the "
                "other way. Breathing refreshes the air side and blood flow "
                "drains the blood side, and both are needed to keep the "
                "concentration difference open.",

    # ── the stretch layer (§5.6) — visible and opt-in to all ────────────────
    # Surfactant: a physics problem solved by a chemical. Nothing in the body
    # is retracted by it (MRB-225) — the moist lining is taught above as one of
    # the four requirements, and this gives that lining its cost as well as its
    # use.
    "stretch": [
        {"type": "explainer", "id": "why-a-wet-surface-does-not-stick-shut",
         "text": "A wet surface that thin should stick shut, and in premature "
                 "babies it sometimes does. Alveoli are lined with a film of "
                 "liquid, and the surface tension of that film pulls the walls "
                 "together — enough that inflating them would take more force "
                 "than a newborn's muscles can produce. The solution is "
                 "surfactant, a detergent-like substance made by cells in the "
                 "alveolar wall that lowers the surface tension dramatically. "
                 "It is produced late in pregnancy, from about week 24 "
                 "onwards, which is a large part of why gestational age "
                 "matters so much to a premature baby's survival. Artificial "
                 "surfactant delivered directly into the lungs has been "
                 "standard treatment since the 1990s and is one of the "
                 "clearest examples of a physics problem solved by a "
                 "chemical."},
    ],

    # Present and empty — §5.6's ruling: may be empty, never absent.
    "support": [],

    # ── end matter (§4.8.1 C, D) ────────────────────────────────────────────
    # Design heads the card "Ask Mr Badmus AI", puts the question in the
    # paragraph under it, and points the CTA back at the bench.
    "tutor": {"prompt": "Ask Mr Badmus AI",
              "body": "Want to check what happens to the crossings when the "
                      "gradient closes?",
              "cta": "Ask about this lesson",
              "anchor": "s-gradient"},

    # ⊕ `convention_note`, not `safety_note`. Design draws one plain
    # `.ks3-legal` paragraph and nothing in it is a safety instruction — it
    # declares where the numbers came from. Routing it through `safety_note`
    # would print it in the treatment reserved for real hazards, which devalues
    # the safety line wherever it is genuinely needed.
    "convention_note": "Crossing counts on the bench are illustrative numbers "
                       "chosen to make the two-way nature of diffusion "
                       "visible; they are not measured rates. Partial "
                       "pressures are typical resting values in kPa.",

    # ── working scientifically (§5.7) ───────────────────────────────────────
    # `analysis-and-evaluation`: the whole bench is reading two counts and the
    # difference between them, and rungs 2 and 4 are that reading applied to a
    # case the student has not seen.
    "ws": ["analysis-and-evaluation"],

    # ── governance (§5.10) ──────────────────────────────────────────────────
    "review_state": "draft",
}
