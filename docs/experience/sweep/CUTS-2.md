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
