# MRB-328 — round three

Four jobs, one same-day run, all four landed. Two commits: `ffbd1a756` (J1)
and `f66c920d9` (J2/J3/J4).

---

## J1 · BMT's lesson becomes BRB's

**Done, on production, verified.**

The sheet gives BMT exactly one teaching cell — `8r/Sc3`, **Wednesday P4** —
and BMT holds no timetable at all, because no `pending_staff` row carries the
code. Under your ruling it is now BRB's. He already taught that class twice;
the sheet's own class-summary row reads `8r/Sc3 | BRB | BMT | BRB`, so all
three of its lessons now sit with one teacher.

One row, `source='manual'` rather than `'seeded'` — `seeded` means "came from
the sheet's staffing", and this row deliberately did not. It is the single
entry on the platform with no counterpart in the sheet's columns.

**The slot-guard was proved live, not assumed.** An insert passing is not by
itself evidence anything checked it. A second insert into the same slot was
attempted inside a `DO` block trapping `23505`: refused, caught, and the live
count at Wed P4 stayed at **1**.

**Verification: zero rows, all 13 teachers.** `verify_timetable_sheet.py`
emits one statement that set-differences sheet against platform server-side,
so the comparison never depends on transcribing 200 rows by hand. Nothing on
the sheet is missing from the platform; nothing on the platform is absent from
the sheet; BRB's Wed P4 is accounted for as a ruled addition rather than a
surplus.

### Two traps it walked into first

**Resolving a staff code to an owner needs both directions.** An entry is
owned either by a `pending_staff` row (unclaimed) or by a `profile` (claimed,
since MRB-293). Joining one way silently drops every claimed teacher.

**And both directions still miss BDA.** He was a real profile before the
pending-staff seeding ever ran, so no `pending_staff` row carries his code.
The first run reported **21 missing lessons** — the whole of one teacher's
timetable — when nothing whatever was wrong. The query now maps "owned by a
profile no `pending_staff` row claims" to BDA and carries a guard that reports
a row if a second such owner appears, since the mapping would then quietly
pool two teachers under one code.

That guard reports rather than raises. The first draft used `1/0`, which
Postgres constant-folds at **plan** time — so it fired on every run, healthy
ones included. A guard that always cries wolf is no better than one that
sleeps.

---

## J2 · Import picker, whole-school for admins

**Done.** The chip was derived from the uploaded CSV, so before a file existed
it read "Not chosen yet" and an admin arriving from a colleague's class had
nowhere to go. It is now a real selector in the same pill: whole-school for a
school admin grouped Year 7 → 11, own classes for a plain teacher.

**A foreign preselect is refused by construction.** The list is role-scoped,
so a foreign id is simply not in it — no throw, no silent select, and no
second permission test that a later change could forget to run.

The confirm step names the class and its teachers —
`IMPORTING INTO [HZ 10A Science ▾] · Amy Barlow, Ben Hough` — and adds no
explanatory sentence about one roster serving them all. The names carry it.

With no class chosen, behaviour is byte-for-byte as before, multi-class file
included.

**The fixture gap is closed with a real import.** An admin opens a colleague's
class → Import → preselected → completes a synthetic import on TEST → the
students are read back **as members of that class and of no other**, with no
second class of that name created, and the run leaves nothing behind.

### A ruling inside J2, for your eye

A chosen class already exists, and `roster-import` ignores every field of a
found class except its name. So it is not asked for its course, and its
teacher defaults to **nobody** — an admin importing into a colleague's class
is not becoming its teacher. Asking again for something the import cannot
write is the redundancy the fidelity protocol forbids.

That made a pre-existing dash newly reachable: the review table rendered
`— · —` under COURSE, which reads as *"we do not know this class"* when the
truth is *"this import does not touch it"*. MRB-326 already ruled the answer —
drop an unknown rather than dashing it — so `courseLabel` now drops.

---

## J3 · Admin teacher view

**Done.** Each staff row on `admin.html` opens that teacher's classes as the
My-classes grid, scoped to them, with their name as the page context: live
links for a claimed teacher, pending assignments rendered as cards for an
unclaimed one, an honest "No classes" for one with none.

**The grid is reused, not rebuilt.** The only thing that changed is where the
class ids come from, so Design's card builder and everything below it — the
KS filter, the sort, the year strip — is untouched. Cards open class detail
acting-as-admin through the existing ruling, so the marker comes free.

No new copy: the pending eyebrow reuses `admin.html`'s own "NOT YET SIGNED
IN", the empty state is Design's own panel.

**Fixed in passing:** the card line read "**1 classes** · 4 students".
Unreachable for Design's twelve-class sample teacher, and hit every single
time an admin opens a one-class colleague.

A non-admin passing the param gets her own classes — never an error, never a
colleague's list.

---

## J4 · Performance

### (a) The beacon

`rum_timings` is one row per page load and is deliberately blind:

- **No URL, ever.** Ours carry `?class=<uuid>` and `?student=<uuid>`; storing
  one would quietly rebuild a per-child browsing log out of columns that each
  look harmless. `page` is a coarse screen name off a fixed list.
- **No free text.** Fetch labels are table names taken from the REST path with
  the query string discarded *first*, re-checked against a slug pattern.
- **No names.**

All of it is enforced in Postgres — whitelists plus a slug-checked JSONB shape
— rather than by trusting the JavaScript, which anyone can edit in a console
and post as themselves. Verified on both projects: `"classes"` accepted,
`"Jamie Smith"` refused.

RLS rehearsed on TEST across seven cases: insert-as-self allowed,
insert-as-another refused, plain teacher reads nothing, own-school admin reads,
**other-school admin reads zero**, delete affects nothing, and the shape check
reaches an authenticated writer too.

**A correction worth recording.** The first cut had the client send
`school_id`. It is usually absent from the JWT, so rows would have arrived
with a null school — and the admin read policy requires it non-null. The table
would have filled with rows **no admin could ever read**, and nothing would
have looked broken until someone finally asked for the numbers and got an
empty result. That is precisely the failure this ticket exists to stop having.
It is now derived by a trigger, which also stops a client asserting its own
school.

**A false green, caught.** The first RLS probe "passed" several cases because
the *probe table's* own RLS was rejecting the recording — not because
`rum_timings` refused anything. Redone with every recording after `reset role`.

### (b) The cheap wins

- **Cross-page cache** for the own-classes list and session/role, on
  `class-entry.js`'s existing machinery rather than a second one. It does not
  skip the read: the point is to let the *second* read start early, since
  `loadClassMatrices` used to sit idle a whole round trip waiting to be told
  which ids to ask for. **The fresh list always wins**, so a stale entry costs
  one extra read and can never put a stale class on a teacher's screen.
  Invalidated on sign-out and on roster import.
- **Scoped views cannot poison it**, structurally rather than by a flag: the
  scoped branch never calls `loadTeacherClasses` at all, and that function
  derives the viewer's id from the session, so it can only ever cache the
  viewer's own list.
- **Hover/touchstart prefetch** on class cards — once per card however many
  times the pointer crosses its descendants, for the URL that card's own
  handler would open, and **never on a colleague's list**.
- **`_headers`.** There was none, so `/shared/*` sat on Cloudflare's four-hour
  revalidate default — a class set of 30 Chromebooks paying 30 conditional
  requests for bytes that had not changed. `immutable` is safe only because
  every published reference is `?v=` stamped, and that was **checked, not
  assumed**: 10,328 stamped references, **zero** unstamped in any published
  HTML (the 18 unstamped strings in the repo are all inside JS comments). I
  deliberately left out a `/*` HTML rule — it also matches `/shared/*`, and if
  the later rule wins it would silently undo the whole file.

### (c) The numbers, honestly

`teacher_perf_budget` stays **green**, all four journeys, throughout.

Baseline is post-J2/J3 and pre-J4(b), so the comparison isolates the perf work.

| journey | before | after (3 samples) |
|---|---|---|
| landing · today.html | **843** (843/479/1004) | **231, 187, 371** |
| Today → class detail | **1703** (1703/884/3211) | 1611, 670, 1279 |
| class detail → marking | **536** (730/521/536) | 673, 363, 567 |
| class detail → student | **571** (536/571/674) | 1442, 389, 668 |

**Only the landing journey is a claim I will make.** Its before-runs spanned
479–1004 ms and its after-runs, across three separate samples, spanned
180–392 ms — non-overlapping. That is the page a teacher opens first, and the
one the session/role caching helps most.

**The other three are inside the noise, and I am not calling them wins.** This
environment is very noisy: one journey varied 537 → 3057 ms *within a single
sample*. The first after-sample looked like a serious regression on
`class detail → student` (571 → 1442, non-overlapping ranges); re-sampling put
it at 389 ms. Two more samples were taken precisely because one would have
supported whichever story I wanted.

One limitation stated plainly: there is **one** before-sample, because the
before state no longer exists in the tree. A stronger comparison would have
needed a revert-and-rebuild, and would still be a laptop on home broadband.

### The beacon was proved to actually fire, and it found its own bug

A beacon that is silent on failure by design is exactly the thing that can be
dead on arrival with nobody the wiser — and the "browse ten pages" ask would
then have cost a round trip and returned nothing. So it was driven end-to-end
on TEST rather than assumed: **46 rows across all four teacher page types**,
`school_id` filled by the trigger on every one, fetch labels coming through as
clean table names (`class_teachers`, `profiles`, `staff_scopes`,
`timetable_entries`, `assignment_submissions`) — no URLs, no names.

The first run of that test found a real defect. Every ported screen carried a
`build`; **`teacher-today` carried NULL**. `__MRB_ASSET_V__` is published by
the ported runtime, and the hand-written pages do not have it — so the landing
page, the one most worth attributing to a deploy, was the one page whose rows
could not be. Fixed by reading the stamp off the document's own tags.

The first fix then had its own flaw: taking the first stamped tag made
today.html report `tokens.css`'s hash while the ported screens reported
`config.js`'s, so `build` was per-page and could not be grouped on. It now
picks `config.js` by name. Re-driven: **one value, `d1fecb43`, across all four
pages, 46 rows, zero nulls.**

**Which is the point.** ⚠️ **PROD truth arrives via the beacon, and there are
no prod rows yet** — the table went live with this push and nothing has
browsed. So, the one-line ask:

> **Browse ten pages on the live site — a few teacher screens, a couple of
> student ones — and the next run reads the truth instead of a laptop's guess.**

---

## Deviations

1. **J2, J3 and J4 are one commit, not three.** One unit is one commit, but
   three lanes worked one checkout and their built output interleaved;
   splitting afterwards would have produced commits whose `mrbadmus_site/`
   did not match their own source. J1 is separate, as it was independent.
2. **The prod migration was applied outside a merge.** The rule allows it when
   you rule the migration in the prompt, which J4(a) does, and the prompt
   anticipates prod rows appearing mid-run — impossible unless the table is
   live. Rehearsed on TEST first regardless.
3. **The MCP swap dance was not performed.** It could not be, in a
   non-interactive session. The confusion it guards against is structurally
   absent here: the production tool requires the project ref typed explicitly
   on every call, and the TEST tool cannot reach production at all.
4. **Migration version drift, reconciled.** TEST recorded two versions (it was
   built in two passes); production recorded one. The local file is named for
   production's, per MRB-326. The schemas are identical; a version-by-version
   diff of the two projects will show the difference, and that is expected.
5. **I set a password on the TEST throwaway admin** (`f3260000-…-0002`) so the
   half of `mrb328_card_prefetch_drive` that had been SKIPPING could actually
   run. It was skipping the leak-adjacent case — an admin on a colleague's
   list — which is the one most worth proving. It now passes.
6. **13 lane worktrees are on this machine and disk is at 97%.** Pruning them
   is your call, not this ticket's; several hold unmerged work.

### ⚠️ The perf gate is flaky in this environment

`Today → class detail` measured, across eight samples: 406, 462, 670, 1279,
1286, 1611, 1703, **2952** ms. One run of it went red — a single 6124 ms stall
dragged the median-of-3 over the 2500 ms budget — and two immediate re-runs
came back at 462 and 1286 ms.

It is not weakened and the budget is not moved. But a median of three is not
robust against a tail like that, and anyone reading a single red run of this
gate should re-run before believing it. This is a further argument for the
beacon: real rows in volume do not have this problem.

## Findings not acted on

- **`import_year_drive.py`'s `run_case` docstring is wrong.** It claims "A
  FRESH PAGE TARGET each time"; `cdp.Browser.page()` is `attach().goto()` —
  one target per browser — so injected scripts *accumulate*. It survives only
  because `hold()` is `configurable: true` and later scripts win. A one-line
  correction, in its own unit.
- **A fixture-name coincidence.** The TEST fixture surnames "Spedding" and
  "Barlow" each match a real staff surname on production, and `SPD` is a real
  code. **No full name matches** — checked against every fixture name visible
  in the committed screenshots — so this is coincidence, not a leak, and it
  predates this run. Worth knowing, not worth renaming mid-ticket.
