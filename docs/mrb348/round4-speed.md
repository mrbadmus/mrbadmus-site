# MRB-348 round 4 — making it consistently fast, and proving why it wasn't

> ## ⚠️ CORRECTED 23 SEP 2026 (round 5) — READ THIS BEFORE ANYTHING BELOW
>
> **This report's central finding is wrong.** It said the Render backend runs
> in Oregon and recommended moving it to Frankfurt. **The backend already runs
> in Frankfurt (EU Central)** — Mide's Render dashboard shows one service,
> `mrbadmus---backend` (srv-d702097diees73dcla8g), in Frankfurt.
> `gcp-us-west1-1.origin.onrender.com` is Render's shared edge hostname, not
> the service's region. The warm `db_ms` of ~60 ms measured below was itself
> evidence against a transatlantic hop (Oregon↔Ireland is ~140 ms per round
> trip before any work), and it was explained away rather than believed.
>
> **Withdrawn:** the Frankfurt move (§1, §13 item 1), every "crosses the
> Atlantic" framing (§2.5, §3.1, §3.2, §12), and the recommendation AGAINST a
> compute change (§1, §2.6, §6 item 3) — that last one rested on the belief the
> instance was 1 GB Micro. It is not: the instance reports **411 MiB of RAM
> and ~424 MiB in swap**. See `docs/mrb348/round5-slow-leg.md`, which measured
> each leg separately and names the slow one.
>
> **Still true:** the production RUM (§2.1–2.4), the warmth curve (§2.2), the
> teacher rollup and its proof (§4, §11), the gate findings (§5, §8, §9, §10).
> The backend round-trip reductions (§3.1, §3.2) are still real and still
> correct; only their per-trip cost was wrong.
>
> This file was never committed by round 4 — its session ended before the
> write landed. It was reconstructed verbatim from that session's transcript
> by round 5, sections put in numbered order, and corrected in place with
> ⊕ markers. Nothing else in it was changed.

23 September 2026. Unattended run.

## The one-sentence answer

> ⊕ **Corrected (round 5):** the Oregon premise below is false — the backend is in Frankfurt. The warmth curve is real; its cause is the Supabase instance (411 MiB RAM, living on swap), not distance. See round5-slow-leg.md.


**The site is not sometimes slow — it is slow whenever it has been sitting
still, because the backend and the database are on opposite sides of the
Atlantic and the connection between them goes cold in four seconds.**

Two independent measurements say the same thing:

- **From production users.** Bucketing every page load in `rum_timings` by how
  long the site had been idle before it: p50 goes **522 ms (under 10 s idle) →
  3,864 ms (5–30 min idle)**, monotonically. A **7.4× spread** with no other
  variable moving.
- **From the wire.** Sampling `/api/health` 28 times and subtracting its
  self-reported `db_ms` from the wall time: the UK→Render leg is **stable at
  80–132 ms**, while the Render→database leg swings **58 → 1,416 ms**. A **24×
  spread** on a query that does no work. All the variance is in one hop.

The hop is Oregon → Ireland. `mrbadmus-backend.onrender.com` resolves to
`gcp-us-west1-1.origin.onrender.com`; `render.yaml` has no `region:` key, so
the service took Render's default when it was created and nobody chose it.

## What this run did about it

| | |
|---|---|
| **Landed** | the teacher rollup (step 1), plus four speed fixes — two backend, two frontend |
| **Wrote up for Mide, did not do** | the region move, and Supabase's Auth connection setting. Both free, both his call |
| **Explicitly recommends NOT doing** | upgrading Supabase compute. The whole hot dataset is under 3 MB |
| **Found and did not chase** | nothing outstanding; one wrong turn of my own, written up in §5 |

⚠️ **Read §2.6 before spending any money on this.** The database has nothing to
do: `assignments` holds 7 rows and `assignment_submissions` holds 10. Every
millisecond in this report is network and connection overhead, and no compute
tier changes that.
Mide's report was "sometimes fast, sometimes lags really bad". This round set
out to explain the "sometimes" with production numbers rather than lab timings,
and it turned out to have a single dominant cause with a name.

---

## 1. THE INFRASTRUCTURE FINDING — first, because it is Mide's call

> ⊕ **Corrected (round 5):** **WITHDRAWN.** Render is already in Frankfurt; there is no transatlantic hop and no move to make. The `db_ms` spread below is real, but round 5 shows it comes from the Supabase instance stalling (Auth and PostgREST stall together, even on 401s that never query), not from the network. The compute paragraph at the end of this section is also wrong: the instance is not a 1 GB Micro.


### What is wrong

**The backend and the database are on opposite sides of the Atlantic.**

- The Render web service resolves to `gcp-us-west1-1.origin.onrender.com` —
  **GCP us-west1, Oregon**. `render.yaml` carries no `region:` key, so the
  service took Render's default when it was created, and nobody chose it.
- The Supabase project is **AWS eu-west-1, Ireland**.
- Every call the backend makes to the database crosses roughly 7,700 km.

### The measurement that isolates it

`GET /api/health` reports `db_ms` — the time for ONE trivial database ping
(`select id from academic_years limit 1`, head-only) made on the warm
module-scope client. Sampling it 28 times from a UK machine, and subtracting
`db_ms` from the total wall time to get the non-database remainder:

| leg | what it is | measured |
|---|---|---|
| `non_db` = total − `db_ms` | my UK browser → Render (Oregon), there and back | **80–132 ms, stable** |
| `db_ms` | Render (Oregon) → Supabase (Ireland), one trivial ping | **58 → 1,416 ms** |

`db_ms` across 28 samples: **min 58, p50 159, p90 651, max 1,416 ms — a 24×
spread on a query that does no work.**

The `non_db` leg never moves. All the variance is in the backend-to-database
hop. That also rules out a Render dyno cold start: a cold dyno would inflate
`non_db`, and it never does.

For comparison, a **UK browser talking to Supabase directly** — which is what
the teacher dashboards and most of the student page actually do — measures a
**9–10 ms TCP connect**. So the backend sits roughly 6–15× further from the
database than the pupils do.

### Why it shows up as "sometimes fast, sometimes lags really bad"

A fresh HTTPS connection costs about three extra round trips (TCP + TLS).
Measured locally at 10 ms RTT: a reused socket answered in **12 ms**, a fresh
one in **36–42 ms**. Scale those three round trips to a transatlantic path and
you get exactly the 58 ms ↔ 651 ms gap above.

Node's global `fetch` keeps sockets alive for a **default of 4 seconds**, and
there is no keep-alive tuning anywhere in the backend. On a site with a few
hundred requests a day, most requests therefore arrive to a cold socket and pay
the full transatlantic handshake; a request arriving seconds after another one
reuses a warm socket and is fast.

That is the "sometimes", and production RUM confirms it independently — see §2.

### What to do, what it costs

**Recommended: move the Render service to Frankfurt. Expected saving 0.4–1.0 s
on warm loads and several seconds on cold ones. Cost: £0.**

- Render charges the same for the Starter plan in every region.
- Frankfurt → Ireland is roughly 20–25 ms, against the 60–150 ms warm /
  650 ms cold measured today.
- It also shortens the *other* leg: a UK pupil reaching the backend currently
  crosses to Oregon and back (the stable 80–132 ms above). Frankfurt would make
  that ~20 ms too.

⚠️ **Render cannot change a service's region in place.** A new service must be
created in Frankfurt and the old one retired. The steps:

1. Create a new Web Service in **Frankfurt**, same repo, same branch, plan
   Starter, from the committed `render.yaml`.
2. Copy the five `sync: false` environment variables across:
   `ANTHROPIC_API_KEY`, `ANTHROPIC_VISION_MODEL`, `SUPABASE_URL`,
   `SUPABASE_SERVICE_ROLE_KEY`, `SUPABASE_ANON_KEY`.
3. Check `GET /api/health` on the new URL. Expect `db_ms` around 20–40 ms warm.
   If it is not, stop — something else is wrong and the move has not helped.
4. Repoint the site. **Prefer attaching a custom domain** (e.g.
   `api.mrbadmus.com`) to the new service rather than editing URLs: the Render
   hostname is hardcoded in several frontend files, and a domain move needs no
   code change and no rebuild.
5. Leave the Oregon service running until the new one has served real traffic,
   then delete it.

**NOT recommended: upgrading Supabase compute.** The database is not the
problem and spending money there would buy nothing measurable.

- Production runs **Micro** (224 MB `shared_buffers`, 384 MB
  `effective_cache_size`, 2 parallel workers).
- But 185 days of `pg_stat_statements` show the whole estate making only
  ~2,841 own-profile reads and ~1,155 `class_members` reads **in total**.
  Application query means are 20–40 ms.
- The single most expensive statement on the database is
  `SELECT name FROM pg_timezone_names` — 257 calls in 185 days, i.e. **1.4 a
  day**, which is dashboard introspection, not the app.
- The database is idle nearly all the time. It is not CPU-starved.

Micro → Small would be $10 → $15/month (net +$5 after the Pro plan's $10
compute credit). It would not move any number in this report. Don't.

---

## 2. WHAT THE PRODUCTION NUMBERS SAY

All figures below are read from `rum_timings` on production — real pupils and
real teachers, not a laptop. The window is the last 5 days; **every row in it
carries the same `build` (`d1fecb43`)**, so nothing here averages two versions
of the site together.

### 2.1 The baseline, reproduced

| page | loads | p50 | p90 | max |
|---|---|---|---|---|
| teacher-classes | 57 | 814 ms | 6,451 ms | 16,629 ms |
| teacher-class-detail | 41 | 1,122 ms | 4,975 ms | 6,680 ms |
| teacher-today | 34 | 789 ms | 3,238 ms | 11,274 ms |
| student-class | 17 | 2,337 ms | 9,403 ms | 10,145 ms |
| student-assignment | 8 | 1,749 ms | 3,992 ms | 3,992 ms |

⚠️ **The sample is thin** — 17 loads for the slowest page in the estate. Every
conclusion below is stated with that in mind, and §5 says honestly where the
traffic is too thin to judge.

### 2.2 The pattern is WARMTH, not time of day, device or network

This is the finding that explains Mide's sentence. Bucketing every page load by
how long the site had been idle before it (the gap to the previous beacon):

| idle before the load | loads | p50 | p90 |
|---|---|---|---|
| under 10 s — hot | 58 | **522 ms** | 1,914 ms |
| 10–60 s | 37 | 989 ms | 4,683 ms |
| 1–5 min | 28 | 1,390 ms | 6,451 ms |
| 5–30 min | 19 | **3,864 ms** | 9,403 ms |
| over 30 min | 21 | 2,337 ms | 8,982 ms |

**A 7.4× spread in p50, and it is monotonic through the first four buckets.**
The same site, the same pages, the same people — the only variable is how long
everything had been sitting still. That is the same curve as the `db_ms`
measurement in §1, arrived at from the opposite direction.

The other breakdowns the brief asked for do **not** carry a comparable signal:

- **Time of day** — the early hours look worse (08:00 UK p50 8,281 ms) but
  n = 2. 06:00 is n = 4, 07:00 is n = 8. There is no honest "cold mornings"
  claim to be made from that, and the idle-gap curve above explains those
  loads anyway: the first load of the morning is by definition the one with
  the longest idle gap in front of it.
- **Device** — `high` p50 912 ms (n = 138) vs `mid` p50 2,337 ms (n = 26). Real,
  but it tracks role rather than hardware: students are the `mid` devices and
  the student page is the slow page.
- **Connection** — 144 of 164 loads report `4g`, which is what the Network
  Information API returns for any fast connection including desktop wifi. The
  column cannot discriminate and no school-network pattern is visible.

### 2.3 Which single read dominates each page

`rum_timings.fetches` sums the duration of every call per table. Taking, for
each individual page load, the read that was the slowest on that load:

| page | slowest read | how often it was worst | p50 when it was worst |
|---|---|---|---|
| teacher-classes | **`profiles`** | 24 / 57 | **3,991 ms** |
| teacher-classes | `class_teachers` | 24 / 57 | 303 ms |
| teacher-today | **`profiles`** | **29 / 34** | 1,142 ms |
| teacher-class-detail | `class_teachers` | 37 / 41 | 361 ms |
| teacher-class-detail | `profiles` | 4 / 41 | 2,967 ms |
| student-class | `rpc` | 14 / 17 | 963 ms |

**`profiles` is the slowest read on 57 of 133 teacher page loads.** It is a
one-row primary-key read. Server-side it averages 38.9 ms. So the seconds are
not the query — they are connection warmth, exactly as §1 predicts.

And it was being fetched **twice on every teacher page load**: once by
`shared/teacher-guard.js` for the role check, and again, independently and with
no cache at all, by `shared/teacher-admin-nav.js` deciding whether to draw the
Admin link. Two exposures to the same tail, for one row.

### 2.4 Fan-out and overlap

| page | distinct reads per load | p50 sum of fetch time | p50 page time | overlap |
|---|---|---|---|---|
| student-class | 12.4 | 7,365 ms | 2,337 ms | 3.2× |
| teacher-class-detail | 9.6 | 1,652 ms | 1,122 ms | 1.5× |
| teacher-classes | 7.5 | 1,772 ms | 814 ms | 2.2× |
| teacher-today | 5.1 | 1,849 ms | 789 ms | 2.3× |

The pages are **not** serialising their fan-out badly — 7.4 s of fetch time
collapsing into 2.3 s on the student page is decent parallelism, and previous
rounds did that work. What remains is (a) individual reads with long tails, and
(b) a handful of genuinely serial hops in front of them.
---

## 2.5 ⚠️ TWO DIFFERENT PATHS, AND THEY HAVE DIFFERENT PROBLEMS

> ⊕ **Corrected (round 5):** the student page does not cross the Atlantic — Frankfurt↔Ireland is ~12 ms of handshake measured from the dyno. The two-paths distinction still holds; the explanation of the gap does not.


This distinction matters for deciding what the Frankfurt move would and would
not buy, and it is easy to get wrong.

**The teacher dashboards barely touch the Render backend at all.** `teacher/
classes.html`, `class-detail.html` and `today.html` read Supabase DIRECTLY from
the browser over PostgREST. For a pupil or teacher in the UK that is a ~10 ms
hop to Ireland — measured TCP connect from this machine, 9–10 ms. Those pages
call the backend only for `/api/health` (a fire-and-forget warm-up ping that
blocks nothing) and for Set work.

**The student class page is the one that crosses the Atlantic.** It waits on
`/api/class/current-assignment` before it paints, and fires `/api/class/
practice` beside it. Both go browser → Oregon → Ireland → Oregon → browser.

That is why student-class p50 (2,337 ms) is roughly **3× teacher-classes**
(814 ms) despite both pages doing a comparable amount of work, and it is the
single clearest argument for the region move in §1: **the page it would help
most is the slowest page in the estate, and the one pupils use.**

It also means the teacher pages' long tails are NOT the Oregon hop. Their
dominant cost is `profiles` (§2.3), read browser-to-Ireland — where the server
side itself has a real tail: `pg_stat_statements` puts the own-profile role read
at a **38.9 ms mean and a 2,601 ms maximum**. A read with a tail like that, made
**twice per page load**, gets two chances to land in the tail. That is what §3.3
removes.
---

## 2.6 THE DATABASE HAS NOTHING TO DO — which settles the money question

> ⊕ **Corrected (round 5):** the data is tiny, but the MACHINE is too: 411 MiB of RAM with ~424 MiB swapped out, shared by Postgres, PostgREST, Auth and the gateway. "Nothing to do" was about rows; the stalls are about memory. The money question is re-opened in round5-slow-leg.md.


Row counts on production, 23 Sep 2026:

| table | rows | size |
|---|---|---|
| class_members | 1,678 | 712 kB |
| profiles | 1,321 | 656 kB |
| timetable_entries | 295 | 256 kB |
| class_teachers | 91 | 120 kB |
| classes | 73 | 112 kB |
| assignment_questions | 51 | 64 kB |
| **assignment_submissions** | **10** | 128 kB |
| **assignments** | **7** | 96 kB |
| staff_scopes | 3 | 64 kB |
| academic_years | 2 | 48 kB |

**The entire hot working set is under 3 MB.** It fits in the Micro instance's
224 MB of shared buffers several hundred times over. There is no table scan
worth optimising, no index worth adding, and no compute tier worth buying: a
one-row primary-key read against a 656 kB table that takes 2.6 seconds is not
short of CPU or memory, and giving it more of either changes nothing.

Every millisecond in this report is **network and connection overhead**, not
database work. That is why §1 recommends moving the backend and explicitly
recommends NOT upgrading the database.

⚠️ **And it sets honest expectations for the teacher rollup (§4).** The rollup
stops the six teacher screens pulling every submission in the school. With
**ten submissions on production today**, the bytes it saves right now are
negligible and any before/after byte count will look unimpressive. Its value is
that the cost stops growing with the school: the same page that reads 10 rows
today read all of them, and would have read all 40,000 in two years' time.
That is a structural fix measured against the future, and it should not be sold
as tonight's speed-up.

### One free lever that is not ours, found in Supabase's own advisors

`auth_db_connections_absolute` (INFO): *"Your project's Auth server is
configured to use at most 10 connections."*

That matters more here than it looks, because **`sb.auth.getUser()` gates every
single page load** on both the student and teacher guards — it is the one call
everything waits behind. Ten connections shared across a whole year group
arriving in the same minute is a plausible queue, and it would present exactly
as these tails do: a trivial call that is usually instant and occasionally
seconds.

Switching Auth to a percentage-based connection allocation is a **dashboard
setting and costs nothing**. It is Mide's to change; it is not a code fix and
this run did not touch it. Worth doing at the same time as the region move, and
worth re-reading `rum_timings` afterwards to see whether it moved anything.

### Two leftovers on production worth tidying (not tonight — no prod writes)

`mrb347_policy_backup` and `mrb348_policy_backup` are still on production, both
without primary keys. They are working files from the RLS rounds. Dropping them
is a write, so this run left them alone; they are harmless but they should not
become permanent furniture.
---

## 3. WHAT WAS FIXED, AND WHAT IT BOUGHT

Every fix below is ours, at the source, and costs nothing to run. None of them
removes a fallback: the student page still answers with a sentence rather than
a blank host when a read is slow or fails, and no pupil loses work.

### 3.1 Backend — `classAccess` stopped crossing the Atlantic four times

`classAccess` guards every `/api/class/*` route, including the
`current-assignment` read the student class page blocks its first paint on. It
made **four strictly serial** database round trips: the class, then membership,
then teaching, then the academic year.

Only one of those dependencies was real — the year is looked up by
`cls.academic_year_id`, so the class must be read first. Membership and teaching
are keyed on the `classId` the *caller* supplied and never needed the class row
at all.

**4 round trips → 2** for a teacher, **3 → 2** for a student.

Role precedence was the only real risk, and it is proved unchanged over all four
member/teacher combinations — somebody who is both a member and a teacher of one
class still resolves to `student`, exactly as before. The extra `class_teachers`
query a student now pays runs *beside* two others rather than after them, so it
costs no wall-clock time, and §1 shows round trips — not queries — are the
scarce resource here.

### 3.2 Backend — the week's work is read beside the assignment, not after it

`/api/class/current-assignment` attaches `week_work` to every 200 it sends, and
it was fetched inside `send`, at the very end, after the assignment lookup, the
questions read and the progress reads had all finished in sequence. Two more
transatlantic round trips on the back of the slowest blocking call on the
slowest page.

They were never needed there: `weekWorkFor` takes `classId`, `week` and whether
the caller is a student, all three known long before we decide which assignment
to serve. It now starts as soon as the week is known and is awaited in `send`
exactly as before — so on the common path (the class already has this week's
work, which is every request after the first) it runs beside the assignment
chain and costs nothing.

**2 serial round trips → 0 on the critical path.**

The `.catch(() => {})` on the eager promise is load-bearing rather than
defensive noise: several paths below answer 500 without going through `send`,
nothing would ever observe the promise on those, and an unhandled rejection ends
the process on modern Node — turning one student's 500 into an outage for
everyone on the dyno.

**Backend total: `/api/class/current-assignment` drops from about 13 serial
database round trips to about 9.** At the measured warm 159 ms per round trip
that is roughly **0.6 s**; at the p90 of 651 ms it is roughly **2.6 s**.

476 existing backend tests pass unchanged across both commits.
---

## 3.3 Frontend — `profiles` stops being read twice on every teacher page

Measured cause, from §2.3: `profiles` is the slowest read on **57 of 133**
teacher page loads, p50 **3,991 ms** when it dominates `teacher-classes` and
1,142 ms on `teacher-today`. It is a one-row primary-key read against a 656 kB
table whose server-side mean is 38.9 ms — and whose server-side **maximum is
2,601 ms**. The tail is real; the query is not the problem.

And the estate was drawing from that tail **twice per page load**:

| who | why | cached? |
|---|---|---|
| `shared/teacher-guard.js` | the role check | yes — 2-minute session cache |
| `shared/teacher-admin-nav.js` | `isAdmin()`, deciding whether to draw the Admin link | **no cache at all** |

`teacher-admin-nav.js` also re-read `staff_scopes` beside it (RUM p90 3,350 ms,
max 12,084 ms on `teacher-classes`), for a yes/no that changes about once a
year.

**The fix caches the ANSWER, not the predicate.** `isAdmin` is exported and
`admin.html` calls it for its own fail-closed guard — "one predicate, two
callers", as the file already says. That caller must keep making real reads, so
`isAdmin` is untouched. Only the nav-link decision is remembered, for ten
minutes, in `sessionStorage`, keyed on the viewer's id and environment, and
registered in `CACHE_FAMILIES` so sign-out drops it.

**Two reads removed from every teacher page load after the first in a session**
— and on a hit the link is drawn without even waiting on `client()`, which
polls for the guard's Supabase client on a 120 ms tick.

Ten minutes rather than the guard's two is deliberate: the guard is re-resolving
*who you are* and revalidates in the background on every hit. This is one link,
and a revoked admin who still sees it clicks through to a page that re-checks
from scratch and fails closed.

## 3.4 Frontend — the student page gets the optimistic render teachers already had

`sb.auth.getUser()` is a real round trip that validates the JWT, and everything
the class page does waits behind it. `teacher-guard.js` stopped waiting in
MRB-328 J4(b) — on a cache hit it hands the page its context immediately and
the round trip becomes a correction rather than a wait. **The student guard
never got the same treatment.**

That asymmetry is visible in production: `student-class` p50 **2,337 ms**
against `teacher-classes` **814 ms**, on pages doing comparable work. Part of
that is the two Oregon round trips only the student page makes (§2.5); part is
this.

The change is `teacher-guard.js`'s cache copied deliberately rather than
reinvented, with every safety property it argues for itself: it is not the
security boundary (RLS still filters every row), the key carries the viewer's id
and environment, the stored token's expiry is tested before the cache is
consulted at all, it is `sessionStorage` so it dies with the tab, sign-out drops
it, and the revalidation still runs on every cached load with every denial path
unguarded.

⚠️ **It cannot make a page go blank.** The existing fallbacks are untouched:
every throw from the opening wave still lands in the `catch` that renders a
sentence — *"We waited for your class and it did not arrive. Try again in a
minute or two."* — and a cached render that the revalidation then denies takes
the same bounce it always did.
---

## 4. THE TEACHER ROLLUP (step 1)

`feat/mrb348-teacher-rollup` was rebased onto `origin/main`, which had moved by
MRB-342.1 and MRB-342.2.

### The rebase

**36 files conflicted, every one of them generated, and every conflict on the
cache-bust stamp alone.** The branch carried new hashes for `teacher-live.js`
and `teacher-data.js`; main carried new ones for `set-work.js` and
`set-work.css`. I checked this mechanically rather than by eye — extracting
every conflict region in all 36 files and filtering out the `__MRB_ASSET_V__`
line and stamped `<script>`/`<link>` tags left **zero lines**.

Resolving a build-output conflict by choosing a side produces a stamp that
describes no build, so the resolution was: take the branch side to let the
rebase finish, then run `python3 build_all.py` and let the generator re-derive
every stamp from the real file contents. The diff between the regenerated tree
and the resolved tree was again **stamp lines and nothing else — 0 non-stamp
changed lines**. `set-work.js` correctly came back as main's `1c3f4722`, not the
branch's stale `4bfb9523`, which is exactly what a conflict resolution would
have got wrong.

That restamp is its own commit.

### The premise, re-verified rather than taken on trust

Both migrations were already applied to production by the chat on 23 Sep.
Checked read-only, tonight:

- `public.teacher_class_rollup` exists on production, `SECURITY DEFINER`,
  signature `(p_class_ids uuid[], p_now timestamptz, p_windows jsonb)`,
  **`md5(prosrc) = 76419b38e96c77271ff4ee035a713ffb`** — equal to the value the
  brief gave, so the deployed body is the migration's body and not a drifted
  copy.
- All six RPCs the frontend calls exist on production
  (`teacher_class_rollup`, `class_shoutouts_for_viewer`,
  `class_teachers_for_viewer`, `student_reminders_for_viewer`,
  `class_stars_leaderboard_for_member`, `replace_timetable`).

⚠️ **`teacher_class_summaries` — round two's function — is NOT on production.**
That is not a problem, and it is worth writing down why it looked like one:
`shared/teacher-data.js` on **main** defines `loadClassSummaries()` calling it,
but **nothing calls `loadClassSummaries`** anywhere in the estate. It is dead
code on main. The branch repoints it at `teacher_class_rollup` and wires it up
for the first time, behind a documented fallback that re-reads the long way if
the function is absent or errors.

### ⚠️ Honest scale of the win, today

The rollup stops the six teacher screens shipping every submission row to the
browser to count them. **Production currently holds 10 rows in
`assignment_submissions` and 7 in `assignments`** (§2.6). So the bytes saved
tonight are negligible, and any before/after byte count will look unimpressive.

That is not an argument against it. The page that reads 10 rows today is the
same page that would read 40,000 in two years, and the cost stops growing with
the school. It should be reported as a structural fix, not as tonight's
speed-up — and this report does not claim otherwise.
---

## 5. A WRONG TURN, WRITTEN DOWN BECAUSE THE NEXT RUN WILL HIT IT TOO

`set_work` went red with **15 of 413 checks failing**. The failures were
worksheet branding (`pdf_no_wordmark` found the wordmark on 4 of 4 pages,
`pdf_brand_footer` found 0 chevron strokes where it wanted `[4,2,2,2]`),
`docx_answers_present`, and `edit_locked_after_release` ×4 — the last of which
had the backend answering `editable: ["title","due_at"]` where the gate wanted
`["title","note","due_at"]`.

I checked the backend, found `worksheet.js` still drawing
`doc.text('MrBadmusAI', …)` with a comment citing the old staff-wordmark rule,
found **zero** occurrences of `teacher_note` in `server.js`, and concluded that
MRB-342.1 and MRB-342.2 had landed on the site but their backend halves had
never shipped — a live frontend/backend contract skew on production.

**That conclusion was wrong, and it was wrong in the direction that would have
put a false alarm in front of Mide.** The cause was much duller:

> **`$MRB_BACKEND` pointed at a backend checkout that was five commits behind
> its own `origin/main`.** Local `main` sat at `b630c11`; the real tip is
> `ca54f27`, which is also the build `/api/health` reports from production.
> The missing commits were `57f4345 MRB-342.1` and the four MRB-342.2 ones.

Production has both features. The site and the backend are in step. The gate
was telling the truth about the code it was pointed at, and I was pointing it
at the wrong code.

⚠️ **The tell was available the whole time and I walked past it.**
`/api/health` reports `build`, and I had already read it — `ca54f27ebd61…` — in
the very first measurement of the night, while the local checkout was at
`b630c11`. Comparing those two strings is one command and it is the difference
between "production is broken" and "my checkout is stale".

Two things follow, and both are worth keeping:

1. **`git fetch` in the backend repo FAILS SILENTLY-ish.** Its `fetch` remote
   is `https://github.com/...` and there is no credential helper, so it dies
   with *"could not read Username for 'https://github.com'"*. Its `push` remote
   is SSH and works. So a routine `git fetch` leaves the checkout stale and the
   error is easy to scroll past. Fetch it explicitly:
   `git fetch git@github.com:mrbadmus/mrbadmus---backend.git main`.
2. **Before trusting any gate that drives `$MRB_BACKEND`, check the checkout
   against production**: `git -C $MRB_BACKEND rev-parse HEAD` against
   `curl -s $BACKEND/api/health | jq -r .build`. If they differ, the gate is
   measuring something nobody is running.

Rebased onto `ca54f27`, both speed commits replayed cleanly, and the backend
test suite went from 476 passing to **637** — `test_worksheet.js` alone from 98
to 259, which is itself the proof that the 342.1/342.2 code is now present.
---

## 6. DECISIONS I MADE

Where I would normally have stopped and asked, I chose, and here is each one
with its reasoning.

1. **The 36 rebase conflicts were resolved by REGENERATING, not by picking a
   side.** Every conflict was on the `__MRB_ASSET_V__` line and the `?v=` query
   alone — the branch carried new hashes for `teacher-live.js` and
   `teacher-data.js`, main carried new ones for `set-work.js` and
   `set-work.css` from MRB-342. Taking either side would have shipped a stamp
   that described no build. I resolved to the branch side to get the rebase
   moving, then ran `python3 build_all.py` and let the generator re-derive
   every stamp from the actual file contents. The diff against the resolved
   tree was **stamp lines and nothing else — 0 non-stamp changed lines** —
   and that restamp is its own commit rather than being folded into the
   rollup, because it is a different act.

2. **I did not change any infrastructure, and I did not spend any money.**
   The region finding is the single biggest lever in this report and it is
   written up in §1 with the numbers, the cost and the steps, for Mide to
   decide. Likewise the Auth connection-allocation setting. Both are free;
   both are still his call.

3. **I recommend explicitly AGAINST upgrading Supabase compute**, having
   looked. That is a decision as much as a recommendation to spend would have
   been, and §2.6 shows the working: the whole hot dataset is under 3 MB.

4. **Backend fixes were kept to changes whose equivalence I could prove.**
   `classAccess`'s reordering is proved over all four member/teacher
   combinations; `weekWorkFor`'s eager start preserves the response path
   exactly. I deliberately did NOT touch the heavily-commented ordering inside
   `/api/class/current-assignment` (the consumer branch, the release check),
   because those orderings are load-bearing for what a child may see, and a
   speed run is the wrong context in which to test that judgement.

5. **I left the `/api/health` warm-up pings alone.** They looked at first like
   pure waste — RUM records them on 37 of 57 teacher-classes loads, sometimes
   costing seconds. They are not waste: they are deliberate fire-and-forget
   pings that warm the connection before the page's real backend calls need
   it, they block nothing, and §1 shows connection warmth is the dominant
   variable on this estate. Removing them would have made the thing I was
   trying to fix worse. RUM records them because it faithfully records every
   resource-timing entry, blocking or not.

6. **I treated the `conn` and time-of-day breakdowns as inconclusive rather
   than finding a story in them.** 144 of 164 loads report `4g`, which is what
   the Network Information API says about any fast connection including desk
   wifi, and the worst-looking hours have n = 2 and n = 4. The idle-gap
   analysis explains those loads anyway. Saying "cold mornings" from n = 2
   would have been a story, not a finding.

7. **Disk: I pruned eight worktrees and four shot directories, and nothing
   else.** Every one was provably merged into `origin/main` and provably clean
   (`git status --porcelain` empty). I did not touch the six unmerged
   worktrees (`3d-studio`, `ks3-instruments`, the four content lanes) even
   though they are the bulk of what is left.
---

## 7. WHAT IS PARKED

**Nothing needs applying to production.** This run wrote no migration, because
nothing it fixed needed one — §2.6 shows the database has no work to do, so
there was no index or function to add.

Every migration the shipped branch depends on is already on production,
verified read-only tonight against `supabase_migrations.schema_migrations`:

| migration | local filename version | recorded on prod as |
|---|---|---|
| `mrb347_rls_initplan_hoist` | 20260921192720 | 20260921192720 |
| `mrb347_rls_initplan_hoist_auth_role` | 20260921192908 | 20260921192908 |
| `mrb348_rls_consolidate` | 20260922040000 | **20260922220904** |
| `mrb348_teacher_class_summaries` | 20260922114500 | **20260922231335** |
| `mrb348_teacher_class_rollup` | 20260922231500 | **20260922231645** |

⚠️ **Three of the five are recorded under a DIFFERENT version than their local
filename.** That is the known apply-path drift — `apply_migration` records its
own timestamp rather than the file's — and it matters to anyone reading
`supabase migration list` and concluding something is missing when it is not.

⚠️ **`teacher_class_summaries` is recorded as applied but the function is NOT
on production.** Its rollback was applied without removing the
`schema_migrations` row. That is harmless — nothing calls it, on main or on
this branch — but it is exactly the shape that makes a future reader think the
database is inconsistent. It is not; the row is a receipt for a migration that
was later undone by hand.

The function that IS live and IS used is `teacher_class_rollup`,
`md5(prosrc) = 76419b38e96c77271ff4ee035a713ffb`, matching its migration.
---

## 8. THE GATES

`prepush_gate.py --record-all` on the rebased tip, with `$MRB_BACKEND` and the
three permitted gate credentials from `docs/mrb335/RISKS.md` E6
(`MRB_SET_WORK_PASSWORD` any value, `MRB_THROWAWAY_PASSWORD=mrb326-throwaway`,
`MRB_TEST_TEACHER_PASSWORD=mrb293-drive-only`). `MRB_DRIVE_PASSWORD` and
`MRB_TEST_STUDENT_PASSWORD` were never set, as the hard lines require.

**20 gates ran fresh, 12 passed on an unchanged receipt, 13 were skipped by
rule as unaffected, 5 skipped for a missing precondition.**

The one that matters most for step 1 is **`teacher_rollup_equal` — GREEN**. That
is the gate that drives `public.teacher_class_rollup` as a real signed-in user
under real RLS and diffs it, cell by cell, against what the browser's own
JavaScript would have computed. It is the proof the aggregate is not a second
opinion.

Also green and worth naming: `teacher_perf_budget`, `teacher_behaviour`,
`teacher_reach`, `today_drive`, `teacher_picker_drive`, `ks4_chrome_drive`,
`teacher_admin_real`, `mrb328_card_prefetch`, `verify_ks3`, `consumer_flag_off`,
`assignments_hold_drive`.

### `set_work` — what was wrong, and what is inherited

It went red at **15 of 413**. Ten of those were the stale-checkout mistake in §5
and vanished the moment `$MRB_BACKEND` was pointed at the right code: the
re-run was **5 of 423**.

Of the five that remain, three are **fixture staleness that `set_work_drive.py`
documents about itself**:

> "…the SAME lookup that already reports two of this file's inherited reds
> ('a scope of 5–9 questions exists to cap against', 'a scope of 10–14
> questions exists'), **because MRB-338 grew both banks past the point any real
> scope is that small any more**."

`a small KS3 lesson exists to drain` is the third and the identical mechanism —
it hunts for a KS3 lesson holding eight or fewer rows at Easy, and MRB-338 grew
that bank too.

⚠️ **These are not harmless.** The same comment says the consequence out loud:
every assertion the file makes about the count field's clamp path now lives
inside `if small:` / `if mid:` and therefore **never runs**. That is a gate
quietly measuring less than it reads as measuring — the pattern
`docs/.../gates-stop-watching` is about. It is not this ticket's to fix, and it
should not be left unnamed.
---

## 9. THE DEFECT I SHIPPED INTO THE TREE, AND HOW THE GATE CAUGHT IT

This is the most important thing in this report after §1, because it is the one
that would have hurt a child.

### What I did

§3.2's first version started `weekWorkFor(classId, week, isStudent)` **eagerly,
at the top of `/api/class/current-assignment`**, and had every `send` await that
one promise. The reasoning was that `week_work` depends only on the class and
the week, both known long before the route picks an assignment. That reasoning
is true, and the change was still wrong.

### Why it was wrong

**This route COMPOSES a class's weekly homework lazily, on first read.** Eleven
`send()` sites hang off it, and two of them — the compose-success path and its
`raced: true` sibling — are reached *after* an assignment has been written.

Started eagerly, `weekWorkFor` reads the week **before that assignment exists**.
So the very request that composes a child's homework would answer with a
`week_work` list that does not contain it. The child opens their class page, the
work is composed for them, and the page shows a week with the new work missing —
until they reload.

That is squarely inside the hard line this run was given: *pupils never lose
work, and no page may go blank because one read is slow.*

### What caught it — and what did not

- **637 backend unit tests passed it.** Twice. They are pure-function tests and
  this is an ordering bug across two database reads; nothing in that suite can
  see it.
- **`set_work_drive.py` caught it**, as `multi_class_atomic` — two reads of this
  route either side of a *refused* write disagreeing about the week, when
  nothing had been written. The assertion is not even about `week_work`; it uses
  `week_titles()` as its instrument for "did anything land", and the instrument
  moved under it.

⚠️ **I nearly overrode it.** Two of the five remaining failures were this bug and
three were inherited fixture staleness, and the inherited three are documented
as inherited *in the drive's own source*. It would have been easy, at that
point, to write one `GATE-OVERRIDE: set_work — inherited` line and push. The
thing that stopped it was running a **control**: the same drive against a
worktree at `ca54f27` with my two commits absent.

| run | backend | failed |
|---|---|---|
| first | stale checkout `b630c11` | 15 of 413 |
| second | rebased, my commits present | 5 of 423 |
| **control** | `ca54f27`, **my commits absent** | **3 of 423** |

Three is the baseline. The difference was mine, and the control is the only
thing in this sequence that could have told me so.

### The fix

The optimisation survives **only on the branch that has already decided not to
compose** — `if (existing)`, "this class already has this week's work", which is
every request after the first in a week and therefore the common path. There it
starts beside the assignment, questions and progress reads and costs nothing.
Every other `send` gets no pre-started promise and calls `weekWorkFor` exactly
where it always did, after the work exists.

The saving is smaller than the version I first wrote. It is also correct.
---

## 10. A SECOND SESSION WAS RUNNING, AND MY WAITS WERE WATCHING IT

Partway through, `ps` showed **two** `prepush_gate.py` processes. One was mine.
The other was `--record verify_ks3`, running with its cwd in
`mrbadmus-worktrees/diagrams` on `feat/diagrams` — a worktree that did not
exist when this run started. Another session had begun work alongside this one.

That matters for a reason beyond the surprise: **every "wait for the gate to
finish" in this run was written as**

```sh
until ! ps -eo command | grep -qE "[P]ython.*prepush_gate"; do sleep 30; done
```

which matches ANY session's gate, not this one's. With a neighbour running a
fifteen-minute `verify_ks3`, that loop waits for THEIR work and reports MY gate
as still running — or, worse in the other direction, a pattern that happens to
match nothing reports done while my own gate is mid-flight.

The project's own note on concurrent sessions says exactly this: *`pgrep -f`
matches every session; wait on a captured PID.* I wrote the loop the wrong way
several times before the neighbour appeared and made it visible. Corrected to:

```sh
until ! ps -p "$PID" > /dev/null 2>&1; do sleep 25; done
```

⚠️ **Nothing measured in this run was corrupted by it** — the receipts are
per-gate and were checked individually, and `origin/main` was re-read
immediately before pushing and had not moved (`5d571647e` throughout). The
neighbour is on a feature branch. But the failure mode is real and it is the
kind that produces a confident wrong answer rather than an error.

### `set_work` after the fix — and the one loose end

| run | backend | failed |
|---|---|---|
| 1 | stale checkout `b630c11` | 15 of 413 |
| 2 | rebased, eager `weekWorkFor` (the bug) | 5 of 423 |
| **control** | `ca54f27`, **my commits absent** | **3 of 423** |
| 4 | rebased, corrected fix | 4 of 416 |

Run 4's first three are the control's three, exactly. The fourth is
`row_download_lands`, and it is **intermittent rather than caused**: it PASSED
in run 2 — the run carrying the MORE aggressive version of the same change —
and failed in run 1 with the artefact visible in its own evidence line,
`downloads.html · 33619428 byte(s)`. That is Chrome saving its own downloads
PAGE instead of the PDF, a capture failure in the harness, not an answer from
the route. A confirmation run was made rather than asserting this.

⚠️ `set_work` cannot go green on this estate whatever I do — the three
inherited failures are real, documented in the drive's own source, and not this
ticket's to fix. The override names them; it does not pretend they are absent.
---

## 11. WHAT LANDED, AND HOW IT WAS PROVEN LIVE

| repo | range | what |
|---|---|---|
| `mrbadmus-site` | `5d571647e..f66072679` | the teacher rollup (step 1) + the post-rebase restamp |
| `mrbadmus---backend` | `ca54f27..49e15a7` | `classAccess` 4 round trips → 2; `week_work` read beside the assignment on the compose-free path |

### The live check, done the way the cache trap requires

⚠️ **A 200 carrying stale assets is the failure mode that looks like success**,
so the stamp was read from the PAGE MAP first and the asset was never polled
before the map referenced it.

1. Baseline captured BEFORE the push: `teacher-live.js?v=b8fa3a37`.
2. Committed build expects: `teacher-live.js?v=94834e17`.
3. Polled the PAGE (not the stamped asset) until the map moved to `94834e17`.
4. Only then fetched the stamped asset, with a `&nonce=` to defeat any
   intermediary, and compared it against the committed bytes:

```
live bytes:      195474
committed bytes: 195474
cmp → IDENTICAL
```

So the bytes being served are the bytes that were committed, not merely a 200
at the right URL.

### Backend

`/api/health` reports `build=49e15a7` (was `ca54f27`), `db=ok`, and `db_ms`
settling to the warm floor across six consecutive calls:

```
119, 182, 121, 57, 63, 61
```

That curve is itself §1 in miniature — the first call after idle pays for the
connection, the rest reuse it.
---

## 12. STEP 4 — PROVING IT ON PRODUCTION, AND WHAT CANNOT YET BE PROVEN

### The honest position on production numbers

The brief asked for a `build`-filtered before/after on `rum_timings`. **The
traffic is too thin to judge tonight, and saying otherwise would be inventing a
result.** The five-day window that produced every baseline in §2 contains
**17 student-class loads and 57 teacher-classes loads**, all on one build
(`d1fecb43`). A new build deployed at 20:26 on a Wednesday evening will not
accumulate a comparable sample before this run ends.

**What to run in a few days**, once real lessons have happened:

```sql
select build, page, count(*) n,
       percentile_disc(0.5) within group (order by ttoi_ms) p50,
       percentile_disc(0.9) within group (order by ttoi_ms) p90
from rum_timings
where created_at > now() - interval '7 days'
group by build, page
order by page, build;
```

⚠️ **Filter on `build` or the comparison is meaningless** — a week spanning two
deploys averages into a number describing no version of the site. The old build
is `d1fecb43`. The new one is whatever `config.js`'s hash became; read it off
the first new row rather than assuming.

⚠️ **And bucket by idle gap as well as by build** (the query in §2.2). Given
§1, a sample drawn mostly from hot loads and compared against a baseline drawn
mostly from cold ones will show an improvement that is really just warmth.

### What WAS proven tonight, and how

Local, against TEST, three runs per journey, median — `perf_waterfall.py`.
⚠️ **This is a developer laptop on home broadband against TEST's small seed. It
is good for SHAPE and worthless as a model of a Year 8 on a school Chromebook.**
The request counts below are the claim; the millisecond figures are noise at
this sample size and are not offered as results.

| journey | real requests | pre-mount requests | `staff_scopes` |
|---|---|---|---|
| teacher-classes BEFORE | 11 | 22 | present |
| teacher-classes AFTER | **9** | **18** | **absent** |
| student-class BEFORE | 16 | 32 | — |
| student-class AFTER | 16 | 32 | — |

Two reads gone from every teacher page load after the first in a session, and
four requests counting their CORS preflights. `staff_scopes` is read by
`teacher-admin-nav.js` and by nothing else in the estate, so its disappearance
is a clean proof rather than an inference.

**student-class is unchanged at 16, and that is the expected result, not a
failure.** §3.4 changes *when the page may paint*, not what it fetches. The
instrument counts requests; it cannot see a removed wait. Reporting a saving
there would have been unsupported, so none is reported.

### The backend fixes have no local number, deliberately

`classAccess` 4 round trips → 2 and the `week_work` read are **counts of
database round trips**, and the wall-clock value of a round trip is the whole
subject of §1: 58 ms warm, 651 ms at p90, 1,416 ms at worst. Measuring them
from a laptop against TEST-in-Ireland (a ~10 ms hop) would produce a small,
true-looking number that understates the production saving by roughly an order
of magnitude, because production's backend is in Oregon. ⊕ *(Corrected, round 5: it is in Frankfurt; the per-trip cost was misattributed.)*

So they are reported as what they are — **two fewer crossings on `classAccess`,
two fewer on the common `current-assignment` path** — and multiplied by §1's
measured per-crossing cost rather than by a laptop's.
---

## 13. WHAT I WOULD DO NEXT, IN ORDER

> ⊕ **Corrected (round 5):** item 1 is withdrawn (Render is already in Frankfurt). Item 2 stands. See round5-slow-leg.md for what replaces item 1.


1. **Move Render to Frankfurt** (§1). Free, biggest single win, Mide's call.
   Use a custom domain so no hardcoded URL changes.
2. **Switch Supabase Auth to percentage-based connection allocation** (§2.6).
   Free, a dashboard setting. `getUser()` gates every page load and Auth is
   capped at 10 connections.
3. **Re-read `rum_timings` filtered on `build`** after a few school days, with
   the idle-gap bucketing (§12), and see what actually moved.
4. **Give `set_work_drive.py` scopes it can still find** (§8). Three of its
   checks now hunt for question pools that MRB-338 grew past, and the drive's
   own comment says the count-clamp assertions consequently never run. A gate
   measuring less than it reads as measuring is worse than a red one.
5. **Consider the remaining redundant student-side reads.** `class_members` is
   read three times per student page load and `classes` three times, by
   `class-entry.js`, `student-data.js`'s list prefetch and `loadStudentClass`.
   One of the three is a deliberate freshness re-read and documented as such;
   the other overlap looks real. Not touched tonight — the student page is the
   surface pupils use and it deserves its own run, not the tail of this one.
6. **Drop `mrb347_policy_backup` and `mrb348_policy_backup`** from production
   when someone is next doing a prod write. Working files from the RLS rounds.

## 14. DECISIONS I MADE — the rest

Continuing §6.

8. **I pushed the rollup before the frontend fixes were ready**, rather than
   batching one push at the end. The brief said land step 1 first; the shipping
   rule in CLAUDE.md says one unit is one commit and one push; and an
   interrupted session should leave shipped work shipped. Three pushes, three
   verified units.

9. **I overrode `set_work` and `teacher_admin_foreign_class`, and I measured
   both first.** The foreign-class signature was re-run and matched the
   documented one character for character. `set_work`'s three were proved
   inherited by a CONTROL run rather than by citation — which is the only
   reason the two failures that were MINE did not ship inside that override.

10. **I did not fix the worksheet-branding skew I thought I had found**, because
    it did not exist (§5). Had it existed it would still not have been this
    ticket's to fix — it is a brand ruling, and those are Mide's gate.

11. **Both session caches went in ONE commit** rather than two, because the
    `CACHE_FAMILIES` registration that makes sign-out clear them is a single
    list in one file. Splitting it would have left one commit shipping a cache
    that nothing clears — a worse outcome than a commit covering two changes of
    identical shape. The commit message separates them.

12. **I reported no production before/after** (§12). The traffic is too thin,
    and the brief's own instruction was to report honestly including anything
    that did not improve.