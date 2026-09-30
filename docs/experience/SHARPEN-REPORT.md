# The sharpen run — 29–30 Sep 2026

Mide used the flashcard flow as a pupil and a teacher on 29 Sep: "I really love
this system… we just need to sharpen it up a little bit", then found the teacher
pages "all over the show". Mid-run he added four more items (Stage D). Plans,
reviews and audits by Fable 5.1; builds by Opus 5.5. Each stage pushed and
proved live by md5 before the next.

| Stage | What | Site commit | Proved live |
|---|---|---|---|
| A | Flashcard sitting sharpened | `4c7ad9ec8` | md5 of flashcard-homework.js, flashcard-keyboard.js, student-live.js, student-data.js, student/class.html |
| B | What the teacher sees about flashcards | `91357a7fe` | md5 of flashcard-breakdown.js, flashcard-progress.js, teacher-data.js, teacher-live.js + 4 teacher pages |
| C | Teacher and pupil pages: tight | backend `496f8f2`, site `0e369081e` | Render /api/health build `496f8f2…`; md5 of 8 pupil/teacher files |
| D | Mide's four follow-ups (progress saved, no jumps, library) | `d9e040c95` and parents | md5 of the flashcard engine, keyboard, library, student-live.js, student/class.html |

## Stage A — the flashcard sitting (plan: PUPIL-FLOW.md §13)

| Ruling | Now | Proof |
|---|---|---|
| A1 verdict caps the rating | Wrong → only Not yet; Nearly → Nearly/Not yet; Right → all; blank → Not yet. Greyed buttons stay visible. Enforced once in `Engine.rate()`, so keys and swipe obey it. No verdict (timeout/no key) → no cap | engine test; TEST shots 01–05 |
| A2 "I don't know" teaches | Question stays; ANSWER block below; box "Now write it in your own words"; no ratings until typed; capped at Nearly; card replays at the end of the pass, question first | TEST shots 04–06; Fable phone review (keyboard up at 390/360) |
| A3 honest end | All right → "N of N right" + secured line + Done; else "N of M right" + Try again (+ ×) | shots 07, 10 |
| A4 Try again = leftovers | Green numbered strip (tap to redo), then only the not-yet cards | shots 08–09 |
| A5 deleted set | Fresh reads already hid it (RLS); a page loaded before the delete now shows "Your teacher has taken this work down" | shots 11–12 |

Fable sent it back once (an IDK card reopened uncapped via ‹ Back; a mid-pass
"Revise…one more time" line) — both fixed, plus dark-mode chips, fresh pass
after ×, IDK state kept on the device.

## Stage B — teacher flashcard views (plan: docs/experience/SHARPEN-PLAN.md)

- B1 the three chips under the title are gone (and the Open/Scheduled chip).
- B2 **Fable decided: drop the ANSWERS column**; the per-pupil panel carries one line "4 right · 3 nearly · 1 wrong · 2 blank" (zero buckets omitted). Why: a diagnostic, not an at-a-glance number, and the column fought for width at 390.
- B3 per-pupil sheet = the centred wide breakdown panel with ‹ › pupils; per card: question + one state chip, latest answer + verdict, model answer, "Tries: N"; phases and ratings under "History", closed.
- B4 flashcard rows: Not started → In progress → Complete; "6/10 secured"; Breakdown opens the B3 panel; Add feedback once a submission exists.
- B5 new Score column before AVERAGE ("7/10", "6/10 secured", "—").
- B6 class cards count the set currently open (newest if two); "opens Thu 09:00" when only a scheduled set exists.

Fable sent it back once (review-mode cards would have said "No written answer" on production) — fixed.

## Stage C — tight

- **C1** every teacher table on a fixed column grid, header and cells sharing tracks, title the only wrapping column. Below 720px tables **drop columns** (no sideways scroll, nothing ellipsised); Edit/Download/Delete on their own line under each row on a phone. `teacher_reach` now measures header/cell edges ±1px at 390 and 360.
- **C2** breakdown panel: "Pupil N of M" and the Due line gone.
- **C3** term spine → one week select ("Week 5 · this week"), default this week when it has work, else All weeks; same filter.
- **C4** top bars carry the parent, never the h1.
- **C5** pupils can always reopen homework: "See your answers" / "Finish it" (one button per state); change any answer or finish the rest; the teacher's score updates to the latest; "revised after marking" on the teacher's row and in the breakdown ("Revised 23:54" same day). Backend `revise:true` on /api/assignment/answer revises the same attempt in place; completed_at / is_late / attempt_no never change. Without the flag the old 409 is byte-identical. "Revised" = complete and updated_at > 2 s after completion (3 production rows sat inside 2 s from an in-flight race; 0 beyond it).
- **C6** cuts: `docs/experience/sweep/CUTS-2.md` (pupil + teacher sections, done/skipped with reasons). Fable audits found 31 pupil items (9 must) and 65 teacher items (18 must); all musts done.

Fable re-audit round 1 → SEND BACK (teacher week bar squeezed at 390, marking stems clipped at 390, phone table headers off their cells); round 2 → **PUSH**.


## Stage D — Mide's four follow-ups (plan: docs/mrb351/STAGE-D-PLAN.md; as built: PUPIL-FLOW.md §14–§15)

| Mide said | Now | Proof |
|---|---|---|
| Clicking the answer box moves the question up (desktop and phone); the question takes too much room | The card sizes to its question (min 120–140px). Compact mode only when a real keyboard is up, measured against the tallest unfocused height (so Android's resizes-content works too). On a tall desktop the answer box grows to 200px. Nothing moves on focus on a desktop | drive: rest/focus/type/blur rects identical at 1440, 1280 and 1366×660; phone 390/508 and 360/404 with Check visible |
| Progress must save at every point — ×, closing, a dead phone | Every answer and rating is sent at once; the device keeps a queue; a keepalive send on pagehide/hidden. Reopening rebuilds the pass from the pupil's own saved ratings, so it lands on the next undone card on any device | TEST: × → reopen on card 4 at "2 of 10 right"; SIGKILL then a fresh browser profile → card 5; offline then reload → card 6; Try again survives × |
| Clicking a homework card lifts the page | Root cause: opening the overlay hid both html and body, which reset scrollY to 0 on the live page. Now only html is locked; the dialog's slide-in is removed; the scrollbar gutter is stable | drive + live: scrollY 316→316, no scroll event, at 1440 and 390 |
| A finished set becomes a Quizlet-style deck; "View your flashcards"; pupils can rename | One "View your flashcards" button under the Flashcards card once a set's first pass is done. Sets list (teacher's name or the pupil's own), tap card to flip (model answer + YOUR ANSWER), ‹ ›, Shuffle, rename via the pencil. Revising here never counts toward secured. Deleted sets vanish. Renames stay on the device until the parked `flashcard_set_names` migration is applied, then upload once | drive (390/1440, light/dark); TEST live proof 24 checks; RLS proof as real pupils |

Fable reviewed D1 → GO with a patch (Android keyboard; IDK record by round) and D2 → GO with corrections (the migration's UPDATE rule let a pupil move a name onto a set they couldn't see — closed and proved; pencil for rename).

## Parked for the chat (nothing here is on production)

| Item | Where | md5 |
|---|---|---|
| B3 migration: `flashcard_pupil_detail` returns review answers + shown count | `feat/mrb352-migrations` @ `c8d06436b`, `supabase/migrations/20260930090000_mrb352_flashcard_pupil_detail_answers.sql` | `fadcd122b82d37940857cf5120429b45` |
| its rollback | `supabase/rollbacks/20260930090000_…_rollback.sql` | `488b6a36685f9ed82fbab1cfbbcc9fef` |
| D2 migration: `flashcard_set_names` (pupil's own set name, RLS) | same branch, `supabase/migrations/20261001090000_mrb352_flashcard_set_names.sql` | `b576184631f1375657adf2e9049fbcca` |
| its rollback | `supabase/rollbacks/20261001090000_…_rollback.sql` | `f3a487b980b6af21fd71183e1123b960` |
| Edge function `flashcard-answer-check` (batch path gains the deleted/release check) | main, `supabase/functions/flashcard-answer-check/index.ts` | `6cc6e1f0341c0a87c69a904b099b8acb` |

Both migrations rehearsed on TEST (apply → rollback → apply) and left applied
there. Until applied on production: Tries counts rated passes and review-mode
answers are omitted (never "No written answer"); renames stay on the pupil's
device and upload once when the table appears. Until the edge function is
deployed with a key, A1's cap bites on production only for exact / one-word /
blank answers (multi-word answers get no verdict, so no cap).

## Gates

Every push through `prepush_gate.py --check` → "every registered gate is green".
Overrides, each with its signature line:
- `set_work` — the 3 inherited TEST-bank preconditions (small KS3 lesson / 5–9 / 10–14 scopes), on A, B and C.
- Stage D: `student_parity` hung for 2½ hours relaunching Chrome in the gate round; killed, it passes alone in minutes; all receipts recorded green.
- `student_bell_drive` — `bell_survives_redraw` / `panel_survives_redraw` fail identically on main before this run whenever a local backend is up (the drive likely presses the reminder's Dismiss). On A and B. **Open: the drive needs its own look.**

## For Mide

1. On a real iPhone and Android phone: open a flashcard homework, tap the box — question, box and Check above the keyboard; also the "I don't know" step.
2. A pupil who changes class or moves up a year loses that class's sets from "Your flashcards" (pupils can only read their current classes). If "over time" means across years, that is a policy change — its own ticket.
3. After "I don't know", the chip may say **Right** while Got it is greyed (capped at Nearly) — correct per A2; say if you'd rather the chip said Nearly.
4. The Done screen can read "6 of 6 right / 0 of 6 secured so far" right after a perfect pass (secured needs a second sitting an hour later).
5. "Tries" and review answers in the per-pupil panel wait for the parked B3 migration.
6. When the current set is a flashcard deck, a class card's "N of M in" counts pupils who have secured every card, so it reads low for most of the week.
7. A partly answered set can show "1/2" when the set has 4 questions (the backend's `max_score` = answered count on completion) — pre-existing; worth a ruling now that "Finish it" exists.
8. Live read-only walk of 8r/Sc1 and 10h/Ph1 as the teacher was not possible from here (no production teacher credential) — please look at both classes.
