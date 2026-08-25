# MRB-290 — the KS4 weekly leaderboard system, planned before built

25 Aug 2026, written as part of the overnight run, before the build.

## What the feature set needs, and where each number comes from

Design's page runs entirely on a ten-field per-student record —
`{name, rank, pct, marks, total, secs, per{B,C,P}, done[], move, streak}` —
plus a weeks strip, four header stats, a countdown, and the viewer's own
standing. Everything below her `deco()` is pure presentation over that
record; everything above it fabricates. The port therefore cuts at exactly
that line: real records in Design's own shapes, Design's arithmetic
untouched beneath.

## Derive vs capture — the audit

Production already records, per attempt: `score`, `max_score`,
`time_taken`, `subject`, `tier`, `pathway`, and the week via
`challenge_id → weekly_challenges.week_start`. Eleven weeks of history
(24 Apr → 21 Aug 2026), zero null `time_taken`, zero null `tier`,
verified by direct reads.

**Every feature in the delivery is derivable. Capture needed: NONE.
DDL needed: NONE.**

| Feature | Derivation |
|---|---|
| weekly history strip | distinct attempted `week_start`s in view + current week |
| per-week top bar | that week's board, rank 1's pct |
| countdown | `closes_at` computed SERVER-side from `getWeekStart()`'s manual BST rule; client ticks against `server_now`, never the device clock |
| own standing | viewer's row + rank over the FULL board, via Bearer token |
| tier toggle / subject filters | `tier` and `subject` columns, recorded at attempt |
| podium + table | board sort: pct desc → secs asc → name asc (MRB-137's percentage rule, kept — pathways merge) |
| paper chips / breakdown | per-subject rows: which subjects have a row (`done`), each row's pct (`per`) |
| movement ▲▼/NEW/HELD | rank joined against the PREVIOUS ATTEMPTED week's board (not week−7d — a week nothing happened is not a competition week) |
| streaks | consecutive strip weeks entered in view, ending at the viewed week |
| entries / median / fastest / climb | full board server-side; fastest is the minimum single-PAPER time (the label says paper; Design's sample only had per-student totals) |
| cut line | rank 10's pct, null under 10 entries |

Because nothing is stored that a student's real rows don't already imply,
weeks recorded before tonight need no honest "—": every column the
derivations touch has existed since the system launched. The "—" states
that DO render are data states: a paper not attempted, no positive climb,
week one carrying no movement and no streak — all falling out of the
derivations, never special-cased with literals.

## The backend

One new endpoint, additive: `GET /api/weekly-leaderboard/board`
(`?tier=…[&subject=…][&week_start=…]`, optional Authorization). It ships
ONLY the top 10 rows plus the viewer's own — ranks beyond 10 are computed
server-side precisely so the names behind them never leave the server
(the README's board rule, and the safeguarding-friendly reading of it).
Stats are computed over the full board server-side for the same reason.
Deployed and verified against direct SQL before the frontend work began:
404 before push, 200 after; entries/median/fastest/top row all equal to
a hand-run query on week 2026-08-14.

## Identity is frozen

Who appears and under what name/avatar is exactly the live rule:
`username || first_name || 'Student'`, `avatar_url`, school. ⚠️ Real
usernames are GENERATOR-STYLE (`WolfSummit53` is a real student) — the
same shape as Design's samples, which is why grepping for "sample-looking
names" proves nothing. The tells gate pins the EXACT 61 derived sample
handles (30 Higher + 30 Foundation off Design's roster formula +
`AmberYew12`), computed from the vendored delivery's own constants on
every run, never typed.

## The frontend port

Through the porter, never pasted: a `PAGES` row compiles the vendored
delivery via `student_template.py`; `build_leaderboard_port.py` (modelled
on `build_teacher_port.py`) emits `leaderboard.html` + a fixture pair in
an unpublished directory; `shared/leaderboard-live.js` seams
`roster/raw/board/streak/weekDates/VIEWER/WEEKS/LIVE/hash/rng` with reads
from the new endpoint and leaves `deco()` and the renderVals tail as
Design wrote them. Stats arrive from the payload (the client cannot
compute them — it never sees the full board).

Mide's two rulings applied: the delivery defines the look below the nav
(cream language, no correction toward the old dark theme); the nav is the
LIVE LANDING PAGE's nav — full-bleed, `space-between`, wordmark hard left,
cluster hard right, gold-to-rust root-page chevron — replacing Design's
1180px-inset nav wholesale. That replacement also dissolves the delivery's
single `x-import` (the student BrandMark, wrong for a root page), which is
what lets the compiler run without a standalone capture.

Design defaults the tier toggle to Higher; the live page lands the viewer
on their own profile tier. Live logic wins: profile tier when signed in,
foundation otherwise.

The hand-written `leaderboard.html` retires to `docs/ks3/retired/`, and
the builder refuses to run if the retired copy is missing — same
protection the teacher port uses.
