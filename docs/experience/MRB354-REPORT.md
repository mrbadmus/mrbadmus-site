# MRB-354 — one word, and right first time is Secured (2 Oct 2026)

Mide's ruling, 2 Oct 2026: "Students need to be able to do flashcards and move
on … A student who saw a question and answers it directly probably has that
knowledge secured already."

## The rule as built

- **Secured** = the card has a Secured rating (stored token `got_it`), counting
  only the latest rating per card per sitting per phase (the ‹ Back rule, as
  before). One rating is enough: no second sitting, no hour gap, no
  make + review pairing.
- The verdict cap is unchanged: Wrong / blank → Not yet only; Nearly → Nearly or
  Not yet; Right → any. So nothing that wasn't typed right can be Secured.
- "I don't know" → learn step → capped at Nearly → the card comes back → typed
  right → Secured. Nearly / Wrong → model answer shown → comes back → right →
  Secured.
- A secured card stays secured. ‹ Back in the same sitting can still change a
  rating. A later sitting can only add.
- **Done = every card secured.** That is the moment the pupil reaches Done, and
  the moment the page writes the submission the teacher reads as "in".
- **One word.** "Got it" is gone from every pupil and teacher surface. Four
  states: **Secured · Nearly · Not yet · Not seen** (the progress strip, the
  legend, the chips, History, the CSV, the teacher sheet, the class cards).
- **End screen.** "N of M secured". When not all are secured, one button: **Try
  again** (leftovers only). When all are secured: **Done**, plus the quieter
  **Revise flashcards one more time**, which starts a fresh pass of the whole
  deck and never un-secures anything or un-does the homework.
- **Set work / Edit.** The Secure / Quick completion choice is gone. The page
  still sends `p_rule = 'secure'` (the server validates it), and every set,
  old or new, follows the one rule.
- The two deck modes are untouched. Make mode's writing pass ends on the same
  end screen: all secured → Done; otherwise Try again.
- **Forward ›** sits beside ‹ Back and walks back up to the card the pupil was
  on, one card a press, changing no rating. It is hidden on the newest card.

## Where the rule lives, before the SQL lands

| who | reads | why it's right today |
|---|---|---|
| pupil page | `securedInfo()` / `finishedAt()` in `shared/flashcard-homework.js`, from the pupil's own `flashcard_reviews` (now with `session_id`) | computes the new rule itself |
| teacher pages | the RPC's `known` (`teacher-data.js` fills `secured` from it; progress page, panel, CSV, class cards) | production's `known` IS the new rule; after the SQL, `secured` = `known` |
| "in" / done | `assignment_submissions`, written by the pupil page at Done and healed on load | fed by the new `finishedAt` |

## Parked SQL — `feat/mrb354-migrations` (on top of MRB-353, which is also still parked)

| file | md5 |
|---|---|
| `supabase/migrations/20261002120000_mrb354_one_word_secured.sql` | `a972486c15b75e1a0e85b798cba934e1` |
| `supabase/rollbacks/20261002120000_mrb354_one_word_secured_rollback.sql` | `0e40fd5e85e16d4e1c150b342338a9e8` |

`flashcard_card_state` `2ed66c5f…` (production) → `eb50f6a2…` (one line: secured
= `known`). `flashcard_record` `85643a2b…` (MRB-353's parked body) → `9f910628…`
(only the completion block). The rollback restores `2ed66c5f…` / `85643a2b…`
byte for byte. Order: MRB-353, then MRB-354. Apply sheet:
`supabase/MRB354-APPLY.md`. Rehearsed on TEST (apply → rollback → apply), and
TEST is left applied.

Production today (read-only): three pupil × deck pairs have any flashcard
activity; two of them rise to 10/10 secured under the new rule, and one of
those has no submission yet. It gets one on that pupil's next class-page load.

## Phone typing screen

Root cause: under a real keyboard the answer box was a fixed 64 px (an earlier
fix for Check disappearing under the keyboard on a 360×740 phone), so
everything below it was dead space, and the card had a flat percentage cap that
cut the model answer mid-line. Now (`shared/flashcard-keyboard.js`), measured
from `visualViewport` and the dialog's real rects:

- the card gets the room it needs first, down to a three-line answer box;
- if the card still has to scroll, it snaps to whole lines and shows a fade
  in its own colour (light and dark);
- the box fills down to Check, which sits 6 px above the keyboard plus the
  accessory bar.

Proof: `tools/flashcard_phone_layout.py` at 390×844 and 360×740, with a 336 px
keyboard and a 52 px accessory bar, for the normal card and the "I don't know"
step, long and short. Before: 28 failed assertions (gap 31–146 px). After: 0,
also with `offsetTop` 40.

**Mide to check on his iPhone.**

## Proof on TEST

`tools/mrb354_secured_live.py`: real pages, real TEST DB, the committed
answer-check function with only the model stubbed, 390 px. Card 1 typed right →
Secured at once. Card 2 "I don't know" → Nearly → comes back → right → Secured.
Card 3 Nearly → comes back → right → Secured. ‹ Back ×2 then Forward ›×2 lands
on the same card with no rating changed. "1 of 3 secured" → Try again →
"3 of 3 secured" → Done. The teacher's My classes card, homework row and
progress page show the pupil in, with four-state chips, and no "Got it" on any
page visited. The throwaway world was deleted by id.

## Gates

Affected slow gates were recorded on the pushed tree; `--check` was green
before the push. The flashcard homework, progress and decks drives, the
request-shape drive, student behaviour, parity and themes, and the teacher
behaviour, reach and contrast audits are all green. The fast gates also ran
and were green.

## Decisions I made

- **Built on MRB-353's parked body.** Production's `flashcard_record` is still
  `5380b3e2…`, so MRB-353 is unapplied; this migration sits on top of it, as the
  brief says.
- **The stored token stays `got_it`.** Only the word a person reads changed;
  renaming the DB value would have meant a data migration for no reader's gain.
- **Teacher pages read `known`**, not the old `secured`, so they follow the new
  rule today without waiting on the SQL.
- **Make mode's writing pass** uses the same end screen. A writing pass where
  every card is typed right is Done; the modes are otherwise untouched.
- **Fixed in passing:** the Revise button had the card's cream ink on the cream
  page and read blank. It now uses the page ink, and the homework drive measures
  its contrast.
- **Teacher-data shape:** builder A pointed one reader at `known`, but the
  object it read didn't carry `known`, so class cards would have read 0. I fixed
  it once, at the source (`teacher-data.js`), so all three readers agree.
- **Left as is:** the teacher's MCQ reteach lines ("…% of the class got it
  right") use "got it" in the ordinary sense, about multiple-choice questions,
  not the flashcard rating.
- **Accepted edge:** if a pupil reloads mid-sitting and then uses ‹ Back to
  downgrade a card that was already saved, their own screen keeps it secured
  until the next reopen, while the server stops counting it. This is rare and
  never un-does the homework.
- **Fresh-pass ordering** still reads the server's old `secured` to order a
  fresh pass. This changes which card comes first, nothing else, and goes away
  when the SQL lands.
- One inert probe function, `public.mrb354_comment_probe()`, is left on TEST:
  the connector declines an unattended DROP.
