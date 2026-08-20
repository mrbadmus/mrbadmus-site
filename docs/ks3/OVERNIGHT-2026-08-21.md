# Overnight run — 21 August 2026

Run log. Every ruling applied, every deviation, every finding, timestamped (UTC+1 / local).
Follows the run ending at `fbbe2f0be`.

---

## Step 0 — Recon

| | |
|---|---|
| Worktree | `~/Documents/GitHub/mrbadmus-site` — **the main worktree**, confirmed (`git rev-parse --show-toplevel`, `--git-dir` = `.git` not a worktree pointer) |
| Branch | `main` |
| HEAD vs origin/main | **zero ahead, zero behind** — identical |
| Working tree | one untracked directory, `ks3-formula-blocks/` (7.8 MB, dated 19 Aug, a Design drop with `PROMPT-FOR-CODE.md` + `source/` + `open-these/`). Not mine, not touched tonight. |
| Disk free | 11 GB at start |
| Production ref | **`urklkrwevjtlfbwnipjn`** — ends in N. Stated before the first write, as required. |
| `MRB_TEST_STUDENT_PASSWORD` | **SET** — so B3 drives as `midebolabadmus@gmail.com` and **no throwaway account is created**. The pre-authorised account-creation fallback is not exercised. |

Parallel session: `content-chem` worktree is at `5306f1e20`, a different branch head. No shared working files.

---
## Workstream A — clear the ground

### A1 · Disk — DONE, 03:0x

11 GB → **15 GB**. Reclaimed: npm cache (922 MB), `ms-playwright` left alone (unused by
these gates — nothing in the repo references playwright; the gates drive Chrome over CDP
directly), pip http cache, three Electron auto-updater staging caches (VS Code, Linear ×2),
`node-gyp`, and `brew cleanup --prune=all` (152 MB). `~/tmp/ks3-gates` was only 5.3 MB and
was left intact — it holds `.bak` files from earlier runs that are cheap to keep.

Target was 10 GB; 15 GB reached. No gate needs to be re-run for a disk death.

### A3 · The `.ks3-commit` token — RULED, NOT APPLIED HERE

Ruling recorded: `.ks3-commit` resolves to **`--ks3-on-dark` (cream)**, not amber.

The rule lives in `shared/ks3.css`, which is **off-limits tonight** under the parallel-session
rule. Per the prompt's own instruction, the ruling is recorded here with the exact change and
left for the `content-chem` session to apply:

```
shared/ks3.css — the .ks3-commit rule: colour: var(--ks3-on-dark);   /* was --ks3-amber */
```

Reason: amber is already carrying four jobs (the MRB-252 finding), and Design's own later lane
chose cream. Single token. One-line reversal if Mide disagrees.

**Deviation: the prompt assumed this might be applicable here → it is not, because the file is
under the other session's ownership → recorded rather than applied, which the prompt explicitly
authorises.**

### A4 · C2-06 — CONFIRMED UNDISTURBED

`docs/ks3/design-reference/c2/redelivery-2026-08-19/` is present and untouched, holding
`c2-06-conservation-of-mass.dc.html`, `README.md` and `NOTE-ks3-commit-divergence.md`. C2-06
stays as built. No action taken.

---

## What the ground actually looks like — recon findings that changed the plan

Six things were measured before any code was written. Three of them move the plan.

### F1 · ⚠️ The working academic year has not started yet

`academic_years` on production:

| name | start | end | `is_current` |
|---|---|---|---|
| 2025-26 | 2025-09-01 | 2026-08-31 | **true** (stale, as CLAUDE.md warns) |
| 2026-27 | 2026-09-01 | 2027-08-31 | false |

`workingAcademicYear()` correctly resolves to **2026-27** — but 2026-27 **starts on 1 September,
eleven days from tonight**. So "the current teaching week, computed from the server clock against
the academic year's dates" is, tonight, *before week 1*.

The prompt rules that the week comes from the server clock against the year's dates and never
from `is_current` or the device. It does not say what happens before the year opens. **Ruled here,
in the spirit of the 30-day lookahead that `workingAcademicYear()` already uses:**

> Before the academic year's `start_date`, the current teaching week is **week 1**.
> After `end_date`, there is no current week and nothing is generated.
> Otherwise `week = floor((today − start_date) / 7) + 1`, capped at 39.

The helper already looks 30 days ahead — that lookahead is the only reason the working year
resolves to 2026-27 at all. A class page opened in the last days of August should show the first
week's work, which is what a student or teacher is actually looking for then. And the ruling
already says **week one may legally be short**, so week 1 is the safest week to be standing in.

### F2 · A KS3 week is three lessons, one per science — and that is exactly `compose_assignment`'s shape

`scheme_of_work_entries` holds 183 active KS3 rows. For Year 8 week 1 there are **three**:

| subject | topic | subtopic (slug) |
|---|---|---|
| Biology | Breathing and gas exchange | `the-gas-exchange-system` |
| Chemistry | Chemical reactions | `chemical-vs-physical-change` |
| Physics | Pressure | `pressure-force-over-area` |

So "this week's lessons" for a KS3 class is *all* active SOW rows at `(key_stage, year_group,
academic_week)` — which is precisely `compose_assignment(current_lessons=[...])`. One assignment
per class per week, spanning the sciences. That settles the "which subject?" question that the
per-subject scheme first appears to raise: **the assignment is filed under `Science`**, matching
`class_teachers.subject_id` for `8r/Sc1` and the demo assignment already on production.

### F3 · ⚠️ The bank covers 70 lessons — Biology and C1–C2 only. No Physics, no C3 upward.

`bank_by_lesson()` returns 70 lessons × 12 questions: **B1–B11, C1, C2**. Nothing else.

For Year 8 week 1 that means one of the week's three lessons (`the-gas-exchange-system`, B4-01)
is banked and two are not. Four `standard` questions reachable, fifteen wanted.

Week one is the one week where that is **legal** — `compose_assignment` is documented and tested
to allow a short week one and to raise `ShortAssignment` everywhere else. So tonight's producer
can compose a real, honest, four-question assignment for `8r/Sc1`. It is not a workaround; it is
the ruled behaviour, landing on the one week it fits.

**But the producer must handle `ShortAssignment` as a normal outcome, not a 500.** Outside week
one, a class whose week is not banked yet gets *no* assignment and a clear reason, rather than a
half-filled one. Logged as a finding for Mide: **the scheme runs to week 35 and the bank reaches
week ~4 of it. The producer will go quiet in week 2 for Physics-led weeks.** That is a content
gap, not an engineering one, and it is the other session's territory.

### F4 · ⚠️ `/api/assignment-submit` discards every column the last run added

`/api/quiz-score` was extended (backend `2bc9459`, `6b44ad0`, `4ad4acc`) to carry `rung`,
`question_ref`, `selected_option_letter`, `correct_option_letter`, `criteria_met`,
`criteria_total`, and to stop coercing `is_correct` to `false` for a self-marked rung.

**Its sibling `/api/assignment-submit` — the route the assignment page actually posts to — got
none of it.** `server.js:445-451` still maps six fields and still writes `is_correct: !!a.is_correct`.
`assignment_question_attempts` grew all the same columns on 20 August; nothing writes them.

So the columns were opened on both tables and wired on only one. This is squarely B2's
"attempts carry question_ref, letter and text separate, `is_correct` NULL on self-marked", and it
is fixed tonight.

### F5 · The backend is NOT ahead of its remote

`git rev-list` against the *stale local* `origin/main` ref said the backend had two unpushed
commits. It has none: a fetch over SSH (origin is HTTPS and cannot authenticate) shows
`FETCH_HEAD == HEAD == 4ad4acc`. The local ref was simply old. Corrected before it became a
false premise.

### F6 · The mount seam already exists, but Design's data is not in it

`window.MrBadmusStudentRuntime.mount({into, template, imports, Component, props: {}})` — props
are already a parameter and already empty. But Design's example data is **not** passed in: it is
declared as class fields on `Component` itself (`work`, `roster`, `weekPts`, `lessonDefs`,
`questions`), extracted verbatim by the porter. So the seam has a socket and no plug, and the
fixture is welded to the logic. A2 is therefore a real piece of work, not a rename.

---

## The plan, decided

**Where the producer lives.** `compose_assignment()` is Python and the bank is 70 Python modules;
the backend is a separate Node repo. Three ways to bridge that were weighed:

1. Port the bank and the algorithm into the backend — duplicates 70 files of content, drifts.
2. Export the bank as JSON, vendor it into the backend, port the ~40-line algorithm to JS —
   one vendored copy, still a copy, and the *page* still has to scrape `/ks3/<slug>.html` for
   question text the way `student/assignment.html:96` does today.
3. **Export the bank and the lesson ladders into Postgres**, from a checked-in exporter, and let
   the backend compose from two tables it already talks to.

**Chosen: 3.** It keeps Python the single source (the tables are a build artefact, refreshed by a
gated script), it removes the DOM-scraping question resolver from the page entirely, and it means
the assignment page can read question text, options, option letters and per-distractor `why`
feedback directly. Both 2 and 3 need a backend deploy anyway; 3 needs less code and leaves less
that can drift.

**Order:** A2 data seam → schema → exporter → backend producer + submit fix → wire pages → drive →
gate → swap.

---

## C3 landed on main mid-run — pulled, and the nine instruments checked

Mide sent word mid-run that C3 had merged. Pulled before pushing anything further.

**It was a clean fast-forward, so there was nothing to resolve.** `origin/main` was two
commits ahead (`5306f1e20` C3, then merge `4df7c4dae`) and this branch was zero ahead, so
C3's contribution to `shared/ks3.js` and `shared/ks3.css` arrives byte-identical — it *is*
those commits. No hand-merge, no chance of losing a marked region. Verified after the pull:

| C3 region | expected | found |
|---|---|---|
| `wireCards` replacement | ~line 1046 | `shared/ks3.js:1060` |
| `BEGIN/END C3 wiring` block before `wireInstruments` | 1,257 lines | 17323–18578, **1,256 lines**, immediately before `wireInstruments` at 18580 |
| nine dispatch lines in their own BEGIN/END pair | 9 | 9, at 18844–18859 |
| appended `ks3.css` hunk | one | `BEGIN C3` 15634 → `END C3` 16731 |

⚠️ **A rebase was not possible and was not forced.** `git pull --rebase` refused because the
working tree was dirty — a subagent was mid-edit on `build_student_port.py` and
`shared/student-runtime.js`. Stashing would have pulled files out from under a running
process. Instead the incoming file list (620 files) was diffed against the dirty file list;
the intersection was **empty**, so `git merge --ff-only` was safe and was used. Recorded
because "I used ff-only instead of rebase" is exactly the kind of thing that should not be
silent.

### The nine instruments — and the one that looked dead and was not

Mide named the failure mode precisely: *a page that renders with a dead instrument looks
fine*. Every existing KS3 gate measures the page **at rest**, so none of them can see it.

So a new gate was written — **`ks3_instrument_liveness.py`**. It serves the built site,
loads each page in headless Chrome, presses the controls inside each instrument block, and
asserts the block's own DOM changed. A wired instrument responds to its own controls; a dead
one is inert, and inert is invisible in a screenshot.

**First run flagged `dissolve-lab` as INERT. It is not. My probe was wrong.**

The dissolving bench ships `<div class="ks3-dlab" data-dlab hidden data-dlab-lock=
"gate-which-dial">`. It is **deliberately locked** behind the predict block above it:
`ks3.js:17708` reads `data-dlab-lock`, finds the sibling `[data-activity]` block it names,
hides the whole section, and re-opens it when any option in that gate is clicked. Every
control was therefore 0×0 and my probe skipped all eleven of them.

⚠️ **Two things nearly let that false positive through as a real finding.** First, a
`grep --include=*.py` run under zsh errored on the glob (`no matches found`) and printed
nothing — which reads exactly like "this string appears nowhere", and I briefly took it that
way. Second, the lock names its gate by `data-activity`, not by `id`, so searching for
`id="gate-which-dial"` also found nothing. Both dead ends pointed the same wrong way. What
settled it was reading the wire function itself.

The probe now opens gates before pressing, and the distinction it draws — *locked* versus
*dead* — is the whole value of the gate. A liveness check that cannot tell them apart
reports every gated instrument as broken and is worse than no check at all.

**Result: 9/9 C3 instruments live.**

```
✅ purity-sorter        pure-or-mixture.html            ✅ still-run            distillation.html
✅ dissolve-lab         dissolving-and-solutions.html   ✅ chroma-run           chromatography.html
✅ sequence-rebuild     filtration.html (2 blocks)      ✅ plan-critique        proving-something-is-pure.html
✅ crystal-bench        evaporation-and-crystallisation ✅ melting-point-bench  proving-something-is-pure.html
✅ method-choice        evaporation-and-crystallisation
```

Zero console errors on any of the seven pages.

### And C3 grew the question pools

C3 brought seven new `questions_*.py` modules, so the export is no longer 70 lessons:

| pool | before C3 | after C3 |
|---|---|---|
| bank | 840 questions / 70 lessons | **924 / 77** |
| ladder | 140 / 70 | **154 / 77** |

The export is idempotent upserts, so re-running it after a content merge is the whole
maintenance story. It has been re-run and re-applied.

---

## B1 — the assignment producer. Built, deployed, proved.

The consumer shipped in MRB-238. The producer never did. It does now.

### Where it lives, and why it took a schema change to get there

`compose_assignment()` is Python and the bank is 77 Python modules; the Render backend is
Node, in another repo. The bridge chosen was **mirror the pools into Postgres** (the
reasoning is in the plan section above). That meant three migrations, all applied to
production `urklkrwevjtlfbwnipjn` one at a time via `apply_migration`, BEGIN/COMMIT stripped:

| version | what | why it was needed |
|---|---|---|
| `20260820212314` | `assignments_class_week_uniq` — partial unique index on `(class_id, academic_week)` | **the concurrency ruling.** Two students opening the class in the same second would each find nothing and each compose one |
| `20260820212322` | `assignment_questions.band` added, `rung` made nullable, `rung XOR band` check | **`rung` was `NOT NULL` with a CHECK in (recall, apply, explain, produce).** A bank question has a *band*, not a rung — Mide's 20 Aug ruling made difficulty a property of the question. So a bank question could not physically be stored. This was the schema gap that would have stopped the build |
| `20260820212341` | `ks3_bank_questions` + `ks3_ladder_questions`, RLS read-only to `authenticated` | the pools |

⚠️ All three were written back as local files under `supabase/migrations/` with the exact
versions Postgres recorded, because `apply_migration` writes no local file and records its
own version — the known drift gotcha. Without that, the next `db push` re-applies them.

**Of MRB-239's four schema gaps, three were already closed** by earlier runs
(`assignments.academic_week`, `auto_generated`, `source_sow_entry_id` all existed). The
fourth — the `rung` NOT NULL — is the one closed above. Nothing else was touched.

### The rules it implements

- **The week comes from the server clock against the year's dates.** Never `is_current`
  (2025-26 still carries `is_current = true` tonight), never the device clock.
- **Current week only. It never backfills.**
- **Only classes in the current academic year with scheme-of-work rows.**
- **Short outside week one is refused, not shipped.** If fewer than fifteen questions are
  reachable and it is not week one, no assignment is created and the caller gets a `reason`.
  A 200 with `"reason": "not_enough_banked_questions"` — "no work set this week" is a normal
  state, not an error.
- **The race is settled by the index, not by a lock.** The loser catches `23505`, re-reads,
  serves the winner's row. Safe *because composition is deterministic* — both would have
  written the same fifteen.
- A scheduled trigger can later sit on top as "the first visitor" and call the same
  function. Nothing would need reworking. Not built tonight.

### The JS mirror is proved against the Python, not against my expectations

`composeFromBank` in `assignment-compose.js` is a second implementation of one ruling, which
is the exact arrangement that drifts. So `test_assignment_compose.js` does not check it
against hand-written answers — it shells out to the real `compose_assignment()` in this repo,
on real bank data, and compares the chosen question ids.

**25 assertions, 0 failures**, including four cross-checks at three different bands:

```
✅ case 1: JS picks exactly what Python picks (4 questions, band standard)
✅ case 2: JS picks exactly what Python picks (15 questions, band standard)
✅ case 3: JS picks exactly what Python picks (15 questions, band harder)
✅ case 4: JS picks exactly what Python picks (15 questions, band easier)
```

If the site repo is ever absent, that test SKIPS loudly rather than passing quietly.

`dueAtFor` is tested on both sides of the October clock change — 18:00 school-local is 17:00Z
in September and 18:00Z in November, and an implementation that is right for half the year
looks right until half term.

### F4 fixed — `/api/assignment-submit` was throwing away six columns

Detailed in the findings above. It now carries `question_ref`, `rung`, both option letters
and both self-marking columns, and `is_correct` survives as `null`.

**And a second defect found while fixing the first:** `score` counted
`answers.filter(a => a.is_correct)` and `max_score` was `answers.length`. A self-marked rung
sends `is_correct: null`, so it was **scored as wrong** and counted against the student.
Now only markable questions are scored — `max_score` is what the platform could mark, not
what was asked.

### Deployed, and proved BEHAVIOURALLY

`/api/health` cannot prove which build Render is serving. So the proof is the new route
itself: before the deploy `GET /api/class/current-assignment` returned **404**; forty-one
seconds after the push it returned **401** (auth required). A route cannot demand
authentication until it exists.

```
22:35:52  404  (old build)
22:36:13  404  (old build)
22:36:33  401  ← new build live
```

### B3 — driven against production as a real student

`MRB_TEST_STUDENT_PASSWORD` was **set**, so the drive signs in as
`midebolabadmus@gmail.com` and **no throwaway account was created** — the pre-authorised
account-creation fallback was not needed and not exercised. No credential reaches a file, a
log, a commit or a capture; the token is truncated to eight characters everywhere it is shown.

Passing already:

```
✅ signed in                                             ✅ a class the student is NOT in → 403
✅ producer returns 200                                  ✅ no bearer token → 401
✅ current week is 1 (the year opens 1 Sep)              ✅ recall returns 200
```

**Deviation: the drive script hit `CERTIFICATE_VERIFY_FAILED` before it could do anything.**
macOS system Python has no usable CA bundle and `certifi` is not installed, while `curl` —
which uses the system trust store — was fine all along. Fixed by pointing `ssl` at
`/etc/ssl/cert.pem`. ⚠️ Deliberately **not** fixed with an unverified SSL context: this
script signs in with a real password, and a disabled-verification switch is not a thing to
leave lying in a drive script where somebody later copies it.

---

## A2 — the data seam. Built before the wiring, as ruled.

The finding from the last run was that `student_behaviour.py` oracles the ported page against
**Design's own delivered file**, so the moment the port loads real data every drive diverges
on every screen and the gate stops being able to say anything. The ruling was to build a
fixture mode first. Done.

**The seam had to reach further than expected (F6).** Design's example data is in two places,
not one:

1. **Class fields on the logic** — `work`, `roster`, `weekPts`, `lessonDefs`, `questions`
   (class view); `questions`, `wrongPlan`, `figCaptions`, `KEY`, `DUE` (assignment).
2. **Literal text nodes inside Design's template** — `8r/Sc1`, `Ayo`, `AY`, `Mr Badmus`,
   `MB`, `28 students`, `Biology`, `Cells & microscopy`, `AUTUMN TERM`, and the welcome line.

⚠️ **The second half could not be solved the obvious way.** Turning a literal text node into
an interpolation would have been one line — but `shared/student-runtime.js` wraps every
interpolation in `<span class="sc-interp">` and leaves a literal bare. That wrapper is
deliberate (it is 132 nodes on the class view, and the parity gate counts nodes), so
converting the literals would have silently added wrapper spans and broken structural parity.
The literals are therefore bound **by path**: the porter records a path into the template
JSON per binding, and the runtime clones the tree and sets `node.v` in place before
rendering. The node stays a literal, the node count is unchanged, and the gates never notice
the seam is there.

**Fixture mode is a separate PAGE, not a flag.** The porter now emits four pages:

| page | last script tags | carries fixture data? |
|---|---|---|
| `class-ported.html` / `assignment-ported.html` | `<script src="/shared/student-live.js">` | **no** |
| `class-fixture.html` / `assignment-fixture.html` | the fixture, then `__MRB_MOUNT__()` | yes |

Both are the same bytes apart from the banner and those last two tags. **The production page
has no code path to the fixture at all** — which is a stronger guarantee than a flag, because
a flag can be set. And `student-live.js` **throws** rather than falling back to the fixture:
a fallback would make "the production page cannot render Design's example data" a matter of
configuration, and it needs to be a matter of fact.

### Both gates green, with nothing weakened

```
student_behaviour.py   27 drives, every one "text identical", RULED_DIVERGENCE untouched
student_parity.py      all 8 layers A–H green at 360 / 390 / 820 / 1460
```

`grep -c "Ayo\|Mr Badmus\|28 students\|Tiwa A\.\|Cells & microscopy"` on both **production**
pages: **0**.

### ⚑ A content consequence Mide should see — the closed right-answer slot

Design's own recall data carries **four** feedback strings, one per option, the correct one
reading *"Right. Each lens magnifies the image the next one receives…"*. The real lesson
ladder carries **three** — one per distractor. The correct option has none, deliberately, and
parity layer H forbids inventing a fourth ("0 authored right-answer line(s): none yet, which
is the ruled state").

**So when a student answers a recall question correctly on real data, there is no sentence
under it.** That is the ruled behaviour and it is what has been built. It is also a visible
difference from Design's mock, and it is Mide's call whether to leave it or ask authors to
write a fourth string per rung. **Not a bug. A ruling with a consequence.**

### ⚠️ And the seam unit found a defect worth more than the seam

**The three MRB-275 rulings had been applied to generated files.** Commit `895f34766`
(20 Aug) applied them correctly and carefully to four files — and all four are build output:

```
student/class-ported.html            mrbadmus_site/student/class-ported.html
student/assignment-ported.html       mrbadmus_site/student/assignment-ported.html
```

`build_student_port.py` writes all four, and its own banner says *"GENERATED — do not edit"*.
So the rulings held for exactly as long as nobody re-ran the build — and **this run re-ran
it**, which silently reverted all three and turned the behaviour gate red in thirteen places
naming a divergence that had been correct that morning.

That is the same class of mistake `895f34766`'s own commit message diagnosed in its
predecessor, made one layer down: `student/class-ported.html` sits in the repo root and reads
like source. It is the mirror.

**Fixed properly, not re-applied.** The rulings now live in `student_rulings.py` as
transformations applied to Design's logic and template at build time. Every `new` string is
byte-for-byte what `895f34766` wrote, *extracted from that commit rather than retyped*, and
the build asserts each `old` appears **exactly once** in Design's delivery before touching it
— so if Design redraws that span, the build stops rather than applying a ruling to a line
that has moved. A rebuild now carries the rulings instead of destroying them.

⊕ **And it clarifies the "980 feedback lines" blocker** recorded on 20 Aug in `64c3815d4`.
980 = 140 ladder rungs + 840 bank questions, and the missing line is the **right answer's**
explanation, in every one of them. It was never authored anywhere. Ruling 1a is what settles
it: v1 ships with three feedback strings and the right-answer slot closes. So the blocker is
not outstanding work — it is a ruling, already applied. The distractor feedback, by contrast,
is complete: **2,520 wrong options, every one carrying its `why`; 924 correct options, not
one of them carrying a line it should not have.**

### B3 — the drive passed. A real assignment now exists on production.

```
assignment  72a5b315-f8ef-4c04-9369-664c8d1a4b8e
title       Breathing and gas exchange · Pressure · Chemical reactions
due         2026-09-03T17:00:00Z   ← Thursday 3 Sep, 18:00 British Summer Time
week        1        auto_generated  true      quiz_type  subtopic_quiz
questions   b4-01-s01 … s04, positions 1-4, rung NULL, band 'standard'
source_sow  → the week-1 Biology row, `the-gas-exchange-system`
```

Every field read back from production and checked. `teacher_id` is the class's own teacher,
`subject_id` is `Science` (the KS3 filing subject), `school_id` / `key_stage` / `year_group`
match the class, and the `rung XOR band` constraint held — every question row carries a band
and no rung, which is what the migration was for.

**All 21 drive checks pass**, including the two that matter most for trust:

```
✅ second call did NOT create; same id, same questions, same order
✅ a class the student is NOT in → 403;  no bearer token → 401
✅ the RIGHT-ANSWER slot is closed (why is null, not a generic line)
✅ exactly three feedback strings, one per distractor
```

**It is four questions, not fifteen**, and that is the ruled behaviour rather than a fault:
week 1's three lessons are Biology `the-gas-exchange-system` (banked), Physics
`pressure-force-over-area` (not banked) and Chemistry `chemical-vs-physical-change` (not
banked). One banked lesson supplies four standard questions, week one is allowed to be short,
and there is nothing earlier in the scheme to fill from. **From week 2 onward this class gets
no assignment at all until Physics and C4+ are banked** — the producer refuses rather than
shipping short. That is a content gap, and it is the other session's territory.

### ⚑ The pools: 1 MB applied in two seconds, via one guarded function

Loading 924 + 154 rows as generated SQL through MCP round-trips was slow and kept stalling
part-way. Replaced with `ks3_pools_ingest(pool, payload)` — SECURITY DEFINER, taking the whole
pool as one jsonb payload over PostgREST. Both pools now apply in about two seconds.

⚠️ **The guard is the entire safety story**, so it is written down plainly: it is *not* open
to `authenticated` at large — a student with a valid JWT must not be able to rewrite the
question bank — and it raises unless the caller's email is Mide's own. Migration
`20260820220000`. If Mide would rather it did not exist, dropping it costs nothing but speed;
nothing calls it except the exporter.

**Deviation: I burned time on this the wrong way first.** Three separate subagents were asked
to apply the SQL and between them managed two chunks in half an hour. I should have reached
for a different mechanism after the first one stalled instead of the second and third.

### ⚠️ B4 CONDITION NOT MET — fixture content is still reachable in production

The seam closed every class field and every bound template literal, and
`grep "Ayo\|Mr Badmus\|28 students\|Tiwa A\."` on the production page is 0. But four strings
are welded inside **method bodies** rather than field initialisers, so the extractor could not
see them, and they still ship:

| line | what still ships |
|---|---|
| `shoutouts:` | `{ who: 'MB', text: 'Best score in the class on digestion this week.', meta: 'MR BADMUS · 2 DAYS AGO' }` |
| `crumbRight:` | `'AUTUMN TERM · WEEK 04 / 12'` and `'WK 04 / 12'` |
| `boardScopeNote:` | `'WHOLE AUTUMN TERM'`, `'WEEK 04'` |
| `<title>` | `8r/Sc1 · My class · MrBadmusAI` |

The seam unit reported all four rather than hiding them, and the build names them on every
run. **This alone is enough to hold the B4 swap**, and it is being closed next.

### The submit route, driven and read back — F4 proved fixed

Three answers posted as the real student: one right, one wrong, and one **self-marked** rung
sending `is_correct: null` with `criteria_met: [1, 3]` of 3. That third row is the whole
point — it is the shape that used to be coerced to `false` and counted against the student.

```
POST /api/assignment-submit → {"success":true,"score":1,"max_score":2}
```

**`max_score` is 2, not 3.** Only what the platform could mark is scored. Read back from
`assignment_question_attempts`:

| # | question_ref | sel / correct letter | is_correct | criteria |
|---|---|---|---|---|
| 0 | `b4-01-s01` | B / B | `true` | — |
| 1 | `b4-01-s02` | **B / A** | `false` | — |
| 2 | `b4-01-s03` | null / D | **`null`** | `[1,3]` of 3 |

The letter is its own column and differs from the text; `is_correct` survives as null rather
than becoming a false claim; the criteria the student claimed are recorded as what they are.
Every one of the six columns the route used to discard is populated.

### Identity scoping proved at the database, not just at the route

The route returns 403 for a class the student is not in — but the page will also read Supabase
directly, so RLS was probed with the student's own JWT:

```
✅ assignments for my class            2 rows      ✅ a class I am NOT in            0 rows
✅ assignment_questions of mine        4 rows      ✅ another student's submissions   0 rows
✅ my own submissions                  2 rows      ✅ INSERT into ks3_bank_questions  42501 refused
✅ the reference pools readable        4 / 2 rows
```

RLS is enabled on all six tables including the two new pools. `submissions_teacher_read` and
`attempts_teacher_read` exist and are scoped by `auth_user_teaches_class(...)` **and**
school, so the submission is visible to this class's teacher and to nobody else's.

⚠️ **Verified structurally, not driven.** I do not hold the teacher account's password, so
"the submission shows on the teacher dashboard" is proved by the policy and the row, not by
signing in as the teacher and looking. That is the one part of B3 I could not do end-to-end,
and it is named here rather than glossed.

### The mirror is now gated, not just asserted

The migration comment claimed "a gate asserts they match". It does now:
`export_ks3_questions.py --verify` reads both live tables over PostgREST and compares them
against Python **row for row, field for field**, including the options JSON.

```
✅ bank      924 in Python,  924 live, 0 missing, 0 extra, 0 differing
✅ ladder    154 in Python,  154 live, 0 missing, 0 extra, 0 differing
✅ the database is exactly what these files say it is.
```

It names the three ways a mirror rots, separately, because they mean different things: rows in
Python and not live (*the export was never applied*), rows live and not in Python (*a retired
question is still being served*), and rows that differ (*edited and not re-exported*).

⚠️ It **SKIPS LOUDLY** without `MRB_TEST_STUDENT_PASSWORD` rather than passing — same rule as
the JS/Python cross-check in the backend. A gate that goes green because it could not run is
the exact failure this project keeps naming.

Cross-check: `verify_questions.py` independently reports **77 lessons, 924 questions, all nine
checks clean** — the same numbers the exporter produces and the same numbers now live.

### ⚠️ Deviation — a subagent I had stopped kept writing to production

One of the SQL-loading subagents, before I stopped it, had spawned **its own fleet of
children**. Stopping the parent did not stop them. Forty minutes later they surfaced one at a
time, reporting successful writes to production out of `/tmp/ks3-transport/` — 55 SQL files I
had not generated and a directory I had not created.

**No harm done, and here is why, checked rather than assumed.** They were applying the same
generated upserts from the same export, and the upserts are idempotent. `--verify` was run
immediately afterwards: **924/924 and 154/154, nothing missing, extra or differing.** The
stray files have been deleted.

But it is worth writing down plainly, because the general shape is nasty: **stopping an agent
does not stop the agents it started**, and their writes land on production long after you
believe you have stopped them. Tonight it was harmless because the writes were idempotent and
identical. If they had not been, I would have had unsupervised concurrent writers on a live
table with no way to tell which one wrote last. The lesson is not "check the children" — it is
that a task which writes to production should not be delegated to something that can fan out.

### ⚑ A design point for whoever does the swap — read this first

`generate_site_v5.py:5255` copies the **whole `student/` directory** into the output tree, so
`student/class.html` is *hand-written source* today. Both generators list it in `_REFUSED` and
physically cannot write it.

A swap that copies the ported build output over `student/class.html` would put **generated
output into a source path** — which is precisely the trap that cost this run a red gate and
`student_rulings.py` to fix (the MRB-275 rulings were hand-edited into `-ported.html`, which
is build output, and the next build ate them). Doing it that way would set the same trap one
more time, one file along.

**The swap should therefore be: take `class.html` and `assignment.html` OUT of `_REFUSED` and
let `build_student_port.py` write them directly.** The old hand-written pages retire to a
dated name; git holds them regardless. Then a rebuild keeps the live page correct instead of
reverting it, and nothing about the live pages is ever edited by hand again.

### A second backend deploy — and one I could NOT prove behaviourally

Self-reviewing the producer turned up a latent bug: `schemeLessons()` filtered the scheme by
key stage and year group and **ignored `tier` and `pathway`**. At KS3 both are NULL by table
constraint, so it made no difference. At KS4, where a scheme row exists per (tier, pathway),
it would have handed a Foundation Combined class the Higher Triple scheme — silently, with
real lessons in it, on a page that would look entirely normal. There are no KS4 scheme rows on
production yet, which is the reason to fix it now rather than the reason to leave it.

⚠️ **This change is deliberately a no-op on today's data, so it cannot be proved
behaviourally, and I am not going to pretend otherwise.** The first deploy was provable
because the route went 404 → 401: a route cannot demand authentication before it exists. This
one changes a filter whose effect on every row currently on production is nil. There is no
observable difference to point at.

What I did instead, and what it does and does not show: re-ran the full drive after the
redeploy — **all 21 checks still pass**, same assignment, same questions, same order. That
proves the deploy did not break the working path. It does not prove the new build is the one
answering. `/api/health` returning 200 shows only that the service is up.

The honest state: the guard is committed (`d0b65b5`) and pushed, Render auto-deploys from
`main`, and its correctness is covered by the KS4 case being unreachable rather than by a
measurement. **The first KS4 scheme rows to land should be treated as the test.**

---

## B2 — the pages, wired. The class page renders real data. The assignment page refuses.

`shared/student-live.js` (630 lines) loads the SDK, `config.js`, `class-entry.js`,
`student-guard.js` and `student-data.js` **in that order** (load-bearing, per CLAUDE.md),
resolves the student's working-year class, and maps 21 keys for the class view and 8 for the
assignment.

**The class page works.** At 390px and at 1460px, against production:

```
✅ rendered — 358 node(s)          ✅ nothing renders as 'undefined'
✅ no console errors               ✅ this week's real assignment title is on screen
✅ the student's real identity is on screen — 8r/Sc1, AY
```

Screenshots: `docs/ks3/shots/wired-class-390.png`, `wired-class-1460.png`.

**The assignment page refuses**, honestly: *"This week's work is not ready yet. Check again
later today."* Because this week's real assignment has **four** questions and the page's own
logic has a hardwired floor of six (`roundLive: st.qi < 6`, `Math.min(st.qi, 5)`, "/ 06"). The
loader would rather say nothing is ready than mount a page that runs off the end of the array
mid-assignment. That is the right refusal and it is content meeting a page limitation, not a
wiring fault.

### Three real defects found by driving, and fixed

1. **The guard fail-closed with no explanation** — three runs bounced straight to `/auth.html`
   and it looked like broken wiring. `shared/config.js` selects the **TEST** Supabase project
   on `localhost` and `127.0.0.1`, deliberately, so local dev cannot touch real students. The
   guard's client then looked for a session under the test project's storage key and found
   none. `config.js` has an escape hatch built for exactly this — `?env=prod` — and the drive
   now uses it. **Nothing was wrong with the page.**
2. **CORS blocked every backend call from the drive.** The allowlist is the four real origins.
   Fixed by serving the drive from `http://localhost:5500`, which the allowlist **already
   contains** — the live allowlist was not widened to make a test possible.
3. **⚠️ `Date` is not a CORS-safelisted response header**, so `res.headers.get('date')`
   returned null cross-origin, silently, with no error anywhere. The pages decide whether work
   is still open or **missed** and are required to decide it against the server's clock, never
   the device's — a tablet a week fast would grey out this week's work as overdue. Without a
   readable Date the loader refused to render rather than guess. One line on the backend
   (`exposedHeaders: ['Date']`) makes the refusal unnecessary.

   **This deploy WAS provable behaviourally**: `access-control-expose-headers: Date` was absent
   at 23:20:24 and present at 23:21:10.

### ⚠️ And the thing a screenshot caught that my own check could not

With the class page finally rendering, the text check said **no fixture content on screen**.
It was wrong, and I only found out by looking at the picture. The docket at the top of that
page still read:

> **QUESTIONS 8 · DRAWS ON Using a microscope · SET Mon 15 Sep · DUE Thu 18 Sep, 18:00 ·
> 2 days left · 40 POINTS AT STAKE**

over a real assignment of **four** questions due **Thursday 3 September**. Also hardcoded:
"Eight questions, set from this week's lessons", "Answer the eight questions", the recall
panel's "46 ANSWERED THIS WEEK", the term spine's twelve weeks with **week 04** marked as now,
and "LEADERBOARD WEEK 04 · FINAL".

**My `FIXTURE_TELLS` list held names and headlines and no numbers.** So the check went green
on a page telling a student the wrong number of questions and the wrong due date. The list is
now widened — counts, dates and week numbers included — and the drive fails as it should:

```
❌ NO fixture content on screen — leaked: Using a microscope, Mon 15 Sep, Thu 18 Sep, DUE THU 18:00
```

The general lesson, written down because it will recur: **a fixture tell is not only a name.**
It is any authored constant that a real page must have replaced, and the numbers are the ones
that read as plausible.

---

## B4 — THE SWAP: NO. Four independent conditions fail.

The live pages are untouched. `student/class.html` and `student/assignment.html` are exactly as
Mide left them.

| # | condition | verdict |
|---|---|---|
| 1 | parity green at 360/390/820/1460 | ✅ green, all 8 layers |
| 2 | behaviour green through the A2 seam | ✅ green, 28 drives, text identical |
| 3 | **no fixture content reachable in production** | ❌ **the docket, the recall count, the term spine and the leaderboard week are hardcoded in Design's logic where the seam cannot reach** |
| 4 | **B3 passed with every field correct** | ❌ **the assignment page will not render this week's real work (4 questions < its hardwired 6)** |
| 5 | full gate set green | ✅ for the gates that exist |
| 6 | Render proven behaviourally | ✅ twice; once honestly not-proven and said so |

And the one that would block it on its own, independent of all six:

⛔ **`handIn` submits nothing.** `assignment-ported.html:280`:

```js
handIn = () => {
  const stamp = this.state.late ? '20 SEP, 19:07' : '17 SEP, 20:41';
  ...
};
```

It writes a **hardcoded timestamp** and posts to no endpoint. A student pressing "Hand it in"
would see a false hand-in time — 17 September, whatever today is — and their work would never
reach their teacher. `/api/assignment-submit` exists, works, and was driven and proved tonight;
the page simply does not call it.

**Swapping tonight would have replaced a working page with one that loses a child's work.**

Per B5: since B4 did not swap, the demo assignment on `8r/Sc1` and the test student's
enrolment are **left in place** — they remain the fixtures. Nothing was deleted.

---

## B6 — fresh eyes on the edges

### The concurrency ruling, proved at the mechanism

The one part of B1 the drive could not exercise (it needs two simultaneous first-openers) was
tested directly against the index, inside a transaction that rolls back either way:

```
unique_violation (23505) — the second writer lost, as ruled
```

Nothing was left behind. The route's `catch (23505) → re-read → serve the winner's row` is
therefore sitting on a mechanism that provably fires.

### What an interrupted or malformed hand-in does

| what a student's browser sends | what comes back |
|---|---|
| no `answers` array (connection died mid-post) | `400 assignment_id and a non-empty answers array are required` |
| an empty `answers` array | `400` — same |
| no `assignment_id` | `400` — same |
| **2 of 4 questions answered** — what an interrupted student actually produces | `200 {score: 1, max_score: 2}` — accepted, and scored on what was answered |
| `band=zzz` | `200`, falls back to `standard` |
| `class_id` that is not a UUID | `404 class_not_found` |
| no `class_id` | `400 class_id is required` |

A partial hand-in being accepted and scored on what it contains is the right behaviour: a
student who loses their connection halfway should not lose the half they did.

### ⚠️ And one real defect, found and fixed

**A hand-in against an assignment id that does not exist returned a 500 carrying raw Postgres
text** — `insert or update on table "assignment_submissions" violates foreign key constraint …`.
That tells the student nothing, tells anybody else the table and column names, and reads as
"the site is broken" when the truthful answer is "that is not a piece of work you have".

Now `404 assignment_not_found`, and `403 not_your_assignment` for one belonging to a class the
student is not in — the route validates before it writes.

**Proved behaviourally**, the third deploy tonight that could be: 500 at 23:35:48, **404 at
23:36:03**.

### Flakiness, observed once

One run of the page drive rendered the error state at 390px (20 nodes) while desktop was fine.
Two further consecutive runs were clean at both widths (371 and 358 nodes). Most likely a cold
Render instance on the first request of that run. **Recorded rather than dismissed** — one
failure in five runs is exactly the rate that gets explained away and then turns out to be
real.

### Still welded, and left deliberately

The seam unit closed **seven** literals, not the four it was given — the current week number is
also spliced into the readings strip and the work row, and the teacher's real name was hiding
inside the status word `'WITH MR BADMUS'`, which no grep for the name would have matched in
that shape.

What remains welded in Design's logic is **figures rather than names**, and it is listed here
rather than quietly left:

- the docket: `'2 days left'`, `'40 POINTS AT STAKE'`, `'58%'`, and the leak the screenshot
  caught — the question count, `'Using a microscope'`, `'Mon 15 Sep'`, `'Thu 18 Sep, 18:00'`
- the recall panel's `'46'` and the readings strip's paired `'46'` / `'77%'`
- `recallStats` `'ROUNDS', '08'`, and **`pad(Math.max(9, st.streak))` — a hardcoded floor of 9
  on a real student's best streak**
- `roundNote: 'Six answers logged against Week 04…'` — the same week datum in lower case,
  which is the only reason it survives the grep
- `'DUE THU 18:00'`

Every one of these is student-visible and wrong on real data. They are the reason B4's third
condition fails, and closing them is the next unit's whole job.

### Two things the units found in passing

- **`_MUST_NOT_LEAK` in `build_student_port.py` is defined and never referenced** — dead since
  it was written. The assertion that actually runs iterates `bind_values`, which is broader, so
  nothing is unguarded; but the constant is a promise nothing keeps.
- **A student can hand the same assignment in repeatedly**, each creating a new
  `assignment_submissions` row with `attempts: 1`. There is no unique constraint on
  `(assignment_id, student_id)` and no upsert. Whether a re-do should replace, add an attempt,
  or be refused is a product decision — Design's own work rows carry a `retake` flag, so the
  intent exists somewhere. **Not decided tonight.** Flagged because `handIn` will hit it the
  moment somebody wires it up.

### Test data left on production, precisely

B5's housekeeping is conditional on B4 swapping, and B4 did not, so nothing was deleted. What
exists on `8r/Sc1` this morning:

| | |
|---|---|
| the hand-seeded demo assignment (`282f2277`, `academic_week` null) | **left** — B5 says it stays if there is no swap |
| the producer's first real assignment (`72a5b315`, week 1, 4 questions) | **left** — it is the working example |
| 3 submissions by the test student | **left** — one full, one partial, one pre-existing. They are the only worked examples of a real submission with the new columns populated, and the pages are not live, so no student sees them |
| the test student's enrolment in `8r/Sc1` | **left** — B5 says it stays if there is no swap |

No throwaway account was created; `MRB_TEST_STUDENT_PASSWORD` was set, so the pre-authorised
fallback was never needed.
