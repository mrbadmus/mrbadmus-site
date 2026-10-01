# MRB-353 — apply sheet (for the chat)

One migration, one edge function. Production is untouched until you apply.

| file | md5 |
|---|---|
| `supabase/migrations/20261001190000_mrb353_flashcard_verdicts_finish.sql` | `c3e29e89a618016ec296c90031499939` |
| `supabase/rollbacks/20261001190000_mrb353_flashcard_verdicts_finish_rollback.sql` | `35064462e39a8f2d0f9c859937de5899` |
| `supabase/functions/flashcard-answer-check/index.ts` (on `main`) | see the report — the committed file's md5 |

Function bodies (`select md5(prosrc) from pg_proc where proname = …`):

| function | before (production today) | after this migration |
|---|---|---|
| `flashcard_record` | `5380b3e22fee33b2d0fd197fa3032916` | `85643a2ba4e2ab5bf718b0356a2401d8` |
| `flashcard_store_verdict` (new) | — | `4ea8f0e16188469d11296a1a1d985d8d` |
| `flashcard_card_state` | `2ed66c5fa80fc0b1151f0e7d8729dbf4` | unchanged — not in this migration |

## Order

1. **Check the base first.** `select md5(prosrc) from pg_proc where proname='flashcard_record'`
   must still be `5380b3e2…`. If it is not, stop: something replaced production's
   body since 1 Oct and this migration was built on the wrong base.
2. Apply the migration (it is one transaction).
3. Verify: `flashcard_record` = `85643a2b…`, `flashcard_store_verdict` = `4ea8f0e1…`,
   `flashcard_answer_verdicts` exists with RLS on and no grants to anon/authenticated,
   `flashcard_reviews.check_claimed_at` exists. Then
   `python3 tools/mrb353_body_diff.py --deployed-md5 <flashcard_record md5>` → PASS
   (the deployed body is production's old body + the finish walk + the verdict
   lookup, nothing removed).
4. Deploy `flashcard-answer-check` from `main`. Before step 2 it falls back to
   exactly its old behaviour, so the two orders are both safe; migration first
   is the intended one.
5. **Backfill — no data writes.** Each flashcard set's pending review answers are
   checked the next time a teacher opens that set's progress page (the page's
   existing batch call now checks pending REVIEW answers too, up to 200 per
   open). Watch: `select answer_check, count(*) from flashcard_reviews where
   answer is not null group by 1` — the 50 `pending` drain as sets are opened.
   ⚠️ Those 50 were never stored anywhere before this fix, so the batch asks the
   model again; a re-check can very occasionally differ from what the pupil saw
   then. From this fix on, the stored verdict is the one the pupil saw.

## Rollback

`supabase/rollbacks/20261001190000_mrb353_flashcard_verdicts_finish_rollback.sql`
restores `flashcard_record` to `5380b3e2…` byte for byte, then drops
`flashcard_store_verdict`, `flashcard_reviews.check_claimed_at` and
`flashcard_answer_verdicts`. Roll back the edge function first (or not at all —
without the table it falls back on its own).

## Rehearsal on TEST (qeppkiswvclkkwbxmlok), 1 Oct 2026

| step | result |
|---|---|
| apply | `flashcard_record` `85643a2b…` (= file), `flashcard_store_verdict` `4ea8f0e1…` (= file), ACLs `{postgres,authenticated,service_role}` / `{postgres,service_role}`, table RLS on, `tools/mrb353_body_diff.py --deployed-md5` PASS |
| rollback | `flashcard_record` back to `5380b3e2…` — production's body byte for byte — with production's ACL and `search_path` |
| ⚠️ rollback's three DROPs | **not run by this session**: the Supabase connector declines destructive statements in an unattended run. They are `drop … if exists` of objects the migration itself created. Run the rollback once on TEST yourself if you want them rehearsed. |
| re-apply | `85643a2b…` / `4ea8f0e1…` again; the `if not exists` DDL re-ran cleanly over the surviving table/column |

⚠️ TEST's `flashcard_card_state` (`50abdc35…`) is NOT production's (`2ed66c5f…`).
That is older drift on TEST; this migration does not touch that function.
