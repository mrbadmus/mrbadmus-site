# Prompt Y — one-word answers — apply sheet

**What it fixes.** A pupil's ONE-word answer was marked **Right** whenever that
word appeared anywhere in the model answer, and Right goes straight to
Secured. So "energy" secured *"Define activation energy." → "The minimum
amount of energy needed for particles to react"*, and "reaction" secured
*"What is a catalyst?"*. A class would find this in minutes.

**The new rule.** A one-word answer is Right on the spot only when it IS the
model answer's one key word (ignoring little words like *the*, *of*, and one-
or two-letter symbols like J, N, kg): "joules" for "Joules (J)", "newton" for
"The newton (N)". Every other one-word answer goes to the AI answer check
(the same one that already judges every longer answer), which decides
Right / Nearly / Wrong. A lone little word ("the") is still Wrong at once,
and "idk"-type answers are still No answer at once.

The site (shared/flashcard-homework.js) already uses the new rule. This
migration makes the database's copy agree, so the teacher sees the same
verdict the pupil saw.

## Files and md5s

| file | md5 |
|---|---|
| `supabase/migrations/20261004120000_y_quick_check_key_word.sql` | `e3718847dc59015b48ea78ad19bc699e` |
| `supabase/rollbacks/20261004120000_y_quick_check_key_word_rollback.sql` | `51237aa3996922a3abf550e6321c9caa` |

| function | prosrc md5 | state |
|---|---|---|
| `flashcard_quick_check` | `e7115d4ab2090efa95187e6dd6abc3d3` | production's CURRENT body (read 4 Oct 2026) — the BASE; the rollback restores it byte for byte |
| `flashcard_quick_check` | `ab1d58c567c4ad5d6b7674154011fe20` | this migration's NEW body (only the ONE WORD block differs) |

Bases of the other flashcard functions on production, read 4 Oct 2026, for the
record (this migration does not touch them): `flashcard_card_state`
`eb50f6a2…`, `flashcard_record` `9f910628…`, `flashcard_store_verdict`
`4ea8f0e1…`, `flashcard_pupil_detail` `ad73dae2…`.

## Apply steps

1. **Check the base**, on production (`urklkrwevjtlfbwnipjn`):
   `select md5(prosrc) from pg_proc where proname = 'flashcard_quick_check';`
   must read `e7115d4ab2090efa95187e6dd6abc3d3`. If not, stop.
2. Apply `20261004120000_y_quick_check_key_word.sql` (one `create or replace`,
   no DROP, no data writes, grants kept).
3. **Verify**: the same query reads `ab1d58c567c4ad5d6b7674154011fe20`
   (if your tool strips `--` comments, compare the comment-stripped body
   instead — see the note below). Then run the case table:
   `node flashcard_engine_test.js --sql` prints one query; run it on
   production; every `v` must equal the `sql` column of
   `tests/fixtures/quickcheck_cases.json` (88 cases).
4. Nothing to backfill. Answers already stored keep the verdict they were
   given.

**Comment-stripping note.** Some SQL tools drop `--` comments when they send
a function. If step 3's md5 differs, check the body with comments removed:
it must equal the migration's body with comments removed. The rule itself
is three lines (`when pa !~ ' ' and pa = (select string_agg … )`).

## Rollback

Apply `supabase/rollbacks/20261004120000_y_quick_check_key_word_rollback.sql`;
`md5(prosrc)` returns to `e7115d4a…`. The site does not need rolling back with
it: until the migration is applied — or after a rollback — the only
difference is that, for one-word answers, the teacher may see the old
instant verdict while the pupil saw the AI's.

## Rehearsal on TEST (`qeppkiswvclkkwbxmlok`)

4 Oct 2026, through the per-call Supabase connector (`project_id` given on
every call; TEST's own ref):

| step | `md5(prosrc)` | spot check |
|---|---|---|
| before | `4f1522f9…` (production's body with its `--` comments stripped — TEST drift, same logic) | — |
| apply migration | `ab1d58c567c4ad5d6b7674154011fe20` ✓ | `quick_check('energy', 'The minimum amount of energy…')` = null; `('joules','Joules (J)')` = match; grants unchanged |
| apply rollback | `e7115d4ab2090efa95187e6dd6abc3d3` ✓ (production's exact bytes) | `'energy'` = match again (the old rule) |
| re-apply migration | `ab1d58c567c4ad5d6b7674154011fe20` ✓ | TEST is left on the new body |

The case table (88 cases) was evaluated against this exact body text on TEST
and matches `shared/flashcard-homework.js` case for case
(`node flashcard_engine_test.js`: 88/88).
