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
