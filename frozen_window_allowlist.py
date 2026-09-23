"""The MRB-352 frozen-window exception — exactly 28 ids, and no others.

⚠️ READ THIS BEFORE ADDING AN ID. You almost certainly must not.

MRB-335's rule: `bank_position` 0–11 of any bank leaf is the window that
`bankFor()` (backend) and `auto_pool()` / `compose_assignment()`
(`ks3_data/question_bank.py`) read for AUTOMATIC weekly composition, forever.
Inserting into or reordering that window changes every auto-composed
assignment the estate has ever produced, silently. That rule is untouched.

What Mide ruled on 23 Sep 2026 is narrower, and is a one-time exception of
the same shape as SYS-7. The described-diagrams audit
(`docs/diagrams/described-diagrams-audit.md`) found 28 rows inside the frozen
window whose stems DESCRIBE a picture in words instead of showing one —
"a circle with a cross inside it", "a rectangle with an arrow through it".
Those stems are the defect Mide's standing rule forbids, and they sit at the
positions every automatic assignment draws from, so leaving them is not
neutral: they are the rows pupils are most likely to meet.

THE RULING, verbatim in effect. These 28 ids — and only these — may be
edited IN PLACE, provided:

  * the `id` is unchanged;
  * the `band` (and at KS4 the `tier`) is unchanged;
  * the `bank_position` is unchanged — nothing is inserted, removed or
    reordered, so every auto window still holds the same twelve ids in the
    same order;
  * the ONLY edits are (a) attaching a `figure`, and (b) rewording the stem
    so it refers to that figure instead of describing it. Options may change
    only where the old options were themselves descriptions of a picture.

The science and the difficulty stay the same. This is a presentation repair,
not a re-authoring.

⊕ SECOND RULING — Mide, 23 Sep 2026 (MRB-352 run 2), WIDENING the first for
these same 28 ids and no others: "No question ever asks a pupil to describe a
diagram." Where one of the 28 is a description question, it is scrapped and
replaced — same id, same band and tier, same bank_position. So for these 28
ONLY, a row may now change in full: its `text`, its `options` (at KS3 each
option's `correct` flag and `why`), at KS4 its `correct_index` and its
`why` explanation, and its `figure`. What still may NOT change, under either
ruling: the `id`, the `band`, the `tier`, `triple_only`, the `bank_position`,
and the leaf's id order in positions 0–11. The examiner's replacement spec is
the run-2 content specification (`docs/diagrams/`, workstream C).

WHY IT IS SAFE, checked rather than assumed. Production was read twice —
once by the chat when the ruling was made, once again immediately before the
load (both recorded in `docs/diagrams/fix-run-report.md`):

  * 0 of these 28 ids appear in `assignment_questions.source_ref` — no
    assignment ever set has drawn one;
  * 0 appear in `assignment_question_attempts.question_ref`,
    `quiz_question_attempts.question_ref` or `unit_check_attempts`;
  * and `assignment_question_attempts` snapshots `question_text` at attempt
    time anyway, so a pupil's recorded answer keeps the wording they actually
    saw even if the bank row is later repaired.

So no pupil's past answer sits under a changed question.

EVERY OTHER FROZEN ROW IN THE ESTATE IS STILL UNTOUCHABLE. The gates that
enforce that were not weakened to make this run pass; they were taught this
one allowlist and stay strict for all ~2,800 other frozen rows. The gate that
checks it is `frozen_window_guard.py`, which proves each non-allowlisted
frozen row is byte-identical to what production serves.
"""

# ── The 14 CONFIRMED frozen rows ──────────────────────────────────────────
CONFIRMED = [
    "b10-01-e01",                            # pos  0  KS3 biology B10
    "b4-05-e04",                             # pos  3  KS3 biology B4
    "b9-01-e03",                             # pos  2  KS3 biology B9
    "b9-01-s03",                             # pos  6  KS3 biology B9
    "c1-02-e01",                             # pos  0  KS3 chemistry C1
    "p10-05-h02",                            # pos  9  KS3 physics P10
    "p4-02-h02",                             # pos  9  KS3 physics P4
    "p8-01-e04",                             # pos  3  KS3 physics P8
    "p9-02-s04",                             # pos  7  KS3 physics P9
    "ks4-circuit-symbols-e01",               # pos  0  KS4 physics electricity
    "ks4-circuit-symbols-s03",               # pos  6  KS4 physics electricity
    "ks4-circuit-symbols-h02",               # pos  9  KS4 physics electricity
    "ks4-circuit-symbols-h04",               # pos 11  KS4 physics electricity
    "ks4-acceleration-h03",                  # pos 10  KS4 physics forces
]

# ── The 14 BORDERLINE frozen rows ─────────────────────────────────────────
# Borderline rows are repaired only where the examiner judged a picture
# genuinely belongs; the ones left alone are listed, with reasons, in the
# run report. Being on this list is PERMISSION to edit, never a requirement.
BORDERLINE = [
    "b10-03-h01",                            # pos  8  KS3 biology B10
    "b3-05-s04",                             # pos  7  KS3 biology B3
    "b5-02-h01",                             # pos  8  KS3 biology B5
    "c1-02-e03",                             # pos  2  KS3 chemistry C1
    "p10-02-s03",                            # pos  6  KS3 physics P10
    "p8-06-s03",                             # pos  6  KS3 physics P8
    "p9-03-s01",                             # pos  4  KS3 physics P9
    "ks4-food-chains-webs-s02",              # pos  5  KS4 biology ecology
    "ks4-covalent-bonding-s04",              # pos  7  KS4 chemistry bonding
    "ks4-condensation-polymerisation-h02",   # pos  9  KS4 chemistry organic
    "ks4-circuit-symbols-e04",               # pos  3  KS4 physics electricity
    "ks4-circuit-symbols-e02",               # pos  1  KS4 physics electricity
    "ks4-direct-alternating-pd-h02",         # pos  9  KS4 physics electricity
    "ks4-distance-time-graphs-h02",          # pos  9  KS4 physics forces
]

ALLOWLIST = frozenset(CONFIRMED + BORDERLINE)

RULING = (
    "Mide, 23 Sep 2026 — a one-time exception to MRB-335's frozen window, "
    "covering exactly these 28 ids. Same id, same band/tier, same "
    "bank_position; the only changes are adding a figure and rewording the "
    "stem to point at it."
)

# ⊕ The second ruling, same day, same 28 ids — see the module docstring.
RULING_REPLACEMENT = (
    "Mide, 23 Sep 2026 (MRB-352 run 2) — No question ever asks a pupil to "
    "describe a diagram. A description question among these 28 is scrapped "
    "and replaced: same id, same band and tier, same bank_position. Its "
    "text, options (with their whys), correct answer, explanation and "
    "figure may all change; nothing else may."
)

# The fields either ruling lets an allowlisted row change, per key stage.
# `frozen_window_guard.py` reads these; it applies them to the 28 only.
KS3_PERMITTED_FIELDS = frozenset({"text", "options", "figure"})
KS4_PERMITTED_FIELDS = frozenset({"text", "options", "correct_index", "why",
                                  "figure"})

assert len(CONFIRMED) == 14, "the ruling covers 14 confirmed rows"
assert len(BORDERLINE) == 14, "the ruling covers 14 borderline rows"
assert len(ALLOWLIST) == 28, "the ruling covers exactly 28 ids, with no duplicates"
