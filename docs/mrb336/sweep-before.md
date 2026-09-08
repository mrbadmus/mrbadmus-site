# MRB-336/337 §8 — student pages, the BEFORE sweep

**Merge base `44dadd96c`.** Everything in this file was measured on that commit,
in a worktree that contains no part of today's work. Its purpose is to let the
AFTER pass classify each defect it finds as *ours* or *pre-existing*: a row that
appears here is pre-existing, with proof.

Nothing was fixed. No product file was changed. `python3 build_all.py` exited 0
before any measurement was taken.

---

## The world, so the AFTER pass can reproduce it exactly

| | |
|---|---|
| Worktree | `/Users/midebadmus/Documents/GitHub/mrbadmus-worktrees/sweep-before` (detached at `44dadd96c`) |
| Build | `python3 build_all.py` — exit 0, all six generators |
| Backend | the MAIN checkout `/Users/midebadmus/Documents/GitHub/mrbadmus---backend` at `6f4b3fa` (`main`, pre-change), run as `PORT=3336 EXTRA_CORS_ORIGINS=http://localhost:5501 node server.js`. **No file in that checkout was modified** — `EXTRA_CORS_ORIGINS` is the sanctioned env seam (`server.js:110`) that exists for exactly this |
| Site | `python3 -m http.server 5501 --bind 127.0.0.1` in `<worktree>/mrbadmus_site` |
| Second site | `python3 -m http.server 5500` in the same directory, for the production-data leaderboard pass only (see G1) |
| Supabase | TEST `qeppkiswvclkkwbxmlok`. Reached by serving from `localhost` with **no** `?env` — `shared/config.js:93` makes localhost mean TEST unless `?env=prod` |
| URL shape | `http://localhost:5501/<page>?api=http://localhost:3336` — the localhost-only backend override at `shared/config.js:127` |
| Sign-in | real GoTrue password grants, no fabricated JWTs. Password `TestPass!2026`, from `supabase/seeds/20260503221955_stage2_test_seeds_expanded.sql:197` |

### Identities

| key | email | class | shape |
|---|---|---|---|
| `ks4comb` | `hannah.patel@test-rainford.local` | 10A `2a000000-…-0002` | KS4 combined higher, 17 assignments, 2 teachers, 3 shoutouts |
| `ks4trip` | `student1@test-rainford.local` | 10X1 Biology `22000000-…-0001` | KS4 triple higher, 4 assignments, **1** teacher |
| `ks3` | `aiden.cole@test-rainford.local` | 8X1 `2a000000-…-0001` | KS3, 4 assignments, 2 teachers |

Three personas × two viewports (390, 1280) × eight pages = 48 walks, 48
screenshots in `docs/mrb336/shots-before/`, plus two production-data leaderboard
shots (`prod-leaderboard-390.png`, `prod-leaderboard-1280.png`). 132 controls
pressed individually, each on its own fresh mount.

### ⚠️ The state of the TEST fixtures, which bounds what could be tested

Every assignment on TEST — all 30 of them, across all six classes — has
`academic_week = NULL`, `release_at = NULL` and **zero rows in
`assignment_questions`**, and every `due_at` is in May 2026. TEST also holds
exactly one `academic_years` row, `2025-26`, `2025-09-01 → 2026-08-31`, which
**ended eight days before this sweep ran**.

That is not a product defect and it is not reported as one. It does mean:

- The academic-year fallback path is what every persona exercised (see B4/F3).
- **No held / unreleased assignment exists on TEST**, so "a held-state card
  shown wrongly" could not be exercised at all. That is a gap, recorded as M1,
  not a pass.
- **No assignment with questions exists on TEST**, so the answering surface of
  `student/assignment.html` was unreachable by any route (see "pages I could
  not reach").

---

## Inventory — 26 findings

Severity: **S1** a child sees something wrong or is stuck; **S2** visibly
broken but recoverable; **S3** cosmetic, hygiene, or invisible to a student.

| # | Page | Finding | Rendered text | Source | Viewport | Sev | Shot |
|---|---|---|---|---|---|---|---|
| **A — empty labels and placeholder glyphs** (no literal `null`/`undefined`/`NaN` was found anywhere) |
| A1 | class | The teaching week is an em-dash in the crumb rail | `SUMMER TERM · WEEK — / 39` | `shared/student-live.js:2892`, `:3273-3274` | both | S2 | `ks4comb-class-390.png` |
| A2 | class | Two more em-dash placeholders in the stat block | `PRACTICE —` / `ANSWERED · WK —` | `shared/student-live.js:2892` | both | S2 | `ks4comb-class-390.png` |
| A3 | class | The teacher chip renders **its own label as its value**, beside an empty avatar circle, whenever the class has other than exactly one teacher | `YOUR TEACHER` (and nothing else) | `shared/student-live.js:2918-2921` | both | S2 | `ks4comb-class-390.png` |
| A4 | class | A shout-out whose `message` is NULL renders as a **blank praise card** — avatar, author, timestamp, no words | `MB` / `MIDE BADMUS · 15 WEEKS AGO` with an empty body | `shared/student-live.js:2684` (`text: s.message \|\| ""`) | both | **S1** | `ks4comb-class-390.png` |
| A5 | class | `LESSONS IN THIS TOPIC` draws a panel containing a bare count and nothing else — no content, no empty-state sentence | `LESSONS IN THIS TOPIC` / `00` | compiled template via `build_student_port.py` | both | S3 | `ks4comb-class-1280.png` |
| A6 | class | `SHOUTOUTS` does the same when the feed is empty | `SHOUTOUTS` / `00` | as A5 | both | S3 | `ks3-class-1280.png` |
| A7 | leaderboard | The two week-step buttons have no accessible name at all (SVG only, no `aria-label`) | `(no label)` ×2 | `shared/leaderboard-live.js` (compiled nav) | both | S3 | `prod-leaderboard-1280.png` |
| **B — wrong, stale or self-contradictory status** |
| B1 | class | The page says the leaderboard has not started, on a page whose own header says 17 pieces of work are marked | `THE LEADERBOARD STARTS WHEN THE FIRST WORK IS MARKED` above/below `17 MARKED` and `MARKED 17` | compiled template + `shared/student-live.js:2813` | both | **S1** | `ks4comb-class-390.png` |
| B2 | class | A null teaching week is silently rendered as **week 1**, so the leaderboard heads itself `WEEK 01 · FINAL` while every work row is W37–W39 | `LEADERBOARD  WEEK 01 · FINAL`, tabs `W01 W02 W03 W04` | `shared/student-live.js:2813` (`boardWeek: weekNo == null ? 1 : weekNo`) | both | **S1** | `ks4comb-class-390.png` |
| B3 | class | The term spine draws 12 blank tiles `01`–`12` under a `DONE / OPEN / MISSED` legend. No tile can match any row, because every row is W37–W39 | `TERM SPINE` / `01`…`12` | `shared/student-live.js:2891` (`currentWeek: weekNo == null ? 0 : weekNo`) | both | S2 | `ks4comb-class-390.png` |
| B4 | class | `SUMMER TERM` on 8 September 2026 | `SUMMER TERM` | `shared/student-live.js:700` | both | S2 | `ks4comb-class-390.png` |
| B5 | leaderboard | The week strip closes its own gaps: non-contiguous weeks are drawn as an even run, so 8–14 May sits directly beside 24–30 Jul | `24–30 APR 60% · 1–7 MAY 60% · 8–14 MAY 80% · 24–30 JUL 87% · 14–20 AUG 100% · 21–27 AUG 98% · 4–10 SEP —` | `shared/leaderboard-live.js` | both | S2 | `prod-leaderboard-1280.png` |
| **C — the aggregated "+N more" mush** |
| — | — | **None found.** Zero matches for `+N more` across 8 pages × 3 personas × 2 viewports, and none on the production leaderboard | — | — | — | — | — |
| **D — controls that do nothing when pressed** (scrolling counted as dead) |
| D1 | class | The `My class` crumb in the header is a button and does nothing | `My class` | compiled template | 1280 | S2 | `ks4comb-class-1280.png` |
| D2 | class | The class chip beside it (`10A`) is a button and does nothing | `10A` | compiled template | 1280 | S2 | `ks4comb-class-1280.png` |
| D3 | class | The whole flashcards card is a button drawn with a `›` affordance; with an empty deck, pressing it changes not one pixel | `FLASHCARDS 00 There is nothing to look back over yet.` `›` | compiled template | 1280 | S3 | `ks4comb-class-390.png` |
| **E — links to a 404** |
| E1 | every page | `/favicon.ico` 404s on every page load. There is no favicon in `mrbadmus_site/` and no `<link rel="icon">` in `index.html` or `leaderboard.html` | *(console)* `Failed to load resource: 404 … /favicon.ico` | absent asset | both | S3 | — |
| — | — | All 15 distinct in-page local links return **200**, including `/3d/`, `/student/settings.html`, `/ks3/index.html` | — | — | — | — | — |
| **F — pages wired past their own config seam** |
| F1 | leaderboard, weekly-challenge, my-challenges, revision | Four pages hardcode the **production** Supabase project and backend and ignore `shared/config.js` entirely, so none of them can be pointed at TEST or at a local backend | leaderboard: `COULD NOT LOAD`; the other three render their **signed-out** gate to a signed-in pupil | `shared/leaderboard-live.js:55-56`; `weekly-challenge.html:303,305`; `my-challenges.html:163,165`; `revision.html:215,300` | both | S2 | `ks4comb-leaderboard-390.png`, `ks4comb-weekly-1280.png` |
| F2 | class, assignment | The backend warm-up ping uses the literal production URL rather than `MrBadmusConfig.BACKEND_URL`, so it CORS-fails and logs on every student page in any non-production world | *(console)* `Access to fetch at 'https://mrbadmus-backend.onrender.com/api/health' … blocked by CORS` | `shared/student-live.js:41` | both | S3 | — |
| F3 | class | `workingAcademicYear()` resolves to a year that finished on 31 Aug 2026, and the page then reports that year's term and weeks as current | *(drives A1, A2, B2, B3, B4)* | `shared/class-entry.js` | both | S2 | — |
| **G — sideways scroll at 390px** |
| G1 | leaderboard | Document `scrollWidth` **525** against a **390** viewport. ⚠️ Confirmed on *loaded production data*, not on the empty local state — the week-strip pill reaches `right=485`, the `BIGGEST CLIMB` stat tile `right=525`, and the results table header runs to `right=779`, i.e. **389px past the edge** | `RANK STUDENT PAPERS MOVE SCORE MARKS TIME` | `shared/leaderboard-ds.css` | 390 | **S1** | `prod-leaderboard-390.png`, `ks4comb-leaderboard-390.png` |
| — | — | class, assignment, classes, claim-confirm, weekly-challenge, my-challenges and revision: **no** overflow at 390. No text clipping detected on any page at either width | — | — | — | — | — |
| **H — faff: meta copy about how the platform works** |
| H1 | class | Instructional micro-copy over a control surface that filters nothing (pairs with B3) | `TAP A WEEK TO FILTER` | compiled template | both | S2 | `ks4comb-class-390.png` |
| H2 | class | The platform explaining its own rule to a child — and the rule is not true on this page (pairs with B1) | `THE LEADERBOARD STARTS WHEN THE FIRST WORK IS MARKED` | compiled template | both | S2 | `ks4comb-class-390.png` |
| **I — stated twice on one page** |
| I1 | class | The term is printed twice — once in the crumb rail, once as the WORK panel's own header | `SUMMER TERM` ×2 | `shared/student-live.js:3273` + compiled template | 1280 | S3 | `ks4comb-class-1280.png` |
| I2 | leaderboard, weekly, my-challenges, revision | The entire navigation is in the text layer twice: the header nav, and the off-canvas drawer, which is laid out (measured `right=1600` at a 1280 viewport) and present in `innerText` while shut. Not a visual duplicate — a duplicate for assistive tech and for any text-based gate | `🏠 Home ⚡ Challenge 🏆 Leaderboard …` ×2 | `shared/nav.css` drawer | both | S3 | `ks4comb-leaderboard-1280.png` |
| **J — duplicated `@font-face`** |
| J1 | leaderboard | **21 `@font-face` rules for 7 faces — each declared three times.** Once in `shared/tokens.css` and *twice inside* `shared/leaderboard-ds.css`, and `leaderboard.html` loads both | *(not rendered)* | `shared/tokens.css:14,22,50,58,66,74,82`; `shared/leaderboard-ds.css:132-207` **and again** `:2037-2086`; loaded at `leaderboard.html:20` and `:26` | both | S2 | — |
| — | — | Every other page in scope declares 7 or 14 faces with **no** duplicate key | — | — | — | — | — |
| **K — console errors** |
| K1 | assignment | A state the file itself documents as normal is logged as an **error** | *(console)* `[student-live] Error: no_current_week` | thrown `shared/student-live.js:3370`, logged `:3973`; the comment at `:3366-3367` reads "a NORMAL state … It means no work is set, not an error" | both | S3 | — |
| — | — | The other console errors observed are E1, F1 and F2 and are not counted twice | — | — | — | — | — |
| **L — the dead end** |
| L1 | class, assignment | `say()` **empties the mount host and appends one centred sentence** — no brand, no nav, no link back, no way out. It is the terminal render for **all eight** states in `SAY`: `generic`, `noClass`, `slow`, `pastYear`, `notMine`, `noPractice`, `noWork`, `workNotSet`. Measured: `student/assignment.html` rendered **10 DOM nodes in total** | `No work has been set for this week yet.` — alone on cream | `shared/student-live.js:115-120`, `SAY` at `:65-85` | both, all 3 personas | **S1** | `ks4comb-assignment-390.png`, `ks4comb-assignment-1280.png` |
| **M — not exercised** |
| M1 | class, assignment | A held / unreleased assignment card could not be tested: **no** assignment on TEST has a `release_at` at all. Recorded as a gap, not a pass | — | — | — | — | — |

**Count by class — A 7 · B 5 · C 0 · D 3 · E 1 · F 3 · G 1 · H 2 · I 2 · J 1 ·
K 1 · L 1 = 26 findings**, plus one unexercised area (M1).

---

## The five worst

1. **L1 — every terminal state on both student pages is a bare sentence with no
   way out.** One `say()` call serves eight different states, and it wipes the
   host. A child whose work has not been set, whose class finished last year, or
   whose page simply failed, lands on one line of text on a cream field with no
   brand, no navigation and no back link. `student/assignment.html` was measured
   at **10 DOM nodes**. This is the single highest-leverage fix on the list
   because one change covers all eight states and both pages.

2. **B1 + B2 + B3 — the class page contradicts itself about weeks and marking.**
   It announces `THE LEADERBOARD STARTS WHEN THE FIRST WORK IS MARKED` directly
   beneath its own `17 MARKED`; it heads the leaderboard `WEEK 01 · FINAL`
   because `boardWeek: weekNo == null ? 1 : weekNo` turns "unknown" into
   "one"; and it draws a 12-tile term spine that cannot match a single one of
   its own W37–W39 rows. Three symptoms, one root: a null teaching week is
   coerced to a plausible number instead of being handled.

3. **F1 — four pages are hardwired to production and ignore `shared/config.js`.**
   `shared/leaderboard-live.js:55-56`, `weekly-challenge.html:303`,
   `my-challenges.html:163` and `revision.html:215` each carry their own literal
   production Supabase URL and (for two of them) their own literal backend URL.
   The config seam exists precisely so a page can be pointed elsewhere; these
   four cannot be, which is why no local or TEST verification of them is
   possible at all today.

4. **G1 — `leaderboard.html` scrolls sideways at 390px**, and the results table
   header runs 389 pixels past the right edge. Confirmed against **loaded
   production data**, so it is not an artefact of an empty state.

5. **A4 — a shout-out with a NULL message renders as a blank praise card.**
   `text: s.message || ""` has no fallback to the `template_key`, so
   `top_of_class` with no message becomes an avatar, a teacher's name, a
   timestamp, and silence. A child is shown a piece of praise with the praise
   missing.

Honourable mention: **J1**, 21 `@font-face` rules for 7 faces on one page.

---

## What I deliberately did **not** report, and why

This matters more than the findings list, because each of these looked exactly
like a defect and is not one. The AFTER pass should not "rediscover" them.

**Nine leaderboard controls that pressed dead were not dead.** In my local world
`leaderboard.html` can only say `COULD NOT LOAD` (F1), and in that state
`This week`, both week arrows, `Foundation`, `Higher`, `Overall`, `Biology`,
`Chemistry` and `Physics` all changed nothing when pressed. Re-driven from
`localhost:5500` — an origin production's CORS allowlist already contains — with
the real public board loaded, **all nine responded**. This is precisely the
"a CORS-blocked page gives a false layout pass" trap, and it would have produced
nine fabricated defects.

**Four `Open menu` buttons and four `×` buttons that pressed dead were not
dead.** The drawer's items are in `innerText` while it is shut (I2), so a text
probe sees no change when it opens; a pixel probe does. And every `×` press had
been made on a fresh mount where the drawer is parked off-canvas at
`right=1600` — pressing a closed drawer's close button is correctly a no-op. Re-
driven with the drawer opened first, `×` closes it on all four pages.

**`ALL 17`, `MARKED 17` and `W01` are active-state no-ops, not dead controls.**
All 17 of 10A's assignments are marked, so `ALL` and `MARKED` select the same
list; `W01` is already the selected leaderboard week. `TO DO 0` — the one that
selects a genuinely different set — does change the page.

**`student/classes.html` is correct.** It showed Hannah `10A` and `10Z Physics`;
`class_members` confirms both, neither with a `left_at` or `deleted_at`.

**Seed-data artefacts are not product defects.** `Welldone` (one word) in a
shoutout, and `WELCOME BACK, T` where a pupil's `first_name` is the single
letter `T`, are both in the fixtures.

**The signed-out nav on the four hardcoded pages is a symptom of F1 in *my*
world, not a live defect.** Those pages look for
`sb-urklkrwevjtlfbwnipjn-auth-token` (production) and my session is a TEST one.
On mrbadmus.com the student's session *is* the production one and the nav will
show their name. The reportable fact is the hardcoding, not the rendering.

---

## Pages I could not fully reach

| Page | Reached? | What was missed, and why |
|---|---|---|
| `student/assignment.html` | Loaded, all 3 personas, both viewports — but **only in its `noWork` state** | No assignment on TEST has any `assignment_questions` rows, and none has a `release_at`, so `/api/class/current-assignment` answers `no_current_week` for every pupil. The answering surface — questions, the answer controls, per-answer save, hand-in — was **not exercised at all**. This is a finding about the TEST fixtures, not a silent gap: TEST needs one released, question-bearing assignment before the AFTER pass, or the same blind spot repeats |
| `leaderboard.html` with data | Reached, but only by leaving my world | It ignores `shared/config.js` (F1), so it had to be driven from `:5500` against production, signed out. **A signed-in leaderboard was never observed** — `YOUR STANDING` and the "auto-land on your own track" behaviour are untested |
| `student/claim-confirm.html` | Loaded — but only its refusal state | It needs a claim token in the query string. With none, it correctly renders `This link can't be used`. The successful-claim path was not driven |
| `weekly-challenge.html`, `my-challenges.html` | Loaded — but only their signed-out gate | Same cause as F1. Their signed-in surfaces were never rendered |
| A held / unreleased assignment card | **Not reached** | M1 — no such row exists on TEST |
| `ks3/**` lesson pages | Not attempted | Out of scope per the brief |

---

## How to reproduce

```bash
# backend — no file in that checkout is modified; EXTRA_CORS_ORIGINS is the seam
cd /Users/midebadmus/Documents/GitHub/mrbadmus---backend
PORT=3336 EXTRA_CORS_ORIGINS=http://localhost:5501 node server.js &

# site
cd <worktree> && python3 build_all.py
cd <worktree>/mrbadmus_site && python3 -m http.server 5501 --bind 127.0.0.1 &

# then, signed in as one of the three pupils above (GoTrue password grant,
# password TestPass!2026), open e.g.
#   http://localhost:5501/student/class.html?api=http://localhost:3336
```

Set the viewport **before** navigating, one browser per persona, sequentially.
