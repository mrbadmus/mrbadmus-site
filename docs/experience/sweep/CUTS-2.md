# CUTS round 2 — C6 audit of the Sharpen build

Rule: CLAUDE.md "No redundant text on any page". **must** = a number or word
shown twice on one screen, a retired name, or a wrong readout; **should** = a
label or control the screen already implies.

## Pupil pages

Audit of build 6bd5cbc9e (feat/sharpen-p), 29 Sep 2026. It was walked at
390×844 and 1440×900, light and dark, as TEST pupils `mrb326_pupil_a` and
`mrb326_pupil_b` on real data. The audit's shots are in
`~/tmp/ks3-gates/sweep2-pupil/`. The after-shots are in
`~/tmp/ks3-gates/sharpen-C-pupil/` (from `tools/sharpen_pupil_live.py`).

States the audit could not reach with a pupil's normal clicks:
- **"Finish it"** (a completed set with questions left) only arises server-side. `tools/sharpen_pupil_live.py` builds it through the API and drives it.
- **The flashcard homework end screens.** No flashcards homework exists for these pupils on TEST.
- **claim-confirm.** Reached only without a token.

### student/classes.html

| id | now | after | sev | done / skipped (why) |
|---|---|---|---|---|
| P1 | "Pupil, pick a class" under the h1 "My classes" | remove | should | skipped — not in this batch (commander's list) |

### student/class.html

| id | now | after | sev | done / skipped (why) |
|---|---|---|---|---|
| P2 | row meta "W05 · OPEN" under a select reading "WEEK 5 · THIS WEEK" | "OPEN"; W-code only under All weeks | must | done — `metaLine` drops "W05 ·" while a week is chosen. The ≥720px row's separate W-column is Design's grid cell and stays |
| P3 | "ALL 8 · TO DO 7 · MARKED 1" over one row (week 5) | counts follow the selected week | should | done — tab counts count the chosen week (`inWk`). `student_behaviour` registers it on the two week drives only (new drive-scoped entries) |
| P4 | "LESSONS IN THIS TOPIC 04" over rows 01–04 | remove the corner "04" | must | done — `lessonCount: ""`, binding marked `drop`. Design's fixture keeps "04" |
| P5 | "SHOUTOUTS 05" over five rows | remove the corner count | should | skipped — not in this batch |
| P6 | "50%" + "CORRECT · late"; expanded "… · 5 OF 10 MARKS" | "5 / 10" + "late"; expanded "COMPLETED SUN 6 SEP" | must | done — live rows show the fraction and "late" only. The detail line drops the marks. Design's fixture rows (no `rawMax`) keep "82% CORRECT" |
| P7 | done bench "SCORE 4 / 15" and row "27% · CORRECT" | row "4 / 15" | must | done — same change as P6. AVG SCORE is an average across sets, a different fact, and stays |
| P8 | reminder "…: this week's work for 7z/Sc9 is waiting — 0 of 15 answered." | "…: this week's work is waiting." | must | done |
| P9 | "0 / 3 DONE" meter; "Nothing under this filter" with ALL 0; bench work missing from the list | meter blank when the count is unknown; "No work set" when ALL is 0; list re-read | must | done — the checklist fallback shows only on Design's fixture (`benchChecklist`). The empty list says "No work set in this class yet". When the bench names work the list lacks (lazy composition raced the list's read), the list is read once more |
| P10 | open row: "Complete homework" · "Close" | one button, no Close | should | done (Close) — every live row has ONE button. The label stays "Complete homework" / "Continue": that wording is Mide's own ruling of 22 Sep (P9 of 25 Sep), and the audit's "Open it" would reverse it |
| P11 | "LEADERBOARD CURRENT WEEK" over an empty board | drop the label when empty | should | skipped — not in this batch |
| P12 | shoutout meta "THROWAWAY TEACHER · 2 DAYS AGO" | "2 DAYS AGO" when the author is the only teacher | should | skipped — not in this batch |
| P13 | 1440 practice caption wraps "ANSWERED · / WK 05" | "THIS WEEK" | should | skipped — not in this batch |
| P14 | 1440 row sub-line "15 questions" on the bench's own set | remove for the current set | should | skipped — not in this batch |
| P15 | 1440 ~350px empty band under a single work row | stack the left column from the top | should | skipped — not in this batch |

### student/assignment.html — answering

| id | now | after | sev | done / skipped (why) |
|---|---|---|---|---|
| P16 | ≥820 bar "‹ MrBadmus · 7z/Sc9 · Forces / WEEK 05 · 15 QUESTIONS" | bar keeps "‹ 7z/Sc9" only | must | done — PRUNE 21 (`if wide` title + headMeta). Registered in `student_behaviour` |
| P17 | question 1 footer "‹ Back" beside the bar's "‹" | hide on question 1 | should | skipped — not in this batch |
| P18 | grid overlay "ALL 15 QUESTIONS" | "Questions" | should | skipped — not in this batch |

### student/assignment.html — results ("See your answers")

| id | now | after | sev | done / skipped (why) |
|---|---|---|---|---|
| P19 | "WRONG 11 · MISSED 00 · TIME TAKEN 00:46" | "TIME TAKEN 00:46"; MISSED only when > 0 | should | done — live page only (`doneAll`) |
| P20 | footer "Look through all 15 ›" under the full list | remove | should | done — PRUNE 344 |
| P21 | "COMPLETED 29 SEP, 17:39 · REVISED AFTER MARKING" wraps at 390 | drop the clock time | should | done — the time drops only when revised, so an ordinary "Completed 29 Sep, 17:39" keeps it |
| P22 | 1440: right-answered cards stretch to a wrong neighbour's height | `align-items:start` | should | done — CSS only (`[data-mrb-results-grid]`) |
| — | "See your answers" on a set the server cannot serve falls through silently to this week's set | `SAY.noWork` | (commander) | done — a named assignment that comes back as a different set, or with no questions, says "No work has been set for this week yet." |

### Flashcards

| id | now | after | sev | done / skipped (why) |
|---|---|---|---|---|
| P23 | eyebrow "DEFINITION" over "Define: evaporating" | no eyebrow when the prompt opens "Define:" | should | done |
| — | "SAVED ON THIS PHONE" on the homework strip AND the end screen | once | (commander) | done — the end screen no longer repeats it (`hwEndOffline: false`); the strip keeps it |

### student/settings.html

| id | now | after | sev | done / skipped (why) |
|---|---|---|---|---|
| P24 | "Manage your MrBadmusAI account." under the h1 | remove | must | done |
| P25 | h2 "Used MrBadmusAI before with a different email?" + 60-word paragraph | h2 "Used a different email before?"; one sentence | must | done |
| P26 | "Still stuck? Ask your teacher — they can help get your old progress moved across." | "Stuck? Ask your teacher." | should | skipped — not in this batch |
| P27 | "← Back home" above the h1 | remove | should | skipped — not in this batch |

### student/claim-confirm.html

| id | now | after | sev | done / skipped (why) |
|---|---|---|---|---|
| P28 | "This link is invalid or incomplete. If you're unsure, ask …" | "Ask for a new one in Account settings, or ask your teacher." | must | done |
| P29 | "Go to sign in" to a signed-in pupil | "Account settings" when a session exists | should | done |

### leaderboard.html

| id | now | after | sev | done / skipped (why) |
|---|---|---|---|---|
| P30 | 390: the table clips at "RANK · STUDENT · PA" | wrap or show the scroll | should | skipped — not in this batch; the leaderboard is its own generated port |

### KS3 lesson — top bar only

| id | now | after | sev | done / skipped (why) |
|---|---|---|---|---|
| P31 | 390: bar title cut to "‹ Health and d…" above the eyebrow saying it whole | "‹" alone below 420px | should | done — `shared/topbar.css`, KS3 bar only: below 420px the link keeps its words for a screen reader (font-size 0) and draws the "‹" alone. No lesson content touched |

### Also in this round (commander)

- **A revision queued offline survives a reload.** The load-time cleanup dropped any queued answer to a question the server already held, which silently lost a pupil's changed answer. It now keeps entries queued as revisions on a completed set and sends them with `revise: true`. If the backend refuses one (409), the page puts the server's answer back and goes read-only, as for any refused revision. Proven live in `tools/sharpen_pupil_live.py` (score 3 → 4, same row).
- **For the audit, not fought here.** On the teacher's student screen at 1440, "revised after marking" wraps to three lines in the 100px SCORE column. Lane T's column widths (C1) settle it.

## Teacher pages

Source: Fable's C6 audit of `6034aad4c` (65 items, T1–T65; shots in
`~/tmp/ks3-gates/sweep2-teacher/`). Applied on `feat/sharpen-bc` in the commit
"Stage C teacher, C6 cuts". After shots: `~/tmp/ks3-gates/sharpen-C/`
(1440/390, light/dark). Commander's rulings: all 18 musts; the 390 scroll
deviation is overruled (tables drop columns below 720px); the named shoulds.

| id | sev | status | what was done / why skipped |
|---|---|---|---|
| T1 | must | done | "‹ Back to 8X1" (nodes 331/371, `data-mrb-back`) hidden above 560px, where the bar's crumb shows; kept on a phone, where the bar has no crumb. |
| T2 | should | skipped | the bar's name/env-pill order lives in `teacher-topbar.js` and `flashcard-decks.js` shared by every teacher page; not a repeat on any one screen, left for a chrome pass. |
| T3 | should | skipped | the lit "Flashcard decks" tab on decks.html is the same "you are here" state the Today/My classes tabs carry; muting it would make it the only tab that is not lit on its own page. |
| T4 | should | done | the warm-up ping uses `MrBadmusConfig.BACKEND_URL + "/api/health"` (`teacher-live.js`); no ping when there is no configured base. |
| T5 | must | done | Today's no-timetable state: the summary line and the button only; the "Your lessons" heading is hidden and the self-explanation sentence is gone. |
| T6 | should | skipped | the Today eyebrow's year: Today is hand-written and outside this lane's files for C; the year is the only place Today states it. |
| T7 | should | skipped | "N shown" beside the KS filter — Design's control; a count that changes with the filter, not a repeat once a filter is used. Left for Design. |
| T8 | should | skipped | the sort labels wrapping at 390 are Design's control; not a table (C1) issue. Left for Design. |
| T9 | should | skipped | the top "Set work" button sets to any class; the card link is scoped to one. Different actions; not cut. |
| T10 | should | skipped | "VIEWING 2026–27" is the year switcher's own state line; changing it touches MRB-261's year model. |
| T11 | should | skipped | the idle card's dashed box holds the Set work link, the only action on it; kept. |
| T12 | must | done | a week with no papers lists the term's latest five (`wTable`), and the eyebrow reads "LAST 5 OF 18 THIS TERM"; no header over nothing. |
| T13 | must | done | "nothing set this week" said once: the homework card's title. The card draws no "—" and no empty bar (`WRAP` 227/228 on `g.hasBar`); THIS WEEK has no dot and no words, and Score is blank, when no work is in the week. |
| T14 | must | done | "NOT SUBMITTED SHOWN FIRST" only when the week has work. |
| T15 | must | done | NEEDS A LOOK is suppressed when it would be on every row of a class of 2+ (`allFlagged`). |
| T16 | should | skipped | the watch list's cap/"+N more" is Design's glance card; reads fine once T15 stops flagging everyone (it uses the same flag). |
| T17 | should | skipped | the reteach card's reserved height comes from the three-card grid's `align-items:stretch`; collapsing one card breaks the row. |
| T18 | should | skipped | the shoutout eyebrow's "newest first" is one mono line; left. |
| T19 | should | skipped | composer label vs placeholder: both are needed for a screen reader (the label) and at rest (the placeholder); the 0/500 counter is Design's. |
| T20 | should | done | your own shoutout reads "2 days ago"; a colleague's "by Ms Ademola · 1 week ago" (`byLine`). |
| T21 | should | skipped | a "More" menu for the class header actions is a new control — Design's call. |
| T22 | must | done | the week bar wraps below 720px with the caption on its own line, so the chevrons and the chip strip get the row (`data-mrb-weekbar`). |
| T23 | should | skipped | two in-week sets stack two score lines on purpose (B5: one line per set, never a sum that hides which set). |
| T24 | should | skipped | "NO LESSON TODAY" is the timetable's fact on the class header; stays while the timetable feature exists. |
| T25 | must | done | the marking eyebrow drops the class code: "CLOSED · SET … · DUE …". |
| T26 | must | done | the LOWEST tile is gone from the marking screen (the reteach banner and the question row keep the fact). |
| T27 | should | done | (with T26 — the tile is gone, so it is never "—"). |
| T28 | should | skipped | the on-time sub-line is `MRB_ONTIME_SUB`, shared with the class and digest screens; one wording change there moves three pages. |
| T29 | must | done | below 720px a question row is `Qn · bar · %` with the stem full-width under it (`data-mrb-qrow`); the percentage always shows. |
| T30 | should | not reproduced | the fixture's "Still open" under CLOSED is the fixture's own `closed:false` paper; live 8X1 renders correctly (the audit's own note). |
| T31 | must | done | Submission history STATUS is one line: chip · Add feedback · Breakdown in a fixed 400px track (row height back to one line). On a phone the chip and links sit on one line under title · score. |
| T32 | must | done | the student summary band is pruned (`REDUNDANT` 343). |
| T33 | should | skipped | the LAST ACTIVE sub-line is the tile's own data from the seam; changing what it names is a data change, not a cut. |
| T34 | should | skipped | ON TIME's "N not submitted" is `stTimeSub`'s ruled wording (Mide's 23 Sep ruling). |
| T35 | should | done | history SCORE in one form: "9/10" (the pupil results precedent kept the fraction). Lane P's "revised after marking" sits beside it on the same line at ≥720px (SCORE track 210px), and under it on a phone. |
| T36 | must | done | SUBMITTED is a date or "—"; "In progress" is only the status chip's word. |
| T37 | should | done | "1 assignment" singular. |
| T38 | should | skipped | the empty-pupil tile sub-lines are ruled strings shared with a populated pupil; no "—" sub-line remains after T35. |
| T39 | should | skipped | "Send a reminder" / "Send shoutout" — Design's two buttons; a wording change, not a cut. |
| T40 | should | done | breakdown SCORE tile "9 / 10" only. |
| T41 | should | done | HANDED IN sub-line "21 May, 05:19". |
| T42 | should | done | a sitting with a score but no per-question rows says "No question-by-question marks for this sitting." — never "hasn't started". |
| T43 | should | done | no question map and no "All 0 / Wrong 0" toggle when there are no questions. |
| T44 | should | done | flashcards DONE tile "2/6" only. |
| T45 | should | skipped | the RUSHED cell word keeps the column readable when the header is scrolled off on a phone table. |
| T46 | should | done | flashcards.html: the bar carries "‹ 8r/Sc1" as on the generated pages; the eyebrow is gone. |
| T47 | should | skipped | the panel's HANDED IN tile carries the hand-in date once there is one; kept so the tile row does not change shape between pupils (Design's redesign of both panels is pending). |
| T48 | should | skipped | the filter counts are the filter's own result sizes (Wrong-only precedent on the MCQ panel). |
| T49 | — | kept | (audit: no cut). |
| T50 | must | done | below 720px every teacher table drops columns instead of scrolling: Students name · THIS WEEK · AVERAGE; Assignments title · STATUS · SUBMITTED; history title · SCORE (status line under); digest class · SUBMITTED · NEEDS A LOOK. No sideways scroll; nothing ellipsised; only the first column wraps (the digest's last column may wrap). The initials disc beside a pupil's name is hidden on a phone. |
| T51 | must | done | superseded by T50 (no scrolling table at 390). |
| T52 | should | done | superseded by T50 (the digest header reads in full at 390). |
| T53 | must | done | the digest subtitle drops the submissions count. |
| T54 | should | skipped | the digest ON TIME tile is `MRB_ONTIME_SUB`, shared (see T28). |
| T55 | should | skipped | the digest h1 size is Design's type scale. |
| T56 | must | done | Charts card title drops the class ("Submissions by assignment"); the corner tag is pruned (`REDUNDANT` 537). |
| T57 | should | skipped | the ASSIGNMENTS tile and the subtitle count: the tile sits in a chart-specific tile row that changes per chart kind. |
| T58 | should | skipped | the per-row CLOSED eyebrow in Charts is the row's own state; flagging only OPEN is a Design decision. |
| T59 | must | done | below 720px a chart row stacks: label full width, bar and count under it. |
| T60 | — | kept | (audit: fine). |
| T61 | should | skipped | the decks Search box is the deck library's only filter and appears once decks exist on the shared tab. |
| T62 | should | done | admin's refusal is one sentence: "This page is for school admins." |
| T63 | should | done | timetable: "Pick a class for each period you teach." |
| T64 | should | done | timetable upload: "A CSV with day, period and class columns (or your MIS export)." |
| T65 | should | done | timetable "Back to Today" button removed (the bar's Today tab). |
