# MRB-336/337 §8 — student pages, the AFTER sweep

Worktree `mrbadmus-worktrees/set-work-v21`, branch `feat/set-work-v21`, on top
of `75abe44ce` — the merge of every lane's work. Unlike the before pass, this
one FIXES. Mide's instruction was *"code should also look through the student
pages and fix everything that needs fixing."*

Companion to `sweep-before.md`, which measured the merge base `44dadd96c` and
found 26 items. Every one of them is answered below as **FIXED**, **NOT FIXED**
(with the reason) or **WAS NOT REAL**, plus what this pass found that the before
pass could not see, plus the regression checks, plus one defect I introduced and
caught.

---

## Headline

| | |
|---|---|
| Before-pass findings answered | **26** — 13 fixed, 7 not fixed (each with a reason), 6 were not real |
| New defects found in this pass | **6**, of which **5 fixed** |
| Defects I introduced | **1**, caught by this pass's own console capture, fixed the same run |
| Regression checks on today's work | **5 of 5 pass** |
| Gates | **7 of 7 green**, none weakened |
| `build_all.py` | **exit 0** |

---

## The world

| | |
|---|---|
| Site | `python3 -m http.server` on **5508**, serving `<worktree>/mrbadmus_site` |
| Backend | the set-work-v21 backend worktree at commit `7490ca9`, started by me as **PORT=3338** with `EXTRA_CORS_ORIGINS=http://localhost:5508` |
| Supabase | TEST `qeppkiswvclkkwbxmlok` |
| URL shape | `http://localhost:5508/<page>?api=http://localhost:3338` |
| Sign-in | real GoTrue password grants handed to the Supabase SDK. No fabricated JWT anywhere |
| Personas | `student1@` (10X1 Biology, KS4 triple higher) · `aiden.cole@` (8X1, KS3) · `hannah.patel@` (10A, KS4 combined higher) |
| Walk | 3 personas × 8 pages × 2 widths = **48 walks**, 48 screenshots, 48 bell presses |

### ⚠️ Why a SECOND backend on 3338 rather than the 3337 I was given

The brief said the new backend was already running on **3337** and not to kill
it. It is also not reachable from a page served on 5508: its CORS allowlist is
`mrbadmus.com`, `www.`, `localhost:3000` and `localhost:5500`, and the running
process carried no `EXTRA_CORS_ORIGINS` (probed: 5500 answers with an
`Access-Control-Allow-Origin`, 5501 and 5508 answer with none). A CORS-blocked
page is the trap the brief itself names — it gives a false layout pass and false
dead controls.

So I started a **second** process from the same backend worktree on **3338**,
with the sanctioned `EXTRA_CORS_ORIGINS` env seam and no edit to backend source.
3337 was never touched. When the coordinator restarted 3337 mid-run at `7490ca9`,
I restarted my own 3338 from the same worktree so I was measuring the same code
— node does not hot-reload, and everything below was re-measured after that.

### ⚠️ The TEST academic year was rolled forward, deliberately

TEST held exactly one `academic_years` row, `2025-26`, which **ended on
31 Aug 2026 — eight days before this sweep**. `workingAcademicYear()` correctly
fell back to it, and everything downstream followed: `currentTeachingWeek`
returned NULL, so `POST /api/teacher/set-work` filed new work with
`academic_week = null`, which no pupil's week list can ever match. **The pupil
answering surface was unreachable for that reason and no other** — which is
exactly why the before pass could not reach it either (its M1).

I rolled that one row to `2026-27`, `2026-09-01 → 2027-08-31`. Every class keeps
its `academic_year_id`, so nothing detached. It is a **fixture repair**, and it
is NOT restored at teardown: putting it back would restore the broken state.

It also dissolves four before-pass findings (A1, A2's second half, B3, B4) which
were consequences of a stale fixture rather than product defects. Each is marked
WAS NOT REAL below with that shown, not asserted.

### The fixture gap, closed through the product

Two assignments were created on 10X1 Biology by signing in as its real teacher
(`teacher@test-rainford.local`) and calling `POST /api/teacher/set-work` — the
product's own path, exercising today's new code. No raw row was seeded.

* `92e79166…` — **released now**, 6 questions, due +4 days
* `99934296…` — **scheduled**, release +2 days, due +5 days

Both removed at teardown with `DELETE /api/teacher/set-work/:id` (HTTP 200,
`already_deleted: false` on each), along with the two superseded ones made
before the year roll. **Re-queried afterwards**: all four `deleted_at` non-null;
the automatic week-2 assignment restored; `schools.assignments_open_from` back
to NULL; zero unread notifications pointing at a deleted assignment. The one
live `Cell Biology %` row left on the class is the May 2026 seed
`25000000-…-0001`, not mine.

---

## ⚠️ `student_controls_drive.py` did NOT run, and this is what stood in for it

`student_controls_drive.py` is the gate that presses every control on every
student screen and reports any whose only effect is a scroll. **It could not run
in this session**: it defaults to `MRB_DRIVE_EMAIL=midebolabadmus@gmail.com`
(its line 99) — Mide's own account on PRODUCTION — and this run may not use a
production credential for his account. No TEST identity is wired into it.

It exists because five controls once shipped dead, and the other three student
gates structurally cannot see that class of defect: parity checks the page
LOOKS right, behaviour checks a scripted sequence produces the right TEXT, the
page drive checks the DATA is real. None asks *"I pressed it — did it do what it
says?"*

Its questions were asked here instead, against TEST, in two files:

* `sweep_after_drive.py` — the walk, and the **bell on every surface**
* a control sweep that presses **every** button and link on the class page on a
  fresh mount each, comparing a signature that **deliberately excludes scroll
  offset**, so a control whose only effect is a scroll reads DEAD

Its two rules were kept: **scrolling counts as dead**, and **a control that
reports nothing is often correct** — an active filter chip, the current view's
own crumb. Candidates were judged, not asserted.

### The bell — pressed on every surface that has one, at both widths

| surface | bell | opens | rows | panel width 390 / 1280 | Escape closes | Close closes |
|---|---|---|---|---|---|---|
| `student/class.html` | yes | ✅ | 0–3 | 366 / 380 | ✅ | ✅ |
| `student/assignment.html` | yes | ✅ | 0–3 | 366 / 380 | ✅ | ✅ |
| `student/classes.html` | yes | ✅ | 0–3 | 366 / 380 | ✅ | ✅ |
| `leaderboard.html` | yes | ✅ | 0–3 | 366 / 380 | ✅ | ✅ |
| `weekly-challenge.html` | yes | ✅ | 0–3 | 366 / 380 | ✅ | ✅ |
| `my-challenges.html` | yes | ✅ | 0–3 | 366 / 380 | ✅ | ✅ |
| `revision.html` | yes | ✅ | 0–3 | 366 / 380 | ✅ | ✅ |
| `student/claim-confirm.html` | **absent** | — | — | — | — | — |

48 presses, 48 opens, zero dead. The panel's own controls — `Close` and Escape —
were pressed on every one of them and both closed it every time. Row counts
track the persona (Hannah 3, Aiden 0, and `student1` 1 while the released
fixture stood, 0 after it was deleted), which is the badge, the panel and the
banner agreeing rather than three independent numbers.

`claim-confirm.html` having no bell is **correct**: it is the pre-authentication
claim page and there is no signed-in student to have messages.

### The class page's 41 controls, pressed one at a time

Nine reported nothing. Judged:

| control | verdict |
|---|---|
| `My class`, `10X1 Biology` | **correct** — the crumb and chip naming the view you are already on |
| `ALL 6` | **correct** — the already-active filter chip |
| `W02` | **correct** — the already-selected leaderboard week |
| flashcards card, empty deck | **correct** — `openCards` refuses to open an empty overlay; a ruled refusal, not a dead control |
| **the four `Lessons in this topic` cards** | **REAL, AND FIXED** — see N2 |

---

## Every before-pass finding, answered

### FIXED (13)

| # | What it was | What I changed |
|---|---|---|
| **L1** | `say()` emptied the mount host and left one sentence on cream — no brand, no nav, no way out, for **all eight** `SAY` states on both pages. `student/assignment.html` measured **10 DOM nodes in total** | `shared/student-live.js` — `say()` now keeps page chrome: a header carrying **Design's own `MrBadmusDS.BrandMark`**, read out of `window.__MRB_TPL__.imports` (the same string the compiled header renders — not an SVG retyped here), the `MrBadmusAI` wordmark linking to `/student/classes.html`, and one exit link under the message: `Your class` → `/student/class.html` on the assignment page, `Your classes` → `/student/classes.html` on the class page. **Measured after: 34 nodes, brand SVG present, both links present, at 390 and 1280.** It still cannot survive the mount — it appends into the host after clearing it, exactly as before — so the boot line's guarantee is untouched |
| **B2** | `boardWeek: weekNo == null ? 1 : weekNo` — "unknown week" rendered as **week 1**, heading the board `WEEK 01 · FINAL` over rows from another week and lighting the `W01` tab | `shared/student-live.js` — `boardWeek` and `currentWeek` both carry **null**, not a fabricated number. They are compared against each other by the template's `boardScopeNote`, and coercing them to *different* numbers (1 and 0) is what produced the `FINAL` branch. Null keeps them in step: the note reads `CURRENT WEEK` and no tab claims to be selected. Every other consumer is `<=` or `===` against a week number, and null fails both exactly as nought did. **Measured after: `CURRENT WEEK`** |
| **B1 / H2** | `THE LEADERBOARD STARTS WHEN THE FIRST WORK IS MARKED`, printed directly under the page's own `17 MARKED` — and false: `roster`/`weekPts` are RULED empty because no per-student per-week points series exists anywhere, so the board is empty for every class however much work is marked | A new, narrow ruling mechanism — `SET_TEXT` in `student_rulings.py`, applied in `build_student_port.py`, which asserts Design's old string byte for byte and refuses a node with anything but one text child. The line now reads **"There is nothing to show here yet"** — the words this page already uses one panel over for the empty flashcard deck, so a student meets one voice. It says nothing about marking, nothing about leaderboards starting, and nothing about the software (CLAUDE.md §8.10) |
| **F1** | Four pages hardcoded the production Supabase project and backend and ignored `shared/config.js`, so none could be pointed at TEST — which is why none had ever been verified anywhere but live, and why a signed-in pupil saw the **signed-out gate** | `shared/leaderboard-live.js` (⚠️ read **lazily** through `backendUrl()`/`supabaseUrl()`/`anonKey()`, because `leaderboard.html` loads `config.js` with `defer` and this file without one — capturing at parse would have taken the fallback every time and *looked* fixed); `weekly-challenge.html`, `my-challenges.html`, `revision.html` (config.js is undeferred above them, so a direct read is safe). `revision.html`'s `localStorage` session key followed too — it named the production **project ref**, so it could never find a test session. Production literals stay as the fallback everywhere; on mrbadmus.com `config.js` resolves to the same values, so nothing about the live pages changes. **Measured after: `weekly-challenge.html` renders the signed-in surface — "You're taking: Combined Higher" — where it previously showed the signed-out gate** |
| **F2** | The backend warm-up ping used the literal production URL, so it CORS-failed and logged on every student page in any non-production world — and warmed the wrong dyno | `shared/student-live.js` — the ping **moved** rather than being rewritten. `config.js` is `DEPS[0]` and is not on the page where the ping was written, so `MrBadmusConfig` cannot be read there; it now fires the instant `config.js` lands, still inside the first milliseconds and still ahead of every Supabase round trip. Fire and forget exactly as before. **Measured after: zero console errors on the student pages** |
| **G1** | `leaderboard.html` document `scrollWidth` **525** against a 390 viewport | `build_leaderboard_port.py` **R35**, two causes measured separately. (1) The stats row is `repeat(4, 1fr)`, and `1fr` floors each track at its content's min-content width — `FASTEST PAPER` cannot fold into 76px, so the grid refused to shrink below 497 inside a 334 container. Now two columns below 720px, four at and above it (`gridTemplateColumns` measured `160px 160px` at 390 and `295.5px ×4` at 1280, so R31/R34's widths are untouched). (2) The ranked table is a nine-track 750px grid inside a 332px frame whose `overflow: hidden` clips its own radius — **SCORE, MARKS and TIME were simply not on the page** and no gesture reached them. `overflow-x` is now `auto` with `overflow-y` held at `hidden`, so the radius still clips. **Measured after: document scrollWidth 390 at a 390 viewport; the frame scrolls (`scrollLeft` 0 → 200, scrollWidth 750 vs clientWidth 332)** |
| **A4** | A shout-out whose `message` is NULL rendered as a **blank praise card** — avatar, teacher's name, timestamp, silence — because `text: s.message \|\| ""` had no fallback | `shared/student-live.js` — falls back to the template's label, read from `window.MrBadmusShoutouts.templateByKey()`. ⚠️ **Not a seventh copy of the six labels**: `shared/shoutouts.js` is the locked enum mirroring `class_shoutouts_template_key_chk`, `shared/teacher-live.js` already reads them from exactly there, and so does this. It joins `DEPS` (last, in the same parallel wave, not in series) and `STAMPED_DEPS` in `build_student_port.py`, since `/shared/*` is served `immutable, max-age=31536000` and an unstamped file is a year-long pin. A card that still ends up with no words is dropped rather than drawn empty |
| **J1** | `leaderboard.html` loaded **21 `@font-face` rules for 7 faces** | `dedupe_faces()` in `build_student_port.py`, imported by `build_leaderboard_port.py` — **one** implementation, because both builds assemble the same six sheets from Design's delivery and both had the same duplication. Two of her sheets declare the same seven faces. **Measured after: `leaderboard-ds.css` and `student-ds.css` 7 each**; the leaderboard page's total is 14 (its own 7 plus the site's `shared/tokens.css` link), which is what every other page in the estate carries |
| **A7** | The two leaderboard week-step buttons had **no accessible name at all** — one `aria-hidden` chevron each, so a screen reader announces "button" twice on the control that moves the board through time | `build_leaderboard_port.py` **R36** — `aria-label` `Earlier weeks` / `Later weeks`, anchored on Design's own handler names `scrollBack`/`scrollFwd` rather than node indices, because a handler name is what a control MEANS. Nothing visible changes; the chevrons stay `aria-hidden`, which is now right rather than merely quiet |
| **K1** | `[student-live] Error: no_current_week` logged as a console **error** on a state the file itself documents as normal — "It means no work is set, not an error" | `shared/student-live.js` — an error carrying `mrbSay` is a state this file CHOSE to show, and goes to `console.info`; only the ones it did not choose stay `console.error` |
| **A1 / A2** (first half) | `SUMMER TERM · WEEK — / 39`, `ANSWERED · WK —` | Dissolved by the fixture repair — the week is real. **Measured after: `WK 02 / 39`, `ANSWERED · WK 02`, `AUTUMN TERM`.** The remaining `PRACTICE —` is *not* a defect: see NOT FIXED |
| **A5** | `LESSONS IN THIS TOPIC` drew a panel with a bare `00` and nothing else | Dissolved: with a real assignment the panel lists its four lessons. It was an empty-state artefact of a world with no live work |
| **H1** | `TAP A WEEK TO FILTER` over a spine that filtered nothing | Now true. All twelve term-spine tiles were pressed individually and all twelve changed the page |

### NOT FIXED, and why (7)

| # | What it is | Why it stands |
|---|---|---|
| **A2** (`PRACTICE —`) | The practice tile's value is an em-dash | **Honest, not empty.** `practiceAnswered` is a ruled COULD-NOT-SOURCE — nothing records how many practice questions a student answered in a week — and the template falls back to `dash`, the **same glyph the neighbouring tiles use** for a missing value (`avg == null ? dash`). Replacing it with `0` would state something false. The caption beside it now reads a real week |
| **A3** | The teacher chip renders its own label `YOUR TEACHER` as its value, beside an empty avatar, whenever a class has other than exactly one teacher | Genuinely ambiguous and **Mide's call, not mine.** The RPC `class_teachers_for_viewer` returns names WITHOUT ids, so on a co-taught class there is no way to say which teacher this chip means, and picking the first would put a name in front of a child that may not be theirs — the existing ruling says so and it is right. What a co-taught class's chip should show (both names? the word "teachers"? no chip?) is a design decision. On a singly-taught class it is already correct: 10X1 shows `SARAH WHITFIELD` |
| **A6** | `SHOUTOUTS 00` — a heading and a bare count with no empty-state sentence | Real but cosmetic, and it is Design's drawn empty branch rather than a data fault. Writing a sentence into it is new prose on a student surface, which is out of scope for a sweep |
| **B5** | The leaderboard's week strip closes its own gaps — non-contiguous weeks are drawn as an even run, so 8–14 May sits beside 24–30 Jul | The strip renders the weeks the payload contains. Whether a gap should be drawn as a gap is a design decision about a control Mide has already ruled on twice (R28/R33), and it needs data (which weeks *should* exist) that the endpoint does not send |
| **E1** | `/favicon.ico` 404s on every page of the site | The site has no favicon at all and no `<link rel="icon">`. Adding one is a **brand asset decision** — CLAUDE.md pins four brand presentations and none of them names a favicon — and it would touch every page the KS4 generator writes, not just the student ones |
| **I1** | The term is printed twice at 1280 — once in the crumb rail (`AUTUMN TERM · WEEK 02 / 39`) and once as the WORK panel's own header | Both are Design's, both are correct in their own right, and at 390 the crumb takes its narrow form (`WK 02 / 39`) so there is no duplicate at all. Cutting either is a layout decision |
| **I2** | The whole navigation is in the text layer twice — the header nav and the off-canvas drawer, which is laid out and present in `innerText` while shut | Structural to `shared/nav.css`'s drawer, shared with every public page on the site including the 865 KS4 lesson pages. Fixing it properly (`inert`, or `visibility:hidden` while closed) is a nav change that deserves its own unit and the KS4 gates |

### WAS NOT REAL (6)

| # | Reported as | What it actually was |
|---|---|---|
| **B3** | A 12-tile term spine no row could match, because every row was W37–W39 | A consequence of the stale TEST academic year. With the year current, rows are W01/W02 and tile `02` matches. The 12-vs-39 tile count is Design's drawing, unchanged and not a defect |
| **B4** | `SUMMER TERM` on 8 September | Same cause. `termLabelFrom` reads the academic year's own dates; against a year starting 2025-09-01 it correctly answers SUMMER for September 2026. Against the current year it answers **AUTUMN TERM**, measured |
| **F3** | `workingAcademicYear()` resolves to a year that finished on 31 Aug 2026 | The helper's documented **fallback**, behaving exactly as specified when no unfinished year exists. The fault was the fixture having only one year, not the resolution |
| **D1 / D2** | The `My class` crumb and the class chip are dead | Both name the view you are already on. The controls-drive's own rule: a control that reports nothing is often correct |
| **D3** | The flashcards card is dead | With an empty deck, `openCards` refuses to open an empty overlay — a ruled refusal recorded in `student_rulings.py`. With a real deck (KS3 persona, 29 cards) the card is live |
| **M1** | A held/unreleased assignment card could not be tested | Now testable and tested — see the regression checks. Recorded here because the before pass recorded it as a gap, and the gap is closed |

---

## New in this pass (6 found, 5 fixed)

The before pass could not sign in on four of the eight pages (F1), could not
reach the answering surface at all, and had no released or scheduled work to
look at. All six of these live in that blind spot.

| # | Page | What it is | Status |
|---|---|---|---|
| **N1** | every page loading `shared/nav.js` | The nav's auth check read `localStorage['sb-urklkrwevjtlfbwnipjn-auth-token']` and its own hardcoded production Supabase URL. **On any world but the live one it could not find a signed-in student at all** and drew `Sign In / Sign Up` over the head of a pupil who was signed in. Same class as F1, and it is what made F1's symptom look like four separate page bugs | **FIXED** — `shared/nav.js` reads `MrBadmusConfig` and derives the session key from the configured project ref, the same derivation `shared/student-bell.js` already uses. Production literals remain the fallback |
| **N2** | `student/class.html` | **All four `Lessons in this topic` cards scroll the page to the top when tapped, on every KS4 class.** The 22 Aug ruling that fixed this left one branch live: `open` read `if (!l.href) { return; }` *before* `preventDefault`, so a card with no page returned and Design's `href="#top"` fired. `lessonHref` resolves against `MRB_KS3_LESSONS` only, so **every** KS4 lesson card takes that branch. This is the exact defect class the controls-drive exists for, and the controls-drive could not run | **FIXED** — `student_rulings.py`: the guard moves below the `preventDefault`. ⚠️ The card is now inert rather than live; giving KS4 lessons real URLs is the product fix and is separate work, because the two key stages share **eight byte-identical subtopic slugs** (MRB-332) so it needs its own map and a key-stage argument, never one index keyed on the slug alone |
| **N3** | leaderboard, weekly, my-challenges, revision | `shared/nav.js` fetches the avatar from a hardcoded `https://mrbadmus-backend.onrender.com/api/profile`. It is only reached once a session has been FOUND, so while N1 stood it could never run outside production — fixing N1 exposed it, as a red CORS line on every page carrying the nav | **FIXED** — through `MrBadmusConfig.BACKEND_URL`, production literal as fallback |
| **N4** | `student/class.html`, `student/assignment.html` | Student pages carried **14 `@font-face` rules for 7 faces**, four keys duplicated — the same duplication as J1, in `student-ds.css`, which the before pass's "every other page declares 7 or 14 with no duplicate key" had counted as normal | **FIXED** by the same shared `dedupe_faces()` |
| **N5** | leaderboard, weekly, my-challenges, revision | At 390px the nav cluster reaches **395.3px** for a long display name, giving ~5px of sideways scroll. Cause: `shared/nav.js` builds the chip's name from `user_metadata.first_name` and falls back to **the whole email local part** — `👤 aiden.cole` — and `.nav-cluster` does not shrink. Invisible to the before pass because it never had a signed-in nav on these pages | **NOT FIXED, deliberately.** The correct fix is two things — nav.js reading `profiles.first_name` (which it already fetches, one line away) and an ellipsis cap on the chip — and both are in `shared/nav.js`/`shared/nav.css`, loaded by ~900 KS4 pages whose gates are not in this unit's set. 5px, driven by a name shape TEST produces and production mostly does not. It deserves its own unit, and the diagnosis above is the whole of it |
| **N6** | TEST only | `/api/weekly-leaderboard/board` and `/api/weekly-scores/history` answer **500** on TEST: `PGRST205`, the weekly-challenge tables do not exist on that project. Not a product defect; it is why `leaderboard.html` reads `COULD NOT LOAD` in this world. `student1`'s `/u` avatar 404 and its `first_name` of `T` are seed values, likewise | **not a defect** — recorded so the next pass does not rediscover it |

---

## ⚠️ A defect I introduced, and caught

**The first version of `dedupe_faces()` kept the FIRST declaration of each face
and broke the font on every student page.**

`tokens/src-styles-tokens.css` declares its seven faces with
`url('../fonts/…')`, which from `/shared/student-ds.css` resolves to `/fonts/…`
and 404s; `fonts/fonts.css` is the copy whose `./` this build rewrites to the
served path. Keeping the first threw away the working URL and kept the broken
one. **No error appeared on the page** — the browser simply fell back to a
system font. No gate watches it. It surfaced only because this sweep captures
the console on every walk: `404 /fonts/instrument-sans-var-latin.woff2`.

Fixed by keeping the **LAST** declaration, which is a rendering no-op by
construction — identical `@font-face` descriptors do not merge, the later rule
is the one the browser already used, so keeping it deletes only rules that were
already being overridden. And the build now **refuses** a surviving face whose
`src` is not an absolute site path, so this cannot recur silently.

Measured after: `student-ds.css` — 7 faces, all `url('/shared/fonts/…')`, and
zero font 404s across all 48 walks.

---

## The regression checks on today's work

Driven as `student1@test-rainford.local` on 10X1 Biology, at 390px, one world
state at a time.

| # | Claim | Result |
|---|---|---|
| 1 | **A teacher-set assignment released NOW reaches the pupil even though the school hold is in the future** | ✅ With `assignments_open_from = 2026-09-14`, `Cell Biology check-in` is in the pupil's work list, and the bell says `Messages, 1 unread` with the panel row `NEW WORK · Your teacher set you "Cell Biology check-in"` |
| 2 | **A SCHEDULED assignment is not visible and cannot be reached by its id** | ✅ Absent from the page; `/student/assignment.html?assignment=99934296…` refuses with `No work has been set for this week yet.` |
| 3 | **A DELETED assignment disappears from the page, the bell and the banner** | ✅ After `DELETE /api/teacher/set-work/:id`: bench empty, no title on the page, bell label back to plain `Messages` with **no badge**, panel `No messages` with 0 rows, no banner. Its id refuses like the scheduled one |
| 4 | **The bell badge, the panel and the top banner agree on one count** | ✅ Badge `1` ↔ panel 1 row ↔ label `Messages, 1 unread`; and after the delete, badge empty ↔ 0 rows ↔ `Messages`. Across all 48 walks the row count tracked the persona and never disagreed with the badge |
| 5 | **Still-open work does not fall off the bench when the teaching week rolls** (the coordinator's mid-run fix) | ✅ Proven on both halves. Server: with the row stamped `academic_week = 1` and the class in week 2, `/api/class/current-assignment` returns `week: 2` and `week_work` containing `Cell Biology check-in wk=1`. Client: with no automatic assignment in the slot, the class page draws **`ON THE BENCH NOW · DUE SAT 12 SEP · Cell Biology check-in`** — the carried-over row, in the wrong week, on the bench |

### What I changed for check 5, and why it is a removal

`shared/student-live.js` re-checked the week itself:

```js
if (current.week != null && w.academic_week != null
    && w.academic_week !== current.week) { return false; }
```

That is now **removed**, not widened. Every clause of the server's new rule
(`academic_week = week OR (release_at <= now AND due_at > now)`) is already
enforced line for line in the same filter — the release gate on the next line,
`card.is_submitted` and `card.due_at < serverNow` two lines after it, and
membership of `cards`, which is the student's own RLS-filtered read, before
either. Restating the server's disjunction here would be a second
implementation of one decision, and the two would drift on the first change to
either. What is left can only narrow `week_work` on facts the client can see for
itself; it can no longer overturn an inclusion the server made deliberately.

Safe in either deploy order: an older backend's `week_work` is week-filtered
already, so on that payload the removal changes nothing.

⚠️ Framed as the coordinator asked: this was a **demotion, not a
disappearance**. The work list is not week-scoped — `shared/student-data.js`
reads every undeleted assignment for the class and buckets by `due_at` — so the
work stayed reachable in the cards list throughout. What was lost was the
prominent "do this now" card.

---

## Gates

Every gate re-run on the final tree. **None weakened.**

| gate | result |
|---|---|
| `python3 build_all.py` | **exit 0** |
| `student_behaviour` | **PASS** — every drive produces the same visible text and the same controls on the ported page as on Design's own |
| `student_parity` | **PASS** — both previews reproduce Design's file exactly at 360/390/820/1460 |
| `student_themes` | **PASS** — seven cases, all 21 contrast figures clear AA 4.5 |
| `student_switches` | **PASS** |
| `leaderboard_behaviour` | **PASS** |
| `leaderboard_tells` | **PASS** — no invented handle, no fabricator, PRNG budget intact |
| `leaderboard_seam` | **PASS** |
| `student_controls_drive` | **DID NOT RUN** — production credential for Mide's account; substituted as described above |

---

## Files changed

| file | what |
|---|---|
| `shared/student-live.js` | `say()` keeps page chrome (L1) · `boardWeek`/`currentWeek` carry null (B2) · shoutout template fallback (A4) · `shoutouts.js` joins `DEPS` · health ping moved behind `config.js` (F2) · normal states log as info (K1) · the bench week re-check removed |
| `shared/nav.js` | session key + Supabase URL + avatar fetch through `config.js` (N1, N3) |
| `shared/leaderboard-live.js` | backend and Supabase read lazily through `config.js` (F1) |
| `weekly-challenge.html`, `my-challenges.html`, `revision.html` | through `config.js`; revision's session key follows the project ref (F1) |
| `student_rulings.py` | new `SET_TEXT` register + the leaderboard empty-state line (B1/H2) · lesson-card `preventDefault` (N2) |
| `build_student_port.py` | applies `SET_TEXT` · `dedupe_faces()` + its absolute-src assertion (J1/N4) · `shoutouts.js` in `STAMPED_DEPS` |
| `build_leaderboard_port.py` | R35 phone width (G1) · R36 rail-step labels (A7) · imports `dedupe_faces` |
| `sweep_after_drive.py`, `sweep_after_regress.py` | new — the walk, the bell sweep and the five regression checks |
| `docs/mrb336/sweep-after.md`, `sweep-after.json`, `regress-*.json`, `shots-after/` | this report and its evidence |

## Reproducing

```bash
# backend — a SECOND process, on its own port; 3337 is not touched
cd /Users/midebadmus/Documents/GitHub/mrbadmus-backend-worktrees/set-work-v21
PORT=3338 EXTRA_CORS_ORIGINS=http://localhost:5508 node server.js &

cd <worktree> && python3 build_all.py
python3 sweep_after_drive.py            # 48 walks, 48 bell presses, 48 shots
python3 sweep_after_regress.py hold     # one world state per run
```

Set the viewport **before** navigating, one browser per persona, sequentially,
and pass an explicit width to every `screenshot()` — it resets the viewport to
1280×900 (`ks3_browser.py:577`).
