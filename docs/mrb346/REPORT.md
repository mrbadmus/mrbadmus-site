# MRB-346 — Gate machinery: make a landing cost minutes, not hours

Branch `feat/gate-machinery`, off `origin/main` at `96fa2f0b8`. Touches gate,
drive, and registry code only — no product code, no content, no generators.

## 1 · Why

The night-2/worksheet landing finished its real work by Sunday afternoon and
then spent roughly 30 hours on: docs commits invalidating all 18 receipts
(twice); drives dirtying the tree with screenshots; a drive exhausting its
own rate limit; one DNS blip turning nine gates red; and a content-only
branch running the full site drive suite that provably reads nothing from
the question bank. This ticket fixes the machinery, not the content.

## 2 · What changed

### 2.1 · `watches`, on every gate

Every one of `gate_registry.py`'s 49 pre-existing gates (50 with the new
`gate_watches_check`) now carries a `watches` list — glob patterns naming
every tracked file that can change that gate's outcome. Built by reading
each gate's script, its imports, and (for a `*_drive.py` gate) the page(s)
it drives and the generator/shared assets behind them; then independently
reviewed by an Opus pass against the same standard, which corrected 14
gates — see §2.2.

Two absolute rules, enforced by the new `gate_watches_check` fast gate:

1. `docs/**`, `**/*.md`, `docs/**/shots/**`, and `README*` may never appear
   in any `watches` list.
2. Every gate's `watches` must be non-empty and must include the gate's own
   script.

### 2.2 · The Opus review — 14 gates corrected

Under-watched (a real dependency was missing):

- **`ks4_chrome_tells`** — added the whole built tree its wall-walk actually
  visits (`mrbadmus_site/{teacher,student,consumer,parents,go,org}/**`); it
  previously watched only the chrome pages themselves, i.e. the half that
  can't drift.
- **`export_ks3_questions_verify`** — added `shared/config.js`, the file
  `--verify` reads its anon key out of.
- **`teacher_picker_drive`** — added `shared/set-work.js`/`.css`, which its
  fixture links.

Over-watched (a false dependency, verified by reading the actual code path):

- **`teacher_behaviour`**, **`teacher_reach`**, **`teacher_picker_drive`** —
  removed `shared/teacher-live.js` (and `teacher_behaviour`/`teacher_reach`
  also `shared/rum.js`, `shared/tokens.css`): a `-fixture.html` replaces the
  live page's last two script tags with Design's data/mount, so it never
  loads that chain.
- **`leaderboard_behaviour`** — removed the two `leaderboard.html` copies;
  it drives `leaderboard_fixtures/` only.
- **`ks4_pool_drive`** — removed `ks3_data/**`; it imports only `ks4_data`,
  and the KS3 half of its collision check is asserted on id prefix, which no
  KS3 authoring change can move.
- **`import_year_drive`**, **`mrb328_import_picker`** (`--section b`) —
  removed `supabase/functions/roster-import/**`; both stub the function
  call, so its source cannot change their outcome.

Narrowed (a real dependency, but the wrong grain):

- **`pool_ownership`**, **`teacher_admin_real`** — `supabase/migrations/**`
  narrowed to the one migration file each actually reads/depends on;
  RLS behaviour changes when a migration is *applied*, not when the file
  lands, so watching the whole folder would have selected a slow,
  credentialed, row-writing drive for every unrelated migration in the
  estate.
- **`3d_parity`** — `3d-studio/reference/**` narrowed to `*.html` (it opens
  two named files; the glob otherwise swept a `.md` design-notes file), and
  added `.design-sync/**` by extension so its own `.md` files stay excluded.
- **`verify_ks3`** — re-scoped to what its KS4-drift check actually reads
  (`git status --porcelain`, then `mrbadmus_site/ks3/**`, `generate_site_v5.py`
  and the shared assets the driven pages load) rather than an arbitrary
  quarter of the root HTML surface the check's own logic doesn't single out.

### 2.3 · A named, accepted gap under the docs/md rule

A few gates' real source-of-truth genuinely lives under `docs/`:

| gate | speed | what's unwatchable |
|---|---|---|
| `ks3_rail_manifest` | fast | both sides of its comparison (`docs/ks3/design-reference/*/*.dc.html` vs `docs/ks3/rail-manifest.md`) are under `docs/` |
| `ks3_statutory` | fast | its register, `docs/ks3/statutory-register.md` |
| `student_switches` | **slow** | Design's reference standalones under `docs/ks3/design-reference/student/` |
| `leaderboard_tells`, `ks4_chrome_tells` | fast | their vendored `.dc.html` tell-corpus (their *live-page* watches are unaffected and verified correct) |
| `3d_parity` | slow | three `.md` files inside its own sweep roots (watched by extension instead) |

`ks3_rail_manifest` and `ks3_statutory` are `fast`, so the pre-push hook's
"every fast gate runs regardless of selection" rule backstops the gap.
`student_switches` is `slow` and does **not** have that backstop — a change
to a Design standalone under `docs/` will not select it. This is the one
gap this ticket ships with rather than closes, because rule 1 is
unconditional and the alternative (bending it) is worse than naming it.

### 2.4 · `prepush_gate.py` — watch-hash receipts, affected-gate selection, one retry

- A receipt now binds to a `watch_hash` (a fingerprint of the blob-sha of
  every tracked file a gate's `watches` cover) instead of `HEAD^{tree}`. A
  receipt survives any commit that doesn't touch a path in the gate's own
  `watches`.
- `--record-all` and `--check` (the pre-push hook, unchanged:
  `hooks/pre-push` still calls plain `--check`) compute the paths this
  branch's own commits touch since the merge-base with `origin/main`, and a
  slow gate with no already-valid receipt is only required if one of those
  paths falls in its `watches` — otherwise SKIPPED BY RULE, printed by name.
  `--force` bypasses selection (used once, below, because this branch
  changes the machinery itself).
- A gate whose failure output matches a known transient signature
  (`urlerror`, `closed the websocket mid-frame`, DNS/timeout strings, …) is
  retried once before it counts; a receipt records `retried: true` either
  way, and a second failure is a real red regardless of signature.
- Fast gates are untouched by any of this — they still run on every
  invocation, unconditionally, exactly as before.

### 2.5 · Drives — MRB_SHOTS, and a live bug it caught mid-landing

`ks3_browser.gate_tmp()` now resolves `$MRB_SHOTS` → `$KS3_GATE_TMP` →
`~/tmp/ks3-gates`, in that order — outside the repo by default. While
verifying this, `set_work_drive.py --shots` was found defaulting to
`docs/mrb335/shots` (a committed path) and caught live overwriting 18
committed reference screenshots during this ticket's own verification runs.
Fixed to the same scratch root; a caller who wants to refresh committed
evidence still passes `--shots docs/mrb335/shots` explicitly.

### 2.6 · `set_work_drive.py` — fresh throwaway account, and 18 sleeps converted

`check_worksheet_rate_limit` used the STANDING throwaway teacher
(`mrb331_fixture.TEACHER_EMAIL`) to deliberately exhaust the worksheet
route's 30/hour ceiling. A re-run inside the same hour inherited a
part-spent bucket and refused early (429 on call 15), a false red the
MRB-342 report named and deliberately deferred. It now mints a `BurstActor`
— a uniquely-named throwaway teacher, granted class access, torn down by its
own captured ids (never a predicate delete, matching the fixture's existing
teardown discipline) — once per run, for this one check only.

18 `time.sleep(...)` calls that sat directly before an assertion-feeding
`p.eval(...)` read, with no polling, were converted to state polls on the
condition each assertion actually depends on (reusing the existing
`wait_for` helper, plus a new `wait_stable`/quiet-window helper for
geometry-settling and negative assertions). Three of the first-pass
conversions were wrong — each the same failure shape, a poll settling in a
gap *before* an async payload actually lands — and the drive itself caught
all three on re-run; see the commit for detail.

## 3 · Proof

### 3.1 · Selection is real, not cosmetic

Computed directly against this branch's own commit (which touches the
shared `ks3_browser.py` driving harness, so most drives are legitimately
reachable):

- **27 of 28 slow gates: AFFECTED.** The one exception, `ks4_pool_drive`,
  is genuinely API-only (no `ks3_browser` import at all) — confirmed by
  reading its imports, not assumed from its name.
- A synthetic branch touching only `ks3_data/**` and one touching only
  `shared/set-work.js` were run for real against a temporary worktree —
  see §3.3.

### 3.2 · Full forced pass, and the timings

`python3 prepush_gate.py --record-all --force`, run for real from this
worktree on the machinery commit `197b1902b`, tree clean.

**Wall clock: 3419 s — 56 min 59 s.** Exit 1 (the inherited red; see below).
`--record-all` covers the 28 SLOW gates; the 22 fast gates are not receipted
and run on every `--check` regardless.

**28 slow gates: 22 PASS · 5 SKIP (precondition/credential) · 1 FAIL ·
0 SKIP-BY-RULE** (0 is correct — `--force` bypasses selection entirely).

| gate | outcome |
|---|---|
| `verify_ks3` | PASS |
| `student_parity` | PASS |
| `student_behaviour` | PASS |
| `student_themes` | PASS |
| `today_drive` | PASS |
| `import_year_drive` | PASS |
| `teacher_behaviour` | PASS |
| `teacher_reach` | PASS |
| `teacher_picker_drive` | PASS |
| `leaderboard_behaviour` | PASS |
| `ks4_pool_drive` | PASS |
| `ks4_chrome_drive` | PASS |
| `ks3_instrument_liveness` | PASS |
| `student_switches` | PASS |
| `student_controls_drive` | SKIP — neither `$MRB_DRIVE_PASSWORD` nor `$MRB_TEST_STUDENT_PASSWORD` set |
| `3d_parity` | SKIP — `3d-studio/dist` does not exist |
| `3d_render_check` | SKIP — `3d-studio/dist` does not exist |
| `seating_drive` | PASS |
| `assignments_hold_drive` | PASS |
| `consumer_flag_off` | PASS |
| `teacher_perf_budget` | SKIP — `$MRB_TEST_TEACHER_PASSWORD` not set |
| **`teacher_admin_foreign_class`** | **FAIL — the inherited red** |
| `set_work` | PASS |
| `teacher_admin_real` | PASS |
| `mrb328_import_picker` | PASS |
| `mrb328_import_picker_real` | PASS |
| `mrb328_card_prefetch` | SKIP — `$MRB_TEST_TEACHER_PASSWORD` not set |
| `student_bell_drive` | PASS |

**Nothing was red except the known inherited gate**, and its signature is
the documented one, character for character:

```
❌ teacher_admin_foreign_class_drive: 3 check(s) failed
   · C7. REMINDERS — the control is drawn on the foreign class
   · …labelled for the children who actually owe the paper
   · …and pressing it UPSERTS student_notifications
```

That is the same signature `docs/mrb335/REPORT.md` and
`docs/mrb338/REPORT.md` §11 record on `origin/main` before this branch
existed. MRB-346 does not touch `teacher_admin_foreign_class_drive.py` and
nothing here was weakened to make it pass.

**No gate needed the new one-shot retry.** Every receipt carries
`"retried": false`; the transient-retry path was exercised (see the
deviation in §5) but did not fire on the run that counts.

⚠️ **The five SKIPs are credential/precondition skips, not passes.** They are
printed by name, they write no receipt, and `--check` will keep reporting
them as SKIPPED. Three of them (`student_controls_drive`, and the two
`$MRB_TEST_TEACHER_PASSWORD` gates) are the documented precedent from
docs/mrb338/REPORT.md §11 — this run was not given a legitimate credential
for them, and guessing one would mean an authentication attempt against a
real account. The `3d_*` pair skip exactly as §4 says they should.

**Before, for comparison:** a full receipts pass under the OLD whole-tree
mechanism historically took roughly an hour end to end (docs/mrb338/REPORT.md
§11.1 records receipts at 14:45 and 15:53 on the same night) and had to be
repeated in full after any docs commit. **The new full FORCED pass measured
56 min 59 s** — i.e. roughly the same hour, which is the honest result and
the expected one: `--force` deliberately runs everything, so it cannot be
faster than running everything.

**The hour was never the thing to fix.** What MRB-346 removes is the
*repetition* of that hour. Under the old mechanism that hour had to be paid
again after every docs commit and again on every narrow branch; under the new
one it is paid once, a docs commit costs **zero** re-runs (§3.5), and a
narrow branch pays only for what it can actually reach — 23 min 37 s for the
content branch and 17 min 28 s for the Set-work branch (§3.3), against the
57 min those same branches would have cost before.

### 3.3 · Two synthetic branches, run for real

Run in a temporary worktree (`tmp/mrb346-proof-content`), one throwaway
commit at a time, `--record-all` **unforced**. The worktree, the branch and
both commits were destroyed afterwards; `origin/main` is untouched and no
`tmp/*` ref exists locally or on origin.

⚠️ **The base had to be the machinery commit, not `origin/main` — and that
is not a shortcut.** Selection only exists on this branch. A worktree
branched off `origin/main` runs the OLD `prepush_gate.py`, which has no
selection at all: the first attempt did exactly that and printed the
pre-MRB-346 `receipt written for tree 2c78259fa331`, proving nothing. It was
killed and redone with the branch based on `197b1902b`, so the tree under
test carries the machinery and the merge-base is the machinery commit —
which is precisely the world an ordinary narrow branch will be in once this
lands on `main`. The only thing supplied by hand is that base commit;
`watches`, `_affected`, the printing and the running are the real code.

**(a) Content-only — one trivial line appended to `ks3_data/biology_b1_cells.py`**

`git diff --name-only <base> HEAD` → `ks3_data/biology_b1_cells.py`, and
nothing else.

**4 ran · 19 SKIPPED BY RULE · 5 SKIP (credential/precondition) · 0 red.
Exit 0. Wall clock 1417 s — 23 min 37 s.**

```
  PASS    verify_ks3 — receipt written
  PASS    student_parity — receipt written
  SKIP-BY-RULE student_behaviour unaffected — no path this branch's commits changed is in its `watches`
  SKIP-BY-RULE today_drive    unaffected — …
  SKIP-BY-RULE teacher_behaviour unaffected — …
  SKIP-BY-RULE teacher_reach  unaffected — …
  SKIP-BY-RULE teacher_picker_drive unaffected — …
  SKIP-BY-RULE leaderboard_behaviour unaffected — …
  SKIP-BY-RULE ks4_pool_drive unaffected — …
  SKIP-BY-RULE ks4_chrome_drive unaffected — …
  PASS    ks3_instrument_liveness — receipt written
  SKIP-BY-RULE student_switches unaffected — …
  SKIP-BY-RULE seating_drive  unaffected — …
  SKIP-BY-RULE teacher_admin_foreign_class unaffected — …
  PASS    set_work — receipt written
  SKIP-BY-RULE student_bell_drive unaffected — …
```

The four that ran are the four that can actually see a KS3 question file:
`verify_ks3`, `student_parity`, `ks3_instrument_liveness`, and `set_work`
(which serves KS3 bank questions). Every teacher dashboard, leaderboard,
KS4, seating, consumer and import drive was skipped **by name, with its
reason printed** — none silently absent.

⚠️ **The 15-minute target was MISSED: 23 min 37 s, not under 15.** Stated
plainly rather than rounded toward the goal. The floor is structural —
`verify_ks3` rebuilds the whole site before it measures, and `set_work`
alone takes about 8 minutes — so no amount of selection gets a branch that
legitimately touches KS3 content under 15 minutes. It is still 23 min
against the 57 the same branch cost before. Closing the rest is a question
about those two gates' own cost, not about selection.

**(b) Set-work only — one comment appended to `shared/set-work.js`**

`git diff --name-only <base> HEAD` → `shared/set-work.js`, and nothing else.

**5 ran (4 PASS, 1 FAIL) · 18 SKIPPED BY RULE · 5 SKIP · exit 1. Wall clock
1048 s — 17 min 28 s.**

```
  SKIP-BY-RULE verify_ks3     unaffected — no path this branch's commits changed is in its `watches`
  SKIP-BY-RULE student_parity unaffected — …
  SKIP-BY-RULE today_drive    unaffected — …
  PASS    teacher_behaviour — receipt written
  PASS    teacher_reach — receipt written
  PASS    teacher_picker_drive — receipt written
  SKIP-BY-RULE leaderboard_behaviour unaffected — …
  SKIP-BY-RULE ks4_pool_drive unaffected — …
  SKIP-BY-RULE ks3_instrument_liveness unaffected — …
  FAIL    teacher_admin_foreign_class (exit 1)
  PASS    set_work — receipt written
  SKIP-BY-RULE teacher_admin_real unaffected — …
  SKIP-BY-RULE student_bell_drive unaffected — …
```

Exactly the complement of (a): the content gates that ran there are skipped
here, and the teacher/Set-work gates skipped there run here. The one FAIL is
the inherited `teacher_admin_foreign_class`, which is **correctly** selected
— `shared/set-work.js` genuinely is in its `watches`, because the sheet it
drives is the thing that changed. That is selection working, not selection
failing.

The pair is the real point: `set_work` is the only gate in both lists, and
each branch ran 4–5 of 28 slow gates instead of all 28.

### 3.4 · Repeatability — same tree, twice

`--record-all --force` run a second time immediately after §3.2's pass, on
the exact same tree (`git status --porcelain --untracked-files=no` empty
before and after), with the first run's `.gate-receipts/` copied aside for
comparison.

**Identical. All 22 `watch_hash` values byte-for-byte the same, same 22-gate
receipt set, same 22/5/1 outcome split, same single inherited red.** Zero
mismatches. Wall clock 3395 s (56 min 35 s) against the first run's 3419 s
(56 min 59 s) — a 24-second difference in runtime, and no difference at all
in what was recorded.

This is the property the whole mechanism rests on: a `watch_hash` is a
fingerprint of tracked blob shas, so it is a pure function of the committed
tree. Re-recording an unchanged tree cannot move it, and a receipt therefore
cannot "go stale" for any reason other than a watched file actually
changing.

### 3.5 · The acceptance test — a docs-only commit invalidates nothing

This very file is that commit. After §3.2's full forced pass:

1. `git add docs/mrb346/REPORT.md && git commit` (this file, filled in,
   nothing else).
2. `python3 prepush_gate.py --check` (the real, unforced push-guard path).
3. The result, measured:

**THE ACCEPTANCE TEST PASSED. All 22 slow gates that held a receipt passed
on it — zero re-ran. `--check` took 31 seconds.**

```
   20 gate(s) ran fresh, 22 passed via an unchanged receipt, 0 skipped by rule,
   7 skipped for a missing precondition.
```

Every one of the 22 printed the receipt line:

```
  PASS    verify_ks3           (receipt — watched paths unchanged)
  PASS    student_parity       (receipt — watched paths unchanged)
  PASS    teacher_behaviour    (receipt — watched paths unchanged)
  PASS    leaderboard_behaviour (receipt — watched paths unchanged)
  PASS    ks4_chrome_drive     (receipt — watched paths unchanged)
  PASS    set_work             (receipt — watched paths unchanged)
  PASS    teacher_admin_real   (receipt — watched paths unchanged)
  PASS    student_bell_drive   (receipt — watched paths unchanged)
  …22 in total
```

⚠️ **The 20 that "ran fresh" are all FAST gates, checked mechanically, not by
eye** — every name in the `running …` list was cross-referenced against
`gate_registry`'s `speed` field and **not one is slow**. Fast gates run on
every invocation by design (rule 4 of §2.4); that is the backstop, not a
re-run. So the docs commit caused **zero** slow-gate re-runs, which is rule 1
demonstrated on this branch rather than argued.

**31 seconds, against the ~57 minutes the same commit would have cost under
the old whole-tree mechanism.** That is the ticket, in one number.

4. **`--check` is nonetheless RED, and correctly so** — on
`teacher_admin_foreign_class`, and on nothing else:

```
❌ 1 GATE(S) RED:
     teacher_admin_foreign_class NEVER RUN against these watched paths — no receipt.
   PUSH REFUSED. 1 of them carry no override.
```

Worth being precise about why, because "no receipt" and "failed" are
different states and the guard says the first:

- it FAILED in §3.2, and a failing gate's stale receipt is deleted rather
  than kept, so it holds no receipt at all;
- it is genuinely AFFECTED by this branch — `ks3_browser.py` is in its
  `watches` and this branch changed `ks3_browser.py`, confirmed by
  computing the intersection rather than assuming it;
- so selection cannot excuse it, and the guard refuses the push.

This is the machinery behaving exactly as §2.4 says it must: **selection
only ever widens what runs on top of an already-red gate; it never makes a
red gate look green.** The branch therefore ships with an explicit
`GATE-OVERRIDE:` line in the tip commit naming this gate, which is the same
override this inherited red has required on every full run since MRB-335 —
not a new concession, and not a weakening of the gate.

⚠️ Note the asymmetry worth keeping: in §3.3(a) the *content* branch skipped
this gate BY RULE and pushed green, because a KS3 question file cannot reach
a teacher-admin drive. Only a branch that genuinely touches its watched
paths — like this one — inherits the red.

### 3.6 · `set_work_drive.py` — five consecutive runs, identical

Already run and recorded before this file existed (see the commit):
5 consecutive runs, `392 checks, 0 failed` every time, the worksheet
rate-limit burst refusing at call 31 (the route's real ceiling of 30) in
every run — never call 15, which was the pre-fix false-red signature.
Zero leftover burst accounts on TEST after any run.

## 4 · What did NOT change

No gate's assertions were weakened. `watches` changes which gates run and
what invalidates a receipt, never what a gate checks once it runs. The
inherited red `teacher_admin_foreign_class` (C7 REMINDERS × 3) is untouched
and — because this branch's changes to `ks3_browser.py` genuinely reach
it — was selected and re-confirmed red in §3.2, exactly as it was on
`origin/main` before this ticket (docs/mrb335/REPORT.md, docs/mrb338/REPORT.md
§11 both record the identical signature). `3d_*` gates still skip cleanly
without `3d-studio/dist`.

## 5 · Deviations

1. **CLAUDE.md had no pre-existing dedicated "receipts" section to rewrite
   in ⊕ style** — only one incidental, still-accurate mention under "How the
   Site is Generated". A new section was added instead
   (`## Gate machinery — the pre-push guard`), which says so explicitly
   rather than fabricating a ⊕-superseded quote for text that never existed.
2. **The first full forced pass was invalid, and the cause was the
   verification's own credentials — not the branch.** It was run with
   `MRB_THROWAWAY_PASSWORD` and `MRB_TEST_TEACHER_PASSWORD` set to arbitrary
   throwaway strings, on the assumption that these variables *set* a
   throwaway account. They do not: they are the passwords of accounts
   already provisioned on TEST, and the correct value for the first is the
   documented `mrb326-throwaway`. Five gates went red — `teacher_admin_real`,
   `mrb328_import_picker_real`, `student_bell_drive` on an explicit
   `invalid_credentials`, and `teacher_perf_budget` and
   `mrb328_card_prefetch` on an unhandled `HTTPError 400` that is the same
   sign-in failure with worse manners. None was a regression; all five are
   wrong-password reds.

   Two things are worth keeping from it. First, `mrb331_fixture.py` lines
   120–122 already warn about exactly this trap — *"set_work went green on
   any value and teacher_admin_real answered a bare sign-in FAILED with
   nothing pointing at the password"* — and that is precisely what happened
   again: `set_work` passed on the junk value because it provisions its own
   actor, while its neighbours failed opaquely. Second, the transient-retry
   path fired on the two `HTTPError 400` gates and correctly refused to
   rescue them: retried once, still red, counted as red. A retry that had
   swallowed a wrong-password failure would have been a far worse outcome
   than the false red.

   Fixed by setting `MRB_THROWAWAY_PASSWORD=mrb326-throwaway` and **leaving
   `MRB_TEST_TEACHER_PASSWORD` unset**. The latter is the MRB-293 fixture
   password, set by SQL, with no literal fallback in the tree; guessing it
   would have produced another wrong-password red, so the honest outcome is
   the documented clean SKIP the gate itself prescribes. §3.2 is the corrected
   run. The invalid run's numbers are not reported as results anywhere.

3. **The §3.3 synthetic branches could not be based on `origin/main`.**
   The plan called for a temp worktree off `origin/main`; selection does not
   exist there, so the first attempt silently ran the pre-MRB-346 code and
   demonstrated nothing. Re-based on the machinery commit — see the ⚠️ note
   in §3.3 for what that does and does not change.

4. **The content branch missed the 15-minute target at 23 min 37 s.**
   Recorded as a miss in §3.3 rather than softened. The cause is the cost of
   `verify_ks3` and `set_work` themselves, which selection cannot reduce.

5. **A harness note, not a product finding.** The wait-loops used to poll for
   these runs matched their own `pgrep -f` pattern and so never exited —
   the same self-matching trap `docs`' concurrency notes record. It cost
   wall-clock time only; no run or measurement was affected.
