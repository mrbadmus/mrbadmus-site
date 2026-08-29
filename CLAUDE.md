# CLAUDE.md — MrBadmusAI Frontend Project Guide

This file gives Claude Code (the AI assistant) everything it needs to understand this project and work on it effectively.

---

## AUTONOMY CONTRACT — applies to every session, overrides any cautious instinct

Default: ACT. You have authority to investigate, decide, fix, and continue. When something is
wrong, missing, or unexpected, your first move is to SOLVE IT — dig for the root cause, fix it
properly, verify the fix, note it, carry on. Do not stop to ask.

A stop costs a full human round trip and Mide's attention. Treat it as expensive. Never use a
stop as a substitute for thinking harder.

### Stop ONLY for these three
1. **Irreversible loss** — an action that would destroy data, history, or work that cannot be
   recovered (force-push, dropping a table, deleting uncommitted work, wiping an OAuth token).
2. **Science or content accuracy** — whether GCSE science is correct, or whether AQA would credit
   a given answer. Mide is examiner-qualified; this is his sole gate.
3. **Genuinely blocked** — you have tried at least two substantively different approaches and
   cannot proceed. Say what you tried and why each failed.

**Pushing is NOT one of them.** See below.

### Everything else, you handle
- Missing prerequisite → create it, use it, remove it if it was temporary
- A test can't run as specified → find an equivalent that proves the same property, and say so
- Unexpected state → investigate, explain it in the report, proceed
- Unspecified design detail → choose what's most consistent with the existing system, state the choice
- Small adjacent defect spotted in passing → fix it, note it
- Ambiguous scope → take the reading that best serves the student, state it
- Something in the prompt is wrong or impossible → do the right thing instead, and say what you changed

### Push authorisation is STANDING and PERMANENT ⊕ (MRB-228, 16 Aug 2026)

**You push. `git push origin main` from the terminal is authorised, always, and needs no
per-run permission.** The remote is SSH and works without intervention.

This used to say the opposite — production deploy was a stop-for item, and several other places
in this file still said "GitHub Desktop only". That was true when the repo had no working SSH
key from a terminal session and pushing genuinely required Mide. It stopped being true on
15 Aug 2026, and the stale instruction then cost real work: sessions reached the end of a long
build, stopped at the push, and a session limit killed one of them with everything unshipped.

The rule that replaces it is a SHIPPING rule, and it matters more than the old one did:

> **One unit is one commit and one push.** Finish a unit, run its gates, commit, push, verify
> live. Never carry two units' work in an uncommitted tree. Assume you will be interrupted —
> what has shipped has shipped, and the next session resumes at a clean boundary.

What still binds:
- **A red gate means no commit and no push for that unit.** Never weaken a gate to make
  something pass. A failing gate is a finding, not an obstacle.
- **Verify live after pushing** — `./check_ks3_live.sh` for KS3. Check the cache-bust stamps,
  not just the status code: a 200 carrying stale assets is the failure mode that looks like
  success. Pin the stamps from the committed build, not the working tree.
- **Force-push is still a stop.** It is item 1 above, and it always was.
- If a live check fails, report it — do not revert unilaterally.

### Deviations go in the report, not mid-run
Where you'd have stopped, write one line at the end instead:
"Deviation: [what was unexpected] → [what I did] → [why]."
Mide reads deviations once, at the end, alongside everything else.

### The judgement standard
Ask: "would a competent senior engineer with full context stop here, or just handle it?" If they'd
handle it, handle it. Reserve interruption for things that are genuinely Mide's call, not things
that are merely uncertain.

---

## What is MrBadmusAI?

MrBadmusAI is a free GCSE Science revision website for UK secondary school students. It covers all three AQA sciences — Physics (spec 8463), Chemistry (spec 8462), and Biology (spec 8461) — at both Foundation and Higher tier, across Combined Science and Triple Science pathways.

The site features:
- Topic notes and subtopic pages for every AQA spec point
- A live AI tutor chat (powered by Claude via a backend API)
- A weekly challenge system with a leaderboard (Champion of the Week + per-track leaderboards)
- Past paper links
- User accounts (sign up / sign in) with personalised profiles

The name "MrBadmus" refers to Mide Badmus, the teacher who built this site for his students. Over 135 students actively use it.

---

## Tech Stack

| What | How |
|---|---|
| **Frontend** | Plain HTML, CSS, and vanilla JavaScript — no React, no framework |
| **Styling** | A single shared stylesheet: `shared/styles.css` |
| **AI chat engine** | `shared/mrbadmus.v2.js` — one JavaScript file shared across all pages |
| **AI model** | Claude (Anthropic) — accessed via a custom backend |
| **Backend API** | Separate Node/Express server at `https://mrbadmus-backend.onrender.com` — lives in a separate repo |
| **Auth & database** | Supabase — handles user sign-in, session tokens, profiles, and leaderboard data (project ID `urklkrwevjtlfbwnipjn`) |
| **Site generation** | **`build_all.py`** — the entry point. It runs FOUR generators in a load-bearing order: `generate_site_v5.py` (KS4), `build_ks3.py` (KS3), `build_student.py` (previews), then `build_student_port.py` (**the live student pages**). ⚠️ `generate_site_v5.py` alone does NOT build KS3 — see "How the Site is Generated" below |
| **Hosting** | Cloudflare Pages at mrbadmus.com (auto-deploys from GitHub) |
| **Email** | Resend.com from noreply@mrbadmus.com |

---

## Brand presentation rule

The site has FOUR brand presentations. Always check which applies before adding nav markup to a new page.

**Why:** External pages need a visible brand for prospective students, parents, and schools (first impression, marketing). STAFF surfaces stay clean and utilitarian — they're working instruments for authenticated adults, no marketing surface needed. KS3 pages take Claude Design's mark (MRB-197, ruled by Mide) — the same key-stage split already ruled for the palette under MRB-183. STUDENT surfaces take Design's mark too (MRB-197 extended, 20 Aug 2026): a student's class page is the product, and it is continuous with the KS3 lesson pages the same student has been reading all term.

| Surface | Brand markup |
|---|---|
| **KS4 CHROME pages** ⊕ | Claude Design's `BrandMark`: a right-pointing **double** chevron in `#E4572E` (second chevron at `stroke-opacity="0.34"`, stroke-width 3.4, viewBox `0 0 22 22`) **+** "MrBadmusAI" in Bricolage Grotesque 800. Emitted by `nav_html(chrome=True)` in `generate_site_v5.py`, styled by `shared/ks4-chrome.css`. Applies to the seven pages of the front-door journey: `index.html`, `ks4.html`, `{combined,triple}/index.html`, the four tier pages, the twelve subject hubs and all 98 topic pages. |
| **Other external / public pages (KS4 + root)** | Gold-to-rust two-chevron SVG **+** "MrBadmusAI" text. Uses `nav-brand` + `brand-logo` classes from `shared/styles.css`. Applies to: `auth.html`, `leaderboard.html`, `past-papers.html`, `weekly-challenge.html`, `my-challenges.html`, `revision.html`, every KS4 **lesson** (subtopic) page, and any future external/public page **outside KS3** that is not part of the KS4 chrome. |
| **KS3 pages** | Claude Design's mark: a single bold `#E4572E` chevron + "MrBadmusAI" wordmark in Bricolage Grotesque 800, exactly as drawn in the frozen reference (`docs/ks3/design-reference/`). Emitted by `build_ks3.py` (`NAV_BRAND`), styled by `.ks3-brand` in `shared/ks3.css`. Never hand-copy it onto a page — KS3 pages are generated. |
| **Student surfaces** | Claude Design's `BrandMark`: a right-pointing **double** chevron in `#E4572E` (the second chevron at `stroke-opacity="0.34"`) **+** "MrBadmusAI" in Bricolage Grotesque 600. Drawn by Design in the 19 Aug 2026 student delivery; emitted by `build_student.py` from that delivery. Applies to: `student/class.html`, `student/assignment.html` and every future student-facing page. ⚠️ This is NOT the same drawing as the KS3 lessons' mark — that one is a single *upward* chevron at stroke-width 4.6. Both are Design's, both `#E4572E`, both carry the wordmark; they are not interchangeable, and neither is hand-copied (both are generated). |
| **Staff / school-operations pages** | Plain white text "MrBadmusAI", **no logo asset**, with the exact styling pinned below. Applies to: all `/teacher/*`, `/admin/*` and `/hod/*` pages, and all current/future HoD / SLT / admin dashboards. |

### ⊕ MRB-301, 29 Aug 2026 — the external row SPLIT in two

There used to be one external row, and it read: *"Gold-to-rust two-chevron
SVG + 'MrBadmusAI' text … Applies to: `index.html`, `auth.html`,
`combined/index.html`, `triple/index.html`, all generator-output KS4 topic
pages, and any future external/public page outside KS3."*

It is kept here rather than deleted because it named `index.html` and the KS4
topic pages explicitly, and following it on one of those pages now would
UNDO the port.

**What changed.** MRB-301 landed Claude Design's chrome redesign on the front
door and the whole KS4 navigation journey — landing, GCSE hub, pathway, tier,
subject picker, topic list, topic page. Design drew those with her own
`BrandMark`, the same double chevron the student surfaces have carried since
MRB-197, and Mide's instruction for the run was to keep it.

**What did NOT change, and why the row had to split rather than move.** The
KS4 **lesson** pages are a separate run. They still load `shared/nav.css` and
still render `nav_html()`'s default branch, so they still wear the gold-to-rust
chevron — as do `auth.html`, `leaderboard.html` and the other hand-written
root pages, none of which MRB-301 was allowed to touch. Rewriting the single
row in place would have declared those pages non-conformant overnight.

So the site currently has TWO external marks, deliberately, for the length of
one run. When the lesson pages are ported, the two rows collapse back into one
and the gold-to-rust chevron retires with them. ⚠️ Until then, do not "fix"
a lesson page's brand to match the chrome: that is the seam, not drift.

⚠️ `build_leaderboard_port.py` used to lift its nav out of `index.html`
verbatim (Mide's MRB-290 R1). It now reads `generate_site_v5.nav_html()`
instead, so the leaderboard keeps the classic nav while the chrome wears
Design's. That is an OPEN item on Mide, written up in the MRB-301 report.

### Canonical KS4-chrome brand markup

This one is GENERATED — `nav_html(chrome=True)`. Never hand-copy it onto a
page; a chrome page is a generator output, exactly like a KS3 page.

### Canonical external chevron markup (KS4 lesson + root — NOT KS3, NOT KS4 chrome)

Copy this verbatim into the nav of any external page outside KS3:

```html
<a class="nav-brand" href="/index.html"><svg class="brand-logo" width="22" height="22" viewBox="0 0 24 24" fill="none"><path d="M4 6l4-4 4 4" stroke="url(#navGrad)" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/><path d="M4 6l4-4 4 4" stroke="url(#navGrad)" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" transform="translate(4,6)"/><defs><linearGradient id="navGrad" x1="4" y1="2" x2="16" y2="12" gradientUnits="userSpaceOnUse"><stop stop-color="#FFD93D"/><stop offset="1" stop-color="#FF6B35"/></linearGradient></defs></svg> MrBadmusAI</a>
```

Requires `shared/styles.css` to be loaded (for `.nav-brand` + `.brand-logo`).

### Canonical staff text markup

Copy this verbatim into the nav of any staff / school-operations page:

```html
<a href="/index.html" style="font-family:'Sora',sans-serif;font-weight:700;font-size:1.2rem;color:var(--text);text-decoration:none;letter-spacing:0.01em;">MrBadmusAI</a>
```

No stylesheet dependency — fully inline-styled. This is the canonical staff brand styling — match it exactly on every new staff page.

### ⊕ Superseded 20 Aug 2026 (MRB-197 extended) — the student/staff fork

The staff row above used to read *"Dashboards / school-operations pages … Applies to:
all `/teacher/*` pages, and all current/future **student** / HoD / SLT / admin
dashboards."* That sentence is kept here rather than deleted, because it is the one
that caused the fork.

**Two written rules disagreed.** The 19 August 2026 student handover told Design that
student pages carry the chevron, and Design drew them that way. This file said student
dashboards take the plain white wordmark, and the then-live `student/class.html`
followed it and carried no logo. Design flagged the contradiction rather than resolving
it unilaterally: *"If Mide reads the plain-white-text rule as covering these too, it is
one component swap in the header."*

**Ruled 20 Aug 2026: the chevron stays on student surfaces.** The plain-white-wordmark
rule covers STAFF surfaces only — `/teacher/*`, `/admin/*`, `/hod/*` and school-ops
pages — because those are working instruments for adults. A student's class page is the
product.

So "dashboard" is no longer the word that decides it; **who the page is for** is. A page
for a student takes Design's mark whether or not it is shaped like a dashboard; a page
for a teacher takes the plain wordmark whether or not it is.

### ⚠️ Retired placeholders — never use on a new page

- The green octopus logo (obsolete)
- The alembic emoji `⚗️` (quick stand-in, fully retired)

If you find either on a page, that's brand drift — flag it, don't propagate it.

---

## Key Files and Folders

```
mrbadmus-site/
│
├── index.html              — Homepage (shows landing leaderboard with Champion of the Week)
├── auth.html               — Sign in / sign up page
├── profile-setup.html      — User profile wizard (collects science_pathway + tier)
├── weekly-challenge.html   — Weekly quiz challenge (subject picker only, pathway+tier from profile)
├── leaderboard.html        — Student leaderboard (Champion + 12 per-track views)
├── my-challenges.html      — Student's personal challenge history
├── past-papers.html        — Links to AQA past papers
│
├── shared/
│   ├── styles.css          — All site-wide CSS styles
│   └── mrbadmus.v2.js      — Core AI chat engine (shared by every page, SINGLE SOURCE OF TRUTH)
│
├── biology/                — Biology topic pages (auto-generated)
├── chemistry/              — Chemistry topic pages (auto-generated)
├── physics/                — Physics topic pages (auto-generated)
├── triple/                 — Triple Science pages (auto-generated)
├── combined/               — Combined Science pages (auto-generated)
│
├── build_all.py            — ⭐ THE ENTRY POINT. Runs all three generators, in the correct order.
├── generate_site_v5.py     — KS4 generator: topic pages + copies root HTML into mrbadmus_site/
├── build_ks3.py            — KS3 generator (ks3/). SEPARATE ON PURPOSE. generate_site_v5.py never builds KS3.
├── build_student.py        — student preview pages. Runs LAST.
├── ks3_art/                — one module per KS3 unit: that unit's drawers, instruments and registrations.
│                             Adding a unit = adding ONE file here. See docs/ks3/worktrees.md.
├── all_subtopics_*.py      — Python files defining subtopic content per subject/tier
│
└── mrbadmus_site/          — OUTPUT FOLDER. Cloudflare Pages serves from HERE, not from the repo root.
                               Never edit files in here directly — they get overwritten by the generator.
```

⚠️ **Critical file location rule:** Cloudflare Pages serves the site from `mrbadmus_site/`, not from the repo root. The generator copies root-level HTML files into `mrbadmus_site/` automatically. Always edit root-level files, then run the generator.

---

## The Weekly Challenge System (v3.0 — 12-track)

The quiz is split across **12 tracks**: 3 subjects × 2 pathways × 2 tiers.

- Subjects: Biology, Chemistry, Physics
- Pathways: Combined, Triple
- Tiers: Foundation, Higher

**How a student takes the quiz:**
1. They must be registered with `science_pathway` AND `tier` set in their profile
2. On weekly-challenge.html they pick ONLY the subject — pathway and tier come from their profile silently
3. Backend returns the correct quiz for their (subject, pathway, tier) combo
4. One attempt per (student, week, subject, pathway, tier) — locked at attempt time

**The leaderboard structure:**
- **Champion of the Week** at the top (hero section) — cross-all-tracks, raw score, tiebreak by time, ≥1 subject completed
- Pathway toggle (Combined / Triple)
- Tier toggle (Foundation / Higher)
- Subject tabs (Overall / Biology / Chemistry / Physics)
- Auto-lands on the student's own track

**Content scoping rules (critical):**

| Pathway + Tier | Content shown |
|---|---|
| Combined Foundation | Base only (shared AQA Combined Science content, Foundation difficulty) |
| Combined Higher | Base + Higher (NO Triple-only topics) |
| Triple Foundation | Base + Triple-only topics (Foundation difficulty) |
| Triple Higher | Everything (full AQA Triple spec, full difficulty range) |

The backend's Claude API prompt enforces this via 4-way branching in `generateWeeklyChallenge`. The frontend must never send `tier` or `pathway` as query params — the backend reads them from the authenticated user's profile.

---

## Frontend–Backend Coordination

The backend lives in a **separate repo**: `mrbadmus---backend` (three dashes) at `/Users/midebadmus/Documents/GitHub/mrbadmus---backend`.

The two repos share an API contract documented in **`API-CONTRACT.md` in the backend repo**. If you're making changes that touch API endpoints, open that file FIRST.

**Rule: frontend and backend changes that affect the API contract must be deployed together.** A breaking change pushed to only one side will cause student-visible errors. The correct deployment sequence:
1. Run any required SQL migrations in Supabase
2. Push backend repo (Render auto-deploys, wait for "Live")
3. Run `python3 build_all.py` (NOT `generate_site_v5.py` alone — that skips KS3 and the student previews)
4. Push frontend repo (Cloudflare auto-deploys)
5. Smoke test

---

## How the Site is Generated

### ⚠️ There are THREE generators, and one entry point

Run this, always:

```bash
python3 build_all.py
```

It runs, in this order:

| # | Script | Builds |
|---|---|---|
| 1 | `generate_site_v5.py` | the KS4 site — `combined/`, `triple/`, root pages, `shared/` |
| 2 | `build_ks3.py` | the KS3 site — everything under `ks3/` |
| 3 | `build_student.py` | the student preview pages |
| 4 | `build_student_port.py` | **the LIVE student pages** — `student/class.html`, `student/assignment.html` |

### ⊕ 22 Aug 2026 — the student pages are GENERATED, and are not hand-editable

`student/class.html` and `student/assignment.html` went live in commit
`e0ad28a95`. They are written by `build_student_port.py` from Design's template
and logic; the hand-written originals are retired in `docs/ks3/retired/`.

**Never hand-edit either file.** A fix typed into one survives exactly until the
next build — that is how the MRB-275 rulings were destroyed once already, and
`student_rulings.py` exists to recover from it. Instead:

| what you want to change | where it lives |
|---|---|
| Design's behaviour (a computed string, a default, a method body) | `student_rulings.py` |
| what the page renders (real data, empty states, wording from data) | `shared/student-live.js` |
| the markup itself | Design's delivery in `docs/ks3/design-reference/student/` |

⚠️ **Step 4 must run after step 1**, for the same reason step 3 does:
`generate_site_v5.build_site()` wipes `mrbadmus_site/` and `student/` is not on
its skip list.

The gates are `student_parity.py` (Design-fidelity, layers A–H at 360/390/820/
1460) and `student_behaviour.py` (30 drives, visible text identical to Design's
own file).

⊕ **Corrected 22 Aug 2026.** This used to read *"Both drive `*-fixture.html`,
never the live page"*. Only one of them does, and the difference matters:

| gate | drives | which generator wrote it |
|---|---|---|
| `student_behaviour.py` | `student/class-fixture.html` | `build_student_port.py` — the ported page, **with the rulings applied** |
| `student_parity.py` | `student/class-preview.html` | `build_student.py` — a headless-Chrome snapshot of Design's own standalone, with **no rulings applied at all** |

So `student_parity` gates the PREVIEW generator's reproduction of Design's
original file. It has no path to `student/class.html`, to
`student/class-fixture.html`, to `build_student_port.py`, to
`student_rulings.py` or to `shared/student-live.js` — its `PAIRS`,
its `COUNT_SOURCES` and `ks3_parity.ST_SWEEP_PAGES` all name the preview pair
and nothing else. ⚠️ **A change to the ported page cannot turn `student_parity`
red**, and reasoning that assumes it can — as the 22 Aug port plan did — will
plan around a gate that is not watching. `student_behaviour` is the gate that
watches the port.

The fixture must keep Design's own values even when the live page shows
different words. A ruling that changes what Design DREW belongs in `RULED_DIVERGENCE`;
a value that merely DIFFERS on real data belongs in the data seam.

**The order is load-bearing.** `generate_site_v5.build_site()` opens by wiping
`mrbadmus_site/` — everything except the foreign output trees it is told to skip
(`ks3/`, `3d/`) — so anything else emitted before it is deleted by it. KS3 is
safe in either order because it is on that skip list; the student previews are
not, which is why they run last.

**`generate_site_v5.py` does NOT build KS3.** This is the single easiest mistake
to make here, and it fails *silently in the direction that looks fine*: after a
KS3 change, running the KS4 generator alone exits 0, prints a successful build,
and leaves `ks3/` exactly as it was. A green run that did nothing. If you have
changed anything under `ks3_data/`, `ks3_art/` or `build_ks3.py`, you need
`build_all.py` or `build_ks3.py` — never `generate_site_v5.py` on its own.

They are separate on purpose: wiring KS3 into `build_site()` would rebuild 300+
KS4 pages on every KS3 content change, and would make architecture.md §9's
"zero KS4 pages changed" gate impossible to demonstrate.

### KS3 units live in `ks3_art/`, one module each

Since MRB-271, a KS3 unit's drawers, instruments and registrations live in
`ks3_art/<unit>.py` and nowhere else. Adding a unit is adding ONE new file —
the registry discovers its modules rather than listing them, so there is no
shared manifest to edit. **If you are working in a worktree, read
`docs/ks3/worktrees.md` first**: it says which lane owns which units, which
files are still genuinely shared, and how a lane merges back.

### The KS4 generator

Topic pages (e.g. `/physics/energy.html`, `/biology/bioenergetics/photosynthesis.html`) are **not written by hand** — they're produced by `generate_site_v5.py` (step 1 above).

The script reads structured data from `all_subtopics_*.py` files (topics, subtopics, equations, required practicals, higher-tier flags, triple-only flags) and outputs complete HTML files for every spec point. It also copies hand-edited root HTML files (weekly-challenge.html, leaderboard.html, etc.) into `mrbadmus_site/` which Cloudflare serves.

**If you want to edit topic content:** change the generator or the subtopic `.py` files — never edit the HTML output directly, because the generator will overwrite it.

**If you want to edit hand-written pages (weekly-challenge.html, leaderboard.html, etc.):** edit the root-level file, then run the generator so it copies into `mrbadmus_site/`.

### ⚠️ 3D Studio has a manual build step BEFORE the generator

3D Studio (`/3d`) is a Vite app in `3d-studio/`. The generator does not build it — it only **publishes** whatever build already exists, copying `3d-studio/dist/` into `mrbadmus_site/3d/`. So if you have changed anything in `3d-studio/`, the full deploy sequence is:

```bash
cd 3d-studio && npm run build && cd ..   # 1. build the studio  ← easy to forget
python3 build_all.py                     # 2. build the site and publish the studio
git add -A && git commit && git push     # 3. commit + push (authorised, see the
                                         #    Autonomy Contract) — then verify live
```

**Step 1 is only needed when `3d-studio/` has changed.** For everything else, `python3 build_all.py` on its own is the whole job.

**If you forget step 1, the generator will tell you** — it compares the build against the source and prints a large `!!!!` banner, twice, once where it happens and again as the last thing on screen. It is deliberately hard to miss, because it is otherwise invisible: the studio would simply ship as whatever it was last time.

**Why the generator does not just run `npm run build` itself:** a Node or npm problem would then be able to fail the whole site build, and KS3 and KS4 have nothing to do with the studio. The warnings are loud; neither is fatal. If there is no build at all, the generator leaves `mrbadmus_site/3d/` exactly as it is rather than deleting it, so a machine without Node can never wipe the deployed studio.

To check the isolation still holds: `python3 3d_isolation_check.py`.

---

## Question pool ownership — a named contract (MRB-288, ruled by Mide 24 Aug 2026)

Three KS3 question pools. **One per surface. No surface SERVES questions from a
pool it does not own. Ever.** The `pool_ownership` gate fails the build on a
violation; the `one_pool_per_assignment` CHECK (migration `20260824214711`)
refuses the seam at the database.

| Surface | Owner pool | Where the serving read lives |
|---|---|---|
| Lesson-page ladder (recall/apply/explain/produce) | the authored ladder in `ks3_data` — baked into the page by `build_ks3.py`; `ks3_ladder_questions` is its DB mirror | no runtime pool read at all |
| Weekly assignment | **`ks3_assignment_bank`** (renamed from `ks3_bank_questions`, 24 Aug 2026 — the generic name invited the mixing) | backend composition only: `server.js` `bankFor()` → `/api/class/current-assignment` |
| Dashboard flashcards | `ks3_cards` | `shared/student-live.js`, one serving read |

**FROZEN EXCEPTION (awaiting Mide's ruling):** the class page's **practice
round** (renamed from "recall" — MRB-288 kills that collision; "recall" now
only ever names a ladder rung) serves scored MCQs, and the only pool holding
scored MCQs is the ladder mirror. Its ruled owner pool (`ks3_cards`) holds
front/back flashcards and cannot supply a round. Frozen exactly as it reads:
one serving read of `ks3_ladder_questions` in `shared/student-live.js` plus
`/api/class/practice` on the backend, both named and bounded in the gate.

**Serving ≠ resolving ≠ weighting.** Resolving an `assignment_questions.source_ref`
to a lesson slug, and reading attempt history (`question_ref` + `is_correct`)
to weight practice toward weaknesses (FROM YOUR WORK), are both intended and
both survive — the contract governs where questions are SERVED from, nothing
else.

## How the AI Chat Backend Works

Every topic page embeds a chat panel powered by `shared/mrbadmus.v2.js`. When a student sends a message:

1. JavaScript builds a system prompt telling the AI it's "Mr Badmus AI — an expert AQA GCSE Science teacher", including current subject context and detailed AQA spec content
2. Sends to: `POST https://mrbadmus-backend.onrender.com/api/chat`
3. Backend forwards to Claude API
4. Response comes back as `data.content[].text`
5. Displayed and appended to `chatHistory` (capped at 20 messages)

The AI is instructed to always use the **FIFA method** for calculations (Formula → Insert → Fix → Answer), always include units, use encouraging language, label Higher Tier (⭐) and Triple-only (🔬) content clearly, and answer across all three sciences regardless of the current page.

If the backend is unreachable, the chat falls back to a static message.

---

## Known Conventions and Gotchas

- **No build tools.** No npm, no webpack, no bundler. Everything runs as plain files in the browser.
- **Class naming convention** (MRB-263, ruled by Mide 19 Aug 2026): year number,
  lowercase band letter, slash, subject code with a single capital, set number —
  `7h/Sc5`, `10h/Ph1`, `11r/Sc1`. The 2026-27 timetable classes already follow it;
  the 2025-26 leftovers `10R1` and `10H/Ph1` were renamed in place to match.
  ⚠️ **`classes.name` is not purely cosmetic.** Nothing joins on it, but
  `supabase/functions/roster-import/index.ts` find-or-creates a class by exact
  `(school_id, academic_year_id, name)` match, so renaming a class outside the app
  and then re-importing a CSV that still carries the old name creates a SECOND
  class rather than finding the existing one. Rename the CSV too, or don't
  re-import a year you have renamed into.
- **A class belongs to an academic year, and every class list must say so**
  (MRB-261). Never scope a class list on `academic_years.is_current` — that flag
  is moved by hand on 1 September, so through late August it still points at the
  year that finished in July. Use the `workingAcademicYear()` helper.
  A plain `end_date >= today` is also wrong: academic
  years run to 31 August, so through the summer two years are both unfinished.
  The helper resolves that with a 30-day LOOKAHEAD — the earliest year whose
  `end_date` is still ahead of today+30 — falling back to the latest year if
  none qualifies.
  ⊕ **Superseded 21 Aug 2026.** This used to read *"the `workingAcademicYear()`
  helper (three hand-synced copies: `shared/class-entry.js`,
  `shared/student-data.js`, `shared/teacher-data.js`)"*. MRB-267 consolidated
  them on 19 Aug 2026: there is now exactly ONE implementation, in
  **`shared/class-entry.js`**, and the copies in `student-data.js` and
  `teacher-data.js` are delegating shims that throw a named error if
  `class-entry.js` has not been loaded onto the page first. The superseded
  sentence is kept rather than deleted because it is an instruction to go and
  hand-sync three files, and doing that would reintroduce precisely the drift
  MRB-267 removed. ⚠️ Load order is now load-bearing: `class-entry.js` must come
  before `student-data.js` / `teacher-data.js` on any page that uses either.
- **Shared JS via `window.MrBadmus`.** The chat engine exposes itself as a global so any page can call `MrBadmus.init(...)`.
- **Supabase auth is client-side.** Sessions in `localStorage` under `sb-urklkrwevjtlfbwnipjn-auth-token`. Supabase JS SDK loaded via CDN — no import system.
- **Inline auth-check scripts.** Each HTML page has a small inline `<script>` at the top of `<nav>` that swaps Sign In / Sign Up for the logged-in user's name + avatar.
- **Color-coded subjects:** Physics teal (`#4ECDC4`), Chemistry pastel pink (`#FFD2E6`), Biology green (`#6BCB77`)
- **Pathway colours:** Combined teal (same as Physics), Triple pastel pink (same as Chemistry)
- **`--chemistry` vs `--danger` split** (MRB-46 Phase 3 v3, 2026-05-25):
  Chemistry used to be `#FF6B6B` red, which was being conflated with
  "warning" UI semantics (overdue tones, error text, delete-X hover).
  Swapped Chemistry to pastel pink `#FFD2E6`; introduced a paired
  `--danger: #FF6B6B` token for destructive UI. **For NEW code: use
  `var(--chemistry)` only for chemistry-subject identity; use
  `var(--danger)` for everything red-as-warning** (overdue, missed,
  error states, destructive button hovers). Existing files outside
  `student/class.html` still route destructive UI through
  `var(--chemistry)` — that's a known limitation, not a desired
  state. Route to `var(--danger)` when you next touch each surface.
- **Tier colours:** Foundation green, Higher yellow (`#FFD93D`)
- **Backend URL is hardcoded** as `https://mrbadmus-backend.onrender.com` in `mrbadmus.v2.js`. No environment variables on the frontend (no build step).
- **Supabase anon key is hardcoded** in pages that need it (e.g. leaderboard.html for profile reads). Anon keys are designed to be public — safe to commit.
- **Cloudflare `_redirects` proxy is broken** — all API calls point directly at the Render URL, not through the frontend domain.

---

## Supabase migrations toolchain

Established by MRB-84 (2026-05-24). Future migration work follows this pattern.

### Folder taxonomy

Four sibling folders under `supabase/`, each with a `README.md`. The Supabase CLI only reads `migrations/`; the other three are invisible to `supabase db push` and `supabase migration list`.

- **`supabase/migrations/`** — forward migrations. Files named `YYYYMMDDHHMMSS_description.sql` where the timestamp matches the `schema_migrations.version` they register as. CLI parses the version from the filename.
- **`supabase/rollbacks/`** — manual undo SQL for specific migrations. Apply manually only. Files keep the original `NNNN_` sequence prefix (CLI never reads them).
- **`supabase/baselines/`** — bootstrap/recovery SQL (recreate from scratch, disaster recovery). Apply manually only.
- **`supabase/seeds/`** — test-only fixture SQL (fake users, fake submissions). Never applied on prod via CLI; manual psql only against test.

### Apply path

- **Primary:** `supabase db push` against a linked project. Faster and more durable than the MCP, and produces a clean local migration file as part of the workflow. Use this for all routine forward migrations from MRB-46 Phase 2 onward.
- **Fallback:** MCP `apply_migration` for one-off ad-hoc SQL where a checked-in migration file isn't warranted (e.g. emergency hotfix). MCP auth is fragile — tokens expire, `remove` + `add` cycles wipe the token. Use sparingly.

### Auth setup for the CLI

The CLI's OAuth flow stores its token in macOS Keychain, which isn't accessible to Claude Code's Bash tool (non-interactive shell can't unlock the keychain). Use a Personal Access Token instead, stashed in a tmp file:

```bash
read -rs SUPABASE_ACCESS_TOKEN
printf '%s' "$SUPABASE_ACCESS_TOKEN" > /tmp/sb_token && chmod 600 /tmp/sb_token
unset SUPABASE_ACCESS_TOKEN
```

Then prefix CLI commands with `SUPABASE_ACCESS_TOKEN="$(cat /tmp/sb_token)"`. DB password follows the same pattern (`/tmp/sb_pw`). Clean both up at end of session. Generate the PAT from `supabase.com/dashboard/account/tokens`.

### Other Supabase-related operational notes

- `supabase-test` MCP stays permanently write-enabled. Never swap its `read_only` URL flag — project-scope (`project_ref=qeppkiswvclkkwbxmlok`) is the actual safeguard; toggling `read_only` costs an OAuth re-auth per swap.
- Production project ref: `urklkrwevjtlfbwnipjn`. Test project ref: `qeppkiswvclkkwbxmlok`. Never confuse them; the test project is the safe sandbox.
- Pooler maintenance for `eu-west-1` on 2026-06-01 14:00 UTC. Test DB is in this region. During the window, expect intermittent failures via the session pooler (`aws-0-eu-west-1.pooler.supabase.com:5432`). Avoid migration apply or DB verification work during the window.

---

## Working with Mide

Mide is a teacher and creative founder, not a developer. Keep this in mind at all times:

- **Always explain what you're about to do before doing it.** Never make a change silently.
- **Explain technical things in plain English.** Avoid jargon. If a technical term is necessary, define it in the same sentence.
- **Investigate before changing.** Read the code first. Don't guess at schemas or file structures. Ask "are you sure that's everything?" before multi-file changes. Ask "what could go wrong?" before structural changes.
- **Show before/after diffs before editing.** Mide must understand the why before approving.
- **One change at a time.** Strict scope discipline — slow and thorough beats fast and patchy.
- **Prefer small, reversible changes over big rewrites.**
- **When suggesting terminal commands, always explain what each one does** — not just what to type, but what will happen when it runs.
- **Flag anything that could break the live site** before proceeding. 135+ students rely on this site.
- **You push, from the Terminal.** ⊕ Superseded 16 Aug 2026 (MRB-228) — this line used to read
  "Never `git push` in Terminal; Mide uses GitHub Desktop exclusively". Push authorisation is now
  standing and permanent; see the Autonomy Contract at the top of this file. Mide may still use
  GitHub Desktop when he wants to; that is a preference of his, not a restriction on you.
- **For Supabase admin tasks**, give Mide direct SQL to paste into the Supabase SQL Editor. Never try to migrate schemas from code.

---

## Working pattern (how Mide and Claude operate)

Captured 12 May 2026 mid-way through MRB-38 build. This is how Mide
and chat-Claude have been operating across the schools layer rollout.
Future-Mide and future-Claude (and any new collaborator) should keep
to this.

**1. Three-way workflow with clear lanes.** Mide directs (product,
scope, priorities). Chat-Claude architects (plans, writes prompts,
gates between phases, plain-English translator). Claude Code executes
(queries, code, file edits, Linear writes). Each lane does what it's
best at. None of us tries to do the others' jobs.

**2. Investigate before editing.** Read the current state first. No
"I'll just change this" without recon. Diffs shown before approval.
The work moves faster long-term because we don't waste time undoing
wrong assumptions.

**3. Gate-driven phases.** Big tasks split into sub-phases. Each
phase has an explicit gate where chat-Claude pauses for Mide's
approval. No barrelling through. Catches divergence early when it's
cheap to fix.

**4. "What could go wrong?" before structural changes.** Standard
pre-flight check before any migration, refactor, or scope change.
Catches edge cases that would otherwise become Phase 6 bugs.

**5. "Are you sure that's everything?" before approving multi-file
changes.** Specifically catches scope-creep in batches.

**6. Linear is source of truth.** Every decision, gotcha, deferred
item gets pinned. No "remind me why we did this" 6 weeks later.
Comments on the right ticket so context lives with the work.

**7. New scope goes in new tickets or comments, never folded silently
into the current ticket.** Avatar bank → MRB-55. Multi-attempts →
comment on Stage 4 ticket. Brand drift → MRB-54. The thing in front
of us stays the thing in front of us.

**8. Production-touching work uses the MCP swap dance.** Both
Supabase MCPs (prod + test) are never live simultaneously.
`claude mcp remove supabase-test` before any prod step, re-add after.

**9. You push, one unit at a time.** ⊕ Superseded 16 Aug 2026 (MRB-228) —
this item used to read "Never `git push` from terminal. GitHub Desktop
only. Always." Push authorisation is now standing and permanent. The
discipline that replaces it is one unit = one commit = one push =
verify live, so that an interrupted session leaves shipped work
shipped rather than a long uncommitted tree.

**10. Mide manages his own schedule.** Chat-Claude does not project
fatigue or advise breaks unless Mide explicitly raises it. Speed of
ideation→execution is the priority.

**11. Supabase tooling discipline.** Hard-won from MRB-46 Phase 1
(24 May 2026) after ~2 hours of MCP auth churn. Apply paths, folder
taxonomy, CLI auth pattern, and operational notes (test/prod refs,
pooler maintenance, `supabase-test` MCP write-enabled rationale)
live in the "Supabase migrations toolchain" section above. With
MRB-84 landed, the CLI (`supabase db push`) is the primary apply
path; MCP `apply_migration` is the one-off ad-hoc fallback. The
swap-dance in item 8 above applies only when explicitly switching
to prod, not for read/write toggles within test. Gotchas observed
in the wild:

- **RLS soft-delete gotcha.** If a SELECT policy filters by a column
  the UPDATE will set (e.g. `deleted_at IS NULL`), the UPDATE fails
  with `42501: new row violates row-level security policy` even when
  the UPDATE policy passes. Postgres applies SELECT USING to the
  post-update row state to prevent information-leak via update-into-
  invisibility. Fix: widen the SELECT policy to cover the legitimate
  post-update state (e.g. allow author to see their own deleted rows),
  or use a SECURITY DEFINER function. The frontend can continue
  filtering defensively — UX stays the same. Discovered in MRB-46
  Phase 2 when wiring author-only soft-delete on `class_shoutouts`;
  fix lives in migration `20260524195500_fix_class_shoutouts_soft_delete.sql`.

Mide's stated principle: "Slow and thorough beats fast and patchy" —
applied to *correctness*, not pace. Ideation cycles stay short;
verification stays rigorous.

---

## Known Deferred Items

Small things to tighten when you're next in the relevant area — not urgent, not blockers:

1. **`auth.html` redirect check:** currently only checks `science_pathway`, not `tier`. A user with `tier=null` slips past the redirect and only hits the backend's 400 on the weekly-challenge page. Fix when next editing auth.html: check both fields.

2. **`profile-setup.html` edit mode:** the Save button in edit mode bypasses step 2 validation. Safe today because existing profiles have pathway/tier pre-filled, but add a finish() guard when next editing profile-setup.

3. **`/api/weekly-leaderboard/landing` champion:** doesn't include `subjects_done`, unlike `/api/weekly-leaderboard/champion`. The landing page hardcodes "all 3 subjects" in the display copy — slightly inaccurate if the champion only did 1–2 subjects. Tighten when next touching the landing section of index.html.

---

## Supabase Schema (key tables)

- `profiles` — user data. Key columns: `id`, `first_name`, `school_name`, `avatar_url`, **`science_pathway`** (values: `combined` / `triple`), **`tier`** (values: `foundation` / `higher`)
- `weekly_challenges` — generated quizzes. Unique constraint: `(week_start, subject, pathway, tier)`. **Note: profile column is `science_pathway`, but here it's just `pathway`.**
- `weekly_scores` — student attempts. Stores pathway, tier, subject, score, max_score, time_taken. `pathway` is locked at attempt time (copied from the challenge row, not from profile).

⚠️ **Schema naming gotcha:** the profile table uses `science_pathway`, but `weekly_challenges` and `weekly_scores` use just `pathway`. Don't confuse them in queries.
## How to work (commander, executor, scout)

You are the commander. Hand work off instead of doing it yourself:
- Reads, searches, "where is X" -> the scout.
- Content authoring, porting, any file edits -> the executor.
- You keep your focus for planning and judgement.

Act, do not ask. Only stop for Mide on: anything touching the live site,
anything that cannot be undone, a real product or scope decision, and the
merge decision. Everything else, just do it and say what you did.

You push. ⊕ Superseded 16 Aug 2026 (MRB-228) — this line used to read "Never git
push. Mide pushes via GitHub Desktop." Push authorisation is standing and
permanent: one unit is one commit and one push, then verify live. One session
still works one worktree.