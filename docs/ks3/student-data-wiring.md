# Wiring the student pages to real data — what is ready, and the one thing that is not

Measured 21 August 2026 against production (`urklkrwevjtlfbwnipjn`) and the repo at
`5e0b85458`. Written because the finding below stops a phase of work, and it could not
be filed in Linear: **the workspace has hit its free issue limit**, and MRB-275 was the
last ticket that fit. That limit is itself a blocker for the "Linear is source of truth"
convention and is Mide's to resolve.

## The short version

The **class view** can be wired. The **assignment page** cannot, and not because of the
page — the page is already correct. There is no code anywhere that *creates* an
assignment. The consumer was built; the producer never was.

## What is ready

**Year scoping is already right, and already done.** `workingAcademicYear()` in
`shared/class-entry.js:135` never touches `is_current`. It takes the earliest academic
year whose `end_date` is still ahead of today + 30 days, falling back to the latest year
if none qualifies. Verified against production today: the 2026-27 row
(`2026-09-01` → `2027-08-31`) has **`is_current = false`** — exactly the trap CLAUDE.md
warns about — and the helper still resolves to it correctly, because 21 Aug + 30 days is
20 Sep and 2027-08-31 is beyond it.

⊕ And CLAUDE.md was stale about this. It said the helper had "three hand-synced copies".
MRB-267 consolidated them on 19 Aug: there is one implementation, and the copies in
`student-data.js` and `teacher-data.js` are delegating shims that throw a named error if
`class-entry.js` is not loaded first. Corrected in place, superseded sentence kept.

**The class view's data layer exists.** `MrBadmusStudentData.loadStudentClass(classId,
viewerId)` already returns the class, the viewer's stats, assignments bucketed by due
status, the leaderboard and the shoutout feed, and it already refuses a class from a past
year with the error code `class_not_current`. No year picker is needed because no year
picker is possible.

**The attempt columns are open.** As of `20260820160311`, `quiz_question_attempts` has
`question_ref` alongside `rung`, `selected_option_letter`, `correct_option_letter`,
`criteria_met`, `criteria_total`, and its `is_correct` was already nullable. Its sibling
`assignment_question_attempts` got the same shape on 20 Aug. Both tables can now record
which question, the letter and the text separately, and a NULL correctness claim for a
self-marked rung.

**The scheme of work is populated.** `scheme_of_work_entries` holds 183 rows, matching
the 183 lesson slots the build reports.

## The blocker: nothing generates an assignment

`compose_assignment()` is real, tested and deterministic — `ks3_data/question_bank.py:201`.
It returns bank questions each carrying a permanent `id` (`c1-04-h02`), which is exactly
what `assignment_questions.source_ref` and the new `question_ref` columns are for.

**It is called from exactly one place in the entire codebase: `verify_questions.py`, a
gate.** Nothing in the product calls it. Checked: no Python caller outside that gate, no
JavaScript caller, no backend route in `mrbadmus---backend`, and no Supabase edge
function (there are three — `account-claim-confirm`, `account-claim-request`,
`roster-import` — and none mentions assignments).

So on production:

| | |
|---|---|
| live assignments | **1** |
| rows in `assignment_questions` | **2** |
| how that assignment was created | a hand-written demo migration, version `20260818234137`, `mrb238_demo_assignment_questions_8r_sc1` |

⚠️ That migration is **recorded on production but has no file in this repo** — confirmed
both ways today: it is in `supabase_migrations.schema_migrations`, and `ls
supabase/migrations/` has nothing with that version. It is the known `apply_migration`
gotcha (the MCP writes no local file and records its own version), and it means the SQL
that seeded the only assignment on production exists nowhere anybody can read it. Worth
reconstructing before it is deleted, if only so the next demo does not have to be
reinvented from scratch.
| what it is | `Particle model — recall and apply` on `8r/Sc1` |

That single assignment is the demo the housekeeping phase orders **deleted** before
Sil's rosters land. Delete it and production has zero assignments and zero
`assignment_questions`.

`student/assignment.html:127` already reads `assignment_questions` correctly, resolving
`source_ref` + `rung` into the bank question. Pointing the ported page at that read is a
small job. It would render nothing, because there is nothing to render.

**This is MRB-239** — *"Assignments are auto-generated from the scheme of work, not
authored by teachers — model recorded, four schema gaps found"* — which is in Backlog and
unbuilt, and which records four schema gaps still open.

⚑ **This is product scope, not engineering.** Whether an assignment is generated from the
scheme of work on a schedule, composed when a teacher opens a class, or authored by hand
is a decision about how the school day works. MRB-239 says a model was recorded; that
model has not been built, and building it is a new subsystem rather than the last step of
wiring an existing one. It is reserved to Mide.

## The second thing wiring will hit: the behaviour gate's oracle

Worth knowing before anyone starts, because it is not obvious.

`student_behaviour.py` drives the ported page and **Design's own delivered file** through
the same 28 interactions and asserts the visible text is identical. Design's file carries
Design's example data. The moment the ported page loads real data, every drive diverges
on every screen, and the gate stops being able to say anything at all.

That is not a reason to weaken it. The shape that survives is a **data seam**: the ported
pages should take their data from an injected source that *defaults to Design's fixture*.
The gate keeps driving the fixture and stays exactly as strict; production injects the
real load. Anything else means either deleting the drives or comparing something weaker
than visible text, and both are how a gate quietly stops covering the thing it was
written for.

The one precedent already in place is `RULED_DIVERGENCE` in `student_behaviour.py`, added
21 Aug for the leaderboard split — but that is for a handful of ruled, listed strings. It
does not scale to "all the data is different", and it should not be stretched to.

## Suggested order, if this is picked up

1. **Mide rules on how assignments come into existence** (MRB-239). Nothing below is
   worth building first.
2. Build the data seam described above, keeping Design's fixture as the default, and
   confirm `student_behaviour.py` is still green with no drives removed.
3. Wire the class view through `loadStudentClass()` — it is ready.
4. Build the recall round's source. Recall questions come from each lesson's
   `LESSON["ladder"]` `recall` and `apply` rungs, which have **no stable per-rung id**;
   `(lesson_slug, rung_name)` is the identifier available, and that is what
   `question_ref` should carry for a ladder question.
5. Only then the assignment page, against whatever step 1 produced.
