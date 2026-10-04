# Prompt X — the class page tells the truth about every week

4 October 2026. Written for Mide and the lane.

## What is live

| | what | where |
|---|---|---|
| Push 1 | Set work "Set automatically · Wk N" · reopened-homework scoring (code) · class page week truth | site `main` `61804e1b1` → `ec5af259a` → `692a23f2f`; backend `128c2e9` (Set work) and `cb8f9a3` (reopen) |
| Push 2 | Pupil class page: leaderboard (top five) and PRACTICE counts rounds | site `main` `a9e4d3dc4`; backend `e4e6964` |

Every changed file was compared byte for byte with what mrbadmus.com serves
after each push: 12 of 12 and 8 of 8 match. One note on push 2:
`/shared/student-live.js` without its `?v=` stamp is a five-day-old copy held at
the Cloudflare edge as `immutable`. No page asks for it; the stamped URL the pages
actually load (`?v=e9fbb89e`) matches.

**Waiting on the lane: two parked SQL changes, not applied to production by me**

| migration | branch | file md5 | rollback md5 | apply sheet |
|---|---|---|---|---|
| `20261004010000_x_reopen_fair_scoring.sql` | `feat/x-mig-reopen` | `a2f85b26a5ed478112f4d13de2a214c2` | `ea08fe5cfced11b274890ef71b358b4d` | `supabase/X-REOPEN-APPLY.md` |
| `20261004120000_x_pupil_class_board_and_practice.sql` | `feat/x-mig-pupil-class` | `b22aa03a4fc19676e42ad22e4061f88f` | `f88dcf3a2c8bd136769259b03a14e575` | `supabase/X-PUPIL-CLASS-APPLY.md` |

- **Reopen scoring.** Restart Render after applying it. The teacher's fair
  score works the moment the SQL lands, but the "Changed after answers shown"
  label and the "Now X / Y" line switch on only after a restart.
- **Leaderboard and practice.** Mide's ruling (top five) is built in and the
  hold is lifted. It redefines `class_stars_leaderboard_for_member`, and it was
  built from production's current body, md5(prosrc) `9271514c…`. It adds
  `class_stars_board_for_member` (md5(prosrc) on TEST `c309e041…`) and the
  `practice_rounds` table. No restart is needed.
- Neither touches `flashcard_card_state` (ec4834b7…) or `flashcard_record`
  (118ade9a…), which the lane applied at 18:2x.
- Until each is applied, the pages behave as they did before this run:
  - the board stays empty;
  - the practice tile shows a dash;
  - the teacher's score keeps today's rule.

  Nothing breaks.

## ⛔ Superseded the same evening — the reteach rule

The "last set that closed by the end of the week" rule in the next three
sections was the lane's, and it was wrong: it carried week 4's Changes of
State onto weeks 5 and 6 and left week 4 saying "Nothing to reteach yet".
Mide's rule (4 Oct, 21:56) replaced it on main: **every week shows only its own
homework.** `weekScope()` now returns only the selected week's own sets and
`reteach` — the first of them with a hand-in — and the "most recent closed
set" search is deleted. See the box at the top of `X-WALK.md` for the
expectations that now hold. The sections below are kept as the record.

## The class page: what was wrong, in three sentences

The reteach card never asked "which set had closed by this week?". On a past week
it showed that week's own set, and on the newest chip it showed the newest set
anyone had touched, even one still open. The page also had two separate sets of
rules for "Keep an eye on", "Worth a shoutout" and the NEEDS A LOOK flag: one for
the newest chip and one for every other chip. Nothing knew whether a week had
started yet, so on a Sunday, when the teaching week has already rolled forward,
the not-yet-started week judged every pupil. Finally, "Open the full breakdown"
always opened the newest set.

**The fix is one function, `weekScope()`.** It lives in `shared/teacher-live.js`
and reaches the page as `MRB_WEEK_SCOPE`. For the chosen week it answers three
questions:

- which sets belong to this week;
- has the week started;
- which set was the last to close by the end of this week.

The end of a week is the following Monday 00:00, or now, if that is sooner.
Every card, the table's flags and cells, and the breakdown link read that one
answer. The newest chip no longer has rules of its own.

## 10h/Ph1, week by week — before and after

The live data has two sets:
- **Changes of State.** Set in week 4, closed Mon 28 Sep at 09:00, 8 of 17
  handed in.
- **Temperature Changes and SHC.** Set in week 5, due Mon 5 Oct at 18:00,
  3 of 17 handed in.

There are also two deleted "Energy" sets, which never appear.

The clock is the moment of Mide's screenshots: Sunday 4 Oct, 01:04. On a Sunday
the bar's newest chip is already week 6.

| week | card | before (live, 4 Oct) | after | why the after is right |
|---|---|---|---|---|
| **4** (21/09) | Homework | Changes of State, closed, 8 of 17, chips headed "Not in yet" | same set, closed, 8 of 17, chips headed **"Missed it"** | it is week 4's own set; it has closed, so nobody is "yet" to hand it in |
| | Reteach | Changes of State (its own set) | **"Nothing to reteach yet"**, no breakdown link | week 4 ended Mon 28 Sep 00:00; Changes of State closed 9 hours later, and nothing earlier exists |
| | Keep an eye on | "Missed it" | "Missed it" for the 9, plus "+5 more" | same words as the chips beside it |
| | Breakdown | opened the newest set | hidden | there is no set to break down |
| **5** (28/09) | Homework | Temperature, 3 of 17, Remind all 14 | unchanged | it is week 5's own set, still open |
| | Reteach | "Nothing to reteach yet" | **Changes of State, 8/17: Q4 50%, Q7 50%** | it closed during week 5. Both bars are that set's own numbers (checked on production: 8 hand-ins, Q4 and Q7 both 50%) |
| | Keep an eye on | 14 × "Not in yet" (the same names as the chips) | only Temperature hand-ins under 50%; otherwise "Nothing to flag yet." | an open set's missing pupils are already named on the homework card |
| | Breakdown | opened the newest set | opens **Changes of State** | the set the card is showing |
| **6** (05/10, not started) | Homework | "No work set in this week" | **"Nothing set yet · starts Mon 5 Oct"** | true, and says when it begins |
| | Reteach | **Temperature: still open**, 3/17, Q2 67% / Q3 67% | **Changes of State**, 8/17 | the last set closed as of now; Temperature does not close until Mon 18:00 |
| | Keep an eye on | "1 missed this term" | "Nothing to flag yet." | nothing in this week has started |
| | Worth a shoutout | "Top average 90%", "Up 20 points on the last set" | nothing | no work, no scores |
| | Students table | every row "No activity yet" + NEEDS A LOOK | no flags, blank week and score cells, last active only where real | a week that has not begun judges nobody |
| | Breakdown | opened Temperature | opens Changes of State | the set the card is showing |
| 1–3 | all | no work; reteach "Nothing to reteach yet" | unchanged; Keep an eye on reads "Nothing to flag." | nothing set or closed |

**What changes on Monday.** From Mon 5 Oct 18:00, when Temperature closes:
- Week 6's reteach becomes Temperature (3/17).
- Week 5's stays Changes of State, because Temperature closed after week 5 ended.
- Week 5's homework card becomes the closed Temperature card, with its chips
  headed "Missed it" and 14 names, and "Keep an eye on" names those 14 too.

All four clocks were walked on TEST in headless Chrome, at data shaped exactly
like this: Sun 01:04, Wed 30 Sep, Mon 5 Oct 12:00 and Tue 6 Oct 12:00. They are
written out in `docs/experience/X-WALK.md`.

## A class with a different history — 8r/Sc1, Sunday 01:04

Its sets:
- an automatic week-1 set;
- three teacher sets released together in week 2 (two due Tue 15 Sep, one due
  Wed 16 Sep);
- a quiz and a flashcard deck due Mon 5 Oct;
- two decks due 9 and 10 Oct;
- one old set from before the start of term.

| week | before | after |
|---|---|---|
| 6 (not started) | reteach = the 5 Oct quiz, **still open** | "Nothing set yet · starts Mon 5 Oct"; reteach = teacher set C (closed 16 Sep), 1/2; nothing flagged |
| 5 | reteach = its own open week, or nothing | homework = the 5 Oct quiz (2 of 2) and deck (0 of 2, both chased), "+2 more"; reteach = set C; nothing flagged yet |
| 3, 4 | no work | no work; reteach = set C |
| 2 | reteach = its own sets | homework = set C (closed, 1 of 2, "Missed it"), "+2 more"; reteach = **the week-1 automatic set**, because all three week-2 sets closed after week 2 ended; pupils "Missed 1 of 3" / "Missed 2 of 3" |
| 1 (oldest) | its own set | the automatic set and the pre-term set share this chip; reteach = the automatic set, 2/2; both pupils "Missed 1 of 2" (the pre-term set) |

Flashcard decks are never a reteach source, because they have no questions to
reteach.

A third class, with exactly one set ever (closed, nobody handed it in), shows
that set as the reteach from the week after it closed: "0/3 submitted", no bars
and no breakdown link. Mide's rule says the last set that closed, even an empty
one.

## Files and functions changed

**Class page (`692a23f2f`)**
- `shared/teacher-live.js`:
  - `buildWeeks()` gives every week `started` and `endMs`;
  - new `weekScope()`;
  - `load()` prefetches the grid of the reteach set it will show.
- `build_teacher_port.py`: `MRB_WEEK_SCOPE`, `MRB_OPENS_LABEL`.
- `teacher_rulings.py`:
  - `wScope` is computed once and read by `lastP`, the homework cards, a single
    week-scoped rule for "Keep an eye on" / "Worth a shoutout" / NEEDS A LOOK,
    the roster cells, `glance.openMarking`, and the new `noWatchLine` and
    `hasBreakdown`;
  - `RETEXT_AT[266]` (the empty-state line) and `RETEXT_AT[231]` (the chip
    heading, "Not in yet" / "Missed it");
  - `WRAP[253]` hides the breakdown link when there is nothing to open.
  - The old chip-0 branch and the MRB-353 branch are deleted.
- New fast gate `week_scope_check` (`.py` + `.js`), registered in
  `gate_registry.py`.
- `week_truth_fixture.py` and `week_truth_drive.py`, the TEST world and the walk.
  Both are listed as excluded: hand-run proofs, not push gates.

**Set work (`61804e1b1`, backend `128c2e9`)**
- `/api/teacher/set-work/scope` also reads automatic sets. It maps each set's
  questions to the topics they cover, which also fixes multi-topic teacher sets
  and old sets with no recorded scope.
- It sends `last_set_source` and `last_set_week`, and the sheet's
  `lastSetTag()` reads "Set automatically · Wk N".
- Backend: `autoSetHistory`, `assignmentQuestionTopics`, `classSetHistory`, and
  `SW.mergeSetHistory` (newest wins; a tie goes to the teacher's set).

**Reopen scoring (`ec5af259a`, backend `cb8f9a3`)**
- `shared/breakdown.js`: column probes, a truthful `isRevised()`, per-question
  "was B", and "Now X / Y".
- `server.js`: `revealColumnsSupported()`, `submissionCols()`, and `isRevised()`
  answered from the stored answer times.

**Pupil page (`a9e4d3dc4`, backend `e4e6964`)**
- `shared/student-data.js`, `shared/student-live.js`, `student_rulings.py`,
  `build_student_port.py`.
- `POST /api/class/practice/round`.

## The leaderboard: why it was always empty, and the fix

There were two causes.

1. **The page threw the data away.** It fetched the board on every load and
   then drew a roster hard-coded to empty.
2. **The database function chose the wrong week.** It picked "this week's" work
   by due date, but work is set one week and due the next, so the current week
   never held anything. It also counted a hand-in as on time only if it came
   after the week started, so early work never counted.

**The fix:**
- A set belongs to the week it was set in.
- On time means handed in by the due time.
- The page draws the server's rows.

**Mide's ruling is enforced inside the database function.** A pupil's browser
never receives more than five names:

- A pupil sees at most five pupils per tab (W01–W04 and TERM), with their
  points, and nothing about anyone else.
- A pupil outside the five sees no rank, no score and no row of their own.
- A tie at fifth keeps it to five: whoever handed in first wins.
- A teacher of the class gets everyone.

This was rehearsed on TEST with a 17-pupil class and a tie at fifth:
- the 17th pupil's call returned five rows, none of them theirs;
- a top-five pupil was marked as "you";
- the teacher's call returned all 17.

## The practice tile: where the count lives

A new table, `practice_rounds`, holds one row per finished round: pupil, class,
teaching week, questions, and how many were right.

- Only the server writes to it, through `POST /api/class/practice/round`. That
  route checks the pupil belongs to the class, works out the week itself, and
  writes with the server's own key.
- Pupils can read their own rows; teachers and admins can read their classes'
  rows.
- The tile reads **N · ROUNDS · WK N**, with a bar showing how many practice
  questions were answered right this week.
- A round left halfway is not counted.

## Reopened homework: the reveal moment, and a worked example

**Where the reveal is recorded:** `assignment_submissions.answers_revealed_at`.
- A database trigger stamps it with the database's own clock the moment a set is
  handed in, because hand-in is when every correct answer is shown.
- After that the stamp never changes. A browser cannot set it or move it.
- Before hand-in, each question already shows its answer as soon as it is
  confirmed, and a confirmed answer is locked.

**How each answer is kept:** every answer row keeps its first answer for good, in
`first_option_letter`, `first_is_correct` and `first_answered_at`. A later change
moves only `answered_at`.

**How the score is worked out:** the database marks every answer against the
question bank. It never takes the browser's word for right or wrong. Then:
- `score`, the figure every teacher screen already reads, counts only first
  answers given before the reveal;
- `latest_score` is "if I marked it today".

I replayed this marking against all 168 real answers on production. Every one
agrees with today's marks, so applying it moves no existing score.

**Worked example (run on TEST through the real routes):**
1. A pupil answers Q1 with **B**, which is wrong. The browser falsely claims it
   is right; the database marks it wrong anyway. Score **0 / 1**.
2. They hand in. The database stamps the reveal.
3. They reopen the set, copy the correct answer **C** and save. The teacher's
   score **stays 0 / 1**. `latest_score` becomes 1.
4. The breakdown shows Q1 "Changed after answers shown · was B", and "Now 1 / 1"
   beside the score.

**A three-question set**, with one right before hand-in, then one fixed and one
blank filled in afterwards: the teacher sees **1 / 3**; latest **3 / 3**.

**The "revised after marking" label is now truthful.** It means some answer was
changed, or newly given, after the reveal. Before the SQL is applied, the old
rule still applies.

**This also closes a hole.** Pupils' own database permissions previously let a
pupil write their own score straight from the browser. Now the score is always
recomputed by the database, and pupils can no longer write answer rows at all.

## Deviations

- **The empty-set rule.** Mide's rule ("the most recent set that had closed")
  replaces the earlier rule that skipped a closed set nobody sat. An empty set
  now shows as "0/N submitted", with no bars and no link.
- **The "Keep an eye on" list.** Pupils who are only not in yet on a set that is
  still open are left to the homework card's chips, which already name them.
  Listing them twice broke the no-redundant-text rule.
- **A closed card's chip heading** now reads "Missed it". The old heading said
  "Not in yet" while "Keep an eye on", beside it, called the same pupils
  "Missed it".
- **`verify_ks3` ran detached twice.** A full run takes longer than one call can
  stay in the foreground. Mide approved it, and nothing else was running at the
  time.
- **One of my builds overlapped another lane's `verify_ks3`.** That happened
  once, before I started checking for other lanes' work before every build.
- **A push hook ran in the background.** The push of `feat/x-mig-pupil-class`
  overran the time limit and moved to the background with its gates running. The
  safety check would not let me stop it, so it was left to finish.
- **`curriculum_tree_mirror`** was carried with an override, inherited from the
  KS4 route-flag merge and held on Mide. `frozen_window_guard` went green on its
  own once that lane fixed it. `teacher_admin_foreign_class` passed rather than
  showing its known inherited red.
- **Proofs not done:**
  - No 10h/Ph1-shaped class-detail fixture was added; the TEST walk and the new
    fast gate stand in for it.
  - `mrb348_teacher_equiv` was not run as a before/after capture.
  - Three of the one-set class's Sunday chips rest on the Node reproduction.

## Left over

- **18 test-only accounts remain on TEST.** TEST's sign-in service fails every
  admin delete ("Database error loading user"), so these accounts survive. Every
  row that pointed at them is deleted. To remove them later:
  ```sql
  delete from auth.users where id in ('21b2d104-9d3c-4e10-8bbd-a07733e81c2d','2b458eef-2ec0-40cc-af5c-1d52df7735c3','1295d99f-8452-4d44-ad1e-5a4ff4d47247','1a620bed-f810-4765-b425-601b7e955b62','b7470d5a-e84d-4e86-966f-b8c24fae2758','b3cea982-1d72-4d69-8a15-bfbeb6420005','b7d8a857-2acf-40ac-af92-f24346f67e10','bfd33c7f-3269-4e98-8060-9d1abde92c20','3c4141b6-6fa6-4d89-a5b1-e04338069aae','83297d9b-d560-42f0-98aa-bc2989b76553','d319c52c-5bc7-4ba7-ab1e-721bb153081c','2ef33d24-7954-47a8-8e72-fc47e1e44d38','2c2ec7eb-f105-45cd-8c5b-b0f02acd42a4','bd4e8cc2-f59b-4f71-b6d5-d44bf2da9742','ba7f69c4-a61c-4541-b9f7-ad833684886e','d87b93fa-dd51-4ebf-9002-533b42b8853f','7c9055bb-0984-4d10-9d5f-589ffe23dab2','5d0edd49-abb3-4e6a-af29-98d124ee8cb8');
  ```
- **Pupils don't see their latest score.** `latest_score` is not shown to them
  anywhere. Their own page already shows their current answers, so nothing
  needed it.
- **The teacher has no leaderboard screen.** None exists today (it was removed
  in MRB-287). The database function is ready to give a teacher the full ranking
  if one is ever wanted.
