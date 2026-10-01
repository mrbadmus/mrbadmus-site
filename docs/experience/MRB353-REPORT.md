# MRB-353 — flashcard verdicts, "First try", the parked finish migration, week-scoped class cards

Run of 1 Oct 2026, unattended. Started from origin/main `4a17c1aea` (the design
port, prompt Q, on main).

**TEST database login:** this session had the claude.ai Supabase connector,
scoped per call by project id, and used it on TEST (`qeppkiswvclkkwbxmlok`)
for DDL and on production (`urklkrwevjtlfbwnipjn`) for read-only SELECTs only.
The connector **declined every destructive statement** (`DROP`) in this
unattended run, so the rollback's three `DROP … IF EXISTS` lines were not
rehearsed by this session — everything else was (see item 3).

## The md5s

| what | where | md5 |
|---|---|---|
| migration `20261001190000_mrb353_flashcard_verdicts_finish.sql` | `feat/mrb353-migrations` | `c3e29e89a618016ec296c90031499939` |
| rollback `20261001190000_mrb353_flashcard_verdicts_finish_rollback.sql` | `feat/mrb353-migrations` | `35064462e39a8f2d0f9c859937de5899` |
| `flashcard_record` body after the migration (prosrc) | | `85643a2ba4e2ab5bf718b0356a2401d8` |
| `flashcard_store_verdict` body (prosrc) | | `4ea8f0e16188469d11296a1a1d985d8d` |
| `flashcard_record` body today on production, and after rollback | | `5380b3e22fee33b2d0fd197fa3032916` |
| edge function `supabase/functions/flashcard-answer-check/index.ts` | `main` | `4aab8c487b9bbdd93f4e594a61db313e` |

Apply sheet for the chat: `supabase/MRB353-APPLY.md` on `feat/mrb353-migrations`.
Order: migration → edge function → nothing else (the backfill runs itself).

## 1 · "First try" / "Later tries"

`shared/flashcard-breakdown.js`: in a make-mode set, History groups the
make-phase rating under **First try** and every later rating under **Later
tries**, and each chip's tooltip names the same words. A ready-made deck shows
its ratings with no label. The CSV export never named the phase, so it had
nothing to rename.

Proof: `flashcard_progress_drive.py` (all green; the label checks rewritten
for the new words, a new check that a ready-made deck has no label), and live
on TEST (below, check D).

## 2 · "Checking" never went away

**Cause, confirmed:** the edge function's sync check returned the verdict to
the pupil's page and wrote it onto `flashcard_pupil_cards` (the make-phase
answer) only. A review answer's `flashcard_reviews` row stayed `pending`, and
that row is what the teacher's "Latest answer" reads. Production today: 50
typed review answers pending, 9 decided.

**Fix (choice and why):** a small table, `flashcard_answer_verdicts`, holding
the verdict per (assignment, pupil, card, **exact answer text**), written only
through `flashcard_store_verdict()` (service role only). That function also
copies the verdict onto every still-pending review and make row with that
text. `flashcard_record` looks the verdict up when it writes a row later. So
neither order matters: a rating written first is updated when the verdict
lands, and a rating that arrives in a later batch is born with it. I chose a
table over stamping the `answer_submitted` event row because the page's flush
of that event can fail or time out while the check still returns a verdict
to the pupil. A verdict keyed on the text doesn't depend on the event having
arrived first.

- The **batch mode** (end of sitting / teacher opens the progress page) now
  claims and checks pending **review** answers too
  (`flashcard_reviews.check_claimed_at`). A verdict already stored for the
  same text is reused, not re-asked.
- **Backfill:** no data writes. Once the migration and function are live,
  each set's pending answers are checked the next time a teacher opens that
  set's progress page. ⚠️ The 50 existing rows were never stored anywhere, so
  they get a fresh check; it can occasionally differ from what the pupil saw
  then. From the fix on, the stored verdict is the one the pupil saw.
- **"Checking"** shows only for an answer under a minute old. An older
  pending answer shows no chip, and the pupil's verdict line drops "N
  checking". While a chip is showing, the open panel re-reads every 5 s so
  the verdict appears without reopening.
- Without the migration, the edge function falls back to exactly its old
  behaviour, so either deploy order is safe.

**Proof, live on TEST** — `tools/mrb353_verdicts_live.py`, 58/58 PASS, teardown
by snapshotted id list left nothing behind:

| deck | card | pupil typed | pupil saw | teacher saw | `flashcard_reviews.answer_check` |
|---|---|---|---|---|---|
| make, writing | unit of charge | it is the coulomb | Right | — | (make row) |
| make, review | unit of charge | yes it's the coulomb for sure | Right | Right | match |
| make, review | unit of current | roughly half an ampere | Nearly | Nearly | partial |
| make, review | unit of resistance | nah that's wrong, volts | Wrong | Wrong | no |
| ready-made | unit of frequency | it is the hertz | Right | Right | match |
| ready-made | unit of pressure | about half the pascal | Nearly | Nearly | partial |
| ready-made | unit of mass | wrong guess newtons | Wrong | Wrong | no |

The teacher never saw "Checking" on any of them. Also proved: the verdict
lands **before** the rating (the row is born decided), **after** the rating
(the row flips from pending), and through the **batch path** with no sync
check (pending → checked when the teacher's progress page opens, the model
asked exactly once). History reads First try / Later tries on the make deck
and is unlabelled on the ready-made deck. No console errors from our files.
Screenshots at 1440 and 390: `~/tmp/mrb353/shots/`.

⚠️ **What this proof stands in for:** neither TEST nor this machine has an
`ANTHROPIC_API_KEY`. The committed edge function ran locally under Deno
against the TEST database, with ONLY `checkWithModel` swapped for a
deterministic stand-in through an import map (`tools/mrb353_stub_model.ts`).
The pages, RLS, `flashcard_record`, the new SQL and the function's own code
are all real. The model's judgement is not under test here; where the verdict
is stored is.

## 3 · The parked "finished = done" migration, rebuilt

`feat/fc-complete-migrations` was built on the 24 Sep `flashcard_record`. It
is **closed** (`2f040151f`): both SQL files removed and a note pointing here.

The new migration on `feat/mrb353-migrations` is built **programmatically**
from production's current body. The pupil-flow migration file's `$$` body
md5-matches production's prosrc (`5380b3e2…`), and the builder asserts that
before it edits. It adds the round-aware finish walk (logic unchanged from
the parked port, minus its unused round counter, plus skipping ratings for
cards no longer in the deck as `finishedAt()` does) and item 2's verdict
lookup. `flashcard_card_state` is **not** touched: ‹ Back's
latest-rating-per-sitting rule stays exactly as production has it.

`tools/mrb353_body_diff.py` is the check that nothing is removed. It diffs
the migration's body against the rollback's (asserted to be production's),
fails on any removed line not on its named list of nine replaced lines, and
fails on any added line outside a `⊕ MRB-353` block that isn't one of those
lines' named replacements. With `--deployed-md5` it also proves the deployed
body is the file's.

Rehearsal on TEST:

| step | result |
|---|---|
| apply | `85643a2b…` / `4ea8f0e1…` = the files; ACLs as production's; diff check PASS against the deployed md5 |
| rollback | `flashcard_record` = `5380b3e2…`, production's body byte for byte, with its ACL and `search_path` |
| rollback's 3 DROPs | **not run** — the connector declined destructive statements unattended |
| re-apply | `85643a2b…` / `4ea8f0e1…` again |

⚠️ TEST's `flashcard_card_state` (`50abdc35…`) differs from production's
(`2ed66c5f…`) — older TEST drift. I tried to align it once and the connector
declined. This migration doesn't touch that function.

## 4 · The class page's three cards follow the selected week

`teacher_rulings.py`, regenerated by `build_all.py`. On any week but the
current one:

- **Homework card:** that week's set, closed, with its final "N of M in" and
  its not-in names. No Remind: node 236, the button, is wrapped on the card's
  Remind label, which a closed card leaves empty. One closed card plus "+N
  more", because the Reteach card only keeps its column while there are
  fewer than two homework cards.
- **Reteach:** that week's own closed set (it used to pick the newest
  released set in the whole class, open or not, which is how week 4 showed
  week 5's 2/17).
- **Keep an eye on / Worth a shoutout:** that week's results, from the same
  `wIdxs`/`wTally` the Students table's week column uses.

Proof: both classes' real sets (read from production, read-only) seeded
into the class-detail fixture, every week of the strip driven in headless
Chrome:

| class | week | homework card | reteach | keep an eye on | Students table agrees |
|---|---|---|---|---|---|
| 10h/Ph1 | 5 (current) | identical to main | identical to main | identical to main | ✓ |
| 10h/Ph1 | 4 | Closed · Changes of State · 8 of 17 in · 9 names · no Remind | Changes of State · 8/17 | low scorer + the 9 who missed it | ✓ 9 Missing |
| 10h/Ph1 | 1–3 | No work set | Nothing to reteach | no one | ✓ all "—" |
| 8r/Sc1 | 5 (current) | identical to main | identical to main | identical to main | ✓ |
| 8r/Sc1 | 3–4 | No work set | Nothing to reteach | no one | ✓ |
| 8r/Sc1 | 2 | Closed · Live Test · 1 of 2 in · +2 more | Live Test · 1/2 | Student 2 · Missed it | ✓ |
| 8r/Sc1 | 1 | Closed · Breathing… · 3 of 2 in · +1 more | Breathing… · 3/2 | Student 2 · 1 of 2 in | ✓ |

Main on the same fixture shows Mide's bug exactly: week 4 reads "Nothing open
this week" with Reteach on week 5's set at 2/17. "3 of 2 in" on 8r/Sc1 week 1
is real production data (3 submissions, 2 members), shown as-is.

Fixture caveats: the pupils are numbered placeholders and their scores are
synthetic. The proof is about which sets each card reads and whether the
cards match the table.

## Shipped

| unit | commit | live check |
|---|---|---|
| items 1–2 (site + edge function source) | `c0567b991` on main | `shared/flashcard-breakdown.js` served md5 `077dddcd…` = build; `teacher/flashcards` carries `?v=077dddcd` |
| item 4 (class page) | this commit, on main | see the closing message |
| item 3 + item 2's SQL | `f4862d7d6` on `feat/mrb353-migrations` — parked, not applied |  |
| old branch closed | `2f040151f` on `feat/fc-complete-migrations` |  |

## Decisions I made

1. **A verdict table keyed on exact answer text**, not the `answer_submitted`
   event row: it survives the case where the page's flush of the answer fails
   but the check still returns a verdict to the pupil.
2. **A sync check reuses a stored verdict for identical text** (no second
   model call): the stored verdict must be the one the pupil saw, and it saves
   a call.
3. **"In flight" = under 60 s old.** For a make answer the age is its
   make-phase rating, else the pupil's latest sitting activity. While a
   "Checking" chip shows, the open panel re-reads every 5 s.
4. **The finish walk lives only in `flashcard_record`; `flashcard_card_state`
   is untouched.** The brief named both, but the walk doesn't need
   card_state, and leaving it alone is what keeps ‹ Back's rule byte for byte.
   The rollback restores `flashcard_record` only, because that's all the
   migration replaces.
5. **The migration was built by a script from production's exact bytes**, not
   hand-copied. The committed pupil-flow file's body md5-matches production's
   prosrc, and the builder asserts it.
6. **The live proof stubs only the model call** (no API key on TEST or this
   machine); everything else is real.
7. **Past week = one closed card plus "+N more"**, so the week's Reteach card
   keeps its column (it hides when there are two homework cards).
8. **The closed card keeps its "Not in yet" names and drops only Remind**, by
   wrapping the button (node 236) on its label rather than dropping the whole
   footer.
9. **Keep an eye on / Worth a shoutout are week-scoped on past weeks**,
   overriding the 25 Sep note that they never are. Mide's 1 Oct brief asks for
   it in so many words; the current week keeps the old rule. On a past week,
   "keep an eye on" = didn't hand everything in, or under 50% on that week's
   work. "Worth a shoutout" = top score on that week's work, plus the biggest
   rise from the pupil's previous set.
10. **Reteach on a past week needs the set CLOSED**, not just released: an open
    set nobody has finished is nothing to reteach from.
11. **Item 4 was replayed onto main after unit A landed** (its one source file,
    then a rebuild) instead of rebasing generated pages, whose cache-bust
    stamps both units touch.
