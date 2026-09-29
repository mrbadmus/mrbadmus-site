# Stage B — what came off the pupil pages (phone run, 28 Sep 2026)

Rule applied: CLAUDE.md "No redundant text on any page". Every line below was
on screen somewhere else, or explained what the screen already shows.
Measured at 360×780 and 390×844, light and dark; full captures in
`~/tmp/ks3-gates/pupil-sweep/{before,after}/` (outside the repo, per MRB-346).
TEST pupils `mrb326_pupil_a` / `_b`, real data, local backend at origin/main.

## The header — one bar everywhere

| page | before | after |
|---|---|---|
| KS3 lesson (signed in) | 198.6px, four rows: brand / trail "Cells and organisation › Animal and plant cells" / theme control / "My class" pill | 58px, one row: brand · "‹ Cells and organisation" · bell · avatar · theme |
| KS3 unit index | 162.8px (signed in), 112.4px (out) | 58px |
| KS3 landing | 128.4px (in), 78px (out); "KS3" crumb | 58px; no title (the eyebrow says Key Stage 3) |
| KS4 pilot lesson | 184.3px, four rows: "GCSE › Chemistry › Bonding, structure and properties › Ionic bonding" + theme | 58px; "‹ Bonding, structure and properties" → the unit's topic page |
| Leaderboard | classic nav: ⚡ challenge, 🔍, "👤 Pupil", burger | 57px: brand · bell · avatar · theme; no title (the h1 is "Leaderboard") |
| student/classes, settings, claim-confirm | "PROD" pill, "👤 name", "⚙️ Settings", "Sign out" | brand · bell · avatar (menu: My class · Settings · Sign out) · theme |
| Assignment | 124px incl. readout; no brand below 820px; back button went to /ks3/ | bar one row with brand · class code · bell · avatar · theme; back goes to the class |

Pairs: `before-/after-ks3-lesson-390-dark-in.jpg`, `…ks3-lesson-360-light`,
`…ks3-unit-390-light-in`, `…ks4-pilot-390-light`,
`…ks4-pilot-360-dark-in`, `…leaderboard-360-light-in`,
`…student-classes-390-light-in`, `…assignment-A-360-light`,
`…assignment-A-390-dark`.

## Cut, page by page

| page | cut | why (what already says it) | level |
|---|---|---|---|
| all KS3 | the breadcrumb trail's upper rungs (KS3 › Biology › …) | the parent is the bar's title link; the lesson's eyebrow and h1 say the rest | generator |
| all KS3 | "My class" lozenge | the avatar menu carries My class | generator |
| KS4 pilot | four-rung breadcrumb | same as KS3 | ruling R-TOPBAR |
| leaderboard | the classic nav's challenge chip, search, burger drawer | not pupil-bar controls; the h1 names the page | R1 |
| pupil pages | "PROD" env pill, "👤 Name" | the avatar says who; the env pill told a pupil nothing | stamp |
| class | crumb strip "7z/Sc9 › OVERVIEW · WK 05 / 39" | class is the h1; one view; the week is on the term spine. **⚑ For Mide's veto (B-A4)** | template (PRUNE 32) |
| class | "· your class" after "Welcome back, NAME" | the class name is the h1 under it | data |
| class | "Your teacher" chip when there is no single named teacher | named nobody | data (`drop`) |
| class | empty subject pill when the class has no pill label | an empty box | data (`drop`) |
| class | bench eyebrow "ON THE BENCH NOW · DUE THU 1 OCT, 18:00" | DUE is the docket row beside it | data (`drop`) |
| class | bench blurb "15 questions … complete it before Thursday" (wide) | the button and the docket say it | data (`drop`) |
| class | checklist "Open it · Answer the 15 questions · Complete it" | the one button under it | data (empty list) |
| class | "Practice" button beside "Open the assignment" | a second route off the one job; practice now fills an empty bench | data (`drop`) |
| class | docket rows DRAWS ON (lesson list) and SET (date) | DRAWS ON repeats the topic and the lessons panel; SET is not actionable | data + LOGIC filter |
| class | docket flag "OPEN" (MISSED stays) | the button says open | data + WRAP 94 |
| class | docket "3 days left", worth line, elapsed bar | DUE is the row above; the bench meter is the progress | template (PRUNE 100) |
| class | "SET IN THIS WEEK'S ASSIGNMENT" on every lesson card | the panel is "Lessons in this topic"; four identical lines | data |
| assignment | readout "ANSWERED 00 / 15 · 15 LEFT" | the strip shows every question; "Question 01 of 15" is under it | template (PRUNE 48) |
| assignment | clock in the bar on a phone | moved into the progress strip's right end, not cut | CSS + INSERT_AT |
| assignment | LATE chip on a phone; HANDED IN chip everywhere | the work list says late; the done screen's h1 says complete | CSS / LOGIC |
| assignment done | "MARKED · WEEK 05", "70%", "03 OF 10", RIGHT stat | eyebrow says completed; score is the fraction; the wrong list is the count; RIGHT is the numerator | template (PRUNE 296/299/317) + LOGIC |
| assignment done | header clock after hand-in | TIME TAKEN in the stats row | WRAP 33 |
| flashcards overlay | "FLASHCARDS · 7z/Sc9" → "Flashcards" | the overlay opens over the class page | data |

## Kept on purpose

- The four-stat block (amendment B-A1). **Open item:** its Practice tile is
  always "—": practice rounds write nowhere (`practiceAnswered` is a
  COULD-NOT-SOURCE empty in student-live.js), so there is no count to fill.
- "0 OF 15 ANSWERED" + meter on the bench; QUESTIONS and DUE on the docket.
- Term spine, work list, lessons, shoutouts, leaderboard: untouched this run.

## Added

- An empty bench is never empty (`after-benchnext-practice-390-light.jpg`):
  missed work ("Finish it") → practice on the current topic ("Practise") →
  the next lesson ("Read it"). One heading, one line, one button.

## Swept, not converted (amendment B-A3)

weekly-challenge.html, my-challenges.html, revision.html: their classic bar
measured one row, 62px, no sideways scroll, at 360 and 390, light and dark,
signed in and out, so nothing needed fixing in place.

## Round two — the Fable pupil audit (390px on TEST, 29 Sep 2026)

| # | page | cut / change | why | level |
|---|---|---|---|---|
| 10 | class, done bench | "Good week, NAME." | the hero greets | data (`drop`) |
| 10 | class, done bench | "✓ OPENED · ANSWERED · COMPLETED 3 / 3" row | COMPLETED row + the work list say it | graft `omit` 106 |
| 10 | class, done bench | "27%" and the RIGHT "4 of 15" row → SCORE "4 / 15" | one score form, the results page's | data + graft `omit` 128 |
| 10 | class, done bench | MARKED / COMPLETE chip | SCORE and COMPLETED under it | data (`drop`) |
| 10 | class, done bench | "Practise recall"; "Revisit this week's lessons" only when there is no feedback | ONE primary action: "Read the feedback", else Revisit | graft `omit` 116 + data |
| 12 | practice round | strip "CLASS · PRACTICE  UNLIMITED ROUNDS", "ROUND 01 · UNLIMITED ROUNDS", the outer "QUESTION 01 / 05" + bar | the pill names the class, the h1 the round, the card carries its own counter and bar | graft `omit` 369/378/379 |
| 12 | practice round, flashcards | the class page no longer scrolls underneath an open overlay | a full-screen surface | after-draw hook |
| 1 | class, docket | QUESTIONS row | "0 OF 15 ANSWERED" carries the 15 | data |
| 2 | class, term spine | "TAP A WEEK TO FILTER" | the bars are buttons | template (PRUNE 114) |
| 3 | class, work rows | status "DUE" → "OPEN" | matches the spine legend DONE · OPEN · MISSED | data |
| 4 | class, flashcards card | corner count ("60") | "01 / 60" under it | data (`cardCorner`) |
| 6 | class, shoutouts | the card when there are none (and its "NONE YET") | an empty heading | WRAP 236 |
| 6 | class, leaderboard | week chips + "Show top 10" when the board is empty | one "nothing to show here yet" line is the state | WRAP 253 |
| 7 | assignment | the bare "›" beside "Confirm answer" while a pick is pending | it skipped without saving; a pupil skipped 15 questions | LOGIC |
| 8 | results | "LOOK AT QUESTION 02 ›" → "Look at it ›" | the card shows 02 | LOGIC |
| 9 | results | "Back to <class>" | the bar's "‹ class" | template (PRUNE 347) |
| 11 | class, empty bench | "36 questions" → the ROUND's size ("5 questions") | the button opens a round of 5 | data |

After: `after-class-A-390-light.jpg` (re-shot), `after-audit-assignment-picked-390-light.jpg`
(footer while a pick is pending: Back · Confirm answer). The done bench and the results
screen were not re-shot live: reaching either hands in a TEST pupil's work.

Flagged, not changed: (13) the class page's avatar-menu Settings opens Design's in-page
account sheet (it holds the bench theme) while every other page goes to
/student/settings.html — for Mide; (14) KS3 leaderboard dashes / the TEST 500; the
Practice stat tile "—".

## Round three — the Fable re-audit follow-ups (29 Sep 2026)

| # | screen | cut / change | why | level |
|---|---|---|---|---|
| S1 | class, done bench | the ~120px empty band between the topic and the docket → 36px at 390 | the pruned greeting/checklist left Design's 64px reward-slot reservation (donor 117), an empty 28px action row and a 40px column gap. Slot omitted (**⚑ a Design reservation removed — for Mide**), the row draws only when it holds "Revisit…", the gap is 20px when the columns stack | graft `omit` 117 + WRAP 10112 + STYLE_EDIT 10101 |
| S2 | class, done bench | "THE WEEK'S WORK" eyebrow | the docket says THIS WEEK'S ASSIGNMENT; the open bench has none | graft `omit` 103 |
| S3 | class, empty bench | the practice card named ONE lesson for a round drawn from several | titled from the round it opens (`recallRound()`): one lesson → its name; several → "Mixed practice", line "5 questions from 3 lessons" | data |
| S4 | practice round end | "Back to my class" | the "‹ class" pill above it | graft `omit` 424 |
| S4 | practice round end | "Go again as many times as you like. Nothing here is handed in." → "Nothing here is handed in." | "go again" is the button under it | SET_TEXT 10419 |
| C1 | practice round | "QUESTION 01 / 05 ·" / "LEVELS OF ORGANISATION" wrapped with an orphan dot | one line, ellipsised; the pips drop below when they must | STYLE_EDIT 10388 |

After: `after-reaudit-done-bench-390-light.jpg` (fixture, with the two nodes the live
data empties removed, to show the live layout), `after-reaudit-practice-end-390-light.jpg`.
(`before/after-ks3-index-390-light.jpg` were dropped to keep the folder at 24 images.)
