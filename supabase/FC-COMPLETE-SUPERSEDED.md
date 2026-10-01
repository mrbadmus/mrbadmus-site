# feat/fc-complete-migrations — CLOSED, superseded by `feat/mrb353-migrations`

**Do not apply anything from this branch.** The migration it held
(`20261001120000_flashcard_finish.sql`, md5 `bce3e716…`) was written from the
24 Sep `flashcard_record`, not the body live on production since 29 Sep
(`20260929120000_mrb351_pupil_flow`, prosrc md5 `5380b3e2…`). Applied, it
would have silently stopped review answers being stored
(`flashcard_events.answer`, `flashcard_reviews.answer/answer_check`) and its
rollback would have restored the 24 Sep body, not the live one. Its header
also claimed a TEST rehearsal that did not happen.

Both files are removed in this commit (still in git history at `bbd68a144`).
The round-aware finish walk now lives in
`feat/mrb353-migrations`: `supabase/migrations/20261001190000_mrb353_flashcard_verdicts_finish.sql`,
built on production's current body and rehearsed on TEST — see
`supabase/MRB353-APPLY.md` on that branch.
