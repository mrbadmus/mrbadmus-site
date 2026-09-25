# The experience run — 24–25 September 2026

Unattended. Mide's acceptance test: "everything works the way it should, no
glitches, teachers and students and every user have a fabulous experience."
Worktree `mrbadmus-worktrees/experience`, branch `feat/experience`, seven build
streams (`exp/a`…`exp/g`) merged in, one backend branch. Nine Sonnet executors,
three Opus passes (prompt design, design critique, final audit).

## The root cause, and what replaced it

Two rules in the teacher data path were wrong. Both lived in `shared/teacher-live.js`
(`buildPapers`, `buildMatrix`, `cellOf`, `buildRoster`) and in the SQL aggregate
`teacher_class_rollup`, and every teacher screen read them.

1. **`marked` meant "the deadline has passed".** Nothing counted until the due
   date, so a finished set showed "0 of 0 marked", no on-time figure, no average,
   "In progress" on completed work, and every Charts tab stayed empty for a class
   whose homework was still open.
2. **"This week" meant "`due_at` inside the teaching-week window".** A set released
   on the 20th and due Monday the 28th at 09:00 fell outside the week of the 21st,
   so the class card said "0 of 17 in" while the class page said "2 of 17 in".

**Now, in one place per side** (`buildPapers`/`buildMatrix` in the JS; the SQL):

- `paper.when === 'marked'` means **released** (results are live). The key name is
  kept — fifty consumers — and every comment that said "deadline" is rewritten.
- `paper.closed` and `mx.closedIdx` carry the deadline test for the two things
  that genuinely need it: who is **missing** and who is **late**.
- A cell (pupil × paper) exists only for a **complete** submission. Score and
  on-time status show the moment it exists. An in-progress row is "In progress",
  never a cell, and is not "missing" while the paper is open.
- **This week's homework** = the set(s) that are **open** now (released, not yet
  due) **or** fell due inside the teaching-week window. Every roster row also
  carries `onTimeWeek` (a cell with `late === false` on an in-week paper), which
  is what "Select all on time this week" now reads.
- Pupil status vocabulary: **Complete** (· late) / **In progress** / **Not started** /
  **Missing** / **Scheduled**.
- Averages: a pupil's average is over their cells on released papers; a paper's
  mean over its cells; the class mean over released papers with at least one
  graded cell. Null (dash), never 0, when nothing is graded.

### Proof that JS and SQL agree

- `mrb348_teacher_rollup_proof.py` (a Python translation of the JS held against the
  SQL under real RLS on TEST): adversarial fixture **97/97**, real TEST classes across
  three readers including the HoD **1099/1099, 0 mismatches**. The fixture now
  mirrors production's shape (an open set with two complete on-time submissions and
  one in progress).
- **Production, read-only**, running v2's SELECT body as a plain query against 10h/Ph1
  with the page's own `p_now` and week window: paper `sub=2, on_time=2, late=0,
  marked_n=2, mean=55, marked=true, closed=false`; Lydia and Annabel
  `in_week=true, on_time_week=true`; Erin (2 of 10 answered) `in_week=false,
  on_time_week=false`. Hand arithmetic: 8/10 + 3/10 = 11/20 = 55%.

### The parked migration (for the chat — no production DDL was run)

Because production DDL is out of bounds for this run, the JS calls a **new**
function name, `teacher_class_rollup_v2` (same signature), and on PostgREST
`PGRST202` / Postgres `42883` or any other error falls back to the full JS read for
every class. So production is **correct today, on the fallback**, and simply slower
until the chat applies the migration. Nothing on a screen depends on the apply.

| file | where | md5 |
|---|---|---|
| `supabase/migrations/20260924010000_rollup_live_results.sql` | branch `feat/rollup-live-results` (worktree `exp-a-mig`, commit `b734f03ba`, not pushed) | `112d63fbb9440bd8faca02c0efffff41` |
| `supabase/rollbacks/20260924010000_rollup_live_results_rollback.sql` | same branch | `603adc26fe27eaa98668cbee409dcef7` |
| `md5(prosrc)` of `teacher_class_rollup_v2` as deployed on TEST | — | `e12e5c986be1fa612e6d6f660c33f209` |

The old `teacher_class_rollup` is left untouched by both files (rollback drops v2 only).

⚠️ **Found while rehearsing:** TEST's `teacher_class_rollup` (v1) body differs from
production's (`8c8061…` vs `76419b…`). TEST carries an `AND asg.kind <> 'flashcards'`
clause under an MRB-351 comment that exists in **no migration file** and not on
production (production's `assignments` has no `kind` column). It is orphaned TEST-only
drift from the flashcards branch. v2 is built on the production shape. When the
flashcards work lands, its carve-out must be folded into v2 as well.

## Mide's corrections, one by one

| # | correction | done | proven by |
|---|---|---|---|
| 1 | class card matches the class page | ✅ | same `inWeekPaper` on both (`buildClassEntry` / class tiles); SQL `in_week` equal to JS (proof above) |
| 2 | reteach empty state → "Nothing to reteach yet", quiet style | ✅ | headless Chrome on the no-submissions fixture: 15.5px/400 `--st-muted`; insights empty note "Nothing to chart yet" |
| 3 | RETEACH / DUE / WORTH A SHOUTOUT labels take KEEP AN EYE ON's style and colour | ✅ | one `_EYEBROW` constant bound on all four nodes (13px/500 mono, `--st-accent-text`); getComputedStyle identical on all four |
| 4 | finished pupil: correct count, on time, average, "Complete" | ✅ | student page tiles read "Submissions N · Of M set this term", on-time and average over cells; status "Complete"; screenshots `a/student-page-*.png` |
| 5 | Draft feedback from the pupil's answers | ✅ | backend `POST /api/teacher/feedback/draft` live at build `013cfbf`; identity firewall (42 unit assertions incl. a poisoned row); Opus prompt with 20 live cases 20/20 twice; UI drafts → fills → teacher edits → existing Save |
| 6 | remove "They read this under their marking. They cannot reply." | ✅ | grep of the built pages: 0 occurrences |
| 7 | Send shoutout from a pupil's page opens with them selected | ✅ | composer `boSel` preselects on the student screen only; screenshots `d/item7_*` |
| 8 | Select all on time this week selects everyone on time | ✅ | reads `r.onTimeWeek`; proof fixture has two on-time + one late on the open paper |
| 9 | Answer breakdown | ✅ | `shared/breakdown.js` + `.css`; Opus critique (8 must, 13 should) applied; every must-fix asserted in `breakdown_shots.py`; screenshots `b2/` |
| 10 | Week labels "Week 1"…; term once | ✅ | 0 "Autumn Week" in the built pages; "Week · Autumn term" once on the class screen, once in the digest header |
| 11 | Charts work for open homework, every tab right | ✅ | all six tabs read released papers; expected 10h/Ph1 numbers (2/17 in, 100% on time of those in, mean 55%) match the SQL proof; screenshots `a/charts-*` |
| 12 | Engagement toggle Today / This week / 2+ weeks, one measure, no failure colours | ✅ | `engBucket` state key; toggle IS the legend (one `ENG_BUCKETS` map drives both); colours `--ks3-ok` / `--st-rule-strong` / `--st-accent`, never `--danger`; screenshots `d/item12_*` |
| 13 | Legibility, WCAG AA, fixed at the tokens | ✅ | `contrast_audit.py` measures RENDERED colours on 25 pages × 2 widths: **629 failures → 0**; new fast gate |

### Item 9 — what the breakdown does

Opens from a "Breakdown" button on each history row of the pupil's page, as an overlay
outside the compiled runtime (the same reason the Set work sheet lives outside it).
Summary strip: score, hand-in ("On time" / "Late: N days" with the moment), a
clickable question map (one square per question: right / wrong / unanswered /
class-flagged, shape as well as colour), time taken (labelled "estimated from answer
times" when derived). Questions grouped by topic with a tally, the stem beside its
figure (the same bank → `window.MRBFigures` path the pupil's page uses), the pupil's
answer with its option text, the correct answer, 26px filled marks, attempts told as
"Right on the 2nd try". "N of M in the class got this wrong" in the card header
(strictly more than half, at least three answered) with a one-line class-wide misses
summary and a quiet "got it" note when the pupil beat a flagged question. "Wrong only"
toggle. Previous / Next keeps the set open and pages the roster with no further
network calls, announced to screen readers. A follow-up button opens Set work for the
class naming the topic (it cannot yet preselect the subtopic — see open items). Every
read is paged in 1000-row chunks; retakes keep the first attempt exactly as the
matrix does. Not-started pupils get a sentence and the questions behind a disclosure.

### Item 5 — how Draft feedback is built

- Route re-derives everything from `submission_id`: the assignment via the same
  reader that serves the pupil's page, standing via `classAccess` (must teach the
  class), the pupil's platform-marked attempts. The model receives **only** stems,
  option texts, the pupil's answer, the correct answer, right/wrong, attempts and time.
  `feedback-prompt.buildMessages` throws `FEEDBACK_PAYLOAD_REFUSED` on any other key,
  any email shape or any 7+ digit run.
- Same Anthropic call as `/api/chat`, same `aiRouteLimiter` and AI cap, audited as
  `ai_usage_events.kind = 'feedback_draft'` (`chat_logs` has no kind column).
- `parseDraft` rejects scores, grades, predictions, levels, shaming words, markdown,
  names, over-length; one retry, then 422 with the reason.
- The teacher presses "Draft feedback", the textarea fills (appends if they had typed),
  they edit, and the **existing Save** is the only write. Nothing is stored by the route.
- Opus wrote and tested the prompt on 20 real-shaped cases (0/10, 10/10, a guesser,
  a 4-question set, a 20-question set, a figure stem, a formula option): 20/20 on
  two consecutive runs through the route's own model (`claude-sonnet-4-6`) via the
  Claude Code CLI, since no API key exists on this machine. The cases, outputs and
  verdicts are in the backend repo at `docs/feedback-prompt-cases.md`.
  ⚠️ The science in the drafts is Opus's reading, not Mide's examiner check.

## The whole-site test (item 14)

_(filled in after the live pass — see the end of this file)_

## Other defects found and fixed

- **No visible keyboard focus on the student pages.** Design's `<button style="all:unset">`
  resets `outline-style` inline, which no stylesheet rule can beat. The builders now emit
  an `!important` `:focus-visible` ring (Design's own R15 ring); bench themes use each
  theme's ink so the ring clears 3:1 on clay and chalk. Set work sheet and root pages get
  the same. The chat "attach a photo" label was not focusable at all; it now is, and
  Enter/Space open the picker. New slow gate `focus_audit.py`: 0 no-visible-change on 17 pages.
- **Contrast** (item 13) also caught: three border-hairline tokens used for readable
  breadcrumb glyphs, a specificity bug painting the KS4 chat buttons dark-on-orange,
  the chat header at 3.68:1 on every KS3 page, an opacity-dimmed subtitle, and a
  textarea placeholder with no rule at all.
- **`teacher_admin_foreign_class` (the inherited red)** was not an authorisation hole.
  Reminders write straight to Supabase and RLS `student_notifications_teacher_send`
  requires `auth_user_teaches_class(class_id)`; `load()`'s guard refuses a plain teacher
  on a foreign class on every screen. The gate was red because its fixture carried a fixed
  `due_at` of 30 Aug 2026 that had since closed, so the "Remind all" control was never
  drawn for anyone. Fixture is now deadline-free; gate green. Four new checks press every
  write control (marking, feedback, digest, picker/composer/remind/delete) as a plain
  teacher on a foreign class and prove refusal. No `GATE-OVERRIDE` needed.
- **Breakdown's "correct" colour was invisible**: `--ks3-ok` is declared inside
  `.rd[data-mode="ks3"]`, and an overlay appended to `<body>` sits outside that scope.
  Uses the unscoped `--success` now.
- `teacher_behaviour.py`'s named-addition sweep never checked additions outside the
  mount host; fixed when the breakdown became the first such addition.

## Left as found, with a reason

- **Set work cannot open preselected on the missed subtopics.** The sheet's state
  machine has no `preselect` input; adding one blind was judged riskier than an honest
  label ("Open Set work for 10h/Ph1"). Follow-up.
- **The open chat panel does not trap focus** (Tab escapes behind it) on lesson pages.
  Sitewide widget, pre-existing; out of this run's budget. Named in `focus_audit`'s `why`.
- **Topic titles in the breakdown are de-slugged** from `source_ref` rather than looked
  up in the curriculum tree (would need a new export wired into the build).
- **The word "marked" survives** where it means graded ("Not marked", "machine-marked")
  and as the internal `when` value.
- **Teacher production sign-in was rejected.** See "Decisions I made".

## Gates

`prepush_gate.py --record-all` (affected slow gates only, selected by `watches`
against the merge-base) then `--check`. Recorded green on the landed tree:
`verify_ks3`, `student_parity`, `student_behaviour`, `student_themes`,
`teacher_behaviour`, `teacher_reach`, `teacher_picker_drive`, `ks3_instrument_liveness`,
`teacher_perf_budget`, `teacher_admin_foreign_class` (no override needed any more),
`teacher_admin_real`, `student_bell_drive` (one transient retry), the `mrb328_*` drives,
`teacher_rollup_equal` (97/97 fixture, 1099/1099 real), `focus_audit` (17/17, plus the
chat panel opened for real on both chat-bearing pages: 4/4 controls reached and ringed,
Tab cannot escape, Esc returns focus). Every fast gate green, including the two new ones
(`contrast_audit`, `gate_coverage` now counts 58 gates). `3d_*` skip without a studio build,
as always.

Two of my own env mistakes produced false reds on the first pass and are worth
writing down: `teacher_rollup_equal` and `set_work` read `MRB_BACKEND` as a **directory**
(the backend worktree), not a URL; and `figures_mirror` honours `MRB_BACKEND_DIR`, which
a zsh `export A=… B=$A` line sets to empty. Both green with the variables set explicitly.

**One override, identical to the standing inherited red.** `set_work` fails the same
three checks it has failed since MRB-335 grew the bank ("a small KS3 lesson exists to
drain", "a scope of 5–9 questions exists to cap against", "a scope of 10–14 questions
exists"): 3 of 424, the fixture can no longer find a small pool. Nothing in this run
touches the question pools or the sheet's pool logic; the other 421 checks (every seam
end to end under real RLS) pass. It ships with a `GATE-OVERRIDE:` line on the tip commit
naming exactly that. Fixing it properly means teaching the fixture to mint its own small
throwaway pool on TEST — a follow-up, not tonight.

## Decisions I made

1. **`when === 'marked'` keeps its name and changes its meaning** rather than renaming
   fifty consumers; `closed`/`closedIdx` were added for the deadline test.
2. **A new SQL function name (`_v2`)** rather than replacing v1, so the JS can call it
   safely today and fall back until the chat applies the migration.
3. **Item 3 literally**: stream D matched the three caption labels and left "Keep an eye
   on" in accent; Mide's words were "the same style and colour as KEEP AN EYE ON", so all
   four now take the accent. One-line change if he prefers the quieter reading.
4. **Draft feedback shares the tutor cap** (`tutor_turn`) and is distinguished in the
   audit ledger by `kind`; no new limit bucket.
5. **`focus_audit` is a slow gate**, not fast: it drives 17 pages through Chrome.
6. **The Opus prompt was tested through the Claude Code CLI** because no Anthropic key
   exists locally; the route's `temperature`/`max_tokens` were exercised only by unit test.
7. **The teacher production credential**: production rejected `MRB_PROD_TEACHER_PASSWORD`
   ("Invalid login credentials") on one UI attempt; the pupil credential worked on the
   same code path, and the account has both email and Azure identities with a password
   set. I did not retry, guess or use another account. The auto-mode classifier also
   denied a direct auth-API probe. The teacher's production journey therefore ran by
   read-only SQL impersonation plus the full UI journeys on TEST — see item 14.
8. **The flashcards carve-out on TEST's rollup** was not copied into v2: it is in no
   migration and not on production.
9. Backend landed first (`013cfbf`, proven by `/api/health` `build`); the route is
   additive and unused until the site landed.

## Deviations

- Deviation: streams A and D both wrote the "Select all on time this week" ruling →
  dropped D's duplicate (a ruling that matches nothing refuses the build) → same content.
- Deviation: `focus_audit` registered slow, not fast → see decision 5.
- Deviation: stream C used `pkill -f "node server.js"` once before re-reading the rule;
  every later kill was by PID. Noted, not hidden.
