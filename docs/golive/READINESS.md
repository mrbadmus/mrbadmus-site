# Go-live readiness — Rainford High, Monday 14 September 2026

Read-only pass on 12 Sep 2026 against production (ref ending in "n") and TEST
(ref `qeppkiswvclkkwbxmlok`). Nothing was written to production. Companion
files: `dry-run.md` (your phone click-through on 8r/Sc1), `monday.md` (07:30).

## Verdict

**READY WITH ACTIONS FOR MIDE.** The composition path is proven end to end on
TEST and every Rainford cohort with pupils has the scheme rows and the bank
rows Monday needs. The actions are in §5; the first one is the only one that
matters before 07:30.

## 1. How and when week-3 work will exist — proved

**There is no cron, no timer and no manual trigger.** Production's `cron.job`
holds five consumer (B2C) jobs and nothing for schools; the backend has no
timer. A class's automatic assignment is composed **lazily, on the first
authorised read of `GET /api/class/current-assignment`** — which the pupil class
page makes on load (`shared/student-live.js:1902`). `server.js:1545–1930`:

1. `classAccess` — caller must be an active `class_members` row or an active
   `class_teachers` row for that class; anyone else (school admin included) is
   `403 not_authorised` and composes nothing.
2. `week = currentTeachingWeek(year, now)` — Sunday-rolling on the London date
   (MRB-330). Week zero is Sun 30 Aug; **Sun 13 – Sat 19 Sep is week 3.**
3. "Already composed?" — `.eq('source','auto').eq('academic_week', week)`
   served as-is. Everything below only ever CREATES; nothing retracts.
4. `auto_assignments === false` → `auto_assignments_off`, nothing composed.
5. Key stage has a bank (KS3/KS4) → else `no_bank_for_key_stage`.
6. **The hold:** `today = now.toISOString().slice(0,10) < schools.assignments_open_from`
   → `assignments_not_open_yet`. ⚠️ That is the UTC date, so on Mon 14 Sep the
   hold still bites from 00:00 to 01:00 UK and clears at 01:00 UK. Harmless.
7. `schemeLessons(cls, week)` — `scheme_of_work_entries` for the class's
   `(key_stage, year_group, tier, pathway)`, weeks ≤ 3; empty current week →
   `no_scheme_for_week`.
8. `bankFor(key_stage, slugs, 'standard', null, classBankOpts(cls))` — reads
   `classes.tier` + `classes.science_pathway` (`server.js:895`); KS4 scope is an
   INCLUSION (`ks4BankScope`); both banks are read with
   `.lt('bank_position', 12)` as a default inside `bankFor` (`server.js:976`).
9. `composeFromBank` takes 15 from current-week slugs then earlier slugs; short
   outside week one → `not_enough_banked_questions`, nothing composed.
10. Insert `assignments` (`academic_week = 3`, `release_at` NULL = visible,
    `due_at = dueAtNotBornLate(...)` = **Thu 17 Sep 18:00 UK** when
    `assignment_day_of_week` is NULL, which it is on every production class),
    then 15 `assignment_questions`; a 23505 race re-reads the winner. Idempotent
    per (class, week, auto) by the partial unique index. No notification row is
    written at composition; the bell's `New work` derives from teacher-set work only.

**So on Monday:** from 01:00 UK, the first pupil of each class to open their
class page composes that class's week-3 assignment; every later read serves the
same row. A class nobody opens has no row, and needs none.

### 1.1 TEST rehearsal — TEST Rainford's `assignments_open_from` set to 13 Sep (tomorrow), backend run locally against TEST with a pinned clock

| Clock (UK) | 7z/Sc9 KS3, 2 pupils, had a wk-2 row | 9Y1 KS3, 3 pupils, no row | 10A KS4 higher/combined | 10X1 KS4 higher/triple | 7z/Sc0-golive KS3, 0 pupils, 0 teachers |
|---|---|---|---|---|---|
| A · Sat 12 Sep 10:00 (week 2) | served its existing week-2 row, `created:false` | `assignments_not_open_yet`, opens_on 2026-09-13 | served existing week-2 row | served existing week-2 row | **403** (non-member) |
| B · Sun 13 Sep 00:30 (week 3, UTC date still the 12th) | `assignments_not_open_yet` | `assignments_not_open_yet` | `assignments_not_open_yet` | `assignments_not_open_yet` | 403 |
| C · Sun 13 Sep 07:30 (open day) | **`created:true`, week 3, 15 Qs, due Thu 17 Sep 17:00Z** | `created:true`, week 3, 15 Qs, due Mon 14 Sep 17:00Z (that TEST class has `assignment_day_of_week = 1`) | `created:true`, week 3, 15 Qs, due Thu 17 Sep | `created:true`, week 3, 15 Qs, due Thu 17 Sep | 403 |
| D · Mon 14 Sep 07:30 | same row, `created:false` | same row | same row | same row | 403; **0 assignment rows, 0 notifications** for the class after the whole run |

Database read of the four rows created at C: every one of the 60 question rows
is `band = standard` with `bank_position ≤ 7` (`all_under_12 = true`), drawn from
4 slugs each; `student_notifications` written by composition: 0.

- **KS4 tier/pathway (MRB-334) is what the composer reads:** 10A (higher,
  combined) and 10X1 (higher, triple) were composed under
  `classes.tier`/`classes.science_pathway`; every drawn row sits inside the
  inclusion scope (`tier ∈ {foundation, higher}`, `triple_only` false for
  combined, `{false,true}` for triple). All 36 production KS4 classes with
  pupils carry `tier_pathway_source = 'rule'` with tier and pathway set.
- **KS3 draws only `bank_position < 12` and the MRB-338 top-up is invisible to
  it:** TEST holds 3,711 KS3 rows at position ≥ 12 (production: 3,711; 1,237
  per band, max position 95). For the very slugs drawn at C, 60 (7z/Sc9) and
  35 (9Y1) standard-band top-up rows were available and none was drawn.

TEST was returned to its prior state (4 rows deleted, throwaway class deleted,
hold back to NULL; verified 0/0/NULL). Rig: `node -r fakeclock.js server.js`
with `MRB_FAKE_NOW`, the site drives' own pattern of a pinned `Date`.

### 1.2 Production — every cohort with pupils can compose week 3 (read-only, mirrors steps 7–9)

| Cohort | Classes (auto on, ≥1 pupil) | Week-3 scheme rows | Earlier rows | Standard-band rows at pos < 12 across weeks ≤ 3 | Result |
|---|---|---|---|---|---|
| KS3 Y7 | 7h/Sc1 7h/Sc4 7h/Sc5 7r/Sc1 7r/Sc2 7r/Sc3 7r/Sc4 | 3 (changes-of-state, animal-and-plant-cells, relative-motion) | 6 | 36 | composes 15 |
| KS3 Y8 | 8h/Sc2 8h/Sc3 8h/Sc4 8h/Sc5 8r/Sc2 8r/Sc4 8r/Sc5 | 3 | 6 | 36 | composes 15 |
| KS3 Y9 | 9h/Sc1 9h/Sc2 9h/Sc3 9h/Sc5 9r/Sc3 9r/Sc4 9r/Sc5 | 3 | 6 | 36 | composes 15 |
| KS4 Y10 foundation combined | 10h/Sc5 | 3 | 6 | 36 | composes 15 |
| KS4 Y10 higher combined | 10h/Sc1 10h/Sc2 10h/Sc3 10r/Sc1 | 3 | 6 | 36 | composes 15 |
| KS4 Y10 higher triple | 10A/Bi1 10D/Bi1 10h/Ph1 10r/Ch1 10r/Ch3 10r/Ph2 10r/Ph3 | 3 | 6 | 36 | composes 15 |
| KS4 Y11 foundation combined | 11h/Sc4 11h/Sc5 | 3 | 6 | 36 | composes 15 |
| KS4 Y11 higher combined | 11h/Sc1 11h/Sc3 11r/Sc1 11r/Sc2 | 3 | 6 | 36 | composes 15 |
| KS4 Y11 higher triple | 11A/Bi1 11D/Bi1 11h/Ch1 11h/Ph1 11r/Ch1 11r/Ch3 11r/Ph1 11r/Ph2 | 3 | 6 | 36 | composes 15 |

47 classes compose; 8r/Sc1 (2 pupils) has auto OFF, correctly. Production
holds 5 live assignments, all on 8r/Sc1: four teacher-set (one from 18 Aug, three
from 8 Sep, released, week 2) and one automatic week-1 row from 20 Aug (pre-hold).
`schools.assignments_open_from` = 2026-09-14.

## 2. The unauthenticated half — live

- Backend: 15 teacher/admin/class/student routes probed with no token and with a
  garbage token — **401 on every one, both ways** (`/api/teacher/me`, the five
  Set-work routes, `/api/admin/class-tier`, `/api/admin/school/assignments-open-from`,
  `/api/class/auto-assignments|current-assignment|practice|progress`,
  `/api/student/notifications` list and read). `/api/health` 200.
- Site: `check_ks4_live.sh` 22 pages ✅ on this build's assets;
  `check_ks3_live.sh` 185 lessons ✅; `student/class.html`,
  `student/assignment.html`, `teacher/class-detail.html`, `teacher/admin.html`,
  `teacher/classes.html` — every `/shared/*?v=` stamp byte-identical to the
  committed `mrbadmus_site/` at `dd7deaf30` (origin/main).

## 3. The 21 current-year classes with zero pupils

KS3 (9): **7h/Sc2, 7h/Sc3, 7h/Sc6, 7r/Sc5, 8h/Sc1, 8r/Sc3, 9h/Sc4, 9r/Sc1, 9r/Sc2**
KS4 (12): **10B/Bi1, 10C/Bi1, 10h/Ch1, 10h/Sc4, 10r/Ch2, 10r/Ph1, 10r/Sc2, 11B/Bi1, 11C/Bi1, 11h/Sc2, 11r/Ch2, 11r/Ph3**

All 21 have automatic work ON and 20 of them have no teacher either, so no
caller can reach the compose route for them. `11B/Bi1` has one teacher and no
pupils. Every class WITH pupils has at least one teacher.

## 4. Found and fixed

Nothing. No §4 fix was warranted: no defect found would make Monday fail.

## 5. Found and NOT fixed — with the Monday workaround

1. **The Admin "Start now" / Save control probably answers 500 on production.**
   `POST /api/admin/school/assignments-open-from` (`server.js:3388`) still builds
   its standing check through `callerClient`, which throws
   `anon_key_not_configured` without `SUPABASE_ANON_KEY`; MRB-335 recorded that
   Render's environment does not carry that variable (`server.js:1291–1296`),
   and MRB-335 rewrote `setWorkAccess` to avoid it but left this route. I cannot
   prove the variable's presence without your account or the Render dashboard.
   Reading the card is unaffected. **Monday does not depend on it** — the hold
   lifts by date. Workaround if you ever need the dial: add `SUPABASE_ANON_KEY`
   on Render (no code), or the SQL line in `monday.md` §1. The proper fix is the
   same substitution MRB-335 made — a service-role read of the same scope
   predicates — one backend route; deferred because it is a deploy, not a dial.
2. **The hold compares the UTC date** (`server.js` step 6). On 14 Sep, 00:00–01:00
   UK is still held; clears at 01:00. No action; noted so a midnight report is
   not mistaken for a failure.
3. **Separate-science classes get all three sciences.** `schemeLessons` filters
   by key stage, year group, tier and pathway, never by `science_subject`, and
   the Rainford scheme rows for Y10/Y11 triple cover biology, chemistry and
   physics lessons in one week — so 10A/Bi1 will be composed
   `cell-specialisation · model-of-the-atom · energy-changes-in-systems` on
   Monday, the same set as 10h/Ph1. Content/product call, yours; the workaround
   is the class's own switch off plus Set work.
4. **Higher KS4 classes are composed from the first twelve of each subtopic,
   whose tier is a property of the subtopic** (positions 0–11 of every KS4 slug
   share one `tier`). Week 3's three slugs are all foundation/base, so a higher
   class's week-3 set is identical to a foundation class's. Correct by the
   MRB-335 freeze; saying it so nobody reads it as a scoping bug.
5. **MRB-336's `student_controls_drive` and `export_ks3_questions_verify` were
   skipped** because they need your production account; not re-run here for
   the same reason. The dead-control questions were answered by hand in that
   run's `sweep-after.md`.

## 6. Deviations

- The prompt named `docs/mrb336/REPORT.md` and `docs/mrb336/mide-live-check.md`;
  the checkout did not have them because **local main was 33 commits behind
  origin** (MRB-336 report + MRB-338 night 1). Fast-forwarded (no local commits
  were ahead; nothing lost), then read them.
- `docs/mrb336/mide-live-check.md` is MRB-336's; MRB-335's is at
  `docs/mrb335/mide-live-check.md`. Both read.
- TEST writes for §1 only: the hold date, one throwaway class, three fixture
  pupils' passwords re-asserted (the drives' own practice), and the four rows
  the composer wrote. All but the passwords reverted and verified.
- The "roll the clock" mechanism: the drives pin `window.Date` in the page; the
  hold and the week are computed on the SERVER, so the backend was pinned the
  same way with a preload shim, restarted per instant.

---

# MRB-341 — separate-science classes compose from their own science

Shipped 12 September 2026, the evening before go-live. This section closes
§5.3 above, and it changes what §1.2 predicts for the fifteen triple classes.

## 1. What was wrong, measured

`schemeLessons()` (backend `server.js`) filtered the scheme by key stage, year
group, tier and pathway, and **never by subject**. At KS3 that is right — a KS3
week really is three lessons, one per science. At KS4 it is right for Trilogy
and wrong for separate sciences, where `10h/Ph1` is a physics class taught by a
physics teacher.

Driven end to end on TEST at week 3, on the pinned-clock harness, against the
unmodified `origin/main` (7490ca9):

| class | composed | biology | chemistry | physics |
|---|---|---|---|---|
| 10Z Physics (KS4 triple physics) | 15 | 4 | 4 | 7 |
| 10X1 Biology (KS4 triple biology) | 15 | 4 | 4 | 7 |
| 10A (KS4 combined) | 15 | 4 | 4 | 7 |

⚠️ **All three sets were byte-identical** — same fifteen `source_ref`s in the
same order. A physics class was getting **eight of its fifteen questions from
two courses it does not sit with that teacher**. Real questions, correct
science, well authored, and nothing anywhere saying so — the worst shape a
content bug takes, because every individual question passes review.

## 2. The fix

- `schemeLessons(cls, week, subjectId)` now takes the subject and applies it.
  **Pass nothing and the query is byte-identical to the one it sent before**,
  which is what every KS3 and Trilogy caller does — and what
  `/api/class/practice` keeps doing. This is a ruling about the AUTOMATIC
  COMPOSER and nothing else.
- The composer refuses when a triple class has no `science_subject`
  (`no_science_subject_for_class`, one log line, no student data) rather than
  widening back to all three. Set work's tree makes the opposite choice on
  purpose: it OFFERS a teacher a menu, composition CHOOSES for the child.
  ⚠️ On production this refusal fires on **nothing**: all 24 triple classes
  carry a `science_subject`, stamped `tier_pathway_source = 'rule'`.
- The subject resolves **by name** through the existing `scienceSubjectId`.
  The `subjects` UUIDs **differ between TEST and production** (Physics is
  `b7cc103d…` on TEST, `9aad49e5…` on production), so a hardcoded id would pass
  on one database and silently match nothing on the other.
- **KS3 has no equivalent to mirror, as expected.** `ks3_data/question_bank.py`
  `compose_assignment()` receives its lesson list from the caller and does no
  scheme read at all — no pathway, no subject, nothing to filter. KS3 has no
  pathway to be triple on. Nothing was changed there.

## 3. Proof

Gate `test_compose_subject_scope.js` (new, backend) drives the real
`schemeLessons` against the real TEST scheme across all 38 weeks and **writes
nothing**. Its central assertion is the PAIR — triple narrows AND nothing else
moves — because a filter applied one branch too wide would satisfy the first on
its own and quietly halve every KS3 and Trilogy assignment in the school.

End to end on the harness (two servers, same pinned clock — Mon 14 Sep 07:30
UK, week 3 — one at `origin/main`, one at the fix, week-3 rows wiped between
runs so the second server composed rather than serving the first's):

| class | before | after |
|---|---|---|
| 10Z Physics (triple physics) | composed 15, three sciences | **refuses** · `not_enough_banked_questions` · `subject: physics, slugs: 3, available 12 of 15` |
| 10X1 Biology (triple biology) | composed 15, three sciences | **refuses** · same, `subject: biology` |
| 10A (combined) | composed 15 | **byte-identical 15** |
| 7z/Sc9, 8X1, 9Y1 (KS3) | composed 15 each | **byte-identical 15 each** |
| throwaway triple, NULL subject | composed 15, three sciences | **refuses** · `no_science_subject_for_class` |

Green: `test_compose_subject_scope` 28, `test_assignment_compose` 109,
`test_generate_week_guard` 16, `test_set_work_v2` 177, `test_ks4_bank_read` 35,
`verify_week_truth` PASS, `assignments_hold_drive` PASS. Auto window unchanged —
every row the composer can see is still `bank_position < 12`.

TEST was returned to the state it was found in and **re-queried, not assumed**:
0 week-3 assignments, 13 auto assignments (as before), throwaway class and
membership gone, `assignments_open_from` NULL on both schools.

## 4. ⚠️ THE ONE THING TO KNOW FOR MONDAY — the fifteen triple classes compose NOTHING in week 3

This is a consequence of the ruling, not a defect in the change, and it is
arithmetic:

- A separate-sciences class draws from **a third of the slugs** a Trilogy class
  does. At week 3 the scheme holds one lesson per science per week, so its own
  science gives **3 slugs**.
- Bank positions 0–11 hold **four standard-band rows per slug**, and
  `composeFromBank` draws the standard band only.
- 3 × 4 = **12, against an assignment size of 15**. Short outside week one is
  the one outcome Mide's ruling forbids, so the class composes nothing and the
  page says "No work has been set for this week yet" — which is true.

Measured on production, read-only, for all 15 triple classes with pupils
(**379 pupil-places**): every one has 3 slugs, 36 eligible rows at
`bank_position < 12` across all bands, and **12 of them standard**.

**It heals itself at week 4**, for every cohort, measured on production:

| week | slugs (own science) | standard rows | composes |
|---|---|---|---|
| 3 (Sun 13 – Sat 19 Sep) | 3 | 12 | ✗ short |
| 4 (Sun 20 Sep) | 4 | **16** | ✓ 15 |
| 5 | 5 | 20 | ✓ |
| 6 | 6 | 24 | ✓ |

**Why this was still the right thing to ship.** The alternative on the table was
turning `auto_assignments` off for every triple class — which produces the
**same** student-facing week 3 (no automatic work) while also requiring a
production data change to make and to reverse, and it would still be wrong in
week 4 and every week after. Shipping the fix gives the same quiet week 3, no
production write, and correct work from week 4 forward. Doing nothing was the
only option that put wrong-subject work in front of 379 children.

**The classes (all higher tier, all auto on, all with `science_subject` set):**

| year | class | science | pupils |
|---|---|---|---|
| 10 | 10A/Bi1 | biology | 25 |
| 10 | 10D/Bi1 | biology | 29 |
| 10 | 10r/Ch1 | chemistry | 30 |
| 10 | 10r/Ch3 | chemistry | 27 |
| 10 | 10h/Ph1 | physics | 17 |
| 10 | 10r/Ph2 | physics | 28 |
| 10 | 10r/Ph3 | physics | 27 |
| 11 | 11A/Bi1 | biology | 26 |
| 11 | 11D/Bi1 | biology | 22 |
| 11 | 11h/Ch1 | chemistry | 18 |
| 11 | 11r/Ch1 | chemistry | 27 |
| 11 | 11r/Ch3 | chemistry | 31 |
| 11 | 11h/Ph1 | physics | 17 |
| 11 | 11r/Ph1 | physics | 27 |
| 11 | 11r/Ph2 | physics | 28 |

Nothing changed for the 32 combined and KS3 classes, proved byte-identical.

## 5. OPEN ON MIDE — one product call, and it is worth making before Monday

**Should a separate-sciences class be allowed a SHORT set in the weeks where
its own science cannot fill fifteen?** Today those classes get nothing; a short
set would give them **twelve right-subject questions** instead. Week one is
already allowed to be short (`weekOne`), so the machinery exists — it is one
condition, and it is your ruling to make, not mine. It affects week 3 only,
after which the question disappears for the rest of the year.

If you want it, say so and it is a small change Monday morning; the fallback in
the meantime is that those fifteen teachers set work by hand, which the Set work
sheet already does correctly per subject.

## 6. Deviations

- **The prompt's prod check was "≥ 36 eligible bank rows for week 3 in its own
  subject". Every class has exactly 36 — and it still cannot compose**, because
  36 is the count across all three bands and the composer draws only the
  standard band's 12. Reported both numbers rather than the passing one.
- **A second commit was needed to prove the first.** MRB-341's change is
  auth-gated AND sits behind the assignments hold (production's
  `assignments_open_from` is 2026-09-14, checked before the scheme read), so on
  12 Sep there was **no request anyone could make that would tell the old build
  from the new one** — `/api/health` answered `status: ok` either way. Added
  `build` and `branch` to `/api/health` from Render's own
  `RENDER_GIT_COMMIT`/`RENDER_GIT_BRANCH`. The deploy was then proved
  behaviourally: `build: null` → `build: 8217010e6ba59fa978fe2c1726bcca5513183244`,
  `branch: main`. Every future deploy is now provable the same way.
- The same hold is why shipping the night before was safe: the changed path is
  unreachable on production until 01:00 UK on Monday.
- A duplicate `scienceSubjectId` was written and then removed. A second `async
  function` of the same name **silently replaces** the earlier declaration
  rather than erroring, so the composer would have called whichever came last in
  the file. One name, one function — noted in the code so it is not re-added.
