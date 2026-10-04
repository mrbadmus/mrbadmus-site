# Prompt Y2 — once secured, stays secured — apply sheet

**Mide's ruling, 4 Oct 2026:** "Once secured, stays secured. It also helps
with students not losing motivation."

**What it fixes.** A card's "secured" counted only the LATEST rating per card
per sitting, so a pupil who went ‹ Back to a secured card (or opened a second
tab) and answered it wrong in the same sitting un-secured it — for the
teacher, and for their own count. Now any Secured rating ever keeps the card
secured; the later attempt is still recorded and shows in the teacher's
"Later tries".

The site already uses this rule (shared/flashcard-homework.js, live with this
change). **Until this migration is applied, the teacher's pages can show such
a card as not secured while the pupil sees it secured** — apply it with, or
soon after, the site push.

## Files and md5s

| file | md5 |
|---|---|
| `supabase/migrations/20261004180000_y2_secured_stays_secured.sql` | `151e29b5c38522226a2252e1cededdff` |
| `supabase/rollbacks/20261004180000_y2_secured_stays_secured_rollback.sql` | `b18864861c7cf69f920509843d2da85e` |

| function | BASE (production, read 4 Oct 2026) | NEW |
|---|---|---|
| `flashcard_card_state` | `eb50f6a2648e23a26af93ab3691ddc65` | `ec4834b787ec5c7e4b3408c9876457bb` |
| `flashcard_record` | `9f9106282729fcd97c8975983a880cb0` | `118ade9a51a976365626b3aa67e91e56` |

Unchanged on purpose (read 4 Oct, verified to need nothing):
`flashcard_store_verdict` `4ea8f0e1…` (writes verdicts, never ratings),
`flashcard_pupil_detail` `ad73dae2…` and `flashcard_progress` `6569eb5d…`
(both read `flashcard_card_state`, so they follow it), `flashcard_quick_check`
`ab1d58c5…` (yesterday's one-word rule, already on production).

Both bodies were taken from the committed migration files whose bodies
md5-match production byte for byte, never retyped; each new body changes one
filter (and its comment):
1. `flashcard_card_state.known` = any `got_it` row of the card in
   `flashcard_reviews` (was: among the latest-per-sitting-per-phase rows).
   `secured` is `known`, so both follow.
2. `flashcard_record`'s finish walk takes every `got_it` row, so a card's
   secured moment is its FIRST `got_it` (was: groups' latest only).

## Apply steps (production, `urklkrwevjtlfbwnipjn`)

1. **Check the bases:** `select proname, md5(prosrc) from pg_proc where proname
   in ('flashcard_card_state','flashcard_record');` must read `eb50f6a2…` and
   `9f910628…`. If either differs, stop.
2. Apply `20261004180000_y2_secured_stays_secured.sql` — one transaction, two
   `create or replace`, the same `revoke` MRB-354 carried, no DROP, no data
   writes.
3. **Verify:** the same query reads `ec4834b7…` and `118ade9a…`; grants are
   `flashcard_card_state`: postgres, service_role; `flashcard_record`:
   authenticated, postgres, service_role (unchanged).
4. Nothing to backfill: secured is computed on read. A pupil whose deck is
   now all secured but has no submission gets one on their next rating or
   class-page load (the existing heal).

## Rollback

Apply the rollback file; md5s return to `eb50f6a2…` / `9f910628…`.

## Rehearsed on TEST (`qeppkiswvclkkwbxmlok`), 4 Oct 2026

| step | `flashcard_card_state` | `flashcard_record` |
|---|---|---|
| before (= production) | `eb50f6a2…` | `9f910628…` |
| apply | `ec4834b7…` ✓ | `118ade9a…` ✓ |
| rollback | `eb50f6a2…` ✓ | `9f910628…` ✓ |
| apply again (TEST left here) | `ec4834b7…` ✓ | `118ade9a…` ✓ |

Grants unchanged at every step. Behaviour, live on TEST with the real pages
(`tools/y_runthrough_live.py --phases backwalk`): ‹ Back to a secured card and
a wrong answer → pupil "10 of 10 secured", Done; teacher's pupil detail: card
Secured, history `got_it, not_yet`. With the rollback in place the same run
shows the teacher "not secured" — the check discriminates.
