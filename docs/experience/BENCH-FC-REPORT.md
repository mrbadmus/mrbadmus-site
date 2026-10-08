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
light and dark, plus tablet 820. **690 checks, 0 failed**; teardown by
snapshotted id list left nothing behind. The live-finish case was confirmed to
fail with the fix removed. Evidence: `docs/experience/bench-shots/`.

Built by Sonnet 5.5, reviewed by Opus 5.5. The review's one must-fix (the
server writes the submission itself when the last card secures, so the page's
"just finished" hook never fired and the deck stayed on the bench until a
reload) is fixed and covered by the live-finish case.

## Open for Mide

1. **The work list lags behind on a live finish (pre-existing, not changed).**
   When a pupil finishes a deck in the overlay, the bench now updates at once,
   but the deck's work row stays in "To do" until the page is reloaded — the
   same "already written by the server" gap. It predates this change; the work
   list was out of scope, so it is left as it was. A one-line follow-up.
2. **Missed work vs a deck.** On an otherwise empty bench, a past-due unfinished
   question set used to get a "Finish it" nudge there. An open deck now takes
   the whole card instead (rule: only one thing to do → it fills the card), so
   that nudge is not on the bench while a deck is open. The missed set is still
   in the work list.
