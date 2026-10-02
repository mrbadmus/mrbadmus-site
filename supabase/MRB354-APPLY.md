# MRB-354 — secured, one rule — apply sheet

Mide's ruling, 2 Oct 2026: "Students need to be able to do flashcards and move
on ... A student who saw a question and answers it directly probably has that
knowledge secured already." Full rule in the commander's `RULE.md` for this
build; summary below.

## md5s (top)

| file | md5 |
|---|---|
| `supabase/migrations/20261002120000_mrb354_one_word_secured.sql` | `a972486c15b75e1a0e85b798cba934e1` |
| `supabase/rollbacks/20261002120000_mrb354_one_word_secured_rollback.sql` | `0e40fd5e85e16d4e1c150b342338a9e8` |

| function | prosrc md5 | state |
|---|---|---|
| `flashcard_card_state` | `2ed66c5fa80fc0b1151f0e7d8729dbf4` | production's CURRENT body (pupil-flow, 20260929120000) — the migration's BASE |
| `flashcard_card_state` | `eb50f6a2648e23a26af93ab3691ddc65` | this migration's NEW body (one-line `secured` change) |
| `flashcard_record` | `85643a2ba4e2ab5bf718b0356a2401d8` | MRB-353's body (PARKED, not yet on production) — the migration's BASE |
| `flashcard_record` | `9f9106282729fcd97c8975983a880cb0` | this migration's NEW body (completion block replaced) |

## Order — load-bearing

**MRB-353 first, then MRB-354.** This migration's `flashcard_record` base is
MRB-353's body (`85643a2b…`), not production's current live body
(`5380b3e2…`). MRB-353 (`supabase/migrations/20261001190000_mrb353_flashcard_verdicts_finish.sql`)
is itself still parked and NOT yet applied to production. Applying MRB-354 to
a database that is still pre-MRB-353 would not reproduce MRB-353's effects
(the verdict table, `flashcard_store_verdict()`, `check_claimed_at`) and
would leave `flashcard_record` in a shape the rest of MRB-353's migration
never created — there is no SQL guard against this, only this note and
applying the two in order.

`flashcard_card_state` has no such dependency — MRB-353 never touched it — so
its half of MRB-354 could in principle run standalone, but the migration
file updates both functions in one transaction, so in practice it's applied
as a unit, after MRB-353.

## What changes

1. **`flashcard_card_state`** — production's current body carried forward
   byte for byte except one line: the `secured` column's
   `case when completion_rule = 'quick' then known else twice end` becomes
   plain `known`. Any got_it, any phase, any sitting, ever. `completion_rule`'s
   quick/secure split, the make+review pairing and the hour-gap-between-
   sittings rule (`twice`) no longer decide `secured`. `twice` stays computed,
   unused.
2. **`flashcard_record`** — only the `⊕ MRB-353 finish walk` completion block
   (declarations + body) is replaced:
   - `done` = `v_n > 0 and bool_and(cs.secured)` read straight off
     `flashcard_card_state` (so it inherits the new rule for free).
   - `finish` = the moment the LAST card became secured: per card, the
     earliest `rated_at` among its counting got_it rows (same
     latest-per-card-per-sitting-per-phase rows `flashcard_card_state`'s own
     `r` CTE counts, reproduced against `flashcard_reviews` directly); finish
     is the MAX of those per-card moments over the deck. The finishing row's
     `event_id` feeds `v_finish_server` exactly as MRB-353 does (event's
     `server_at`, falling back to `least(rated_at, now())`).
   - Verdicts, the event/review inserts, and the returned state json are
     byte-identical to MRB-353 — untouched.

## Body-diff proof

`tools/mrb354_body_diff.py --deployed-card-state-md5 eb50f6a2648e23a26af93ab3691ddc65 --deployed-record-md5 9f9106282729fcd97c8975983a880cb0`:

```
== flashcard_card_state ==
base (rollback) md5 2ed66c5fa80fc0b1151f0e7d8729dbf4  len 2639
new  (migration) md5 eb50f6a2648e23a26af93ab3691ddc65  len 2879
lines removed: 1 (all named: True)
lines added:   6 (6 inside ⊕ MRB-354 blocks, 0 named)
== flashcard_record ==
base (rollback) md5 85643a2ba4e2ab5bf718b0356a2401d8  len 16574
new  (migration) md5 9f9106282729fcd97c8975983a880cb0  len 15337
lines removed: 64 (all named: True)
lines added:   34 (34 inside ⊕ MRB-354 blocks, 0 named)

PASS both bodies = named base + only ⊕ MRB-354 changes
```

## Grants / ACL — unchanged

Read from production before building this migration:

| function | proacl (production, current) |
|---|---|
| `flashcard_card_state` | `{postgres=X/postgres,service_role=X/postgres}` (no `authenticated` — the pupil-flow migration's `revoke all … from public, anon, authenticated` holds) |
| `flashcard_record` | `{postgres=X/postgres,authenticated=X/postgres,service_role=X/postgres}` |

The migration restates `revoke all on function public.flashcard_card_state(uuid, uuid) from public, anon, authenticated;` after its `create or replace` (matching the pupil-flow migration's own statement) and does not touch `flashcard_record`'s grants (MRB-353 didn't either — `CREATE OR REPLACE FUNCTION` preserves existing ACL regardless). Verified identical on TEST after apply (see below): same `provolatile`/`prosecdef`/`proconfig`/`proacl` as production, body only differs.

## Rehearsal on TEST (qeppkiswvclkkwbxmlok) — step by step

TEST's `flashcard_card_state` was drifted (`50abdc35bdb18d2114a0d6a3084de194`
— confirmed by direct computation to be production's exact body with its
`-- ⊕ MRB-351 pupil flow` comment block stripped; i.e. the same logic, just
missing a comment, from an earlier apply that dropped it). `flashcard_record`
was already on MRB-353's body (`85643a2ba4e2ab5bf718b0356a2401d8`, rehearsed
in the MRB-353 landing).

| step | action | `flashcard_card_state` md5 | `flashcard_record` md5 |
|---|---|---|---|
| 0 | baseline — apply the rollback's `flashcard_card_state` body only (bring TEST to production's current body; record already matched MRB-353) | `2ed66c5fa80fc0b1151f0e7d8729dbf4` ✓ | `85643a2ba4e2ab5bf718b0356a2401d8` ✓ |
| 1 | apply MRB-354 | `eb50f6a2648e23a26af93ab3691ddc65` ✓ | `9f9106282729fcd97c8975983a880cb0` ✓ |
| 2 | functional check (below) | — | — |
| 3 | apply the rollback | `2ed66c5fa80fc0b1151f0e7d8729dbf4` ✓ | `85643a2ba4e2ab5bf718b0356a2401d8` ✓ |
| 4 | re-apply MRB-354 | `eb50f6a2648e23a26af93ab3691ddc65` ✓ | `9f9106282729fcd97c8975983a880cb0` ✓ |
| 5 | re-verify functional check | — | all 10 cards `secured:true` again |

**Left APPLIED at the end** (step 4/5 state), for the commander's end-to-end
proof on TEST.

Deviation noted: step 3's first attempt was typed by hand into the SQL tool
and mis-transcribed `flashcard_record`'s submission-INSERT branch as `v_now,
v_now` instead of MRB-353's `v_finish_server, v_finish_server` — producing a
body (`3d9f1f97f43f0b719dc481193e59d4d5`) matching neither named base. The
*file* `supabase/rollbacks/20261002120000_mrb354_one_word_secured_rollback.sql`
was never wrong (confirmed `85643a2b…` by direct extraction before and after);
the error was only in one interactive SQL submission. Re-applied the body
read directly from the file and re-verified — `85643a2ba4e2ab5bf718b0356a2401d8`
confirmed. Table above shows the corrected, verified sequence.

### Functional check (step 2 / step 5) — real TEST data, no throwaway rows

Assignment `1df990b3-bf1e-4b91-918e-4a6f49ef18ef` (flashcard_mode `review`,
completion_rule `secure`, 10 cards) already had real review data from earlier
TEST sessions. Two pupils proved the rule without creating or deleting
anything:

- **Pupil `7d23dd26-ddce-485e-96b6-eac734ef19e3`** — exactly ONE `got_it`
  rating per card, all in a single sitting (session `3c88feec-…`), all
  `review` phase. Under the OLD `secure` rule this is NOT secured (one
  sitting, no make+review pairing, no second sitting an hour apart) — only
  `known`. After MRB-354: `select * from flashcard_card_state(...)` →
  **all 10 cards `secured:true`**. This is the exact case Mide's ruling names:
  one direct answer, counted.
- **Pupil `37e9109d-81d9-47c8-bb10-d4b09267fee4`** — TWO full passes (two
  sessions), both all-`got_it`. Proves the "earliest counting got_it row,
  per card, across sessions" logic picks the FIRST (earlier) session's time,
  not the second redundant pass: manual re-derivation of the migration's
  completion CTE gave `n_counting_rows=20` (2 sessions × 10 cards) and
  `v_finish_at = 2026-09-30 19:55:28.64102+00` — the last card of session 1
  (`a8ca4731-…`), not session 2.
- Re-derivation of the full completion block (done/finish/finish_event/
  finish_server) for pupil `7d23dd26` by hand, matching the migration's SQL
  exactly: `v_done=true`, `v_finish_event=0037f62a-b7bc-49bf-9b67-53b97a040a87`,
  `v_finish_at=2026-09-30 19:56:38.649293+00` (= the last of the 10 `got_it`
  ratings in that sitting), `v_finish_server=2026-09-30 19:56:32.160231+00`
  (that event's `server_at`).

No rows were inserted or deleted for this check — all data pre-existed on
TEST from earlier work. **One stray scratch function was left on TEST**:
`public.mrb354_comment_probe()` (used to confirm the apply tool does NOT
generally strip comments — it was a one-off transcription slip on my part
that omitted a comment block, not a connector bug). The connector declined
an unattended `DROP FUNCTION` for it (`{"status":"declined"}`). It is inert
(returns `1`, reads/writes nothing) — flagged here for manual cleanup or a
future attended drop; not referenced by anything.

## Rollback

`supabase/rollbacks/20261002120000_mrb354_one_word_secured_rollback.sql` —
restores `flashcard_card_state` to production's current body
(`2ed66c5fa80fc0b1151f0e7d8729dbf4`) and `flashcard_record` to MRB-353's body
(`85643a2ba4e2ab5bf718b0356a2401d8`, "production's body as the parked MRB-353
leaves it"). Undoes ONLY MRB-354 — MRB-353's verdict table,
`flashcard_store_verdict()` and `check_claimed_at` are untouched and stay in
place if MRB-353 is already applied when this is rolled back. Apply manually
only.

## Production impact (read-only, computed 2 Oct 2026, both rules derived from
`flashcard_reviews`/`flashcard_sessions` directly — the live function was
never called)

Production has very little flashcard activity so far (3 pupil×assignment
pairs with any review data at all):

| assignment | pupil | `completion_rule` | cards | secured (OLD rule) | secured (NEW rule) | already submitted? |
|---|---|---|---|---|---|---|
| `19c65ca0-…` | `a4bbb0e9-…` | secure | 10 | 3 | **10** | no |
| `19c65ca0-…` | `b0308282-…` | secure | 10 | 10 | 10 | yes |
| `f5820c3a-…` | `b0308282-…` | secure | 10 | 0 | **10** | yes |

- **Pairs whose secured count rises under the new rule: 2 of 3.**
- **Pairs that become "every card secured" under the new rule but weren't
  before: 2 of 3** (same two).
- **Of those, pairs with NO submission yet: 1** (`19c65ca0-…` /
  `a4bbb0e9-…` — this pupil will see their homework flip to Done the next
  time their page loads after this migration ships, with no further action).
  The other newly-all-secured pair already has a submission (its
  `assignment_submissions` row predates `secured`'s involvement in
  completion at all — production's CURRENT live `flashcard_record` is still
  the pre-MRB-353 body, whose `done` check already used the OLD `secured`
  definition directly; that pupil's submission must have been written before
  MRB-354 by whatever satisfied the pre-353 rule at the time, or by a non-
  flashcard path — not reopened or altered by this migration either way,
  since the `done`-and-no-submission-yet guard only ever WRITES a submission,
  never overwrites a completed one's `submitted_at`).

Query used (read-only, against `urklkrwevjtlfbwnipjn`): reproduces
`flashcard_card_state`'s `r`/`per` CTEs and both the OLD (`case when
completion_rule='quick' then known else twice end`) and NEW (`known`) secured
rules per card, aggregates per (assignment, pupil), and cross-checks against
`assignment_submissions`. No write statements were run against production.
