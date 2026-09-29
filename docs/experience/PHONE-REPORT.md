# The phone run — 28–29 Sep 2026

Mide used the site as a pupil on his phone on 28 Sep and called it
"overwhelming", "too jampacked and tacky", and the flashcards "a job not fully
thought through". This run fixed what he hit, in three stages, each pushed and
proved live before the next. Plans and audits by Fable 5.1; builds by Opus 5.5.

The standing rule it wrote into CLAUDE.md: **no redundant text on any page.**

| Stage | What | Commit | Proved live |
|---|---|---|---|
| A | Flashcard pupil flow | `5beb5760b` | md5 of `student-live.js`, `flashcard-homework.js`, `flashcard-keyboard.js` = committed build |
| B | One pupil top bar; quieter screens; a bench that is never empty | `6344e304b` | md5 of 6 shared assets + class, assignment, leaderboard, a KS3 lesson |
| C | Teacher bits: flashcard rows, "M ·", Delete on automatic work, one-row teacher bar | site `4b1f8cd17`, backend `ac03385` | md5 of 5 assets + 4 teacher pages; Render `/api/health` build `ac03385…` |
| B+ | Re-audit follow-ups | `deff8661e` | md5 of class.html, `student-live.js`, `student-runtime.js` |

---

## Stage A — the flashcard pupil flow

Full plan, review and as-built: `docs/mrb351/PUPIL-FLOW.md`.

| Mide hit | Now | Proof |
|---|---|---|
| "0 of 10 secured" never moved | Headline "N of M right" moves on every card; "secured" is a quieter second fact | TEST live run: 0 → 5 of 5 right; end screen "5 of 5 right this time / 4 of 5 secured so far" |
| End screen "00 / 10 SECURED · FOR NOW · Go again" | "7 of 10 right this time / 4 of 10 secured so far" + ONE button: "Revise flashcards one more time" or "Done". Secured line blank until the server answers; "SAVED ON THIS PHONE" if offline | drive + live |
| No way back | "‹ Back" re-answers the previous card; the rating is replaced for this pass; the event log keeps both | engine test + drive |
| Keyboard covered the answer box | `shared/flashcard-keyboard.js`: overlay pinned to `visualViewport`, card shrinks while typing, box scrolled into view; Android gets `interactive-widget=resizes-content` | drive at 390×844 / 360×740 `mobile:true` with a 508 / 404 px visual viewport: question and box both inside it, Check visible |
| "Get every card right once more, later on" | "Revise flashcards one more time", and nothing beside it | drive asserts retired strings absent |
| Nobody typed in review | Every card, both modes: type → Check → model answer + verdict chip (Right / Nearly / Wrong / No answer) with the suggested rating filled → tap to go on. "I don't know" reveals and pre-fills Not yet | engine test 66/0; drive 121/0 |

Two sittings on TEST, real database, real page: sitting 1, then the sitting
shifted back 61 minutes by service role, sitting 2 → all 5 secured, submission
written (score 5), teacher's `flashcard_progress` = done, 2 sittings. Run once
on production's function bodies and once with the parked migration applied.
Screenshots: `~/tmp/ks3-gates/pupil-flow/{drive,prod-state,migrated}/`.

**For the chat to apply (nothing here is on production yet):**

| Item | Where | md5 |
|---|---|---|
| Migration | `feat/mrb351-pupil-flow-migrations` @ `33b582c5b`, `supabase/migrations/20260929120000_mrb351_pupil_flow.sql` | `d34e18dd002c0ba1cf677ce8185bf9fc` |
| Rollback | same branch, `supabase/rollbacks/20260929120000_mrb351_pupil_flow_rollback.sql` | `03cc3282d4bee9c95c00c99e80cbcc17` |
| Edge function | `supabase/functions/flashcard-answer-check/index.ts` on main (sync per-card mode added; batch mode unchanged) | `94f7c9d5b4d1cefdcaf8f2bfef0079a6` |

Until the migration is applied, production counts a Got it that the pupil later
changed (via Back) as known — slightly generous, never blocking. Until the edge
function is deployed, pupils see no verdict chip and rate themselves; the old
deployed function answers the new call with its existing claimed batch (no
double charge, no wait). TEST currently has the migration applied, so TEST's
two flashcard functions differ from production until the chat applies or rolls
back.

## Stage B — pupil pages on a phone

Every cut, page by page, with before/after pairs: `docs/experience/sweep/CUTS.md`
(24 JPEG pairs in the same folder).

- **One top bar** (`topbar.py` + `shared/topbar.css` + `shared/topbar.js`):
  brand · title (the parent page, as a "‹" link) · bell · avatar · theme. One
  row, 56–58 px at 360 and 390, light and dark, signed in and out, no sideways
  scroll. On KS3 lessons (was 198.6 px, four rows), KS3 unit/landing, the KS4
  pilot (was 184.3 px), the leaderboard, the assignment page (was 124 px),
  student/classes, settings, claim-confirm. The class page keeps Design's
  header; the flashcards overlay is titled "Flashcards". Signed-out visitors
  get brand · title · Sign in · theme.
- **Assignment back button** went to /ks3/index.html → now the pupil's class.
- **Question screen**: "ANSWERED 01 / 10 · 01 RIGHT · 09 LEFT" gone; the clock
  moves into the progress strip on a phone; the bare "›" that skipped without
  saving is hidden while an answer is picked but unconfirmed.
- **Results**: "MARKED · WEEK", the %, "03 OF 10", the RIGHT stat, the header
  clock and "Back to class" gone; "Look at question 02" → "Look at it".
- **Bench**: checklist, eyebrow, blurb, Practice button, DRAWS ON / SET /
  QUESTIONS rows, "7 days left" and the OPEN flag gone. Kept: title, the one due
  date, "Open the assignment", "0 OF 15 ANSWERED". The done bench: one score
  ("4 / 15"), the completed date, one button.
- **The bench is never empty**: a missed set ("Finish it") → practice on the
  current topic ("Practise", with the round's real size) → this week's lesson
  ("Read it"). One heading, one line, one button.
- Class page: crumb strip cut (**⚑ for your veto**), "· your class", "Your
  teacher" chip, "TAP A WEEK TO FILTER", "SET IN THIS WEEK'S ASSIGNMENT" ×4,
  empty Shoutouts card, empty-leaderboard chips; "DUE" → "OPEN" in the work
  list to match the spine legend. Practice overlay: its doubled strip, round
  line, counter and bar cut; the page no longer scrolls under an overlay.

**The Fable pupil audit** (390 px, TEST, a Year 8 pupil's walk: sign in,
classes, class with and without open work, open a set, answer, results,
flashcards, KS3 and KS4 lessons signed in and out, leaderboard, bell, avatar
menu, settings): round 1 → *pushable after 2 must-fixes* (the done bench still
said the result three ways under a "3 / 3" checklist; the practice round said
everything twice) + 9 should-fixes, all taken. Re-audit → **PUSH**: every item
confirmed on screen. Four smaller follow-ups it raised (a gap left on the done
bench, a doubled label, the practice card named after one lesson, "Back to my
class") landed as B+ above. B+ removed Design's empty 64 px "reward slot" on the
done bench, which was most of that gap — **⚑ a Design reservation, for your veto**.

What the audit still flagged and why it was left:
- **Class page "Settings" opens Design's in-page account sheet** (it holds the
  bench theme) while every other page's Settings goes to /student/settings.html.
  One word, two places. Left: moving the bench theme is a product call. For Mide.
- **A KS3 pupil's leaderboard is a page of dashes** (TEST backend 500 on the
  board read for tier=foundation). The page was not in this run's scope.
- **The Practice stat tile always reads "—"**: practice rounds are not saved
  anywhere, so there is no number to show. Kept (it is one of the "four clean
  stats"); needs a data decision.
- The HOMEWORK flashcards flow was not re-walked in the Stage B audit (no
  flashcard homework on the TEST pupil that day); it was proved in Stage A.

## Stage C — teacher bits

| Item | Now | Proof |
|---|---|---|
| "Flashcards · 10 cards" in the Weakest question column | Deck size as a quiet line under the title; Submitted = done/N; Class mean "—" with a "Not graded" tooltip; weakest cell empty | TEST proof 27/27; `after-class-assignments-{1440,390}.png` |
| "M ·" before ratings | Ratings grouped under "while writing" / "in review", only when a card has both phases or the set is make mode; tooltip "Not yet · while writing · time" | flashcard_progress_drive |
| No Delete on automatic work | Delete (same two-tap confirm, same toast, soft delete) on automatic rows; Edit and Download stay teacher-set only. A deleted automatic week is never recomposed: the next pupil read answers `auto_assignment_deleted` | backend `test_set_work_v2.js` 461/0 (auto delete soft, idempotent, not recomposed); set_work drive D4; TEST proof |
| Today's bar wrapped into two rows | One 62 px row at ≤560 px: brand · Today/My classes · Menu (name, env badge, Admin, Flashcard decks, Find a student, Charts, theme, Sign out). Applied to Today, admin, timetable, decks, flashcards and all six generated teacher screens (class-detail was three rows) | today_drive 5b at 360 and 390; teacher_reach; screenshots `~/tmp/ks3-gates/phone-teacher/` |

Backend `ac03385` pushed first (safe: the live site never offered Delete on
automatic rows), Render confirmed on that build, then the site.

## Gates

Every push went through `prepush_gate.py --check`.
- A: "28 gate(s) ran fresh … ✅ every registered gate is green".
- B: green except `figures_mirror` (the shared backend checkout is 33 commits
  behind and has no figures.json) → `GATE-OVERRIDE: figures_mirror` on the tip.
- C and B+: "✅ every registered gate is green", `figures_mirror` green against a
  backend worktree equal to backend main (`MRB_BACKEND_DIR`, no override);
  `GATE-OVERRIDE: set_work` for its three inherited TEST-bank preconditions
  (454/457; this run's auto-delete checks inside it are green).
- Skipped for want of a credential (by design, never set here):
  student_controls_drive, student_bell_drive, teacher_perf_budget and others.

## For Mide to check by hand

1. On a real iPhone (Safari) and an Android phone (Chrome): open a flashcard
   homework, tap the answer box — the question and the box must both stay
   above the keyboard. The drive fakes the keyboard; only a phone can raise one.
2. The class-page crumb strip cut — keep it cut or veto.
3. "secured" — a 12-year-old may read it as a bank word; "locked in" is the
   alternative if you want one.
4. Class-page Settings → in-page sheet vs /student/settings.html.

## Decisions I made

1. Freed ~3 GB (VS Code / Claude Desktop / GitHub Desktop updater caches + Homebrew downloads) — disk was 4.3 GB free, too little for builds + headless Chrome.
2. Staff brand = the one mark (CLAUDE.md's newer one-mark ruling, 13 Sep / 27 Sep), not the older plain-text staff rule.
3. Stage A headline = "N of M right" (Mide's "out of N"); plan said "N right".
4. Adopted all 13 of the Fable reviewer's required changes to the Stage A plan; refined A8: when a new pass can't secure anything (<60 min), button is "Done" but the "Revise flashcards one more time" line still shows.
5. Kept "8r/Sc1" in the flashcards header in Stage A (reviewer suggested blanking); Stage B then retitles the overlay "Flashcards".
6. Built Stage C and Stage B part 1 in parallel worktrees while Stage A was being built; landing order stays A → B → C, each pushed and proved live before the next is pushed.
7. Stage B: kept the class page's four-stat block (Mide's model of good); Practice tile filled if data is loaded, else flagged, not cut.
8. Stage B: challenge / my-challenges / revision / profile-setup pages keep their public nav this run (swept; fixed only if they wrap).
9. Stage B: class-page crumb strip cut ("8r/Sc1 › OVERVIEW · WK 05/39" repeats the h1 and week) — flagged for Mide's veto.
10. Verified TEST and production flashcard function bodies are identical (md5 of comment/whitespace-stripped prosrc, all 9 functions) so the TEST proof stands for production.
11. Stage A pushed 5beb5760b and proved live by md5 (student-live 43fbbbe9…, flashcard-homework 0817bbdd…, flashcard-keyboard cf9da204…).
12. Checked the DEPLOYED (old) flashcard-answer-check against the new per-card call before pushing: it only queues its existing claimed batch over pending rows and returns 202 with no verdict → page shows no chip + manual rating; no double charge, no 4 s hang. So shipping the site before the edge function is safe.
13. Left the parked pupil-flow migration APPLIED on TEST (builder rehearsed apply → rollback → re-apply). TEST's flashcard_card_state/flashcard_record now differ from production until the chat applies it to prod or rolls TEST back.
14. Accepted builder deviation: "latest rating per card per sitting" made per sitting PER PHASE (else make mode's writing-pass Got it is erased by its own review pass and nothing secures); review answer text stored on flashcard_events.answer.
15. Stage C: Delete extended to automatic rows; Edit and Download stay teacher-set only. A deleted automatic set is never recomposed for that class+week (backend step 1a answers auto_assignment_deleted).
16. Stage C: generated teacher screens (class-detail etc.) were also 3 rows at 390, so the same one-row bar + Menu applies to all six generated screens and the five hand-written ones, not only Today.
17. Stage C: set_work gate lands with GATE-OVERRIDE for 3 inherited TEST-bank data preconditions (small KS3 lesson / 5-9 / 10-14 question scopes) — documented in set_work_drive.py, unrelated to this run.
18. Stage B: bars on the leaderboard, classes, settings, claim-confirm and KS3 landing carry NO title (their h1/eyebrow directly below says it); KS4 pilot title links to the unit's topic page (labelled with the unit name) rather than /ks4.html.
19. Stage B: sweep tooling kept in scratch, not in the repo (MRB-346: drives don't write into the tree); CUTS.md + 23 small JPEG pairs committed under docs/experience/sweep/.
20. Stage B: accepted the builder's gate fixes that measure the control a pupil actually uses (ks4_parity compact theme slot; brand_fingerprint's own 404 guard) — same strictness, not weakened.
21. Ran the Fable pupil audit in parallel with Stage B's gate round, against a copy of the committed build, so it didn't cost wall-clock.
22. Stage B audit round 1 → PUSHABLE AFTER must-fixes. Took both must-fixes (done bench, practice overlay header) and 9 of the should-fixes; left: class-page "Settings" opening Design's in-page account sheet (holds the bench theme) — flagged for Mide; KS3 pupils' leaderboard of dashes (TEST 500, page untouched this run); Practice stat tile "—".
23. Stage B: the bare "›" beside "Confirm answer" hidden while an answer is picked but unconfirmed — the auditor skipped 15 questions by accident with it.
24. Stage B re-audit (Fable) → PUSH; pushed 6344e304b with GATE-OVERRIDE: figures_mirror (message-only amend, tree unchanged); proved live by md5 on 6 shared assets + 4 pages.
25. Took the re-audit's four should-fixes (done-bench gap, doubled label, practice-card title, "Back to my class") as a separate follow-up unit landing AFTER Stage C, rather than delaying Stage B by another ~1h gate round.
26. Stage C: backend pushed FIRST (ac03385; Render /api/health build = ac03385…), safe because the live site never offered Delete on automatic rows; then site 4b1f8cd17, proved live by md5 on 5 assets + 4 teacher pages.
27. figures_mirror reads MRB_BACKEND_DIR (not MRB_BACKEND, as I first set). Pointed at a backend worktree equal to backend origin/main it runs GREEN honestly — Stage C and the follow-up pushed with no figures_mirror override; only Stage B carries one. The shared backend checkout (33 commits behind, missing undici/@resvg) was left untouched.
28. Re-audit follow-up (S1–S4, C1) pushed deff8661e with the same inherited set_work override text as Stage C; proved live by md5 (class.html, student-live.js, student-runtime.js).
29. Follow-up removed Design's empty 64px "reward slot" on the done bench (most of the 120px gap); student_themes now asserts it is absent — flagged for Mide as a Design reservation removed.
30. Practice fallback card is titled from the round it opens: one lesson → that lesson; several → "Mixed practice" / "5 questions from 3 lessons".
