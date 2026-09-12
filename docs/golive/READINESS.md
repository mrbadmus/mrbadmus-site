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
