# MRB-326 — Round two on Today and class detail

6 September 2026. Worked in `main`; two units shipped (Job 1 first, on its own, so the data
rebuild could follow it live; then Jobs 2–5 together). Real staff and children are live: every
account, class and pupil used for proof is a throwaway on the TEST project, and no name appears
below.

Mide's governing message for the run — *"PLEASE STOP REDUNDANCY ON THIS PROJECT!!!!!! SO MANY
PAGES ARE TOO REDUNDANT!!!!!"* — was applied as a rule: if a number, label or sentence appears
anywhere else on the page or is implied by the class name, it does not appear again. The cut list
is in §6.

The fidelity protocol is now permanent for teacher surfaces: Design's v3 template is the spec,
section by section. The three reconciliation tables (Today, class detail, class cards) are in this
folder and summarised in §5.

---

## 1. Job 1 — the timetable reads were wrong: actual cause, with Mide's real rows

### What the rows said (prod, before any change; counts only)

Mide's `timetable_entries` for 2026-27:

| source | live | soft-deleted | created | deleted |
|---|--:|--:|---|---|
| seeded | 0 | 21 | 31 Aug 10:01 UTC | 6 Sep 03:54:29 UTC |
| manual | 24 | 0 | 6 Sep 03:54:29 UTC | — |

`week_cycle` is NULL on every row in the table, for all 13 teachers, and no teacher had two live
rows in one slot. So suspect (a) — seeded-vs-manual duplicates the unique index cannot see — is
**not** what happened. The gap is real, though, and is closed below: the index keys on
`coalesce(week_cycle,'')`, so an `'A'` row and a NULL ("every week") row can share a slot.

The 21 soft-deleted seeded rows match the fresh departmental sheet (`Timetable/Science TT
2026-27.xlsx`, row BDA) slot for slot. Of the 24 live manual rows, **13 disagree with the sheet**.

### The mechanism — suspect (b), in two steps

**The read.** `loadTimetable()` "self-filtered" by looking up the signed-in user's classes in
`class_teachers` and then querying `timetable_entries … in('class_id', myClassIds)`. It filtered by
CLASS, never by `teacher_id`. Mide holds `school_admin`; `timetable_entries_admin_read` admits every
row in the school to that scope, so the query returned every lesson of every class he co-teaches,
taught by anyone. Ten of his twelve classes are shared (the sheet's class rows list two or three
staff codes each). That is why Monday P1 showed three classes — his 11h/Ph1 plus two colleagues'
lessons of shared classes at Mon:1 — and why Monday held ten. The earlier "11h/Sc2/3/4" sighting
predates MRB-325, when the read had no filter at all.

**The write.** `teacher/timetable.html` draws its grid from the same loader — `bySlot[weekday:period]
= classId`, last row wins each cell — so colleagues' lessons took his cells. When he corrected
Monday and pressed Save, `readGrid()` serialised every cell and `replace_timetable` did exactly what
it is built to do: retired his 21 correct rows and inserted the grid as 24 `manual` rows under HIS
`teacher_id`, one transaction, both halves stamped 03:54:29. That is why "the wrong rows survived
alongside the edit": they had become his own, and the next read merged the colleagues' rows on top
again.

Every one of the 13 wrong manual rows is the co-teacher's lesson at that slot. His Monday and the
sheet agree at P1, P3, P4; they disagree at P2 (manual 10h/Sc2, sheet 10h/Ph1) and P5 (manual
7r/Sc3, sheet 7h/Sc5) — in both cases the class shown is the colleague's lesson at that slot, the
bug's signature, so the sheet wins and the disagreement is recorded here rather than preserved.

**Suspect (c), seed drift:** none. All 12 other teachers' rows match the fresh sheet on every slot
whose class exists on the platform.

### The three layers shipped

| layer | what | where |
|---|---|---|
| read | `loadTimetable()` scopes by `.eq('teacher_id', self)` for every role; the class pre-read is gone; one row per (weekday, period, cycle), newest `updated_at` wins. The class-detail "next lesson today" read goes through the same loader. | `shared/teacher-data.js` |
| invariant | BEFORE INSERT/UPDATE trigger `timetable_entries_slot_guard` refuses a second live lesson in one (owner, year, weekday, period) when either row's `week_cycle` is NULL. Seeded-vs-manual was already caught by the index (`source` is not in the key). Rehearsed on TEST with seven proofs, including the same-statement multi-row insert; applied to prod with read-back. | `supabase/migrations/20260906044804_mrb326_timetable_slot_guard.sql` + rollback |
| data | after the read fix was live (so a re-save could not re-corrupt), the 24 manual rows were soft-deleted and the 21 sheet-exact seeded rows restored — both reversible by swapping the two updates. | prod, 6 Sep |

Fixture: `today_drive.py` case 8 — a teacher with a seeded and a manual row in one slot renders that
period ONCE (the newer wins), and a colleague's row of a shared class is never drawn.

### 13-teacher verification against the fresh sheet (prod, after the rebuild)

| code | sheet lessons | on platform | matching | not on platform (why) |
|---|--:|--:|--:|---|
| BDA | 21 | 21 | **21** | — (was 24 manual, 11 matching) |
| BLF | 19 | 14 | 14 | 5 — Y12/13 sets |
| BRB | 21 | 17 | 17 | 4 — Y12/13 |
| ELV | 12 | 12 | 12 | — |
| FNL | 20 | 17 | 17 | 3 — Y12/13 |
| HRS | 17 | 17 | 17 | — |
| HTJ | 19 | 13 | 13 | 6 — Y12/13 |
| JKS | 19 | 12 | 12 | 7 — Y12/13 |
| MKB | 20 | 16 | 16 | 4 — Y12/13 |
| RNN | 18 | 18 | 18 | — |
| SPD | 18 | 16 | 16 | 2 — Y12/13 |
| SRE | 18 | 18 | 18 | — |
| WKN | 13 | 13 | 13 | — |

Zero differing rows, zero extra rows, for all 13. The 31 unmatched sheet lessons are sixth-form
sets (12B/Ph1, 13C/Ph1, 12A/Ch1, 13D/Ch1, 12C/Bi1, 13B/Bi1, 12D/As1, 13D/Py1, 13A/Py1) with no
class row — KS5 is not on the platform. The sheet also carries a 14th code, BMT, with one lesson
(8r/Sc3, Wed P4) and cover; there is no pending_staff row for it, so it holds no timetable.
Flagged, not created — adding staff needs an email only Mide can supply.

---

## 2. Job 2 — admin, completely

### Why only some classes refused

`loadClassMatrices` drove off `class_teachers`; a class with no live link came back as
`not_authorised` → "That class is not one of yours." On prod, 25 of the 69 classes in 2026-27 have
no live link at all — their only teacher is a pending_staff row that has not claimed an account
(7 of 12 seeded staff are unclaimed). So "some refuse" meant "every class whose teacher has not
signed in yet". Fix: missing ids fall through to a read of `classes` itself. RLS remains the check —
a plain teacher's `classes_teacher_read` returns nothing for a class they do not teach and the same
throw fires; the widening is the set of classes an admin reaches, not the set of readers.
`loadStudentDetail` takes the same fallback with its membership check intact.

A second defect found on the way: an admin who teaches nothing hit "You are not teaching any
classes this year" before `load()` ever read `?class=`. The guard now stands aside when the URL
named a class; `load()` still asks the authorisation question.

### The migration (b)

`supabase/migrations/20260906054837_mrb326_admin_write_authority.sql` (+ rollback), from the
MRB-325 draft with three corrections: the condition is `auth_user_has_scope('school_admin')`, not
`auth_user_role() = 'admin'` (MRB-322: admin is the scope); `assignment_submissions` has no
`class_id`, so the predicate goes via `assignments`; and a fourth table the draft never named —
`student_notifications_teacher_send` requires `auth_user_teaches_class`, which blocked Reminders
identically. The authorship conjuncts (`author_id` / `teacher_id` / `sent_by = auth.uid()`) and the
recipient-is-a-member subquery are kept, so no admin policy is wider than its teacher counterpart.
`slt` is excluded from all seven. Rehearsed on TEST, applied to prod, seven policies read back.

### Per capability, acting as admin in a foreign class

| capability | what blocked it | fixture (teacher_admin_foreign_class_drive.py) |
|---|---|---|
| Import CSV | nothing — import.html lists staff by school; the edge function authorises by role + school | C1 |
| Pick a student | the class itself (pool = `loadClassMatrices().members`) → the fallback | C2 |
| Seating plan | nothing — `seating_plans`/`room_layouts` already carry `school_admin` | C3 |
| Marking | screen: the class; score write: RLS → `submissions_admin_write` | C4 + real 3a |
| Feedback | `submission_feedback_insert` RLS → admin insert/update policies | C5 |
| Shoutouts | `class_shoutouts_insert` RLS → admin read/insert/update policies | C6 |
| Reminders | `student_notifications_teacher_send` RLS → `student_notifications_admin_send` | C7 |
| Digest / Print | the class → the fallback | C8 |

Plus B4 (an admin with no classes of their own opens a class from the URL) and `av.C_NONE`
(a class nobody teaches opens for the admin; the plain teacher is still refused).

### Real sign-ins against TEST — `teacher_admin_real_drive.py`

Two throwaway accounts (a plain teacher with one class of two pupils; a school_admin with no
classes). Thirteen checks, all green: the teacher opens their own class and is refused a
colleague's; `classes` returns the teacher nothing for an unstaffed class (HTTP 200, `[]`); the
admin opens their colleague's class, a staffed foreign class and an unstaffed one, all marked
"Acting as admin"; `loadStudentDetail` reaches a pupil and not one off the roster; under real RLS
with the admin's JWT, marking returns the updated row, shoutout/feedback/reminder return 201, and
the plain teacher is still refused the same writes (403, 42501). Every row the drive wrote was
removed. Registered as a slow gate that skips by name without `MRB_THROWAWAY_PASSWORD`.

---

## 3. Job 3 — Today matches Design's structure

Full table: `today-reconciliation.md`. Condensed:

| Design section | shipped | verdict |
|---|---|---|
| nav: tabs, Find a student, name, Sign out | same | MATCHES (search rebuilt lazily — reads nothing until pressed) |
| nav: Design's chevron mark | plain wordmark | RULED DIVERGENCE — CLAUDE.md staff brand rule |
| nav: Admin link | when admin-scoped | RULED ADDITION — MRB-303 |
| nav: Charts button, crumb | not rendered | REMOVED — second navigation the page never had; nothing computes a crumb |
| eyebrow date line | from the clock, term from the month, year name from data; each part dropped rather than guessed | MATCHES |
| greeting, summary sentence | same | MATCHES |
| Set work | not rendered | RULED — DEAD platform-wide |
| Weekly digest / Upload timetable | same | MATCHES / RULED ADDITION (MRB-325 r1) |
| "Today's lessons" h2 | names the day when not today ("Monday's lessons") | MATCHES + ruling 2 |
| `lessonCount` beside the h2 | not rendered | REMOVED (redundancy — the summary says it) |
| Edit timetable | underline link | MATCHES |
| lesson row: period, time, code, status, chevron | same; time only when the school has one | MATCHES |
| lesson row: `l.meta` | not rendered | REMOVED — ruling 1 |
| lesson row: name-picker | icon button, own roster only | RULED ADDITION — MRB-323 |
| Students to chase: header, count, rows, reasons, Send reminders | same; pool is every class | MATCHES |
| chase footer "+N MORE ACROSS YOUR CLASSES" | an openable full list, grouped by class, collapsible | RULED CHANGE — ruling 5 |
| Worth a reteach | conditional card, Design's `< 55` threshold and colour rule | MATCHES |
| Needs setting up | not rendered | REMOVED — its rows repeat the lesson rows' own status lines; one of its two actions is DEAD |

Deleted from the live page: the weekend explainer and its weekday twin; the "Next: Monday" label;
the day-chip strip; `l.meta`; `lessonCount`; four of five copies of "No assignment set yet" (said
once, in the summary); "Send reminders" in the held state; a duplicated load-failure sentence;
"nothing to chase" (→ "29/29 in"); "· N still to hand in"; the average on rows where it is not the
reason; the reteach "+N more"; and ~80 lines of CSS inherited from admin.html that matched nothing.

`today_drive.py`: 112 checks (was 53). Every assertion that named a deleted thing now asserts its
absence; the held state asserts "No assignment set yet" appears exactly once in the document.

---

## 4. Jobs 4 and 5 — class detail, cards, copy

Full tables: `class-detail-reconciliation.md`, `classes-reconciliation.md`.

**Card size (4a).** Measured, not guessed: Design's own file rendered in headless Chrome at 1460px
against the built fixture — card 449.3 × 447.6 px, padding 20, radius 12, gap 16, fonts 13/21/34,
identical on both. The live cards were shorter for one reason: content. The reteach card drew no
bars and the homework card no Remind button, so `align-items:stretch` sized all three to a short
card. Fixing 4b and 4c restores Design's proportion honestly; no min-height was pinned (it would
reserve ~200px of empty paper under "No one flagged" on every small class).

**Reteach bars (4b).** Not `worstTwo`, not the question data: the grid was never fetched. `gridFor`
returns null for an unfetched grid and `load()` prefetched grids only for marking and insights, so
`g1` was null on every production class render and the list was correctly empty. `load()` now
prefetches ONE grid on the class screen — the newest closed paper somebody sat. New fixture
`class-detail-gridreteach` holds exactly that shape and renders both bars; Today→class detail
measured at 431 ms against the 2500 ms budget.

**The banner (4c).** "Everyone has handed this week's work in." and its Remind all / Reminded today
box are deleted (~120 lines). Reminders live on Design's dark "Remind all N" button under the
Not-in-yet chips (node 236 taken off DEAD), one group per paper so a two-assignment week cannot
nudge a child about the one they handed in; "Reminded today" after a press.

**The week sentence (4d).** "This week · 31/08/26 · 2 assignments set · Week mean 42%" is gone; the
chips stay (MRB-325 ruling 7).

**Cards (5a).** "14 STUDENTS · SCIENCE" is gone. A card is class code → homework chip or block →
activity line. The byte guard now asserts the eyebrow's absence and the ruling's presence.

**Copy (5b).** "Everyone in — nothing to chase" and cousins: where the count is already displayed
beside it (the card's "2 of 2 in", the panel's "3 of 4 in") the sentence is cut, because the numeric
form would repeat the number one line up; where the sentence was the only place the count appeared
(Today's lesson row) it is the numeric form, "29/29 in".

---

## 5. Reconciliation — class detail (condensed)

| Design section | shipped | verdict |
|---|---|---|
| (above the header) | banner deleted | REMOVED — not Design's, and redundant |
| Back to today | same | MATCHES |
| Set work | absent | REMOVED — DEAD |
| Shoutouts, Charts, Print report | same | MATCHES |
| Pick a student, Seating plan | present | RULED ADDITIONS — MRB-323, MRB-322 |
| h1 class code | same | MATCHES |
| eyebrow `klass.meta` | "16 STUDENTS" (+ "NO LESSON TODAY"/next lesson; "ACTING AS ADMIN" leads when it applies) | REMOVED in part — "YEAR 8 SCIENCE" is the class code |
| stat line | "Class mean 64% · 86% on time" | REMOVED in part — "N students to keep an eye on" is the card beside it |
| week bar chips | present | RULED ADDITION — MRB-325 r7 |
| week sentence | deleted | REMOVED — Job 4d |
| homework card + Remind all N | same, button restored | MATCHES |
| "Everyone's in — nothing to chase." | cut | REMOVED — Job 5b |
| reteach card, two bars | same, now fed | FIXED |
| keep-an-eye / shoutout card | same | MATCHES |
| Students h2 + caption | caption "NOT SUBMITTED SHOWN FIRST" | REMOVED in part — the count is in the eyebrow |
| Students table, Assignments table | same | MATCHES |
| Shoutouts composer + feed | present | RULED ADDITION — Mide, 3 Sep |

---

## 6. The cut list beyond the named instances

Named by Mide and done: lesson-row meta; weekend explainer; day-chip strip; the class-detail banner;
the week sentence; the card eyebrow; "Everyone in — nothing to chase" and cousins.

Cut under the rule on top of those: `lessonCount` ("4 LESSONS" beside a summary that says "4
lessons today"); "Needs setting up" (repeats the lesson rows' status lines); four of five copies of
"No assignment set yet" on Today; "Send reminders" in the held state; "Couldn't load your classes"
said twice; "· N still to hand in" (the subtraction of two numbers already shown); "· avg 78%" on
chase rows where the average is not the reason; the reteach "+N more"; "…and there isn't one on
your account yet"; the `.strip` band; ~80 lines of dead CSS; "YEAR 8 SCIENCE" in the class-detail
eyebrow (implied by `8r/Sc1`); "N students to keep an eye on" in the stat line (the card is beside
it); "2 STUDENTS ·" on the Students caption (the eyebrow says it); the Charts button and crumb on
Today's nav.

---

## 7. Verification

- Gates: see §7a (filled from the final run on the pushed tree).
- Prod: assets served by mrbadmus.com byte-identical to the committed build (`shared/teacher-data.js`
  hash and the `?v=` stamps compared, not just a 200).
- Paired screenshots in `shots/`: `target-today-design.png` ↔ `after-today.png`;
  `target-class-detail-design.png` ↔ `after-class-detail.png`; `after-classes-cards.png` against
  Mide's live-cards screenshot (kept in his `v3 targets/` folder, not copied — it shows real class
  data).
- TEST: two throwaway sign-in accounts, one throwaway class and two throwaway pupils (ids prefixed
  `f3260000-`), plus Job 2's throwaway paper/submission/unstaffed class, documented in
  `teacher_admin_real_drive.py` as fixture. Every row the drives wrote was removed.

### 7b. Cold pass on the merged diff, as a stranger's

An independent reviewer read the merged source diff with the brief "correctness, security, the
redundancy rule, honesty, gate weakening". Outcome:

| finding | what was done |
|---|---|
| The foreign-class drive's Reminders fixture (C7) still pressed the banner control this run deleted — a red gate waiting to happen | re-anchored on Design's in-card "Remind all N" button; re-run |
| A 1 May migration file shows a school-wide FOR ALL policy on `classes` that would let any teacher's fallback read succeed | read prod's `pg_policy`: that policy no longer exists — the July role-model swap (20260703181456) replaced it, and every admin read on classes / class_teachers / class_members / assignments is `auth_user_has_scope('school_admin') OR slt` + same school, matching the seven new writes. A plain teacher's `classes` read returns nothing (also proved under real sign-in on TEST). No gap; the teacher-live.js comment now says exactly this |
| A failed question-pack read rendered "0 topics worth a reteach" | unknown is not zero: the segment is dropped on failure, with a drive check |
| "Reminded N students" counted rows, not children | distinct students, with a drive check |
| Today printed the chase count in the panel badge and the summary, and a third time when zero | badge and zero-sentence cut; the summary is the one place |
| Class detail's no-work state said "N students" twice and "no work" three times | stat line empty when nothing is set; the count dropped from the no-work sentence |
| "Class mean" appeared in the header stat line and the reteach card | dropped from the card's line |
| Three references still cited the admin-write migration's pre-rename version | fixed |
| `class_shoutouts_admin_read` has no `deleted_at` conjunct | left as is: prod's existing `class_shoutouts_select` already grants a school_admin the school's soft-deleted shoutouts, so the new policy widens nothing |
| The claim function's retire step still uses the cycle-equal predicate, so a NULL-vs-'A' pair at claim time would now raise inside `claim_pending_staff` | OPEN, dormant: no school uses A/B cycles and the editor cannot write one. Belongs with the A/B feature (see §8) — not patched blind into a 150-line SECURITY DEFINER function today |

### 7a. Gate results

Full slow set recorded on the merged tree (`prepush_gate.py --record-all`, 6 Sep 07:29–08:19), then
recorded again on the final tree that carries this file. Verbatim:

```
PASS  verify_ks3            PASS  student_parity        PASS  student_behaviour
PASS  student_themes        PASS  today_drive           PASS  import_year_drive
PASS  teacher_behaviour     PASS  teacher_reach         PASS  teacher_picker_drive
PASS  leaderboard_behaviour PASS  ks4_chrome_drive      PASS  ks3_instrument_liveness
PASS  student_switches      PASS  3d_render_check       PASS  seating_drive
PASS  assignments_hold_drive PASS consumer_flag_off     PASS  teacher_perf_budget
PASS  teacher_admin_foreign_class                       PASS  teacher_admin_real
SKIP  student_controls_drive — no $MRB_DRIVE_PASSWORD / $MRB_TEST_STUDENT_PASSWORD (skips by name)
FAIL  3d_parity — the same three pre-existing 3D Studio findings MRB-325 recorded
      (heart-plate TODO, --st-ok-room token, two 1.5px border drifts); GATE-OVERRIDE in the commit
```

Fast set (run by the push guard): verify_questions, ks3_smoke --static, answer_positions,
answer_lengths, teacher_tells, pool_ownership, leaderboard_tells, leaderboard_seam,
ks4_chrome_tells, gate_coverage (38 gates over 38 scripts, 41 excluded with a reason),
ks3_statutory, ks3_key_audit, ks3_rail_manifest, seating_tells — all green.

Drives, per lane: `today_drive.py` 131 checks; `teacher_admin_foreign_class_drive.py` every
check, ten capabilities; `teacher_admin_real_drive.py` 13/13 under real sign-in on TEST;
`teacher_behaviour` 24 fixtures / 866 controls pressed; `teacher_reach` 24 × 2 widths / 3234
controls hit-tested; `teacher_perf_budget` all four journeys inside the 2500 ms warm-load budget.

---

## 8. Deviations and findings outside the named jobs

- `supabase/migrations/20260831144809_mrb306_replace_timetable.sql` did not exist in the repo though
  the migration is registered on both projects since 31 Aug. Recovered from prod's
  `pg_get_functiondef` and `proacl`, byte for byte.
- The MCP `apply_migration` path records its own version per project: the slot-guard landed as
  …044022 on TEST and …044804 on prod; the admin-write as …044802 and …054837. Files are named by
  prod's version and TEST's registry rows were updated to match, so all three agree.
- The auth.users trigger on TEST refuses usernames containing "teacher"/"admin" and stamps a KS4
  pathway/tier on every new profile, which the KS3 CHECK then refuses — seed-time gotchas, not
  product defects; noted for the next person who seeds a fixture.
- `class_shoutouts_select` carries a `school_admin` arm on both projects that no migration in this
  repo creates (applied ad hoc at some point). `class_shoutouts_admin_read` is kept rather than
  dropped as redundant, so the repo now states the policy.
- A co-tenant applied `mrb327_operator_email_setting` to TEST during this run; not touched.
- A second migrations gap, found while answering the reviewer: the July role-model policy swap
  (`20260703181456_role_model_policy_swaps`, registered on both projects) has no file under
  `supabase/migrations/` — the folder still carries only the 1 May role-gated policies, so a reader
  of the repo sees `classes_staff_write FOR ALL` where prod has scope-gated reads. Not recovered
  this run (it is a large policy set outside MRB-326's blast radius); named here so it is
  recovered deliberately rather than found the next time someone reads the wrong file.
- The trigger-guard's first draft claimed a BEFORE ROW trigger cannot see rows from its own
  multi-row INSERT; measured on TEST that it can, and the comment was corrected before it shipped.
- `teacher_perf_budget` and `teacher_admin_real` need credentials (`MRB_TEST_TEACHER_PASSWORD`,
  `MRB_THROWAWAY_PASSWORD`); both were run for the final receipts rather than skipped.
- Two pre-existing limitations of the timetable editor, noted not fixed: the grid has no week_cycle
  dimension (an A/B school would be flattened on save), and a live row whose class the teacher no
  longer teaches renders as a blank cell and is dropped on save.
- The Today search ("Find a student") could not borrow the generated pages' bar (it is compiled
  template driven by a self-running module with no export); it was rebuilt rather than shipped dead.
