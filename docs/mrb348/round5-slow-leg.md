# MRB-348 round 5 — the slow leg, measured

23–24 September 2026. Unattended run.

## The answer

**The slow leg is the Supabase instance itself. It has 411 MiB of RAM and it
is living on swap.**

It is not the network, not the edge, not Render, not the pooler, and not
query execution inside Postgres. When a request is slow, it is waiting on a
starved machine. Everything on that machine stalls at once: the gateway,
Auth and PostgREST all slow down together.

- `node_memory_MemTotal` = **411 MiB**. That is Nano-sized; a Micro is about
  1 GB. Round 4 assumed Micro from `shared_buffers` and was wrong.
- **~424 MiB is in swap**, and the instance has swapped in **744 million
  pages** since boot (~185 days).
- During this run, a quiet night, it swapped in a **median 214 pages/s (p90
  551)**. 6% of all CPU time was spent waiting on disk, three times the
  lifetime average. CPU steal was 0.002%, so CPU credits are not the problem.

**Correction first.** `docs/mrb348/round4-speed.md` said the backend runs in
Oregon. It runs in **Frankfurt**. That report was never committed by round 4
(its session ended first). It is committed now, reconstructed from the
transcript, with the Oregon claim, the Frankfurt-move recommendation and the
"don't touch compute" advice marked **withdrawn** in place.

## 1. Each leg, cold vs warm

The probe ran for 4½ hours, 30 rounds, with the idle gaps interleaved.
Each round had three phases:

- **cold**: the first call after the idle gap, on a fresh connection;
- **warm-fresh**: the same call again straight away, on a new connection;
- **warm-reused**: the same call again, on the same connection.

The Mac → production calls used the anon key and were read-only.
Mac → TEST used `hz_amy@test.mrbadmus`. Render → production ran through a
temporary route, now removed.

Figures are the total time in ms, **p50 / p90**. Cold columns are n=10 each;
warm-fresh n=30; warm-reused n=60.

| path | leg | cold 1 min | cold 5 min | cold 20 min | warm, fresh conn | warm, reused conn |
|---|---|---|---|---|---|---|
| Mac → prod | `/auth/v1/user` | 145 / 258 | 225 / 658 | 140 / 338 | 162 / 502 | **32 / 58** |
| Mac → prod | `profiles?id=eq.` | 606 / 1234 | 438 / 2686 | 205 / 1866 | 199 / 878 | **92 / 710** |
| Mac → prod | `rpc/class_tier_rule` | 154 / 382 | 167 / 1156 | 181 / 590 | 170 / 926 | **98 / 324** |
| Mac → TEST | `/auth/v1/user` | 176 / 249 | 184 / 226 | 204 / 340 | 59 / 80 | 27 / 34 |
| Mac → TEST | `profiles?id=eq.self` | 316 / 439 | 500 / 584 | 134 / 227 | 83 / 132 | 33 / 63 |
| Mac → TEST | `rpc/class_tier_rule` | 100 / 158 | 116 / 151 | 572 / 716 | 79 / 113 | 29 / 56 |
| Render → prod | Auth admin user read | 427 / 705 | 326 / 528 | 261 / 569 | 106 / 448 | 68 / 293 |
| Render → prod | `profiles?id=eq.` | 444 / 2662 | 536 / 1463 | 204 / 569 | 156 / 838 | 132 / 552 |
| Render → prod | `rpc/class_tier_rule` | 211 / 1627 | 244 / 1642 | 161 / 269 | 167 / 967 | 105 / 455 |
| Render → prod | `/auth/v1/health` | 172 / 409 | 108 / 501 | 93 / 183 | 76 / 590 | 63 / 149 |

What the table says:

- **The handshake is small.** DNS + TCP + TLS has a median of 22–45 ms from
  the Mac and 10–16 ms from Frankfurt. The network is not the leg.
- **Production's idle gap is not the variable.** Twenty minutes idle is no
  worse than one minute. Production is never really idle: the backend's
  health read lands about once a minute. TEST, which nothing else touches,
  *does* show a real cold start (Auth 176 vs 59 ms).
- **A fresh connection costs production ~100–130 ms beyond its handshake.**
  Auth goes from 162 to 32 ms and profiles from 199 to 92 ms (Mac, p50).
  This is part of the connection-warmth curve real users see.
- **Production's tails are about 5–7× TEST's**, on the same instance size,
  even on warm calls. TEST swaps about 8× less: 73 million pages over ~146
  days, against 744 million over ~185 days.

## 2. Where the time goes when a request is slow (server side)

| question | evidence | answer |
|---|---|---|
| At the edge? | Our requests' `response.origin_time` (p50 207/175/72 ms) against what the Mac saw after the handshake (225/171/68) | **No.** The edge plus the UK network adds about 0–20 ms. |
| Inside Postgres? | `pg_stat_statements` for the same probe reads: profiles mean 17.6 ms (max 71), RPC mean 8.2 ms (max 61). Upstream, the same calls took p90 942 / 684 ms, max 1,835 / 1,112. The hot statements read ~0 blocks from disk. | **No.** Under a tenth of the time, and even that is slow for work this small. |
| Waiting for a pooler? | PostgREST and Auth connect directly, not through the pooler. `pgbouncer` clients waiting = 0 in all 92 samples. | **No.** |
| In Auth (GoTrue)? | On `/user` calls that never touch the database (our anon 403s), Auth's own log says p50 4.7 ms, **p90 98, max 328**. The edge recorded p50 72, p90 428, max 860 for the same calls. | **Yes, and around it.** A Go process doing no I/O is sometimes 20–70× slower than its median. |
| In PostgREST? | 24 hours of real traffic: slow requests arrive in **bursts that finish together** across tables, clients and services. At 17:56:21, eight reads took 4.1–4.2 s each. At 05:34:38, Auth and six PostgREST reads took ~3.9 s each. At 18:06:01, four **401s** took 1.7 s; a 401 is refused before any query runs. | **Yes.** It stalls at the same moments as Auth. |
| Is it the machine? | Every request in the run, grouped by the swap-in rate in the 30-second interval that contained it (table below). | **Yes.** The tail follows swap. |

| swap-in rate in the same interval | n | p50 | p90 | p99 | share over 1 s |
|---|---|---|---|---|---|
| lowest third (184–310 pages/s) | 292 | 97 ms | 479 ms | 1,131 ms | 2.1% |
| middle third (335–546) | 277 | 111 ms | 526 ms | 1,627 ms | 5.1% |
| highest third (557–2,309) | 243 | 170 ms | 1,047 ms | 3,713 ms | **11.5%** |

One caveat: the linear correlation is weak (r = 0.18). The relationship is
in the tail, not the median, and the tail is what users feel.

The real-traffic view says the same thing. Over 24 hours, the browser's
own-profile read had origin time p50 **16 ms**, p99 3.3 s and max 10.3 s.
Auth `/user` measured *inside* Auth was p50 75 ms, p90 1.2 s, max 10.5 s.

## 3. The backend path

- Node's global fetch closes an idle socket after **4 s** unless the server
  sends a Keep-Alive hint. Supabase sends none (`server: cloudflare`, no
  header), and nothing in the backend overrode the default.
- The Frankfurt → Ireland handshake is about 12 ms, but a fresh connection
  costs about 40 ms more than a reused one on a trivial Auth call (76 vs
  63 ms p50; 106 vs 68 on the admin read).

## 4. The client path

Mapped from the code, then measured:

- **Teacher pages:** on a session-cache hit (2 min), the page does not wait
  on `getUser()`; on a miss, everything in `onAllowed` waits.
  `teacher-admin-nav.js` separately re-read `profiles` + `staff_scopes` on
  every load.
- **Student page:** `getUser()` gated every load. The class-list reads are
  already prefetched beside it (0 of 8 loads wait). But
  **`/api/class/current-assignment`, which blocks first paint, started only
  after `/auth/v1/user` returned, on 8 of 8 loads.**
- One `createClient` per page, with no custom `auth.lock`. When a token has
  expired, every read queues behind `/auth/v1/token` (production browser
  p50 497 ms, p90 1.7 s, 22 calls/day). **Not measured separately this
  round.**

## 5. What I changed, before → after

| change | before | after | notes |
|---|---|---|---|
| **Backend keep-alive 60 s** (`a43b46a`, live) | second read 8 s after the first: p50 183, p90 309 ms | p50 **135**, p90 **247** ms | 15 interleaved pairs each, on the live dyno. At a 2 s gap: 113 → 129 (noise). About 50 ms, when a call lands on an idle socket. |
| **Student session cache**: round 4's unpushed `b99b9b7e8` carried over, TTL 2 → **30 min** (site `802d689cb`, live) | `current-assignment` waits for Auth on 8/8 loads, starting ~100 ms in | **0/8**, starting ~40 ms in | ⚠️ **TEST's mount median did not improve** (827 → 940 ms, within noise): TEST's Auth is ~90 ms. The gain is production's Auth leg (p50 214, p90 1.7 s at the edge) on repeat loads within 30 minutes. 30 min because RUM's worst bucket is 5–30 min idle, where a 2-minute cache has already expired. |
| **Admin-link cache** (same commit, round 4's work) | 11 real requests on teacher-classes | 9, `staff_scopes` gone | Round 4's measurement, not re-measured here. |
| TEST schema: added the missing `add_profiles_external_student_id` | the `class_csv_upload` gate could not write pupils | green | TEST only. It has been on production since 29 Jun. Found once the gate below could actually run. |
| `class_csv_upload_drive.py` read a pruned worktree's `config.js` | gate crashed before driving anything | runs, green | |

**Not improved, and not ours to fix in code:** the instance stalls. No
query shape, cache or pre-warm removes a swap-in on a 411 MiB machine. I did
not add a keep-warm pinger: production is already hit about once a minute,
and the stalls happen anyway.

## 6. For Mide: change the compute size (dashboard, your call)

**Evidence.** 411 MiB of RAM with ~424 MiB swapped out. Constant swap-in at
night (median 214 pages/s). The tail more than doubles in high-swap
intervals (p90 479 → 1,047 ms; share over 1 s 2.1% → 11.5%). Auth and
PostgREST stall together.

**Expected gain.** Prod's working set is roughly 600 MB: what's in RAM plus
what's in swap. A 1 GB **Micro** holds it with room to spare, so swapping
should mostly stop. My best estimate from our own data is that the
high-swap tail disappears. I have no non-swapping instance to measure
against, so treat that as an estimate and re-measure.

**Price.** The org is on **Pro**. Supabase bills a Nano in a paid org at the
Micro price (~$10/month, covered by the Pro plan's $10 compute credit). So
**Nano → Micro should cost nothing extra.** Small (2 GB) is ~$15/month,
+$5 net, if Micro still swaps.

**Clicks.** Supabase dashboard → project **mrbadmus** → **Project Settings →
Compute and Disk**.
1. Confirm it says **Nano**.
2. Choose **Micro**, then Review → Confirm.

Supabase says the restart takes under 2 minutes. **Do it outside school
hours.** Afterwards, ask for this round's probe to be re-run. The numbers to
compare are the swap-in rate and the p90/p99 of `response.origin_time` on
`/rest/v1/profiles`.

**Optional, free, low value:** switch Auth to percentage-based connection
allocation (the advisor's only notice). Auth is slow even on calls that
never touch its database, so the 10-connection cap is **not** the named
cause.

**Performance advisor:**
- 50 unindexed foreign keys (INFO): all on tiny tables, so not real.
- One multiple-permissive-policies warning on `school_invitations`: an
  onboarding-only table, not hot.
- Two backup tables with no primary key.
- **Nothing acted on.**

## Decisions I made

1. **Rebuilt round 4's report from its transcript** and committed it with
   the corrections marked, rather than rewriting it. Its session ended
   before the file was written, so it existed nowhere on disk.
2. **Carried round 4's unpushed `b99b9b7e8`** into my own worktree by
   cherry-pick, rather than working in its worktree (one session per
   worktree). If that session is resumed, a rebase will drop the duplicate.
3. **Changed the student cache TTL to 30 minutes.** The measurement showed
   2 minutes only helped loads that were already fast. Safety rests on the
   per-load revalidation, RLS and the token-expiry check, none of which
   changed.
4. **Authenticated the diagnostic route with a secret header** (only its
   sha256 committed), because the probe needed production's service-role
   key and no production user account may be used. The secret file is
   deleted.
5. **Added `undici` as a backend dependency** for the keep-alive setting.
   Node's built-in fetch exposes no other way to change it.
6. **Applied one additive production migration to TEST** to unblock a gate.
   TEST is the sandbox, and the migration had been on production for three
   months.
7. **No production writes or DDL.** Production was only read: anon GETs,
   service-role GETs via the removed route, the metrics endpoint,
   `pg_stat_statements` and logs.

**Deviations:**
- The brief asked me to correct "the memory note you wrote". No memory note
  mentioned Oregon; round 4 never wrote one. → I wrote a correct one
  (`project_infra_regions_and_instance`).
- The brief asked for cold samples after 1, 5 and 20 minutes idle. On
  production the server is never idle that long, because the backend's
  health read runs about once a minute. → I ran it as specified and report
  that the gap made no difference there (it does on TEST).
- The privileged metrics endpoint returns a cached scrape, so per-round
  before/after deltas were meaningless. → I used a separate 30-second
  series instead.

## Landed

| repo | commit | what |
|---|---|---|
| backend | `6f22702` | temporary diagnostic route (removed) |
| backend | `a43b46a` | keep-alive 60 s |
| backend | `0f2e1d6` | route removed, on top of MRB-352's `8055b79`. **Live**; `/api/_diag/*` answers 404 even with the secret. |
| site | `b689a81df` | round 4's session caches (carried) |
| site | `90e8e0ef9` | student TTL 30 min |
| site | `802d689cb` | `class_csv_upload` drive fix. **Live**; `student-guard.js` and `teacher-admin-nav.js` byte-identical to the commit. |

**Gates:** 20 fresh passes, plus `class_csv_upload` green after the fix.
Two overrides, both inherited with identical signatures:
- `teacher_admin_foreign_class` (C7 ×3);
- `set_work` (3 of 423, round 4's control-proven fixture staleness).
