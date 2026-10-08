# The bench shows flashcard homework too (8 Oct 2026)

Mide, 8 Oct: *"why can't we have the flashcard on that bench instead when
flashcard is set."* The big dark card at the top of a pupil's class page (the
**bench**) now carries unfinished flashcard homework as well as question
homework.

## The rule (Mide confirmed)

| Unfinished homework | Unfinished deck | The bench shows |
|---|---|---|
| yes | yes | two halves — homework left, deck right; stacked on a phone (and below 1024px), homework on top |
| yes | no  | homework, whole card — unchanged |
| no  | yes | the deck, whole card |
| no  | no  | exactly as before (done bench / Mixed practice / "Finish it" / held line) |
| overdue (missed) | yes | two halves — the overdue set's "Finish it" box on the homework side, the deck on the other |
| overdue (missed) | no  | the full-size "Finish it" box fills the card — unchanged |
| open + overdue | yes | open homework \| deck; the overdue nudge is not on the bench (as today) |

Overdue unfinished homework counts as unfinished homework (Mide's lane ruling,
8 Oct). `benchNextMissed` (a past-due unfinished question set with an address)
is still the one source of truth for it. Practice, the next lesson and the done
bench are not homework, so a deck with only those fills the card.

- **Unfinished deck** = a flashcard assignment the pupil can see (released),
  not past its due date, whose submission is not yet written — the work
  list's own "done" truth (`is_submitted`), not a second one.
- **Several unfinished decks** → the one due soonest (undated last), the same
  ordering the homework fallback already used.
- **A Done deck drops off**, including in the same visit when the pupil
  finishes it from the bench (the next-soonest deck moves up, or the bench
  goes back to what it would otherwise show). Finished teacher-set homework
  already dropped off the bench; every deck is teacher-set, so decks behave
  the same. The only "done" card the bench draws is the automatic weekly
  set's, and an unfinished deck takes the card ahead of it.
- **The deck half:** the deck title, its due day (docket), its card count
  ("10 CARDS") — replaced by "4 OF 10 SECURED" with a bar once the pupil has
  started — and one button, "Complete homework" (the work row's own words for
  the same deck), which opens the deck exactly as the work row does
  (`#cards=<id>`). Secured is counted with the player's own `securedInfo`
  rule over the pupil's own ratings — the same rule that decides Done.

## What changed

`shared/student-live.js` only. The template, the fixture, the work list, the
flashcard player, the "View your flashcards" card, the stats row, teacher and
KS4 pages are untouched. The half is drawn into the bench frame after each
redraw (the same mechanism as the Mixed-practice box), using only the bench's
own tokens, so all six bench themes and light/dark follow.

## Proof

`tools/fc_bench_live.py` — a throwaway TEST world (one teacher, one KS3
class, one question homework, two 10-card decks with different due dates, a
fresh pupil per case), the real class page, a local backend at origin/main.
Cases: both, homework only, flashcards only, neither, started (4 of 10),
soonest deck done → the later deck shown, the button opens the deck, heal on
load, and **live finish** (play a whole deck through the real overlay from the
bench button; the bench updates with no reload). Phone 390 and desktop 1280,
light and dark, plus tablet 820. **984 checks, 0 failed**; teardown by
snapshotted id list left nothing behind. The live-finish case was confirmed to
fail with the fix removed. Evidence: `docs/experience/bench-shots/`.

Built by Sonnet 5.5, reviewed by Opus 5.5. The review's one must-fix (the
server writes the submission itself when the last card secures, so the page's
"just finished" hook never fired and the deck stayed on the bench until a
reload) is fixed and covered by the live-finish case.

## The two rulings (8 Oct) and what was done

1. **The work list lagged on a live finish — fixed.** The page's row patch
   wrote to a `state.work` that does not exist (the list reads
   `this.work = MRB_DATA("work")`), so it had never moved a row. It now patches
   the row in place in `window.__MRB_DATA__.work`, and the "already submitted
   by the server" branch of `recordFinish` goes through `fcPatchWorkRow` like
   the other path, so the row leaves To do, the bench drops the deck and the
   page redraws once. The patch never touches a row already done (`marked` or
   `pending`), so a revision pass on a deck finished in an earlier visit does
   not re-date it to "COMPLETED today".
2. **Overdue homework keeps its place.** With a deck to do, no open homework and
   a missed set, `drawBenchFc` has `drawBenchNext` draw its normal full
   "Finish it" box (heading, "Was due …", filled button) and treats that box as
   the homework half of the split. A pupil with no deck never takes that path,
   so their bench is as it was. The done bench is never drawn beside the deck.

Both rulings are proved in `tools/fc_bench_live.py` (new cases m-split,
m-nodeck, m-open, revise, and the work-row assertions inside live-finish). Each
was confirmed to fail with its fix removed.
