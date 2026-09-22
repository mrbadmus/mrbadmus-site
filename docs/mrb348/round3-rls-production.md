# MRB-348 round three, WS-3 — the production RLS consolidation, ready to apply

22 September 2026.

**Status: the migration and its rollback are written, verified against
production's live catalogue, and NOT APPLIED.** The production BEFORE
baseline — which round two reported but never persisted — now exists as a
file. Nothing in this workstream wrote to production.

---

## 1. Short version

| | |
|---|---|
| Forward | `supabase/migrations/20260922040000_mrb348_rls_consolidate.sql` |
| Rollback | `supabase/rollbacks/20260922040000_mrb348_rls_consolidate_rollback.sql` |
| Generated from | production's own catalogue (`urklkrwevjtlfbwnipjn`), 153 policies |
| Production drift since generation | **none** — proven by hash, below |
| Proof A on production's real expressions | 108 clauses, 205 branches, **0 round-trip failures** |
| BEFORE baseline | `docs/mrb348/prod-visibility-before.json` — 290 cells, 112 non-empty, 3 grant-denied, 14,734 rows |
| Applied? | **No.** The chat applies it; then §5 is run. |

---

## 2. ⚠️ The gap this round found and closed

Round two's report states a production BEFORE baseline of *"290 cells, 126
non-empty, 16,147 rows"*. Those are **aggregates**. The per-cell digests were
computed through the connector and **never written to a file**, so there was
nothing left for an after-capture to be compared against.

That matters more than it sounds. The whole safety argument for this migration
is "apply, re-capture, and if a single digest moves the rollback goes in" — and
that sentence was not executable, because the left-hand side of the comparison
did not exist anywhere but in a paragraph of prose.

So the baseline has been re-captured and **persisted**, and the capture is now
emitted as one pinned SQL statement by `tools/mrb348_prod_visibility.py`, so
the before and after phases run the same bytes rather than two hand-written
queries that are alike.

### ⚠️ And the method had to change, because production is not TEST

The TEST rehearsal hashed **whole rows**. That is right on a database nobody is
using. Production is a live site with children submitting work while the capture
runs, so a whole-row digest moves when a pupil edits an answer — which is not a
policy change, it is Tuesday. A capture that cannot tell those apart would raise
a false alarm on nearly every table, and a proof that cries wolf is worse than no
proof, because the real signal then gets argued away.

The production digest is therefore over the **visible primary key set**. What an
RLS policy decides is exactly *which rows a person may see*; a faithful merge
leaves that set untouched whatever the rows say. On top of that every table is
frozen at `created_at <= 2026-09-22T18:00:00Z`, pinned in the script, so rows
**inserted** between the two captures cannot move a cell either.

A row **deleted** in the window still can. That is rare, the count moves with it,
and `--compare` prints the counts beside the digests and says so in terms rather
than reporting a bare mismatch.

### The numbers differ from round two's, and that is expected

112 non-empty against 126, and 14,734 rows against 16,147. Three causes, all
benign: the freeze filter excludes rows created since; the identity set is
re-derived (below); and three cells are now recorded as **grant-denied** rather
than counted. They are not the same measurement and are not claimed to be — what
matters is that the BEFORE and AFTER captures are the same measurement as each
other, which is now enforced by both phases running one generated statement.

---

## 3. The identities — production's real standings, measured not assumed

Production holds exactly **five** distinct standings. Two identities are pinned
per standing (lowest and highest profile id, so the choice is reproducible and
carries no judgement), except the single operator, plus the signed-out `anon`
role: 9 + 1 = **10 identities × 29 tables = 290 cells**.

| standing | how many exist | pinned |
|---|---|---|
| student, in a school, with a membership | 1,126 | 2 |
| student, no school, no membership (the empty-standing edge) | 58 | 2 |
| teacher, teaches classes | 7 | 2 |
| teacher + `school_admin` scope | 3 | 2 |
| `admin` role + active platform operator | 1 | 1 |
| signed out (`anon`) | — | 1 |

⚠️ **Production has no `hod` and no `slt` scope holder at all.** Both policy
branches exist and were merged, so this capture **cannot** prove those two on
production. Only TEST's rehearsal did, where fixtures for them exist. That is a
real limit of this proof and is stated here rather than rounded up.

⚠️ **`anon` is refused by the GRANT layer, not by RLS, on three tables**
(`platform_operators`, `platform_operator_activations`, `staff_scopes`). Those
cells are recorded as their own state (`n = -1`, digest `denied`) rather than as
zero rows — "cannot reach the table" and "reaches it and finds it empty" are
different facts, and flattening them would overstate what the capture proves.

No personal data left the database: the capture is counts and hashes.

---

## 4. What was verified, and how

### 4a. Production has not drifted since the migration was generated

The migration is **catalogue-pinned**: it carries the expected `qual` /
`with_check` of every policy it drops and aborts if the live catalogue differs by
a byte. Safe, but an abort at apply time is a wasted window, so drift was checked
in advance rather than discovered.

Production was asked, server-side, for a single hash over its whole policy
catalogue; the same hash was computed locally over the catalogue file the
migration was generated from:

```
production, live   : 153 policies, md5 bb032d4b1448aeb57aee1ae140ba066a
generated-from file: 153 policies, md5 bb032d4b1448aeb57aee1ae140ba066a
```

Identical. **The guard will pass.**

### 4b. The committed file really is production's, byte for byte

Rather than trust the header's claim, the migration was **regenerated** from that
verified catalogue and diffed against the committed file:

```
forward  : identical except one line — the "GENERATED FROM ... at <time>" comment
rollback : identical except the same comment
```

Not one byte of executable SQL differs. The committed pair is exactly what the
tool produces from production's catalogue, and it was left untouched — churning
the file to refresh a timestamp comment would gain nothing and lose the honest
generation time.

### 4c. Proof A passes on production's real expressions

Every merged expression split back into its top-level OR branches and compared,
as a multiset, against the originals — with a paren-, string- and
identifier-aware scanner, never a regex on `" OR "`.

```
[plan] 29 tables consolidated: 106 policies -> 88
[plan] 11 skips
[proof A] clauses checked    : 108
[proof A] branches checked   : 205
[proof A] round-trip failures: 0
```

### 4d. The baseline transcription is provably exact

The capture reaches this machine through a connector, so it is typed out — and
round two's report is explicit that hand-transcription is the one risk none of
the proofs cover. So it was checked rather than trusted: production was asked for
the md5 of its own capture blob, and the local file was hashed the same way.

```
production's own md5 : ff51e40d18378faf0946070a4dbca4f7
local file's md5     : ff51e40d18378faf0946070a4dbca4f7
```

Identical. That is two facts at once: the transcription is byte-perfect, **and**
the capture is deterministic — a second independent run of the same statement
produced the same blob, which is what the freeze filter exists to guarantee.

---

## 5. ⚠️ What happens after the chat applies it

The migration is applied **by the chat, through the Supabase connection,
byte-for-byte from the committed file**. Then:

```bash
# 1. re-capture, with the SAME generated statement
python3 tools/mrb348_prod_visibility.py --emit-sql       # paste into the connector
python3 tools/mrb348_prod_visibility.py --ingest raw_after.txt \
        --phase after --out docs/mrb348/prod-visibility-after.json

# 2. compare
python3 tools/mrb348_prod_visibility.py --compare \
        docs/mrb348/prod-visibility-before.json \
        docs/mrb348/prod-visibility-after.json
```

**If a single digest moves, the rollback goes in** —
`supabase/rollbacks/20260922040000_mrb348_rls_consolidate_rollback.sql`, which
restores all 153 originals from `public.mrb348_policy_backup` with their
expressions, their `permissive` flag, their roles and their command.

⚠️ Read the **count** beside a moved digest before concluding the policy moved: a
row deleted between the captures moves a key set with no policy having changed. A
moved digest with an **unchanged** count, or any count that **grew**, is the
serious shape — a count that grew is someone seeing more than they did.

Expected linter movement: **251 → a small residue**, the survivor being
`school_invitations`, whose two policies are granted to different roles. Closing
that is a product decision about who may read an invitation, not a performance
refactor, and it is deliberately untouched.

---

## 6. ⚠️ The TEST/production policy drift — do not ship TEST's version

This is recorded so that nobody later reaches for the TEST-generated file. It
lives at `supabase/seeds/mrb348_rehearsal_test_consolidate.sql`, deliberately
outside `migrations/` so `supabase db push` can never pick it up.

Measured, not recalled — production's verified catalogue against TEST's
pre-consolidation catalogue:

```
prod policies: 153     TEST policies: 141
present on PRODUCTION only   : 12
present on TEST only         : 0
present on BOTH but DIFFERING: 1
```

### The one differing body, and why it is the dangerous one

`profiles.profiles_teacher_read_students` (SELECT):

```
PROD: ... EXISTS (SELECT 1 FROM class_members cm
        WHERE cm.student_id = profiles.id
          AND cm.left_at IS NULL
          AND cm.deleted_at IS NULL            <-- present on production
          AND auth_user_teaches_class(cm.class_id))

TEST: ... EXISTS (SELECT 1 FROM class_members cm
        WHERE cm.student_id = profiles.id
          AND auth_user_teaches_class(cm.class_id)
          AND cm.left_at IS NULL)              <-- no deleted_at clause
```

**Shipping TEST's generated SQL to production would silently let a teacher read
the profile of a student whose membership had been soft-deleted.** The production
file keeps the clause, because it was generated from production's own catalogue.
The pinning guard would also abort rather than mis-merge — but the guard is the
second line of defence, not the reason this is safe.

### The 12 production-only policies

All on tables TEST never received — the legacy quiz and weekly-challenge estate:

```
chat_logs.Service role only for chat_logs                     [ALL]
class_teachers.class_teachers_member_read                     [SELECT]
quiz_question_attempts.qqa_self_all                           [ALL]
quiz_question_attempts.qqa_teacher_read                       [SELECT]
quiz_scores.Users can insert own scores                       [INSERT]
quiz_scores.Users can view own scores                         [SELECT]
quiz_scores.quiz_scores_teacher_read                          [SELECT]
weekly_challenges.Authenticated users can view active challenges  [SELECT]
weekly_challenges.Service role manages challenges             [ALL]
weekly_scores.Authenticated can view weekly leaderboard       [SELECT]
weekly_scores.Users can submit own score                      [INSERT]
weekly_scores.Users can view own scores                       [SELECT]
```

This is why the plan differs between the two projects — 29 tables and 106
policies on production against 25 and 97 on TEST — and why the two migrations are
not interchangeable in either direction.

---

## 7. Deviations

- **The production baseline had to be re-captured rather than re-used**, because
  round two never persisted it (§2). This was not in the brief; it was the
  difference between the stated proof being executable and not.
- **The digest method changed from whole-row to primary-key, plus a freeze
  instant** (§2). Deliberate, and stated rather than quietly substituted: the
  TEST method would have produced false alarms on a live database.
- **`freeze` cannot be a PL/pgSQL variable name** — it is a reserved keyword and
  the block fails to parse. Renamed `freeze_at`.
- **`anon` hits `insufficient_privilege` on three tables**, which aborted the
  first full capture and would have lost the other 289 cells. Now caught and
  recorded as its own state (§3).
- **The migration files were NOT regenerated into the repo**, though regeneration
  was performed and diffed (§4b). The committed pair is byte-identical in
  executable SQL, so rewriting them would only move a timestamp comment.
- **Round two's `--project prod --apply` path is still unavailable** — no
  production service-role key exists on this machine, and the Supabase CLI's
  token is in the macOS Keychain, which a non-interactive shell cannot unlock.
  The connector was the only channel, and it was used for reads only.
