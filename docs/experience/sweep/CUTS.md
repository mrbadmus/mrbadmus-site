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
`…ks3-unit-390-light-in`, `…ks3-index-390-light`, `…ks4-pilot-390-light`,
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
